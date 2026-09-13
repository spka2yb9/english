import { readFileSync, readdirSync, writeFileSync } from 'node:fs'

const root = new URL('../', import.meta.url)
const vocabularyDirectory = new URL('../src/content/vocabulary/', import.meta.url)
const oxfordPath = process.argv[2] ?? '/tmp/oxford-5000.csv'
const ejdictDirectory = process.argv[3] ?? '/tmp/english-vocab-sources-3000/EJDict-master/src'
const sentencePath = process.argv[4] ?? '/tmp/english-vocab-sources-3000/jpn.txt'
const outputPath = process.argv[5] ?? '/tmp/vocabulary-expansion.json'
const cmudictPath = process.argv[6] ?? '/tmp/cmudict.dict'

let candidates = []

function main() {
  const existingWords = readExistingWords()
  candidates = readOxfordCandidates().filter((candidate) => !existingWords.has(candidate.key))
  const definitions = readEjdict()
  const examples = findReferenceExamples(candidates)
  const pronunciations = readCmudict()

  const entries = candidates.map((candidate) => ({
    ...candidate,
    pronunciation: pronunciations.get(candidate.key) ?? candidate.pronunciation,
    meaningCandidates: getDefinitionCandidates(candidate, definitions),
    referenceExample: examples.get(candidate.key) ?? null,
  }))

  const missingMeanings = entries.filter((entry) => entry.meaningCandidates.length === 0)
  const missingExamples = entries.filter((entry) => !entry.referenceExample)
  const byLevel = Object.groupBy(entries, (entry) => entry.level.toLowerCase())
  const byPartOfSpeech = Object.groupBy(entries, (entry) => entry.partOfSpeech)

  writeFileSync(outputPath, `${JSON.stringify(entries, null, 2)}\n`)
  console.log(
    JSON.stringify(
      {
        entries: entries.length,
        byLevel: Object.fromEntries(Object.entries(byLevel).map(([key, value]) => [key, value.length])),
        byPartOfSpeech: Object.fromEntries(
          Object.entries(byPartOfSpeech)
            .map(([key, value]) => [key, value.length])
            .sort((left, right) => right[1] - left[1]),
        ),
        missingMeanings: missingMeanings.length,
        missingMeaningWords: missingMeanings.slice(0, 50).map((entry) => entry.word),
        missingReferenceExamples: missingExamples.length,
        outputPath,
      },
      null,
      2,
    ),
  )
}

function readExistingWords() {
  const words = new Set()
  for (const file of readdirSync(vocabularyDirectory).filter((name) => /^batch\d+\.ts$/.test(name))) {
    const source = readFileSync(new URL(file, vocabularyDirectory), 'utf8')
    for (const match of source.matchAll(/\bword:\s*(['"])(.*?)\1/g)) {
      words.add(normalizeWord(match[2]))
    }
  }
  return words
}

function readOxfordCandidates() {
  const rank = new Map([
    ['a2', 0],
    ['b1', 1],
    ['b2', 2],
  ])
  const candidatesByWord = new Map()

  for (const line of readFileSync(oxfordPath, 'utf8').split(/\r?\n/).slice(1)) {
    const [rawWord, rawLevel, transcription, , rawClass] = line.split(';')
    const key = normalizeWord(rawWord)
    if (!key || !rank.has(rawLevel)) continue

    const level = rawLevel.toUpperCase()
    const candidate = candidatesByWord.get(key)
    if (!candidate) {
      candidatesByWord.set(key, {
        key,
        word: rawWord.trim(),
        level,
        partOfSpeech: mapPartOfSpeech(rawClass),
        pronunciation: cleanOxfordPronunciation(transcription),
      })
      continue
    }

    if (rank.get(rawLevel) < rank.get(candidate.level.toLowerCase())) candidate.level = level
    const partOfSpeech = mapPartOfSpeech(rawClass)
    if (!candidate.partOfSpeech.split('・').includes(partOfSpeech)) {
      candidate.partOfSpeech += `・${partOfSpeech}`
    }
  }

  return [...candidatesByWord.values()]
}

function readEjdict() {
  const entries = new Map()
  for (const file of readdirSync(ejdictDirectory).filter((name) => /^[a-z]\.txt$/.test(name))) {
    for (const line of readFileSync(`${ejdictDirectory}/${file}`, 'utf8').split(/\r?\n/)) {
      const tab = line.indexOf('\t')
      if (tab < 1) continue
      const headwords = line.slice(0, tab).split(/,\s*/)
      const definition = line.slice(tab + 1).trim()
      for (const headword of headwords) {
        const key = normalizeWord(headword)
        if (!key) continue
        const current = entries.get(key) ?? { exactLower: '', fallback: '' }
        if (!current.fallback) current.fallback = definition
        if (headword.trim() === key && !current.exactLower) current.exactLower = definition
        entries.set(key, current)
      }
    }
  }
  return entries
}

function findReferenceExamples(targets) {
  const byFirstToken = new Map()
  for (const target of targets) {
    target.forms = buildForms(target)
    for (const form of target.forms) {
      const firstToken = form.match(/[a-z]+/)?.[0]
      if (!firstToken) continue
      const bucket = byFirstToken.get(firstToken) ?? []
      if (!bucket.includes(target)) bucket.push(target)
      byFirstToken.set(firstToken, bucket)
    }
  }

  const best = new Map()
  for (const line of readFileSync(sentencePath, 'utf8').split(/\r?\n/)) {
    const [english, japanese, attribution = ''] = line.split('\t')
    if (!english || !japanese || !isUsableSentence(english, japanese)) continue
    const lower = english.toLowerCase()
    const tokens = new Set(lower.match(/[a-z]+(?:'[a-z]+)?/g) ?? [])

    for (const token of tokens) {
      const bucket = byFirstToken.get(token)
      if (!bucket) continue
      for (const target of bucket) {
        const matchedForm = target.forms.find((form) => containsWholePhrase(lower, form))
        if (!matchedForm) continue
        const score = scoreSentence(english) + (matchedForm === target.key ? 4 : 0)
        const previous = best.get(target.key)
        if (!previous || score > previous.score) {
          best.set(target.key, { english, japanese, attribution, score })
        }
      }
    }
  }
  return best
}

function getDefinitionCandidates(candidate, definitions) {
  const override = definitionOverrides[candidate.key]
  if (override) return override.split('、').filter(Boolean)
  const definition = definitions.get(candidate.key)
  return cleanDefinitionCandidates(definition?.exactLower || definition?.fallback || '')
}

function readCmudict() {
  const raw = new Map()
  for (const line of readFileSync(cmudictPath, 'utf8').split(/\r?\n/)) {
    if (!line || line.startsWith(';;;')) continue
    const separator = line.indexOf(' ')
    if (separator < 1) continue
    const key = line.slice(0, separator).toLowerCase().replace(/\(\d+\)$/, '')
    if (!raw.has(key)) raw.set(key, line.slice(separator + 1).trim().split(/\s+/))
  }

  const pronunciations = new Map()
  for (const candidate of candidates) {
    const parts = candidate.key.split(/[ -]+/)
    const phonemes = parts.map((part) => raw.get(part))
    if (phonemes.every(Boolean)) {
      pronunciations.set(candidate.key, `/${phonemes.map(arpaToIpa).join(' ')}/`)
    }
  }
  return pronunciations
}

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
      const onsetStart = validOnsets.has(cluster)
        ? clusterStart
        : Math.max(clusterStart, index - 1)
      marks.set(onsetStart, 'ˈ')
    }
    previousVowel = index
  }

  return tokens.map((token, index) => `${marks.get(index) ?? ''}${token.ipa}`).join('')
}

function buildForms(target) {
  const forms = new Set([target.key])
  if (!/^[a-z]+$/.test(target.key)) return [...forms]
  const word = target.key
  if (/名詞|動詞/.test(target.partOfSpeech)) {
    if (word.endsWith('y') && !/[aeiou]y$/.test(word)) forms.add(`${word.slice(0, -1)}ies`)
    else if (/(?:s|x|z|ch|sh)$/.test(word)) forms.add(`${word}es`)
    else forms.add(`${word}s`)
  }
  if (/動詞/.test(target.partOfSpeech)) {
    if (word.endsWith('y') && !/[aeiou]y$/.test(word)) forms.add(`${word.slice(0, -1)}ied`)
    else forms.add(word.endsWith('e') ? `${word}d` : `${word}ed`)
    forms.add(word.endsWith('e') && !word.endsWith('ee') ? `${word.slice(0, -1)}ing` : `${word}ing`)
  }
  for (const form of irregularForms[word] ?? []) forms.add(form)
  return [...forms]
}

function cleanDefinitionCandidates(definition) {
  if (!definition) return []
  const withoutUsageMarkup = definition
    .replace(/[『』]/g, '')
    .replace(/〈[^〉]*〉/g, '')
    .replace(/《[^》]*》/g, '')
    .replace(/\{[^}]*\}/g, '')
    .replace(/\([^()]*\)/g, '')
    .replace(/\([^()]*\)/g, '')
    .replace(/\[[^\]]*\]/g, '')

  return withoutUsageMarkup
    .split(/\s*(?:\/|;|・|、|,)\s*/)
    .filter((sense) => !/《(?:古|まれ|廃|俗|文|差別的表現)/.test(sense))
    .map((sense) => sense
      .replace(/^=\s*/, '')
      .replace(/:[A-Za-z].*$/, '')
      .replace(/^[…]+/, '')
      .replace(/\s+/g, ' ')
      .trim())
    .filter((sense) => /[ぁ-んァ-ン一-龯]/.test(sense))
    .map((sense) => sense.slice(0, 48))
    .filter((sense, index, senses) => senses.indexOf(sense) === index)
    .slice(0, 24)
}

function cleanOxfordPronunciation(value) {
  if (!value) return '/—/'
  return `/${value
    .replace(/^\[|\]$/g, '')
    .replaceAll('ʹ', 'ˈ')
    .replaceAll('͵', 'ˌ')
    .replaceAll('ı', 'ɪ')
    .replaceAll('aʋ', 'aʊ')
    .replaceAll('eı', 'eɪ')
    .replaceAll('ɔ:', 'ɔː')
    .replaceAll('ɑ:', 'ɑː')
    .replaceAll('ɜ:', 'ɜː')
    .replaceAll('i:', 'iː')
    .replaceAll('u:', 'uː')}/`
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

function isUsableSentence(english, japanese) {
  const words = english.match(/[A-Za-z]+(?:'[A-Za-z]+)?/g) ?? []
  if (words.length < 5 || words.length > 18) return false
  if (english.length > 120 || japanese.length > 70) return false
  if (['[', ']', '_', '*', '#', '“', '”'].some((character) => english.includes(character))) return false
  if (/https?:|@/.test(english)) return false
  return /[.!?]$/.test(english)
}

function scoreSentence(sentence) {
  const wordCount = (sentence.match(/[A-Za-z]+(?:'[A-Za-z]+)?/g) ?? []).length
  let score = 100 - Math.abs(11 - wordCount) * 4
  if (/\b(?:Tom|Mary|John)\b/.test(sentence)) score -= 22
  if (/\b(?:I|you)\b/i.test(sentence)) score -= 3
  if (/[,;:]/.test(sentence)) score -= 3
  return score
}

function containsWholePhrase(sentence, phrase) {
  const escaped = phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  return new RegExp(`(^|[^a-z])${escaped}([^a-z]|$)`, 'i').test(sentence)
}

function normalizeWord(word) {
  return word.trim().toLowerCase().replace(/\s+/g, ' ')
}

const definitionOverrides = {
  'according to': '〜によれば、〜に従って',
  act: '行動する、演じる、行為',
  affordable: '手頃な価格の、無理なく買える',
  aids: 'エイズ、後天性免疫不全症候群',
  'all right': '大丈夫な、問題のない',
  analyse: '分析する',
  annoyed: 'いら立った、腹を立てた',
  'any more': 'もう、これ以上',
  anyway: 'とにかく、それでも',
  app: 'アプリ、アプリケーション',
  artwork: '芸術作品、挿絵',
  as: '〜として、〜のように、〜するとき',
  associated: '関連した、結びついた',
  backwards: '後ろ向きに、逆方向へ',
  base: '拠点を置く、基礎、根拠',
  based: '〜に基づいた、〜を拠点とする',
  biological: '生物学的な、生物学の',
  bombing: '爆撃、爆弾攻撃',
  board: '理事会、役員会、板',
  can: '〜できる、缶',
  cartoon: '風刺漫画、漫画、アニメ',
  catch: '列車などに間に合う、捕まえる、つかむ',
  closed: '閉まった、閉鎖された',
  critically: '重大に、批判的に',
  curved: '曲がった、湾曲した',
  dairy: '乳製品の、酪農の、乳製品',
  database: 'データベース',
  defence: '防御、防衛',
  depressing: '気がめいる、憂うつにさせる',
  desperately: '必死に、どうしても',
  disc: '円盤、ディスク',
  divorced: '離婚した',
  download: 'ダウンロードする、ダウンロードしたファイル',
  downwards: '下向きに、下へ',
  dressed: '服を着た、〜の服装をした',
  effectively: '効果的に、事実上',
  efficiently: '効率よく',
  enquiry: '問い合わせ、調査',
  equip: '装備する、備えさせる',
  expected: '予想された、期待された',
  extensively: '広範囲に、幅広く',
  failed: '失敗した、うまくいかなかった',
  firefighter: '消防士',
  'full-time': '常勤の、フルタイムで',
  funding: '資金、資金提供',
  genuinely: '心から、本当に',
  globalization: 'グローバル化、世界規模の一体化',
  grab: 'つかむ、ひったくる',
  guest: '客、宿泊客、招待客',
  have: '持っている、ある',
  healthcare: '医療、保健医療',
  hearing: '聴力、聴覚、聴聞会',
  helmet: 'ヘルメット',
  hold: '収容できる、持つ、開催する',
  id: '身分証明書、本人確認書類',
  impressed: '感心した、感銘を受けた',
  info: '情報',
  innovative: '革新的な、新しい発想の',
  judgement: '判断、判決',
  jury: '陪審員団、審査員団',
  laptop: 'ノートパソコン',
  logo: 'ロゴ、図案化した商標',
  manufacturing: '製造業、製造',
  media: 'メディア、報道機関',
  matching: '一致する、おそろいの',
  maths: '数学',
  meanwhile: 'その間に、一方で',
  mode: '方式、状態、モード',
  offence: '犯罪、違反、不快感',
  opposed: '反対して、対立した',
  petrol: 'ガソリン',
  planning: '計画、計画立案',
  programming: 'プログラミング、番組編成',
  relaxed: 'くつろいだ、緊張していない',
  reporting: '報道、報告すること',
  seminar: 'セミナー、研究会',
  set: '組み立てる、置く、設定する',
  shot: '発砲、銃声、一打',
  sink: '流し台、沈む',
  smile: '笑顔、ほほえみ、ほほえむ',
  smartphone: 'スマートフォン',
  speed: '速度、速さ',
  spicy: '辛い、香辛料のきいた',
  spending: '支出、消費',
  spokesperson: '報道担当者、代弁者',
  terms: '条件、用語、関係',
  testing: '試験、検査',
  ton: 'トン',
  tour: '旅行、見学ツアー',
  treat: '扱う、治療する、おごる',
  towards: '〜の方へ、〜に対して',
  tsunami: '津波',
  unacceptable: '受け入れられない、容認できない',
  upwards: '上向きに、上へ',
  'used to': '以前は〜したものだ',
  venue: '会場、開催地',
  voting: '投票、採決',
  warming: '温暖化、暖めること',
  workplace: '職場',
}

const irregularForms = {
  be: ['am', 'is', 'are', 'was', 'were', 'been'],
  can: ['could'],
  do: ['does', 'did', 'done'],
  go: ['goes', 'went', 'gone'],
  have: ['has', 'had'],
  make: ['made'],
  may: ['might'],
  take: ['took', 'taken'],
  write: ['wrote', 'written'],
}

const vowelPhonemes = new Set(['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'])
const validOnsets = new Set(['', 'b', 'd', 'f', 'g', 'h', 'dʒ', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ʃ', 't', 'tʃ', 'θ', 'v', 'w', 'j', 'z', 'ð', 'ŋ', 'bl', 'br', 'dr', 'fl', 'fr', 'gl', 'gr', 'kl', 'kr', 'pl', 'pr', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tr', 'θr', 'ʃr', 'spl', 'spr', 'str', 'skr', 'skw'])
const arpaMap = {
  AA: 'ɑ', AE: 'æ', AH: 'ʌ', AO: 'ɔ', AW: 'aʊ', AY: 'aɪ', EH: 'ɛ', ER: 'ɝ', EY: 'eɪ',
  IH: 'ɪ', IY: 'i', OW: 'oʊ', OY: 'ɔɪ', UH: 'ʊ', UW: 'u', B: 'b', CH: 'tʃ', D: 'd',
  DH: 'ð', F: 'f', G: 'g', HH: 'h', JH: 'dʒ', K: 'k', L: 'l', M: 'm', N: 'n', NG: 'ŋ',
  P: 'p', R: 'r', S: 's', SH: 'ʃ', T: 't', TH: 'θ', V: 'v', W: 'w', Y: 'j', Z: 'z', ZH: 'ʒ',
}

main()

void root
