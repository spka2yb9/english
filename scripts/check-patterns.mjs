// 5文型データの整合性チェック。
//   node --experimental-strip-types --no-warnings scripts/check-patterns.mjs
// 次を検証し、問題があれば終了コード1で落とす。
//   - 例文・対比のすべての英文に文型がある(content.test.ts と同じ検査)
//   - 文型表に、どの例文でも使われないキー(打ち間違いの疑い)がない
//   - レベルをまたいで同じ英文に違う文型が付いていない

import { allLessons } from '../src/content/grammar/index.ts'
import { a2Patterns } from '../src/content/grammar/patterns/a2.ts'
import { a2PlusPatterns } from '../src/content/grammar/patterns/a2plus.ts'
import { b1Patterns } from '../src/content/grammar/patterns/b1.ts'
import { b1PlusPatterns } from '../src/content/grammar/patterns/b1plus.ts'
import { b2aPatterns } from '../src/content/grammar/patterns/b2a.ts'
import { b2bPatterns } from '../src/content/grammar/patterns/b2b.ts'
import { examplePatterns } from '../src/content/grammar/patterns/index.ts'

const used = new Set()
let missing = 0
for (const lesson of allLessons) {
  for (const block of lesson.blocks) {
    const items =
      block.type === 'examples'
        ? block.items
        : block.type === 'contrast'
          ? [...block.left.items, ...block.right.items]
          : []
    for (const item of items) {
      used.add(item.en)
      if (!examplePatterns[item.en]) {
        missing++
        console.error(`MISSING  ${lesson.id}: ${item.en}`)
      }
    }
  }
}

const maps = { a2: a2Patterns, a2plus: a2PlusPatterns, b1: b1Patterns, b1plus: b1PlusPatterns, b2a: b2aPatterns, b2b: b2bPatterns }
const seen = new Map()
const conflicts = []
for (const [name, map] of Object.entries(maps)) {
  for (const [en, entry] of Object.entries(map)) {
    if (seen.has(en)) {
      if (seen.get(en).pattern !== entry.pattern) {
        conflicts.push(`${en}: ${seen.get(en).level}=${seen.get(en).pattern} vs ${name}=${entry.pattern}`)
      }
    } else {
      seen.set(en, { level: name, pattern: entry.pattern })
    }
  }
}

const unused = Object.keys(examplePatterns).filter((en) => !used.has(en))

console.log(`使われている英文: ${used.size}`)
console.log(`文型エントリ: ${Object.keys(examplePatterns).length}`)
console.log(`文型なし: ${missing}`)
console.log(`未使用キー: ${unused.length}`)
console.log(`レベル間の衝突: ${conflicts.length}`)
for (const en of unused) console.error(`UNUSED  ${en}`)
for (const conflict of conflicts) console.error(`CONFLICT  ${conflict}`)

if (missing > 0 || unused.length > 0 || conflicts.length > 0) process.exit(1)
