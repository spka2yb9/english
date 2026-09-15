// STEP 5「文と文をつなぐ」の構造データ。
//
// 接続詞・関係詞・副詞節を、独立した暗記事項ではなく
// 「2つの文がどうやって1つになるか」という視点で扱う。

import type { LessonStructureMap } from './types.ts'

export const step5Structures: LessonStructureMap = {
  // 関係代名詞: 2文が1文になり、増えた部分は名詞を説明する修飾部分になる。
  'u14-l1': {
    blocks: [
      {
        type: 'expansion',
        title: '2つの文が1つになる過程',
        steps: [
          { en: 'I know the man.', ja: '私はその男性を知っています。', note: 'まずこの1文が土台です。骨格は S + V + O です。' },
          {
            en: 'The man lives next door.',
            ja: 'その男性は隣に住んでいます。',
            note: '説明したい情報は、そのままだと別の文になります。2文のままでは「どの男性か」がつながりません。',
          },
          {
            en: 'I know the man who lives next door.',
            ja: '私は隣に住んでいる男性を知っています。',
            focus: 'who lives next door',
            note: 'who が the man を受け持ち、2文目が説明として組み込まれました。文全体の骨格は I know the man. のままです。',
          },
        ],
        caption: '関係代名詞節は名詞 the man を説明する部分なので、骨格の外側に足された修飾部分(M)として働きます。',
      },
      {
        type: 'breakdown',
        title: '複雑になった文の骨格',
        sentence: 'I know the man who lives next door.',
        ja: '私は隣に住んでいる男性を知っています。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'know', role: 'V' },
          { text: 'the man', role: 'O' },
          { text: 'who lives next door.', role: 'M', note: 'the man を説明する関係代名詞節' },
        ],
        skeleton: 'I know the man.',
        skeletonPattern: 'SVO',
        caption:
          '説明の節を外すと I know the man. の SVO が残ります。関係代名詞節は「主語 + 動詞」を含みますが、文全体の骨格には入りません。',
      },
    ],
    quiz: [
      {
        id: 'u14-l1-s1',
        prompt: 'I know the man who lives next door. の骨格を選んでください。',
        sentenceJa: '関係代名詞節を外して考えます。',
        choices: [
          'I know the man.',
          'I know who lives next door.',
          'The man lives next door.',
          'I know the man lives next door.',
        ],
        correctIndex: 0,
        explanation: 'who lives next door は the man を説明する関係代名詞節(M)です。外すと I know the man. の SVO が残ります。',
        choiceNotes: [
          null,
          'who lives next door は the man を説明する部分なので、これだけ残しても骨格になりません。',
          'この節は the man を説明しており、文全体の骨格ではありません。',
          '関係代名詞 who は節の中の主語です。I know の目的語は the man ひとつです。',
        ],
        audioEn: 'I know the man who lives next door.',
      },
      {
        id: 'u14-l1-s2',
        prompt: 'who lives next door の働きを選んでください。',
        sentenceJa: '節が何を説明しているかに注目します。',
        choices: ['主語(S)', '目的語(O)', '補語(C)', 'the man を説明する修飾部分(M)'],
        correctIndex: 3,
        explanation: '関係代名詞節は直前の名詞 the man を説明します。文の骨格には入らず、修飾部分(M)として働きます。',
        choiceNotes: [
          '文全体の主語は I です。',
          '目的語は the man です。',
          '補語ではありません。C なら the man = who lives next door のような関係になります。',
          null,
        ],
        audioEn: 'I know the man who lives next door.',
      },
    ],
  },

  // 接続詞: 副詞節は理由や譲歩を足す修飾部分で、骨格の外側にある。
  'u16-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '理由の because節は骨格の外側',
        sentence: 'I stayed home because it was raining.',
        ja: '雨が降っていたので、私は家にいました。',
        pattern: 'SV',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'stayed', role: 'V' },
          { text: 'home', role: 'M', note: '「家に」を表す語' },
          { text: 'because it was raining.', role: 'M', note: '理由を足す副詞節' },
        ],
        skeleton: 'I stayed home.',
        skeletonPattern: 'SV',
        caption:
          'because 以下は理由を足す副詞節で、文の骨格には入りません。骨格は I + stayed の第1文型(SV)です。節の中に「主語 + 動詞」があっても、文全体の要素は増えません。',
      },
      {
        type: 'breakdown',
        title: '譲歩の although節も同じ',
        sentence: 'Although she was tired, she finished her homework.',
        ja: '疲れていたけれど、彼女は宿題を終えました。',
        pattern: 'SVO',
        parts: [
          { text: 'Although she was tired,', role: 'M', note: '譲歩(〜だけれど)を足す副詞節' },
          { text: 'she', role: 'S' },
          { text: 'finished', role: 'V' },
          { text: 'her homework.', role: 'O' },
        ],
        skeleton: 'She finished her homework.',
        skeletonPattern: 'SVO',
        caption:
          '譲歩も理由と同じく副詞節です。文頭に置かれていても骨格の外側にあり、骨格は she + finished + her homework の SVO です。',
      },
    ],
    quiz: [
      {
        id: 'u16-l1-s1',
        prompt: 'I stayed home because it was raining. の骨格を選んでください。',
        sentenceJa: 'because節を外して考えます。',
        choices: ['I stayed home.', 'I stayed because it was raining.', 'because it was raining.', 'I stayed home because.'],
        correctIndex: 0,
        explanation: 'because 以下は理由を足す副詞節(M)なので、外しても骨格は壊れません。残るのは I stayed home. の SV です。',
        choiceNotes: [
          null,
          'because 以下は修飾部分なので、これだけ残しても骨格になりません。',
          '主語 I と動詞 stayed が抜けています。',
          'because だけを残すことはできません。接続詞には続く節が必要です。',
        ],
        audioEn: 'I stayed home.',
      },
      {
        id: 'u16-l1-s2',
        prompt: '文全体の主語(S)はどれですか。',
        sentence: 'Although she was tired, she finished her homework.',
        sentenceJa: '疲れていたけれど、彼女は宿題を終えました。',
        choices: ['Although', 'she', 'her homework', 'tired'],
        correctIndex: 1,
        explanation:
          '文全体の骨格は she finished her homework です。Although 以下は譲歩を表す副詞節で、その中の she は文全体の主語ではありません。',
        choiceNotes: [
          'Although は譲歩の副詞節を導く接続詞です。',
          null,
          'her homework は目的語(O)です。',
          'tired は Although節の中で she を説明する補語です。',
        ],
        audioEn: 'Although she was tired, she finished her homework.',
      },
    ],
  },
}
