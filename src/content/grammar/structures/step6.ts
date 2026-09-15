// STEP 6「B1〜B2の文法も英文の構造で見る」の構造データ。
//
// 分詞構文・仮定法のような高度な項目も、骨格の取り方と修飾部分の見方は同じだと示す。
// 特に「元の節がどう圧縮されたか」を並べて見せる。

import type { LessonStructureMap } from './types.ts'

export const step6Structures: LessonStructureMap = {
  // 分詞の後置修飾: 関係詞節が分詞句に圧縮される。
  'u25-l2': {
    blocks: [
      {
        type: 'expansion',
        title: '関係詞節から分詞句へ',
        steps: [
          {
            en: 'The man who is standing there is my uncle.',
            ja: 'そこに立っている男性は私のおじです。',
            focus: 'who is standing there',
            note: '関係代名詞 who と be動詞を使った後置修飾。名詞 The man を後ろから説明します。',
          },
          {
            en: 'The man standing there is my uncle.',
            ja: 'そこに立っている男性は私のおじです。',
            focus: 'standing there',
            note: 'who is が省かれ、分詞句だけが残りました。骨格 The man is my uncle. は変わりません。',
          },
        ],
        caption: '長い説明を短くする道具が分詞です。まず骨格を確かめ、そのあと修飾部分がどの名詞を説明しているかを見ます。',
      },
      {
        type: 'breakdown',
        title: '分詞句も名詞を説明する修飾部分',
        sentence: 'The man standing there is my uncle.',
        ja: 'そこに立っている男性は私のおじです。',
        pattern: 'SVC',
        parts: [
          { text: 'The man', role: 'S', note: '主語の中心' },
          { text: 'standing there', role: 'M', note: 'The man を後ろから説明する分詞句' },
          { text: 'is', role: 'V' },
          { text: 'my uncle.', role: 'C', note: '主語を説明する' },
        ],
        skeleton: 'The man is my uncle.',
        skeletonPattern: 'SVC',
        relation: 'The man = my uncle',
        caption:
          '分詞句を外すと The man is my uncle. の SVC が残ります。後置修飾の分詞句は、関係代名詞節と同じく骨格の外側の修飾部分です。',
      },
    ],
    quiz: [
      {
        id: 'u25-l2-s1',
        prompt: 'The man standing there is my uncle. の骨格を選んでください。',
        sentenceJa: '分詞句を外して考えます。',
        choices: ['The man is my uncle.', 'The man is standing there.', 'standing there is my uncle.', 'The man standing there is.'],
        correctIndex: 0,
        explanation: 'standing there は The man を説明する分詞句(M)です。外すと The man is my uncle. の SVC が残ります。',
        choiceNotes: [
          null,
          '「立っている」という動作の文になっていますが、元の文の骨格ではありません。',
          '主語 The man が抜けています。',
          '補語 my uncle が抜けています。SVC には補語が必要です。',
        ],
        audioEn: 'The man is my uncle.',
      },
      {
        id: 'u25-l2-s2',
        prompt: 'who is standing there の役割を選んでください。',
        sentence: 'The man who is standing there is my uncle.',
        sentenceJa: '説明している名詞を確かめます。',
        choices: ['主語(S)', '動詞(V)', '補語(C)', 'The man を説明する修飾部分(M)'],
        correctIndex: 3,
        explanation:
          'who is standing there は直前の The man を説明する部分で、文の骨格には入りません。だから分詞句に圧縮しても骨格は変わりません。',
        choiceNotes: ['文全体の主語は The man です。', '文全体の動詞は is です。', '補語は my uncle です。', null],
        audioEn: 'The man who is standing there is my uncle.',
      },
    ],
  },

  // 分詞構文: 副詞節が分詞句に圧縮される。
  'u25-l3': {
    blocks: [
      {
        type: 'expansion',
        title: '副詞節が分詞構文に圧縮される',
        steps: [
          {
            en: 'Because I was tired, I went to bed early.',
            ja: '疲れていたので、私は早く寝ました。',
            focus: 'Because I was tired,',
            note: '理由を表す副詞節。主語 I と動詞 was を持つ、ひとつの節です。',
          },
          {
            en: 'Being tired, I went to bed early.',
            ja: '疲れていたので、私は早く寝ました。',
            focus: 'Being tired,',
            note: '節が分詞句に圧縮されました。主節 I went to bed early. と骨格は変わりません。',
          },
        ],
        caption: '分詞構文は、節を短くした修飾部分です。もとの節が何を表していたか(理由・時・条件など)を押さえると意味を取り違えません。',
      },
      {
        type: 'breakdown',
        title: '分詞構文も修飾部分',
        sentence: 'Being tired, I went to bed early.',
        ja: '疲れていたので、私は早く寝ました。',
        pattern: 'SV',
        parts: [
          { text: 'Being tired,', role: 'M', note: '理由を表す分詞構文。文全体を修飾する' },
          { text: 'I', role: 'S' },
          { text: 'went', role: 'V' },
          { text: 'to bed', role: 'M', note: 'どこへ' },
          { text: 'early.', role: 'M', note: 'どんなふうに' },
        ],
        skeleton: 'I went to bed early.',
        skeletonPattern: 'SV',
        caption:
          '分詞構文は文頭に置かれ、後ろの文全体を修飾します。骨格は I + went の第1文型(SV)で、通常の文とまったく同じ作りです。',
      },
    ],
    quiz: [
      {
        id: 'u25-l3-s1',
        prompt: 'Being tired, I went to bed early. の骨格を選んでください。',
        sentenceJa: '分詞構文を外して考えます。',
        choices: ['I went to bed early.', 'Being tired.', 'I was tired.', 'Being tired, I went.'],
        correctIndex: 0,
        explanation: 'Being tired は理由を表す分詞構文(M)で、外すと骨格 I went to bed early. の SV が残ります。',
        choiceNotes: [
          null,
          '分詞構文だけでは文になりません。',
          'もとの副詞節の中身で、この文の骨格ではありません。',
          'went のあとの情報(to bed early)が抜けています。',
        ],
        audioEn: 'I went to bed early.',
      },
      {
        id: 'u25-l3-s2',
        prompt: 'Because I was tired, I went to bed early. を分詞構文にしたとき、圧縮されるのはどの部分ですか。',
        sentenceJa: 'どちらの部分が短くなるかを考えます。',
        choices: [
          '主節の I went to bed early',
          '理由を表す副詞節の Because I was tired',
          '文全体の主語 I',
          '時を表す語句',
        ],
        correctIndex: 1,
        explanation: '分詞構文は副詞節を圧縮したものです。主節 I went to bed early. はそのまま残り、骨格も変わりません。',
        choiceNotes: [
          '主節は圧縮されず、そのまま骨格として残ります。',
          null,
          '節の中にあった I は省かれ、主節の I と一致していると分かります。',
          'この文に時の副詞節はありません。',
        ],
        audioEn: 'Being tired, I went to bed early.',
      },
    ],
  },

  // 仮定法: if節は条件を足す修飾部分で、骨格の作りは普通の文と同じ。
  'u23-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '仮定法でも骨格の作りは同じ',
        sentence: 'If I had studied harder, I would be a doctor now.',
        ja: 'もっと勉強していたら、今ごろ医者になっていたでしょう。',
        pattern: 'SVC',
        parts: [
          { text: 'If I had studied harder,', role: 'M', note: '条件を表す副詞節' },
          { text: 'I', role: 'S' },
          { text: 'would be', role: 'V', note: '助動詞 + be で述語の形' },
          { text: 'a doctor', role: 'C', note: '主語を説明する' },
          { text: 'now.', role: 'M', note: 'いつのことか' },
        ],
        skeleton: 'I would be a doctor now.',
        skeletonPattern: 'SVC',
        relation: 'I = a doctor',
        caption:
          '仮定法という名前がついていても、骨格の探し方は同じです。if節は条件を足す修飾部分(M)で、主節は S + V + C の第2文型。仮定法らしさは動詞の形に表れます。',
      },
    ],
    quiz: [
      {
        id: 'u23-l1-s1',
        prompt: 'If I had studied harder, I would be a doctor now. の骨格を選んでください。',
        sentenceJa: 'if節を外して考えます。',
        choices: ['I would be a doctor now.', 'If I had studied harder.', 'I had studied harder.', 'I would be a doctor.'],
        correctIndex: 0,
        explanation: 'if節は条件を足す副詞節(M)です。外すと I would be a doctor now. の SVC が残ります。',
        choiceNotes: [
          null,
          'if節は条件を表す修飾部分で、それだけでは主節の骨格になりません。',
          'これは条件の節の中身で、文全体の骨格ではありません。',
          'now は時の修飾語(M)なので、外しても骨格にはなりますが、元の文の骨格からは now まで含めて捉えます。',
        ],
        audioEn: 'I would be a doctor now.',
      },
      {
        id: 'u23-l1-s2',
        prompt: 'この文で if I had studied harder の役割を選んでください。',
        sentence: 'If I had studied harder, I would be a doctor now.',
        sentenceJa: '条件の部分が文の中で何をしているか考えます。',
        choices: ['主語(S)', '目的語(O)', '条件を足す修飾部分(M)', '補語(C)'],
        correctIndex: 2,
        explanation: 'if節は主節に対して条件を足す副詞節で、骨格の外側にある修飾部分(M)です。だから外しても主節の骨格は残ります。',
        choiceNotes: [
          '文全体の主語は主節の I です。',
          '目的語ではありません。仮定法の if節は条件を表します。',
          null,
          '補語は a doctor です。',
        ],
        audioEn: 'If I had studied harder, I would be a doctor now.',
      },
    ],
  },
}
