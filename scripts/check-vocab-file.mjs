// 1ファイル分の語彙エントリを自己点検する。
// index.ts へ入れる前のバッチ(plusNN.ts)を、統合前の時点で検査するために使う。
// 検査内容は check-vocab.mjs と同じ。
// 使い方: node --experimental-strip-types --no-warnings scripts/check-vocab-file.mjs src/content/vocabulary/plus40.ts
import { pathToFileURL } from 'node:url'

const file = process.argv[2]
if (!file) {
  console.error('usage: node --experimental-strip-types --no-warnings scripts/check-vocab-file.mjs <file.ts>')
  process.exit(1)
}

const mod = await import(pathToFileURL(file).href)
const entries = Object.values(mod).find((value) => Array.isArray(value))
if (!entries) {
  console.error(`${file}: 配列のエクスポートが見つかりません`)
  process.exit(1)
}

const bad = []
const seenId = new Set()
const seenWord = new Set()
const cjk = (text) => /[\u3000-\u30ff\u4e00-\u9fff\uff00-\uffef]/.test(text)

for (const e of entries) {
  const miss = []
  const head = String(e.word ?? '').toLowerCase().split(' ')[0]
  const stem = head.slice(0, Math.max(3, head.length - 3))

  if (!e.id?.length) miss.push('id')
  if (!e.word?.length) miss.push('word')
  if (!e.mnemonic?.length) miss.push('mnemonic')
  if (!e.meaningsJa?.length) miss.push('meaningsJa')
  if (!e.partOfSpeech?.length) miss.push('partOfSpeech')
  if (!e.exampleTranslationJa?.length) miss.push('exampleTranslationJa')
  if (!e.pronunciation?.length) miss.push('pronunciation')
  else if (!/^\/.+\/$/.test(e.pronunciation)) miss.push(`pronunciation not IPA: ${e.pronunciation}`)
  if (!['A2', 'B1', 'B2'].includes(e.level)) miss.push(`level: ${e.level}`)

  if (!e.collocations?.length) miss.push('collocations')
  else if (!e.collocations.some((c) => c.toLowerCase().includes(stem))) miss.push(`stem "${stem}"`)
  if (!e.exampleSentence?.toLowerCase().includes(stem)) miss.push(`example lacks "${stem}"`)
  if (e.exampleSentence && cjk(e.exampleSentence)) miss.push('example has Japanese')
  for (const c of e.collocations ?? []) if (cjk(c)) miss.push(`collocation has Japanese: ${c}`)
  for (const w of e.relatedWords ?? []) if (cjk(w)) miss.push(`relatedWord has Japanese: ${w}`)

  if (seenId.has(e.id)) miss.push('dup id')
  if (seenWord.has(String(e.word).toLowerCase())) miss.push('dup word')
  seenId.add(e.id)
  seenWord.add(String(e.word).toLowerCase())

  if (miss.length) bad.push(`${e.id}: ${miss.join(', ')}`)
}

console.log(`${file}: total ${entries.length}, bad ${bad.length}`)
for (const line of bad) console.log(' ', line)

const eyeball = entries.filter((e) => /[A-Za-z]{3,}/.test(e.exampleTranslationJa ?? ''))
console.log(`\n訳文に英字を含む ${eyeball.length} 件(正当なものも含む。目で確認する)`)
for (const e of eyeball) console.log(' ', e.id, '::', e.exampleTranslationJa)
