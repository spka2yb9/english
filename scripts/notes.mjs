// 語彙の解説文(覚えるヒント)を notes.ts に蓄積する。中断しても再開できる。
//   npm run notes status [n]      進捗と、未作成の先頭 n 語(TSV)を出力
//   npm run notes add < x.json    {"id":"解説文"} を追記(既存キーは上書き)
import { readFileSync, writeFileSync } from 'node:fs'

const notesPath = new URL('../src/content/vocabulary/notes.ts', import.meta.url)
const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
const { vocabularyNotes } = await import('../src/content/vocabulary/notes.ts')

const [mode, arg] = process.argv.slice(2)
const pending = allVocabulary.filter((e) => !e.mnemonic)

if (mode === 'status') {
  const done = allVocabulary.length - pending.length
  console.error(`${done}/${allVocabulary.length} 完了 / 残り ${pending.length}`)
  for (const e of pending.slice(0, Number(arg) || 40)) {
    console.log([e.id, e.level, e.partOfSpeech, e.meaningsJa.join('、'), e.exampleSentence].join('\t'))
  }
} else if (mode === 'add') {
  const incoming = JSON.parse(readFileSync(0, 'utf8'))
  const known = new Set(allVocabulary.map((e) => e.id))
  const unknown = Object.keys(incoming).filter((id) => !known.has(id))
  if (unknown.length > 0) throw new Error(`未知のID: ${unknown.join(', ')}`)
  const merged = { ...vocabularyNotes, ...incoming }
  const body = Object.keys(merged)
    .sort()
    .map((id) => `  ${JSON.stringify(id)}: ${JSON.stringify(merged[id])},`)
    .join('\n')
  writeFileSync(
    notesPath,
    `// 語彙の「覚えるヒント」解説文。scripts/notes.mjs で追記する(手で編集しない)。\n` +
      `// キーは VocabularyEntry.id。index.ts で mnemonic として合流する。\n` +
      `export const vocabularyNotes: Record<string, string> = {\n${body}\n}\n`,
  )
  console.error(`+${Object.keys(incoming).length} → 解説文 ${Object.keys(merged).length} 件`)
} else {
  console.error('usage: notes status [n] | notes add < file.json')
  process.exit(1)
}
