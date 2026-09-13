// 4,500見出し語への拡張(+1,500語)の作業用ツール。中断しても再開できる。
//   npm run vocab4500 prepare      Oxford C1帯 + 追加リスト + CMUdict発音 → vocab4500-meta.tsv
//   npm run vocab4500 status [n]   例文が未作成の語を先頭 n 件だけ TSV で出力
//   npm run vocab4500 check        執筆済みの行だけを検査する
//   npm run vocab4500 build        meta + 執筆済み本文 → src/content/vocabulary/extended.ts
//
// 執筆する本文は scripts/vocab4500-content.tsv (追記のみ)。列は
//   word / meaningsJa(、区切り) / exampleSentence / exampleTranslationJa /
//   collocations(|区切り・空可) / mnemonic
// レベル・品詞・IPA は meta 側に持つので本文側では書かない。
import { existsSync, readFileSync, writeFileSync } from 'node:fs'

const root = new URL('../', import.meta.url)
const metaPath = new URL('scripts/vocab4500-meta.tsv', root)
const extrasPath = new URL('scripts/vocab4500-extras.tsv', root)
const contentPath = new URL('scripts/vocab4500-content.tsv', root)
const outputPath = new URL('src/content/vocabulary/extended.ts', root)

const [mode, arg] = process.argv.slice(2)

async function main() {
  if (mode === 'prepare') await prepare(arg ?? '/tmp/oxford-5000.csv', process.argv[4] ?? '/tmp/cmudict.dict')
  else if (mode === 'status') status(Number(arg) || 40)
  else if (mode === 'check') checkWritten()
  else if (mode === 'build') await build()
  else {
    console.error('usage: vocab4500 prepare [oxford.csv] [cmudict.dict] | status [n] | check | build')
    process.exit(1)
  }
}

// 既収録の見出し語と id が衝突するため外す語。set up(句動詞)と set-up(名詞)は id が同じになる。
const excluded = new Set(['set-up'])

/** Oxford 5000 の C1帯(既収録を除く)と追加リストを結合し、CMUdict の発音を付けた台帳を作る。 */
async function prepare(oxfordPath, cmudictPath) {
  // 「既収録」は拡張分を除いた 3,000語。extended.ts を取り込んだ後でも prepare を再実行できるようにする。
  const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
  const { extendedVocabulary } = await import('../src/content/vocabulary/extended.ts')
  const added = new Set(extendedVocabulary.map((entry) => entry.word.toLowerCase()))
  const existing = new Set(
    allVocabulary.map((entry) => entry.word.toLowerCase()).filter((word) => !added.has(word)),
  )

  const targets = new Map()
  for (const line of readFileSync(oxfordPath, 'utf8').split(/\r?\n/).slice(1)) {
    const [rawWord, level, , , rawClass] = line.split(';')
    const word = normalize(rawWord)
    if (!word || level !== 'c1' || existing.has(word) || excluded.has(word)) continue
    // C1帯は B2到達に必要な受容語彙として採り、アプリ内は B2 として提示する。
    const target = targets.get(word) ?? { word, level: 'B2', partOfSpeech: '' }
    const partOfSpeech = mapPartOfSpeech(rawClass)
    if (!target.partOfSpeech.split('・').includes(partOfSpeech)) {
      target.partOfSpeech = target.partOfSpeech ? `${target.partOfSpeech}・${partOfSpeech}` : partOfSpeech
    }
    targets.set(word, target)
  }

  for (const line of readFileSync(extrasPath, 'utf8').split(/\r?\n/)) {
    const [rawWord, level, partOfSpeech] = line.split('\t')
    const word = normalize(rawWord)
    if (!word || !level) continue
    if (existing.has(word)) throw new Error(`追加リストが既存語と重複: ${word}`)
    if (targets.has(word)) throw new Error(`追加リストが Oxford C1 と重複: ${word}`)
    targets.set(word, { word, level, partOfSpeech })
  }

  const cmudict = readCmudict(cmudictPath)
  const rows = []
  const missing = []
  for (const target of targets.values()) {
    const pronunciation = lookupPronunciation(target.word, cmudict)
    if (!pronunciation) missing.push(target.word)
    rows.push([target.word, target.level, target.partOfSpeech, pronunciation ?? ''].join('\t'))
  }

  writeFileSync(metaPath, `${rows.join('\n')}\n`)
  console.error(`台帳 ${rows.length} 語を書き出しました。発音が引けなかった語: ${missing.length}`)
  if (missing.length > 0) console.error(missing.join(', '))
}

/** 本文がまだ書かれていない語を、台帳の順で返す。 */
function status(limit) {
  const meta = readMeta()
  const written = new Set(readContent().keys())
  const pending = [...meta.values()].filter((entry) => !written.has(entry.word))
  console.error(`${meta.size - pending.length}/${meta.size} 完了 / 残り ${pending.length}`)
  for (const entry of pending.slice(0, limit)) {
    console.log([entry.word, entry.level, entry.partOfSpeech].join('\t'))
  }
}

/** 執筆済みの行だけを検査する(全件そろう前でも使える)。 */
function checkWritten() {
  const meta = readMeta()
  const content = readContent()
  const problems = [...content.values()].flatMap((body) =>
    meta.has(body.word) ? check(meta.get(body.word), body) : [`${body.word}: 台帳にない語です`],
  )
  console.error(problems.length === 0 ? `${content.size} 語すべて問題なし` : problems.join('\n'))
  if (problems.length > 0) process.exit(1)
}

async function build() {
  const meta = readMeta()
  const content = readContent()
  const unknown = [...content.keys()].filter((word) => !meta.has(word))
  if (unknown.length > 0) throw new Error(`台帳にない語: ${unknown.join(', ')}`)
  const pending = [...meta.keys()].filter((word) => !content.has(word))
  if (pending.length > 0) throw new Error(`本文が未作成の語が ${pending.length} 件あります: ${pending.slice(0, 10).join(', ')}`)

  const problems = [...meta.values()].flatMap((entry) => check(entry, content.get(entry.word)))
  if (problems.length > 0) {
    console.error(problems.join('\n'))
    throw new Error(`本文の検査で ${problems.length} 件の問題があります`)
  }

  const rows = [...meta.values()].map((entry) => {
    const body = content.get(entry.word)
    return [
      entry.word,
      entry.level,
      entry.partOfSpeech,
      body.meaningsJa,
      entry.pronunciation,
      body.exampleSentence,
      body.exampleTranslationJa,
      body.collocations.length > 0 ? body.collocations : null,
      body.mnemonic,
    ]
  })

  const source =
    `// このファイルは scripts/vocab4500.mjs で生成する(手で編集しない)。\n` +
    `// 3,000語から4,500語へ拡張した分。Oxford 5000 の C1帯を B2到達に必要な受容語彙として採り、\n` +
    `// 高頻度句動詞・定型表現・派生語を加えた。例文・和訳・コロケーション・覚えるヒントは本プロジェクトの自作。\n` +
    `import type { VocabularyEntry } from '../types'\n\n` +
    `type ExtendedRow = [\n` +
    `  word: string,\n` +
    `  level: 'A2' | 'B1' | 'B2',\n` +
    `  partOfSpeech: string,\n` +
    `  meaningsJa: string[],\n` +
    `  pronunciation: string,\n` +
    `  exampleSentence: string,\n` +
    `  exampleTranslationJa: string,\n` +
    `  collocations: string[] | null,\n` +
    `  mnemonic: string,\n` +
    `]\n\n` +
    `const rows: ExtendedRow[] = ${JSON.stringify(rows, null, 2)}\n\n` +
    `export const extendedVocabulary: VocabularyEntry[] = rows.map((row) => ({\n` +
    `  id: row[0],\n` +
    `  word: row[0],\n` +
    `  level: row[1],\n` +
    `  partOfSpeech: row[2],\n` +
    `  meaningsJa: row[3],\n` +
    `  pronunciation: row[4],\n` +
    `  exampleSentence: row[5],\n` +
    `  exampleTranslationJa: row[6],\n` +
    `  ...(row[7] ? { collocations: row[7] } : {}),\n` +
    `  mnemonic: row[8],\n` +
    `}))\n`

  writeFileSync(outputPath, source)
  console.error(`${rows.length} 語を ${outputPath.pathname} に書き出しました。`)
}

/** 取り込み前の本文検査。content.test.ts と同じ規則を先に全件まとめて出す。 */
function check(entry, body) {
  const problems = []
  const at = entry.word
  if (!entry.pronunciation) problems.push(`${at}: 発音がありません`)
  if (body.meaningsJa.length === 0) problems.push(`${at}: 語義がありません`)
  if (body.exampleTranslationJa.length < 4) problems.push(`${at}: 和訳が短すぎます`)
  if ([...body.mnemonic].length < 20) problems.push(`${at}: 覚えるヒントが短すぎます`)
  for (const character of ['(', ')', '[', ']', '_', '*', '#', '/']) {
    if (body.exampleSentence.includes(character)) problems.push(`${at}: 例文に ${character} が含まれています`)
  }
  if (!/[.!?]$/.test(body.exampleSentence)) problems.push(`${at}: 例文の文末に句読点がありません`)
  const wordCount = body.exampleSentence.split(/\s+/).filter(Boolean).length
  if (wordCount < 6 || wordCount > 22) problems.push(`${at}: 例文が ${wordCount}語です`)
  // content.test.ts と同じ、語幹の前方一致で見出し語の使用を確かめる
  const head = entry.word.toLowerCase().split(' ')[0]
  const stem = head.slice(0, Math.max(3, head.length - 3))
  if (!body.exampleSentence.toLowerCase().includes(stem)) problems.push(`${at}: 例文が見出し語を含みません`)
  return problems
}

function readMeta() {
  const meta = new Map()
  for (const line of readFileSync(metaPath, 'utf8').split(/\r?\n/)) {
    const [word, level, partOfSpeech, pronunciation] = line.split('\t')
    if (!word) continue
    meta.set(word, { word, level, partOfSpeech, pronunciation })
  }
  return meta
}

function readContent() {
  const content = new Map()
  if (!existsSync(contentPath)) return content
  for (const [index, line] of readFileSync(contentPath, 'utf8').split(/\r?\n/).entries()) {
    if (!line.trim() || line.startsWith('#')) continue
    const [word, meanings, sentence, translation, collocations = '', mnemonic = ''] = line.split('\t')
    const at = `${contentPath.pathname}:${index + 1}`
    if (!word || !meanings || !sentence || !translation || !mnemonic) throw new Error(`${at}: 列が足りません`)
    if (content.has(word)) throw new Error(`${at}: ${word} が重複しています`)
    content.set(word, {
      word,
      meaningsJa: meanings.split('、').map((value) => value.trim()).filter(Boolean),
      exampleSentence: sentence.trim(),
      exampleTranslationJa: translation.trim(),
      collocations: collocations.split('|').map((value) => value.trim()).filter(Boolean),
      mnemonic: mnemonic.trim(),
    })
  }
  return content
}

function readCmudict(path) {
  const raw = new Map()
  for (const line of readFileSync(path, 'utf8').split(/\r?\n/)) {
    if (!line || line.startsWith(';;;')) continue
    const separator = line.indexOf(' ')
    if (separator < 1) continue
    const key = line.slice(0, separator).toLowerCase().replace(/\(\d+\)$/, '')
    if (!raw.has(key)) raw.set(key, line.slice(separator + 1).trim().split(/\s+/))
  }
  return raw
}

// 英綴りは CMUdict にないため、米綴りに寄せて引く(表示する語は英綴りのまま)。
const cmudictAliases = {
  councillor: 'councilor',
  counselling: 'counseling',
  enrol: 'enroll',
  favourable: 'favorable',
  sceptical: 'skeptical',
}

function lookupPronunciation(rawWord, cmudict) {
  const word = cmudictAliases[rawWord] ?? rawWord
  const parts = word.split(/[ ]+/)
  const phonemes = parts.map((part) => cmudict.get(part) ?? cmudict.get(part.replace(/-/g, '')))
  if (!phonemes.every(Boolean)) {
    // ハイフン語は構成語に分けて引き直す(decision-making → decision + making)
    const pieces = word.split(/[ -]+/).map((part) => cmudict.get(part))
    if (!pieces.every(Boolean)) return null
    return `/${pieces.map(arpaToIpa).join(' ')}/`
  }
  return `/${phonemes.map(arpaToIpa).join(' ')}/`
}

// ARPABET → IPA。scripts/prepare-vocabulary-expansion.mjs と同じ規則。
function arpaToIpa(phonemes) {
  const tokens = phonemes.map((phoneme) => {
    const match = phoneme.match(/^([A-Z]+)([012])?$/)
    const base = match?.[1] ?? phoneme
    const stress = match?.[2] ?? ''
    let ipa = arpaMap[base] ?? base.toLowerCase()
    if (base === 'AH') ipa = stress === '0' ? 'ə' : 'ʌ'
    if (base === 'ER') ipa = stress === '0' ? 'ɚ' : 'ɝ'
    return { ipa, stress, vowel: vowelPhonemes.has(base) }
  })

  const marks = new Map()
  let previousVowel = -1
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index]
    if (!token.vowel) continue
    const vowelCount = tokens.filter((item) => item.vowel).length
    if (token.stress === '1' && vowelCount > 1) {
      const clusterStart = previousVowel + 1
      const cluster = tokens.slice(clusterStart, index).map((item) => item.ipa).join('')
      const onsetStart = validOnsets.has(cluster) ? clusterStart : Math.max(clusterStart, index - 1)
      marks.set(onsetStart, 'ˈ')
    }
    previousVowel = index
  }

  return tokens.map((token, index) => `${marks.get(index) ?? ''}${token.ipa}`).join('')
}

function mapPartOfSpeech(value = '') {
  const normalized = value.trim().toLowerCase()
  if (normalized.includes('phrasal verb')) return '句動詞'
  if (normalized.includes('noun')) return '名詞'
  if (normalized.includes('adjective')) return '形容詞'
  if (normalized.includes('adverb')) return '副詞'
  if (normalized.includes('verb')) return '動詞'
  if (normalized.includes('preposition')) return '前置詞'
  if (normalized.includes('conjunction')) return '接続詞'
  if (normalized.includes('pronoun')) return '代名詞'
  if (normalized.includes('determiner')) return '限定詞'
  if (normalized.includes('exclamation')) return '間投詞'
  if (normalized.includes('number')) return '数詞'
  return 'その他'
}

function normalize(word) {
  return (word ?? '').trim().toLowerCase().replace(/\s+/g, ' ')
}

const vowelPhonemes = new Set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'])
const validOnsets = new Set(['', 'b', 'd', 'f', 'g', 'h', 'dʒ', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ʃ', 't', 'tʃ', 'θ', 'v', 'w', 'j', 'z', 'ð', 'ŋ', 'bl', 'br', 'dr', 'fl', 'fr', 'gl', 'gr', 'kl', 'kr', 'pl', 'pr', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tr', 'θr', 'ʃr', 'spl', 'spr', 'str', 'skr', 'skw'])
const arpaMap = {
  AA: 'ɑ', AE: 'æ', AH: 'ʌ', AO: 'ɔ', AW: 'aʊ', AY: 'aɪ', EH: 'ɛ', ER: 'ɝ', EY: 'eɪ',
  IH: 'ɪ', IY: 'i', OW: 'oʊ', OY: 'ɔɪ', UH: 'ʊ', UW: 'u', B: 'b', CH: 'tʃ', D: 'd',
  DH: 'ð', F: 'f', G: 'g', HH: 'h', JH: 'dʒ', K: 'k', L: 'l', M: 'm', N: 'n', NG: 'ŋ',
  P: 'p', R: 'r', S: 's', SH: 'ʃ', T: 't', TH: 'θ', V: 'v', W: 'w', Y: 'j', Z: 'z', ZH: 'ʒ',
}

await main()
