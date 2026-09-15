// STEP 4「句と節」の構造データ。
//
// 単語 → 句 → 節 と長くなっても、文の中での働き(席)が同じなら同じ要素として扱う。
// 「長いか短いか」ではなく「何の役割をしているか」で分類する視点を入れる。

import type { LessonStructureMap } from './types.ts'

export const step4Structures: LessonStructureMap = {
  // 動名詞: 句が S や O の席に入る。
  'u10-l2': {
    blocks: [
      {
        type: 'breakdown',
        title: '動名詞は「〜すること」で目的語の席に入る',
        sentence: 'I enjoy playing tennis.',
        ja: '私はテニスをすることが好きです。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'enjoy', role: 'V' },
          { text: 'playing tennis.', role: 'O', note: '動名詞句。enjoy の目的語' },
        ],
        caption:
          'playing tennis は動詞の形をした語から始まりますが、文全体の動詞は enjoy です。playing tennis は「何を楽しむのか」を表す目的語(O)の席にあります。',
      },
      {
        type: 'breakdown',
        title: '主語の席にも入る',
        sentence: 'Playing tennis is fun.',
        ja: 'テニスをすることは楽しいです。',
        pattern: 'SVC',
        parts: [
          { text: 'Playing tennis', role: 'S', note: '動名詞句が主語の席に' },
          { text: 'is', role: 'V' },
          { text: 'fun.', role: 'C', note: '主語を説明する' },
        ],
        relation: 'Playing tennis = fun',
        caption:
          '動名詞句は長くても、S の席に1つのかたまりとして入ります。席が決まれば、あとは骨格(S + V + C)だけを見れば文全体の形が見えます。',
      },
    ],
    quiz: [
      {
        id: 'u10-l2-s1',
        prompt: 'Playing tennis is fun. の主語(S)を選んでください。',
        sentenceJa: '句全体で主語になることがあります。',
        choices: ['Playing', 'tennis', 'Playing tennis', 'fun'],
        correctIndex: 2,
        explanation: 'Playing tennis がひとまとまりで主語(S)です。1語ずつではなく、句全体が主語の席に入ります。',
        choiceNotes: [
          'Playing だけでは主語のまとまりを作りません。',
          'tennis だけでは主語になりません。',
          null,
          'fun は主語を説明する補語(C)です。',
        ],
        audioEn: 'Playing tennis is fun.',
      },
      {
        id: 'u10-l2-s2',
        prompt: 'I enjoy playing tennis. で playing tennis の役割を選んでください。',
        sentenceJa: '「何を楽しむのか」にあたる部分です。',
        choices: ['主語(S)', '目的語(O)', '補語(C)', '修飾語(M)'],
        correctIndex: 1,
        explanation: '動名詞句 playing tennis は動詞 enjoy の目的語(O)の席にあります。「何を楽しむのか」にあたる部分です。',
        choiceNotes: [
          '主語は I です。',
          null,
          '補語なら I = playing tennis の関係が成り立つはずですが、成り立ちません。',
          'enjoy の対象を表しているので、修飾語ではありません。',
        ],
        audioEn: 'I enjoy playing tennis.',
      },
    ],
  },

  // that節: 「主語 + 動詞」を含む節も、まるごと1つの名詞として扱う。
  'u29-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '節が目的語の席に入る',
        sentence: 'I think that he is right.',
        ja: '彼は正しいと思います。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'think', role: 'V' },
          { text: 'that he is right.', role: 'O', note: 'that節全体で目的語。that は節の始まりを示す印' },
        ],
        caption:
          'that のあとには「he is right」という別の主語・動詞の組が入っていますが、文全体の動詞は think です。節はまるごと1つの目的語(O)として扱います。',
      },
    ],
    quiz: [
      {
        id: 'u29-l1-s1',
        prompt: 'I think that he is right. で、文全体の動詞(V)を選んでください。',
        sentenceJa: '節の中の動詞と混同しないようにします。',
        choices: ['think', 'is', 'that', 'right'],
        correctIndex: 0,
        explanation: '文全体の動詞は think です。that節の中の is は節の中の動詞で、文全体の V ではありません。',
        choiceNotes: [
          null,
          'is は that節の中の動詞です。文全体の V ではありません。',
          'that は節の始まりを示す語で、動詞ではありません。',
          'right は that節の中で he を説明する補語です。',
        ],
        audioEn: 'I think that he is right.',
      },
      {
        id: 'u29-l1-s2',
        prompt: 'that he is right の役割を選んでください。',
        sentenceJa: '「何を思うのか」にあたる部分です。',
        choices: ['主語(S)', '目的語(O)', '修飾語(M)', '文全体の動詞(V)'],
        correctIndex: 1,
        explanation: 'that he is right は動詞 think の目的語(O)の席に入る名詞節です。「何を思うのか」にあたります。',
        choiceNotes: [
          '文の主語は I です。',
          null,
          '修飾語ではなく、think の対象を表す目的語です。',
          '文全体の動詞は think です。',
        ],
        audioEn: 'I think that he is right.',
      },
    ],
  },

  // wh節: 語・句・節の見た目の違いより、席が同じことを重視する。
  'u29-l2': {
    blocks: [
      {
        type: 'breakdown',
        title: '1語の名詞が目的語',
        sentence: 'I know him.',
        ja: '私は彼を知っています。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'know', role: 'V' },
          { text: 'him.', role: 'O', note: '1語の代名詞' },
        ],
      },
      {
        type: 'breakdown',
        title: '名詞句が目的語',
        sentence: 'I know the answer.',
        ja: '私はその答えを知っています。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'know', role: 'V' },
          { text: 'the answer.', role: 'O', note: '冠詞 + 名詞の句' },
        ],
      },
      {
        type: 'breakdown',
        title: '節が目的語',
        sentence: 'I know what he wants.',
        ja: '私は彼が何を欲しがっているか知っています。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'know', role: 'V' },
          { text: 'what he wants.', role: 'O', note: 'wh節。この文全体の動詞は know' },
        ],
        caption:
          'him(1語)、the answer(句)、what he wants(節)は見た目も長さも違いますが、3つとも動詞 know の目的語(O)です。文型は3文とも SVO です。文の要素は「長さ」ではなく「文の中で何をしているか」で決まります。',
      },
    ],
    quiz: [
      {
        id: 'u29-l2-s1',
        prompt: 'I know him. I know the answer. I know what he wants. の3文に共通することはどれですか。',
        sentenceJa: '3文を並べて、構造の共通点を探します。',
        choices: [
          'どの文も目的語の語数が同じ',
          'どの文も S + V + O で、O の見た目だけが違う',
          'どの文も SVC(第2文型)である',
          'どの文も know のあとに節が続く',
        ],
        correctIndex: 1,
        explanation:
          'him(代名詞1語)、the answer(名詞句)、what he wants(節)と見た目は違いますが、どれも動詞 know の目的語(O)です。3文とも SVO です。',
        choiceNotes: [
          '語数はそれぞれ違います。長さではなく働きで見ます。',
          null,
          'SVC なら補語が必要ですが、3文とも補語はありません。',
          '節が続くのは I know what he wants. だけです。あとの2文は語と句です。',
        ],
        audioEn: 'I know what he wants.',
      },
      {
        id: 'u29-l2-s2',
        prompt: 'I know what he wants. で文全体の目的語(O)はどれですか。',
        sentenceJa: '節の一部ではなく、まとまりで考えます。',
        choices: ['what', 'he', 'what he wants', 'know'],
        correctIndex: 2,
        explanation: 'what he wants は「彼が何を欲しがっているか」というひとかたまりで、know の目的語(O)です。',
        choiceNotes: [
          'what は節の中で目的語の働きをする語で、O の全体ではありません。',
          'he は節の中の主語です。',
          null,
          'know は文全体の動詞(V)です。',
        ],
        audioEn: 'I know what he wants.',
      },
    ],
  },
}
