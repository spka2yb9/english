// イングバードのつぶやき(励まし・学習のコツ・英会話フレーズ)の型。
// 教材本文(grammar/vocabulary)とは独立した、ホーム専用の小さな会話集。

import type { IngbirdMood } from '../../services/studyDays'

/** つぶやきの種類。励まし・コツ・フレーズの3つを順番に混ぜて出す。 */
export type TalkKind = 'encourage' | 'tip' | 'phrase'

export type TalkLine = {
  /** 一意なID。抽選の袋と重複検出に使う。 */
  id: string
  kind: TalkKind
  /** この話をするときの気分。 */
  mood: IngbirdMood
  /** 画面に出す本文。フレーズのときは英文。 */
  text: string
  /** フレーズの和訳。 */
  ja?: string
  /** フレーズの使いどころ・ひとこと解説。 */
  note?: string
  /** フレーズの場面ラベル。「あいさつ」など。 */
  scene?: string
  /** 自動で読み上げる文とロケール。無いときは本文を日本語として読む。 */
  speech?: { text: string; locale: string }
}

/** フレーズ集の1場面。 */
export type PhraseScene = {
  label: string
  /** [英文, 和訳, 使いどころ] の組。 */
  phrases: readonly (readonly [string, string, string])[]
}
