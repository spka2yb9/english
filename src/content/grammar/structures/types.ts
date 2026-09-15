// セクションごとの「英文がどう組み上がっているか」を補うデータ。
//
// patterns(5文型)・expansions(補強解説)・illustrations(挿絵) と同じ方式で、
// 既存のレッスン定義は書き換えず、合成時に本文と追加問題を差し込む。
// これにより UI・Markdown・PDF が同じデータを使う。

import type { LessonBlock, QuizQuestion } from '../../types'

export type LessonStructure = {
  /** レッスン本文へ差し込む構造ブロック(breakdown / expansion など)。 */
  blocks: LessonBlock[]
  /** 構造を判断する追加問題。既存クイズとは別セクションで出す。 */
  quiz?: QuizQuestion[]
}

/**
 * レッスンIDをキーにした構造データ。
 * 学習導線の7ステップ(骨格 → 動詞 → 修飾 → 句 → 節 → 接続 → 長文)のうち、
 * そのセクションが担う補強だけを持つ。無いレッスンは差し込みを行わない。
 */
export type LessonStructureMap = Record<string, LessonStructure>
