import type { LessonExpansionMap } from './types'

export const a2PlusExpansions = {
  'u07-l1': {
    explanationTitle: '比べる2者と比較の軸をそろえる',
    explanationBody:
      '比較級では「AはBより、ある性質の程度が高い」という関係を作ります。than の前後には同じ種類のものを置き、何を比べているかが相手に分かるようにします。This train is faster than the bus. なら、速さという1つの軸で2つの交通手段を比べています。\n\n短い形容詞は -er、長い形容詞は more が基本ですが、good → better、bad → worse、far → farther / further は不規則です。同じものが時間とともに変化する場合も It is getting colder. のように比較級を使えます。than を使わなくても、文脈に比較対象があれば成立します。',
    examples: [
      { en: 'The morning flight is cheaper than the evening flight.', ja: '朝の便は夕方の便より安いです。', highlight: 'cheaper than' },
      { en: 'This explanation is more useful than the first one.', ja: 'この説明は最初のものより役に立ちます。', highlight: 'more useful than' },
      { en: 'The days are getting shorter.', ja: '日がだんだん短くなっています。', highlight: 'getting shorter', note: '同じものの変化にも比較級を使えます。' },
    ],
  },
  'u07-l2': {
    explanationTitle: '「どの範囲で一番か」まで伝える',
    explanationBody:
      '最上級は3つ以上の集団から1つを選び出す形なので、in the class や of the three のように比較の範囲を示すと意味が明確になります。場所・集団には in、数を明示したまとまりには of がよく使われます。\n\n形容詞の前には通常 the を置きますが、my best friend のように所有格がすでに名詞を限定するときは the を重ねません。one of the + 最上級 + 複数名詞は「最も〜なものの1つ」という頻出形です。best / worst など不規則形も、比較級と一緒に三段階で覚えましょう。',
    examples: [
      { en: 'February is the shortest month of the year.', ja: '2月は1年で最も短い月です。', highlight: 'the shortest month' },
      { en: 'This is one of the most popular dishes on the menu.', ja: 'これはメニューで最も人気のある料理の1つです。', highlight: 'one of the most popular dishes' },
      { en: 'Mai is my oldest friend.', ja: 'マイは私の最も古い友人です。', highlight: 'my oldest friend', note: '所有格 my があるため the は付けません。' },
    ],
  },
  'u07-l3': {
    explanationTitle: '同じ程度と差の両方を表す',
    explanationBody:
      'as + 形容詞・副詞の原級 + as は、2者の程度が同じだと述べます。比較級を中に入れず、as faster as ではなく as fast as とする点が重要です。動作のしかたを比べる場合は as carefully as のように副詞を置きます。\n\nnot as ... as は「同じ程度ではない」、つまり最初のものの程度が低いことをやわらかく伝えます。倍数を表す twice as large as や、数量と組み合わせる as many books as の形にも広げられます。完全に同じだと強調するなら just as ... as が使えます。',
    examples: [
      { en: 'The online course is as challenging as the classroom course.', ja: 'オンライン講座は教室の講座と同じくらい難しいです。', highlight: 'as challenging as' },
      { en: 'I cannot type as quickly as my coworker.', ja: '私は同僚ほど速く入力できません。', highlight: 'as quickly as' },
      { en: 'This room is twice as large as mine.', ja: 'この部屋は私の部屋の2倍の広さです。', highlight: 'twice as large as' },
    ],
  },
  'u07-l4': {
    explanationTitle: '基準を超えたのか、満たしたのか',
    explanationBody:
      'too は必要な基準を悪い方向に超え、「そのため何かができない」という含みを持ちます。very hot は単にとても暑いだけですが、too hot to drink は飲めないほど熱いという結果まで含みます。enough は形容詞・副詞の後ろ、名詞の前という位置の違いにも注意してください。\n\n比較級を強める much / far / a lot は「ずっと」、a little / slightly は「少し」という差の大きさを示します。very better とは言いません。表現を選ぶときは、単なる程度か、基準との関係か、2者間の差かを見分けましょう。',
    examples: [
      { en: 'The water is too cold to swim in.', ja: 'その水は冷たすぎて泳げません。', highlight: 'too cold to swim' },
      { en: 'We have enough chairs for everyone.', ja: '全員分の椅子が十分にあります。', highlight: 'enough chairs', note: '名詞の前に enough を置きます。' },
      { en: 'The express bus is much faster than the local bus.', ja: '急行バスは普通バスよりずっと速いです。', highlight: 'much faster' },
    ],
  },
  'u08-l1': {
    explanationTitle: '時間の幅は目安、語句のまとまりで確認する',
    explanationBody:
      '時間の at / on / in は、at seven(時刻)、on Monday(曜日・日付)、in April(月・季節・年)という組み合わせを軸に整理します。in the morning のように、1日より短い時間帯でも in を使うため、長さだけでは決まりません。\n\n特定の日の朝なら on Friday morning、一般的な夜なら at night です。「週末に」はこの教材の基本とするアメリカ英語では on the weekend、イギリス英語では at the weekend を使います。this morning / next year / every day の前には通常、前置詞を付けません。',
    examples: [
      { en: 'The meeting starts at half past nine.', ja: '会議は9時半に始まります。', highlight: 'at half past nine' },
      { en: 'Our office is closed on national holidays.', ja: '私たちの会社は祝日は休みです。', highlight: 'on national holidays' },
      { en: 'Many flowers bloom in spring.', ja: '春には多くの花が咲きます。', highlight: 'in spring' },
    ],
  },
  'u08-l2': {
    explanationTitle: '場所を点・面・内部として見る',
    explanationBody:
      '場所の at は地点、on は面との接触、in は境界の内側というイメージです。at the station は駅を待ち合わせ地点として見ており、in the station は駅舎の中にいることを強調します。同じ場所でも話し手の見方で前置詞が変わります。\n\non は水平面だけでなく on the wall や on the screen のように接触する面に使えます。交通手段では on the bus / train / plane、囲まれた小型車には in a car / taxi が一般的です。日本語訳を一語ずつ対応させず、位置関係のイメージと名詞の自然な組み合わせで覚えましょう。',
    examples: [
      { en: 'I will meet you at the main entrance.', ja: '正面入口で会いましょう。', highlight: 'at the main entrance' },
      { en: 'There is a calendar on the wall.', ja: '壁にカレンダーがあります。', highlight: 'on the wall' },
      { en: 'Your passport is in the top drawer.', ja: 'パスポートは一番上の引き出しの中にあります。', highlight: 'in the top drawer' },
    ],
  },
  'u08-l3': {
    explanationTitle: '出発点・到着点・通った経路を描く',
    explanationBody:
      '移動の前置詞は、動きのどの部分を伝えるかで選びます。to は到着点への方向、into / out of は境界を越えて中へ・外へ、across は面の一方から反対側へ、through は内部を通り抜ける動きです。位置を表す in と、移動を表す into の違いも意識しましょう。\n\n動詞との組み合わせにも注意が必要です。arrive は arrive at / in とし、arrive to とは通常言いません。enter はそれ自体に「中へ入る」を含むので enter the room と前置詞なしです。矢印を頭に描き、動詞に方向の意味がすでに含まれるかも確認してください。',
    examples: [
      { en: 'The cyclist rode across the bridge.', ja: 'その自転車の人は橋を渡りました。', highlight: 'across the bridge' },
      { en: 'We walked through the forest before sunset.', ja: '私たちは日没前に森を通り抜けました。', highlight: 'through the forest' },
      { en: 'The cat jumped out of the box.', ja: '猫が箱から飛び出しました。', highlight: 'out of the box' },
    ],
  },
  'u08-l4': {
    explanationTitle: '前置詞までを1つの語彙として覚える',
    explanationBody:
      'depend on や interested in の前置詞は、日本語訳から自由に選べる部品ではなく、前の動詞・形容詞と結びついた語彙の一部です。新しい単語を覚えるときに、短い例文や後ろに来る名詞まで含めて記録すると誤りが減ります。\n\n同じ動詞でも前置詞で意味が変わることがあります。look at は視線を向ける、look for は探す、look after は世話をする、です。また前置詞の後ろに動詞を置くなら -ing 形にします。be interested in learn ではなく be interested in learning と、次のレッスン領域にもつながります。',
    examples: [
      { en: 'This decision depends on the weather.', ja: 'この決定は天気次第です。', highlight: 'depends on' },
      { en: 'Riku is good at remembering names.', ja: 'リクは人の名前を覚えるのが得意です。', highlight: 'good at remembering' },
      { en: 'We are looking for a larger apartment.', ja: '私たちはもっと広いアパートを探しています。', highlight: 'looking for' },
    ],
  },
  'u09-l1': {
    explanationTitle: '意味が変わっても助動詞の骨組みは同じ',
    explanationBody:
      'can は能力・可能性・許可、could は過去の一般的な能力や丁寧な依頼に使われます。意味は文脈で変わりますが、後ろは必ず動詞の原形、三単現の -s は付けない、疑問文に do を使わないという骨組みは共通です。\n\nCould you ...? は過去を尋ねているのではなく、距離を置いて依頼をやわらげています。過去のある1回だけ実際に成功したことには was able to が好まれる場合がありますが、A2+ではまず could を「昔の一般的な能力」として安定して使いましょう。',
    examples: [
      { en: 'My grandmother can use video calls easily.', ja: '祖母はビデオ通話を簡単に使えます。', highlight: 'can use' },
      { en: 'Could you speak a little more slowly?', ja: 'もう少しゆっくり話していただけますか。', highlight: 'Could you speak' },
      { en: 'I could swim before I started school.', ja: '私は学校に上がる前から泳げました。', highlight: 'could swim', note: '過去の一般的な能力です。' },
    ],
  },
  'u09-l2': {
    explanationTitle: '義務の出どころと否定の意味を分ける',
    explanationBody:
      'must と have to はどちらも義務を表します。must は話し手が強く必要だと考える場面、have to は規則や状況など外部の事情を述べる場面でよく使われますが、多くの会話では重なります。過去や未来には had to / will have to を使える点が have to の強みです。\n\n最重要なのは否定です。must not は禁止、do not have to は義務がないだけで、しても構いません。「しない必要がある」のか「する必要がない」のかを日本語でも言い換えてから選びましょう。',
    examples: [
      { en: 'All visitors have to wear a name badge.', ja: '訪問者は全員、名札を着けなければなりません。', highlight: 'have to wear' },
      { en: 'You must not share this password.', ja: 'このパスワードを共有してはいけません。', highlight: 'must not share' },
      { en: "We don't have to bring any food.", ja: '私たちは食べ物を持ってくる必要はありません。', highlight: "don't have to bring", note: '持ってきてもよいですが、義務ではありません。' },
    ],
  },
  'u09-l3': {
    explanationTitle: '助言の強さと人間関係を考える',
    explanationBody:
      'should は「そうするのがよい」という一般的な助言で、相手に選択の余地を残します。had better は「そうしないと困った結果になる」という具体的な警告を含み、状況によっては強く響きます。目上の人や親しくない相手には should のほうが安全です。\n\nhad better の had は過去を表さず、現在・近い未来への忠告です。後ろは to を付けず原形、否定は had better not + 原形です。アドバイスを受ける側への配慮として、命令口調ではなく Maybe you should ... のようにさらに和らげることもできます。',
    examples: [
      { en: 'You should back up your files regularly.', ja: 'ファイルは定期的にバックアップしたほうがよいです。', highlight: 'should back up' },
      { en: 'We had better leave now, or we will miss the train.', ja: 'もう出たほうがいいです。そうしないと電車に乗り遅れます。', highlight: 'had better leave' },
      { en: 'You had better not touch that wire.', ja: 'その電線には触らないほうがいいです。', highlight: 'had better not touch' },
    ],
  },
  'u09-l4': {
    explanationTitle: '予測の確信度を言葉で調整する',
    explanationBody:
      '未来の推量では、will は話し手がそうなるとかなり強く予測するとき、may / might は可能性はあるが確信していないときに使います。might は may より控えめに感じられることがありますが、日常会話では大きく重なるため、厳密な確率として暗記する必要はありません。\n\n助動詞を2つ重ねて will might とはできません。否定は may not / might not で「〜しないかもしれない」です。副詞の maybe は文全体を修飾して Maybe it will rain. と置けますが、It maybe rain. とはしません。文法上の位置も含めて確信度を調整しましょう。',
    examples: [
      { en: 'The roads will be busy during the holiday.', ja: '休暇中は道路が混むでしょう。', highlight: 'will be' },
      { en: 'Our package may arrive this afternoon.', ja: '荷物は今日の午後に届くかもしれません。', highlight: 'may arrive' },
      { en: 'I might not have enough time tonight.', ja: '今夜は十分な時間がないかもしれません。', highlight: 'might not have' },
    ],
  },
  'u10-l1': {
    explanationTitle: 'to不定詞が示す「これから向かうこと」',
    explanationBody:
      'to不定詞には、まだ実現していない行動や目的へ向かう感覚があります。そのため want・hope・plan・decide・promise など、意志や予定を表す動詞と相性がよい形です。動詞ごとの組み合わせを want to do のようなかたまりで覚えましょう。\n\n目的を表す to do は「何のためにその行動をしたか」を加えます。否定は not to do、疑問詞と組み合わせるなら what to do / how to use it の形です。to の後ろは時制や主語に関係なく動詞の原形になることを毎回確認してください。',
    examples: [
      { en: 'We decided to postpone the picnic.', ja: '私たちはピクニックを延期することに決めました。', highlight: 'decided to postpone' },
      { en: 'I opened the window to let in some fresh air.', ja: '新鮮な空気を入れるために窓を開けました。', highlight: 'to let in', note: '窓を開けた目的を表しています。' },
      { en: 'Please tell me how to use this printer.', ja: 'このプリンターの使い方を教えてください。', highlight: 'how to use' },
    ],
  },
  'u10-l2': {
    explanationTitle: '動作を名詞の席に置く -ing',
    explanationBody:
      '動名詞は動詞に -ing を付け、動作全体を「〜すること」という名詞のかたまりとして扱う形です。主語・目的語・前置詞の後ろなど、名詞が入る席に置けます。Swimming is good exercise. では swimming 全体が主語です。\n\nenjoy・finish・avoid・mind・keep などは目的語に動名詞を取ります。enjoy to swim のように日本語の「〜すること」だけを頼りに形を選ばず、動詞との組み合わせで覚えます。動名詞でも目的語や副詞を伴い、reading books quietly のような長いかたまりを作れます。',
    examples: [
      { en: 'Cooking for friends makes me happy.', ja: '友人のために料理をすると幸せな気持ちになります。', highlight: 'Cooking for friends' },
      { en: 'Please avoid using your phone during the show.', ja: '上演中は携帯電話の使用を控えてください。', highlight: 'avoid using' },
      { en: 'Did you finish writing the email?', ja: 'メールを書き終えましたか。', highlight: 'finish writing' },
    ],
  },
  'u10-l3': {
    explanationTitle: '最初の動詞が次の形を選ぶ',
    explanationBody:
      'to不定詞と動名詞のどちらを置くかは、直前の動詞ごとに決まることが多いので、decide to do / enjoy doing のようにセットで学びます。日本語ではどちらも「〜すること」になるため、訳だけでは選べません。自分用の2列リストを作り、例文ごと覚えるのが効果的です。\n\nlike・love・hate・start・begin は両方を取れることが多く、A2+では意味の差を細かく付けすぎなくて構いません。ただし would like は必ず to不定詞です。より上のレベルでは stop や remember のように形で意味が変わる動詞を学ぶため、今は「動詞が形を支配する」という考え方を固めましょう。',
    examples: [
      { en: 'Nina hopes to study abroad next year.', ja: 'ニナは来年留学したいと思っています。', highlight: 'hopes to study' },
      { en: 'My father enjoys fixing old radios.', ja: '父は古いラジオを修理することを楽しんでいます。', highlight: 'enjoys fixing' },
      { en: 'It started raining during our walk.', ja: '散歩中に雨が降り始めました。', highlight: 'started raining', note: 'start は動名詞もto不定詞も取れます。' },
    ],
  },
  'u10-l4': {
    explanationTitle: 'to が前置詞か不定詞かを見分ける',
    explanationBody:
      '前置詞の後ろには名詞が必要なので、動作を置く場合は動名詞にします。before leaving、without saying、by practicing のように、前置詞 + -ing 全体で時間・方法・付帯状況を加えられます。主節と動名詞の意味上の主語が同じかも確認しましょう。\n\n特に注意したいのが to です。want to do の to は不定詞の印なので原形ですが、look forward to や be used to の to は前置詞なので -ing が続きます。to を見ただけで原形と決めず、直前の表現まで含めて役割を判定してください。',
    examples: [
      { en: 'You can improve your pronunciation by reading aloud.', ja: '音読することで発音を改善できます。', highlight: 'by reading aloud' },
      { en: 'He left without saying goodbye.', ja: '彼は別れのあいさつをせずに立ち去りました。', highlight: 'without saying' },
      { en: 'I am looking forward to meeting your family.', ja: 'あなたのご家族に会うのを楽しみにしています。', highlight: 'to meeting', note: 'この to は前置詞なので動名詞が続きます。' },
    ],
  },
} satisfies LessonExpansionMap
