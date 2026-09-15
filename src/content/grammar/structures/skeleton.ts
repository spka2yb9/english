// 「英文の作られ方から学ぶ」ページの前半。
//
// 旧 u01-l4「英語の語順 SVO」を統合し、さらに文の要素(S / V / O / C / M)の意味を
// ページの最初に置く。レッスンではないため、文型バッジは合成時の patterns を通らず、
// ここで明示的に付与する。

import type { GrammarExample, LessonBlock, QuizQuestion, SentenceRole } from '../../types'

/** S / V / O / C / M が何を表すかを、例と一緒に示す。 */
export type RoleGuide = {
  role: SentenceRole
  /** この役割を担う語句の例 */
  example: string
  /** 例がどの文の一部か */
  sentence: string
  /** この役割の見つけ方(日本語) */
  note: string
}

/** 5つの役割を1文で見せるための文。S / V / O / O / M がそろう。 */
export const roleExampleSentence = 'My sister gave me a book yesterday.'

export const roleGuides: RoleGuide[] = [
  {
    role: 'S',
    example: 'My sister',
    sentence: roleExampleSentence,
    note: '文が「だれが・何が」について述べているかを示します。英語では動詞より前に置かれます。',
  },
  {
    role: 'V',
    example: 'gave',
    sentence: roleExampleSentence,
    note: '文の中心です。まずこの語を探すと、うしろに何が続くかで骨格の形が決まります。',
  },
  {
    role: 'O',
    example: 'me / a book',
    sentence: roleExampleSentence,
    note: '動作の対象です。「だれに・何を」にあたります。この文には2つあるので第4文型になります。',
  },
  {
    role: 'C',
    example: 'happy',
    sentence: 'The news made everyone happy.',
    note: '主語や目的語を説明します。everyone = happy のように「=」の関係が成り立てば補語です。',
  },
  {
    role: 'M',
    example: 'yesterday',
    sentence: roleExampleSentence,
    note: 'いつ・どこで・どんなふうに、を足す語句です。外しても骨格は壊れません。',
  },
]

/** 記号の意味を示す構造図。 */
export const roleBlocks: LessonBlock[] = [
  {
    type: 'breakdown',
    title: '1つの文で役割を確かめる',
    sentence: roleExampleSentence,
    ja: '姉は昨日、私に本をくれました。',
    pattern: 'SVOO',
    parts: [
      { text: 'My sister', role: 'S', note: '文が何について述べているか' },
      { text: 'gave', role: 'V', note: '文の中心' },
      { text: 'me', role: 'O', note: 'だれに' },
      { text: 'a book', role: 'O', note: '何を' },
      { text: 'yesterday.', role: 'M', note: 'いつ。外せる' },
    ],
    skeleton: 'My sister gave me a book.',
    skeletonPattern: 'SVOO',
    caption:
      'S と V はどの文にもあります。そのあとに目的語(O)や補語(C)が続くかどうかで骨格が決まり、修飾語(M)はいつでも外せます。まずこの5つの役割を区別できるようにしましょう。',
  },
]

/** 英語の語順と修飾語の位置(旧 u01-l4 の内容)。 */
export const wordOrderBlocks: LessonBlock[] = [
  {
    type: 'explanation',
    title: '語順が意味を決める',
    body:
      '日本語では「ケン**が**マリ**を**愛している」のように助詞が役割を示します。英語にはその助詞がないので、**どの語がどの役割かを語順で示す**ことになります。\n\n- Ken loves Mari. → ケンがマリを愛しています。\n- Mari loves Ken. → マリがケンを愛しています。\n\n同じ3語でも、順番が変われば意味が反対になります。だから英文を読むときは、まず S → V → O の並びを取り出します。',
  },
  {
    type: 'breakdown',
    title: '骨格は S + V + O の3つ',
    sentence: 'My sister plays the piano.',
    ja: '姉はピアノを弾きます。',
    pattern: 'SVO',
    parts: [
      { text: 'My sister', role: 'S', note: '「だれが」にあたる' },
      { text: 'plays', role: 'V', note: '文の中心' },
      { text: 'the piano.', role: 'O', note: '「何を」にあたる' },
    ],
    caption:
      '動詞 plays より前が S、動詞のすぐあとが O です。日本語の語順にとらわれず、この3つの席を先に埋めるのがコツです。',
  },
  {
    type: 'breakdown',
    title: '場所と時間は骨格の外側に足す',
    sentence: 'My sister plays the piano at the concert hall every year.',
    ja: '姉は毎年、コンサートホールでピアノを弾きます。',
    pattern: 'SVO',
    parts: [
      { text: 'My sister', role: 'S' },
      { text: 'plays', role: 'V' },
      { text: 'the piano', role: 'O' },
      { text: 'at the concert hall', role: 'M', note: 'どこで' },
      { text: 'every year.', role: 'M', note: 'いつ' },
    ],
    skeleton: 'My sister plays the piano.',
    skeletonPattern: 'SVO',
    caption:
      '情報が増えても、残る骨格は My sister plays the piano. のままです。動詞と目的語の間に場所や時間を割り込ませないのが、骨格を見失わないコツです。',
  },
  {
    type: 'structure',
    title: '基本の語順',
    parts: [
      { label: '主語(だれが)', text: 'My sister' },
      { label: '動詞(する)', text: 'plays' },
      { label: '目的語(何を)', text: 'the piano' },
    ],
    caption: '日本語の「姉は ピアノを 弾く」と違い、動詞が主語のすぐあとに来ます。',
  },
  {
    type: 'expansion',
    title: '長い文も骨組みから組み立てる',
    steps: [
      { en: 'My sister plays the piano.', ja: '姉はピアノを弾きます。', note: 'まず S + V + O の骨格を完成させます。' },
      {
        en: 'My sister plays the piano at the concert hall.',
        ja: '姉はコンサートホールでピアノを弾きます。',
        focus: 'at the concert hall',
        note: '場所は骨格のあとに足します。',
      },
      {
        en: 'My sister plays the piano at the concert hall every year.',
        ja: '姉は毎年、コンサートホールでピアノを弾きます。',
        focus: 'every year',
        note: '時間は場所のあとに。順番は「場所 → 時間」が基本です。',
      },
    ],
    caption:
      '頻度を表す usually などは一般動詞の前、場所と時間は「場所 → 時間」の順に置きます。最も強調したい時間は Yesterday, ... のように文頭へ出すこともできます。',
  },
  {
    type: 'explanation',
    title: '語順を変えると意味も変わる',
    body:
      '日本語の語順につられて Yesterday at the office I the report finished. のようにせず、**I finished the report** を先に作ってから場所と時間を足します。\n\n英語では語順そのものが役割を示すので、位置を変えると意味も変わり得ます。作文するときは、まず骨格を作る習慣をつけましょう。',
  },
]

/** 旧 u01-l4 の例文。ページでも音声つきで読めるように残す。 */
export const wordOrderExamples: GrammarExample[] = [
  { en: 'My sister plays the piano.', ja: '姉はピアノを弾きます。', pattern: 'SVO', patternNote: 'play の対象 the piano が目的語(O)。' },
  { en: 'We eat lunch at noon.', ja: '私たちは正午に昼食を食べます。', pattern: 'SVO', patternNote: '時を表す at noon は修飾語(M)で、骨格は SVO。' },
  {
    en: 'Ken met his friend at the station yesterday.',
    ja: 'ケンは昨日、駅で友達に会いました。',
    highlight: 'at the station yesterday',
    pattern: 'SVO',
    patternNote: '場所 → 時間の順に修飾語(M)を並べる。骨格は Ken met his friend の SVO。',
  },
  {
    en: 'I always drink tea in the morning.',
    ja: '私は朝はいつも紅茶を飲みます。',
    pattern: 'SVO',
    patternNote: '頻度の副詞 always と時の句 in the morning はどちらも修飾語(M)。',
  },
  {
    en: 'My father washes the car every Sunday.',
    ja: '父は毎週日曜日に車を洗います。',
    highlight: 'washes the car',
    pattern: 'SVO',
    patternNote: 'the car が目的語(O)。every Sunday は時の修飾語(M)。',
  },
  {
    en: 'She writes emails at the office every morning.',
    ja: '彼女は毎朝オフィスでメールを書きます。',
    highlight: 'at the office every morning',
    pattern: 'SVO',
    patternNote: '動詞のあとの目的語が先、場所と時間はそのあと。',
  },
  {
    en: 'My uncle grows vegetables in his garden.',
    ja: 'おじは庭で野菜を育てています。',
    highlight: 'grows vegetables',
    pattern: 'SVO',
    patternNote: 'grow の対象 vegetables が目的語(O)。',
  },
  {
    en: 'The manager sent the team an update yesterday.',
    ja: 'マネージャーは昨日チームに最新情報を送りました。',
    highlight: 'sent the team an update',
    pattern: 'SVOO',
    patternNote: '人(the team)→ もの(an update)の順に目的語が2つ。',
  },
  {
    en: 'The children played soccer in the park after school.',
    ja: '子どもたちは放課後、公園でサッカーをしました。',
    highlight: 'played soccer in the park after school',
    pattern: 'SVO',
    patternNote: '骨格は played soccer の SVO。場所と時間は外側の修飾語(M)。',
  },
  {
    en: 'I usually read the news on the train.',
    ja: '私はたいてい電車でニュースを読みます。',
    highlight: 'usually read',
    pattern: 'SVO',
    patternNote: 'usually は一般動詞の前、on the train は文末の修飾語(M)。',
  },
]

/** 旧 u01-l4 の理解度チェックと構造チェックを統合し、記号の意味を問う問題を足したもの。 */
export const wordOrderQuiz: QuizQuestion[] = [
  {
    id: 'roadmap-w1',
    prompt: '正しい語順の文を選んでください。',
    sentenceJa: '「トムは毎朝コーヒーを飲みます」と言いたいとき。',
    choices: ['Tom every morning coffee drinks.', 'Tom drinks coffee every morning.', 'Every morning Tom coffee drinks.', 'Tom coffee drinks every morning.'],
    correctIndex: 1,
    explanation: '英語の基本語順は S(Tom)→ V(drinks)→ O(coffee)で、時間の情報は文の後ろに置きます。',
    choiceNotes: ['動詞が最後に来るのは日本語の語順です。', null, '動詞と目的語の順が逆です。V → O の順にします。', '目的語が動詞より前に来ています。'],
    audioEn: 'Tom drinks coffee every morning.',
  },
  {
    id: 'roadmap-w2',
    prompt: '意味が正しく伝わる文を選んでください。',
    sentenceJa: '「猫がネズミを追いかけた」と言いたいとき。',
    choices: ['The mouse chased the cat.', 'The cat chased the mouse.', 'Chased the cat the mouse.', 'The cat the mouse chased.'],
    correctIndex: 1,
    explanation: '英語では動詞の前が「する側」、あとが「される側」です。The cat(する側)chased the mouse(される側)。',
    choiceNotes: ['これでは「ネズミが猫を追いかけた」という逆の意味になります。', null, 'この文は動詞から始められません。まず「追いかけた側」の The cat を置きます。', '目的語を動詞の前に置くことはできません。'],
    audioEn: 'The cat chased the mouse.',
  },
  {
    id: 'roadmap-w3',
    prompt: '場所と時間の位置が正しい文を選んでください。',
    choices: ['She works at a hospital in Tokyo.', 'She at a hospital works in Tokyo.', 'She works in Tokyo at a hospital.', 'At a hospital she in Tokyo works.'],
    correctIndex: 0,
    explanation: '動詞のあとに場所の情報を置きます。狭い場所(at a hospital)→ 広い場所(in Tokyo)の順が自然です。',
    choiceNotes: [null, '場所の情報を主語と動詞の間に挟むことはできません。', '通じますが、狭い場所 → 広い場所の順(at a hospital in Tokyo)がより自然です。', '動詞が最後に来るのは英語の語順ではありません。'],
    audioEn: 'She works at a hospital in Tokyo.',
  },
  {
    id: 'roadmap-w4',
    prompt: '自然な語順の文を選んでください。',
    sentenceJa: '「私は先週、図書館でその本を読みました」と言いたいとき。',
    choices: [
      'I read the book at the library last week.',
      'I read at the library the book last week.',
      'I last week read the book at the library.',
      'I read the book last week at the library.',
    ],
    correctIndex: 0,
    explanation: 'S → V → O のあとに「場所 → 時間」の順で情報を並べます。',
    choiceNotes: [null, '動詞と目的語(read the book)の間に場所を挟まないようにします。', '時間の情報は文の後ろに置くのが基本です。', '「場所 → 時間」の順が基本です(時間が先に来ると不自然に響くことが多い)。'],
    audioEn: 'I read the book at the library last week.',
  },
  {
    id: 'roadmap-w5',
    prompt: '主語(S)を選んでください。',
    sentence: 'My sister plays the piano every Sunday.',
    sentenceJa: '姉は毎週日曜日にピアノを弾きます。',
    choices: ['My sister', 'plays', 'the piano', 'every Sunday'],
    correctIndex: 0,
    explanation: '文が「何について述べているか」を表す My sister が主語(S)です。動詞 plays より前にある語が S です。',
    choiceNotes: [
      null,
      'plays は文の中心になる動詞(V)です。主語ではありません。',
      'the piano は動作の対象で目的語(O)です。',
      'every Sunday は時を表す修飾語(M)で、骨格の外側にあります。',
    ],
    audioEn: 'My sister plays the piano every Sunday.',
  },
  {
    id: 'roadmap-w6',
    prompt: '骨格に含まれない(外しても文が壊れない)語句を選んでください。',
    sentence: 'Tom drinks coffee every morning.',
    sentenceJa: 'トムは毎朝コーヒーを飲みます。',
    choices: ['Tom', 'drinks', 'coffee', 'every morning'],
    correctIndex: 3,
    explanation: 'every morning は動詞 drinks を修飾する「いつ」の情報(M)です。外しても S + V + O の骨格は崩れません。',
    choiceNotes: [
      'Tom は主語(S)で、骨格に欠かせません。',
      'drinks は動詞(V)で、文の中心です。',
      'coffee は目的語(O)で、骨格に欠かせません。',
      null,
    ],
    audioEn: 'Tom drinks coffee every morning.',
  },
  {
    id: 'roadmap-w7',
    prompt: 'この文の骨格(最小限の文)を選んでください。',
    sentence: 'Ken met his friend at the station yesterday.',
    sentenceJa: 'ケンは昨日、駅で友達に会いました。',
    choices: ['Ken met his friend.', 'Ken met at the station.', 'Ken met his friend yesterday.', 'met his friend at the station.'],
    correctIndex: 0,
    explanation: '場所(at the station)も時(yesterday)も修飾語(M)です。外すと主語 Ken + 動詞 met + 目的語 his friend の SVO が残ります。',
    choiceNotes: [
      null,
      'at the station は場所の修飾語(M)なので、これだけ残しても骨格になりません。',
      'yesterday は時の修飾語(M)なので外せます。骨格は S + V + O で足ります。',
      '主語 Ken が抜けています。英語の文には主語が必要です。',
    ],
    audioEn: 'Ken met his friend.',
  },
  {
    id: 'roadmap-w8',
    prompt: '「主語(S)」が表すものを選んでください。',
    choices: ['文が「だれが・何が」について述べているか', '文の中心になる動作や状態', '動作の対象', 'いつ・どこで を表す情報'],
    correctIndex: 0,
    explanation: '主語(S)は、その文が何について述べているかを示します。日本語の「〜が」「〜は」にあたり、英語では動詞より前に置かれます。',
    choiceNotes: [null, 'それは動詞(V)です。', 'それは目的語(O)です。', 'それは修飾語(M)です。'],
    audioEn: 'My sister gave me a book yesterday.',
  },
  {
    id: 'roadmap-w9',
    prompt: '「補語(C)」を見分ける目印はどれですか。',
    choices: ['文のいちばん後ろにある語', 'S や O と C の間に「=」の関係が成り立つ', '動詞の直前に置かれる', '複数の語でできている'],
    correctIndex: 1,
    explanation: 'C は主語や目的語を説明する語です。She = a nurse、everyone = happy のように「=」の関係が成り立てば補語(C)です。',
    choiceNotes: ['後ろにあるから C とは限りません。時を表す語は修飾語(M)です。', null, '動詞の直前にある語は主語(S)です。', '語数は関係ありません。1語でも C になります。'],
    audioEn: 'The news made everyone happy.',
  },
  {
    id: 'roadmap-w10',
    prompt: '「修飾語(M)」の説明として正しいものを選んでください。',
    choices: ['文の骨格に欠かせない要素', '外しても文の骨格が壊れない語句', '必ず文の先頭に置かれる語句', '動詞の目的語になる語句'],
    correctIndex: 1,
    explanation: '修飾語(M)は、いつ・どこで・どんなふうに を足す語句です。外しても S + V (+ O / C) の骨格は壊れません。',
    choiceNotes: ['骨格に欠かせないのは S / V / O / C です。', null, '場所や時間は文の後ろに置くのが基本です。', '動詞の目的語になるのは名詞句や名詞節で、目的語(O)として数えます。'],
    audioEn: 'Ken met his friend at the station yesterday.',
  },
  {
    id: 'roadmap-w11',
    prompt: '文の骨格を探すとき、最初に探すものを選んでください。',
    choices: ['主語(S)', '動詞(V)', '目的語(O)', '修飾語(M)'],
    correctIndex: 1,
    explanation: 'まず動詞(V)を探すと、その前に主語(S)、うしろに目的語(O)や補語(C)があるかを順に確かめられます。動詞が決まれば骨格の形も決まります。',
    choiceNotes: ['主語は動詞の前にあります。動詞を先に見つけると主語も見つけやすくなります。', null, '目的語があるかどうかは、動詞の種類で決まります。', '修飾語は骨格を取ったあとに確かめます。'],
    audioEn: 'Birds fly in the sky.',
  },
]
