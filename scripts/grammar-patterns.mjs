// 5文型データの作業・点検ツール。
//   node --experimental-strip-types --no-warnings scripts/grammar-patterns.mjs <A2|A2+|B1|B1+|B2> [unitId ...]
// そのレベル(ユニット指定があればそのユニットだけ)の全セクションについて、
// 例文・対比の英文と、現在の文型表の対応を一覧する。
// MISSING が残っている英文を patterns/ に足す。focus:MISSING は「文型の視点」未記入。

const level = process.argv[2]
if (!level) {
  console.error('usage: node --experimental-strip-types --no-warnings scripts/grammar-patterns.mjs <A2|A2+|B1|B1+|B2> [unitId ...]')
  process.exit(1)
}

const unitFilter = process.argv.slice(3)

const { grammarUnits } = await import('../src/content/grammar/index.ts')
const { examplePatterns, lessonPatternFocus } = await import('../src/content/grammar/patterns/index.ts')

let total = 0
let missing = 0

const units = grammarUnits.filter(
  (u) => u.level === level && (unitFilter.length === 0 || unitFilter.includes(u.id)),
)

for (const unit of units) {
  console.log(`\n## ${unit.id} ${unit.title}`)
  for (const lesson of unit.lessons) {
    const focusMark = lessonPatternFocus[lesson.id] ? 'focus:ok' : 'focus:MISSING'
    console.log(`\n### ${lesson.id} ${lesson.title} [${focusMark}]`)

    const items = []
    for (const block of lesson.blocks) {
      if (block.type === 'examples') items.push(...block.items)
      if (block.type === 'contrast') items.push(...block.left.items, ...block.right.items)
    }
    for (const example of items) {
      total++
      const entry = examplePatterns[example.en]
      if (!entry) missing++
      console.log(`${entry ? entry.pattern.padEnd(5) : 'MISSING'}\t${example.en}`)
    }
  }
}

console.log(`\n${level}${unitFilter.length ? ` [${unitFilter.join(',')}]` : ''}: ${total} 例文, MISSING ${missing}`)
