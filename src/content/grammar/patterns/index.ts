// 全レッスンぶんの文型データを集約し、合成時に例文へ付与する。
// 補強コンテンツ(expansions)・挿絵(illustrations)と同じ方式で、
// 既存のレッスン定義は書き換えず、ここで一度だけ差し込む。

import type { ContrastSide, GrammarExample, GrammarUnit, LessonBlock } from '../../types'
import { a2Focus, a2Patterns } from './a2.ts'
import { a2PlusFocus, a2PlusPatterns } from './a2plus.ts'
import { b1Focus, b1Patterns } from './b1.ts'
import { b1PlusFocus, b1PlusPatterns } from './b1plus.ts'
import { b2aFocus, b2aPatterns } from './b2a.ts'
import { b2bFocus, b2bPatterns } from './b2b.ts'
import type { PatternEntry, PatternFocusMap, PatternMap } from './types.ts'

export type { PatternEntry, PatternFocusMap, PatternMap } from './types.ts'
export { PATTERN_LABELS, PATTERN_MEANINGS, PATTERN_ORDER } from './types.ts'

export const examplePatterns: PatternMap = {
  ...a2Patterns,
  ...a2PlusPatterns,
  ...b1Patterns,
  ...b1PlusPatterns,
  ...b2aPatterns,
  ...b2bPatterns,
}

/** セクションごとの「文型の視点」本文。すべてのレッスンに用意する。 */
export const lessonPatternFocus: PatternFocusMap = {
  ...a2Focus,
  ...a2PlusFocus,
  ...b1Focus,
  ...b1PlusFocus,
  ...b2aFocus,
  ...b2bFocus,
}

/** 差し込む解説ブロックの見出し。全セクションで共通。 */
export const PATTERN_FOCUS_TITLE = '文型の視点'

function stampExample(example: GrammarExample, where: string): GrammarExample {
  const entry: PatternEntry | undefined = examplePatterns[example.en]
  if (!entry) {
    throw new Error(`${where}: 例文の文型がありません(${example.en})。patterns に追加してください。`)
  }
  return { ...example, pattern: entry.pattern, patternNote: entry.note }
}

function stampContrastSide(side: ContrastSide, where: string): ContrastSide {
  return { ...side, items: side.items.map((item) => stampExample(item, where)) }
}

/**
 * 各例文に5文型を付与し、セクションの「文型の視点」ブロックを最初の解説の直後へ差し込む。
 * UI・Markdown・PDF は合成後の同じデータを使う。
 */
export function applyLessonPatterns(units: GrammarUnit[]): GrammarUnit[] {
  return units.map((unit) => ({
    ...unit,
    lessons: unit.lessons.map((lesson) => {
      const focus = lessonPatternFocus[lesson.id]
      if (!focus) throw new Error(`${lesson.id}: 文型の視点がありません。`)

      let inserted = false
      const blocks = lesson.blocks.flatMap<LessonBlock>((block) => {
        if (block.type === 'examples') {
          return [{ ...block, items: block.items.map((item) => stampExample(item, lesson.id)) }]
        }
        if (block.type === 'contrast') {
          return [
            {
              ...block,
              left: stampContrastSide(block.left, lesson.id),
              right: stampContrastSide(block.right, lesson.id),
            },
          ]
        }
        if (inserted || block.type !== 'explanation') return [block]
        inserted = true
        return [
          block,
          { type: 'explanation', title: PATTERN_FOCUS_TITLE, body: focus },
        ] as LessonBlock[]
      })

      if (!inserted) throw new Error(`${lesson.id}: 文型の視点を差し込む解説ブロックがありません。`)
      return { ...lesson, blocks }
    }),
  }))
}
