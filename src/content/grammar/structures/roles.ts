// 文の要素(S / V / O / C / M)の表示ルール。
//
// 学習の順序は「まず骨格(S V O C)を見つけ、そのうえで修飾語(M)を外す」。
// そのため、S〜C は骨格の要素として、M は骨格に足される情報として区別して扱う。

import type { SentenceRole } from '../../types'

/** 構造図に出す順序。骨格の要素を先に、修飾語を最後に置く。 */
export const ROLE_ORDER: SentenceRole[] = ['S', 'V', 'O', 'C', 'M']

/** バッジやラベルに使う短い名称。 */
export const ROLE_LABELS: Record<SentenceRole, string> = {
  S: '主語 S',
  V: '動詞 V',
  O: '目的語 O',
  C: '補語 C',
  M: '修飾語 M',
}

/** 役割そのものの意味。凡例と読み上げラベルに使う。 */
export const ROLE_MEANINGS: Record<SentenceRole, string> = {
  S: 'だれが・何が。文が何について述べているか。',
  V: 'どうする・どんな状態か。文の中心。',
  O: '動作の対象。「何を・だれを」にあたる。',
  C: '主語や目的語を説明する。「〜はどんな人・どんな状態か」にあたる。',
  M: 'いつ・どこで・どんなふうに。外しても骨格は壊れない。',
}

/** バッジの読み上げラベル。例: 「主語 S。だれが・何が。」 */
export function roleAccessibleLabel(role: SentenceRole): string {
  return `${ROLE_LABELS[role]}。${ROLE_MEANINGS[role]}`
}

/** 骨格の説明に使う一文。各セクションの導入で共通に使う。 */
export const SKELETON_GUIDE =
  '英文を読むときは、まず**動詞(V)を探し**、次に**主語(S)を探し**ます。そのあとに目的語(O)や補語(C)があるかを見て骨格を決め、最後に修飾語(M)を確かめます。修飾語は外しても文は壊れないので、長い文ほど先に外して骨格を取り出すと構造を見失いません。'
