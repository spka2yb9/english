// 英文法ページの学習導線。「文法事項の一覧」ではなく「英文の作られ方」の順で並べる。
//
// 各ステップは既存のレッスンへリンクする。新しいルーティングは増やさず、
// 既存のユニット・セクションをこの流れの中に位置づける。

import type { LessonBlock } from '../types'

export type RoadmapStep = {
  /** 安定したID。表示順は配列の順。 */
  id: string
  /** 1〜7。表示に使う。 */
  number: number
  title: string
  /** この段階で何を学ぶかを1〜2文で。 */
  lead: string
  /** この段階で身につけること。 */
  points: string[]
  /** 対応する既存レッスンのID。 */
  lessonIds: string[]
  /** その段階を象徴する構造図(任意)。 */
  blocks?: LessonBlock[]
}

export const grammarRoadmap: RoadmapStep[] = [
  {
    id: 'skeleton',
    number: 1,
    title: '文の骨格を見つける',
    lead: '英文は「主語 + 動詞 + (目的語・補語)」という骨格からできています。5文型は、この骨格を確かめるための道具です。このページの前半で、S / V / O / C / M の意味と5文型の見方を確かめました。',
    points: [
      '主語(S)と動詞(V)を文から見つける',
      '目的語(O)と補語(C)を区別する(O = C の関係があるかで見る)',
      '修飾語(M)を外して、残る骨格を確かめる',
    ],
    lessonIds: ['u01-l1', 'u01-l2', 'u04-l1'],
    blocks: [
      {
        type: 'breakdown',
        title: '骨格と、そこから外せる部分',
        sentence: 'She made me happy.',
        ja: '彼女は私を幸せにしました。',
        pattern: 'SVOC',
        parts: [
          { text: 'She', role: 'S' },
          { text: 'made', role: 'V' },
          { text: 'me', role: 'O', note: '動作の対象' },
          { text: 'happy.', role: 'C', note: 'me を説明する' },
        ],
        relation: 'me = happy',
        caption:
          'O(me)とC(happy)の間に me = happy の関係があるので、これは補語(C)です。もし happy の代わりに yesterday が来れば、それは動詞を修飾するだけの修飾語(M)になり、SVO に変わります。',
      },
    ],
  },
  {
    id: 'verb',
    number: 2,
    title: '動詞の変化で意味が変わる',
    lead: '文の中心は動詞です。時制・進行形・完了形・助動詞・受動態は、どれも「動詞の部分」を変えて意味を変えます。骨格はそのままです。',
    points: [
      '動詞が何語になっても、ひとまとまりの動詞として捉える',
      '同じ骨格で、意味だけがどう変わるかを確かめる',
      '受動態では目的語が主語の席へ移り、骨格自体が変わることを知る',
    ],
    lessonIds: ['u02-l1', 'u02-l3', 'u11-l1', 'u13-l1'],
    blocks: [
      {
        type: 'expansion',
        title: '動詞の部分だけが変わる',
        steps: [
          { en: 'I play tennis.', ja: '私はテニスをします。', note: '骨格は S + V + O。まずこの形が土台です。' },
          {
            en: 'I am playing tennis.',
            ja: '私はテニスをしています。',
            focus: 'am playing',
            note: '進行形。動詞が2語になっても、ひとまとまりの動詞です。',
          },
          {
            en: 'I have played tennis.',
            ja: '私はテニスをしたことがあります。',
            focus: 'have played',
            note: '完了形。過去と今をつなぐ形に変わります。',
          },
          {
            en: 'I can play tennis.',
            ja: '私はテニスができます。',
            focus: 'can play',
            note: '助動詞が加わり、能力や可能性を表します。',
          },
          {
            en: 'Tennis is played by me.',
            ja: 'テニスは私によって行われます。',
            focus: 'is played',
            note: '受動態。目的語だった Tennis が主語の席へ移るので、ここだけは骨格も変わります。',
          },
        ],
        caption:
          '上の4文はどれも骨格が I + play + tennis の SVO です。変わったのは動詞の部分で、そこが文全体の意味を動かしています。',
      },
    ],
  },
  {
    id: 'modifier',
    number: 3,
    title: '骨格に情報を足す',
    lead: '形容詞・副詞・前置詞句・to不定詞・分詞は、骨格の内側に入るか、外側から情報を足すかで役割が分かれます。足しても骨格は変わらないことを確かめます。',
    points: [
      '修飾語を足しても骨格が変わらないことを確かめる',
      '名詞の前か後ろかで、同じ形の語句の役割が変わることを知る',
      'to不定詞が名詞の席に入る場合と、修飾語になる場合を区別する',
    ],
    lessonIds: ['u05-l1', 'u05-l2', 'u08-l2', 'u10-l1'],
    blocks: [
      {
        type: 'expansion',
        title: 'I saw a dog. を少しずつ長くする',
        steps: [
          { en: 'I saw a dog.', ja: '私は犬を見かけました。', note: '骨格は S + V + O。ここから足していきます。' },
          {
            en: 'I saw a big dog.',
            ja: '私は大きな犬を見かけました。',
            focus: 'big',
            note: '形容詞は名詞とセットになり、目的語の中に入ります。',
          },
          {
            en: 'I saw a dog in the park.',
            ja: '私は公園で犬を見かけました。',
            focus: 'in the park',
            note: '前置詞句が「どこで」を足します。骨格の外側です。',
          },
          {
            en: 'I saw a dog running in the park.',
            ja: '私は公園で走っている犬を見かけました。',
            focus: 'running in the park',
            note: '分詞が犬の様子を説明します。これも修飾部分です。',
          },
          {
            en: 'I wanted to see the dog.',
            ja: '私はその犬に会いたかったのです。',
            focus: 'wanted to see',
            note: '文の中心が wanted に移りました。to see the dog は目的語の席に入ります。',
          },
        ],
        caption: '足した部分はすべて修飾語(M)。中心になる骨格は I saw a dog. のままです。文が長くなっても、まず骨格を探す習慣をつけましょう。',
      },
    ],
  },
  {
    id: 'phrase',
    number: 4,
    title: '句を使う(名詞句・形容詞句・副詞句)',
    lead: '1語の名詞が、冠詞・形容詞・前置詞句といっしょに「句」になって、S や O の席に入ります。席は広がっても、文の中での役割は同じです。',
    points: [
      '名詞句が S / O の席に入ることを確かめる',
      '前置詞句が動詞を修飾するか、名詞を説明するかを見分ける',
      '動名詞句も名詞の席に入ることを知る',
    ],
    lessonIds: ['u03-l3', 'u08-l2', 'u10-l2'],
    blocks: [
      {
        type: 'breakdown',
        title: '長い名詞句も要素としては1つ',
        sentence: 'I bought a very expensive new camera.',
        ja: '私はとても高価な新しいカメラを買いました。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'bought', role: 'V' },
          { text: 'a very expensive new camera.', role: 'O', note: '冠詞 + 副詞 + 形容詞2つ + 名詞で1つの名詞句' },
        ],
        caption:
          '目的語の席に5語が入っていますが、数えるべき要素は目的語1つです。文型は SVO のまま。句は「席の中身」が長くなっただけです。',
      },
    ],
  },
  {
    id: 'clause',
    number: 5,
    title: '節を使う(名詞節・形容詞節・副詞節)',
    lead: '「主語 + 動詞」を含むまとまりが節です。名詞の席に入れば名詞節、名詞を説明すれば形容詞節、文全体に情報を足せば副詞節になります。長さではなく働きで分類します。',
    points: [
      '節が名詞の席に入る(名詞節)ことを確かめる',
      '名詞を説明する節(形容詞節)は骨格の外側にあると知る',
      '理由・時・条件を表す節(副詞節)も骨格の外側にあると知る',
    ],
    lessonIds: ['u29-l1', 'u14-l1', 'u16-l1'],
    blocks: [
      {
        type: 'breakdown',
        title: '節が主語の席に入ることもある',
        sentence: 'What he said was true.',
        ja: '彼が言ったことは本当でした。',
        pattern: 'SVC',
        parts: [
          { text: 'What he said', role: 'S', note: '名詞節が主語の席に' },
          { text: 'was', role: 'V' },
          { text: 'true.', role: 'C', note: '主語を説明する' },
        ],
        relation: 'What he said = true',
        caption:
          '「主語 + 動詞」を含むまとまりが、まるごと主語の席に入っています。文全体の動詞は was です。節の中の動詞 said を文全体の動詞と取り違えないようにします。',
      },
    ],
  },
  {
    id: 'connect',
    number: 6,
    title: '文と文をつなぐ',
    lead: '接続詞・関係詞・間接疑問・間接話法は、2つの文を1つにまとめる道具です。増えた部分が骨格に入るのか、外側に付くのかを見ます。',
    points: [
      '等しい関係の接続詞は、骨格を対等につなぐ',
      '関係詞節は名詞を説明する修飾部分になる',
      '間接疑問・間接話法は、節になって文の一部に組み込まれる',
    ],
    lessonIds: ['u16-l1', 'u14-l1', 'u19-l4'],
    blocks: [
      {
        type: 'breakdown',
        title: '伝えた内容がまるごと目的語になる',
        sentence: 'She said that she was busy that day.',
        ja: '彼女はその日は忙しいと言いました。',
        pattern: 'SVO',
        parts: [
          { text: 'She', role: 'S' },
          { text: 'said', role: 'V' },
          { text: 'that she was busy that day.', role: 'O', note: '伝えた内容の節が目的語の席に' },
        ],
        caption:
          '誰かの言葉を伝えるときも、伝えた内容の節がまるごと目的語(O)の席に入ります。文の骨格は She + said の SVO です。',
      },
    ],
  },
  {
    id: 'long-sentence',
    number: 7,
    title: '複雑な英文を読む',
    lead: 'ここまでの手順を、長い文でも使えるようにします。読む順番を固定して、構造を見失わないようにしましょう。',
    points: [
      'まず動詞(V)を探し、次に主語(S)を探す',
      '目的語・補語の有無で文の骨格を決める',
      '修飾部分をいったん外してから、句・節の役割を確かめる',
    ],
    lessonIds: ['u25-l2', 'u25-l3', 'u30-l2'],
    blocks: [
      {
        type: 'breakdown',
        title: '修飾部分を外すと骨格が見える',
        sentence: 'The woman who lives next door to us has been teaching English at a local high school for ten years.',
        ja: '私たちの隣に住んでいる女性は、地元の高校で10年間英語を教え続けています。',
        pattern: 'SVO',
        parts: [
          { text: 'The woman', role: 'S', note: '主語の中心' },
          { text: 'who lives next door to us', role: 'M', note: 'どの女性かを説明する関係代名詞節' },
          { text: 'has been teaching', role: 'V', note: 'has been + -ing でひとまとまりの動詞' },
          { text: 'English', role: 'O' },
          { text: 'at a local high school', role: 'M', note: 'どこで' },
          { text: 'for ten years.', role: 'M', note: 'どれだけの期間' },
        ],
        skeleton: 'The woman has been teaching English.',
        skeletonPattern: 'SVO',
        caption:
          '修飾部分を3つ外すと、The woman has been teaching English. の SVO だけが残ります。どんなに長い文も、この手順で骨格を取り出せます。',
      },
    ],
  },
]
