import type { LessonAnimation } from '../grammar/animations'
import type { CefrLevel, LessonBlock, QuizQuestion } from '../types'

export type ThreeMinuteSpeaker = 'ingbird' | 'hiyoko'

/** イングバードとヒヨコ君の両方が使える表情。 */
export type ThreeMinuteMood = 'happy' | 'cheer' | 'think' | 'curious' | 'wow' | 'proud' | 'shy'

export type ThreeMinuteLine = {
  speaker: ThreeMinuteSpeaker
  /** 吹き出しの本文。**強調** と箇条書き(- )を使える。 */
  text: string
  mood?: ThreeMinuteMood
  /** 吹き出しの中に英文カードとして見せる場合の英文。 */
  en?: string
  /** 英文カードの和訳。 */
  ja?: string
  /** 英文カード内で強調する部分。 */
  highlight?: string
}

export type ThreeMinutePart =
  | { kind: 'line'; line: ThreeMinuteLine }
  /** 文法ページと同じ教材ブロックを、会話のホワイトボードとして見せる。 */
  | { kind: 'block'; block: LessonBlock; label: string }
  /** 文法ページの3段階アニメーションをそのまま使う。 */
  | { kind: 'animation'; animation: LessonAnimation }

export type ThreeMinuteTerm = {
  term: string
  /** 会話に出てきた文法用語のやさしい意味。 */
  plain: string
}

export type ThreeMinuteSection = {
  lessonId: string
  title: string
  level: CefrLevel
  unitId: string
  unitTitle: string
  objective: string
  /** 会話と図の情報量から出した読了目安(分)。 */
  minutes: number
  parts: ThreeMinutePart[]
  /** 会話に出てきた文法用語のミニ辞典。読み返し用。 */
  terms: ThreeMinuteTerm[]
  /** 最後の理解度チェック。通常の話は4問、5文型の導入は8問。 */
  quiz: QuizQuestion[]
}
