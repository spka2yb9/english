// 全レッスンぶんの構造データを集約し、合成時に本文と追加問題を差し込む。
// patterns(5文型)・expansions(補強解説)・illustrations(挿絵)と同じ方式で、
// 既存のレッスン定義は書き換えず、ここで一度だけ付与する。

import type { GrammarUnit, LessonBlock } from '../../types'
import { PATTERN_FOCUS_TITLE } from '../patterns/index.ts'
import { step2Structures } from './step2.ts'
import { step3Structures } from './step3.ts'
import { step4Structures } from './step4.ts'
import { step5Structures } from './step5.ts'
import { step6Structures } from './step6.ts'
import type { LessonStructureMap } from './types.ts'

export const lessonStructures: LessonStructureMap = {
  ...step2Structures,
  ...step3Structures,
  ...step4Structures,
  ...step5Structures,
  ...step6Structures,
}

/**
 * 構造ブロックを「文型の視点」の直後へ差し込み、追加問題を structureQuiz として付与する。
 * 構造データを持たないレッスンはそのまま返す(全レッスンに必須ではない)。
 */
export function applyLessonStructures(units: GrammarUnit[]): GrammarUnit[] {
  return units.map((unit) => ({
    ...unit,
    lessons: unit.lessons.map((lesson) => {
      const structure = lessonStructures[lesson.id]
      if (!structure) return lesson

      const blocks: LessonBlock[] = []
      let inserted = false
      for (const block of lesson.blocks) {
        blocks.push(block)
        if (inserted) continue
        if (block.type === 'explanation' && block.title === PATTERN_FOCUS_TITLE) {
          blocks.push(...structure.blocks)
          inserted = true
        }
      }
      if (!inserted) throw new Error(`${lesson.id}: 構造ブロックを差し込む「文型の視点」がありません。`)

      return {
        ...lesson,
        blocks,
        ...(structure.quiz ? { structureQuiz: structure.quiz } : {}),
      }
    }),
  }))
}

// 「英文の作られ方から学ぶ」ページが使う内容。
// 旧 u01-l4(英語の語順 SVO)と旧 u01-l5(5文型で文の骨組みを見る)を統合したもので、
// レッスンではないため unit には属さない。
export { roleBlocks, roleExampleSentence, roleGuides, wordOrderBlocks, wordOrderExamples, wordOrderQuiz } from './skeleton.ts'
export type { RoleGuide } from './skeleton.ts'
export { patternBlocks, patternExamples, patternQuiz, patternShowcases } from './patternGuide.ts'
export type { PatternShowcase } from './patternGuide.ts'
export { patternAnimations, skeletonAnimation, wordOrderAnimation } from './patternAnimations.ts'

export type { LessonStructure, LessonStructureMap } from './types.ts'
