import type { ThreeMinuteMood } from './types'

// 各話の冒頭に置く「ヒヨコ君の見当違い」と「イングバード先生のツッコミ」。
// 参照元の3分間ネタのように、生徒が言葉を字面で受け取ったり、規則を大げさに一般化したりする。
// 先生のセリフには必ず正しいルールを1つ入れ、笑いだけで終わらせない。

export type ComedyBeat = {
  /** 生徒の見当違い。 */
  student: string
  /** 先生のツッコミと正しい説明。 */
  teacher: string
  studentMood?: ThreeMinuteMood
  teacherMood?: ThreeMinuteMood
}

export const COMEDY_BEATS: Record<string, ComedyBeat> = {
  // U01 文の基本
  'u01-l1': {
    student: 'be動詞って、『ビーッ』って鳴く動詞? 蜂が飛んでる音?',
    teacher: '蜂じゃない! am / is / are のこと。『〜です』『〜にいます』と主語をつなぐ動詞だよ。',
  },
  'u01-l2': {
    student: '三単現って、三つの単語が現れる魔法? 三単現、三単現、三単現!',
    teacher: '三回言うな! 三人称・単数・現在の略。he / she / it のとき、動詞に -s を付けるルールだ!',
  },
  'u01-l3': {
    student: '否定文は文の頭に No を付ければいいんでしょ? 『No I like natto』!',
    teacher: 'No は答えだ! 文を否定するのは not / do not。疑問文は do を主語の前に出す!',
  },

  // U02 時制の基礎
  'u02-l1': {
    student: '今やってることは全部 -ing でしょ? じゃあ『I am knowing the answer』!',
    teacher: 'know に -ing を付けるな! 状態動詞は進行形にしない。今している動作だけが進行形だ!',
  },
  'u02-l2': {
    student: '今日だけのことなら、全部進行形でいいんだよね? 『I am living in Tokyo today』!',
    teacher: '今日だけ住むのか!? 一時的な動作と、ずっと続く状態を分けるんだ!',
  },
  'u02-l3': {
    student: '過去のことは全部 had を付ければ過去になるんでしょ? 『I had ate sushi』!',
    teacher: 'had は過去完了! まずは -ed か不規則形。had を付けるのは『もっと前』の話だ!',
  },
  'u02-l4': {
    student: '過去進行形は was + -ed でしょ? 『I was watched TV』!',
    teacher: 'was watched は受動態! 進行形は was + -ing。『I was watching TV』だ!',
  },
  'u02-l5': {
    student: '未来は全部 will! 来月の旅行も『I will go』でしょ?',
    teacher: '通じるけど、前から決めた予定なら be going to や進行形のほうが自然。will はその場の決定や予測だ!',
  },
  'u02-l6': {
    student: 'be going to って、『行く』の going? じゃあ『I am going to the park』は未来?',
    teacher: 'それは文字どおり公園へ行く途中! be going to + 動詞の原形で『〜するつもり』だ!',
  },

  // U03 名詞と冠詞
  'u03-l1': {
    student: '水だってコップに入れれば数えられるよね? 1 water, 2 waters!',
    teacher: 'water は water! コップの数を数えるなら two glasses of water だ!',
  },
  'u03-l2': {
    student: '母音字で始まれば全部 an でしょ? 『an university』!',
    teacher: 'university は『ユ』という子音の音で始まる! つづりじゃなく音で決める。a university だ!',
  },
  'u03-l3': {
    student: 'the は『あの』って指させばいいんでしょ? ぜんぶ the!',
    teacher: 'ぜんぶ the にしたら、聞き手は『どれ?』だらけになる! お互いに特定できるときだけ the だ!',
  },
  'u03-l4': {
    student: 'any は疑問文と否定文だけでしょ? 肯定文で使ったら爆発する?',
    teacher: '爆発はしない! any は『どれでも』の意味で肯定文にも使える。some はすすめるときの疑問文にも使うんだ!',
  },

  // U04 代名詞と限定詞
  'u04-l1': {
    student: '『私は』も『私を』も、ぜんぶ I でいいよね? ぼく、I しか覚えてない!',
    teacher: '目的格は me! I / my / me / mine と、席によって形が変わるんだ!',
  },
  'u04-l2': {
    student: '日本語の『それ』は this でしょ? 手元にある感じ?',
    teacher: '日本語の『それ』は距離が3段階。英語は2段階で、離れていれば that だ!',
  },
  'u04-l3': {
    student: 'one は数字の1でしょ? 『I bought a new one』は1個買ったってこと?',
    teacher: 'one は名詞の繰り返しを避ける言葉! 数字の1とは別物。it は特定のそのものだ!',
  },

  // U05 形容詞と副詞
  'u05-l1': {
    student: '形容詞は名詞の後ろに置くんでしょ? 『a cat small』!',
    teacher: '英語は『a small cat』! 基本は名詞の前。something cold のような例外もある!',
  },
  'u05-l2': {
    student: '形容詞に -ly を付ければ全部副詞! 『friendly』も副詞!',
    teacher: 'friendly は形容詞のまま! fast / hard / late も形が同じ。-ly だけで決めるな!',
  },
  'u05-l3': {
    student: 'always は文の最後に置くんだよね? 『I drink coffee always』!',
    teacher: 'それだと不自然! 頻度の副詞は一般動詞の前、be動詞の後ろ。『I always drink coffee』だ!',
  },

  // U06 疑問文
  'u06-l1': {
    student: 'Wh語は文の最後に付ければいいんでしょ? 『You live where?』',
    teacher: 'それじゃあ日本語の直訳! Wh語は文の先頭。あとは疑問文の語順にする!',
  },
  'u06-l2': {
    student: 'How は『どう?』だけ? 『How is the movie?』しか使えない?',
    teacher: 'How のあとに long / often / far / much を足せば、長さ・頻度・距離・量を聞ける!',
  },
  'u06-l3': {
    student: '『誰が電話したの?』は『Who did call you?』でしょ?',
    teacher: '主語を尋ねるときは did を付けない! 『Who called you?』だ!',
  },

  // U07 比較
  'u07-l1': {
    student: '比較級は全部 more を付ければOK! 『more tall』!',
    teacher: 'more tall とは言わない! 短い語は -er。tall → taller だ!',
  },
  'u07-l2': {
    student: '一番なら the を付けなくてもいいよね? 『He is tallest』!',
    teacher: '最上級には the を付ける! 『He is the tallest』。範囲の in / of も忘れるな!',
  },
  'u07-l3': {
    student: 'as tall as は『〜より高い』でしょ? as が2つで最上級?',
    teacher: '同じくらいだ! as ... as で『〜と同じくらい』。not as ... as なら『〜ほどない』!',
  },
  'u07-l4': {
    student: 'too は『とても』でしょ? 『too good』!',
    teacher: 'too は『〜すぎる』! 『too good』は『良すぎる』。very good とは違う!',
  },

  // U08 前置詞
  'u08-l1': {
    student: 'at は場所だけ? 時間には全部 in でいい?',
    teacher: 'at 7:00, on Monday, in April! 点・日・期間で使い分ける!',
  },
  'u08-l2': {
    student: 'on the box も in the box も同じでしょ? 箱の上も中も一緒!',
    teacher: 'on は接している面、in は中! 『on the box』と『in the box』は大違い!',
  },
  'u08-l3': {
    student: 'through も across も『通る』でしょ? 全部 through!',
    teacher: 'through は中を通り抜ける、across は表面を横切る! トンネルは through、橋は across!',
  },
  'u08-l4': {
    student: 'listen は目的語を直接取れるよね? 『listen music』!',
    teacher: 'listen to music! 前置詞までセットで覚える。look at / wait for も同じだ!',
  },

  // U09 助動詞
  'u09-l1': {
    student: 'can のあとは三単現で cans でしょ? 『She cans swim』!',
    teacher: 'cans とは言わない! 助動詞は形が変わらない。あとの動詞も原形だ!',
  },
  'u09-l2': {
    student: "mustn't と don't have to は同じ『しなくていい』でしょ?",
    teacher: "逆だ! mustn't は『してはいけない』、don't have to は『しなくてよい』。正反対!",
  },
  'u09-l3': {
    student: 'had better は過去形だから、過去の話?',
    teacher: 'had は過去の意味じゃない! 『〜したほうがいい』という警告。should より強い!',
  },
  'u09-l4': {
    student: 'might は may より必ず確率が低いんでしょ? 30%と50%?',
    teacher: '固定の確率はない! 文脈で決まる。数字で測るな!',
  },

  // U10 不定詞と動名詞
  'u10-l1': {
    student: 'to のあとは -ing でしょ? 『I want to going』!',
    teacher: 'to のあとは原形! 『I want to go』だ!',
  },
  'u10-l2': {
    student: '動名詞って、動く名詞? 走る名詞?',
    teacher: '動詞の -ing を名詞のように使うんだ! 『Swimming is fun』の swimming だ!',
  },
  'u10-l3': {
    student: 'like は to だけ? 『I like to swimming』?',
    teacher: 'like は to も -ing もOK! でも動詞ごとに相性がある。enjoy は -ing だけだ!',
  },
  'u10-l4': {
    student: 'look forward to のあとは原形でしょ? 『I look forward to see you』!',
    teacher: 'この to は前置詞! だから seeing。to を見ただけで原形と決めるな!',
  },

  // U11 現在完了
  'u11-l1': {
    student: '現在完了って、過去のことをぜんぶ完了させる魔法?',
    teacher: '魔法じゃない! 過去の出来事を『今』とつなげる形。have + 過去分詞だ!',
  },
  'u11-l2': {
    student: '経験なら『I have visited Kyoto last year』でしょ?',
    teacher: 'last year があるなら過去形! 現在完了は『いつ』を言わないんだ!',
  },
  'u11-l3': {
    student: 'for も since も『〜から』でしょ? どっちでも同じ!',
    teacher: 'for は期間の長さ、since は始まった時点! 『for three years』『since 2020』だ!',
  },
  'u11-l4': {
    student: 'already は疑問文でしょ? 『Have you already eaten?』',
    teacher: 'already は肯定文が基本! 疑問文で『もう?』と驚くときにも使えるけど、まずは肯定文だ!',
  },
  'u11-l5': {
    student: 'yesterday と現在完了は相性バツグンでしょ? 『I have lost it yesterday』!',
    teacher: '特定の過去の時点とは一緒に使えない! yesterday なら過去形だ!',
  },
  'u11-l6': {
    student: '現在完了は全部『完了』って意味なんでしょ?',
    teacher: '経験・継続・完了・結果の4つの顔がある! 『今とつながる』が共通点だ!',
  },

  // U12 未来表現
  'u12-l1': {
    student: '進行形は『今』だけ? 未来の予定には使えないよね?',
    teacher: '手配済みの予定なら使える! 『I am meeting Ken tomorrow』は約束済みだ!',
  },
  'u12-l2': {
    student: 'will も be going to も進行形も、全部同じ未来でしょ?',
    teacher: '決めたタイミングと手配の有無で違う! その場なら will、前からなら be going to、手配済みなら進行形!',
  },
  'u12-l3': {
    student: '未来の話なら、if の中も will でしょ? 『If it will rain』!',
    teacher: 'if の中は現在形! 『If it rains』。will は主節だけだ!',
  },

  // U13 受動態
  'u13-l1': {
    student: '受動態は be + -ed でしょ? 『The room is cleaned』は cleaned が -ed だからOK?',
    teacher: '過去分詞は -ed だけじゃない! written / built / made もある。形を覚えるんだ!',
  },
  'u13-l2': {
    student: '受動態なら by を必ず付けるんでしょ? 『The room was cleaned by someone』!',
    teacher: '誰がしたかが重要でなければ省略する! by someone は特に省く!',
  },
  'u13-l3': {
    student: 'will be cleaned も has been cleaned も、全部 be + 過去分詞でしょ?',
    teacher: 'その通り! 変わるのは be の部分だけ。will be / has been と着せ替える!',
  },
  'u13-l4': {
    student: '受動態のほうが丁寧でしょ? ぜんぶ受動態にしよう!',
    teacher: '丁寧とは限らない! 話題の中心を前に出すときに選ぶんだ!',
  },

  // U14 関係詞
  'u14-l1': {
    student: 'who は人だけ? which は物だけ? that は使っちゃダメ?',
    teacher: 'that は人にも物にも使える! でもカンマ付きの非制限用法では使えない!',
  },
  'u14-l2': {
    student: '関係代名詞はいつでも省略できるんでしょ?',
    teacher: '省略できるのは目的格だけ! 主格の who / which は省略できない!',
  },
  'u14-l3': {
    student: '場所の名詞なら、ぜんぶ where でしょ? 『the restaurant where serves sushi』!',
    teacher: 'where のあとは完全な文! 『where we had lunch』。穴があるなら which / that だ!',
  },
  'u14-l4': {
    student: 'カンマは息継ぎの目印でしょ? 意味は変わらないよね?',
    teacher: '意味が変わる! カンマなしは絞り込み、カンマありは補足。兄の人数の話まで変わる!',
  },
  'u14-l5': {
    student: '先行詞が人なら who で確定! もう迷わない!',
    teacher: '待て待て! 続く文に穴があるか、カンマがあるかも見るんだ!',
  },

  // U15 条件文
  'u15-l1': {
    student: 'if の中も未来なら will でしょ? 『If it will rain, we will cancel』!',
    teacher: 'if の中は現在形! 『If it rains』。will は主節だけだ!',
  },
  'u15-l2': {
    student: '過去形だから、過去の話でしょ? 『If I had time yesterday』?',
    teacher: '過去形でも過去の話じゃない! 『今、時間がない』という現実と違う想像だ!',
  },
  'u15-l3': {
    student: 'unless は if と同じでしょ? in case も同じ!',
    teacher: 'unless は if not、in case は『備えて』! 意味が違う!',
  },
  'u15-l4': {
    student: '現実的かどうかは、過去形かどうかで決まるんでしょ?',
    teacher: '形は結果! まず話し手が『本当に起こりうる』と思っているかを見るんだ!',
  },

  // U16 接続詞
  'u16-l1': {
    student: 'because と so は一緒に使えるんでしょ? 『Because it rained, so we stayed in』!',
    teacher: 'それは重複! because か so のどちらか一方にする!',
  },
  'u16-l2': {
    student: '未来の話なら、when の中も will でしょ?',
    teacher: 'when の中は現在形! 『When he arrives』。未来は主節の will が担当する!',
  },
  'u16-l3': {
    student: "neither は否定文で使うんでしょ? 『I don't like neither』!",
    teacher: 'neither 自体が否定! 『I like neither』でいい。not と重ねるな!',
  },

  // U17 現在完了進行形
  'u17-l1': {
    student: 'have been + -ing って受動態?',
    teacher: '受動態は be + 過去分詞! have been + -ing は『今も続いている動作』だ!',
  },
  'u17-l2': {
    student: 'have painted も have been painting も同じでしょ? どっちでもいい!',
    teacher: '結果か作業かが違う! 塗り終えたなら have painted、塗っている途中なら have been painting!',
  },

  // U18 過去完了
  'u18-l1': {
    student: '過去完了は過去のことをぜんぶ表すんでしょ? 過去形の上位版!',
    teacher: '上位版じゃない! 『過去のある時点より前』を表す。基準の過去が必要だ!',
  },
  'u18-l2': {
    student: '順番どおりに話すときも、ぜんぶ過去完了にすれば丁寧?',
    teacher: '丁寧じゃない! 順番どおりなら過去形で十分。過去完了は『さかのぼる』ときだけだ!',
  },
  'u18-l3': {
    student: '物語は全部過去形でしょ? 背景も過去形!',
    teacher: '背景は過去進行形、その前は過去完了! 役割分担がある!',
  },

  // U19 伝達
  'u19-l1': {
    student: 'said のあとは、言った言葉をそのまま入れればいいんでしょ?',
    teacher: 'そのままなら引用! 自分の言葉に直すなら、時制・代名詞・時の表現をずらす!',
  },
  'u19-l2': {
    student: '間接疑問も疑問文の語順でしょ? 『He asked me where did I live』!',
    teacher: '間接疑問は普通の文の語順! 『where I lived』。did は消す!',
  },
  'u19-l3': {
    student: 'suggest は『人に〜を提案する』だから『suggest me to go』でしょ?',
    teacher: 'suggest は人を目的語に取れない! 『suggest going』か『suggest that I go』だ!',
  },
  'u19-l4': {
    student: '『Do you know where is the station?』でしょ? 疑問文だから is が前!',
    teacher: '文の中に入れたら普通の語順! 『where the station is』だ!',
  },

  // U20 助動詞の発展
  'u20-l1': {
    student: 'must は義務だけ? 『You must be tired』は『疲れなければならない』?',
    teacher: 'それだと命令みたい! 根拠から『〜に違いない』という推量にもなる!',
  },
  'u20-l2': {
    student: '過去の推量は『must was』でしょ?',
    teacher: 'must was とは言わない! 『must have + 過去分詞』だ!',
  },
  'u20-l3': {
    student: 'should have は『〜すべき』でしょ? 今もすべき?',
    teacher: '『すべきだったのに、しなかった』という後悔! 過去を振り返る形だ!',
  },
  'u20-l4': {
    student: 'used to は『使った』でしょ? 『I used to a pen』?',
    teacher: 'used to + 原形で『昔は〜した』! 物を使ったわけじゃない!',
  },

  // U21 動名詞・不定詞の発展
  'u21-l1': {
    student: 'stop to do も stop doing も『やめる』でしょ? 同じ!',
    teacher: 'stop doing は『するのをやめる』、stop to do は『〜するために立ち止まる』! 意味が変わる!',
  },
  'u21-l2': {
    student: '『I want that you come』でしょ? that を使えば丁寧!',
    teacher: 'want は that節を取れない! 『I want you to come』だ!',
  },
  'u21-l3': {
    student: 'It is important to study の It は『それ』でしょ? 何を指してるの?',
    teacher: '何も指してない! 長い主語の席を確保する仮主語だ!',
  },

  // U22 第3条件文と wish
  'u22-l1': {
    student: '『If I had known, I would call you』でしょ? 過去も would + 原形!',
    teacher: '過去の結果は would have + 過去分詞! 『would have called』だ!',
  },
  'u22-l2': {
    student: 'wish のあとは現在形でしょ? 『I wish I have more time』!',
    teacher: 'wish のあとは過去形! 『I wish I had more time』。今の現実と違う願望だ!',
  },
  'u22-l3': {
    student: '第1・第2・第3は、過去・現在・未来で決まるんでしょ?',
    teacher: '時間だけじゃない! 『現実的か、今の非現実か、過去の非現実か』で選ぶ!',
  },

  // U23 仮定法の発展
  'u23-l1': {
    student: 'if と結果の時制は、いつも同じでしょ?',
    teacher: '混合条件文はわざとずらす! 『過去の仮定 → 今の結果』もある!',
  },
  'u23-l2': {
    student: 'provided は if と完全に同じでしょ? 長いだけ!',
    teacher: '長いだけじゃない! 『この条件を満たすなら』と強く条件を課す。場面の硬さも違う!',
  },
  'u23-l3': {
    student: "would rather you のあとは原形でしょ? 『I'd rather you stay』!",
    teacher: "別の人にしてほしいときは過去形! 『I'd rather you stayed』だ!",
  },

  // U24 使役と知覚
  'u24-l1': {
    student: '『I had my hair cut』は自分で切ったんでしょ? ハサミを持って!',
    teacher: 'それは『切ってもらった』! 自分で切ったなら I cut my hair だ!',
  },
  'u24-l2': {
    student: 'make のあとも to を付けるんでしょ? 『make me to wait』!',
    teacher: 'make / let / have は原形! to を付けるのは get だけだ!',
  },
  'u24-l3': {
    student: '『I saw him to cross the street』でしょ? to を付ければ丁寧!',
    teacher: '知覚動詞のあとに to は付けない! 原形か -ing だ!',
  },

  // U25 分詞
  'u25-l1': {
    student: '退屈なら『I am boring』でしょ? ぼく、退屈な人?',
    teacher: 'それだと『人を退屈させる人』! 自分が退屈しているなら I am bored だ!',
  },
  'u25-l2': {
    student: '分詞は名詞の前に置くんでしょ? 『the standing man』!',
    teacher: 'それも言えるけど、説明が長いなら後ろ! 『the man standing there』だ!',
  },
  'u25-l3': {
    student: '分詞構文は主語が違ってもOKでしょ? 『Walking home, the bridge...』',
    teacher: '主語が違うと変な意味になる! 分詞の主語と主節の主語をそろえる!',
  },

  // U26 受動態の発展
  'u26-l1': {
    student: '『It is said that』の It は『それ』? 誰のこと?',
    teacher: '何も指してない! 『〜と言われている』の仮の主語だ!',
  },
  'u26-l2': {
    student: '『I want to be invited』は『招待したい』でしょ?',
    teacher: 'それだと自分が招待する側! to be invited は『招待されたい』だ!',
  },
  'u26-l3': {
    student: 'get は『手に入れる』だから、get stolen は『盗まれたものを手に入れる』?',
    teacher: '逆! get + 過去分詞で『盗まれる』という出来事。get は受動も作る!',
  },

  // U27 関係詞の発展
  'u27-l1': {
    student: 'in which は会話でもバリバリ使うんでしょ?',
    teacher: '会話では前置詞を後ろに残すのが自然! in which はフォーマルな書き言葉だ!',
  },
  'u27-l2': {
    student: '『the thing what he said』でしょ? thing と what でダブル!',
    teacher: 'what は先行詞を含む! 『what he said』だけでいい。the thing と並べるな!',
  },
  'u27-l3': {
    student: '文全体を受けるのは that でしょ? 『, that surprised me』!',
    teacher: 'カンマのあとで文全体を受けるのは which だけ! that は使えない!',
  },

  // U28 談話標識
  'u28-l1': {
    student: 'however は接続詞だから、コンマでつなげばOK?',
    teacher: 'however は副詞! コンマだけで2文をつなげない。ピリオドかセミコロンで区切る!',
  },
  'u28-l2': {
    student: 'therefore も接続詞でしょ? so と同じ!',
    teacher: 'therefore は副詞! so のように節をつなぐ接続詞ではない!',
  },
  'u28-l3': {
    student: 'at first は first と同じでしょ? 手順の最初!',
    teacher: 'at first は『最初は〜だった』! 手順の1番目は first / first of all だ!',
  },

  // U29 名詞節
  'u29-l1': {
    student: 'that はいつでも省略できるんでしょ?',
    teacher: '目的語の that は省略しやすいけど、主語の that節では残す! 全部同じじゃない!',
  },
  'u29-l2': {
    student: 'whether と if は完全に同じでしょ? どっちでもいい!',
    teacher: 'whether しか使えない場所がある! 主語・前置詞のあと・to不定詞の前だ!',
  },
  'u29-l3': {
    student: 'It seems that の It は、何かを指してるんでしょ?',
    teacher: '仮主語! 『〜のようだ』の内容を後ろに置くための席だ!',
  },

  // U30 強調・倒置・省略
  'u30-l1': {
    student: 'It was Ken that broke it は関係代名詞でしょ? Ken を説明してる!',
    teacher: '強調構文! It was と that で Ken を挟んでスポットライトを当てる。取り除いても文が成り立つ!',
  },
  'u30-l2': {
    student: 'Never I have seen でしょ? 否定語を前に出しただけ!',
    teacher: 'それだと語順が崩壊! 『Never have I seen』。否定語のあとは疑問文の語順だ!',
  },
  'u30-l3': {
    student: '『I think so』の so は『そう』でしょ? 日本語と同じ!',
    teacher: '意味は近いけど、so は前の内容全体を受ける! 『I hope not』の not も同じだ!',
  },

  // U31 時制と紛らわしいペア
  'u31-l1': {
    student: 'for があれば現在完了でしょ? 『I worked there for five years』は間違い?',
    teacher: '間違いじゃない! for は過去形にも現在完了にも使える。今も続くかで決める!',
  },
  'u31-l2': {
    student: 'by も until も『まで』でしょ? 同じ!',
    teacher: 'by は期限、until は継続の終点! 『by five』は5時までに、『until five』は5時までずっと!',
  },
  'u31-l3': {
    student: 'so も such も『とても』でしょ? どっちでもいい!',
    teacher: 'so のあとは形容詞・副詞、such のあとは名詞のかたまり! 形で選ぶ!',
  },

  // U32 時制と条件の総仕上げ
  'u32-l1': {
    student: '未来の話は全部 will でしょ? will be doing も will have done も同じ!',
    teacher: '途中なら will be doing、完了なら will have done! 未来の一点からの見え方が違う!',
  },
  'u32-l2': {
    student: 'was going to は『行くつもりだった』でしょ? 必ず実現した?',
    teacher: '実現しなかった含みも多い! 『するつもりだったけど…』と続くことが多い!',
  },
  'u32-l3': {
    student: 'Had I known は疑問文でしょ? 質問してるの?',
    teacher: 'if を省いた条件文! 『If I had known』と同じ意味。疑問文じゃない!',
  },
  'u32-l4': {
    student: '『The more you practice, the better』の the は1つでいいんでしょ?',
    teacher: '両方に the が必要! 『The more..., the better...』でワンセットだ!',
  },

  // U33 冠詞・数量詞・句動詞
  'u33-l1': {
    student: 'a と the は日本語にないから、適当でいいよね?',
    teacher: '適当だと伝わらない! 初めて出すなら a、お互いに分かるなら the だ!',
  },
  'u33-l2': {
    student: 'few も a few も『少し』でしょ? 同じ!',
    teacher: 'few は『ほとんどない』、a few は『少しある』! a の有無で評価が反転する!',
  },
  'u33-l3': {
    student: '『turn off it』でしょ? 代名詞は後ろ!',
    teacher: '代名詞は間! 『turn it off』。分離できる句動詞のルールだ!',
  },
}
