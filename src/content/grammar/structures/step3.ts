// STEP 3「骨格に情報を足す」の構造データ。
//
// 形容詞・副詞・前置詞句・to不定詞が、骨格の内側に入るのか外側に付くのかを分けて見る。
// 「文が長くなっても骨格は変わらない」ことを体感させる。

import type { LessonStructureMap } from './types.ts'

export const step3Structures: LessonStructureMap = {
  // 形容詞: 名詞の前に入るか、be動詞のあとで補語になるか。
  'u05-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '名詞の前の形容詞は目的語の一部',
        sentence: 'My sister has a big dog.',
        ja: '姉は大きな犬を飼っています。',
        pattern: 'SVO',
        parts: [
          { text: 'My sister', role: 'S' },
          { text: 'has', role: 'V' },
          { text: 'a big dog.', role: 'O', note: 'a big dog 全体で目的語。big は dog を説明する形容詞' },
        ],
        caption:
          '形容詞は単独で目的語になるのではなく、名詞とセットで「大きい犬」という目的語のかたまりを作ります。目的語(O)は a big dog の3語で1つです。',
      },
      {
        type: 'breakdown',
        title: 'be動詞のあとの形容詞は補語',
        sentence: 'My dog is very big.',
        ja: '私の犬はとても大きいです。',
        pattern: 'SVC',
        parts: [
          { text: 'My dog', role: 'S' },
          { text: 'is', role: 'V' },
          { text: 'very big.', role: 'C', note: '主語 My dog を説明する' },
        ],
        relation: 'My dog = very big',
        caption:
          '同じ big でも、be動詞のあとに置くと主語を説明する補語(C)になります。My dog = very big の関係が成り立ちます。名詞の前か、be動詞のあとかで役割が変わります。',
      },
    ],
    quiz: [
      {
        id: 'u05-l1-s1',
        prompt: 'My dog is very big. の very big の役割を選んでください。',
        sentenceJa: '「My dog = very big」の関係があるかで判断します。',
        choices: ['主語(S)', '目的語(O)', '補語(C)', '修飾語(M)'],
        correctIndex: 2,
        explanation: 'be動詞 is のあとの very big は主語 My dog を説明する補語(C)です。My dog = very big の関係が成り立ちます。',
        choiceNotes: [
          '主語は My dog です。',
          '目的語ではありません。be動詞のあとに目的語は続きません。',
          null,
          'very big は主語を説明しており、外すと意味が伝わりません。',
        ],
        audioEn: 'My dog is very big.',
      },
      {
        id: 'u05-l1-s2',
        prompt: 'a big dog のように名詞の前に置かれた big は、文の中でどのように働いていますか。',
        sentence: 'My sister has a big dog.',
        sentenceJa: '姉は大きな犬を飼っています。',
        choices: ['単独で補語(C)になる', '名詞 dog を説明して、目的語全体を作る', '文全体を修飾する副詞になる', '動詞 has を修飾する'],
        correctIndex: 1,
        explanation: '形容詞は名詞とセットになって1つのかたまりを作ります。この文では a big dog 全体が目的語(O)です。',
        choiceNotes: [
          '補語は be動詞や become のあとに置かれ、主語や目的語を説明します。',
          null,
          'これは目的語の一部で、文全体を修飾しているわけではありません。',
          '動詞を修飾するのは副詞の働きです。',
        ],
        audioEn: 'My sister has a big dog.',
      },
    ],
  },

  // 副詞: 動詞を修飾する M で、足しても骨格は変わらない。
  'u05-l2': {
    blocks: [
      {
        type: 'breakdown',
        title: '副詞は動詞を修飾する修飾語',
        sentence: 'She sings beautifully.',
        ja: '彼女は美しく歌います。',
        pattern: 'SV',
        parts: [
          { text: 'She', role: 'S' },
          { text: 'sings', role: 'V' },
          { text: 'beautifully.', role: 'M', note: '動詞 sings を修飾する' },
        ],
        skeleton: 'She sings.',
        skeletonPattern: 'SV',
        caption:
          'beautifully は動詞 sings を修飾する副詞で、骨格の外側にある修飾語(M)です。外しても She sings. で文が成り立ちます。',
      },
      {
        type: 'expansion',
        title: '修飾語を足しても骨格は変わらない',
        steps: [
          { en: 'She sings.', ja: '彼女は歌います。', note: 'これが骨格。S + V の第1文型です。' },
          {
            en: 'She sings beautifully.',
            ja: '彼女は美しく歌います。',
            focus: 'beautifully',
            note: '副詞が動詞を修飾する修飾語(M)として加わりました。',
          },
          {
            en: 'She sings beautifully in the concert hall.',
            ja: '彼女はコンサートホールで美しく歌います。',
            focus: 'in the concert hall',
            note: '場所を足す前置詞句も修飾語(M)です。',
          },
          {
            en: 'She sings beautifully in the concert hall every year.',
            ja: '彼女は毎年、コンサートホールで美しく歌います。',
            focus: 'every year',
            note: '時を足しても、骨格は最初の She sings. のままです。',
          },
        ],
        caption: '情報が増えても骨格は1つも変わりません。長い文を見たら、まずこの骨格を探します。',
      },
    ],
    quiz: [
      {
        id: 'u05-l2-s1',
        prompt: 'She sings beautifully. で beautifully の役割を選んでください。',
        sentenceJa: 'beautifully が何を説明しているかを考えます。',
        choices: ['主語(S)', '動詞(V)', '補語(C)', '修飾語(M)'],
        correctIndex: 3,
        explanation: 'beautifully は動詞 sings を修飾する副詞で、骨格に含まれない修飾語(M)です。外しても She sings. で文が成り立ちます。',
        choiceNotes: [
          '主語は She です。',
          '動詞は sings です。beautifully はその動詞を説明する側です。',
          '補語なら She = beautifully の関係が成り立つはずですが、成り立ちません。',
          null,
        ],
        audioEn: 'She sings beautifully.',
      },
      {
        id: 'u05-l2-s2',
        prompt: '「姉は毎週日曜日に図書館で英語を勉強します」の骨格を選んでください。',
        sentence: 'My sister studies English at the library every Sunday.',
        sentenceJa: '修飾語を外した形を考えます。',
        choices: [
          'My sister studies English.',
          'My sister studies at the library.',
          'studies English every Sunday.',
          'My sister studies English every Sunday.',
        ],
        correctIndex: 0,
        explanation: 'at the library も every Sunday も修飾語(M)です。外すと主語 + 動詞 + 目的語の SVO が残ります。',
        choiceNotes: [
          null,
          '場所の at the library は修飾語なので、これだけ残しても骨格ではありません。',
          '主語 My sister が抜けています。',
          'every Sunday は時の修飾語(M)なので外せます。',
        ],
        audioEn: 'My sister studies English at the library every Sunday.',
      },
    ],
  },

  // 前置詞句: 動詞を修飾するか、名詞を説明するか。
  'u08-l2': {
    blocks: [
      {
        type: 'breakdown',
        title: '前置詞句は「どこで」を足す修飾語',
        sentence: 'We had lunch at a small restaurant.',
        ja: '私たちは小さなレストランで昼食をとりました。',
        pattern: 'SVO',
        parts: [
          { text: 'We', role: 'S' },
          { text: 'had', role: 'V' },
          { text: 'lunch', role: 'O' },
          { text: 'at a small restaurant.', role: 'M', note: 'どこで' },
        ],
        skeleton: 'We had lunch.',
        skeletonPattern: 'SVO',
        caption:
          'at a small restaurant は「どこで」を足す前置詞句で、骨格の外側にある修飾語(M)です。外しても We had lunch. の SVO が残ります。',
      },
      {
        type: 'breakdown',
        title: '名詞の後ろの前置詞句は名詞を説明する',
        sentence: 'The man in the blue shirt is my teacher.',
        ja: '青いシャツを着た男性は私の先生です。',
        pattern: 'SVC',
        parts: [
          { text: 'The man', role: 'S', note: '主語の中心' },
          { text: 'in the blue shirt', role: 'M', note: 'The man を後ろから説明する' },
          { text: 'is', role: 'V' },
          { text: 'my teacher.', role: 'C', note: '主語を説明する' },
        ],
        skeleton: 'The man is my teacher.',
        skeletonPattern: 'SVC',
        relation: 'The man = my teacher',
        caption:
          '同じ前置詞句でも、動詞のそばに置けば動詞を修飾し、名詞の後ろに置けばその名詞を説明します。どちらも骨格の外側の修飾部分(M)です。だから外すと The man is my teacher. の SVC が残ります。',
      },
    ],
    quiz: [
      {
        id: 'u08-l2-s1',
        prompt: 'The man in the blue shirt is my teacher. の骨格を選んでください。',
        sentenceJa: '前置詞句を外して考えます。',
        choices: ['The man is my teacher.', 'The man in the blue shirt is.', 'in the blue shirt is my teacher.', 'The man is in the blue shirt.'],
        correctIndex: 0,
        explanation: 'in the blue shirt は The man を説明する前置詞句(M)です。外すと The man is my teacher. の SVC が残ります。',
        choiceNotes: [
          null,
          '補語 my teacher が抜けています。SVC には補語が必要です。',
          '主語 The man が抜けています。',
          'in the blue shirt は修飾語で、補語ではありません。',
        ],
        audioEn: 'The man is my teacher.',
      },
      {
        id: 'u08-l2-s2',
        prompt: 'We had lunch at a small restaurant. で、骨格に含まれない部分を選んでください。',
        sentenceJa: '外しても文が壊れない部分を探します。',
        choices: ['We', 'had', 'lunch', 'at a small restaurant'],
        correctIndex: 3,
        explanation: 'at a small restaurant は「どこで」を足す前置詞句で、修飾語(M)です。外しても We had lunch. で骨格は残ります。',
        choiceNotes: [
          'We は主語(S)で骨格に必要です。',
          'had は動詞(V)で文の中心です。',
          'lunch は目的語(O)で骨格に必要です。',
          null,
        ],
        audioEn: 'We had lunch at a small restaurant.',
      },
    ],
  },

  // to不定詞: 名詞の席に入るか、修飾語になるか。
  'u10-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: 'to不定詞は「〜すること」で名詞の席に入る',
        sentence: 'I wanted to see the dog.',
        ja: '私はその犬に会いたかったのです。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'wanted', role: 'V' },
          { text: 'to see the dog.', role: 'O', note: '「〜することを」の意味で wanted の目的語' },
        ],
        caption:
          'to see the dog は4語ありますが、動詞 wanted の目的語(O)の席に1つのかたまりとして入っています。長さではなく、文の中での働きで見分けます。',
      },
      {
        type: 'breakdown',
        title: '同じ to不定詞が「〜するために」になることもある',
        sentence: 'I went to the park to see the dog.',
        ja: '私はその犬に会うために公園へ行きました。',
        pattern: 'SV',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'went', role: 'V' },
          { text: 'to the park', role: 'M', note: '行き先' },
          { text: 'to see the dog.', role: 'M', note: '何のために' },
        ],
        skeleton: 'I went to the park.',
        skeletonPattern: 'SV',
        caption:
          '前の to the park は行き先、うしろの to see the dog は目的を足す修飾語(M)です。同じ to でも、名詞の席に入るのか修飾語になるのかは、文の中での働きで決まります。',
      },
    ],
    quiz: [
      {
        id: 'u10-l1-s1',
        prompt: 'I wanted to see the dog. で to see the dog の役割を選んでください。',
        sentenceJa: '「何を」にあたるかを考えます。',
        choices: ['主語(S)', '動詞(V)', '目的語(O)', '修飾語(M)'],
        correctIndex: 2,
        explanation: 'to see the dog は「〜することを」の意味で、動詞 wanted の目的語(O)として働いています。語数が多くても1つの目的語です。',
        choiceNotes: [
          '主語は I です。',
          '文の動詞は wanted です。to see のほうではありません。',
          null,
          '「〜するために」の意味なら修飾語(M)になりますが、この文は wanted の対象を表す目的語(O)です。',
        ],
        audioEn: 'I wanted to see the dog.',
      },
      {
        id: 'u10-l1-s2',
        prompt: 'I went to the park to see the dog. の骨格を選んでください。',
        sentenceJa: 'went が目的語を取るかどうかが手がかりです。',
        choices: ['I went to the park.', 'I went to see the dog.', 'to see the dog went.', 'went to the park to see the dog.'],
        correctIndex: 0,
        explanation: 'went は目的語を取らない動詞なので、骨格は S + V の第1文型です。残るのは I went to the park. です。',
        choiceNotes: [
          null,
          'to see the dog は目的を表す修飾語(M)なので、これだけ残しても骨格になりません。',
          '動詞 went が最後に来る語順は英語では成り立ちません。',
          '主語 I が抜けています。',
        ],
        audioEn: 'I went to the park to see the dog.',
      },
    ],
  },
}
