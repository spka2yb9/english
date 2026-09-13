// コロケーションを持たない既存語(expanded.ts など)に、後付けでコロケーションを足す。
//   npm run collocations status [n]   未作成の語を先頭 n 件だけ TSV で出力
//   npm run collocations build        scripts/vocab-collocations.tsv → collocations.ts
//
// 執筆する本文は scripts/vocab-collocations.tsv (追記のみ)。列は id / コロケーション(|区切り)。
// notes.ts と同じく、既存データ(batch*.ts / expanded.ts)は書き換えず index.ts で合流させる。
import { existsSync, readFileSync, writeFileSync } from 'node:fs'

const root = new URL('../', import.meta.url)
const tsvPath = new URL('scripts/vocab-collocations.tsv', root)
const outputPath = new URL('src/content/vocabulary/collocations.ts', root)

const [mode, arg] = process.argv.slice(2)

if (mode === 'status') await status(Number(arg) || 40)
else if (mode === 'build') await build()
else {
  console.error('usage: collocations status [n] | build')
  process.exit(1)
}

/** コロケーションをまだ持たず、TSVにも書かれていない語を返す。 */
async function status(limit) {
  const pending = (await pendingEntries()).filter((entry) => !readTsv().has(entry.id))
  const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
  console.error(`${allVocabulary.length - pending.length}/${allVocabulary.length} 完了 / 残り ${pending.length}`)
  for (const entry of pending.slice(0, limit)) {
    console.log([entry.id, entry.partOfSpeech, entry.meaningsJa.join('、')].join('\t'))
  }
}

async function build() {
  const rows = readTsv()
  const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
  const known = new Map(allVocabulary.map((entry) => [entry.id, entry]))

  const problems = []
  for (const [id, collocations] of rows) {
    const entry = known.get(id)
    if (!entry) {
      problems.push(`${id}: 語彙データにないIDです`)
      continue
    }
    problems.push(...check(entry, collocations))
  }
  if (problems.length > 0) {
    console.error(problems.join('\n'))
    throw new Error(`コロケーションの検査で ${problems.length} 件の問題があります`)
  }

  const body = [...rows.keys()]
    .sort()
    .map((id) => `  ${JSON.stringify(id)}: ${JSON.stringify(rows.get(id))},`)
    .join('\n')
  writeFileSync(
    outputPath,
    `// このファイルは scripts/collocations.mjs で生成する(手で編集しない)。\n` +
      `// コロケーションを持たない既存語への後付け分。キーは VocabularyEntry.id。\n` +
      `// index.ts で、自前の collocations を持たないエントリにだけ合流する。\n` +
      `export const vocabularyCollocations: Record<string, string[]> = {\n${body}\n}\n`,
  )
  console.error(`${rows.size} 語を ${outputPath.pathname} に書き出しました。`)
}

/**
 * 取り込み前の検査。見出し語を含まないコロケーションは、別の語からの取り違えである可能性が高い。
 * 語幹の前方一致は content.test.ts の例文検査と同じ規則にそろえる。
 */
function check(entry, collocations) {
  const problems = []
  if (collocations.length < 2 || collocations.length > 4) {
    problems.push(`${entry.id}: コロケーションが ${collocations.length} 件です`)
  }
  if (new Set(collocations).size !== collocations.length) problems.push(`${entry.id}: コロケーションが重複しています`)
  const head = entry.word.toLowerCase().split(' ')[0]
  const stem = head.slice(0, Math.max(3, head.length - 3))
  for (const collocation of collocations) {
    if (!collocation.toLowerCase().includes(stem)) {
      problems.push(`${entry.id}: 「${collocation}」が見出し語を含みません`)
    }
    if (collocation.trim() !== collocation || collocation.length === 0) {
      problems.push(`${entry.id}: 「${collocation}」の前後に空白があります`)
    }
  }
  return problems
}

async function pendingEntries() {
  const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
  return allVocabulary.filter((entry) => !entry.collocations || entry.collocations.length === 0)
}

function readTsv() {
  const rows = new Map()
  if (!existsSync(tsvPath)) return rows
  for (const [index, line] of readFileSync(tsvPath, 'utf8').split(/\r?\n/).entries()) {
    if (!line.trim() || line.startsWith('#')) continue
    const [id, collocations] = line.split('\t')
    const at = `${tsvPath.pathname}:${index + 1}`
    if (!id || !collocations) throw new Error(`${at}: 列が足りません`)
    if (rows.has(id)) throw new Error(`${at}: ${id} が重複しています`)
    rows.set(
      id,
      collocations.split('|').map((value) => value.trim()).filter(Boolean),
    )
  }
  return rows
}
