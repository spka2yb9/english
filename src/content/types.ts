// 教材コンテンツのデータモデル。コンテンツはUIから分離し、
// 同一データから React UI / Markdown / PDF を生成する。

export type CefrLevel = 'A2' | 'A2+' | 'B1' | 'B1+' | 'B2'

/** 英語例文。en は TTS にそのまま渡せるクリーンな英文にする(記号・注記を含めない)。 */
export type GrammarExample = {
  en: string
  ja?: string
  /** en 内の部分文字列。UIで視覚的にハイライトする(音声には影響しない)。 */
  highlight?: string
  /** 短い日本語注記 */
  note?: string
}

/** タイムライン図。軸は 0(過去)〜100(現在)。100超は未来。 */
export type TimelineSpec = {
  title?: string
  /** 一点の出来事の位置(0〜130) */
  point?: number
  pointLabel?: string
  /** 継続の区間 [開始, 終了] */
  range?: [number, number]
  rangeLabel?: string
  /** 区間が「今」まで続くことを矢印で示す */
  arrowToNow?: boolean
  caption?: string
}

export type ContrastSide = {
  label: string
  items: GrammarExample[]
  /** この側のポイント(日本語) */
  pointJa?: string
}

/**
 * 挿絵の種類。図そのものは Illustration コンポーネント、
 * ラベル本数と説明文(alt)は src/content/illustrations.ts が持つ。
 */
export type IllustrationKind =
  | 'equals'
  | 'action'
  | 'helper-verb'
  | 'repeat-cycle'
  | 'clock-moment'
  | 'calendar-day'
  | 'now-to-future'
  | 'scale'
  | 'count-vs-mass'
  | 'one-vs-the'
  | 'filter-group'
  | 'near-far'
  | 'tag-noun'
  | 'question-mark'
  | 'bars-compare'
  | 'podium'
  | 'point-surface-box'
  | 'path-move'
  | 'linked-pair'
  | 'gate-allow'
  | 'arrow-vs-loop'
  | 'bridge-past-now'
  | 'steps'
  | 'spotlight-swap'
  | 'dots-omit'
  | 'two-roads'
  | 'thought-cloud'
  | 'speech-relay'
  | 'earlier-later'
  | 'cause-effect'
  | 'box-in-slot'
  | 'feeling-source'
  | 'handoff'
  | 'eye-ear'
  | 'swap-cards'
  | 'two-cards'

export type LessonBlock =
  /** body: 段落は \n\n 区切り。**強調** と "- " 箇条書きをサポート。 */
  | { type: 'explanation'; title?: string; body: string }
  | { type: 'examples'; title?: string; items: GrammarExample[] }
  | { type: 'timeline'; title?: string; timelines: TimelineSpec[] }
  | { type: 'table'; title?: string; headers: string[]; rows: string[][] }
  | { type: 'contrast'; title?: string; left: ContrastSide; right: ContrastSide; note?: string }
  /** 文構造図: SUBJECT → VERB → OBJECT のような並び */
  | { type: 'structure'; title?: string; parts: { label: string; text: string }[]; caption?: string }
  /** 挿絵。sceneId ごとに固有のSVG構図を持ち、labels は図の中に描き込む。 */
  | { type: 'illustration'; sceneId: string; kind: IllustrationKind; labels: string[]; alt: string; caption?: string }

export type QuizQuestion = {
  id: string
  /** 日本語の設問(例: 正しい文を選んでください。) */
  prompt: string
  /** 設問の横で再生できる英語。設問文に出てくる語や文を聞かせたいときに使う。 */
  promptAudio?: string
  /** 文脈となる英文(空所は ___ )。省略可。 */
  sentence?: string
  sentenceJa?: string
  choices: string[]
  correctIndex: number
  /** 正解の理由(日本語) */
  explanation: string
  /** 各選択肢への注記(誤答がなぜ誤りか)。choices と同じ長さ。正解位置は null 可。 */
  choiceNotes?: (string | null)[]
  /** 回答後に再生できる完全な正解英文 */
  audioEn?: string
}

export type GrammarLesson = {
  id: string
  unitId: string
  level: CefrLevel
  title: string
  /** このセクションでできるようになること(日本語) */
  objective: string
  minutes: number
  /** 前提レッスンID */
  prereqs?: string[]
  blocks: LessonBlock[]
  quiz: QuizQuestion[]
  /** まとめ 2〜5点 */
  summary: string[]
}

export type GrammarUnit = {
  id: string
  level: CefrLevel
  title: string
  lessons: GrammarLesson[]
}

export type VocabularyEntry = {
  id: string
  word: string
  level: 'A2' | 'B1' | 'B2'
  /** 品詞(日本語: 動詞・名詞・形容詞・副詞・句動詞 など) */
  partOfSpeech: string
  meaningsJa: string[]
  /** IPA発音記号 */
  pronunciation: string
  exampleSentence: string
  exampleTranslationJa: string
  /** 外部のオープン対訳を使用する場合の出典。独自例文では省略する。 */
  exampleSource?: {
    name: string
    url: string
    license: string
    attribution?: string
  }
  collocations?: string[]
  /** 語形成(接頭辞・接尾辞・語根)の日本語解説 */
  wordFormation?: string
  /** 確実な場合のみ記載する語源 */
  etymology?: string
  /** 記憶フック(語源とは明確に区別する) */
  mnemonic?: string
  relatedWords?: string[]
}

export type PronunciationEntry = {
  symbol: string
  type: 'vowel' | 'diphthong' | 'consonant'
  /** 例語(TTSで再生可能) */
  examples: string[]
  /** 日本語での音の説明 */
  ja: string
  /** 出し方のコツ(日本語) */
  tip: string
}

/** 対比ペア(right / light など) */
export type MinimalPair = {
  focus: string // 例: 'R と L'
  a: { word: string; ipa: string }
  b: { word: string; ipa: string }
  tip: string
}

/** 発音トピック(強勢・弱形・連結など)。body は RichText 形式。 */
export type PronunciationTopic = {
  id: string
  title: string
  body: string
  examples: GrammarExample[]
}

/** 多読の本文。段落ごとに和訳と音声を持つ。 */
export type ReadingPassage = {
  id: string
  level: 'A2' | 'B1' | 'B2'
  title: string
  titleJa: string
  /** 目安時間(分)。台帳の supply 集計に使う。 */
  minutes: number
  /** 段落。1段落は TTS に渡せるクリーンな英文のみ。 */
  paragraphs: string[]
  /** paragraphs と同じ長さの和訳 */
  paragraphsJa: string[]
  glossary: { word: string; ja: string }[]
  /** 内容理解の設問。文法クイズと同じ形式・同じUIを使う。 */
  questions: QuizQuestion[]
  /** 対応する can-do 記述子ID */
  canDo: string[]
}
