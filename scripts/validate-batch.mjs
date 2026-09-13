// 生成したコンテンツを取り込む前の検査。
// 教師レビューを行わない前提のため、機械で落とせる欠陥はここで全部落としてから src/content へ入れる。
//
// 使い方:
//   npm run validate:batch -- <candidates.json>
//
// 入力は { passages?: ReadingPassage[], questions?: QuizQuestion[] } の JSON。
// 判定は src/content/validation.ts と同じ関数を使う(CIゲートと検査基準を二重管理しない)。

import { readFileSync } from 'node:fs'

const { checkPassage, checkQuestion, findNearDuplicates, unknownWordRatio } = await import(
  '../src/content/validation.ts'
)
const { basicWords } = await import('../src/content/basicWords.ts')
const { allVocabulary } = await import('../src/content/vocabulary/index.ts')
const { readingPassages } = await import('../src/content/reading/index.ts')

const inputPath = process.argv[2]
if (!inputPath) {
  console.error('使い方: npm run validate:batch -- <candidates.json>')
  process.exit(2)
}

const MAX_UNKNOWN_RATIO = 0.1
const batch = JSON.parse(readFileSync(inputPath, 'utf8'))
const known = new Set(basicWords)
for (const entry of allVocabulary) known.add(entry.word.toLowerCase())

const issues = []
const passages = batch.passages ?? []

for (const passage of passages) {
  issues.push(...checkPassage(passage))
  const ratio = unknownWordRatio(passage.paragraphs.join(' '), known)
  if (ratio >= MAX_UNKNOWN_RATIO) {
    issues.push({ where: passage.id, message: `未習語率 ${(ratio * 100).toFixed(1)}% が上限を超えています` })
  }
}

for (const question of batch.questions ?? []) issues.push(...checkQuestion(question, 'batch'))

// 既存コンテンツとの重複も見る(生成モデルは既にある本文と似たものを作りやすい)
issues.push(
  ...findNearDuplicates([
    ...readingPassages.map((p) => ({ id: `既存:${p.id}`, text: p.paragraphs.join(' ') })),
    ...passages.map((p) => ({ id: p.id, text: p.paragraphs.join(' ') })),
  ]),
)

if (issues.length === 0) {
  console.log(`OK: 本文${passages.length}件 / 設問${(batch.questions ?? []).length}件 — 取り込み可能です。`)
  process.exit(0)
}

console.error(`NG: ${issues.length}件の問題が見つかりました。`)
for (const issue of issues) console.error(`  [${issue.where}] ${issue.message}`)
console.error('\n※ 解答の妥当性(正解が本当に正解か)は機械検査では判定できません。')
console.error('  取り込み前に、別モデルで独立に解かせて正解が一致することを確認してください。')
process.exit(1)
