// 新しく書いた語彙ファイルを、index.ts へ組み込む前に検証する。
// 既存語との重複・IPA形式・例文と語幹の一致・コロケーション・覚えるヒントを見る。
//
//   node --experimental-strip-types --no-warnings scripts/validate-vocab-entries.mjs \
//     src/content/vocabulary/plus30.ts src/content/vocabulary/plus31.ts
//
// content.test.ts は index.ts に入った後しか見られないので、その手前で落とすための道具。
import { allVocabulary } from '../src/content/vocabulary/index.ts'
import { checkAudioText } from '../src/content/validation.ts'
import path from 'node:path'

const files = process.argv.slice(2)
if (files.length === 0) {
  console.error('usage: validate-vocab-entries.mjs <plusNN.ts> ...')
  process.exit(1)
}

// index.ts に取りこみ済みのファイルは自分自身が既存側にも現れるので、id が一致するなら通す。
const existing = new Map()
for (const entry of allVocabulary) existing.set(entry.word.toLowerCase(), entry.id)

const seen = new Map()
let bad = 0
let total = 0
const fail = (id, message) => {
  console.error(`  ✗ ${id}: ${message}`)
  bad++
}

for (const file of files) {
  const module = await import(path.resolve(file))
  const entries = Object.values(module).find(Array.isArray)
  if (!entries) {
    fail(file, '配列の export が見つからない')
    continue
  }
  console.log(`${path.basename(file)}: ${entries.length}`)
  total += entries.length
  for (const entry of entries) {
    const word = entry.word.toLowerCase()
    // 取りこみ済みのファイル自身は既存側にも現れるので、id が一致するなら重複ではない
    if (existing.has(word) && existing.get(word) !== entry.id) {
      fail(entry.id, `既存語と重複 (${existing.get(word)})`)
    }
    if (seen.has(word)) fail(entry.id, `新規内で重複 (${seen.get(word)})`)
    seen.set(word, entry.id)

    if (entry.id !== word) fail(entry.id, `id が word の小文字と一致しない (${word})`)
    if (!/^\/.+\/$/.test(entry.pronunciation)) fail(entry.id, `IPAが /.../ 形式でない: ${entry.pronunciation}`)
    if (!entry.meaningsJa?.length) fail(entry.id, 'meaningsJa がない')
    if (!entry.exampleTranslationJa?.length) fail(entry.id, '例文の和訳がない')
    if (!['A2', 'B1', 'B2'].includes(entry.level)) fail(entry.id, `level が不正: ${entry.level}`)
    if (!entry.mnemonic?.length) fail(entry.id, '覚えるヒント(mnemonic)がない')

    // content.test.ts と同じ語幹判定にそろえる
    const head = word.split(' ')[0]
    const stem = head.slice(0, Math.max(3, head.length - 3))
    if (!entry.exampleSentence.toLowerCase().includes(stem)) {
      fail(entry.id, `例文に語幹 "${stem}" が出てこない`)
    }
    for (const issue of checkAudioText(entry.exampleSentence, entry.id)) fail(entry.id, issue.message)

    if (!entry.collocations?.length) fail(entry.id, 'collocations がない')
    else if (!entry.collocations.some((c) => c.toLowerCase().includes(stem))) {
      fail(entry.id, `collocations のどれにも語幹 "${stem}" が入っていない`)
    }
  }
}

if (bad > 0) {
  console.error(`NG: ${bad}件`)
  process.exit(1)
}
console.log(`OK: ${total}語すべて通過`)
