import type { GrammarExample } from '../../types'

/** 既存レッスンへ追加する、理解を深める解説と3つの例文。 */
export type LessonExpansion = {
  explanationTitle: string
  explanationBody: string
  examples: [GrammarExample, GrammarExample, GrammarExample]
}

export type LessonExpansionMap = Record<string, LessonExpansion>
