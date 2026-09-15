import type { GrammarUnit } from '../../types'

// U16 接続詞と文の結合 — 理由・結果・譲歩(because / so / although)、時の接続詞、相関接続詞の3レッスン。
// 「接続詞は文と文の関係を示すラベル」というイメージを軸にする。

export const u16: GrammarUnit = {
  id: 'u16',
  level: 'B1',
  title: '接続詞と文の結合',
  lessons: [
    {
      id: 'u16-l1',
      unitId: 'u16',
      level: 'B1',
      title: 'because / so / although',
      objective: 'because / so / although を使って2つの文を1つに結合し、理由・結果・譲歩の関係を正しく伝えられるようになります。',
      minutes: 10,
      prereqs: ['u01-l3'],
      blocks: [
        {
          type: 'explanation',
          title: '接続詞は文と文をつなぐ「ラベル」',
          body:
            'It was raining. I stayed home. と短い文を並べるだけでも意味は通じますが、2つの文の**関係**(なぜ?それでどうした?)は伝わりません。接続詞は2つの文を1つに結合し、その関係を示すラベルの働きをします。\n\n- **because**: 後ろに「理由」が来る(〜だから)\n- **so**: 後ろに「結果」が来る(だから〜)\n- **although**: 後ろに「予想を裏切る事実」が来る(〜だけれども)\n\n同じ2つの文でも、どの接続詞でつなぐかで「何を伝えたいか」が変わります。',
        },
        {
          type: 'structure',
          title: '文の結合のしくみ',
          parts: [
            { label: '文A(結果)', text: 'I stayed home' },
            { label: '接続詞', text: 'because' },
            { label: '文B(理由)', text: 'it was raining' },
          ],
          caption: '接続詞のあとには必ず「主語 + 動詞」のそろった文が続きます。because なら後ろに理由、so なら後ろに結果が来ます。',
        },
        {
          type: 'table',
          title: 'because / so / although の使い分け',
          headers: ['接続詞', '後ろに来るもの', '意味', '例'],
          rows: [
            ['because', '理由・原因', '〜だから', 'I stayed home because it was raining.'],
            ['so', '結果', 'だから〜', 'It was raining, so I stayed home.'],
            ['although', '譲歩(〜なのに、それでも)', '〜だけれども', 'Although it was raining, I went out.'],
          ],
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'I went to bed early because I was tired.', ja: '疲れていたので早く寝ました。', highlight: 'because' },
            { en: 'It started to rain, so we went inside.', ja: '雨が降り出したので、私たちは中に入りました。', highlight: 'so', note: 'so の前にはカンマを置くのがふつうです。' },
            { en: 'Although the restaurant was expensive, the food was disappointing.', ja: 'そのレストランは高かったのに、料理はがっかりでした。', highlight: 'Although' },
            { en: 'Because the train was delayed, I missed the meeting.', ja: '電車が遅れたため、会議に間に合いませんでした。', highlight: 'Because', note: 'because の節を文頭に置くときは、カンマで区切ります。' },
            { en: 'He kept working although he was sick.', ja: '彼は体調が悪いのに働き続けました。', highlight: 'although', note: 'although の節は文の後半にも置けます。' },
          ],
        },
        {
          type: 'contrast',
          title: 'because と so は向きが逆',
          left: {
            label: 'because(理由を後ろに)',
            items: [
              { en: 'I took a taxi because I was late.', ja: '遅れていたのでタクシーに乗りました。', highlight: 'because I was late' },
            ],
            pointJa: 'because のあとに「原因・理由」を置く',
          },
          right: {
            label: 'so(結果を後ろに)',
            items: [
              { en: 'I was late, so I took a taxi.', ja: '遅れていたので、タクシーに乗りました。', highlight: 'so I took a taxi' },
            ],
            pointJa: 'so のあとに「結果」を置く',
          },
          note: '伝える内容は同じでも、後ろに置くものが逆です。日本語の「〜だから、だから…」につられて because と so を同じ文で重ねることはできません(× Because I was late, so I took a taxi.)。',
        },
        {
          type: 'explanation',
          title: 'although の注意点',
          body:
            'although は「〜だけれども」という**譲歩**を表し、後ろの節の内容から予想されることを本文がくつがえします。but と意味は近いですが、置く場所が違います。\n\n- but は文と文の間に置く: I had a cold, **but** I went to work.\n- although は節の頭に置く: **Although** I had a cold, I went to work.\n\n日本語の「〜だけれども、しかし…」につられて **although と but を同時に使うのは誤り**です(× Although I had a cold, but I went to work.)。どちらか1つで逆接は完成します。\n\nなお、会話では although の代わりに though もよく使われます。意味は同じです。',
        },
      ],
      quiz: [
        {
          id: 'u16-l1-q1',
          prompt: '空所に入る語を選んでください。',
          sentence: "I couldn't sleep last night, ___ I'm very tired today.",
          sentenceJa: '昨夜眠れなかったので、今日はとても疲れています。',
          choices: ['because', 'so', 'although', 'until'],
          correctIndex: 1,
          explanation: '空所の後ろは「疲れている」という結果です。前半が理由、後半が結果の流れなので so を使います。',
          choiceNotes: ['because の後ろには理由が来ます。ここでは後ろが結果なので向きが逆です。', null, 'although だと「眠れなかったのに疲れている」という不自然な逆接になります。', 'until は「〜まで」という時の接続詞で、理由と結果の関係は表せません。'],
          audioEn: "I couldn't sleep last night, so I'm very tired today.",
        },
        {
          id: 'u16-l1-q2',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「熱があったのに、彼女は学校に行きました」と言いたいとき。',
          choices: [
            'Although she had a fever, but she went to school.',
            'Although she had a fever, she went to school.',
            'She had a fever, so she went to school.',
            'Because she had a fever, she went to school.',
          ],
          correctIndex: 1,
          explanation: '「〜なのに」という譲歩は although で表します。although だけで逆接は完成するので、but を重ねません。',
          choiceNotes: ['although と but を同じ文で重ねることはできません。どちらか1つにします。', null, 'so だと「熱があったから学校に行った」という因果関係になり、意味が通りません。', 'because だと「熱があったことが登校の理由」になってしまい、不自然です。'],
          audioEn: 'Although she had a fever, she went to school.',
        },
        {
          id: 'u16-l1-q3',
          prompt: '次の文から読み取れることを選んでください。',
          sentence: 'Although the hotel was cheap, the rooms were very clean.',
          choices: [
            '「安いホテルは部屋が清潔でないことが多い」という予想が話し手の頭にある。',
            'そのホテルは高かった。',
            '部屋はあまり清潔ではなかった。',
            '部屋が清潔だったのは、ホテルが安かったからだ。',
          ],
          correctIndex: 0,
          explanation: 'although は「予想に反して」という感覚を含みます。「安いのに清潔だった」と言えるのは、「安ければ清潔でないことが多い」という予想が背景にあるからです。',
          choiceNotes: [null, 'cheap(安かった)と述べています。', 'very clean(とても清潔だった)と述べています。', 'although は理由ではなく「予想外の対比」を表します。因果関係は述べていません。'],
          audioEn: 'Although the hotel was cheap, the rooms were very clean.',
        },
        {
          id: 'u16-l1-q4',
          prompt: '空所に入る語を選んでください。',
          sentence: 'We canceled the picnic ___ the weather was terrible.',
          sentenceJa: '天気がひどかったので、ピクニックを中止しました。',
          choices: ['so', 'because', 'although', 'but'],
          correctIndex: 1,
          explanation: '空所の後ろは「天気がひどかった」という中止の理由です。理由を後ろに置くのは because です。',
          choiceNotes: ['so の後ろには結果が来ます。ここでは後ろが理由なので向きが逆です。', null, 'although だと「天気がひどかったのに中止した」という不自然な意味になります。', 'but は逆接なので、素直な因果関係のこの文には合いません。'],
          audioEn: 'We canceled the picnic because the weather was terrible.',
        },
      ],
      summary: [
        'because の後ろは理由、so の後ろは結果。同じ内容でも接続詞によって後ろに置くものが逆になる。',
        'because と so、although と but を同じ文で重ねて使わない。1つで関係は完成する。',
        'although は「〜だけれども」という譲歩。予想に反する展開を示し、節は文頭にも文の後半にも置ける。',
        '接続詞の節を文頭に置いたときは、カンマで区切る。',
      ],
    },
    {
      id: 'u16-l2',
      unitId: 'u16',
      level: 'B1',
      title: 'when / while / until / as soon as',
      objective: '時の接続詞で2つの出来事の時間関係を表し、未来の内容でも時の節では現在形を使えるようになります。',
      minutes: 10,
      prereqs: ['u16-l1'],
      blocks: [
        {
          type: 'explanation',
          title: '時の接続詞は出来事を時間軸の上で結ぶ',
          body:
            'when(〜するとき)、while(〜する間に)、until(〜するまでずっと)、as soon as(〜したらすぐに)は、2つの出来事の**時間の関係**を示す接続詞です。\n\n- **when**: 2つの出来事が重なる「時点」を指す\n- **while**: ある出来事が続いている「期間」の中で、もう1つが起きる\n- **until**: ある時点まで状態や動作が**続く**\n- **as soon as**: 1つの出来事の**直後に**もう1つが起きる\n\nどれも because や although と同じく、後ろに「主語 + 動詞」の文が続きます。',
        },
        {
          type: 'table',
          title: '4つの時の接続詞',
          headers: ['接続詞', '意味', 'イメージ', '例'],
          rows: [
            ['when', '〜するとき', '2つの出来事が重なる時点', 'Call me when you arrive.'],
            ['while', '〜する間に', '続いている期間の中で起きる', 'She called while you were out.'],
            ['until', '〜するまでずっと', 'その時点まで継続する', 'Wait here until I come back.'],
            ['as soon as', '〜したらすぐに', '直後に起きる', "I'll call you as soon as I get home."],
          ],
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'When I opened the door, the cat ran out.', ja: 'ドアを開けたとき、猫が飛び出しました。', highlight: 'When' },
            { en: 'Someone knocked on the door while I was taking a shower.', ja: 'シャワーを浴びている間に、誰かがドアをノックしました。', highlight: 'while', note: 'while のあとは進行形がよく使われます。' },
            { en: "Let's wait here until the rain stops.", ja: '雨がやむまでここで待ちましょう。', highlight: 'until' },
            { en: "I'll send you a message as soon as the tickets go on sale.", ja: 'チケットが発売されたらすぐにメッセージを送ります。', highlight: 'as soon as' },
            { en: 'He listened to music while he cooked dinner.', ja: '彼は夕食を作りながら音楽を聞いていました。', highlight: 'while' },
          ],
        },
        {
          type: 'explanation',
          title: '未来の話でも、時の節は現在形',
          body:
            'U12で学んだルールがここでも生きています。**when / while / until / as soon as の節の中では、未来のことでも will を使わず現在形**にします。\n\n- I\'ll call you **as soon as I get** home.(× as soon as I will get)\n- Let\'s wait **until the rain stops**.(× until the rain will stop)\n\n「メインの文(結果側)には will、時の節には現在形」という役割分担です。',
        },
        {
          type: 'contrast',
          title: 'when と while の使い分け',
          left: {
            label: 'when(時点)',
            items: [
              { en: 'When the movie ended, we left.', ja: '映画が終わったとき、私たちは帰りました。', highlight: 'When the movie ended' },
              { en: 'I was cooking when the phone rang.', ja: '電話が鳴ったとき、私は料理をしていました。', highlight: 'when the phone rang' },
            ],
            pointJa: '「その瞬間・その時点」を指す。短い出来事と相性がよい',
          },
          right: {
            label: 'while(期間)',
            items: [
              { en: 'The phone rang while I was cooking.', ja: '料理をしている間に電話が鳴りました。', highlight: 'while I was cooking' },
              { en: 'While we were in Kyoto, we visited three temples.', ja: '京都にいる間に、3つのお寺を訪れました。', highlight: 'While we were in Kyoto' },
            ],
            pointJa: '「続いている期間」を指す。進行形や状態と相性がよい',
          },
          note: 'when + 短い出来事、while + 続いている動作・状態、が基本の組み合わせです。',
        },
      ],
      quiz: [
        {
          id: 'u16-l2-q1',
          prompt: '空所に入る表現を選んでください。',
          sentence: 'Please wait in the lobby ___ your name is called.',
          sentenceJa: 'お名前が呼ばれるまでロビーでお待ちください。',
          choices: ['until', 'as soon as', 'while', 'so'],
          correctIndex: 0,
          explanation: '「名前が呼ばれる」という時点まで「待つ」状態が続くので、継続の終点を示す until を使います。',
          choiceNotes: [null, 'as soon as だと「呼ばれたらすぐに待つ」という順序の合わない意味になります。', 'while だと「呼ばれている間だけ待つ」という不自然な意味になります。', 'so は結果を導く接続詞で、時間の関係は表せません。'],
          audioEn: 'Please wait in the lobby until your name is called.',
        },
        {
          id: 'u16-l2-q2',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「家に着いたらすぐに電話します」と言いたいとき。',
          choices: [
            "I'll call you as soon as I will get home.",
            "I'll call you as soon as I get home.",
            "I call you as soon as I'll get home.",
            "I'll call you as soon as I got home.",
          ],
          correctIndex: 1,
          explanation: '時の節(as soon as 以下)では、未来のことでも現在形を使います。will はメインの文にだけ付けます。',
          choiceNotes: ['as soon as の節の中に will は入れられません。', null, 'will の位置が逆です。メインの文に will、時の節に現在形を使います。', 'got は過去形なので、これからのことには使えません。'],
          audioEn: "I'll call you as soon as I get home.",
        },
        {
          id: 'u16-l2-q3',
          prompt: '空所に入る語を選んでください。',
          sentence: 'The lights went out ___ we were eating dinner.',
          sentenceJa: '夕食を食べている間に電気が消えました。',
          choices: ['while', 'until', 'as soon as', 'because'],
          correctIndex: 0,
          explanation: '「食べている」という続いている期間の中で「電気が消えた」という出来事が起きたので、期間を表す while を使います。',
          choiceNotes: [null, 'until は「〜まで続く」を表しますが、went out は一瞬の出来事なので合いません。', 'as soon as は「〜した直後に」という順序を表し、進行中の状態 were eating とはかみ合いません。', 'because だと「食べていたから電気が消えた」という不自然な因果関係になります。'],
          audioEn: 'The lights went out while we were eating dinner.',
        },
        {
          id: 'u16-l2-q4',
          prompt: '次の文の意味として正しいものを選んでください。',
          sentence: "Don't turn on your phone until the plane lands.",
          choices: [
            '飛行機が着陸するまでは、電話の電源を入れてはいけない。',
            '飛行機が着陸したあとも、電話の電源を入れてはいけない。',
            '飛行機が着陸する前に、電話の電源を入れなければならない。',
            '飛行機の中ではいつでも電話を使ってよい。',
          ],
          correctIndex: 0,
          explanation: "Don't ... until は「〜するまでは…しない」という意味です。着陸という時点で「電源を入れない」状態が終わり、そのあとは入れてかまいません。",
          choiceNotes: [null, 'until は「その時点まで」を表すので、着陸後は電源を入れてよいことになります。', '順序が逆です。着陸の前は電源を入れられません。', '着陸までは使えないと言っているので、意味が逆です。'],
          audioEn: "Don't turn on your phone until the plane lands.",
        },
      ],
      summary: [
        'when は「時点」、while は「期間」、until は「〜までずっと」、as soon as は「〜したらすぐに」。',
        'while のあとは進行形や続いている状態と相性がよい。when は短い出来事と組み合わせる。',
        '時の節の中では、未来のことでも will を使わず現在形にする。',
        'not ... until は「〜までは…しない」。その時点を境に状況が変わる。',
      ],
    },
    {
      id: 'u16-l3',
      unitId: 'u16',
      level: 'B1',
      title: 'both A and B / either / neither',
      objective: 'both A and B / either A or B / neither A nor B を使って2つのものをまとめて表し、動詞の形を正しく合わせられるようになります。',
      minutes: 10,
      prereqs: ['u16-l2'],
      blocks: [
        {
          type: 'explanation',
          title: 'ペアで働く接続詞',
          body:
            'both ... and、either ... or、neither ... nor は、**2語がペアになって働く接続詞**です(相関接続詞と呼ばれます)。2つのものを「両方」「どちらか」「どちらも〜ない」とまとめて示せます。\n\n- **both A and B**: AもBも両方\n- **either A or B**: AかBのどちらか\n- **neither A nor B**: AもBもどちらも〜ない\n\nペアの相手は決まっています。both には and、either には or、neither には nor。組み合わせを崩すことはできません。',
        },
        {
          type: 'table',
          title: '3つのペアの整理',
          headers: ['形', '意味', '文の性質', '例'],
          rows: [
            ['both A and B', 'AもBも両方', '肯定', 'Both Ken and Mari like sushi.'],
            ['either A or B', 'AかBのどちらか', '肯定(選択)', 'You can have either tea or coffee.'],
            ['neither A nor B', 'AもBもどちらも〜ない', 'それ自体が否定(not は不要)', 'Neither Ken nor Mari eats natto.'],
          ],
        },
        {
          type: 'structure',
          title: 'AとBは同じ形をそろえる',
          parts: [
            { label: '主語 + 動詞', text: 'She is' },
            { label: 'both', text: 'both' },
            { label: 'A(形容詞)', text: 'smart' },
            { label: 'and', text: 'and' },
            { label: 'B(形容詞)', text: 'kind' },
          ],
          caption: 'AとBには同じ種類の形(名詞と名詞、形容詞と形容詞など)を入れます。× She is both smart and sings well. のように形をそろえないと不自然になります。',
        },
        {
          type: 'examples',
          title: '例文',
          items: [
            { en: 'Both my brother and my sister live in Nagoya.', ja: '兄も姉も名古屋に住んでいます。', highlight: 'Both my brother and my sister', note: 'both A and B が主語のとき、動詞は複数扱いです。' },
            { en: 'You can pay by either cash or card.', ja: '現金かカードのどちらかで支払えます。', highlight: 'either cash or card' },
            { en: 'Neither the bus nor the train runs after midnight.', ja: 'バスも電車も深夜0時以降は走っていません。', highlight: 'Neither the bus nor the train' },
            { en: 'This app is both free and easy to use.', ja: 'このアプリは無料で、しかも使いやすいです。', highlight: 'both free and easy to use' },
            { en: 'Either you or your brother has to stay home.', ja: 'あなたか弟のどちらかが家にいなければなりません。', highlight: 'has', note: '動詞は近い方(your brother)に合わせるのが基本です。' },
          ],
        },
        {
          type: 'explanation',
          title: '動詞の数と否定のルール',
          body:
            '相関接続詞で主語を作るときの注意点は2つです。\n\n**1. 動詞の数**\n\n- both A and B → 常に**複数扱い**: Both Ken and Mari **like** sushi.\n- either A or B / neither A nor B → **動詞に近い方(B)に合わせる**のが基本: Neither my parents nor my brother **knows** the truth.\n\n**2. neither は not と重ねない**\n\nneither はそれ自体が否定を表すので、not を足すと二重否定になってしまいます。\n\n- ○ I eat neither meat nor fish.\n- ○ I don\'t eat meat or fish.\n- × I don\'t eat neither meat nor fish.',
        },
        {
          type: 'contrast',
          title: 'either と neither',
          left: {
            label: 'either A or B(どちらか)',
            items: [
              { en: 'We can take either the bus or the subway.', ja: 'バスか地下鉄のどちらかで行けます。', highlight: 'either the bus or the subway' },
            ],
            pointJa: '肯定文で「どちらか一方」を選ぶ',
          },
          right: {
            label: 'neither A nor B(どちらも〜ない)',
            items: [
              { en: 'We can take neither the bus nor the subway at this hour.', ja: 'この時間はバスも地下鉄も使えません。', highlight: 'neither the bus nor the subway' },
            ],
            pointJa: '文の形は肯定のまま、意味は否定になる',
          },
          note: 'neither A nor B は、not ... either A or B(We can\'t take either the bus or the subway.)でも同じ意味を表せます。',
        },
      ],
      quiz: [
        {
          id: 'u16-l3-q1',
          prompt: '空所に入る語を選んでください。',
          sentence: 'Neither my father ___ my mother can drive.',
          sentenceJa: '父も母も車の運転ができません。',
          choices: ['or', 'nor', 'and', 'but'],
          correctIndex: 1,
          explanation: 'neither のペアの相手は nor と決まっています。組み合わせを崩すことはできません。',
          choiceNotes: ['or がペアになるのは either です。', null, 'and がペアになるのは both です。', 'but はペアで働く接続詞ではありません。'],
          audioEn: 'Neither my father nor my mother can drive.',
        },
        {
          id: 'u16-l3-q2',
          prompt: '空所に入る形を選んでください。',
          sentence: 'Both the manager and the staff ___ satisfied with the result.',
          sentenceJa: '部長もスタッフも結果に満足しています。',
          choices: ['is', 'are', 'has', 'be'],
          correctIndex: 1,
          explanation: 'both A and B が主語のときは「AとBの両方」という複数の主語なので、動詞は複数扱いの are を使います。',
          choiceNotes: ['both A and B は2つ合わせた複数の主語なので、単数の is は使えません。', null, 'satisfied(形容詞)の前に必要なのは be動詞です。has では文が成り立ちません。', '原形の be はそのまま現在の文には使えません。'],
          audioEn: 'Both the manager and the staff are satisfied with the result.',
        },
        {
          id: 'u16-l3-q3',
          prompt: '正しい文を選んでください。',
          sentenceJa: '「私は肉も魚も食べません」と言いたいとき。',
          choices: [
            "I don't eat neither meat nor fish.",
            'I eat neither meat nor fish.',
            "I don't eat both meat and fish.",
            'I eat either meat nor fish.',
          ],
          correctIndex: 1,
          explanation: 'neither ... nor はそれ自体が否定を表すので、動詞は肯定の形のまま使います。',
          choiceNotes: ["not と neither を重ねると二重否定になります。don't を使うなら meat or fish にします。", null, 'both の否定は「両方は食べない(どちらかは食べる)」という部分的な否定に聞こえてしまいます。', 'either のペアは or です。nor と組み合わせることはできません。'],
          audioEn: 'I eat neither meat nor fish.',
        },
        {
          id: 'u16-l3-q4',
          prompt: '次の文から分かることを選んでください。',
          sentence: 'Either Ken or Yuta will pick you up at the station.',
          choices: [
            '駅に迎えに来るのはケンかユウタのどちらか一人。',
            'ケンとユウタの二人そろって迎えに来る。',
            'ケンもユウタも迎えには来ない。',
            '誰かが迎えに来るかどうかは分からない。',
          ],
          correctIndex: 0,
          explanation: 'either A or B は「AかBのどちらか一方」という意味です。二人そろってではありません。',
          choiceNotes: [null, '二人とも来るなら both Ken and Yuta を使います。', 'どちらも来ないなら neither Ken nor Yuta を使います。', 'will が使われているので、どちらかが来ること自体は確実です。'],
          audioEn: 'Either Ken or Yuta will pick you up at the station.',
        },
      ],
      summary: [
        'both A and B(両方)、either A or B(どちらか)、neither A nor B(どちらも〜ない)。ペアの相手(and / or / nor)を崩さない。',
        'AとBには同じ種類の形(名詞と名詞、形容詞と形容詞など)をそろえる。',
        'both A and B が主語なら動詞は複数扱い。either / neither は動詞に近い方(B)に合わせるのが基本。',
        'neither はそれ自体が否定。not と重ねて二重否定にしない。',
      ],
    },
  ],
}
