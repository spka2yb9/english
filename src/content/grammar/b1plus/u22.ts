import type { GrammarUnit } from '../../types'

// U22 第3条件文と wish — 過去の非現実、wish / if only、条件文1〜3型の総合練習
// 前提: u15(第1・第2条件文)の知識

export const u22: GrammarUnit = {
  id: 'u22',
  level: 'B1+',
  title: '第3条件文と wish',
  lessons: [
    {
      id: 'u22-l1',
      unitId: 'u22',
      level: 'B1+',
      title: '第3条件文',
      objective: '「If + had + 過去分詞, would have + 過去分詞」を使って、「もし〜していたら…だっただろう」という実際とは違う過去を表現できるようになります。',
      minutes: 12,
      prereqs: ['u15-l4'],
      blocks: [
        {
          type: 'explanation',
          title: '変えられない過去を巻き戻して想像する',
          body:
            '「あのとき知っていたら、電話したのに」— 実際には知らなかったし、電話もしなかった。こんなふうに**すでに終わった過去を頭の中で巻き戻して、別の展開を想像する**のが第3条件文です。\n\n- If I **had known**, I **would have called** you.(知っていたら、電話していたのに)\n\n実際に起きたことの反対を語るので、後悔・安堵・言い訳の場面でとてもよく使われます。if節は had + 過去分詞、主節は would have + 過去分詞。どちらも「現実からの距離」を表すために、時制を一段深くずらした形です。',
        },
        {
          type: 'structure',
          title: '第3条件文の形',
          parts: [
            { label: 'if節(実際とは違う過去の条件)', text: 'If I had known about the meeting,' },
            { label: '主節(実際とは違う過去の結果)', text: 'I would have attended.' },
          ],
          caption: 'if節と主節はどちらを先に置いても構いません。主節が先のときはコンマを打ちません。',
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'If I had known about the meeting, I would have attended.', ja: 'その会議のことを知っていたら、出席していました。', highlight: 'had known' },
            { en: 'If we had left ten minutes earlier, we would have caught the train.', ja: '10分早く出ていたら、あの電車に乗れていました。', highlight: 'would have caught' },
            { en: 'She would have passed the exam if she had studied a little harder.', ja: 'もう少し熱心に勉強していたら、彼女は試験に受かっていたでしょう。', note: '主節を先に置く語順も自然です。' },
            { en: "If it hadn't rained, we would have had the barbecue in the garden.", ja: '雨が降っていなかったら、庭でバーベキューをしていたのですが。', highlight: "hadn't rained", note: '否定は had not(hadn\'t)+ 過去分詞です。' },
            { en: 'If you had asked me, I could have lent you the money.', ja: '頼んでくれていたら、そのお金を貸せたのに。', highlight: 'could have lent', note: '主節では would の代わりに could(〜できたのに)や might(〜したかもしれない)も使えます。' },
          ],
        },
        {
          type: 'timeline',
          title: '第2条件文と第3条件文の時間の違い',
          timelines: [
            {
              title: 'If I had more money, I would buy a new car.(第2条件文)',
              point: 100,
              pointLabel: '今の現実と違う想像',
              caption: '想像しているのは「今」のこと。現実は違いますが、この先変わる余地はあります。',
            },
            {
              title: 'If I had known, I would have called you.(第3条件文)',
              point: 35,
              pointLabel: '知らなかった(過去の事実)',
              caption: '想像しているのは「過去」のこと。すでに終わっていて、もう変えられません。',
            },
          ],
        },
        {
          type: 'contrast',
          title: '第2条件文 vs 第3条件文',
          left: {
            label: '第2条件文(今の非現実)',
            items: [
              { en: 'If I had her number, I would call her.', ja: '彼女の番号を知っていれば、電話するのですが。', highlight: 'would call' },
              { en: "If I weren't so busy, I would help you.", ja: 'こんなに忙しくなければ、手伝うのですが。', highlight: "weren't" },
            ],
            pointJa: 'If + 過去形, would + 原形。「今」の現実と違う想像。',
          },
          right: {
            label: '第3条件文(過去の非現実)',
            items: [
              { en: 'If I had had her number, I would have called her.', ja: '彼女の番号を知っていたら、電話していたのですが。', highlight: 'had had' },
              { en: "If I hadn't been so busy, I would have helped you.", ja: 'あんなに忙しくなかったら、手伝えていたのですが。', highlight: "hadn't been" },
            ],
            pointJa: 'If + had + 過去分詞, would have + 過去分詞。終わってしまった「過去」への想像。',
          },
          note: '同じ内容でも、「今ならまだ間に合う話」なら第2条件文、「もう終わってしまった話」なら第3条件文です。had had は「had(持っていた)を had でさらに過去へずらした」形です。',
        },
        {
          type: 'explanation',
          title: "会話の 'd に注意",
          body:
            "会話では第3条件文は短縮されて発音されます。**If I'd known, I'd have called you.** のように同じ 'd が並びますが、**if節の 'd は had**、**主節の 'd は would** です。would have は would've と短くなり、「ウダヴ」程度にしか聞こえません。\n\nもう1つ大事な注意点: **if節の中に would を入れない**ことです。\n\n- × If I **would have known**, I would have called you.\n- ○ If I **had known**, I would have called you.\n\n主節とif節で役割が違うことを意識してください。",
        },
      ],
      quiz: [
        {
          id: 'u22-l1-q1',
          prompt: '空所に入る形を選んでください。',
          sentence: 'If I ___ about the traffic, I would have taken the train.',
          sentenceJa: '渋滞のことを知っていたら、電車で行ったのですが。',
          choices: ['know', 'knew', 'had known', 'would know'],
          correctIndex: 2,
          explanation: '主節が would have taken(実際とは違う過去の結果)なので、if節は had + 過去分詞にします。実際には渋滞を知らなかった、という話です。',
          choiceNotes: ['現在形では、すでに終わった過去への想像を表せません。', '過去形だと第2条件文になり、「今」の想像になってしまいます。主節の would have taken と合いません。', null, 'if節の中に would は入れません。'],
          audioEn: 'If I had known about the traffic, I would have taken the train.',
        },
        {
          id: 'u22-l1-q2',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「もっと早く家を出ていたら、飛行機に乗り遅れなかったのに」と言いたいとき。',
          choices: [
            "If we had left home earlier, we wouldn't have missed the flight.",
            "If we left home earlier, we wouldn't miss the flight.",
            "If we had left home earlier, we didn't miss the flight.",
            "If we would have left home earlier, we wouldn't have missed the flight.",
          ],
          correctIndex: 0,
          explanation: '実際とは違う過去(実際は乗り遅れた)なので、if節は had + 過去分詞、主節は would have + 過去分詞の第3条件文にします。',
          choiceNotes: [null, '第2条件文なので「(いつも・これから)もっと早く出れば乗り遅れないのに」という今の話になってしまいます。', '主節が過去形のままでは「想像」ではなく事実の報告になり、文がかみ合いません。', 'if節の中に would have は入れられません。had left が正しい形です。'],
          audioEn: "If we had left home earlier, we wouldn't have missed the flight.",
        },
        {
          id: 'u22-l1-q3',
          prompt: 'この文から分かる実際の出来事を選んでください。',
          sentence: 'If she had taken that job, she would have moved to New York.',
          choices: [
            '彼女はその仕事に就き、ニューヨークへ引っ越した',
            '彼女はその仕事に就かず、ニューヨークへも引っ越さなかった',
            '彼女はこれからその仕事に就くかどうか迷っている',
            '彼女は仕事には就かなかったが、ニューヨークへは引っ越した',
          ],
          correctIndex: 1,
          explanation: '第3条件文は実際に起きたことの反対を想像する形です。「就いていたら引っ越していただろう」= 実際は就かなかったし、引っ越しもしなかった、と分かります。',
          choiceNotes: ['実際に起きたことなら過去形で She took the job and moved to New York. と言います。', null, 'これからの迷いなら第1・第2条件文を使います。had taken は終わった過去の話です。', '主節も「実際とは違う結果」を表すので、引っ越したという事実は読み取れません。'],
          audioEn: 'If she had taken that job, she would have moved to New York.',
        },
        {
          id: 'u22-l1-q4',
          prompt: '空所に入る語句を選んでください。',
          sentence: 'If you had told me about the problem, I ___ you.',
          sentenceJa: 'その問題のことを話してくれていたら、手伝えたのに。',
          choices: ['can help', 'could have helped', 'could helped', 'had helped'],
          correctIndex: 1,
          explanation: '「〜できたのに(実際はできなかった)」は could have + 過去分詞で表します。第3条件文の主節では would のほかに could や might も使えます。',
          choiceNotes: ['can help は「(今)手伝える」という現在の話で、過去への想像に合いません。', null, 'could のあとに過去分詞を直接は続けられません。have が必要です。', 'had helped は if節で使う形です。主節には would / could / might have + 過去分詞を使います。'],
          audioEn: 'If you had told me about the problem, I could have helped you.',
        },
      ],
      summary: [
        '第3条件文は「If + had + 過去分詞, would have + 過去分詞」で、実際とは違う過去を想像する。',
        '実際に起きたことの反対を語るので、後悔・安堵・言い訳の場面でよく使う。',
        'if節の中に would は入れない。× If I would have known',
        '主節では would の代わりに could have(〜できたのに)/ might have(〜したかもしれない)も使える。',
        "会話では If I'd known(had)/ I'd have called(would)のように短縮される。",
      ],
    },
    {
      id: 'u22-l2',
      unitId: 'u22',
      level: 'B1+',
      title: 'wish / if only',
      objective: 'wish のあとの動詞の形を切り替えて、「今〜ならいいのに」という願望と「あのとき〜していればよかった」という後悔を表現できるようになります。',
      minutes: 10,
      prereqs: ['u22-l1'],
      blocks: [
        {
          type: 'explanation',
          title: '現実と違うことは、動詞を一つ昔にずらす',
          body:
            'wish は「現実はそうではない」と分かっていることへの願望を表します。仕組みは条件文とまったく同じで、**現実との距離を、時制を一段ずらすことで表します**。\n\n- I wish I **had** more time.(今、時間がない → 過去形にずらす)\n- I wish I **had studied** harder.(あのとき勉強しなかった → had + 過去分詞にずらす)\n\n第2条件文と同じずらし方なら「今への願望」、第3条件文と同じずらし方なら「過去への後悔」。この対応を押さえれば、wish は新しく覚えることがほとんどありません。',
        },
        {
          type: 'table',
          title: 'wish の時制対応',
          headers: ['伝えたいこと', '形', '例'],
          rows: [
            ['今の現実が違えばいいのに', 'wish + 過去形', 'I wish I had more time.'],
            ['過去にこうしていればよかった', 'wish + had + 過去分詞', 'I wish I had studied harder.'],
            ['人や状況に変わってほしい(不満)', 'wish + would + 原形', 'I wish he would listen to me.'],
          ],
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'I wish I had more time for my hobbies.', ja: '趣味のための時間がもっとあればいいのですが。', highlight: 'had' },
            { en: 'I wish I were better at explaining things.', ja: '説明がもっと上手だったらいいのですが。', highlight: 'were', note: 'wish のあとの be動詞は、主語が I や she でも were を使うのが基本です。' },
            { en: 'I wish I had taken more photos on that trip.', ja: 'あの旅行でもっと写真を撮っておけばよかったです。', highlight: 'had taken' },
            { en: 'I wish you had told me about the change earlier.', ja: 'その変更のことをもっと早く教えてくれていたらよかったのに。', highlight: 'had told' },
            { en: 'I wish this printer would stop jamming.', ja: 'このプリンター、いいかげん紙詰まりをやめてほしいのですが。', highlight: 'would stop' },
            { en: 'If only I had brought my camera.', ja: 'カメラを持ってきてさえいれば。', highlight: 'If only' },
          ],
        },
        {
          type: 'explanation',
          title: 'wish + would と if only',
          body:
            '相手や周りの状況に「変わってほしいのに変わらない」といういらだち・不満は **wish + 人/物 + would + 原形**で表します。\n\n- I wish my neighbor **would turn down** the music.(隣人が音楽の音量を下げてくれたらいいのに)\n\n注意点は、**自分自身には使わない**ことです。自分の状態には wish + 過去形を使います。\n\n- × I wish I would be taller. → ○ I wish I **were** taller.\n\n**if only** は wish をさらに強めた言い方で、時制のずらし方のルールは wish と同じです。\n\n- If only I **had brought** my camera.(カメラを持ってきてさえいれば)',
        },
        {
          type: 'contrast',
          title: 'hope と wish の使い分け',
          left: {
            label: 'hope(実現しうる期待)',
            items: [
              { en: 'I hope you pass the exam.', ja: '試験に合格するといいですね。', highlight: 'hope' },
              { en: "I hope it doesn't rain tomorrow.", ja: '明日、雨が降らないといいのですが。', highlight: 'hope' },
            ],
            pointJa: 'まだどうなるか分からないことへの期待。あとの動詞はふつうの時制のまま。',
          },
          right: {
            label: 'wish(現実と違う願望)',
            items: [
              { en: 'I wish you lived closer to us.', ja: 'あなたがもっと近くに住んでいたらいいのに。', highlight: 'lived' },
              { en: "I wish it weren't raining right now.", ja: '今まさに雨が降っていなければいいのに。', highlight: "weren't raining" },
            ],
            pointJa: '現実は違うと分かっていることへの願望。動詞を一つ昔にずらす。',
          },
          note: '明日の天気はまだ分からないので hope、今降っている雨は変えられない現実なので wish。「実現の見込みがあるかどうか」が分かれ目です。',
        },
      ],
      quiz: [
        {
          id: 'u22-l2-q1',
          prompt: '空所に入る形を選んでください。',
          sentence: 'I wish I ___ how to drive.',
          sentenceJa: '車の運転ができたらいいのですが。',
          choices: ['know', 'knew', 'had known', 'would know'],
          correctIndex: 1,
          explanation: '「今、運転の仕方を知らない」という現在の現実への願望なので、動詞を一つ昔にずらして過去形 knew にします。',
          choiceNotes: ['wish のあとは動詞を一つ昔にずらします。現在形のままでは使えません。', null, 'had known だと「あのとき知っていればよかった」という過去への後悔になります。', '自分自身のことに wish + would は使いません。would は相手や状況への不満に使います。'],
          audioEn: 'I wish I knew how to drive.',
        },
        {
          id: 'u22-l2-q2',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「あのとき彼女の連絡先を聞いておけばよかった」と言いたいとき。',
          choices: [
            'I wish I asked for her contact information.',
            'I wish I had asked for her contact information.',
            'I wish I would ask for her contact information.',
            'I hope I asked for her contact information.',
          ],
          correctIndex: 1,
          explanation: '過去への後悔は wish + had + 過去分詞で表します。過去のことなので、過去形からさらにもう一段ずらした形です。',
          choiceNotes: ['wish + 過去形は「今〜ならいいのに」という現在への願望になってしまいます。', null, '自分の過去の行動に wish + would は使えません。', 'hope は実現しうることへの期待で、「〜すればよかった」という後悔は表せません。'],
          audioEn: 'I wish I had asked for her contact information.',
        },
        {
          id: 'u22-l2-q3',
          prompt: 'この文が伝える内容として正しいものを選んでください。',
          sentence: 'I wish my brother would clean his room.',
          choices: [
            '弟は今、部屋を掃除しているところだ',
            '弟が部屋を掃除しないことに不満を持っている',
            '弟は昔、よく部屋を掃除していたものだ',
            '弟が部屋を掃除してくれたことに感謝している',
          ],
          correctIndex: 1,
          explanation: 'wish + 人 + would は「変わってほしいのに変わらない」という不満・いらだちを表します。実際には弟は掃除をしていません。',
          choiceNotes: ['今まさに進行中の動作なら My brother is cleaning his room. と言います。', null, '過去の習慣の would(よく〜したものだ)とは別物で、I wish と組み合わせると不満の意味になります。', '感謝の表現ではありません。実際には掃除をしてくれていないのです。'],
          audioEn: 'I wish my brother would clean his room.',
        },
        {
          id: 'u22-l2-q4',
          prompt: '空所に入る語を選んでください。',
          sentence: 'Good luck tomorrow. I ___ you get the job.',
          sentenceJa: '明日、頑張ってください。その仕事が決まるといいですね。',
          choices: ['wish', 'hope', 'wished', 'am wishing'],
          correctIndex: 1,
          explanation: '結果がまだ分からない、実現しうることへの期待なので hope を使います。hope のあとの動詞はふつうの時制のままです。',
          choiceNotes: ['wish のあとに現在形 get をそのまま続けることはできません。実現しうる期待には hope を使います。', null, '今の気持ちを伝えているので、過去形 wished は合いません。', 'この意味の wish は進行形にできません。そもそもここでは hope が必要です。'],
          audioEn: 'Good luck tomorrow. I hope you get the job.',
        },
      ],
      summary: [
        'wish のあとは動詞を一つ昔にずらす。今への願望は過去形、過去への後悔は had + 過去分詞。',
        'wish + 人/物 + would は「変わってほしい」という不満。自分自身には使わない。',
        'if only は wish の強調版。時制のずらし方は同じ。',
        '実現しうることへの期待は hope、現実と違う願望は wish。',
      ],
    },
    {
      id: 'u22-l3',
      unitId: 'u22',
      level: 'B1+',
      title: '条件文 総合練習(1〜3型)',
      objective: '文脈から「現実的な話か、今の非現実か、過去の非現実か」を判断し、第1〜第3条件文を正しく選んで使い分けられるようになります。',
      minutes: 12,
      prereqs: ['u22-l2'],
      blocks: [
        {
          type: 'explanation',
          title: '時制ではなく「現実かどうか」で選ぶ',
          body:
            '条件文の型を選ぶとき、最初に考えるのは時制ではなく次の2つです。\n\n- **実際に起こりうる話か、それとも「現実は違う」と分かっている想像か**\n- **いつのことか(これから/今/過去)**\n\n起こりうる話なら第1条件文。現実と違う想像なら、今・これからのことは第2、終わった過去のことは第3です。\n\nなお「いつでも成り立つ事実」にはゼロ条件文(If you heat ice, it melts.)を使います。迷ったら「話し手はこれを本当に起こりうると思っているか?」と自問するのが近道です。',
        },
        {
          type: 'table',
          title: '条件文の全体マップ',
          headers: ['型', 'if節の形', '主節の形', '使う場面'],
          rows: [
            ['ゼロ条件文', '現在形', '現在形', 'いつでも成り立つ事実'],
            ['第1条件文', '現在形', 'will + 原形', 'これから実際に起こりうること'],
            ['第2条件文', '過去形', 'would + 原形', '今・これからの非現実な想像'],
            ['第3条件文', 'had + 過去分詞', 'would have + 過去分詞', '実際とは違う過去'],
          ],
        },
        {
          type: 'examples',
          title: '4つの型を並べて確認',
          items: [
            { en: 'If you mix blue and yellow, you get green.', ja: '青と黄色を混ぜると緑になります。', note: 'ゼロ条件文。いつでも成り立つ事実です。' },
            { en: "If the weather is nice this weekend, we'll go hiking.", ja: '今週末天気がよければ、ハイキングに行きます。', highlight: 'is', note: '第1条件文。実際にありそうな話です。' },
            { en: 'If I won the lottery, I would travel around the world.', ja: '宝くじが当たったら、世界中を旅行するのですが。', highlight: 'won', note: '第2条件文。まず当たらない、と思いながらの想像です。' },
            { en: 'If I had taken that flight, I would have been stuck at the airport all night.', ja: 'あの便に乗っていたら、一晩中空港で足止めされていたでしょう。', highlight: 'had taken', note: '第3条件文。実際には乗りませんでした。' },
          ],
        },
        {
          type: 'contrast',
          title: '現実の話か、想像の話か',
          left: {
            label: '現実的 → 第1条件文',
            items: [
              { en: "If I finish work early, I'll join you for dinner.", ja: '仕事が早く終わったら、夕食に合流します。', highlight: 'finish' },
              { en: 'If you press this button, the machine will stop.', ja: 'このボタンを押せば、機械は止まります。', highlight: 'press' },
            ],
            pointJa: '話し手が「十分ありうる」と思っている条件。if節は現在形。',
          },
          right: {
            label: '非現実 → 第2・第3条件文',
            items: [
              { en: 'If I spoke French, I would apply for that job.', ja: 'フランス語が話せたら、その仕事に応募するのですが。', highlight: 'spoke' },
              { en: 'If you had pressed that button, the machine would have stopped.', ja: 'あのボタンを押していたら、機械は止まっていたはずです。', highlight: 'had pressed' },
            ],
            pointJa: '「現実は違う」と分かっている条件。今のことは過去形、過去のことは had + 過去分詞。',
          },
          note: '動詞の形が過去へずれるほど、現実からの距離が遠くなるイメージです。形は過去でも、話している時間は過去とは限りません。',
        },
        {
          type: 'explanation',
          title: '同じ未来の話でも、気持ちで型が変わる',
          body:
            '明日のことなのに第2条件文を使う、ということが実際の会話ではよく起こります。\n\n- If I **have** time tomorrow, I **will help** you.(手伝える見込みがそれなりにある)\n- If I **had** time tomorrow, I **would help** you.(実際はほぼ無理そう。遠回しな断りにも聞こえる)\n\n第2条件文の過去形は「過去の時間」ではなく**現実との距離**を表します。だから未来のことにも使えるのです。この控えめな響きを利用して、丁寧な提案や断りにもよく使われます。',
        },
      ],
      quiz: [
        {
          id: 'u22-l3-q1',
          prompt: '空所に入る形を選んでください。',
          sentence: 'If I ___ you, I would apologize to her right away.',
          sentenceJa: '私があなたなら、今すぐ彼女に謝ります。',
          choices: ['am', 'were', 'had been', 'will be'],
          correctIndex: 1,
          explanation: '「私があなた」というのは現実にはあり得ない今の想像なので、第2条件文の were を使います。If I were you は助言の決まり文句です。',
          choiceNotes: ['現実にはあり得ない想像なので、現在形は使えません。', null, 'had been だと「あのとき私があなただったら」という過去の話になり、right away(今すぐ)と合いません。', 'if節の中に will は入れません。'],
          audioEn: 'If I were you, I would apologize to her right away.',
        },
        {
          id: 'u22-l3-q2',
          prompt: '空所に入る形を選んでください。',
          sentence: 'We got lost on the way. If we ___ the map before leaving, we would have arrived on time.',
          sentenceJa: '途中で道に迷ってしまいました。出発前に地図を確認していたら、時間どおりに着いていたでしょう。',
          choices: ['check', 'checked', 'had checked', 'would check'],
          correctIndex: 2,
          explanation: 'すでに道に迷ったあとで、実際とは違う過去を振り返っています。第3条件文なので if節は had + 過去分詞です。',
          choiceNotes: ['現在形では、終わってしまった過去への想像を表せません。', '過去形だと第2条件文になり、主節の would have arrived と型が合いません。', null, 'if節の中に would は入れません。'],
          audioEn: 'We got lost on the way. If we had checked the map before leaving, we would have arrived on time.',
        },
        {
          id: 'u22-l3-q3',
          prompt: '状況に合う文を選んでください。',
          sentenceJa: '空が曇ってきました。「雨が降ったら試合は中止になります」と、実際にありそうなこととして伝えたいとき。',
          choices: [
            'If it rains, the game will be canceled.',
            'If it rained, the game would be canceled.',
            'If it had rained, the game would have been canceled.',
            'If it will rain, the game will be canceled.',
          ],
          correctIndex: 0,
          explanation: '話し手は雨を「実際に起こりうること」と考えているので、第1条件文(If + 現在形, will)を使います。',
          choiceNotes: [null, '第2条件文だと「実際には降りそうにないけれど」という想像に聞こえ、目の前の曇り空に合いません。', '第3条件文は終わってしまった過去の話です。', 'if節の中では、未来のことでも現在形を使います。will は入れません。'],
          audioEn: 'If it rains, the game will be canceled.',
        },
        {
          id: 'u22-l3-q4',
          prompt: '話し手が「実際にはその仕事に就けなかった」と分かる文を選んでください。',
          choices: [
            "If I get the job, I'll move to Tokyo.",
            'If I got the job, I would move to Tokyo.',
            'If I had gotten the job, I would have moved to Tokyo.',
            'I hope I get the job.',
          ],
          correctIndex: 2,
          explanation: '第3条件文は実際とは違う過去を表すので、「仕事に就けず、東京にも引っ越さなかった」という結果まで読み取れます。',
          choiceNotes: ['第1条件文で、結果はまだ分かっていません。', '第2条件文は「就けそうにないが、もし就けたら」という今の想像で、結果はまだ出ていません。', null, 'hope は「就けるといいな」という期待で、結果はまだ分かりません。'],
          audioEn: 'If I had gotten the job, I would have moved to Tokyo.',
        },
      ],
      summary: [
        '型選びは「実際に起こりうるか/想像か」と「いつの話か」の2つで決める。',
        '起こりうる → 第1(現在形 + will)。今の非現実 → 第2(過去形 + would)。過去の非現実 → 第3(had 過去分詞 + would have 過去分詞)。',
        'if節の中に will / would は入れない。未来のことでも if節は現在形。',
        '第2条件文の過去形は時間ではなく「現実との距離」。未来のことにも使え、丁寧な断りにもなる。',
      ],
    },
  ],
}
