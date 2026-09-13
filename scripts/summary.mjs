// ダッシュボード用の軽量サマリーを生成する。
//   - ホーム画面が文法・語彙の全データ(gzip 約700KB)を読み込まないようにする
//   - can-do 記述子ごとの対応コンテンツ数を数え、カバレッジの穴を検出できるようにする
// 使い方: npm run summary(コンテンツを追加・変更したら実行する)
// 生成物のズレは src/content/content.test.ts が検出する。

import { writeFileSync } from 'node:fs'

const { allLessons } = await import('../src/content/grammar/index.ts')
const { allVocabulary } = await import('../src/content/vocabulary/index.ts')

const { readingPassages } = await import('../src/content/reading/index.ts')
const { dictationSentences } = await import('../src/services/sentenceBank.ts')
const { unitCanDo, vocabularyCanDo } = await import('../src/content/cando.ts')

const lessons = allLessons.map((lesson) => ({ id: lesson.id, title: lesson.title, minutes: lesson.minutes }))

const grammarQuestionCount = allLessons.reduce((sum, lesson) => sum + lesson.quiz.length, 0)

// can-do 記述子ごとに、対応するコンテンツが何件あるか
const canDoCoverage = {}
const addCoverage = (ids) => {
  for (const id of ids ?? []) canDoCoverage[id] = (canDoCoverage[id] ?? 0) + 1
}
for (const lesson of allLessons) addCoverage(unitCanDo[lesson.unitId])
for (const entry of allVocabulary) addCoverage(vocabularyCanDo[entry.level])
for (const passage of readingPassages) addCoverage(passage.canDo)
// リスニングはディクテーション演習と判定テストの音声問題が担う
const listeningCanDo = { A2: 'L-A2-1', B1: 'L-B1-1', B2: 'L-B2-1' }
for (const sentence of dictationSentences) addCoverage([listeningCanDo[sentence.level]])

const source = `// 生成ファイル。npm run summary で更新する(手で編集しない)。
// ホーム画面が教材データ本体を読み込まずに件数を表示するためのサマリー。

export type GrammarLessonSummary = { id: string; title: string; minutes: number }

export const grammarLessonSummaries: GrammarLessonSummary[] = ${JSON.stringify(lessons, null, 2)}

export const vocabularyCount = ${allVocabulary.length}

export const readingPassageCount = ${readingPassages.length}

export const grammarQuestionCount = ${grammarQuestionCount}

/** can-do 記述子ID → 対応するコンテンツ件数 */
export const canDoCoverage: Record<string, number> = ${JSON.stringify(canDoCoverage, null, 2)}
`

writeFileSync(new URL('../src/content/summary.ts', import.meta.url), source)
console.log(`summary.ts: ${lessons.length} lessons / ${allVocabulary.length} words / ${readingPassages.length} passages`)
