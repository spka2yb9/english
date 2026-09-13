import type { GrammarUnit } from '../../types'

// U17 現在完了進行形 — have been -ing の基本と、現在完了との使い分け

export const u17: GrammarUnit = {
  id: 'u17',
  level: 'B1+',
  title: '現在完了進行形',
  lessons: [
    {
      id: 'u17-l1',
      unitId: 'u17',
      level: 'B1+',
      title: '現在完了進行形の基本',
      objective: '過去に始まって今も続いている動作を、現在完了進行形(have been + -ing)を使って表せるようになります。',
      minutes: 10,
      prereqs: ['u11-l3'],
      blocks: [
        {
          type: 'explanation',
          title: '「ずっと〜している」を1つの形で',
          body:
            '「1時間前から待ち続けている」「4月からずっと英語を勉強している」— このように**過去に始まった動作が今もまだ続いている**とき、英語では現在完了進行形 have been + -ing を使います。\n\n- I **have been waiting** for an hour.(1時間前に待ち始めて、今もまだ待っている)\n\n「過去と今をつなぐ」現在完了(U11)の性質と、「動作の途中」を表す進行形の性質を組み合わせた形です。for(〜の間)や since(〜から)と非常に相性がよく、How long ...?(どのくらいの間?)への答えにもこの形をよく使います。',
        },
        {
          type: 'structure',
          title: '形: have / has been + 動詞の -ing 形',
          parts: [
            { label: '主語', text: 'She' },
            { label: 'have / has', text: 'has' },
            { label: 'been', text: 'been' },
            { label: '動詞の -ing 形', text: 'studying' },
            { label: '継続の情報', text: 'since April' },
          ],
          caption: 'been は主語が何でも形が変わりません。主語に合わせて変わるのは have / has だけです。',
        },
        {
          type: 'timeline',
          title: '時間のイメージ',
          timelines: [
            {
              title: 'I have been waiting for an hour.',
              range: [70, 100],
              rangeLabel: '1時間前から待ち続けている',
              arrowToNow: true,
              caption: '過去に始まった動作が、今この瞬間までずっと続いています。',
            },
          ],
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'I have been waiting for the bus for twenty minutes.', ja: 'バスを20分間待ち続けています。', highlight: 'have been waiting' },
            { en: 'She has been studying English since April.', ja: '彼女は4月からずっと英語を勉強しています。', highlight: 'has been studying' },
            { en: 'It has been raining all day.', ja: '一日中雨が降り続いています。', highlight: 'has been raining' },
            { en: 'How long have you been working here?', ja: 'ここでどのくらいの間働いているのですか。', highlight: 'have you been working', note: '継続の長さを尋ねる How long と相性抜群です。' },
            { en: "They haven't been sleeping well lately.", ja: '彼らは最近よく眠れていません。', highlight: "haven't been sleeping", note: '否定文は have / has のあとに not を置きます。' },
          ],
        },
        {
          type: 'explanation',
          title: '否定文・疑問文と、-ing にできない動詞',
          body:
            "否定文と疑問文の作り方は現在完了と同じで、have / has が担当します。\n\n- 否定: They **haven't been sleeping** well lately.\n- 疑問: **Have** you **been waiting** long? / **How long have** you **been working** here?\n\n1つ注意があります。know / like / want / believe などの**状態動詞は -ing 形にしません**。「ずっと知っている」のような状態の継続は、現在完了で表します。\n\n- ○ I **have known** her for ten years.\n- × I have been knowing her for ten years.",
        },
      ],
      quiz: [
        {
          id: 'u17-l1-q1',
          prompt: '空所に入る形を選んでください。',
          sentence: 'She ___ for the bus for twenty minutes.',
          sentenceJa: '彼女は20分間バスを待ち続けています。',
          choices: ['waits', 'is waiting', 'has been waiting', 'was waiting'],
          correctIndex: 2,
          explanation: '「20分前から今まで」という継続の長さを表す for twenty minutes があるので、現在完了進行形 has been waiting を使います。',
          choiceNotes: ['現在形は習慣を表すので、「今までの20分間」という継続には合いません。', 'is waiting は「今待っている」だけで、for twenty minutes という今までの継続の長さを表せません。', null, 'was waiting は過去の話になり、「今も待っている」ことが伝わりません。'],
          audioEn: 'She has been waiting for the bus for twenty minutes.',
        },
        {
          id: 'u17-l1-q2',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「今朝からずっと雨が降っています」と言いたいとき。',
          choices: ['It is raining since this morning.', 'It has been raining since this morning.', 'It has been rain since this morning.', 'It rains since this morning.'],
          correctIndex: 1,
          explanation: 'since(〜から今まで)がある継続は、現在完了進行形 has been raining で表します。',
          choiceNotes: ['現在進行形は「今」だけを表し、since と組み合わせて「今までの継続」は表せません。', null, 'been のあとには動詞の -ing 形が必要です。', '現在形は習慣を表すので、since からの継続には使えません。'],
          audioEn: 'It has been raining since this morning.',
        },
        {
          id: 'u17-l1-q3',
          prompt: '誤りを含む文を選んでください。',
          choices: [
            'He has been studying in the library all day.',
            'I have been knowing her for ten years.',
            'They have been living in Sapporo since 2020.',
            'We have been waiting for the test results.',
          ],
          correctIndex: 1,
          explanation: 'know は状態動詞なので -ing 形にしません。「10年前から知っている」は I have known her for ten years. と現在完了で表します。',
          choiceNotes: ['study は動作を表す動詞なので、現在完了進行形にできます。', null, 'live は継続する動作として扱えるので、have been living は自然です。', 'wait も動作を表す動詞なので問題ありません。'],
          audioEn: 'I have known her for ten years.',
        },
        {
          id: 'u17-l1-q4',
          prompt: '空所に入る形を選んでください。',
          sentence: 'How long ___ English?',
          sentenceJa: 'どのくらいの間英語を勉強しているのですか。',
          choices: ['do you study', 'are you studying', 'have you been studying', 'you have been studying'],
          correctIndex: 2,
          explanation: 'How long で「今までの継続の長さ」を尋ねるので、現在完了進行形を使い、疑問文なので have を主語の前に出します。',
          choiceNotes: ['現在形は習慣を尋ねる形で、「今までどのくらい続けているか」は尋ねられません。', '現在進行形は「今していること」を尋ねる形で、How long(どのくらいの間)と合いません。', null, '疑問文なので have を主語 you の前に出す必要があります。'],
          audioEn: 'How long have you been studying English?',
        },
      ],
      summary: [
        '現在完了進行形は have / has been + 動詞の -ing 形で、過去に始まった動作が今まで続いていることを表す。',
        'for(期間)・since(起点)・How long(どのくらいの間)と相性がよい。',
        '否定は have / has のあとに not、疑問は have / has を主語の前に出す。',
        'know / like / want などの状態動詞は -ing にせず、現在完了(have known など)を使う。',
      ],
    },
    {
      id: 'u17-l2',
      unitId: 'u17',
      level: 'B1+',
      title: '現在完了 vs 現在完了進行形',
      objective: '「やり終えた結果」なのか「続けている動作」なのかに注目して、現在完了と現在完了進行形を正しく使い分けられるようになります。',
      minutes: 12,
      prereqs: ['u17-l1'],
      blocks: [
        {
          type: 'explanation',
          title: '結果を伝えるか、作業を伝えるか',
          body:
            'このレッスンでは、**やり終えた結果を伝えるか、続けてきた作業を伝えるか**を比べます。\n\n- I **have painted** the kitchen. → 台所を塗り終えました。完成した結果に注目しています。\n- I **have been painting** the kitchen. → 台所を塗っていたところです。作業に注目し、完成したかどうかは述べていません。\n\n現在完了進行形は、今も作業中の場合にも、少し前にやめた場合にも使えます。また、現在完了がいつも「完了」を意味するわけではありません。I **have known** her for years. のように状態の継続も表します。',
        },
        {
          type: 'timeline',
          title: '2つの形の時間イメージ',
          timelines: [
            {
              title: 'I have painted the kitchen.',
              point: 80,
              pointLabel: '塗り終えた',
              caption: '動作はすでに完了していて、「きれいになったキッチン」という結果が今あります。',
            },
            {
              title: 'I have been painting the kitchen.',
              range: [60, 100],
              rangeLabel: '塗り続けている',
              arrowToNow: true,
              caption: '動作が今まで続いています。終わったかどうかは言っていません。',
            },
          ],
        },
        {
          type: 'contrast',
          title: '結果の現在完了 vs 継続動作の現在完了進行形',
          left: {
            label: '現在完了(結果・完成)',
            items: [
              { en: 'I have painted the kitchen.', ja: 'キッチンのペンキ塗りを終えました。', highlight: 'have painted' },
              { en: 'She has fixed her bike.', ja: '彼女は自転車を修理し終えました。', highlight: 'has fixed' },
            ],
            pointJa: '「やり終えた」という結果・完成に注目',
          },
          right: {
            label: '現在完了進行形(継続する動作)',
            items: [
              { en: 'I have been painting the kitchen all afternoon.', ja: '午後はずっとキッチンのペンキを塗っています。', highlight: 'have been painting' },
              { en: 'She has been fixing her bike since noon.', ja: '彼女は正午からずっと自転車を修理しています。', highlight: 'has been fixing' },
            ],
            pointJa: '「ずっとしている」という動作の継続に注目。終わったかどうかは言っていない',
          },
          note: '同じ動詞でも、形を変えるだけで「完成の報告」か「作業の途中経過」かが変わります。',
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: "I've written five emails this morning.", ja: '今朝はメールを5通書きました。', highlight: "I've written", note: '「5通」のように完了した数や量を言うときは現在完了です。' },
            { en: "I've been writing emails all morning.", ja: '午前中ずっとメールを書いています。', highlight: "I've been writing", note: '何通書けたかではなく、動作の継続に注目しています。' },
            { en: 'Your eyes are red. Have you been crying?', ja: '目が赤いですよ。泣いていたのですか。', highlight: 'Have you been crying', note: '今残っている痕跡から、直前まで続いていた動作を尋ねる使い方です。' },
            { en: 'Someone has eaten my cake!', ja: '誰かが私のケーキを食べてしまいました。', highlight: 'has eaten', note: '「ケーキがなくなった」という結果に注目しています。' },
            { en: 'We have lived in Nagoya for ten years.', ja: '私たちは名古屋に10年住んでいます。', highlight: 'have lived', note: 'live / work では have lived と have been living の意味の差はほとんどありません。' },
          ],
        },
        {
          type: 'explanation',
          title: '両方使える場合と、結果を言い切りたい場合',
          body:
            'live / work では、継続をどちらの形でも表せることがあります。\n\n- We **have lived** here for ten years.\n- We **have been living** here for ten years.\n\nどちらも「ここに10年間住んでいます」です。進行形は、続けてきた活動や一時的な状況を強調することがあります。know のような状態動詞は通常進行形にせず、I **have known** her for years. とします。\n\n「3章読み終えた」と**完成した量**を伝えるなら I **have read** three chapters. です。I **have been reading** three chapters. は、その3章を読む作業について述べる形で、読み終えたという報告にはなりません。数量があれば常に進行形が誤り、というわけではありません。',
        },
      ],
      quiz: [
        {
          id: 'u17-l2-q1',
          prompt: '空所に入る形を選んでください。',
          sentence: 'I ___ three chapters of this book so far.',
          sentenceJa: 'この本をここまでで3章読みました。',
          choices: ['have been reading', 'have read', 'am reading', 'read'],
          correctIndex: 1,
          explanation: '「3章」という完了した量を報告しているので、結果に注目する現在完了 have read を使います。',
          choiceNotes: ['現在完了進行形は動作の継続に注目する形で、「3章」という完了した量の報告には使えません。', null, '現在進行形では「ここまでに読み終えた量」を表せません。', 'so far(今までのところ)は現在とつながる表現なので、過去形とは合いません。'],
          audioEn: 'I have read three chapters of this book so far.',
        },
        {
          id: 'u17-l2-q2',
          prompt: '会話の返事として最も自然な文を選んでください。',
          sentence: "You're out of breath. — ___",
          sentenceJa: '「息が切れていますね」—「駅からずっと走ってきたんです」',
          choices: ['I have been running from the station.', 'I have run from the station.', 'I am running from the station.', 'I was running from the station.'],
          correctIndex: 0,
          explanation: '息が切れているという「今ある痕跡」の理由として、たった今まで続いていた動作を表す現在完了進行形が最も自然です。',
          choiceNotes: [null, 'have run は「走り終えた」という結果の報告になり、息切れの理由の説明としては have been running のほうが自然です。', '今は立ち止まって話しているので、「今走っている最中」の現在進行形は合いません。', '過去進行形では「たった今まで」という現在とのつながりが切れてしまいます。'],
          audioEn: 'I have been running from the station.',
        },
        {
          id: 'u17-l2-q3',
          prompt: '「小説はすでに完成している」と伝わる文を選んでください。',
          choices: ['He has been writing a novel.', 'He has written a novel.', 'He is writing a novel.', 'He was writing a novel.'],
          correctIndex: 1,
          explanation: 'has written は「書き上げた」という完了・結果を表します。has been writing は「ずっと書いている」という継続で、完成したかどうかは伝えません。',
          choiceNotes: ['「ずっと書いている」という継続で、まだ完成していない可能性が高い言い方です。', null, '「今書いている最中」なので、完成していません。', '「過去のある時点で書いている最中だった」という意味で、完成は伝わりません。'],
          audioEn: 'He has written a novel.',
        },
        {
          id: 'u17-l2-q4',
          prompt: '空所に入る形を選んでください。',
          sentence: 'We ___ each other since high school.',
          sentenceJa: '私たちは高校時代からの知り合いです。',
          choices: ['have been knowing', 'have known', 'are knowing', 'know'],
          correctIndex: 1,
          explanation: 'know は状態動詞なので進行形にしません。「高校から今まで」という継続でも、状態動詞は現在完了 have known で表します。',
          choiceNotes: ['状態動詞 know は -ing 形にできません。', null, '状態動詞は現在進行形にもしません。', 'since high school(高校から今まで)という継続には、現在形ではなく現在完了を使います。'],
          audioEn: 'We have known each other since high school.',
        },
      ],
      summary: [
        '現在完了は「やり終えた結果・完成」、現在完了進行形は「続けている動作そのもの」に注目する。',
        '回数や量(three chapters / five emails など)を報告するときは現在完了。',
        '今ある痕跡(息切れ・汚れなど)の理由を説明するときは現在完了進行形が自然。',
        'live / work では両方の形が使えて意味はほぼ同じ。状態動詞(know / like など)は現在完了だけ。',
      ],
    },
  ],
}
