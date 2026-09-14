// 5文型のデータモデルと表示用ラベル。
//
// 文型は「動詞のあとに何が続くか」で決まる。判定は原則として平叙文で行い、
// 次の規約で機械的に決められるようにする(全例文に1つだけ付く)。
//
// - 疑問文・感嘆文: 平叙文に戻して判定する(Are you tired? → SVC)。
// - 命令文: 主語 You を補って判定する(Open the door. → SVO)。
// - 受動態: be + 過去分詞を1つの動詞とみなし、目的語を取らないので SV。
// - there is / are: 第1文型 SV。
// - 強調構文 It is X that ...: S = It, C = X の第2文型 SVC。
// - that節・wh節・to不定詞・動名詞は、名詞の席(S / O / C)に入るなら1要素として数える。
// - 場所・時間・by句などの副詞(句)は要素に数えない。
// - 句動詞は1つの動詞として扱う。

import type { SentencePattern } from '../../types'

/** 例文1文の文型と、その短い日本語注記。 */
export type PatternEntry = {
  pattern: SentencePattern
  /** 例文の文型についての短い注記(日本語)。 */
  note: string
}

/**
 * 例文の英文そのものをキーにした文型表。
 * 教材ファイル(既存のレッスン定義)は書き換えず、合成時にここから付与する。
 */
export type PatternMap = Record<string, PatternEntry>

/** セクションごとの「文型の視点」本文。レッスン定義を書き換えず合成時に差し込む。 */
export type PatternFocusMap = Record<string, string>

/** 表示順・本文中の並び順。 */
export const PATTERN_ORDER: SentencePattern[] = ['SV', 'SVC', 'SVO', 'SVOO', 'SVOC']

/** バッジやラベルに使う短い名称。 */
export const PATTERN_LABELS: Record<SentencePattern, string> = {
  SV: '第1文型 SV',
  SVC: '第2文型 SVC',
  SVO: '第3文型 SVO',
  SVOO: '第4文型 SVOO',
  SVOC: '第5文型 SVOC',
}

/** 文型そのものの意味。凡例や aria-label に使う。 */
export const PATTERN_MEANINGS: Record<SentencePattern, string> = {
  SV: 'S + V。目的語も補語も要らない。',
  SVC: 'S + V + C。補語(C)が主語を説明する(S = C)。',
  SVO: 'S + V + O。動詞のあとに動作の対象(目的語)が続く。',
  SVOO: 'S + V + O + O。人 → もの の2つの目的語を取る。',
  SVOC: 'S + V + O + C。目的語(O)と補語(C)が O = C の関係になる。',
}
