// セクション内Q&A(イングバードにきく)の型。
// コーパス(corpus.ts)が教材データから QaEntry を作り、判定器(matcher.ts)が質問に合う1件を選ぶ。

export type QaIntent =
  /** 解説・なぜ・仕組み */
  | 'concept'
  /** 英文や語句の意味・和訳 */
  | 'meaning'
  /** 例文の一覧 */
  | 'example'
  /** 対比・使い分け */
  | 'difference'
  /** 5文型 */
  | 'pattern'
  /** 構造・S/V/O/C/M・骨格 */
  | 'structure'
  /** セクションの目標・全体像 */
  | 'overview'
  /** まとめ・要点 */
  | 'summary'
  /** 時制のイメージ(タイムライン) */
  | 'timeline'
  /** 表・一覧 */
  | 'table'
  /** 文が段階的に伸びる過程 */
  | 'expansion'
  /** 図解・挿絵 */
  | 'illustration'
  /** クイズのヒント・出題数 */
  | 'quiz'
  /** 注意点・間違えやすいところ */
  | 'note'
  /** 発音・読み方 */
  | 'pronunciation'
  /** この機能でできること */
  | 'capability'
  /** あいさつ・お礼 */
  | 'greeting'

/** 回答に添える教材からの引用。 */
export type QaQuote = {
  /** 「例文」「対比」「まとめ」などの見出し */
  label: string
  /** 英文(読み上げボタンが付く) */
  en?: string
  /** 和訳 */
  ja?: string
  /** 補足・注意 */
  note?: string
  /** 日本語の本文(改行は行ごとに表示) */
  text?: string
}

export type QaAnswer = {
  /** マスコットの導入のひとこと */
  lead: string
  quotes: QaQuote[]
  /** 続けて聞ける質問(タップで送信) */
  followups: string[]
}

export type QaEntry = {
  id: string
  intent: QaIntent
  /** 強く効かせたい対象語(英文・用語・ラベル)。質問文にそのまま含まれていれば加点する。 */
  subject?: string
  /** 質問の言い回し候補(教材の語を流し込んだもの)。判定はこの文字列との類似で行う。 */
  questions: string[]
  /** 検索専用の語(英文・本文・英単語)。質問候補としては表示しないが、判定の索引には載せる。 */
  terms?: string[]
  answer: QaAnswer
  /** 同点時の優先度(大きいほど選ばれやすい) */
  priority: number
}

export type ChatReply =
  | {
      kind: 'answer'
      intent: QaIntent
      /** 選ばれたQAの確信度(0〜1目安)。テストとデバッグ用。 */
      confidence: number
      lead: string
      quotes: QaQuote[]
      followups: string[]
    }
  | {
      kind: 'fallback'
      message: string
      suggestions: string[]
    }
