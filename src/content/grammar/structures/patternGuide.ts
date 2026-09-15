// 「英文の作られ方から学ぶ」ページの後半。
//
// 旧 u01-l5「5文型で文の骨組みを見る」を統合したもの。
// 5文型の一覧は、文章の表ではなく、1文型につき2Dアニメーションと代表例を並べたカードで示す。
// 文型バッジは合成時の patterns を通らないため、ここで明示的に付与する。

import type { GrammarExample, LessonBlock, QuizQuestion, SentencePattern } from '../../types'

/** 5文型の見取り図。1文型につき1枚のカードにする。 */
export type PatternShowcase = {
  pattern: SentencePattern
  /** 骨組みの表記(例: S + V + O + O) */
  skeleton: string
  /** 代表例 */
  example: { en: string; ja: string; note: string }
  /** O = C のような意味上の関係 */
  relation?: string
}

export const patternShowcases: PatternShowcase[] = [
  {
    pattern: 'SV',
    skeleton: 'S + V',
    example: {
      en: 'Birds fly.',
      ja: '鳥は飛びます。',
      note: 'fly は目的語も補語も必要としない動詞です。S と V だけで文が完成します。',
    },
  },
  {
    pattern: 'SVC',
    skeleton: 'S + V + C',
    example: {
      en: 'She became a doctor.',
      ja: '彼女は医者になりました。',
      note: 'a doctor は動作の対象ではなく、主語 She の状態を説明する補語(C)です。',
    },
    relation: 'She = a doctor',
  },
  {
    pattern: 'SVO',
    skeleton: 'S + V + O',
    example: {
      en: 'I bought a new bike yesterday.',
      ja: '私は昨日新しい自転車を買いました。',
      note: 'a new bike が動作の対象で目的語(O)。yesterday は時を表す修飾語(M)なので要素に数えません。',
    },
  },
  {
    pattern: 'SVOO',
    skeleton: 'S + V + O + O',
    example: {
      en: 'My father gave me a camera.',
      ja: '父は私にカメラをくれました。',
      note: '「人 → もの」の順に目的語が2つ並びます。',
    },
    relation: 'me(人)← a camera(もの)',
  },
  {
    pattern: 'SVOC',
    skeleton: 'S + V + O + C',
    example: {
      en: 'The news made everyone happy.',
      ja: 'その知らせはみんなを幸せにしました。',
      note: '目的語 everyone を、うしろの happy が説明しています。',
    },
    relation: 'everyone = happy',
  },
]

/** 5文型の見方と、紛らわしい型の区別(旧 u01-l5 の内容)。 */
export const patternBlocks: LessonBlock[] = [
  {
    type: 'explanation',
    title: '動詞のあとに続くもので型が決まる',
    body:
      '英文は「主語(S)のあとに動詞(V)、そのあとに何が続くか」で型が決まります。\n\n- **目的語(O)**: 動作の対象。「何を・だれを」にあたる。\n- **補語(C)**: 主語や目的語を説明する言葉。「〜はどんな人・どんな状態か」にあたる。\n\n5文型は覚えるための分類ではなく、**動詞のあとに何が続くかを確かめる道具**です。「O = C」の関係が成り立つかどうかが、第3文型と第5文型を分ける目印になります。',
  },
  {
    type: 'structure',
    title: '補語(C)は主語を説明する',
    parts: [
      { label: '主語(S)', text: 'She' },
      { label: '動詞(V)', text: 'is' },
      { label: '補語(C)', text: 'a nurse' },
    ],
    caption: '「She = a nurse」の関係を作るのが補語です。補語には名詞・形容詞などが入り、主語や目的語を説明します。',
  },
  {
    type: 'breakdown',
    title: 'C は目的語を説明する',
    sentence: 'I found the book very useful.',
    ja: '私はその本がとても役に立つと分かりました。',
    pattern: 'SVOC',
    parts: [
      { text: 'I', role: 'S' },
      { text: 'found', role: 'V' },
      { text: 'the book', role: 'O', note: '動作の対象' },
      { text: 'very useful.', role: 'C', note: 'the book を説明する' },
    ],
    relation: 'the book = very useful',
    caption:
      'very useful は the book の状態を説明しているので補語(C)です。the book = very useful の関係が成り立つため、第5文型 SVOC になります。',
  },
  {
    type: 'breakdown',
    title: '似ているが C ではない文',
    sentence: 'I found the book yesterday.',
    ja: '私は昨日その本を見つけました。',
    pattern: 'SVO',
    parts: [
      { text: 'I', role: 'S' },
      { text: 'found', role: 'V' },
      { text: 'the book', role: 'O' },
      { text: 'yesterday.', role: 'M', note: 'found を修飾する副詞' },
    ],
    skeleton: 'I found the book.',
    skeletonPattern: 'SVO',
    caption:
      'yesterday は「いつ見つけたか」を found に足しているだけです。the book = yesterday という関係は成り立たないので C ではなく M。骨格は I found the book. の SVO です。同じ found でも、M が続くか C が続くかで文型が変わります。',
  },
  {
    type: 'contrast',
    title: '第4文型と「to + 人」の言い換え',
    left: {
      label: 'SVOO: 人 → もの',
      items: [
        { en: 'He gave me a book.', ja: '彼は私に本をくれました。', highlight: 'gave me a book', pattern: 'SVOO', patternNote: 'me と a book の2つの目的語。' },
        {
          en: 'She sent her friend a postcard.',
          ja: '彼女は友達に葉書を送りました。',
          highlight: 'sent her friend a postcard',
          pattern: 'SVOO',
          patternNote: 'her friend と a postcard の2つの目的語。',
        },
      ],
      pointJa: '人のあとに「もの」をそのまま続けます。',
    },
    right: {
      label: 'SVO + to: もの → 人',
      items: [
        { en: 'He gave a book to me.', ja: '彼は本を私にくれました。', highlight: 'gave a book to me', pattern: 'SVO', patternNote: '目的語は a book ひとつで、to me は修飾語(M)。' },
        {
          en: 'She sent a postcard to her friend.',
          ja: '彼女は葉書を友達に送りました。',
          highlight: 'sent a postcard to her friend',
          pattern: 'SVO',
          patternNote: '目的語は a postcard ひとつ。to her friend は修飾語(M)。',
        },
      ],
      pointJa: '「もの」を先に言い、to + 人 を文末に置きます。',
    },
    note: '同じ出来事をどちらの型でも表せます。目的語が長いときは文末に回すと読みやすくなります。',
  },
  {
    type: 'explanation',
    title: '第4文型の書き換えと、日本語とのずれ',
    body:
      '第4文型(SVOO)は「人 → もの」の順ですが、もののほうが長いときは第3文型(SVO)+ to / for に置き換えます。give・send・show・teach などは to、buy・make・get・cook などは for を使うのが目安です。\n\nもう一つの注意点は、日本語の「〜を」に引かれないことです。日本語では「彼をケンと呼ぶ」の「彼を」が目的語に見えますが、英語では him のあとに補語 Ken が続き、him = Ken の関係になります。動詞ごとに「あとに何が続くか」を確かめると、第4文型と第5文型を取り違えにくくなります。',
  },
  {
    type: 'breakdown',
    title: '長い文から骨格を取り出す',
    sentence: 'The young man standing near the station gave me a beautiful flower yesterday.',
    ja: '駅の近くに立っていた若い男性が、昨日私に美しい花をくれました。',
    pattern: 'SVOO',
    parts: [
      { text: 'The young man', role: 'S', note: '主語の中心' },
      { text: 'standing near the station', role: 'M', note: 'どの男性かを説明する分詞句' },
      { text: 'gave', role: 'V' },
      { text: 'me', role: 'O', note: '人' },
      { text: 'a beautiful flower', role: 'O', note: 'もの' },
      { text: 'yesterday.', role: 'M', note: 'いつ' },
    ],
    skeleton: 'The young man gave me a flower.',
    skeletonPattern: 'SVOO',
    caption:
      '修飾部分をすべて外すと、The young man gave me a flower. という短い文になります。語数が多くても、骨格は S + V + O + O の4つです。長い文に出会ったら、まず修飾部分を外してみましょう。',
  },
]

/** 旧 u01-l5 の例文。ページでも音声つきで読めるように残す。 */
export const patternExamples: GrammarExample[] = [
  { en: 'Birds fly high in the sky.', ja: '鳥は空高く飛びます。', highlight: 'Birds fly', pattern: 'SV', patternNote: '目的語も補語も必要ない第1文型。' },
  { en: 'My sister is a nurse.', ja: '姉は看護師です。', highlight: 'is a nurse', pattern: 'SVC', patternNote: 'a nurse が主語を説明する第2文型。' },
  { en: 'She became a famous singer.', ja: '彼女は有名な歌手になりました。', highlight: 'became a famous singer', pattern: 'SVC', patternNote: 'become も主語を説明する語を取る第2文型。' },
  { en: 'I bought a new bike yesterday.', ja: '私は昨日新しい自転車を買いました。', highlight: 'bought a new bike', pattern: 'SVO', patternNote: 'a new bike が動作の対象。第3文型。' },
  { en: 'My father gave me a camera.', ja: '父は私にカメラをくれました。', highlight: 'gave me a camera', pattern: 'SVOO', patternNote: '人(me)→ もの(a camera)の第4文型。' },
  { en: 'They named the baby Emma.', ja: '彼らはその赤ちゃんをエマと名づけました。', highlight: 'named the baby Emma', pattern: 'SVOC', patternNote: 'the baby = Emma の関係がある第5文型。' },
  { en: 'The news made everyone happy.', ja: 'その知らせはみんなを幸せにしました。', highlight: 'made everyone happy', pattern: 'SVOC', patternNote: 'everyone = happy の関係がある第5文型。' },
  { en: 'My uncle taught me the guitar.', ja: 'おじは私にギターを教えてくれました。', highlight: 'taught me the guitar', pattern: 'SVOO', patternNote: '人(me)→ もの(the guitar)の第4文型。' },
  { en: 'The teacher left the door open.', ja: '先生はドアを開けたままにしました。', highlight: 'left the door open', pattern: 'SVOC', patternNote: 'the door = open の関係がある第5文型。' },
  { en: 'Can you send me the report?', ja: '私にその報告書を送ってもらえますか。', highlight: 'send me the report', pattern: 'SVOO', patternNote: '平叙文に戻すと You send me the report. の第4文型。' },
]

/** 旧 u01-l5 の理解度チェックと構造チェックを統合し、代表例の文型を問う問題を足したもの。 */
export const patternQuiz: QuizQuestion[] = [
  {
    id: 'roadmap-p1',
    prompt: '次の文の文型を選んでください。',
    sentence: 'She became a doctor.',
    sentenceJa: '彼女は医者になりました。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOO(第4文型)'],
    correctIndex: 1,
    explanation: 'became のあとの a doctor は動作の対象ではなく、主語 She を説明する補語です。She = a doctor の関係なので SVC(第2文型)です。',
    choiceNotes: [
      'SV は目的語も補語も取らない型です。became のあとには欠かせない説明が続きます。',
      null,
      'SVO の O は動作の対象です。a doctor は医者という状態を表す補語で、対象ではありません。',
      'SVOO は人とものの2つの目的語を取ります。この文に目的語はありません。',
    ],
    audioEn: 'She became a doctor.',
  },
  {
    id: 'roadmap-p2',
    prompt: '「私にその地図を送ってください」と伝える文を選んでください。',
    sentenceJa: 'SVOO の語順に注目します。',
    choices: ['Please send me the map.', 'Please send the map me.', 'Please me send the map.', 'Please send to me the map.'],
    correctIndex: 0,
    explanation: '第4文型(SVOO)は「人 → もの」の順です。send + 人 + もの で「人にものを送る」を表します。',
    choiceNotes: [
      null,
      '「もの → 人」の順では第4文型になりません。人は動詞のすぐあとに置きます。',
      '人を動詞の前に置くことはできません。主語の次は動詞です。',
      'to me を先に置くなら send the map to me の順になります。この並びは不自然です。',
    ],
    audioEn: 'Please send me the map.',
  },
  {
    id: 'roadmap-p3',
    prompt: '第5文型(SVOC)の文を選んでください。',
    sentenceJa: 'O と C の間に「O = C」の関係がある文を探します。',
    choices: ['We call him Ken.', 'We call him.', 'We called yesterday.', 'Ken called us.'],
    correctIndex: 0,
    explanation: '第5文型(SVOC)は目的語(O)と補語(C)が「O = C」の関係になります。We call him Ken. では him = Ken です。',
    choiceNotes: [
      null,
      'call は「〜を〜と呼ぶ」の意味では、呼び名にあたる補語が必要です。',
      '目的語も補語もない第1文型(SV)の文です。',
      'これは「ケンが私たちに電話した」という第3文型(SVO)の文です。',
    ],
    audioEn: 'We call him Ken.',
  },
  {
    id: 'roadmap-p4',
    prompt: 'everyone と happy の関係を表すものを選んでください。',
    sentence: 'The news made everyone happy.',
    sentenceJa: '第5文型の目的語と補語の関係を確かめます。',
    choices: ['everyone = happy', 'everyone → happy', 'the news = happy', 'everyone = the news'],
    correctIndex: 0,
    explanation: '第5文型(SVOC)では目的語(O)と補語(C)の間に「O = C」の関係があります。made のあとは everyone = happy です。',
    choiceNotes: [
      null,
      '矢印ではなくイコールの関係です。happy は everyone の状態を説明します。',
      'happy が説明しているのは the news ではなく everyone です。',
      'the news は主語(S)、everyone は目的語(O)で、イコールの関係ではありません。',
    ],
    audioEn: 'The news made everyone happy.',
  },
  {
    id: 'roadmap-p5',
    prompt: '動詞(V)を選んでください。',
    sentence: 'The young man standing near the station gave me a beautiful flower yesterday.',
    sentenceJa: '駅の近くに立っていた若い男性が、昨日私に美しい花をくれました。',
    choices: ['standing', 'gave', 'near', 'yesterday'],
    correctIndex: 1,
    explanation: '文全体の中心になる動詞は gave です。standing は the young man を説明する分詞で、文全体の動詞ではありません。',
    choiceNotes: [
      'standing は the young man を後ろから説明する分詞で、文全体の動詞(V)ではありません。',
      null,
      'near は前置詞で、the station と結びついて「駅の近く」という修飾部分を作ります。',
      'yesterday は時を表す修飾語(M)です。',
    ],
    audioEn: 'The young man standing near the station gave me a beautiful flower yesterday.',
  },
  {
    id: 'roadmap-p6',
    prompt: '主語(S)の中心を選んでください。',
    sentence: 'The young man standing near the station gave me a beautiful flower yesterday.',
    sentenceJa: '駅の近くに立っていた若い男性が、昨日私に美しい花をくれました。',
    choices: ['The young man', 'standing near the station', 'me', 'a beautiful flower'],
    correctIndex: 0,
    explanation: '「だれが」にあたるのは The young man です。standing near the station はその人を説明する修飾部分なので、主語の中心には含めません。',
    choiceNotes: [
      null,
      'standing near the station は The young man を説明する修飾部分で、主語の中心ではありません。',
      'me は「〜に」にあたる目的語(O)です。',
      'a beautiful flower も目的語(O)です。',
    ],
    audioEn: 'The young man gave me a flower.',
  },
  {
    id: 'roadmap-p7',
    prompt: 'この文の骨格を取り出した文を選んでください。',
    sentence: 'The young man standing near the station gave me a beautiful flower yesterday.',
    sentenceJa: '駅の近くに立っていた若い男性が、昨日私に美しい花をくれました。',
    choices: [
      'The young man gave me a flower.',
      'The young man gave me a beautiful flower yesterday.',
      'The young man stood near the station.',
      'The young man gave a flower.',
    ],
    correctIndex: 0,
    explanation: '修飾部分を外すと The young man gave me a flower. になります。主語 + 動詞 + 目的語2つ(SVOO)の骨格は、元の文と同じです。',
    choiceNotes: [
      null,
      '修飾部分を外していないので、まだ骨格とはいえません。',
      'gave が抜けています。文の中心になる動詞を残さないと骨格になりません。',
      'me が抜けています。SVOO では「人」と「もの」の2つの目的語が必要です。',
    ],
    audioEn: 'The young man gave me a flower.',
  },
  {
    id: 'roadmap-p8',
    prompt: 'I found the book very useful. の文型を選んでください。',
    sentenceJa: 'very useful の働きに注目します。',
    choices: ['SV(第1文型)', 'SVO(第3文型)', 'SVOC(第5文型)', 'SVOO(第4文型)'],
    correctIndex: 2,
    explanation: 'the book が目的語(O)、very useful がその目的語を説明する補語(C)で、the book = very useful の関係があります。したがって SVOC(第5文型)です。',
    choiceNotes: [
      'SV は目的語も補語も取らない型です。この文には説明が必要な目的語があります。',
      'SVO なら the book のあとに説明の言葉は続きません。very useful が続いているので SVO ではありません。',
      null,
      'SVOO は「人」と「もの」の2つの目的語を取る型です。very useful はものではないので当てはまりません。',
    ],
    audioEn: 'I found the book very useful.',
  },
  {
    id: 'roadmap-p9',
    prompt: 'I found the book yesterday. が SVO(第3文型)になるのはなぜですか。',
    sentenceJa: 'yesterday の役割から考えます。',
    choices: [
      'yesterday が found を修飾する副詞で、the book を説明していないから',
      'yesterday が目的語として the book と並んでいるから',
      'found が目的語を取らない自動詞だから',
      'the book = yesterday の関係が成り立つから',
    ],
    correctIndex: 0,
    explanation:
      'C(補語)は主語や目的語を説明する語です。yesterday は「いつ」を表して found を修飾するだけなので M(修飾語)であり、骨格は I found the book. の SVO になります。',
    choiceNotes: [
      null,
      'yesterday は目的語ではありません。この文の目的語は the book ひとつです。',
      'found は the book という目的語を取る他動詞です。',
      'the book = yesterday という意味の関係は成り立ちません。yesterday は時を表すだけです。',
    ],
    audioEn: 'I found the book yesterday.',
  },
  {
    id: 'roadmap-p10',
    prompt: 'My sister is a nurse. の文型を選んでください。',
    sentence: 'My sister is a nurse.',
    sentenceJa: '姉は看護師です。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOO(第4文型)'],
    correctIndex: 1,
    explanation: 'is のうしろの a nurse は主語 My sister を説明する補語(C)です。My sister = a nurse の関係なので SVC(第2文型)です。',
    choiceNotes: [
      'SV は目的語も補語も取らない型です。be動詞のうしろには説明の語が続きます。',
      null,
      'SVO の O は動作の対象です。a nurse は対象ではなく、主語の説明です。',
      'SVOO は目的語を2つ取る型です。この文に目的語はありません。',
    ],
    audioEn: 'My sister is a nurse.',
  },
  {
    id: 'roadmap-p11',
    prompt: 'I bought a new bike yesterday. の文型を選んでください。',
    sentenceJa: 'yesterday を要素に数えるかどうかがポイントです。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOC(第5文型)'],
    correctIndex: 2,
    explanation: 'a new bike が動作の対象で目的語(O)です。yesterday は時を表す修飾語(M)なので要素に数えず、骨格は I + bought + a new bike の SVO です。',
    choiceNotes: [
      'SV には目的語がありません。この文には a new bike という目的語があります。',
      'SVC のうしろは主語の説明で、動作の対象ではありません。',
      null,
      'SVOC には目的語を説明する補語(C)が必要です。yesterday は bought を修飾するだけで、bike を説明していません。',
    ],
    audioEn: 'I bought a new bike yesterday.',
  },
  {
    id: 'roadmap-p12',
    prompt: '第4文型(SVOO)の語順を選んでください。',
    choices: ['人 → もの', 'もの → 人', '人 → 人', 'もの → もの'],
    correctIndex: 0,
    explanation: '第4文型は「人 → もの」の順です。give + 人 + もの のように、受け取る人を先に置きます。',
    choiceNotes: [
      null,
      '「もの → 人」の順にするときは、to / for を付けて第3文型にします。',
      '人を2つ並べることはできません。',
      'ものが2つ並ぶのは第3文型と前置詞句の組み合わせです。',
    ],
    audioEn: 'He gave me a book.',
  },
]
