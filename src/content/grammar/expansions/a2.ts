import type { LessonExpansionMap } from './types'

export const a2Expansions = {
  'u01-l1': {
    explanationTitle: 'be動詞を選ぶときの考え方',
    explanationBody:
      "be動詞は、主語を代名詞に置き換えると選びやすくなります。**I なら am、you / we / they なら are、he / she / it なら is** です。you は相手が1人でも are を使います。Tom and Mia は they、my phone は it と考えましょう。\n\n疑問文では Is she busy? のように be動詞を主語の前へ出します。短い肯定の答えは Yes, I am. とし、Yes, I'm. とは言いません。否定の答えは No, I'm not. / No, she isn't. のように短縮できます。",
    examples: [
      { en: 'My parents are at the station.', ja: '私の両親は駅にいます。', highlight: 'are', note: 'my parents は they に置き換えられる複数の主語です。' },
      { en: 'This soup is too salty.', ja: 'このスープは塩辛すぎます。', highlight: 'is' },
      { en: 'Are your keys in the front pocket?', ja: '鍵は前のポケットにありますか。', highlight: 'Are' },
    ],
  },
  'u01-l2': {
    explanationTitle: '現在形が表す「いつもの世界」',
    explanationBody:
      '現在形は「今この瞬間」だけを写す形ではなく、習慣・繰り返し・変わりにくい事実を述べる形です。every day や usually がなくても、文脈が日課や性質なら現在形を選びます。\n\n三単現を判断するときは、主語を he / she / it に置き換えられるか確認します。長い主語でも My sister and her friend なら they なので原形です。一方、The bus to the airport は1台を指す it なので leaves のように -s を付けます。',
    examples: [
      { en: 'My brother takes the train to work.', ja: '兄は電車で通勤します。', highlight: 'takes' },
      { en: 'Water boils at one hundred degrees Celsius.', ja: '水は摂氏100度で沸騰します。', highlight: 'boils', note: '変わらない事実にも現在形を使います。' },
      { en: 'Aya studies English after dinner.', ja: 'アヤは夕食後に英語を勉強します。', highlight: 'studies' },
    ],
  },
  'u01-l3': {
    explanationTitle: '疑問・否定では役割を分担する',
    explanationBody:
      '一般動詞の疑問文と否定文では、時制や三単現の情報を do / does が担当し、内容を表す動詞は原形になります。つまり Does Ken plays では情報が二重です。Does Ken play のように、-s は does だけに持たせます。\n\n疑問詞が付いても仕組みは同じで、Where does she work? の順です。答えるときは Yes, she does. / No, she does not. とヘルパーを再利用できます。be動詞の文には do を足さない、という境界も毎回確認しましょう。',
    examples: [
      { en: 'Does your sister drive to work?', ja: 'あなたのお姉さんは車で通勤しますか。', highlight: 'Does' },
      { en: "We don't need a reservation.", ja: '私たちには予約は必要ありません。', highlight: "don't need" },
      { en: 'Why does this machine make that noise?', ja: 'なぜこの機械はあの音を立てるのですか。', highlight: 'does this machine make' },
    ],
  },
  'u01-l4': {
    explanationTitle: '長い文も骨組みから組み立てる',
    explanationBody:
      '英語では、まず **誰が・どうする・何を** という骨組みを完成させ、そのあとに場所や時間を足します。日本語の語順につられて Yesterday at the office I the report finished. のようにせず、I finished the report を先に作るのがコツです。\n\n頻度を表す usually などは一般動詞の前、場所と時間は多くの場合「場所 → 時間」の順に置きます。ただし最も強調したい時間は Yesterday, ... のように文頭へ出せます。語順は単語の役割を示すため、位置を変えると意味も変わり得ます。',
    examples: [
      { en: 'The manager sent the team an update yesterday.', ja: 'マネージャーは昨日チームに最新情報を送りました。', highlight: 'The manager sent the team an update' },
      { en: 'The children played soccer in the park after school.', ja: '子どもたちは放課後、公園でサッカーをしました。', highlight: 'played soccer in the park after school' },
      { en: 'I usually read the news on the train.', ja: '私はたいてい電車でニュースを読みます。', highlight: 'usually read' },
    ],
  },
  'u02-l1': {
    explanationTitle: '進行形は一時的な場面を切り取る',
    explanationBody:
      '現在進行形は、話している瞬間だけでなく、「今週」「最近」のような現在を含む一時的な期間にも使えます。永続的な性質ではなく、始まりと終わりのある活動をカメラで切り取るイメージです。\n\n形は be動詞 + -ing の2部品なので、be動詞を落とさないことが重要です。疑問文では Is she working?、否定文では She is not working. と、疑問・否定を担当するのは be動詞です。つづりの変化も write → writing、run → running のようにまとまりで覚えましょう。',
    examples: [
      { en: 'The customers are waiting outside.', ja: 'お客さんたちは外で待っています。', highlight: 'are waiting' },
      { en: 'I am staying with my aunt this week.', ja: '今週はおばの家に滞在しています。', highlight: 'am staying', note: '一時的な滞在なので進行形です。' },
      { en: 'Is the baby sleeping now?', ja: '赤ちゃんは今寝ていますか。', highlight: 'Is the baby sleeping' },
    ],
  },
  'u02-l2': {
    explanationTitle: '文脈の時間幅を見極める',
    explanationBody:
      '現在形と現在進行形の選択では、動作そのものよりも **どの時間幅について話しているか** を見ます。I work in Tokyo. は普段の勤務先、I am working in Tokyo this month. は今月だけの一時的な状況です。\n\nknow・believe・want・need・belong などは動作ではなく状態を表すため、通常は進行形にしません。ただし think は「意見を持つ」なら現在形、「検討する」なら進行形のように、意味が変わると形も変わります。時間表現と動詞の意味をセットで判断してください。',
    examples: [
      { en: 'I usually work from home, but I am working at the office today.', ja: '普段は在宅勤務ですが、今日はオフィスで働いています。', highlight: 'usually work' },
      { en: 'Mina knows the answer.', ja: 'ミナは答えを知っています。', highlight: 'knows', note: 'know は状態を表すため、通常は進行形にしません。' },
      { en: 'We are thinking about moving closer to the station.', ja: '私たちは駅の近くへ引っ越すことを検討しています。', highlight: 'are thinking' },
    ],
  },
  'u02-l3': {
    explanationTitle: '過去形は「終わった時間」と結びつく',
    explanationBody:
      '過去形は、出来事が現在より前の、すでに終わった時間に属することを示します。yesterday や last year が明示されなくても、会話の中で「旅行中の出来事」など過去の枠が共有されていれば過去形です。\n\n否定・疑問では did が過去を担当するため、動詞は原形に戻ります。Did you went ではなく Did you go、did not saw ではなく did not see です。不規則形は肯定文だけで現れ、did がある文では原形になると整理すると混乱が減ります。',
    examples: [
      { en: 'We saw a beautiful rainbow after the storm.', ja: '嵐のあとに美しい虹を見ました。', highlight: 'saw' },
      { en: "Leo didn't bring his lunch yesterday.", ja: 'レオは昨日昼食を持ってきませんでした。', highlight: "didn't bring" },
      { en: 'Did you enjoy the concert last night?', ja: '昨夜のコンサートは楽しかったですか。', highlight: 'Did you enjoy' },
    ],
  },
  'u02-l4': {
    explanationTitle: '背景と出来事を別の時制で描く',
    explanationBody:
      '過去進行形は、過去のある時点にカメラを置き、そのとき途中だった動作を背景として見せます。そこへ短い出来事が入るときは、背景を was / were doing、割り込んだ出来事を過去形で表すのが基本です。\n\nwhile は長く続く動作同士、when は短い出来事との組み合わせでよく使われますが、機械的な決まりではありません。大切なのは、話し手がどちらを「進行中の場面」として見せたいかです。同時に続いていた2動作なら両方を過去進行形にもできます。',
    examples: [
      { en: 'I was cooking dinner when the phone rang.', ja: '電話が鳴ったとき、私は夕食を作っていました。', highlight: 'was cooking' },
      { en: 'While Ken was washing the dishes, I was drying them.', ja: 'ケンが皿を洗っている間、私はそれを拭いていました。', highlight: 'was washing' },
      { en: 'Were you sleeping when I sent the message?', ja: '私がメッセージを送ったとき、寝ていましたか。', highlight: 'Were you sleeping' },
    ],
  },
  'u02-l5': {
    explanationTitle: 'will が生まれる瞬間に注目する',
    explanationBody:
      'will は単なる未来マークではありません。話している場で決めたこと、話し手の考えによる予測、相手への申し出・約束に向いています。電話が鳴った瞬間に I will get it. と言うのは、その場で担当すると決めたからです。\n\nすでに準備済みの予定には別の未来表現が自然なことがあります。will を選ぶ前に「決定は今生まれたか」「これは個人的な予測か」「相手に何かを申し出ているか」と考えると、意味のある使い分けになります。否定の will not は unwillingness、つまり「どうしてもしない」という拒否を表すこともあります。',
    examples: [
      { en: 'I think the new café will be popular.', ja: 'その新しいカフェは人気が出ると思います。', highlight: 'will be' },
      { en: 'The doorbell is ringing. I will answer it.', ja: '玄関のベルが鳴っています。私が出ます。', highlight: 'will answer', note: '今、その場で決めた行動です。' },
      { en: 'I will carry that box for you.', ja: 'その箱を運びますよ。', highlight: 'will carry' },
    ],
  },
  'u02-l6': {
    explanationTitle: '計画と目に見える根拠を表す',
    explanationBody:
      'be going to は、発話より前に決めていた意図・計画を表します。日時や予約まで確定していなくても、「そうするつもり」がすでにあれば使えます。形の中心は going ではなく、主語に合う be動詞を含む be going to + 原形です。\n\n予測では、黒い雲やふらつく荷物など、現在見えている根拠から近い未来を読むときに自然です。単なる意見の I think it will ... と対照的です。ただし実際の会話では重なる場面もあり、まず「事前の意図または現在の証拠があるか」を判断軸にしましょう。',
    examples: [
      { en: 'We are going to repaint the kitchen this weekend.', ja: '今週末、キッチンを塗り直すつもりです。', highlight: 'are going to repaint' },
      { en: 'Look at that glass. It is going to fall.', ja: 'あのグラスを見て。落ちそうです。', highlight: 'is going to fall', note: '今見えている状況が予測の根拠です。' },
      { en: 'Are you going to apply for the job?', ja: 'その仕事に応募するつもりですか。', highlight: 'Are you going to apply' },
    ],
  },
  'u03-l1': {
    explanationTitle: '数えるときは「単位」が必要か考える',
    explanationBody:
      '可算・不可算は日本語の感覚だけでは決まりません。英語では、境界のある1個として数えるものは可算名詞、材料・情報・活動などをまとまりとして扱うものは不可算名詞です。同じ語でも coffee が飲み物なら不可算、a coffee が1杯なら可算になることがあります。\n\n不可算名詞を具体的に数えるときは a piece of advice、two bottles of water のように単位を添えます。information や furniture に複数の -s を直接付けないことも重要です。辞書の C と U の表示を確認する習慣を付けると、冠詞や数量表現も正しく選べます。',
    examples: [
      { en: 'She gave me two useful pieces of advice.', ja: '彼女は役に立つ助言を2つくれました。', highlight: 'two useful pieces of advice' },
      { en: 'We need more information before we decide.', ja: '決める前に、もっと情報が必要です。', highlight: 'more information' },
      { en: 'There are three apples in the basket.', ja: 'かごの中にリンゴが3個あります。', highlight: 'three apples' },
    ],
  },
  'u03-l2': {
    explanationTitle: '文字ではなく最初の音を聞く',
    explanationBody:
      'a / an の選択は、次の単語のつづりではなく **発音の最初の音** で決まります。母音の音で始まる an hour や an honest person、子音の音で始まる a university や a European country が代表例です。\n\na / an は「聞き手がまだ特定できない1つ」を会話へ初めて登場させる働きもあります。その後、同じものを再び指すときは the に変わるのが自然です。また職業を述べる He is a designer. のように、単数可算名詞を裸のまま置かないことも確認しましょう。',
    examples: [
      { en: 'We waited for an hour.', ja: '私たちは1時間待ちました。', highlight: 'an hour', note: 'hour は h を発音せず、母音の音で始まります。' },
      { en: 'She studies at a university in Boston.', ja: '彼女はボストンの大学で学んでいます。', highlight: 'a university' },
      { en: 'My uncle is an honest person.', ja: '私のおじは正直な人です。', highlight: 'an honest person' },
    ],
  },
  'u03-l3': {
    explanationTitle: 'the は聞き手と対象を共有する合図',
    explanationBody:
      'the は「有名なもの」だけでなく、話し手と聞き手がどれを指すか特定できるという合図です。一度話に出たもの、その場に1つしかないもの、後ろの説明で限定されたものには the を使います。Please close the door. では、その部屋のどのドアか共有できています。\n\n一方、複数名詞や不可算名詞で種類全体を一般論として述べるときは無冠詞です。Dogs need exercise. は犬一般、The dogs need exercise. は特定の犬たちです。冠詞を選ぶときは「相手はどれか分かるか」「個別の対象か種類全体か」を確認しましょう。',
    examples: [
      { en: 'I bought a lamp, and the lamp is beside my bed.', ja: 'ランプを1つ買い、そのランプはベッドの横にあります。', highlight: 'the lamp', note: '2回目なので、どのランプか特定できます。' },
      { en: 'Please turn off the lights when you leave.', ja: '出るときは電気を消してください。', highlight: 'the lights', note: 'その部屋の電気はお互いにどれか分かるので the です。' },
      { en: 'Books can take us to different worlds.', ja: '本は私たちをさまざまな世界へ連れていってくれます。', highlight: 'Books', note: '本という種類全体なので無冠詞です。' },
    ],
  },
  'u03-l4': {
    explanationTitle: '文の種類だけでなく話し手の意図を見る',
    explanationBody:
      'some は肯定文、any は疑問文・否定文が基本ですが、形式だけで機械的に決めないことが大切です。相手が受け入れると期待して勧める Would you like some tea? や、存在すると考えて頼む Can I have some water? では疑問文でも some を使います。\n\nmany は可算複数、much は不可算と組みます。会話の肯定文では a lot of がどちらにも使えて自然です。数量をたずねる How many books / How much time でも、直後の名詞が数えられるかどうかが判断基準になります。',
    examples: [
      { en: 'Would you like some soup?', ja: 'スープはいかがですか。', highlight: 'some soup', note: '勧める疑問文なので some が自然です。' },
      { en: "We don't have any clean towels.", ja: '清潔なタオルが1枚もありません。', highlight: 'any clean towels' },
      { en: 'How much time do we have?', ja: '時間はどのくらいありますか。', highlight: 'How much time' },
    ],
  },
  'u04-l1': {
    explanationTitle: '代名詞は文中の席で形が決まる',
    explanationBody:
      '代名詞は同じ人を指していても、文の中の席によって形が変わります。動作をする主語の席は I / she / they、動詞や前置詞の後ろの目的語の席は me / her / them、名詞の前は my / her / their です。\n\nmine や yours は「私のもの」「あなたのもの」と名詞まで含むため、後ろに名詞を置きません。This is my bag. と This bag is mine. を対にして覚えると区別できます。長い文では、まず代名詞が何の代わりかではなく、その位置でどんな役割をしているかを見ましょう。',
    examples: [
      { en: 'They invited us to dinner.', ja: '彼らは私たちを夕食に招きました。', highlight: 'us' },
      { en: 'This seat is hers, and that one is mine.', ja: 'この席は彼女のもので、あちらは私のものです。', highlight: 'hers' },
      { en: 'Please send the photos to him.', ja: 'その写真を彼に送ってください。', highlight: 'him', note: '前置詞 to の後ろなので目的格です。' },
    ],
  },
  'u04-l2': {
    explanationTitle: '距離は物理的な遠さだけではない',
    explanationBody:
      'this / these は話し手の近く、that / those は遠くにあるものを指します。まず単数か複数かを決め、次に近いか遠いかを選べば4語を整理できます。指示語を名詞の前に置く場合も、This book / These books のように数を一致させます。\n\n距離は物理的なものだけではありません。電話で名乗る This is Mika.、少し前に話題に出た内容を That sounds great. と受けるように、会話上の近さ・遠さにも使います。相手の近くにある物を Is that your bag? と指す感覚も覚えておきましょう。',
    examples: [
      { en: 'These cookies are still warm.', ja: 'このクッキーはまだ温かいです。', highlight: 'These cookies' },
      { en: 'Who is that man by the gate?', ja: '門のそばにいるあの男性は誰ですか。', highlight: 'that man' },
      { en: 'That sounds like a good plan.', ja: 'それはよい計画に思えます。', highlight: 'That', note: '直前に聞いた内容全体を指しています。' },
    ],
  },
  'u04-l3': {
    explanationTitle: 'one は名詞の代わり、it は特定の物',
    explanationBody:
      'it は、すでに話題に出た同じ物を指します。I lost my pen, but I found it. なら、見つけたのはなくしたペンです。one は数えられる単数名詞の代わりで、I need a pen. Do you have one? なら「ペンを1本持っていますか」です。\n\n**one がいつも別の物を指すわけではありません**。This is the one I bought yesterday. なら「これは昨日買ったものです」と、同じ物を説明できます。one / ones には the red one / the cheaper ones のように説明を添えられます。不可算名詞の代わりには通常使わず、water なら some water や some と表します。',
    examples: [
      { en: 'This chair is uncomfortable. Can I use that one?', ja: 'この椅子は座り心地が悪いです。あちらの椅子を使ってもいいですか。', highlight: 'that one' },
      { en: 'I like the blue shoes more than the black ones.', ja: '黒い靴より青い靴のほうが好きです。', highlight: 'the black ones' },
      { en: 'I found my wallet, but I left it at home again.', ja: '財布を見つけましたが、また家に置いてきました。', highlight: 'it', note: '同じ財布そのものを指します。' },
    ],
  },
  'u05-l1': {
    explanationTitle: '形容詞が説明する相手を確認する',
    explanationBody:
      '形容詞は、名詞の前でその名詞を直接説明するか、be・look・feel・become などの後ろで主語の状態を説明します。a quiet room と The room is quiet. では位置は違っても、quiet が説明するのはどちらも room です。\n\n英語の形容詞には複数形がなく、two reds cars とはしません。また複数の形容詞を並べるときも、まずは size・color などをすべて暗記するより、a small black bag のような頻出のまとまりを例文で身につけるのが実用的です。名詞を説明している語か、動作を説明している語かも見分けましょう。',
    examples: [
      { en: 'They live in a small wooden house.', ja: '彼らは小さな木造の家に住んでいます。', highlight: 'small wooden house' },
      { en: 'The children look tired after the trip.', ja: '旅行のあと、子どもたちは疲れているように見えます。', highlight: 'look tired' },
      { en: 'We watched an interesting documentary.', ja: '私たちは興味深いドキュメンタリーを見ました。', highlight: 'interesting documentary' },
    ],
  },
  'u05-l2': {
    explanationTitle: '何を詳しくする語なのかをたどる',
    explanationBody:
      '形容詞は名詞や主語の状態を、副詞は動詞・形容詞・別の副詞を詳しくします。She is a careful driver. では driver を説明する careful、She drives carefully. では drives のしかたを説明する carefully です。\n\nすべての副詞が -ly になるわけではありません。fast・hard・late は形容詞と副詞が同じ形で、hardly は「ほとんど〜ない」という別の意味です。また look / feel / sound の後ろは主語の状態を述べるので形容詞を使います。空所の直前だけでなく、どの語を修飾するかをたどって判断しましょう。',
    examples: [
      { en: 'Nora explained the problem clearly.', ja: 'ノラはその問題を分かりやすく説明しました。', highlight: 'clearly' },
      { en: 'This train is incredibly fast.', ja: 'この電車は信じられないほど速いです。', highlight: 'incredibly', note: '副詞が形容詞 fast の程度を強めています。' },
      { en: 'The flowers smell sweet.', ja: 'その花は甘い香りがします。', highlight: 'sweet' },
    ],
  },
  'u05-l3': {
    explanationTitle: 'be動詞だけ位置が違うと覚える',
    explanationBody:
      'always・usually・often・sometimes・rarely・never などは、基本的に一般動詞の前、be動詞の後ろです。助動詞や完了形がある場合は、最初の助動詞の後ろに置きます。この「最初の動詞の種類」を見ると、長い文でも位置を決めやすくなります。\n\nsometimes は文頭や文末にも置けますが、never はすでに否定の意味を持つため do not never のように二重否定にしません。頻度をより具体的に示す every day や twice a week は通常文末です。割合のイメージと語順を一緒に覚えましょう。',
    examples: [
      { en: 'Our team usually meets on Monday mornings.', ja: '私たちのチームはたいてい月曜の朝に集まります。', highlight: 'usually meets' },
      { en: 'Sam is rarely late for class.', ja: 'サムは授業にめったに遅れません。', highlight: 'is rarely' },
      { en: 'Our neighbors are never noisy at night.', ja: '近所の人たちは夜に騒ぐことがありません。', highlight: 'are never', note: 'be動詞の後ろに置きます。' },
    ],
  },
  'u06-l1': {
    explanationTitle: '知りたい部分を疑問詞に置き換える',
    explanationBody:
      'Wh疑問文は、元の文で知りたい部分を what / where / when などに置き換え、その疑問詞を文頭へ移すと考えると作りやすくなります。You work at the library. の at the library を where に変えれば Where do you work? です。\n\n疑問詞の後ろは通常の疑問文の形なので、一般動詞なら do / does / did、be動詞なら be動詞を主語の前へ置きます。why への答えは because、how は方法や状態を尋ねます。疑問詞だけで満足せず、その後ろのヘルパーと動詞の形まで一まとまりで確認しましょう。',
    examples: [
      { en: 'Where did you put the spare key?', ja: '予備の鍵をどこに置きましたか。', highlight: 'Where did you put' },
      { en: 'Why is the store closed today?', ja: 'なぜ今日はその店が閉まっているのですか。', highlight: 'Why is' },
      { en: 'What does this button do?', ja: 'このボタンは何をするものですか。', highlight: 'What does this button do' },
    ],
  },
  'u06-l2': {
    explanationTitle: 'How の後ろの語が答えの単位を決める',
    explanationBody:
      'How の後ろに置く語は、求める情報の種類を指定します。How long は時間の長さや物の長さ、How often は頻度、How far は距離、How much は量・価格です。日本語ではどれも「どのくらい」になりやすいので、期待する答えの単位から逆算しましょう。\n\nHow many の後ろには可算名詞の複数形、How much の後ろには不可算名詞を置きます。How old や How tall のように形容詞を続けたあとも、文全体は疑問文の語順です。質問だけでなく For two years. / Twice a month. など典型的な答えと対で練習すると定着します。',
    examples: [
      { en: 'How often do you call your grandparents?', ja: 'どのくらいの頻度で祖父母に電話しますか。', highlight: 'How often' },
      { en: 'How far is the hotel from the airport?', ja: 'ホテルは空港からどのくらい離れていますか。', highlight: 'How far' },
      { en: 'How many guests are coming tonight?', ja: '今夜は何人のお客さんが来ますか。', highlight: 'How many guests', note: 'guest は数えられるので複数形を使います。' },
    ],
  },
  'u06-l3': {
    explanationTitle: '空所が主語なら do を足さない',
    explanationBody:
      '主語を尋ねる疑問文では、Who / What 自体が「動作をする人・もの」の席に座ります。そのため普通の肯定文と同じ語順で Who called? とし、do / does / did を追加しません。答えを Someone called. と仮置きすると、空所が主語かどうかを確認できます。\n\n一方 Who did you call? では you が主語として残り、who は目的語なので did が必要です。主語を尋ねる who は通常単数扱いで、現在形なら Who wants ...? のように三単現の -s を付けます。「誰が」と「誰を」を日本語訳だけでなく文の骨組みで見分けましょう。',
    examples: [
      { en: 'Who left this note on my desk?', ja: '誰が私の机にこのメモを置きましたか。', highlight: 'Who left' },
      { en: 'What caused the delay?', ja: '何が遅れの原因になりましたか。', highlight: 'What caused' },
      { en: 'Who wants the last slice of pizza?', ja: '最後の一切れのピザが欲しい人は誰ですか。', highlight: 'Who wants', note: '主語を尋ねる who は通常単数扱いです。' },
    ],
  },
} satisfies LessonExpansionMap
