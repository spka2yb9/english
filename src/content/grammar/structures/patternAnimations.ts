// 「英文の作られ方から学ぶ」ページの2Dアニメーション。
//
// 形式はレッスンの挿絵(animations.ts)と同じ `scene(title, mode, frames)` を使う。
// レッスンではないため LESSON_ANIMATIONS には入れず(全レッスンとの一致をテストで固定している)、
// 同じ再生UI(GrammarAnimation)で表示する。

import type { SentencePattern } from '../../types'
import { scene, type LessonAnimation } from '../animations.ts'

/** 英語の語順を組み立てる過程(旧 u01-l4 のアニメーションを移設)。 */
export const wordOrderAnimation: LessonAnimation = scene('英語の語順を組み立てる', 'sentence', [
  'I|read. :: まず「だれが」→「する」の順に置きます。ここが骨格の土台です。',
  'I|read|a book. :: 動詞のあとに「何を」を足すと、動作の対象が加わります。',
  'I|read|a book|at home. :: 場所は骨格のあとに足します。骨格は S + V + O のままです。',
])

/** 長い文から修飾語を外して骨格を取り出す過程。 */
export const skeletonAnimation: LessonAnimation = scene('修飾語を外して骨格を取り出す', 'sentence', [
  'The young man|standing near the station|gave|me|a beautiful flower|yesterday. :: まず動詞を探します。文の中心は gave です。',
  'The young man|gave|me|a beautiful flower|yesterday. :: 名詞を説明する分詞句を外しました。まだ修飾語が残っています。',
  'The young man|gave|me|a flower. :: 時と形容詞を外すと、S + V + O + O の骨格だけが残ります。',
])

/** 5文型それぞれの骨格。1文型につき3段階で、同じ骨格が保たれることを見せる。 */
export const patternAnimations: Record<SentencePattern, LessonAnimation> = {
  SV: scene('目的語も補語もいらない文', 'sentence', [
    'Birds|fly. :: 動詞 fly は目的語を必要としません。S + V だけで文が成り立ちます。',
    'Birds|fly|in the sky. :: 場所を足しても、骨格は S + V のままです。',
    'Birds|fly|in the sky|every morning. :: 「いつ」を足しても骨格は変わりません。修飾語(M)は外せます。',
  ]),
  SVC: scene('補語が主語を説明する文', 'sentence', [
    'My sister|is|a nurse. :: My sister = a nurse の関係。うしろの語が主語を説明するので補語(C)です。',
    'My sister|is|very kind. :: 補語は名詞でも形容詞でもかまいません。My sister = very kind です。',
    'My sister|became|a famous singer. :: become のような動詞も、うしろには補語(C)が続きます。',
  ]),
  SVO: scene('動作の対象をうしろに置く文', 'sentence', [
    'I|read. :: まず S + V。ここに目的語が必要かどうかを考えます。',
    'I|read|a book. :: 「何を」にあたる a book が目的語(O)です。',
    'Ken|met|his friend|at the station. :: 場所は修飾語(M)。外しても S + V + O の骨格は残ります。',
  ]),
  SVOO: scene('人ともの、目的語が2つの文', 'sentence', [
    'He|gave|a book. :: これでは「だれに」が言えていません。目的語はまだ1つです。',
    'He|gave|me|a book. :: 人が先、ものがうしろ。目的語が2つ並びます。',
    'He|gave|a book|to me. :: to + 人 に置き換えても、伝わる出来事は同じです。',
  ]),
  SVOC: scene('O = C の関係がある文', 'sentence', [
    'They|named|the baby|Emma. :: the baby = Emma の関係。O を説明する語が補語(C)です。',
    'The news|made|everyone|happy. :: everyone = happy。同じ O = C の関係です。',
    'I|found|the book|very useful. :: the book = very useful。= の関係が見つかれば第5文型です。',
  ]),
}
