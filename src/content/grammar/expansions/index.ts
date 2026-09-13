import type { GrammarUnit, LessonBlock } from '../../types'
import { a2Expansions } from './a2.ts'
import { a2PlusExpansions } from './a2plus.ts'
import { b1Expansions } from './b1.ts'
import { b1PlusExpansions } from './b1plus.ts'
import { b2Expansions } from './b2.ts'
import { extraExamples } from './extraExamples.ts'
import type { LessonExpansionMap } from './types.ts'

export const lessonExpansions: LessonExpansionMap = {
  ...a2Expansions,
  ...a2PlusExpansions,
  ...b1Expansions,
  ...b1PlusExpansions,
  ...b2Expansions,
}

/** 例文ブロックはこの数にそろえる。並べ替え10問の母集団も同じ10文になる。 */
export const EXAMPLES_PER_LESSON = 10

/**
 * 補強解説を主例文の直前に置き、同じ例文ブロックへ補強3文と10文そろえるための追加分を足す。
 * すべての表示・エクスポート経路が共通の GrammarUnit を使うため、ここで一度だけ合成する。
 */
export function applyLessonExpansions(units: GrammarUnit[]): GrammarUnit[] {
  return units.map((unit) => ({
    ...unit,
    lessons: unit.lessons.map((lesson) => {
      const expansion = lessonExpansions[lesson.id]
      if (!expansion) throw new Error(`${lesson.id}: 補強コンテンツがありません。`)

      let examplesAdded = false
      const blocks = lesson.blocks.flatMap<LessonBlock>((block) => {
        if (block.type !== 'examples' || examplesAdded) return [block]
        examplesAdded = true
        return [
          {
            type: 'explanation',
            title: expansion.explanationTitle,
            body: expansion.explanationBody,
          },
          {
            ...block,
            items: [...block.items, ...expansion.examples, ...(extraExamples[lesson.id] ?? [])],
          },
        ]
      })

      if (!examplesAdded) throw new Error(`${lesson.id}: 追加先の例文ブロックがありません。`)
      return { ...lesson, blocks }
    }),
  }))
}

export type { LessonExpansion, LessonExpansionMap } from './types'
