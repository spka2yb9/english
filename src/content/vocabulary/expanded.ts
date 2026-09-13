// このファイルは scripts/generate-vocabulary-expansion.mjs で生成する。
// Oxford A2–B2 差分、CC0英和語義、CMUdict発音、独自例文／Tatoeba対訳を正規化した拡張データ。
import type { VocabularyEntry } from '../types'

type ExpandedRow = [
  word: string,
  level: 'A2' | 'B1' | 'B2',
  partOfSpeech: string,
  meaningsJa: string[],
  pronunciation: string,
  exampleSentence: string,
  exampleTranslationJa: string,
  source: VocabularyEntry['exampleSource'] | null,
]

const rows: ExpandedRow[] = [
  [
    "ability",
    "A2",
    "名詞",
    [
      "能力"
    ],
    "/əˈbɪləti/",
    "Her ability to explain difficult ideas clearly impressed the class.",
    "難しい考えを明確に説明する彼女の能力は、クラスを感心させた。",
    null
  ],
  [
    "able",
    "A2",
    "形容詞",
    [
      "できる"
    ],
    "/ˈeɪbəl/",
    "After a few lessons, I was able to follow the conversation.",
    "数回のレッスンの後、私は会話についていけるようになった。",
    null
  ],
  [
    "abroad",
    "A2",
    "副詞",
    [
      "海外へ"
    ],
    "/əˈbrɔd/",
    "Many students choose to study abroad for a semester.",
    "多くの学生が一学期間、海外で学ぶことを選ぶ。",
    null
  ],
  [
    "absolute",
    "B2",
    "形容詞",
    [
      "絶対的な力を持った",
      "絶対の"
    ],
    "/ˈæbsəlut/",
    "There is no absolute guarantee that the plan will succeed.",
    "その計画が成功するという絶対的な保証はない。",
    null
  ],
  [
    "absolutely",
    "B1",
    "副詞",
    [
      "まったく",
      "絶対に"
    ],
    "/æbsəˈlutli/",
    "You are absolutely right about the need for more practice.",
    "もっと練習が必要だという点で、あなたはまったく正しい。",
    null
  ],
  [
    "accent",
    "B2",
    "名詞",
    [
      "アクセント",
      "アクセント記号"
    ],
    "/əkˈsɛnt/",
    "Her American accent became clearer after months of listening practice.",
    "数か月のリスニング練習で、彼女のアメリカ英語のアクセントはより明瞭になった。",
    null
  ],
  [
    "accept",
    "A2",
    "動詞",
    [
      "を受け取る",
      "を受け入れる"
    ],
    "/ækˈsɛpt/",
    "Please accept our invitation to the opening ceremony.",
    "開会式への私たちの招待を受けてください。",
    null
  ],
  [
    "accident",
    "A2",
    "名詞",
    [
      "事故"
    ],
    "/ˈæksədənt/",
    "No one was seriously injured in the accident.",
    "その事故で重傷を負った人はいなかった。",
    null
  ],
  [
    "accidentally",
    "B2",
    "副詞",
    [
      "誤って",
      "偶然に"
    ],
    "/æksəˈdɛntəli/",
    "I accidentally sent the message to the wrong person.",
    "私は誤ってそのメッセージを別の人に送ってしまった。",
    null
  ],
  [
    "accommodate",
    "B2",
    "動詞",
    [
      "収容する"
    ],
    "/əˈkɑmədeɪt/",
    "The new hall can accommodate up to five hundred guests.",
    "新しいホールは最大500人の客を収容できる。",
    null
  ],
  [
    "accomplish",
    "B2",
    "動詞",
    [
      "達成する",
      "成し遂げる"
    ],
    "/əˈkɑmplɪʃ/",
    "We need a realistic schedule to accomplish this goal.",
    "この目標を達成するには現実的な予定が必要だ。",
    null
  ],
  [
    "according to",
    "A2",
    "前置詞",
    [
      "〜によれば"
    ],
    "/əˈkɔrdɪŋ tu/",
    "According to the forecast, the rain will stop by noon.",
    "予報によると、雨は正午までにやむそうだ。",
    null
  ],
  [
    "accountant",
    "B2",
    "名詞",
    [
      "会計士",
      "会計係"
    ],
    "/əˈkaʊntənt/",
    "The accountant checked every figure in the annual report.",
    "会計士は年次報告書のすべての数字を確認した。",
    null
  ],
  [
    "accuracy",
    "B2",
    "名詞",
    [
      "正確さ"
    ],
    "/ˈækjɚəsi/",
    "Always check the accuracy of information before sharing it.",
    "情報を共有する前に、必ずその正確さを確認しなさい。",
    null
  ],
  [
    "accurately",
    "B2",
    "副詞",
    [
      "正確に"
    ],
    "/ˈækjɚətli/",
    "The map accurately shows the distance between the two towns.",
    "その地図は2つの町の距離を正確に示している。",
    null
  ],
  [
    "acid",
    "B2",
    "名詞",
    [
      "酸"
    ],
    "/ˈæsəd/",
    "This cleaning product contains a mild acid.",
    "この洗浄製品には弱い酸が含まれている。",
    null
  ],
  [
    "act",
    "A2",
    "名詞・動詞",
    [
      "行動する"
    ],
    "/ækt/",
    "We must act quickly before the situation gets worse.",
    "状況が悪化する前に、私たちはすぐ行動しなければならない。",
    null
  ],
  [
    "activate",
    "B2",
    "動詞",
    [
      "作動させる",
      "有効にする"
    ],
    "/ˈæktəveɪt/",
    "Press this button to activate the security system.",
    "このボタンを押して防犯システムを作動させてください。",
    null
  ],
  [
    "active",
    "A2",
    "形容詞",
    [
      "活動的な",
      "積極的な"
    ],
    "/ˈæktɪv/",
    "Regular exercise helps older people remain active.",
    "定期的な運動は高齢者が活動的でい続ける助けになる。",
    null
  ],
  [
    "actual",
    "B2",
    "形容詞",
    [
      "実際上の"
    ],
    "/ˈæktʃəwəl/",
    "The actual cost was much higher than our estimate.",
    "実際の費用は私たちの見積もりよりずっと高かった。",
    null
  ],
  [
    "actually",
    "A2",
    "副詞",
    [
      "実際に"
    ],
    "/ˈæktʃuəli/",
    "I thought the task was difficult, but it was actually quite simple.",
    "その課題は難しいと思ったが、実際にはかなり簡単だった。",
    null
  ],
  [
    "ad",
    "B1",
    "名詞",
    [
      "広告"
    ],
    "/æd/",
    "The company placed an ad in the local newspaper.",
    "その会社は地元の新聞に広告を載せた。",
    null
  ],
  [
    "addiction",
    "B2",
    "名詞",
    [
      "依存",
      "中毒"
    ],
    "/əˈdɪkʃən/",
    "Phone addiction can affect both sleep and concentration.",
    "スマートフォン依存は睡眠と集中力の両方に影響しうる。",
    null
  ],
  [
    "addition",
    "B1",
    "名詞",
    [
      "付け加えること",
      "足した物"
    ],
    "/əˈdɪʃən/",
    "The addition of more windows made the room brighter.",
    "窓を増設したことで、その部屋は明るくなった。",
    null
  ],
  [
    "additionally",
    "B2",
    "副詞",
    [
      "さらに",
      "その上"
    ],
    "/əˈdɪʃənʌli/",
    "The hotel is close to the station; additionally, breakfast is included.",
    "そのホテルは駅に近く、さらに朝食も含まれている。",
    null
  ],
  [
    "address",
    "B2",
    "動詞",
    [
      "演説",
      "に演説する"
    ],
    "/ˈædrɛs/",
    "The mayor will address the public this evening.",
    "市長は今晩、市民に向けて演説する。",
    null
  ],
  [
    "adequately",
    "B2",
    "副詞",
    [
      "十分に"
    ],
    "/ˈædəkwətli/",
    "The report does not adequately explain the cause of the problem.",
    "その報告書は問題の原因を十分に説明していない。",
    null
  ],
  [
    "administration",
    "B2",
    "名詞",
    [
      "政権",
      "行政"
    ],
    "/ædmɪnɪˈstreɪʃən/",
    "The new administration promised to improve public transport.",
    "新政権は公共交通を改善すると約束した。",
    null
  ],
  [
    "adult",
    "A2",
    "形容詞",
    [
      "大人",
      "成人の"
    ],
    "/əˈdʌlt/",
    "Every child must be accompanied by an adult.",
    "子どもには必ず大人が付き添わなければならない。",
    null
  ],
  [
    "adventure",
    "A2",
    "名詞",
    [
      "冒険"
    ],
    "/ædˈvɛntʃɚ/",
    "Travelling alone across the country was a great adventure.",
    "一人で国を横断した旅は大きな冒険だった。",
    null
  ],
  [
    "advertisement",
    "A2",
    "名詞",
    [
      "広告"
    ],
    "/ædˈvɝtəzmənt/",
    "The advertisement made the product look better than it was.",
    "その広告は製品を実物以上によく見せていた。",
    null
  ],
  [
    "advertising",
    "A2",
    "名詞",
    [
      "広告",
      "広告業"
    ],
    "/ˈædvɚtaɪzɪŋ/",
    "The company spends a large amount of money on online advertising.",
    "その会社はオンライン広告に多額のお金を使っている。",
    null
  ],
  [
    "advise",
    "B1",
    "動詞",
    [
      "助言する",
      "勧める"
    ],
    "/ædˈvaɪz/",
    "Doctors advise patients to get enough sleep.",
    "医師は患者に十分な睡眠を取るよう勧めている。",
    null
  ],
  [
    "affordable",
    "B2",
    "形容詞",
    [
      "手頃な価格の"
    ],
    "/əˈfɔrdəbəl/",
    "The city needs more affordable housing for young families.",
    "その市には若い家庭向けの、より手頃な住宅が必要だ。",
    null
  ],
  [
    "after",
    "A2",
    "副詞・接続詞",
    [
      "した後で"
    ],
    "/ˈæftɚ/",
    "We went for coffee after the meeting ended.",
    "会議が終わった後、私たちはコーヒーを飲みに行った。",
    null
  ],
  [
    "afterwards",
    "B2",
    "副詞",
    [
      "その後"
    ],
    "/ˈæftɚwɚdz/",
    "We finished the project and celebrated together afterwards.",
    "私たちはプロジェクトを終え、その後みんなで祝った。",
    null
  ],
  [
    "against",
    "A2",
    "前置詞",
    [
      "〜に反対して",
      "〜に対して"
    ],
    "/əˈgɛnst/",
    "Most residents voted against the proposed development.",
    "住民の大半は提案された開発に反対票を投じた。",
    null
  ],
  [
    "age",
    "B1",
    "動詞",
    [
      "古くなる"
    ],
    "/eɪdʒ/",
    "Some types of cheese improve as they age.",
    "チーズの中には熟成するほど風味がよくなるものがある。",
    null
  ],
  [
    "aged",
    "B1",
    "形容詞",
    [
      "〜歳の",
      "高齢の"
    ],
    "/eɪdʒd/",
    "The program provides meals for people aged sixty-five and over.",
    "その制度は65歳以上の人に食事を提供する。",
    null
  ],
  [
    "agent",
    "B1",
    "名詞",
    [
      "代理人"
    ],
    "/ˈeɪdʒənt/",
    "You should speak to a travel agent before booking the tour.",
    "ツアーを予約する前に旅行代理店の担当者に相談した方がよい。",
    null
  ],
  [
    "agreement",
    "B1",
    "名詞",
    [
      "合意",
      "一致"
    ],
    "/əˈgrimənt/",
    "After several hours of discussion, both sides reached an agreement.",
    "数時間の話し合いの末、双方は合意に達した。",
    null
  ],
  [
    "agriculture",
    "B2",
    "名詞",
    [
      "農業"
    ],
    "/ˈægrɪkʌltʃɚ/",
    "Modern agriculture depends on careful management of water.",
    "現代の農業は水の慎重な管理に依存している。",
    null
  ],
  [
    "ah",
    "A2",
    "間投詞",
    [
      "ああ"
    ],
    "/ɑ/",
    "Ah, now I understand what you meant.",
    "ああ、今あなたの言いたかったことが分かりました。",
    null
  ],
  [
    "aids",
    "B2",
    "名詞",
    [
      "エイズ"
    ],
    "/eɪdz/",
    "Better education has helped reduce the spread of AIDS.",
    "より良い教育がエイズの拡大を抑える助けになっている。",
    null
  ],
  [
    "aircraft",
    "B2",
    "名詞",
    [
      "航空機"
    ],
    "/ˈɛrkræft/",
    "The aircraft landed safely despite the strong wind.",
    "その航空機は強風にもかかわらず安全に着陸した。",
    null
  ],
  [
    "airline",
    "A2",
    "名詞",
    [
      "航空会社",
      "航空路線"
    ],
    "/ˈɛrlaɪn/",
    "The airline cancelled three flights because of the storm.",
    "その航空会社は嵐のため3便を欠航にした。",
    null
  ],
  [
    "album",
    "B1",
    "名詞",
    [
      "アルバム"
    ],
    "/ˈælbəm/",
    "The band will release its new album next month.",
    "そのバンドは来月、新しいアルバムを発売する。",
    null
  ],
  [
    "alcohol",
    "B1",
    "名詞",
    [
      "アルコール",
      "アルコール飲料"
    ],
    "/ˈælkəhɑl/",
    "This medicine should not be taken with alcohol.",
    "この薬はアルコールと一緒に服用してはいけない。",
    null
  ],
  [
    "alcoholic",
    "B1",
    "形容詞",
    [
      "アルコールの",
      "アルコール性の"
    ],
    "/ælkəˈhɑlɪk/",
    "The restaurant offers several non-alcoholic drinks.",
    "そのレストランはいくつかのノンアルコール飲料を提供している。",
    null
  ],
  [
    "alien",
    "B2",
    "名詞",
    [
      "外国人の",
      "在留外国人の"
    ],
    "/ˈeɪliən/",
    "The novel tells the story of an alien who visits Earth.",
    "その小説は地球を訪れる異星人の物語だ。",
    null
  ],
  [
    "alive",
    "A2",
    "形容詞",
    [
      "生きている",
      "生き生きした"
    ],
    "/əˈlaɪv/",
    "The missing climber was found alive the next morning.",
    "行方不明の登山者は翌朝、生きて発見された。",
    null
  ],
  [
    "all",
    "A2",
    "副詞",
    [
      "すべての",
      "全部"
    ],
    "/ɔl/",
    "All the information you need is on this page.",
    "必要な情報はすべてこのページにある。",
    null
  ],
  [
    "all right",
    "A2",
    "形容詞・副詞・間投詞",
    [
      "大丈夫な",
      "問題のない"
    ],
    "/ɔl raɪt/",
    "Do not worry; everything will be all right.",
    "心配しないで。すべて大丈夫になるよ。",
    null
  ],
  [
    "allow",
    "A2",
    "動詞",
    [
      "許す",
      "〜できるようにする"
    ],
    "/əˈlaʊ/",
    "The new rules allow employees to work from home twice a week.",
    "新しい規則では、従業員は週2回在宅勤務ができる。",
    null
  ],
  [
    "almost",
    "A2",
    "副詞",
    [
      "ほとんど"
    ],
    "/ˈɔlmoʊst/",
    "We have almost finished preparing for the event.",
    "私たちはイベントの準備をほぼ終えた。",
    null
  ],
  [
    "alone",
    "A2",
    "形容詞・副詞",
    [
      "ひとりで"
    ],
    "/əˈloʊn/",
    "She prefers to study alone in a quiet room.",
    "彼女は静かな部屋で一人で勉強する方を好む。",
    null
  ],
  [
    "along",
    "A2",
    "副詞・前置詞",
    [
      "〜に沿って"
    ],
    "/əˈlɔŋ/",
    "We walked along the river until sunset.",
    "私たちは日が沈むまで川沿いを歩いた。",
    null
  ],
  [
    "alongside",
    "B2",
    "前置詞",
    [
      "〜に沿って",
      "〜のそばに"
    ],
    "/əˈlɔŋˈsaɪd/",
    "A cycle path runs alongside the main road.",
    "主要道路に沿って自転車道が走っている。",
    null
  ],
  [
    "already",
    "A2",
    "副詞",
    [
      "すでに"
    ],
    "/ɔlˈrɛdi/",
    "By the time I arrived, the film had already started.",
    "私が着いた時には、映画はすでに始まっていた。",
    null
  ],
  [
    "alter",
    "B2",
    "動詞",
    [
      "を変える"
    ],
    "/ˈɔltɚ/",
    "A small change in temperature can alter the result.",
    "わずかな温度変化でも結果を変えることがある。",
    null
  ],
  [
    "although",
    "A2",
    "接続詞",
    [
      "ではあるが"
    ],
    "/ɔlˈðoʊ/",
    "Although the journey was long, the children did not complain.",
    "旅は長かったが、子どもたちは不満を言わなかった。",
    null
  ],
  [
    "altogether",
    "B2",
    "副詞",
    [
      "全部で"
    ],
    "/ɔltəˈgɛðɚ/",
    "There were altogether forty people at the workshop.",
    "その研修会には全部で40人いた。",
    null
  ],
  [
    "amazed",
    "B1",
    "形容詞",
    [
      "驚いた"
    ],
    "/əˈmeɪzd/",
    "We were amazed by the view from the top of the mountain.",
    "私たちは山頂からの景色に驚いた。",
    null
  ],
  [
    "ambulance",
    "B2",
    "名詞",
    [
      "救急車"
    ],
    "/ˈæmbjələns/",
    "An ambulance arrived within five minutes of the call.",
    "通報から5分以内に救急車が到着した。",
    null
  ],
  [
    "among",
    "A2",
    "前置詞",
    [
      "の間で",
      "の間に"
    ],
    "/əˈmʌŋ/",
    "This restaurant is popular among local office workers.",
    "このレストランは地元の会社員の間で人気がある。",
    null
  ],
  [
    "amount",
    "A2",
    "名詞・動詞",
    [
      "量"
    ],
    "/əˈmaʊnt/",
    "The amount of waste produced by the factory has fallen.",
    "その工場が出す廃棄物の量は減少した。",
    null
  ],
  [
    "amusing",
    "B2",
    "形容詞",
    [
      "おもしろい"
    ],
    "/əmˈjuzɪŋ/",
    "He told an amusing story about his first day at work.",
    "彼は仕事初日の面白い話をした。",
    null
  ],
  [
    "analyse",
    "B1",
    "動詞",
    [
      "分析する"
    ],
    "/ˈænəlaɪz/",
    "Researchers will analyse the data before publishing their results.",
    "研究者は結果を発表する前にデータを分析する。",
    null
  ],
  [
    "analyst",
    "B2",
    "名詞",
    [
      "アナリスト",
      "分析者"
    ],
    "/ˈænəlɪst/",
    "A financial analyst explained why the market had changed.",
    "金融アナリストが市場が変化した理由を説明した。",
    null
  ],
  [
    "ancestor",
    "B2",
    "名詞",
    [
      "祖先"
    ],
    "/ˈænsɛstɚ/",
    "One of her ancestors moved here more than a century ago.",
    "彼女の祖先の一人は1世紀以上前にここへ移り住んだ。",
    null
  ],
  [
    "anger",
    "B2",
    "名詞",
    [
      "怒り"
    ],
    "/ˈæŋgɚ/",
    "He found it difficult to control his anger during the argument.",
    "彼は口論中に怒りを抑えるのが難しかった。",
    null
  ],
  [
    "angle",
    "B2",
    "名詞",
    [
      "角度",
      "角"
    ],
    "/ˈæŋgəl/",
    "Try looking at the problem from a different angle.",
    "その問題を別の角度から見てみなさい。",
    null
  ],
  [
    "animation",
    "B2",
    "名詞",
    [
      "アニメーション",
      "動画"
    ],
    "/ænəˈmeɪʃən/",
    "The studio is known for its beautiful hand-drawn animation.",
    "その制作会社は美しい手描きアニメーションで知られている。",
    null
  ],
  [
    "ankle",
    "A2",
    "名詞",
    [
      "足首"
    ],
    "/ˈæŋkəl/",
    "She injured her ankle while running down the hill.",
    "彼女は丘を走り下りている時に足首を痛めた。",
    null
  ],
  [
    "announcement",
    "B1",
    "名詞",
    [
      "発表"
    ],
    "/əˈnaʊnsmənt/",
    "The unexpected announcement surprised everyone in the office.",
    "突然の発表に職場のみんなが驚いた。",
    null
  ],
  [
    "annoyed",
    "B1",
    "形容詞",
    [
      "いら立った"
    ],
    "/əˈnɔɪd/",
    "I was annoyed that the train was delayed again.",
    "電車がまた遅れたので私はいら立った。",
    null
  ],
  [
    "annoying",
    "B1",
    "形容詞",
    [
      "煩わしい",
      "迷惑な"
    ],
    "/əˈnɔɪɪŋ/",
    "The most annoying part was having to enter the same information twice.",
    "最も面倒だったのは同じ情報を2回入力しなければならないことだった。",
    null
  ],
  [
    "annually",
    "B2",
    "副詞",
    [
      "毎年",
      "年々"
    ],
    "/ˈænjuəli/",
    "The safety equipment is checked annually.",
    "安全設備は毎年点検される。",
    null
  ],
  [
    "anxiety",
    "B2",
    "名詞",
    [
      "不安",
      "切望すること"
    ],
    "/æŋˈzaɪəti/",
    "Preparing well can reduce anxiety before an interview.",
    "十分に準備すると面接前の不安を減らせる。",
    null
  ],
  [
    "any",
    "A2",
    "副詞",
    [
      "何か"
    ],
    "/ˈɛni/",
    "Is there any reason to delay the decision?",
    "決定を遅らせる理由は何かありますか。",
    null
  ],
  [
    "any more",
    "A2",
    "副詞",
    [
      "もう"
    ],
    "/ˈɛni mɔr/",
    "We do not use that old system any more.",
    "私たちはもうその古いシステムを使っていない。",
    null
  ],
  [
    "anybody",
    "A2",
    "名詞",
    [
      "誰か",
      "誰でも"
    ],
    "/ˈɛnibədi/",
    "Does anybody know how to open this file?",
    "このファイルの開き方を知っている人はいますか。",
    null
  ],
  [
    "anyway",
    "A2",
    "副詞",
    [
      "それでも"
    ],
    "/ˈɛniweɪ/",
    "The weather looked bad, but we went hiking anyway.",
    "天気は悪そうだったが、それでも私たちはハイキングに行った。",
    null
  ],
  [
    "anywhere",
    "A2",
    "副詞・名詞",
    [
      "どこでも"
    ],
    "/ˈɛniwɛr/",
    "You can sit anywhere in this section.",
    "この区域ならどこに座ってもよい。",
    null
  ],
  [
    "apart",
    "B1",
    "副詞",
    [
      "離れて"
    ],
    "/əˈpɑrt/",
    "The two villages are only five kilometres apart.",
    "その2つの村はわずか5キロしか離れていない。",
    null
  ],
  [
    "apology",
    "B2",
    "名詞",
    [
      "謝罪"
    ],
    "/əˈpɑlədʒi/",
    "The company issued an apology for the long delay.",
    "その会社は長い遅延について謝罪した。",
    null
  ],
  [
    "app",
    "A2",
    "名詞",
    [
      "アプリ",
      "アプリケーション"
    ],
    "/æp/",
    "This app helps users keep track of their daily spending.",
    "このアプリは利用者が毎日の支出を把握するのに役立つ。",
    null
  ],
  [
    "appear",
    "A2",
    "動詞",
    [
      "現れる",
      "表示される"
    ],
    "/əˈpɪr/",
    "A warning message will appear if you enter the wrong password.",
    "間違ったパスワードを入力すると警告メッセージが表示される。",
    null
  ],
  [
    "applicant",
    "B2",
    "名詞",
    [
      "応募者"
    ],
    "/ˈæplɪkənt/",
    "Each applicant must provide two references.",
    "応募者はそれぞれ2人の推薦者を示さなければならない。",
    null
  ],
  [
    "apply",
    "A2",
    "動詞",
    [
      "応募する",
      "適用する"
    ],
    "/əˈplaɪ/",
    "You can apply for the position online.",
    "その職にはオンラインで応募できる。",
    null
  ],
  [
    "appropriately",
    "B2",
    "副詞",
    [
      "適切に",
      "ふさわしく"
    ],
    "/əˈproʊpriɪtli/",
    "Please dress appropriately for the formal ceremony.",
    "正式な式典にふさわしい服装をしてください。",
    null
  ],
  [
    "approval",
    "B2",
    "名詞",
    [
      "承認",
      "賛成"
    ],
    "/əˈpruvəl/",
    "The project cannot begin without official approval.",
    "その事業は正式な承認なしには開始できない。",
    null
  ],
  [
    "architect",
    "A2",
    "名詞",
    [
      "建築家",
      "建築技師"
    ],
    "/ˈɑrkətɛkt/",
    "The architect designed the building to use natural light.",
    "建築家は自然光を活用するようその建物を設計した。",
    null
  ],
  [
    "architecture",
    "A2",
    "名詞",
    [
      "建築術",
      "建築学"
    ],
    "/ˈɑrkətɛktʃɚ/",
    "The city is famous for its modern architecture.",
    "その都市は近代建築で有名だ。",
    null
  ],
  [
    "argue",
    "A2",
    "動詞",
    [
      "議論する",
      "を議論する"
    ],
    "/ˈɑrgju/",
    "Experts continue to argue about the best solution.",
    "専門家は最善の解決策について議論を続けている。",
    null
  ],
  [
    "armed",
    "B2",
    "形容詞",
    [
      "武装した",
      "用意した"
    ],
    "/ɑrmd/",
    "Two armed guards stood outside the entrance.",
    "武装した警備員2人が入口の外に立っていた。",
    null
  ],
  [
    "arms",
    "B2",
    "名詞",
    [
      "兵器"
    ],
    "/ɑrmz/",
    "The two countries agreed to reduce their nuclear arms.",
    "両国は核兵器を削減することに合意した。",
    null
  ],
  [
    "army",
    "A2",
    "名詞",
    [
      "軍",
      "陸軍"
    ],
    "/ˈɑrmi/",
    "The army delivered food and water after the earthquake.",
    "軍は地震後に食料と水を届けた。",
    null
  ],
  [
    "arrival",
    "B1",
    "名詞",
    [
      "到着",
      "到着した人"
    ],
    "/ɚˈaɪvəl/",
    "Please call me immediately upon your arrival.",
    "到着したらすぐに私に電話してください。",
    null
  ],
  [
    "arrow",
    "B2",
    "名詞",
    [
      "矢印",
      "矢"
    ],
    "/ˈæroʊ/",
    "Follow the blue arrow to reach the main entrance.",
    "正面入口へ行くには青い矢印に従ってください。",
    null
  ],
  [
    "artistic",
    "B2",
    "形容詞",
    [
      "芸術家の",
      "芸術的な"
    ],
    "/ɑrˈtɪstɪk/",
    "The neighbourhood is known for its artistic community.",
    "その地区は芸術家の多いコミュニティーで知られている。",
    null
  ],
  [
    "artwork",
    "B2",
    "名詞",
    [
      "芸術作品"
    ],
    "/ˈɑrtwɝk/",
    "Local artwork is displayed throughout the hotel.",
    "地元の芸術作品がホテルの至る所に展示されている。",
    null
  ],
  [
    "as",
    "A2",
    "副詞・接続詞",
    [
      "〜として"
    ],
    "/æz/",
    "She works as an editor for an international magazine.",
    "彼女は国際的な雑誌の編集者として働いている。",
    null
  ],
  [
    "aside",
    "B2",
    "副詞",
    [
      "別にしておいて",
      "しまっておいて"
    ],
    "/əˈsaɪd/",
    "He put the report aside and answered the phone.",
    "彼は報告書を脇に置いて電話に出た。",
    null
  ],
  [
    "asleep",
    "A2",
    "形容詞",
    [
      "眠って"
    ],
    "/əˈslip/",
    "The baby was already asleep when we arrived home.",
    "帰宅した時、赤ちゃんはすでに眠っていた。",
    null
  ],
  [
    "assessment",
    "B2",
    "名詞",
    [
      "評価",
      "評価額"
    ],
    "/əˈsɛsmənt/",
    "A full assessment of the damage will take several days.",
    "被害の全面的な評価には数日かかるだろう。",
    null
  ],
  [
    "asset",
    "B2",
    "名詞",
    [
      "強み",
      "資産"
    ],
    "/ˈæsɛt/",
    "Her ability to speak three languages is a valuable asset.",
    "3言語を話せる能力は彼女の貴重な強みだ。",
    null
  ],
  [
    "assign",
    "B2",
    "動詞",
    [
      "を割り当てる"
    ],
    "/əˈsaɪn/",
    "The teacher will assign each group a different topic.",
    "先生は各グループに別々の話題を割り当てる。",
    null
  ],
  [
    "assistance",
    "B2",
    "名詞",
    [
      "手助け",
      "支援"
    ],
    "/əˈsɪstəns/",
    "Please ask a member of staff if you need assistance.",
    "手助けが必要なら職員に声をかけてください。",
    null
  ],
  [
    "assistant",
    "A2",
    "形容詞・名詞",
    [
      "助手",
      "助…"
    ],
    "/əˈsɪstənt/",
    "The research assistant organized the survey results.",
    "研究助手は調査結果を整理した。",
    null
  ],
  [
    "associated",
    "B2",
    "形容詞",
    [
      "関連した"
    ],
    "/əˈsoʊsieɪtɪd/",
    "Regular exercise is associated with better mental health.",
    "定期的な運動はより良い心の健康と関連している。",
    null
  ],
  [
    "assumption",
    "B2",
    "名詞",
    [
      "想定"
    ],
    "/əˈsʌmpʃən/",
    "The plan was based on the assumption that prices would remain stable.",
    "その計画は価格が安定したままだという想定に基づいていた。",
    null
  ],
  [
    "astonishing",
    "B2",
    "形容詞",
    [
      "驚くべき"
    ],
    "/əˈstɑnɪʃɪŋ/",
    "The team made astonishing progress in just three months.",
    "そのチームはわずか3か月で驚くべき進歩を遂げた。",
    null
  ],
  [
    "athlete",
    "A2",
    "名詞",
    [
      "陸上競技選手"
    ],
    "/ˈæθlit/",
    "The young athlete trains before school every morning.",
    "その若い選手は毎朝、登校前に練習する。",
    null
  ],
  [
    "attachment",
    "B2",
    "名詞",
    [
      "添付ファイル",
      "愛着"
    ],
    "/əˈtætʃmənt/",
    "I have included the schedule as an email attachment.",
    "日程表をメールの添付ファイルとして入れました。",
    null
  ],
  [
    "attack",
    "A2",
    "名詞・動詞",
    [
      "攻撃",
      "攻撃する"
    ],
    "/əˈtæk/",
    "The website went offline after a cyber attack.",
    "そのウェブサイトはサイバー攻撃の後、停止した。",
    null
  ],
  [
    "attention",
    "A2",
    "間投詞・名詞",
    [
      "注意",
      "注意力"
    ],
    "/əˈtɛnʃən/",
    "Please pay close attention to the safety instructions.",
    "安全上の指示に十分注意してください。",
    null
  ],
  [
    "attraction",
    "B1",
    "名詞",
    [
      "観光名所",
      "魅力"
    ],
    "/əˈtrækʃən/",
    "The historic castle is the town's main tourist attraction.",
    "その歴史的な城は町の主要な観光名所だ。",
    null
  ],
  [
    "auction",
    "B2",
    "名詞",
    [
      "競売",
      "を競売にかける"
    ],
    "/ˈɑkʃən/",
    "The painting was sold at auction for a record price.",
    "その絵は競売で記録的な価格で売られた。",
    null
  ],
  [
    "audio",
    "B2",
    "形容詞",
    [
      "音声",
      "音声の"
    ],
    "/ˈɑdioʊ/",
    "The course includes audio material for listening practice.",
    "その講座にはリスニング練習用の音声教材が含まれている。",
    null
  ],
  [
    "author",
    "A2",
    "名詞",
    [
      "著者"
    ],
    "/ˈɔθɚ/",
    "The author answered questions after reading from her new novel.",
    "著者は新作小説を朗読した後、質問に答えた。",
    null
  ],
  [
    "automatic",
    "B2",
    "形容詞",
    [
      "自動式の",
      "自動式ライフル"
    ],
    "/ɔtəˈmætɪk/",
    "The doors are automatic and open when you approach them.",
    "そのドアは自動式で、近づくと開く。",
    null
  ],
  [
    "awful",
    "A2",
    "形容詞",
    [
      "ひどい",
      "恐ろしい"
    ],
    "/ˈɑfəl/",
    "The weather was awful, so we cancelled the picnic.",
    "天気がひどかったので、私たちはピクニックを中止した。",
    null
  ],
  [
    "back",
    "A2",
    "形容詞・動詞",
    [
      "裏",
      "後部にある"
    ],
    "/bæk/",
    "The shop has a small garden at the back.",
    "その店の裏には小さな庭がある。",
    null
  ],
  [
    "background",
    "A2",
    "名詞",
    [
      "経歴"
    ],
    "/ˈbækgraʊnd/",
    "Her background in engineering helped her solve the problem.",
    "工学の経歴が、彼女が問題を解決する助けになった。",
    null
  ],
  [
    "backwards",
    "B1",
    "副詞",
    [
      "後ろ向きに"
    ],
    "/ˈbækwɚdz/",
    "He took two steps backwards to see the whole picture.",
    "彼は絵全体を見るために2歩後ろへ下がった。",
    null
  ],
  [
    "bacteria",
    "B2",
    "名詞",
    [
      "細菌"
    ],
    "/bækˈtɪriə/",
    "Some bacteria are useful for making food such as yogurt.",
    "細菌の中にはヨーグルトなどの食品作りに役立つものがある。",
    null
  ],
  [
    "badge",
    "B2",
    "名詞",
    [
      "バッジ"
    ],
    "/bædʒ/",
    "Visitors must wear a badge inside the building.",
    "訪問者は建物内でバッジを着けなければならない。",
    null
  ],
  [
    "badly",
    "A2",
    "副詞",
    [
      "ひどく"
    ],
    "/ˈbædli/",
    "The roof was badly damaged by the storm.",
    "屋根は嵐でひどく損傷した。",
    null
  ],
  [
    "bake",
    "B1",
    "動詞",
    [
      "パンを焼く",
      "を焼く"
    ],
    "/beɪk/",
    "We decided to bake some bread for the neighbours.",
    "私たちは近所の人たちにパンを焼くことにした。",
    null
  ],
  [
    "balanced",
    "B2",
    "形容詞",
    [
      "バランスが取れた",
      "調和のとれた"
    ],
    "/ˈbælənst/",
    "A balanced diet should include a variety of foods.",
    "バランスの取れた食事には多様な食品を含めるべきだ。",
    null
  ],
  [
    "ballet",
    "B2",
    "名詞",
    [
      "バレエ",
      "バレエ団"
    ],
    "/bæˈleɪ/",
    "She has studied ballet since she was six years old.",
    "彼女は6歳の時からバレエを習っている。",
    null
  ],
  [
    "balloon",
    "B2",
    "名詞",
    [
      "風船"
    ],
    "/bəˈlun/",
    "A red balloon floated above the crowd.",
    "赤い風船が群衆の上に浮かんでいた。",
    null
  ],
  [
    "bar",
    "A2",
    "名詞・動詞",
    [
      "バー"
    ],
    "/bɑr/",
    "We met at a quiet bar near the station.",
    "私たちは駅近くの静かなバーで会った。",
    null
  ],
  [
    "barely",
    "B2",
    "副詞",
    [
      "かろうじて、やっと",
      "ほとんど〜ない"
    ],
    "/ˈbɛrli/",
    "I could barely hear the speaker from the back of the hall.",
    "ホールの後ろからは話し手の声がほとんど聞こえなかった。",
    null
  ],
  [
    "base",
    "B1",
    "名詞・動詞",
    [
      "拠点を置く"
    ],
    "/beɪs/",
    "The company will base its Asian operations in Osaka.",
    "その会社はアジア事業の拠点を大阪に置く。",
    null
  ],
  [
    "baseball",
    "A2",
    "名詞",
    [
      "野球"
    ],
    "/ˈbeɪsˈbɔl/",
    "They play baseball in the park every Sunday.",
    "彼らは毎週日曜日に公園で野球をする。",
    null
  ],
  [
    "based",
    "A2",
    "形容詞",
    [
      "〜に基づいた"
    ],
    "/beɪst/",
    "The film is based on a true story.",
    "その映画は実話に基づいている。",
    null
  ],
  [
    "basement",
    "B2",
    "名詞",
    [
      "地下室"
    ],
    "/ˈbeɪsmənt/",
    "We store old furniture in the basement.",
    "私たちは古い家具を地下室に保管している。",
    null
  ],
  [
    "basic",
    "B1",
    "形容詞",
    [
      "基本的な"
    ],
    "/ˈbeɪsɪk/",
    "The course teaches basic computer skills.",
    "その講座はコンピューターの基本技能を教える。",
    null
  ],
  [
    "basically",
    "B2",
    "副詞",
    [
      "基本的に",
      "根本的に"
    ],
    "/ˈbeɪsɪkli/",
    "The two proposals are basically the same.",
    "その2つの提案は基本的に同じだ。",
    null
  ],
  [
    "basket",
    "B2",
    "名詞",
    [
      "かご",
      "かご1杯"
    ],
    "/ˈbæskət/",
    "She carried the vegetables home in a basket.",
    "彼女は野菜をかごに入れて家へ運んだ。",
    null
  ],
  [
    "basketball",
    "A2",
    "名詞",
    [
      "バスケットボール",
      "バスケットボール用のボール"
    ],
    "/ˈbæskətbɔl/",
    "My brother joined the school basketball team.",
    "弟は学校のバスケットボール部に入った。",
    null
  ],
  [
    "bat",
    "B2",
    "名詞",
    [
      "コウモリ"
    ],
    "/bæt/",
    "A bat flew out of the cave at sunset.",
    "日没時にコウモリが洞窟から飛び出した。",
    null
  ],
  [
    "battery",
    "B1",
    "名詞",
    [
      "電池"
    ],
    "/ˈbætɚi/",
    "The phone battery should last for two days.",
    "その電話の電池は2日間もつはずだ。",
    null
  ],
  [
    "bean",
    "A2",
    "名詞",
    [
      "豆"
    ],
    "/bin/",
    "Add each bean to the soup after soaking it overnight.",
    "一晩水につけた豆をスープに加えてください。",
    null
  ],
  [
    "beat",
    "A2",
    "名詞・動詞",
    [
      "打ち負かす",
      "たたく"
    ],
    "/bit/",
    "Our team hopes to beat last year's champions.",
    "私たちのチームは昨年の優勝チームに勝ちたいと思っている。",
    null
  ],
  [
    "beauty",
    "B1",
    "名詞",
    [
      "美しさ",
      "美"
    ],
    "/bˈjuti/",
    "Visitors come to admire the natural beauty of the island.",
    "訪問者はその島の自然の美しさを楽しみに来る。",
    null
  ],
  [
    "bee",
    "B1",
    "名詞",
    [
      "はち"
    ],
    "/bi/",
    "A bee landed on the yellow flower.",
    "一匹のミツバチが黄色い花に止まった。",
    null
  ],
  [
    "beef",
    "A2",
    "名詞",
    [
      "牛肉",
      "肉"
    ],
    "/bif/",
    "The restaurant buys its beef from local farms.",
    "そのレストランは地元の農場から牛肉を仕入れている。",
    null
  ],
  [
    "before",
    "A2",
    "副詞・接続詞",
    [
      "前に",
      "の前に"
    ],
    "/bɪˈfɔr/",
    "Please read the instructions before you begin.",
    "始める前に説明を読んでください。",
    null
  ],
  [
    "beg",
    "B2",
    "動詞",
    [
      "を懇願する",
      "に懇願する"
    ],
    "/bɛg/",
    "The charity had to beg for additional support.",
    "その慈善団体は追加支援を懇願しなければならなかった。",
    null
  ],
  [
    "behaviour",
    "A2",
    "名詞",
    [
      "行動"
    ],
    "/bɪˈheɪvjɚ/",
    "The teacher praised the students for their responsible behaviour.",
    "先生は生徒たちの責任ある行動を褒めた。",
    null
  ],
  [
    "being",
    "B2",
    "名詞",
    [
      "人間"
    ],
    "/ˈbiɪŋ/",
    "Every human being needs clean water and a safe place to live.",
    "すべての人間には清潔な水と安全に暮らせる場所が必要だ。",
    null
  ],
  [
    "bell",
    "B1",
    "名詞",
    [
      "鐘"
    ],
    "/bɛl/",
    "The church bell rang at noon.",
    "教会の鐘が正午に鳴った。",
    null
  ],
  [
    "belt",
    "A2",
    "名詞",
    [
      "ベルト",
      "ベルト状のもの"
    ],
    "/bɛlt/",
    "Remember to fasten your seat belt before takeoff.",
    "離陸前にシートベルトを締めるのを忘れないでください。",
    null
  ],
  [
    "bend",
    "B1",
    "名詞・動詞",
    [
      "を曲げる",
      "を曲げさせる"
    ],
    "/bɛnd/",
    "Bend your knees slightly when you lift the box.",
    "箱を持ち上げる時は膝を少し曲げなさい。",
    null
  ],
  [
    "beneficial",
    "B2",
    "形容詞",
    [
      "有益な"
    ],
    "/bɛnəˈfɪʃəl/",
    "Daily reading is beneficial for vocabulary development.",
    "毎日の読書は語彙力の向上に役立つ。",
    null
  ],
  [
    "bent",
    "B2",
    "形容詞",
    [
      "曲がった"
    ],
    "/bɛnt/",
    "The metal frame was bent in the accident.",
    "金属製の枠は事故で曲がった。",
    null
  ],
  [
    "beside",
    "B2",
    "前置詞",
    [
      "の横に"
    ],
    "/bɪˈsaɪd/",
    "A small table stood beside the bed.",
    "ベッドの横に小さなテーブルがあった。",
    null
  ],
  [
    "best",
    "A2",
    "副詞・名詞",
    [
      "最善"
    ],
    "/bɛst/",
    "This is the best solution we have found so far.",
    "これはこれまでに見つけた最善の解決策だ。",
    null
  ],
  [
    "bet",
    "B2",
    "名詞・動詞",
    [
      "きっと〜だと思う",
      "賭ける"
    ],
    "/bɛt/",
    "I bet the train will be crowded this evening.",
    "今晩の電車は混むと思うよ。",
    null
  ],
  [
    "better",
    "A2",
    "副詞・名詞",
    [
      "もっとすぐれた",
      "前よりよい"
    ],
    "/ˈbɛtɚ/",
    "The new software works much better than the old version.",
    "新しいソフトウェアは旧版よりずっとうまく動く。",
    null
  ],
  [
    "between",
    "A2",
    "副詞",
    [
      "の間で",
      "の間に"
    ],
    "/bɪtˈwin/",
    "The agreement was signed between the two organizations.",
    "その協定は2つの組織の間で結ばれた。",
    null
  ],
  [
    "beyond",
    "B2",
    "副詞・前置詞",
    [
      "の向こうに",
      "向こうに"
    ],
    "/bɪˈɑnd/",
    "The path continues beyond the bridge.",
    "その道は橋の向こうまで続いている。",
    null
  ],
  [
    "bias",
    "B2",
    "名詞",
    [
      "偏り",
      "偏見"
    ],
    "/ˈbaɪəs/",
    "Good researchers try to recognize and reduce bias.",
    "優れた研究者は偏りを認識し減らそうとする。",
    null
  ],
  [
    "bid",
    "B2",
    "名詞・動詞",
    [
      "入札",
      "入札する"
    ],
    "/bɪd/",
    "Three companies made a bid for the construction contract.",
    "3社がその建設契約に入札した。",
    null
  ],
  [
    "bin",
    "A2",
    "名詞",
    [
      "ごみ箱",
      "容器"
    ],
    "/bɪn/",
    "Please put empty bottles in the recycling bin.",
    "空の瓶はリサイクル用の箱に入れてください。",
    null
  ],
  [
    "biological",
    "B2",
    "形容詞",
    [
      "生物学的な",
      "生物学の"
    ],
    "/baɪəˈlɑdʒɪkəl/",
    "The study examines biological differences between the species.",
    "その研究は種の間の生物学的な違いを調べている。",
    null
  ],
  [
    "birth",
    "A2",
    "名詞",
    [
      "出産",
      "誕生"
    ],
    "/bɝθ/",
    "The hospital recorded more than two thousand births last year.",
    "その病院では昨年2,000件を超える出産が記録された。",
    null
  ],
  [
    "biscuit",
    "A2",
    "名詞",
    [
      "ビスケット"
    ],
    "/ˈbɪskət/",
    "She offered each guest a biscuit with tea.",
    "彼女は客一人ひとりに紅茶とビスケットを出した。",
    null
  ],
  [
    "bit",
    "A2",
    "名詞",
    [
      "少し"
    ],
    "/bɪt/",
    "Could you move the chair a bit closer?",
    "椅子をもう少し近くへ動かしてもらえますか。",
    null
  ],
  [
    "bitter",
    "B2",
    "形容詞",
    [
      "苦い"
    ],
    "/ˈbɪtɚ/",
    "The medicine has a bitter taste.",
    "その薬は苦い味がする。",
    null
  ],
  [
    "blank",
    "A2",
    "形容詞・名詞",
    [
      "空白",
      "空白の"
    ],
    "/blæŋk/",
    "Leave this section blank if it does not apply to you.",
    "自分に当てはまらなければ、この欄は空白にしてください。",
    null
  ],
  [
    "blanket",
    "B2",
    "名詞",
    [
      "毛布",
      "一面に広がっておおう物"
    ],
    "/ˈblæŋkət/",
    "We took an extra blanket because the night was cold.",
    "夜が寒かったので、私たちは毛布をもう1枚持っていった。",
    null
  ],
  [
    "blind",
    "B2",
    "形容詞",
    [
      "目の見えない",
      "盲目の"
    ],
    "/blaɪnd/",
    "The organization provides guide dogs for blind people.",
    "その団体は目の不自由な人に盲導犬を提供している。",
    null
  ],
  [
    "block",
    "B1",
    "名詞・動詞",
    [
      "をふさぐ"
    ],
    "/blɑk/",
    "A fallen tree continued to block the road.",
    "倒れた木が道路をふさぎ続けていた。",
    null
  ],
  [
    "blood",
    "A2",
    "名詞",
    [
      "血"
    ],
    "/blʌd/",
    "Donating blood can help save lives.",
    "献血は命を救う助けになる。",
    null
  ],
  [
    "blow",
    "A2",
    "名詞・動詞",
    [
      "風で動く",
      "吹き飛ぶ"
    ],
    "/bloʊ/",
    "Strong winds can blow sand across the road.",
    "強風で砂が道路を横切って飛ぶことがある。",
    null
  ],
  [
    "board",
    "A2",
    "名詞・動詞",
    [
      "理事会"
    ],
    "/bɔrd/",
    "The board will review the proposal next week.",
    "理事会は来週その提案を検討する。",
    null
  ],
  [
    "boil",
    "A2",
    "動詞",
    [
      "沸騰",
      "沸騰点"
    ],
    "/bɔɪl/",
    "Boil the water for at least one minute before drinking it.",
    "飲む前に水を少なくとも1分間沸騰させてください。",
    null
  ],
  [
    "bold",
    "B2",
    "形容詞",
    [
      "大胆な"
    ],
    "/boʊld/",
    "It was a bold decision to launch the product overseas first.",
    "その製品をまず海外で発売するのは大胆な決定だった。",
    null
  ],
  [
    "bomb",
    "B1",
    "名詞・動詞",
    [
      "に爆弾を投下する"
    ],
    "/bɑm/",
    "Police safely removed the unexploded bomb.",
    "警察は不発弾を安全に撤去した。",
    null
  ],
  [
    "bombing",
    "B2",
    "名詞",
    [
      "爆撃"
    ],
    "/ˈbɑmɪŋ/",
    "The museum exhibition describes the effects of the bombing.",
    "その博物館の展示は爆撃の影響を説明している。",
    null
  ],
  [
    "bone",
    "A2",
    "名詞",
    [
      "骨",
      "骨を作っている物質"
    ],
    "/boʊn/",
    "The doctor confirmed that no bone was broken.",
    "医師は骨が折れていないことを確認した。",
    null
  ],
  [
    "book",
    "A2",
    "動詞",
    [
      "を予約する",
      "予約をする"
    ],
    "/bʊk/",
    "You should book your seat several weeks in advance.",
    "数週間前に席を予約した方がよい。",
    null
  ],
  [
    "booking",
    "B2",
    "名詞",
    [
      "予約"
    ],
    "/ˈbʊkɪŋ/",
    "I received an email confirming my hotel booking.",
    "ホテルの予約を確認するメールを受け取った。",
    null
  ],
  [
    "borrow",
    "A2",
    "動詞",
    [
      "を借りてまねる",
      "を借りる"
    ],
    "/ˈbɑroʊ/",
    "Can I borrow your dictionary until tomorrow?",
    "明日まであなたの辞書を借りてもいいですか。",
    null
  ],
  [
    "boss",
    "A2",
    "名詞",
    [
      "を支配する"
    ],
    "/bɑs/",
    "My boss encouraged me to apply for the position.",
    "上司は私にその職へ応募するよう勧めた。",
    null
  ],
  [
    "bottom",
    "A2",
    "形容詞・名詞",
    [
      "下部"
    ],
    "/ˈbɑtəm/",
    "Your name should appear at the bottom of the form.",
    "氏名は用紙の下部に記載してください。",
    null
  ],
  [
    "bound",
    "B2",
    "形容詞",
    [
      "行きの",
      "「…行きの」の意を表す"
    ],
    "/baʊnd/",
    "The train is bound for the airport.",
    "その電車は空港行きだ。",
    null
  ],
  [
    "bowl",
    "A2",
    "名詞",
    [
      "ボウル",
      "一杯"
    ],
    "/boʊl/",
    "She ordered a bowl of vegetable soup.",
    "彼女は野菜スープを一杯注文した。",
    null
  ],
  [
    "brain",
    "A2",
    "名詞",
    [
      "脳"
    ],
    "/breɪn/",
    "Sleep gives the brain time to process new information.",
    "睡眠は脳に新しい情報を処理する時間を与える。",
    null
  ],
  [
    "branch",
    "B1",
    "名詞",
    [
      "支店"
    ],
    "/bræntʃ/",
    "The bank plans to open a new branch near the university.",
    "その銀行は大学の近くに新しい支店を開く予定だ。",
    null
  ],
  [
    "brave",
    "B1",
    "形容詞",
    [
      "勇敢な",
      "に勇敢に立ち向かう"
    ],
    "/breɪv/",
    "The brave firefighter entered the burning building.",
    "勇敢な消防士は燃えている建物に入った。",
    null
  ],
  [
    "breast",
    "B2",
    "名詞",
    [
      "乳"
    ],
    "/brɛst/",
    "Early tests can help detect breast cancer.",
    "早期検査は乳がんの発見に役立つ。",
    null
  ],
  [
    "breathing",
    "B1",
    "名詞",
    [
      "呼吸",
      "一呼吸の間"
    ],
    "/ˈbriðɪŋ/",
    "Slow breathing can help you feel calmer.",
    "ゆっくりした呼吸は気持ちを落ち着かせる助けになる。",
    null
  ],
  [
    "brick",
    "B2",
    "名詞",
    [
      "れんが",
      "を=れんがで囲う"
    ],
    "/brɪk/",
    "The old school was built of red brick.",
    "その古い学校は赤れんがで建てられていた。",
    null
  ],
  [
    "bride",
    "B1",
    "名詞",
    [
      "花嫁"
    ],
    "/braɪd/",
    "The bride thanked everyone for coming to the wedding.",
    "花嫁は結婚式に来てくれた全員に感謝した。",
    null
  ],
  [
    "bridge",
    "A2",
    "名詞",
    [
      "橋"
    ],
    "/brɪdʒ/",
    "The new bridge has reduced travel time between the towns.",
    "新しい橋によって町どうしの移動時間が短くなった。",
    null
  ],
  [
    "briefly",
    "B2",
    "副詞",
    [
      "手短に"
    ],
    "/ˈbrifli/",
    "The chairperson briefly explained the purpose of the meeting.",
    "議長は会議の目的を手短に説明した。",
    null
  ],
  [
    "bright",
    "A2",
    "形容詞",
    [
      "明るく",
      "晴れた"
    ],
    "/braɪt/",
    "The room felt bright and welcoming after it was painted.",
    "塗装後、その部屋は明るく居心地よく感じられた。",
    null
  ],
  [
    "brilliant",
    "A2",
    "形容詞",
    [
      "宝石に見えるようにカットした石"
    ],
    "/ˈbrɪljənt/",
    "She suggested a brilliant solution to the design problem.",
    "彼女は設計上の問題に見事な解決策を提案した。",
    null
  ],
  [
    "broadcaster",
    "B2",
    "名詞",
    [
      "放送局",
      "放送者"
    ],
    "/ˈbrɔdkæstɚ/",
    "The public broadcaster will show the debate live.",
    "公共放送局は討論会を生中継する。",
    null
  ],
  [
    "broadly",
    "B2",
    "副詞",
    [
      "広く"
    ],
    "/ˈbrɔdli/",
    "The new policy has been broadly welcomed by teachers.",
    "新しい方針は教師たちに広く歓迎されている。",
    null
  ],
  [
    "broken",
    "A2",
    "形容詞",
    [
      "壊れた",
      "折れた"
    ],
    "/ˈbroʊkən/",
    "Take care because the broken glass is still on the floor.",
    "割れたガラスがまだ床にあるので気をつけて。",
    null
  ],
  [
    "brush",
    "A2",
    "名詞・動詞",
    [
      "ブラシ",
      "ブラシをかけること"
    ],
    "/brʌʃ/",
    "Use a soft brush to clean the surface.",
    "表面を掃除するには柔らかいブラシを使ってください。",
    null
  ],
  [
    "bubble",
    "B1",
    "名詞",
    [
      "あわ"
    ],
    "/ˈbʌbəl/",
    "A large bubble rose to the surface of the water.",
    "大きな泡が水面に浮かび上がった。",
    null
  ],
  [
    "bug",
    "B2",
    "名詞",
    [
      "バグ",
      "不具合",
      "虫"
    ],
    "/bʌg/",
    "The developers fixed a bug that caused the app to crash.",
    "開発者はアプリを停止させていた不具合を修正した。",
    null
  ],
  [
    "bullet",
    "B2",
    "名詞",
    [
      "弾丸"
    ],
    "/ˈbʊlət/",
    "Police found a bullet near the damaged vehicle.",
    "警察は損傷した車両の近くで弾丸を見つけた。",
    null
  ],
  [
    "bunch",
    "B2",
    "名詞",
    [
      "束"
    ],
    "/bʌntʃ/",
    "She brought a bunch of flowers to the hospital.",
    "彼女は病院に花束を持ってきた。",
    null
  ],
  [
    "burn",
    "A2",
    "名詞・動詞",
    [
      "燃える"
    ],
    "/bɝn/",
    "Dry leaves burn very quickly in hot weather.",
    "乾いた葉は暑い天気では非常に速く燃える。",
    null
  ],
  [
    "bush",
    "B2",
    "名詞",
    [
      "茂み",
      "低木"
    ],
    "/bʊʃ/",
    "A small bird was hiding in the bush.",
    "小鳥が茂みの中に隠れていた。",
    null
  ],
  [
    "businessman",
    "A2",
    "名詞",
    [
      "実業家"
    ],
    "/ˈbɪznəsmæn/",
    "The local businessman invested in several community projects.",
    "地元の実業家はいくつかの地域事業に投資した。",
    null
  ],
  [
    "but",
    "B2",
    "前置詞",
    [
      "しかし"
    ],
    "/bʌt/",
    "The apartment is small but comfortable.",
    "そのアパートは小さいが快適だ。",
    null
  ],
  [
    "button",
    "A2",
    "名詞",
    [
      "ボタン",
      "にボタンをかける"
    ],
    "/ˈbʌtən/",
    "Press the green button to save your changes.",
    "変更を保存するには緑のボタンを押してください。",
    null
  ],
  [
    "by",
    "B1",
    "副詞",
    [
      "〜までに",
      "〜によって"
    ],
    "/baɪ/",
    "The report must be completed by Friday.",
    "報告書は金曜日までに完成させなければならない。",
    null
  ],
  [
    "cabin",
    "B2",
    "名詞",
    [
      "小屋"
    ],
    "/ˈkæbən/",
    "We stayed in a wooden cabin beside the lake.",
    "私たちは湖畔の木造小屋に泊まった。",
    null
  ],
  [
    "cable",
    "B2",
    "名詞",
    [
      "ケーブル線",
      "にケーブルを敷く"
    ],
    "/ˈkeɪbəl/",
    "A damaged cable caused the internet connection to fail.",
    "損傷したケーブルのせいでインターネット接続が切れた。",
    null
  ],
  [
    "calm",
    "B1",
    "形容詞・名詞・動詞",
    [
      "冷静な",
      "穏やかな"
    ],
    "/kɑm/",
    "She remained calm throughout the emergency.",
    "彼女は緊急事態の間ずっと冷静だった。",
    null
  ],
  [
    "camp",
    "A2",
    "名詞・動詞",
    [
      "野営地",
      "野営"
    ],
    "/kæmp/",
    "We set up camp before it became dark.",
    "暗くなる前に私たちは野営地を設けた。",
    null
  ],
  [
    "camping",
    "A2",
    "名詞",
    [
      "キャンプ"
    ],
    "/ˈkæmpɪŋ/",
    "The family goes camping beside the lake every summer.",
    "その家族は毎夏、湖畔へキャンプに行く。",
    null
  ],
  [
    "campus",
    "B1",
    "名詞",
    [
      "キャンパス"
    ],
    "/ˈkæmpəs/",
    "Smoking is not allowed anywhere on campus.",
    "キャンパス内ではどこでも喫煙が禁止されている。",
    null
  ],
  [
    "can",
    "A2",
    "名詞",
    [
      "〜できる"
    ],
    "/kæn/",
    "This machine can translate short messages automatically.",
    "この機械は短いメッセージを自動で翻訳できる。",
    null
  ],
  [
    "canal",
    "B2",
    "名詞",
    [
      "運河",
      "運河状の地形"
    ],
    "/kəˈnæl/",
    "A narrow canal connects the river with the harbour.",
    "細い運河が川と港を結んでいる。",
    null
  ],
  [
    "cancer",
    "B2",
    "名詞",
    [
      "がん"
    ],
    "/ˈkænsɚ/",
    "Early diagnosis can improve the treatment of cancer.",
    "早期診断はがん治療の改善につながりうる。",
    null
  ],
  [
    "candle",
    "B2",
    "名詞",
    [
      "ろうそく"
    ],
    "/ˈkændəl/",
    "She lit a candle when the electricity went off.",
    "停電した時、彼女はろうそくに火をつけた。",
    null
  ],
  [
    "cap",
    "B1",
    "名詞",
    [
      "帽子",
      "に帽子をかぶせる"
    ],
    "/kæp/",
    "He wore a blue cap to protect his face from the sun.",
    "彼は日差しから顔を守るため青い帽子をかぶった。",
    null
  ],
  [
    "captain",
    "B1",
    "名詞",
    [
      "機長",
      "長"
    ],
    "/ˈkæptən/",
    "The captain asked the passengers to remain seated.",
    "機長は乗客に座ったままでいるよう求めた。",
    null
  ],
  [
    "carbon",
    "B2",
    "名詞",
    [
      "炭素",
      "炭素棒"
    ],
    "/ˈkɑrbən/",
    "The new design produces less carbon during manufacture.",
    "新しい設計では製造時に出る炭素が少ない。",
    null
  ],
  [
    "care",
    "A2",
    "名詞・動詞",
    [
      "気にする"
    ],
    "/kɛr/",
    "Good teachers care about the progress of every student.",
    "よい教師は生徒一人ひとりの成長を気にかける。",
    null
  ],
  [
    "careful",
    "A2",
    "形容詞",
    [
      "気をつける"
    ],
    "/ˈkɛrfəl/",
    "Be careful when crossing this busy road.",
    "この交通量の多い道路を渡る時は気をつけて。",
    null
  ],
  [
    "carefully",
    "A2",
    "副詞",
    [
      "注意深く"
    ],
    "/ˈkɛrfəli/",
    "She carefully compared the two contracts before signing.",
    "彼女は署名する前に2つの契約書を慎重に比較した。",
    null
  ],
  [
    "carpet",
    "A2",
    "名詞",
    [
      "じゅうたん",
      "にじゅうたんを敷く"
    ],
    "/ˈkɑrpət/",
    "A thick carpet made the room feel warmer.",
    "厚いじゅうたんのおかげで部屋がより暖かく感じられた。",
    null
  ],
  [
    "cartoon",
    "A2",
    "名詞",
    [
      "風刺漫画",
      "漫画"
    ],
    "/kɑrˈtun/",
    "The newspaper published a cartoon about the election.",
    "その新聞は選挙についての風刺漫画を掲載した。",
    null
  ],
  [
    "case",
    "A2",
    "名詞",
    [
      "事例"
    ],
    "/keɪs/",
    "This case shows why clear safety rules are necessary.",
    "この事例は明確な安全規則が必要な理由を示している。",
    null
  ],
  [
    "cash",
    "A2",
    "名詞",
    [
      "現金",
      "を現金に換える"
    ],
    "/kæʃ/",
    "This small shop accepts cash only.",
    "この小さな店は現金しか受け付けない。",
    null
  ],
  [
    "cast",
    "B2",
    "名詞・動詞",
    [
      "を与える"
    ],
    "/kæst/",
    "The director chose a young actor to join the cast.",
    "監督は出演者に加える若い俳優を選んだ。",
    null
  ],
  [
    "castle",
    "A2",
    "名詞",
    [
      "城"
    ],
    "/ˈkæsəl/",
    "Thousands of visitors explore the castle each year.",
    "毎年何千人もの観光客がその城を見学する。",
    null
  ],
  [
    "casual",
    "B2",
    "形容詞",
    [
      "普段着の",
      "気軽な"
    ],
    "/ˈkæʒəwəl/",
    "The office allows casual clothes on Fridays.",
    "その職場では金曜日に普段着が認められている。",
    null
  ],
  [
    "catch",
    "A2",
    "名詞・動詞",
    [
      "列車などに間に合う"
    ],
    "/kætʃ/",
    "We left early to catch the first train.",
    "私たちは始発電車に乗るため早く出発した。",
    null
  ],
  [
    "cave",
    "B2",
    "名詞",
    [
      "ほら穴"
    ],
    "/keɪv/",
    "The explorers found ancient paintings inside the cave.",
    "探検家たちは洞窟の中で古代の絵を発見した。",
    null
  ],
  [
    "ceiling",
    "B1",
    "名詞",
    [
      "天井"
    ],
    "/ˈsilɪŋ/",
    "A lamp hung from the centre of the ceiling.",
    "照明が天井の中央から下がっていた。",
    null
  ],
  [
    "celebrate",
    "A2",
    "動詞",
    [
      "を祝う"
    ],
    "/ˈsɛləbreɪt/",
    "The team gathered to celebrate its tenth anniversary.",
    "チームは創立10周年を祝うため集まった。",
    null
  ],
  [
    "celebration",
    "B1",
    "名詞",
    [
      "祝賀",
      "祝賀会"
    ],
    "/sɛləˈbreɪʃən/",
    "The victory led to a joyful celebration in the streets.",
    "勝利によって通りでは喜びに満ちた祝賀が行われた。",
    null
  ],
  [
    "celebrity",
    "A2",
    "名詞",
    [
      "有名人"
    ],
    "/səˈlɛbrɪti/",
    "A local celebrity opened the charity event.",
    "地元の有名人が慈善イベントの開会を務めた。",
    null
  ],
  [
    "central",
    "B1",
    "形容詞",
    [
      "中心的な",
      "不可欠な"
    ],
    "/ˈsɛntrəl/",
    "Trust is central to a successful working relationship.",
    "信頼は良好な仕事上の関係に不可欠だ。",
    null
  ],
  [
    "centre",
    "B1",
    "動詞",
    [
      "中心",
      "を中心に置く"
    ],
    "/ˈsɛntɚ/",
    "The program will centre on practical communication skills.",
    "その講座は実用的なコミュニケーション技能を中心にする。",
    null
  ],
  [
    "certain",
    "A2",
    "形容詞",
    [
      "確信している"
    ],
    "/ˈsɝtən/",
    "I am certain that we locked the door before leaving.",
    "出かける前にドアに鍵をかけたと確信している。",
    null
  ],
  [
    "certainly",
    "A2",
    "副詞",
    [
      "きっと"
    ],
    "/ˈsɝtənli/",
    "This experience will certainly help you in the future.",
    "この経験は将来きっとあなたの役に立つ。",
    null
  ],
  [
    "certainty",
    "B2",
    "名詞",
    [
      "確信"
    ],
    "/ˈsɝtənti/",
    "We cannot predict the result with complete certainty.",
    "私たちは完全な確信をもって結果を予測することはできない。",
    null
  ],
  [
    "certificate",
    "B2",
    "名詞",
    [
      "証明書"
    ],
    "/sɚˈtɪfɪkət/",
    "You will receive a certificate after completing the course.",
    "講座を修了すると証明書を受け取れる。",
    null
  ],
  [
    "chair",
    "B2",
    "動詞",
    [
      "議長",
      "の議長をつとめる"
    ],
    "/tʃɛr/",
    "A senior judge will chair the discussion.",
    "上級判事が討論の議長を務める。",
    null
  ],
  [
    "chairman",
    "B2",
    "名詞",
    [
      "議長"
    ],
    "/ˈtʃɛrmən/",
    "The chairman called the meeting to order at nine.",
    "議長は9時に会議の開始を告げた。",
    null
  ],
  [
    "challenging",
    "B2",
    "形容詞",
    [
      "難しい",
      "やりがいのある"
    ],
    "/ˈtʃæləndʒɪŋ/",
    "Learning to negotiate in another language can be challenging.",
    "別の言語で交渉を学ぶのは難しいことがある。",
    null
  ],
  [
    "champion",
    "B1",
    "名詞",
    [
      "優勝者",
      "最優秀賞をとった人"
    ],
    "/ˈtʃæmpiən/",
    "The defending champion won the race by two seconds.",
    "前回の優勝者は2秒差でレースに勝った。",
    null
  ],
  [
    "championship",
    "B2",
    "名詞",
    [
      "選手権試合"
    ],
    "/ˈtʃæmpiənʃɪp/",
    "Our school reached the national championship for the first time.",
    "私たちの学校は初めて全国選手権に進出した。",
    null
  ],
  [
    "chance",
    "A2",
    "名詞",
    [
      "機会"
    ],
    "/tʃæns/",
    "This internship gives students a chance to gain experience.",
    "この実習は学生に経験を積む機会を与える。",
    null
  ],
  [
    "channel",
    "B1",
    "名詞",
    [
      "チャンネル"
    ],
    "/ˈtʃænəl/",
    "Please change the channel if you want to watch the news.",
    "ニュースを見たいならチャンネルを変えてください。",
    null
  ],
  [
    "chapter",
    "B1",
    "名詞",
    [
      "章"
    ],
    "/ˈtʃæptɚ/",
    "The final chapter explains how the problem was solved.",
    "最終章では問題がどのように解決されたかを説明している。",
    null
  ],
  [
    "character",
    "A2",
    "名詞",
    [
      "人"
    ],
    "/ˈkɛrɪktɚ/",
    "The main character faces a difficult moral choice.",
    "主人公は難しい道徳上の選択に直面する。",
    null
  ],
  [
    "charming",
    "B2",
    "形容詞",
    [
      "魅力的な"
    ],
    "/ˈtʃɑrmɪŋ/",
    "We stayed in a charming village near the coast.",
    "私たちは海岸近くの魅力的な村に滞在した。",
    null
  ],
  [
    "chart",
    "B2",
    "動詞",
    [
      "図表",
      "を図表に作る"
    ],
    "/tʃɑrt/",
    "The chart compares energy use in five countries.",
    "その図表は5か国のエネルギー使用量を比較している。",
    null
  ],
  [
    "chat",
    "A2",
    "名詞・動詞",
    [
      "雑談"
    ],
    "/tʃæt/",
    "We had a quick chat before the lecture began.",
    "講義が始まる前に私たちは少し話をした。",
    null
  ],
  [
    "cheap",
    "B1",
    "副詞",
    [
      "値段が安い"
    ],
    "/tʃip/",
    "The ticket was cheap because I booked it early.",
    "早く予約したので切符は安かった。",
    null
  ],
  [
    "check",
    "A2",
    "名詞",
    [
      "確認する",
      "小切手"
    ],
    "/tʃɛk/",
    "Please check that all the windows are closed.",
    "すべての窓が閉まっているか確認してください。",
    null
  ],
  [
    "cheek",
    "B2",
    "名詞",
    [
      "ほお"
    ],
    "/tʃik/",
    "The cold wind made her cheek turn red.",
    "冷たい風で彼女の頬が赤くなった。",
    null
  ],
  [
    "cheer",
    "B2",
    "名詞・動詞",
    [
      "歓声",
      "応援する"
    ],
    "/tʃɪr/",
    "The crowd began to cheer when the players appeared.",
    "選手が姿を見せると観客は歓声を上げ始めた。",
    null
  ],
  [
    "cheerful",
    "B1",
    "形容詞",
    [
      "明るい",
      "陽気な"
    ],
    "/ˈtʃɪrfəl/",
    "Her cheerful voice made everyone feel more relaxed.",
    "彼女の明るい声でみんながよりくつろいだ気分になった。",
    null
  ],
  [
    "chef",
    "A2",
    "名詞",
    [
      "料理人",
      "料理長"
    ],
    "/ʃɛf/",
    "The chef uses vegetables grown on a nearby farm.",
    "その料理人は近くの農場で育てられた野菜を使う。",
    null
  ],
  [
    "chemistry",
    "A2",
    "名詞",
    [
      "化学",
      "化学的性質"
    ],
    "/ˈkɛməstri/",
    "She decided to study chemistry at university.",
    "彼女は大学で化学を学ぶことにした。",
    null
  ],
  [
    "chest",
    "B1",
    "名詞",
    [
      "胸"
    ],
    "/tʃɛst/",
    "The doctor listened to the patient's chest.",
    "医師は患者の胸の音を聴いた。",
    null
  ],
  [
    "chief",
    "B2",
    "形容詞・名詞",
    [
      "主任の",
      "主要な",
      "長"
    ],
    "/tʃif/",
    "The chief engineer approved the final design.",
    "主任技師が最終設計を承認した。",
    null
  ],
  [
    "childhood",
    "B1",
    "名詞",
    [
      "子供時代"
    ],
    "/ˈtʃaɪldhʊd/",
    "That song reminds me of my childhood.",
    "その歌を聞くと子ども時代を思い出す。",
    null
  ],
  [
    "chip",
    "A2",
    "名詞",
    [
      "欠けあと",
      "欠ける"
    ],
    "/tʃɪp/",
    "A small chip in the glass made it unsafe to use.",
    "ガラスの小さな欠けのため、それは安全に使えなくなった。",
    null
  ],
  [
    "choice",
    "A2",
    "名詞",
    [
      "選択肢",
      "選択"
    ],
    "/tʃɔɪs/",
    "Customers have a choice between three payment methods.",
    "客は3つの支払い方法から選べる。",
    null
  ],
  [
    "choir",
    "B2",
    "名詞",
    [
      "合唱団"
    ],
    "/kˈwaɪɚ/",
    "The school choir performed at the winter festival.",
    "学校の合唱団が冬祭りで演奏した。",
    null
  ],
  [
    "chop",
    "B2",
    "動詞",
    [
      "をたたき切って作る",
      "を切って短くする"
    ],
    "/tʃɑp/",
    "Chop the onions into small pieces before adding them.",
    "加える前に玉ねぎを細かく切ってください。",
    null
  ],
  [
    "church",
    "A2",
    "名詞",
    [
      "教会",
      "教会堂"
    ],
    "/tʃɝtʃ/",
    "The old church stands at the centre of the village.",
    "古い教会が村の中心に建っている。",
    null
  ],
  [
    "cigarette",
    "A2",
    "名詞",
    [
      "紙巻きたばこ"
    ],
    "/sɪgɚˈɛt/",
    "He put out his final cigarette and decided to quit.",
    "彼は最後のたばこを消し、禁煙を決意した。",
    null
  ],
  [
    "circle",
    "A2",
    "名詞・動詞",
    [
      "円",
      "円を描く"
    ],
    "/ˈsɝkəl/",
    "Draw a circle around the correct answer.",
    "正解の周りに円を描いてください。",
    null
  ],
  [
    "circuit",
    "B2",
    "名詞",
    [
      "周回",
      "回路"
    ],
    "/ˈsɝkət/",
    "The runners completed three laps of the circuit.",
    "走者たちはコースを3周した。",
    null
  ],
  [
    "civilization",
    "B2",
    "名詞",
    [
      "文明",
      "文明世界"
    ],
    "/sɪvəlɪˈzeɪʃən/",
    "Writing played an important role in the development of civilization.",
    "文字は文明の発展で重要な役割を果たした。",
    null
  ],
  [
    "clarify",
    "B2",
    "動詞",
    [
      "明確にする"
    ],
    "/ˈklɛrəfaɪ/",
    "Could you clarify what you mean by this sentence?",
    "この文で何を意味しているのか明確にしてもらえますか。",
    null
  ],
  [
    "classic",
    "B2",
    "形容詞・名詞",
    [
      "規範となる",
      "規範となる作品"
    ],
    "/ˈklæsɪk/",
    "The novel has become a classic of modern literature.",
    "その小説は現代文学の名作となった。",
    null
  ],
  [
    "classical",
    "A2",
    "形容詞",
    [
      "クラシックの",
      "古典の"
    ],
    "/ˈklæsɪkəl/",
    "She often listens to classical music while working.",
    "彼女は仕事中によくクラシック音楽を聴く。",
    null
  ],
  [
    "clause",
    "B1",
    "名詞",
    [
      "条項"
    ],
    "/klɔz/",
    "The contract includes a clause about early cancellation.",
    "その契約書には早期解約についての条項がある。",
    null
  ],
  [
    "clear",
    "A2",
    "形容詞・動詞",
    [
      "はっきりした",
      "くっきりした"
    ],
    "/klɪr/",
    "The guide gave clear instructions before the tour.",
    "案内人はツアー前に明確な指示を出した。",
    null
  ],
  [
    "clearly",
    "A2",
    "副詞",
    [
      "はっきりと"
    ],
    "/ˈklɪrli/",
    "Please speak clearly so that everyone can understand.",
    "全員が理解できるようにはっきり話してください。",
    null
  ],
  [
    "clerk",
    "B2",
    "名詞",
    [
      "係員",
      "事務員"
    ],
    "/klɝk/",
    "The hotel clerk helped us change our reservation.",
    "ホテルの係員が予約変更を手伝ってくれた。",
    null
  ],
  [
    "clever",
    "A2",
    "形容詞",
    [
      "賢い",
      "巧妙な"
    ],
    "/ˈklɛvɚ/",
    "She found a clever way to reuse the old materials.",
    "彼女は古い材料を再利用する賢い方法を見つけた。",
    null
  ],
  [
    "click",
    "B1",
    "名詞・動詞",
    [
      "クリックする",
      "カチッという音"
    ],
    "/klɪk/",
    "Click the link to open the full report.",
    "リンクをクリックして報告書全体を開いてください。",
    null
  ],
  [
    "cliff",
    "B2",
    "名詞",
    [
      "がけ"
    ],
    "/klɪf/",
    "A narrow path follows the top of the cliff.",
    "細い道が崖の上に沿って続いている。",
    null
  ],
  [
    "climb",
    "B1",
    "名詞",
    [
      "登る",
      "をよじ登る"
    ],
    "/klaɪm/",
    "It took us four hours to climb the mountain.",
    "その山を登るのに4時間かかった。",
    null
  ],
  [
    "clinic",
    "B2",
    "名詞",
    [
      "診療所"
    ],
    "/ˈklɪnɪk/",
    "The new clinic provides free health checks.",
    "新しい診療所は無料の健康診断を提供する。",
    null
  ],
  [
    "clip",
    "B2",
    "名詞",
    [
      "クリップ",
      "留める物"
    ],
    "/klɪp/",
    "Use this clip to keep the papers together.",
    "書類をまとめるためにこのクリップを使ってください。",
    null
  ],
  [
    "close",
    "A2",
    "形容詞・副詞・名詞",
    [
      "を閉じる",
      "閉める"
    ],
    "/kloʊs/",
    "Please close the gate when you leave.",
    "出る時に門を閉めてください。",
    null
  ],
  [
    "closed",
    "A2",
    "形容詞",
    [
      "閉鎖された",
      "閉まった"
    ],
    "/kloʊzd/",
    "The road remained closed after the heavy snow.",
    "大雪の後、その道路は閉鎖されたままだった。",
    null
  ],
  [
    "closely",
    "B2",
    "副詞",
    [
      "精密に",
      "接近して"
    ],
    "/ˈkloʊsli/",
    "The two organizations work closely on environmental projects.",
    "その2つの団体は環境事業で緊密に協力している。",
    null
  ],
  [
    "cloth",
    "B1",
    "名詞",
    [
      "布"
    ],
    "/klɔθ/",
    "Wipe the screen gently with a soft cloth.",
    "柔らかい布で画面を優しく拭いてください。",
    null
  ],
  [
    "clothing",
    "A2",
    "名詞",
    [
      "衣類"
    ],
    "/ˈkloʊðɪŋ/",
    "Warm clothing is essential in this climate.",
    "この気候では暖かい衣類が不可欠だ。",
    null
  ],
  [
    "cloud",
    "A2",
    "名詞",
    [
      "雲",
      "に暗い影を投げかける"
    ],
    "/klaʊd/",
    "A dark cloud appeared above the mountains.",
    "山々の上に暗い雲が現れた。",
    null
  ],
  [
    "clue",
    "B1",
    "名詞",
    [
      "手がかり",
      "に手掛かりを与える"
    ],
    "/klu/",
    "The photograph provided an important clue to the mystery.",
    "その写真は謎を解く重要な手がかりとなった。",
    null
  ],
  [
    "coach",
    "A2",
    "名詞・動詞",
    [
      "コーチ",
      "走塁コーチ"
    ],
    "/koʊtʃ/",
    "The coach encouraged the players during the break.",
    "コーチは休憩中に選手たちを励ました。",
    null
  ],
  [
    "coal",
    "B1",
    "名詞",
    [
      "石炭",
      "石炭の小塊"
    ],
    "/koʊl/",
    "The country plans to reduce its dependence on coal.",
    "その国は石炭への依存を減らす予定だ。",
    null
  ],
  [
    "coast",
    "A2",
    "名詞",
    [
      "海岸",
      "海岸沿いに航行する"
    ],
    "/koʊst/",
    "We followed the coast north for nearly a week.",
    "私たちはほぼ1週間、海岸沿いを北へ進んだ。",
    null
  ],
  [
    "code",
    "A2",
    "名詞",
    [
      "コード",
      "暗証番号"
    ],
    "/koʊd/",
    "Enter the security code shown on your phone.",
    "電話に表示されたセキュリティーコードを入力してください。",
    null
  ],
  [
    "coin",
    "B1",
    "名詞",
    [
      "硬貨"
    ],
    "/kɔɪn/",
    "I found an old coin while digging in the garden.",
    "庭を掘っている時に古い硬貨を見つけた。",
    null
  ],
  [
    "coincidence",
    "B2",
    "名詞",
    [
      "偶然の一致"
    ],
    "/koʊˈɪnsɪdəns/",
    "It was a coincidence that we chose the same flight.",
    "私たちが同じ便を選んだのは偶然だった。",
    null
  ],
  [
    "collect",
    "A2",
    "動詞",
    [
      "を集める",
      "集める"
    ],
    "/kəˈlɛkt/",
    "Volunteers collect food for local families each month.",
    "ボランティアは毎月、地元の家庭のために食料を集める。",
    null
  ],
  [
    "collection",
    "B1",
    "名詞",
    [
      "収蔵物"
    ],
    "/kəˈlɛkʃən/",
    "The museum has a large collection of early photographs.",
    "その博物館には初期の写真の大規模な収蔵品がある。",
    null
  ],
  [
    "collector",
    "B2",
    "名詞",
    [
      "収集家"
    ],
    "/kəˈlɛktɚ/",
    "A private collector bought the rare painting.",
    "個人の収集家がその珍しい絵を購入した。",
    null
  ],
  [
    "colony",
    "B2",
    "名詞",
    [
      "植民地",
      "アメリカ合衆国を形成した13州のイギリス植民地"
    ],
    "/ˈkɑləni/",
    "The island was once a European colony.",
    "その島はかつてヨーロッパの植民地だった。",
    null
  ],
  [
    "coloured",
    "B1",
    "形容詞",
    [
      "色のついた、着色された"
    ],
    "/ˈkʌlɚd/",
    "The children decorated the wall with coloured paper.",
    "子どもたちは色紙で壁を飾った。",
    null
  ],
  [
    "colourful",
    "B2",
    "形容詞",
    [
      "はなやかな"
    ],
    "/ˈkʌləf(ə)l/",
    "The market is filled with colourful fruit and flowers.",
    "市場には色鮮やかな果物や花が並んでいる。",
    null
  ],
  [
    "column",
    "A2",
    "名詞",
    [
      "列",
      "円柱"
    ],
    "/ˈkɑləm/",
    "Write the total in the final column of the table.",
    "合計を表の最後の列に書いてください。",
    null
  ],
  [
    "comedy",
    "A2",
    "名詞",
    [
      "喜劇",
      "喜劇的要素"
    ],
    "/ˈkɑmədi/",
    "We watched a comedy that made everyone laugh.",
    "私たちはみんなが笑う喜劇を見た。",
    null
  ],
  [
    "comfort",
    "B2",
    "名詞・動詞",
    [
      "慰め",
      "慰めを与える人"
    ],
    "/ˈkʌmfɚt/",
    "Her kind words gave me comfort during a difficult week.",
    "つらい一週間に彼女の優しい言葉が慰めをくれた。",
    null
  ],
  [
    "comfortable",
    "A2",
    "形容詞",
    [
      "快適な",
      "十分な"
    ],
    "/ˈkʌmfɚtəbəl/",
    "These shoes are comfortable enough for a long walk.",
    "この靴は長く歩いても十分に快適だ。",
    null
  ],
  [
    "comic",
    "B2",
    "形容詞・名詞",
    [
      "滑稽な",
      "漫画"
    ],
    "/ˈkɑmɪk/",
    "The play combines a serious subject with comic moments.",
    "その劇は深刻な題材に滑稽な場面を組み合わせている。",
    null
  ],
  [
    "command",
    "B2",
    "名詞・動詞",
    [
      "命令",
      "を命令する"
    ],
    "/kəˈmænd/",
    "The officer gave a command to leave the area.",
    "その士官は区域から離れるよう命令した。",
    null
  ],
  [
    "commander",
    "B2",
    "名詞",
    [
      "指揮官…司令官"
    ],
    "/kəˈmændɚ/",
    "The commander explained the plan to the entire unit.",
    "指揮官は部隊全体に計画を説明した。",
    null
  ],
  [
    "commission",
    "B2",
    "名詞・動詞",
    [
      "委員会",
      "特別の依頼をする"
    ],
    "/kəˈmɪʃən/",
    "An independent commission will investigate the incident.",
    "独立委員会がその出来事を調査する。",
    null
  ],
  [
    "commonly",
    "B2",
    "副詞",
    [
      "一般に"
    ],
    "/ˈkɑmənli/",
    "This expression is commonly used in informal conversation.",
    "この表現はくだけた会話で一般によく使われる。",
    null
  ],
  [
    "communication",
    "B1",
    "名詞",
    [
      "意思疎通",
      "通信"
    ],
    "/kəmjunəˈkeɪʃən/",
    "Good communication prevents many workplace problems.",
    "よい意思疎通は職場の多くの問題を防ぐ。",
    null
  ],
  [
    "comparative",
    "B2",
    "形容詞",
    [
      "比較の",
      "比較による"
    ],
    "/kəmˈpɛrətɪv/",
    "The study provides comparative data from six regions.",
    "その研究は6地域の比較データを示している。",
    null
  ],
  [
    "competitor",
    "B1",
    "名詞",
    [
      "競争相手",
      "競争者"
    ],
    "/kəmˈpɛtətɚ/",
    "The company lowered its prices after a new competitor entered the market.",
    "新たな競争相手が市場に参入した後、その会社は価格を下げた。",
    null
  ],
  [
    "complain",
    "A2",
    "動詞",
    [
      "訴える"
    ],
    "/kəmpˈleɪn/",
    "Several residents complain about noise from the road.",
    "数人の住民が道路の騒音について不満を訴えている。",
    null
  ],
  [
    "completely",
    "A2",
    "副詞",
    [
      "完全に"
    ],
    "/kəmpˈlitli/",
    "The new evidence completely changed our understanding of the event.",
    "新しい証拠でその出来事に対する理解が完全に変わった。",
    null
  ],
  [
    "completion",
    "B2",
    "名詞",
    [
      "完了"
    ],
    "/kəmpˈliʃən/",
    "Payment is due upon completion of the work.",
    "支払いは作業完了時に行われる。",
    null
  ],
  [
    "composer",
    "B2",
    "名詞",
    [
      "作曲家"
    ],
    "/kəmˈpoʊzɚ/",
    "The composer wrote the music for several successful films.",
    "その作曲家はいくつかの人気映画の音楽を書いた。",
    null
  ],
  [
    "compound",
    "B2",
    "名詞",
    [
      "化合物",
      "混合物"
    ],
    "/ˈkɑmpaʊnd/",
    "Water is a compound of hydrogen and oxygen.",
    "水は水素と酸素の化合物だ。",
    null
  ],
  [
    "comprehensive",
    "B2",
    "形容詞",
    [
      "包括的な"
    ],
    "/kɑmpriˈhɛnsɪv/",
    "The website offers a comprehensive guide to local services.",
    "そのウェブサイトは地域サービスの包括的な案内を提供している。",
    null
  ],
  [
    "comprise",
    "B2",
    "動詞",
    [
      "を構成する"
    ],
    "/kəmpˈraɪz/",
    "The course will comprise twelve short online lessons.",
    "その講座は12の短いオンライン授業で構成される。",
    null
  ],
  [
    "compulsory",
    "B2",
    "形容詞",
    [
      "義務的な"
    ],
    "/kəmˈpʌlsɚi/",
    "Safety training is compulsory for all new employees.",
    "安全研修はすべての新入社員に義務付けられている。",
    null
  ],
  [
    "concentration",
    "B2",
    "名詞",
    [
      "集中"
    ],
    "/kɑnsəntˈreɪʃən/",
    "Background noise can reduce your concentration.",
    "周囲の騒音は集中力を低下させることがある。",
    null
  ],
  [
    "concerned",
    "B2",
    "形容詞",
    [
      "気づかっている",
      "心配そうな"
    ],
    "/kənˈsɝnd/",
    "Parents are concerned about the lack of safe play areas.",
    "保護者は安全な遊び場の不足を心配している。",
    null
  ],
  [
    "confess",
    "B2",
    "動詞",
    [
      "告白する",
      "自白する"
    ],
    "/kənˈfɛs/",
    "He decided to confess that he had made the mistake.",
    "彼は自分が間違えたことを告白する決心をした。",
    null
  ],
  [
    "confused",
    "B1",
    "形容詞",
    [
      "混乱した",
      "困惑した"
    ],
    "/kənfˈjuzd/",
    "I felt confused by the different sets of instructions.",
    "異なる指示がいくつもあり、私は混乱した。",
    null
  ],
  [
    "confusing",
    "B2",
    "形容詞",
    [
      "分かりにくい",
      "混乱させる"
    ],
    "/kənfˈjuzɪŋ/",
    "The ticket machine is confusing for first-time users.",
    "その券売機は初めての利用者には分かりにくい。",
    null
  ],
  [
    "confusion",
    "B2",
    "名詞",
    [
      "混乱"
    ],
    "/kənfˈjuʒən/",
    "A change in the schedule caused considerable confusion.",
    "日程変更がかなりの混乱を引き起こした。",
    null
  ],
  [
    "connected",
    "A2",
    "形容詞",
    [
      "つながった",
      "関連した"
    ],
    "/kəˈnɛktɪd/",
    "The two buildings are connected by an underground passage.",
    "その2つの建物は地下通路でつながっている。",
    null
  ],
  [
    "consequently",
    "B2",
    "副詞",
    [
      "その結果として"
    ],
    "/ˈkɑnsəkwəntli/",
    "Demand fell sharply, and consequently the factory reduced production.",
    "需要が急減し、その結果、工場は生産を減らした。",
    null
  ],
  [
    "conservation",
    "B2",
    "名詞",
    [
      "保護"
    ],
    "/kɑnsɚˈveɪʃən/",
    "The project supports the conservation of coastal wildlife.",
    "その事業は沿岸の野生生物の保護を支援する。",
    null
  ],
  [
    "considerably",
    "B2",
    "副詞",
    [
      "かなり"
    ],
    "/kənˈsɪdɚəbli/",
    "The journey is considerably shorter by train.",
    "その旅は電車ならかなり短い。",
    null
  ],
  [
    "consideration",
    "B2",
    "名詞",
    [
      "重要さ"
    ],
    "/kənsɪdɚˈeɪʃən/",
    "Cost is an important consideration when choosing a course.",
    "講座を選ぶ時、費用は重要な検討事項だ。",
    null
  ],
  [
    "consistent",
    "B2",
    "形容詞",
    [
      "一貫した"
    ],
    "/kənˈsɪstənt/",
    "The witness gave a consistent account of what happened.",
    "目撃者は起きたことについて一貫した説明をした。",
    null
  ],
  [
    "consistently",
    "B2",
    "副詞",
    [
      "一貫して"
    ],
    "/kənˈsɪstəntli/",
    "The restaurant consistently provides excellent service.",
    "そのレストランは一貫して優れたサービスを提供している。",
    null
  ],
  [
    "conspiracy",
    "B2",
    "名詞",
    [
      "陰謀",
      "陰謀団"
    ],
    "/kənsˈpɪrəsi/",
    "Police found no evidence of a conspiracy.",
    "警察は陰謀の証拠を見つけられなかった。",
    null
  ],
  [
    "consultant",
    "B2",
    "名詞",
    [
      "コンサルタント",
      "専門的助言をする人"
    ],
    "/kənˈsʌltənt/",
    "The company hired a consultant to improve its training program.",
    "会社は研修制度を改善するためコンサルタントを雇った。",
    null
  ],
  [
    "consumption",
    "B2",
    "名詞",
    [
      "消費消費高"
    ],
    "/kənˈsʌmpʃən/",
    "Household energy consumption fell during the summer.",
    "家庭のエネルギー消費量は夏の間に減少した。",
    null
  ],
  [
    "continent",
    "A2",
    "名詞",
    [
      "大陸"
    ],
    "/ˈkɑntənənt/",
    "Africa is the second-largest continent.",
    "アフリカは2番目に大きい大陸だ。",
    null
  ],
  [
    "continue",
    "A2",
    "動詞",
    [
      "を続ける",
      "続ける"
    ],
    "/kənˈtɪnju/",
    "We will continue the discussion after lunch.",
    "昼食後に話し合いを続ける。",
    null
  ],
  [
    "continuous",
    "B1",
    "形容詞",
    [
      "連続した"
    ],
    "/kənˈtɪnjuəs/",
    "The machine can operate for eight hours of continuous use.",
    "その機械は8時間連続して運転できる。",
    null
  ],
  [
    "control",
    "A2",
    "名詞・動詞",
    [
      "制御"
    ],
    "/kəntˈroʊl/",
    "Drivers must keep control of their vehicles at all times.",
    "運転者は常に車両を制御していなければならない。",
    null
  ],
  [
    "controversial",
    "B2",
    "形容詞",
    [
      "議論の",
      "議論好きの"
    ],
    "/kɑntrəˈvɝʃəl/",
    "The decision to close the library was highly controversial.",
    "図書館を閉鎖する決定は大きな議論を呼んだ。",
    null
  ],
  [
    "controversy",
    "B2",
    "名詞",
    [
      "論争"
    ],
    "/ˈkɑntrəvɝsi/",
    "The new law caused controversy across the country.",
    "新法は国中で論争を引き起こした。",
    null
  ],
  [
    "convenience",
    "B2",
    "名詞",
    [
      "便利",
      "便利なもの"
    ],
    "/kənˈvinjəns/",
    "Online booking offers convenience to busy travellers.",
    "オンライン予約は忙しい旅行者に便利さを提供する。",
    null
  ],
  [
    "convention",
    "B2",
    "名詞",
    [
      "党大会"
    ],
    "/kənˈvɛnʃən/",
    "More than a thousand delegates attended the annual convention.",
    "千人を超える代表者が年次大会に出席した。",
    null
  ],
  [
    "convey",
    "B2",
    "動詞",
    [
      "伝える",
      "運ぶ"
    ],
    "/kənˈveɪ/",
    "His expression did not convey how worried he felt.",
    "彼の表情からは、どれほど心配しているか伝わらなかった。",
    null
  ],
  [
    "convinced",
    "B2",
    "形容詞",
    [
      "確信している"
    ],
    "/kənˈvɪnst/",
    "I am convinced that the new approach will work.",
    "私は新しい方法がうまくいくと確信している。",
    null
  ],
  [
    "convincing",
    "B2",
    "形容詞",
    [
      "説得力のある"
    ],
    "/kənˈvɪnsɪŋ/",
    "She gave a convincing explanation for the unexpected result.",
    "彼女は予想外の結果について説得力のある説明をした。",
    null
  ],
  [
    "cook",
    "A2",
    "名詞",
    [
      "料理人",
      "を料理する"
    ],
    "/kʊk/",
    "My grandfather taught me how to cook this dish.",
    "祖父がこの料理の作り方を教えてくれた。",
    null
  ],
  [
    "cooker",
    "A2",
    "名詞",
    [
      "料理用電気器具"
    ],
    "/ˈkʊkɚ/",
    "Turn off the cooker before you leave the kitchen.",
    "台所を離れる前に調理器具の電源を切ってください。",
    null
  ],
  [
    "cool",
    "B1",
    "動詞",
    [
      "冷ます",
      "涼しい"
    ],
    "/kul/",
    "Allow the bread to cool before cutting it.",
    "パンは切る前に冷ましてください。",
    null
  ],
  [
    "copy",
    "A2",
    "名詞・動詞",
    [
      "こっそり写し取る"
    ],
    "/ˈkɑpi/",
    "Please keep a copy of the signed agreement.",
    "署名済みの契約書の写しを保管してください。",
    null
  ],
  [
    "corner",
    "A2",
    "名詞",
    [
      "かどにある"
    ],
    "/ˈkɔrnɚ/",
    "A small café stands on the corner of the street.",
    "通りの角に小さなカフェがある。",
    null
  ],
  [
    "corporation",
    "B2",
    "名詞",
    [
      "企業",
      "法人"
    ],
    "/kɔrpɚˈeɪʃən/",
    "The corporation employs more than ten thousand people worldwide.",
    "その企業は世界で1万人以上を雇用している。",
    null
  ],
  [
    "correctly",
    "A2",
    "副詞",
    [
      "正しく"
    ],
    "/kɚˈɛktli/",
    "Only half the students answered the question correctly.",
    "その質問に正しく答えた生徒は半数だけだった。",
    null
  ],
  [
    "costume",
    "B1",
    "名詞",
    [
      "衣装",
      "の衣装を用意する"
    ],
    "/kɑˈstum/",
    "Each dancer wore a traditional costume.",
    "踊り手はそれぞれ伝統衣装を着ていた。",
    null
  ],
  [
    "cottage",
    "B1",
    "名詞",
    [
      "小さな家"
    ],
    "/ˈkɑtədʒ/",
    "They rented a cottage in the countryside for the weekend.",
    "彼らは週末に田舎の小さな家を借りた。",
    null
  ],
  [
    "cotton",
    "B1",
    "名詞",
    [
      "綿"
    ],
    "/ˈkɑtən/",
    "This shirt is made from organic cotton.",
    "このシャツは有機栽培の綿でできている。",
    null
  ],
  [
    "counter",
    "B2",
    "名詞",
    [
      "カウンター"
    ],
    "/ˈkaʊntɚ/",
    "Please pay for your drinks at the counter.",
    "飲み物の代金はカウンターで支払ってください。",
    null
  ],
  [
    "countryside",
    "B1",
    "名詞",
    [
      "田園"
    ],
    "/ˈkʌntrisaɪd/",
    "Many people visit the countryside to escape city noise.",
    "多くの人が都会の騒音を離れて田園地帯を訪れる。",
    null
  ],
  [
    "county",
    "B2",
    "名詞",
    [
      "郡"
    ],
    "/ˈkaʊnti/",
    "The service is available throughout the county.",
    "そのサービスは郡全域で利用できる。",
    null
  ],
  [
    "couple",
    "A2",
    "名詞",
    [
      "夫婦"
    ],
    "/ˈkʌpəl/",
    "A young couple moved into the apartment upstairs.",
    "若い夫婦が上の階の部屋に引っ越してきた。",
    null
  ],
  [
    "court",
    "B1",
    "名詞",
    [
      "法廷"
    ],
    "/kɔrt/",
    "The case will return to court next month.",
    "その事件は来月再び法廷で審理される。",
    null
  ],
  [
    "cover",
    "A2",
    "名詞・動詞",
    [
      "に保険を掛ける",
      "を報道する"
    ],
    "/ˈkʌvɚ/",
    "This insurance will cover the cost of emergency treatment.",
    "この保険は緊急治療の費用を補償する。",
    null
  ],
  [
    "coverage",
    "B2",
    "名詞",
    [
      "報道",
      "報道範囲"
    ],
    "/ˈkʌvɚədʒ/",
    "The event received extensive media coverage.",
    "その出来事はメディアで広く報道された。",
    null
  ],
  [
    "covered",
    "B1",
    "形容詞",
    [
      "「…でおおわれた」の意を表す",
      "帽子をかぶった"
    ],
    "/ˈkʌvɚd/",
    "The mountain remained covered in snow until May.",
    "その山は5月まで雪に覆われたままだった。",
    null
  ],
  [
    "crack",
    "B2",
    "名詞・動詞",
    [
      "ひび",
      "にひびを入れる"
    ],
    "/kræk/",
    "A small crack appeared in the wall after the earthquake.",
    "地震後、壁に小さなひびが入った。",
    null
  ],
  [
    "craft",
    "B2",
    "名詞",
    [
      "工芸"
    ],
    "/kræft/",
    "Learning a traditional craft takes patience and practice.",
    "伝統工芸を学ぶには忍耐と練習が必要だ。",
    null
  ],
  [
    "crazy",
    "A2",
    "形容詞",
    [
      "無謀な",
      "正気でない"
    ],
    "/ˈkreɪzi/",
    "It would be crazy to drive in weather like this.",
    "こんな天候で運転するのは無謀だろう。",
    null
  ],
  [
    "cream",
    "B1",
    "形容詞",
    [
      "クリーム",
      "からクリームをとる"
    ],
    "/krim/",
    "Would you like cream in your coffee?",
    "コーヒーにクリームを入れますか。",
    null
  ],
  [
    "creation",
    "B2",
    "名詞",
    [
      "設立",
      "創造"
    ],
    "/kriˈeɪʃən/",
    "The creation of the national park protected the forest.",
    "国立公園の設立によって森林が守られた。",
    null
  ],
  [
    "creativity",
    "B2",
    "名詞",
    [
      "創造力"
    ],
    "/krieɪˈtɪvəti/",
    "The task encourages children to use their creativity.",
    "その課題は子どもたちが創造力を使うよう促す。",
    null
  ],
  [
    "creature",
    "B2",
    "名詞",
    [
      "生物"
    ],
    "/ˈkritʃɚ/",
    "Scientists discovered a tiny sea creature near the island.",
    "科学者たちは島の近くで小さな海洋生物を発見した。",
    null
  ],
  [
    "critically",
    "B2",
    "副詞",
    [
      "重篤に",
      "批判的に"
    ],
    "/ˈkrɪtɪkəli/",
    "Two passengers were critically injured in the crash.",
    "衝突事故で乗客2人が重傷を負った。",
    null
  ],
  [
    "cross",
    "A2",
    "名詞・動詞",
    [
      "渡る"
    ],
    "/krɔs/",
    "Use the pedestrian bridge to cross the busy road.",
    "交通量の多い道路を渡るには歩道橋を使ってください。",
    null
  ],
  [
    "crowd",
    "A2",
    "名詞",
    [
      "たくさん寄り集まっているもの",
      "大勢集まる"
    ],
    "/kraʊd/",
    "A large crowd gathered outside the theatre.",
    "劇場の外に大勢の人が集まった。",
    null
  ],
  [
    "crowded",
    "A2",
    "形容詞",
    [
      "混雑した"
    ],
    "/ˈkraʊdəd/",
    "The beach becomes crowded during the summer holidays.",
    "その浜辺は夏休み中に混雑する。",
    null
  ],
  [
    "cruise",
    "B2",
    "名詞・動詞",
    [
      "を巡航する",
      "を巡航速度で進ませる"
    ],
    "/kruz/",
    "They took a cruise around the islands.",
    "彼らは島々を巡るクルーズ旅行をした。",
    null
  ],
  [
    "cry",
    "A2",
    "名詞・動詞",
    [
      "泣き声"
    ],
    "/kraɪ/",
    "The child began to cry when she lost sight of her mother.",
    "母親が見えなくなると、その子は泣き始めた。",
    null
  ],
  [
    "cue",
    "B2",
    "名詞",
    [
      "合図"
    ],
    "/kju/",
    "The lights going down were our cue to begin.",
    "照明が暗くなることが私たちの開始の合図だった。",
    null
  ],
  [
    "cupboard",
    "A2",
    "名詞",
    [
      "戸棚"
    ],
    "/ˈkʌbɚd/",
    "The plates are in the cupboard above the sink.",
    "皿は流しの上の戸棚にある。",
    null
  ],
  [
    "curly",
    "A2",
    "形容詞",
    [
      "巻き毛の"
    ],
    "/ˈkɝli/",
    "The little boy has thick curly hair.",
    "その小さな男の子は太くて巻いた髪をしている。",
    null
  ],
  [
    "curtain",
    "B1",
    "名詞",
    [
      "カーテン"
    ],
    "/ˈkɝtən/",
    "She opened the curtain to let in the morning light.",
    "彼女は朝の光を入れるためカーテンを開けた。",
    null
  ],
  [
    "curve",
    "B2",
    "名詞・動詞",
    [
      "曲線"
    ],
    "/kɝv/",
    "The road follows a sharp curve beyond the village.",
    "道路は村の先で急な曲線を描いている。",
    null
  ],
  [
    "curved",
    "B2",
    "形容詞",
    [
      "湾曲した"
    ],
    "/kɝvd/",
    "The building has a distinctive curved roof.",
    "その建物には特徴的な湾曲した屋根がある。",
    null
  ],
  [
    "cut",
    "B1",
    "名詞",
    [
      "を切る"
    ],
    "/kʌt/",
    "Use a sharp knife to cut the bread evenly.",
    "よく切れるナイフでパンを均等に切ってください。",
    null
  ],
  [
    "cute",
    "B2",
    "形容詞",
    [
      "かわいい",
      "気のきいた"
    ],
    "/kjut/",
    "The child drew a cute picture of her dog.",
    "その子は自分の犬のかわいい絵を描いた。",
    null
  ],
  [
    "cycle",
    "A2",
    "名詞・動詞",
    [
      "自転車",
      "自転車に乗る"
    ],
    "/ˈsaɪkəl/",
    "More people now cycle to work in the city.",
    "今ではその都市で自転車通勤する人が増えている。",
    null
  ],
  [
    "daily",
    "A2",
    "形容詞・副詞",
    [
      "毎日の",
      "日々の"
    ],
    "/ˈdeɪli/",
    "A short daily review helps new vocabulary remain in memory.",
    "短い毎日の復習は新しい語彙を記憶に残す助けになる。",
    null
  ],
  [
    "dairy",
    "B2",
    "形容詞・名詞",
    [
      "乳製品",
      "乳製品の"
    ],
    "/ˈdɛri/",
    "The farm produces dairy products such as milk and cheese.",
    "その農場は牛乳やチーズなどの乳製品を生産している。",
    null
  ],
  [
    "danger",
    "A2",
    "名詞",
    [
      "危険",
      "危険を引き起こすもの"
    ],
    "/ˈdeɪndʒɚ/",
    "The warning sign alerts walkers to the danger of falling rocks.",
    "警告標識は落石の危険を歩行者に知らせている。",
    null
  ],
  [
    "dare",
    "B2",
    "動詞",
    [
      "思いきって…する",
      "する勇気がある"
    ],
    "/dɛr/",
    "Few people dare to swim in the river during winter.",
    "冬にその川で泳ごうとする人はほとんどいない。",
    null
  ],
  [
    "dark",
    "A2",
    "名詞",
    [
      "暗い"
    ],
    "/dɑrk/",
    "It was already dark when the hikers returned.",
    "登山者が戻った時にはすでに暗かった。",
    null
  ],
  [
    "darkness",
    "B2",
    "名詞",
    [
      "暗さ"
    ],
    "/ˈdɑrknəs/",
    "The village disappeared into darkness during the power cut.",
    "停電中、村は暗闇に包まれた。",
    null
  ],
  [
    "data",
    "A2",
    "名詞",
    [
      "データ",
      "資料"
    ],
    "/ˈdeɪtə/",
    "The research team collected data from over a thousand participants.",
    "研究チームは千人を超える参加者からデータを集めた。",
    null
  ],
  [
    "database",
    "B2",
    "名詞",
    [
      "データベース"
    ],
    "/ˈdeɪtəbeɪs/",
    "All customer records are stored in a secure database.",
    "すべての顧客記録は安全なデータベースに保存されている。",
    null
  ],
  [
    "date",
    "B2",
    "動詞",
    [
      "時代",
      "時代遅れにする"
    ],
    "/deɪt/",
    "The letter does not date from the period we expected.",
    "その手紙は私たちが予想した時代のものではない。",
    null
  ],
  [
    "dead",
    "A2",
    "形容詞",
    [
      "生命を持っていない",
      "効力を失った"
    ],
    "/dɛd/",
    "The battery was dead, so the car would not start.",
    "バッテリーが切れていたので車は動かなかった。",
    null
  ],
  [
    "deadly",
    "B2",
    "形容詞",
    [
      "命にかかわる"
    ],
    "/ˈdɛdli/",
    "The vaccine protects against a deadly disease.",
    "そのワクチンは命に関わる病気を予防する。",
    null
  ],
  [
    "deal",
    "A2",
    "名詞・動詞",
    [
      "合意",
      "取引",
      "扱う"
    ],
    "/dil/",
    "The two companies reached a deal after weeks of negotiation.",
    "2社は数週間の交渉後に合意に達した。",
    null
  ],
  [
    "dealer",
    "B2",
    "名詞",
    [
      "業者"
    ],
    "/ˈdilɚ/",
    "We bought the used car from a trusted dealer.",
    "私たちは信頼できる販売業者から中古車を買った。",
    null
  ],
  [
    "dear",
    "A2",
    "間投詞",
    [
      "〜様",
      "親愛なる"
    ],
    "/dɪr/",
    "Dear Ms Tanaka, thank you for your recent message.",
    "田中様、先日のメッセージをありがとうございました。",
    null
  ],
  [
    "death",
    "A2",
    "名詞",
    [
      "死"
    ],
    "/dɛθ/",
    "The report examines the leading causes of death.",
    "その報告書は主な死因を調べている。",
    null
  ],
  [
    "decent",
    "B2",
    "形容詞",
    [
      "まずまずの",
      "きちんとした"
    ],
    "/ˈdisənt/",
    "We found a decent hotel at a reasonable price.",
    "私たちは妥当な価格のまずまずのホテルを見つけた。",
    null
  ],
  [
    "decision",
    "A2",
    "名詞",
    [
      "決定"
    ],
    "/dɪˈsɪʒən/",
    "The committee will announce its final decision tomorrow.",
    "委員会は明日、最終決定を発表する。",
    null
  ],
  [
    "deck",
    "B2",
    "名詞",
    [
      "甲板"
    ],
    "/dɛk/",
    "Passengers gathered on the upper deck to watch the sunset.",
    "乗客は夕日を見るため上甲板に集まった。",
    null
  ],
  [
    "decoration",
    "B2",
    "名詞",
    [
      "飾りつけること",
      "飾りつけ"
    ],
    "/dɛkɚˈeɪʃən/",
    "The handmade decoration was placed above the entrance.",
    "手作りの飾りが入口の上に置かれた。",
    null
  ],
  [
    "deep",
    "A2",
    "形容詞・副詞",
    [
      "奥深くて測りしれない"
    ],
    "/dip/",
    "The lake is too deep to cross safely.",
    "その湖は深すぎて安全に渡れない。",
    null
  ],
  [
    "deeply",
    "B2",
    "副詞",
    [
      "深く"
    ],
    "/ˈdipli/",
    "The community was deeply affected by the factory closure.",
    "地域社会は工場閉鎖から深い影響を受けた。",
    null
  ],
  [
    "defence",
    "B2",
    "名詞",
    [
      "弁護",
      "防衛"
    ],
    "/dɪˈfɛns/",
    "The lawyer prepared a strong defence for her client.",
    "弁護士は依頼人のために強力な弁護を準備した。",
    null
  ],
  [
    "defender",
    "B2",
    "名詞",
    [
      "選手権保持者"
    ],
    "/dɪˈfɛndɚ/",
    "The defender blocked the final shot of the match.",
    "守備選手は試合最後のシュートを防いだ。",
    null
  ],
  [
    "definite",
    "B1",
    "形容詞",
    [
      "明確な",
      "すでに確定した"
    ],
    "/ˈdɛfənət/",
    "We need a definite answer by the end of the week.",
    "週末までに明確な返事が必要だ。",
    null
  ],
  [
    "delete",
    "B2",
    "動詞",
    [
      "を削除する"
    ],
    "/dɪˈlit/",
    "You can delete old files to free some storage space.",
    "古いファイルを削除すると保存容量を空けられる。",
    null
  ],
  [
    "deliberate",
    "B2",
    "形容詞",
    [
      "計画的な",
      "熟考する"
    ],
    "/dɪˈlɪbɚət/",
    "The change was a deliberate attempt to simplify the process.",
    "その変更は手続きを簡単にするための意図的な試みだった。",
    null
  ],
  [
    "delighted",
    "B2",
    "形容詞",
    [
      "喜んだ"
    ],
    "/dɪˈlaɪtəd/",
    "We were delighted to hear that the project had been approved.",
    "その事業が承認されたと聞いて私たちは大いに喜んだ。",
    null
  ],
  [
    "democracy",
    "B2",
    "名詞",
    [
      "民主主義",
      "民主主義国"
    ],
    "/dɪˈmɑkrəsi/",
    "Free elections are an essential part of democracy.",
    "自由な選挙は民主主義に不可欠な部分だ。",
    null
  ],
  [
    "democratic",
    "B2",
    "形容詞",
    [
      "民主的な",
      "民主主義の"
    ],
    "/dɛməˈkrætɪk/",
    "Members selected their leader through a democratic vote.",
    "会員は民主的な投票で指導者を選んだ。",
    null
  ],
  [
    "demonstration",
    "B2",
    "名詞",
    [
      "実演",
      "デモ"
    ],
    "/dɛmənstˈreɪʃən/",
    "The students watched a demonstration of the new equipment.",
    "学生たちは新しい装置の実演を見た。",
    null
  ],
  [
    "dentist",
    "A2",
    "名詞",
    [
      "歯科医"
    ],
    "/ˈdɛntəst/",
    "My dentist recommended using a softer toothbrush.",
    "歯科医はもっと柔らかい歯ブラシを使うよう勧めた。",
    null
  ],
  [
    "depart",
    "B2",
    "動詞",
    [
      "出発する"
    ],
    "/dɪˈpɑrt/",
    "The final train will depart from platform four.",
    "最終列車は4番線から出発する。",
    null
  ],
  [
    "dependent",
    "B2",
    "形容詞",
    [
      "依存している",
      "従属している"
    ],
    "/dɪˈpɛndənt/",
    "The village is heavily dependent on tourism.",
    "その村は観光に大きく依存している。",
    null
  ],
  [
    "depressing",
    "B2",
    "形容詞",
    [
      "憂うつにさせる",
      "気がめいる"
    ],
    "/dɪˈprɛsɪŋ/",
    "The report presents a depressing picture of ocean pollution.",
    "その報告書は海洋汚染の憂うつな状況を示している。",
    null
  ],
  [
    "depression",
    "B2",
    "名詞",
    [
      "うつ状態",
      "不況"
    ],
    "/dɪˈprɛʃən/",
    "She sought professional help for her depression.",
    "彼女はうつ状態について専門家の助けを求めた。",
    null
  ],
  [
    "derive",
    "B2",
    "動詞",
    [
      "由来する",
      "派生する"
    ],
    "/dɚˈaɪv/",
    "Many English words derive from Latin or Greek.",
    "多くの英単語はラテン語やギリシャ語に由来する。",
    null
  ],
  [
    "desert",
    "A2",
    "名詞・動詞",
    [
      "砂ばく"
    ],
    "/ˈdɛzɚt/",
    "The explorers crossed the desert with a local guide.",
    "探検隊は地元の案内人と砂漠を横断した。",
    null
  ],
  [
    "designer",
    "A2",
    "名詞",
    [
      "デザイナー"
    ],
    "/dɪˈzaɪnɚ/",
    "The designer created a simple but elegant logo.",
    "デザイナーは簡潔で上品なロゴを作った。",
    null
  ],
  [
    "desperately",
    "B2",
    "副詞",
    [
      "必死に"
    ],
    "/ˈdɛspɚətli/",
    "The rescue team searched desperately for the missing child.",
    "救助隊は行方不明の子どもを必死に捜した。",
    null
  ],
  [
    "destruction",
    "B2",
    "名詞",
    [
      "破滅",
      "破壊された状態"
    ],
    "/dɪˈstrʌkʃən/",
    "The world is on the brink of destruction.",
    "世界は破滅の淵に立たされている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8571368",
      "license": "CC BY 2.0 FR",
      "attribution": "#8571368 (CK) / #8571361 (small_snow)"
    }
  ],
  [
    "detailed",
    "B2",
    "形容詞",
    [
      "詳細にわたる"
    ],
    "/dɪˈteɪld/",
    "The guide gave us a detailed map of the old town.",
    "案内人は旧市街の詳しい地図をくれた。",
    null
  ],
  [
    "detective",
    "A2",
    "名詞",
    [
      "刑事",
      "刑事の"
    ],
    "/dɪˈtɛktɪv/",
    "The detective examined the room for evidence.",
    "刑事は証拠を求めて部屋を調べた。",
    null
  ],
  [
    "determination",
    "B2",
    "名詞",
    [
      "決意"
    ],
    "/dɪtɝməˈneɪʃən/",
    "Her determination helped her finish the difficult course.",
    "彼女の決意が難しい課程を修了する支えになった。",
    null
  ],
  [
    "diagram",
    "B1",
    "名詞",
    [
      "の図表を作る"
    ],
    "/ˈdaɪəgræm/",
    "This diagram shows how the parts fit together.",
    "この図は部品がどう組み合わさるかを示している。",
    null
  ],
  [
    "diamond",
    "B1",
    "名詞",
    [
      "ダイヤモンド",
      "ダイヤ"
    ],
    "/ˈdaɪmənd/",
    "The ring contains a small diamond.",
    "その指輪には小さなダイヤモンドが付いている。",
    null
  ],
  [
    "diary",
    "A2",
    "名詞",
    [
      "日記",
      "日記帳"
    ],
    "/ˈdaɪɚi/",
    "I write a few lines in my diary every night.",
    "私は毎晩、日記に数行書く。",
    null
  ],
  [
    "differently",
    "A2",
    "副詞",
    [
      "異なって",
      "違って"
    ],
    "/ˈdɪfrəntli/",
    "People may respond differently to the same medicine.",
    "同じ薬でも人によって反応が異なることがある。",
    null
  ],
  [
    "difficulty",
    "B1",
    "名詞",
    [
      "難しさ"
    ],
    "/ˈdɪfəkəlti/",
    "Please contact us if you have difficulty using the website.",
    "ウェブサイトの利用が難しい場合はご連絡ください。",
    null
  ],
  [
    "dig",
    "B2",
    "動詞",
    [
      "を掘る",
      "を掘り出す"
    ],
    "/dɪg/",
    "Workers had to dig a deep hole for the new pipe.",
    "作業員は新しい管のため深い穴を掘らなければならなかった。",
    null
  ],
  [
    "direction",
    "A2",
    "名詞",
    [
      "方向"
    ],
    "/dɚˈɛkʃən/",
    "The birds flew away in a northern direction.",
    "鳥たちは北の方向へ飛び去った。",
    null
  ],
  [
    "directly",
    "B1",
    "副詞",
    [
      "直接に"
    ],
    "/dɚˈɛktli/",
    "Please send the completed form directly to our office.",
    "記入済みの用紙を当事務所へ直接送ってください。",
    null
  ],
  [
    "director",
    "A2",
    "名詞",
    [
      "取締役"
    ],
    "/dɚˈɛktɚ/",
    "The director approved an increase in the training budget.",
    "取締役は研修予算の増額を承認した。",
    null
  ],
  [
    "dirt",
    "B1",
    "名詞",
    [
      "土"
    ],
    "/dɝt/",
    "Wash the vegetables carefully to remove any dirt.",
    "土を落とすため野菜を丁寧に洗ってください。",
    null
  ],
  [
    "disability",
    "B2",
    "名詞",
    [
      "障害",
      "精神的障害"
    ],
    "/dɪsəˈbɪlɪti/",
    "The building is accessible to people with a disability.",
    "その建物は障害のある人も利用できる。",
    null
  ],
  [
    "disabled",
    "B2",
    "形容詞",
    [
      "身体障害の不具の"
    ],
    "/dɪˈseɪbəld/",
    "The theatre reserves several seats for disabled visitors.",
    "その劇場は障害のある来場者用に数席を確保している。",
    null
  ],
  [
    "disagreement",
    "B2",
    "名詞",
    [
      "意見の相違"
    ],
    "/dɪsəˈgrimənt/",
    "A disagreement about costs delayed the project.",
    "費用についての意見の相違が事業を遅らせた。",
    null
  ],
  [
    "disappointed",
    "B1",
    "形容詞",
    [
      "失望した",
      "落胆した"
    ],
    "/dɪsəˈpɔɪntɪd/",
    "We were disappointed by the quality of the service.",
    "私たちはサービスの質に失望した。",
    null
  ],
  [
    "disappointing",
    "B1",
    "形容詞",
    [
      "失望させるような"
    ],
    "/dɪsəˈpɔɪntɪŋ/",
    "Ticket sales were disappointing despite the good reviews.",
    "よい評価にもかかわらず、券の売れ行きは期待外れだった。",
    null
  ],
  [
    "disappointment",
    "B2",
    "名詞",
    [
      "失望",
      "失望の原因となる物"
    ],
    "/dɪsəˈpɔɪntmənt/",
    "Missing the final was a major disappointment for the team.",
    "決勝を逃したことはチームにとって大きな失望だった。",
    null
  ],
  [
    "disc",
    "B2",
    "名詞",
    [
      "ディスク"
    ],
    "/dɪsk/",
    "The documentary is available on disc and online.",
    "そのドキュメンタリーはディスクとオンラインで入手できる。",
    null
  ],
  [
    "discourage",
    "B2",
    "動詞",
    [
      "思いとどまらせる",
      "に思いとどまらせる"
    ],
    "/dɪˈskɝɪdʒ/",
    "High fees may discourage students from applying.",
    "高い料金は学生の応募を思いとどまらせるかもしれない。",
    null
  ],
  [
    "discover",
    "A2",
    "動詞",
    [
      "を発見する"
    ],
    "/dɪˈskʌvɚ/",
    "Visitors can discover local history at the museum.",
    "来館者は博物館で地域の歴史を知ることができる。",
    null
  ],
  [
    "discussion",
    "A2",
    "名詞",
    [
      "議論"
    ],
    "/dɪˈskʌʃən/",
    "The proposal led to a lively discussion.",
    "その提案は活発な議論につながった。",
    null
  ],
  [
    "dishonest",
    "B2",
    "形容詞",
    [
      "不正直な",
      "不正な"
    ],
    "/dɪˈsɑnəst/",
    "It was dishonest of him to hide the extra charge.",
    "追加料金を隠した彼の行為は不正直だった。",
    null
  ],
  [
    "disk",
    "B2",
    "名詞",
    [
      "ディスク",
      "円盤"
    ],
    "/dɪsk/",
    "Save a backup copy on an external disk.",
    "外付けディスクに予備のコピーを保存してください。",
    null
  ],
  [
    "dislike",
    "B1",
    "名詞・動詞",
    [
      "を嫌う"
    ],
    "/dɪˈslaɪk/",
    "Many people dislike being interrupted while working.",
    "多くの人は仕事中に邪魔されるのを嫌う。",
    null
  ],
  [
    "disorder",
    "B2",
    "名詞",
    [
      "障害"
    ],
    "/dɪˈsɔrdɚ/",
    "The treatment helps people with a sleep disorder.",
    "その治療は睡眠障害のある人を助ける。",
    null
  ],
  [
    "distinct",
    "B2",
    "形容詞",
    [
      "はっきりした",
      "特異な"
    ],
    "/dɪˈstɪŋkt/",
    "The region has four distinct seasons.",
    "その地域にははっきり異なる四季がある。",
    null
  ],
  [
    "distribution",
    "B2",
    "名詞",
    [
      "配布"
    ],
    "/dɪstrəbˈjuʃən/",
    "The charity manages the distribution of food supplies.",
    "その慈善団体は食料の配布を管理している。",
    null
  ],
  [
    "dive",
    "B2",
    "名詞・動詞",
    [
      "飛び込む",
      "頭から飛び込む"
    ],
    "/daɪv/",
    "We watched a seabird dive into the water.",
    "私たちは海鳥が水へ飛び込むのを見た。",
    null
  ],
  [
    "diverse",
    "B2",
    "形容詞",
    [
      "多様の"
    ],
    "/daɪˈvɝs/",
    "The city has a diverse population.",
    "その都市には多様な人々が暮らしている。",
    null
  ],
  [
    "diversity",
    "B2",
    "名詞",
    [
      "多様性"
    ],
    "/dɪˈvɝsɪti/",
    "Cultural diversity can bring new ideas to a workplace.",
    "文化的多様性は職場に新しい考えをもたらしうる。",
    null
  ],
  [
    "divorce",
    "B2",
    "名詞・動詞",
    [
      "離婚",
      "と離婚する"
    ],
    "/dɪˈvɔrs/",
    "The couple decided to divorce after years of conflict.",
    "その夫婦は長年の対立の末に離婚を決めた。",
    null
  ],
  [
    "divorced",
    "A2",
    "形容詞",
    [
      "離婚した"
    ],
    "/dɪˈvɔrst/",
    "He remained friendly with his divorced partner.",
    "彼は離婚した元配偶者と友好的な関係を保った。",
    null
  ],
  [
    "documentary",
    "B1",
    "名詞",
    [
      "ドキュメンタリー"
    ],
    "/dɑkjəˈmɛntɚi/",
    "The documentary explores life in the deep ocean.",
    "そのドキュメンタリーは深海の生物を取り上げている。",
    null
  ],
  [
    "dominant",
    "B2",
    "形容詞",
    [
      "支配的な"
    ],
    "/ˈdɑmənənt/",
    "Online sales have become the dominant part of the business.",
    "オンライン販売が事業の中心的な部分になった。",
    null
  ],
  [
    "donation",
    "B2",
    "名詞",
    [
      "寄付",
      "寄付金"
    ],
    "/doʊˈneɪʃən/",
    "A generous donation allowed the library to buy new books.",
    "多額の寄付で図書館は新しい本を購入できた。",
    null
  ],
  [
    "dot",
    "B2",
    "名詞",
    [
      "点",
      "に点を打つ"
    ],
    "/dɑt/",
    "Mark each city with a red dot on the map.",
    "地図上の各都市に赤い点を付けてください。",
    null
  ],
  [
    "download",
    "A2",
    "名詞・動詞",
    [
      "ダウンロードする",
      "ダウンロードしたファイル"
    ],
    "/ˈdaʊnloʊd/",
    "You can download the full report for free.",
    "報告書全体を無料でダウンロードできる。",
    null
  ],
  [
    "downstairs",
    "A2",
    "形容詞",
    [
      "階下の",
      "階下"
    ],
    "/ˈdaʊnsˈtɛrz/",
    "The meeting room is downstairs beside the entrance.",
    "会議室は階下の入口脇にある。",
    null
  ],
  [
    "downtown",
    "B2",
    "形容詞・副詞・名詞",
    [
      "町の中心街へ",
      "町の中心街の"
    ],
    "/ˈdaʊnˈtaʊn/",
    "A new public park opened downtown last month.",
    "先月、中心街に新しい公園が開園した。",
    null
  ],
  [
    "downwards",
    "B2",
    "副詞",
    [
      "下向きに"
    ],
    "/ˈdaʊnwɚdz/",
    "The path slopes downwards towards the river.",
    "小道は川に向かって下り坂になっている。",
    null
  ],
  [
    "dozen",
    "B2",
    "限定詞・名詞",
    [
      "ダース"
    ],
    "/ˈdʌzən/",
    "We ordered a dozen chairs for the new office.",
    "新しい事務所用に椅子を12脚注文した。",
    null
  ],
  [
    "draft",
    "B2",
    "名詞・動詞",
    [
      "草稿"
    ],
    "/dræft/",
    "Please send me the first draft by Wednesday.",
    "水曜日までに最初の草稿を送ってください。",
    null
  ],
  [
    "drama",
    "A2",
    "名詞",
    [
      "劇"
    ],
    "/ˈdrɑmə/",
    "The school drama deals with the pressure of exams.",
    "その学校劇は試験の重圧を扱っている。",
    null
  ],
  [
    "dramatically",
    "B2",
    "副詞",
    [
      "劇的に",
      "非常に効果的に"
    ],
    "/drəˈmætɪkli/",
    "Housing costs have risen dramatically in recent years.",
    "住宅費は近年劇的に上昇した。",
    null
  ],
  [
    "drawing",
    "A2",
    "名詞",
    [
      "図面",
      "絵"
    ],
    "/ˈdrɔɪŋ/",
    "The architect showed us a drawing of the new entrance.",
    "建築家は新しい入口の図面を見せてくれた。",
    null
  ],
  [
    "dream",
    "A2",
    "名詞・動詞",
    [
      "夢"
    ],
    "/drim/",
    "Her dream is to open a small restaurant.",
    "彼女の夢は小さなレストランを開くことだ。",
    null
  ],
  [
    "dressed",
    "B1",
    "形容詞",
    [
      "正装した",
      "服を着た"
    ],
    "/drɛst/",
    "Everyone was dressed in formal clothes for the ceremony.",
    "式典では全員が正装していた。",
    null
  ],
  [
    "drive",
    "A2",
    "名詞",
    [
      "を車で運ぶ",
      "車で行く"
    ],
    "/draɪv/",
    "It takes about an hour to drive to the coast.",
    "海岸まで車で約1時間かかる。",
    null
  ],
  [
    "driving",
    "A2",
    "名詞",
    [
      "運転の"
    ],
    "/ˈdraɪvɪŋ/",
    "Driving in heavy snow requires extra care.",
    "大雪の中での運転には特別な注意が必要だ。",
    null
  ],
  [
    "drug",
    "A2",
    "名詞",
    [
      "薬"
    ],
    "/drʌg/",
    "The new drug reduced the patient's pain.",
    "新薬は患者の痛みを和らげた。",
    null
  ],
  [
    "drum",
    "B1",
    "名詞",
    [
      "太鼓の音",
      "太鼓"
    ],
    "/drʌm/",
    "A steady drum kept the dancers in time.",
    "一定の太鼓の音が踊り手のリズムを保った。",
    null
  ],
  [
    "drunk",
    "B1",
    "形容詞",
    [
      "酔った",
      "drinkの過去分詞"
    ],
    "/drʌŋk/",
    "The police stopped a drunk driver near the bridge.",
    "警察は橋の近くで飲酒運転者を止めた。",
    null
  ],
  [
    "dry",
    "A2",
    "形容詞・動詞",
    [
      "を乾かす"
    ],
    "/draɪ/",
    "Leave the paint to dry overnight.",
    "塗料を一晩乾かしてください。",
    null
  ],
  [
    "duration",
    "B2",
    "名詞",
    [
      "存続期間"
    ],
    "/ˈdʊˈreɪʃən/",
    "The exact duration of the course depends on your level.",
    "講座の正確な期間はレベルによって異なる。",
    null
  ],
  [
    "dust",
    "B1",
    "名詞",
    [
      "ほこり",
      "ほこりを払う"
    ],
    "/dʌst/",
    "A layer of dust covered the unused desk.",
    "使われていない机はほこりに覆われていた。",
    null
  ],
  [
    "dynamic",
    "B2",
    "形容詞",
    [
      "活力のある"
    ],
    "/daɪˈnæmɪk/",
    "She is a dynamic leader who welcomes new ideas.",
    "彼女は新しい考えを歓迎する活力ある指導者だ。",
    null
  ],
  [
    "earth",
    "A2",
    "名詞",
    [
      "地球",
      "地"
    ],
    "/ɝθ/",
    "The satellite sends images of Earth back to scientists.",
    "その衛星は地球の画像を科学者へ送る。",
    null
  ],
  [
    "easily",
    "A2",
    "副詞",
    [
      "容易に"
    ],
    "/ˈizəli/",
    "The instructions can be easily understood by beginners.",
    "その説明は初心者にも簡単に理解できる。",
    null
  ],
  [
    "eastern",
    "B1",
    "形容詞",
    [
      "東部地方の"
    ],
    "/ˈistɚn/",
    "Heavy rain is expected in the eastern region.",
    "東部地域では大雨が予想されている。",
    null
  ],
  [
    "economics",
    "B2",
    "名詞",
    [
      "経済学",
      "経済状態"
    ],
    "/ɛkəˈnɑmɪks/",
    "He studied economics before working for a bank.",
    "彼は銀行で働く前に経済学を学んだ。",
    null
  ],
  [
    "economist",
    "B2",
    "名詞",
    [
      "経済学者"
    ],
    "/ɪˈkɑnəmɪst/",
    "The economist warned that prices might continue to rise.",
    "経済学者は物価が上がり続ける可能性を警告した。",
    null
  ],
  [
    "editor",
    "B1",
    "名詞",
    [
      "編集者",
      "編集長"
    ],
    "/ˈɛdətɚ/",
    "The editor asked the writer to shorten the article.",
    "編集者は書き手に記事を短くするよう求めた。",
    null
  ],
  [
    "editorial",
    "B2",
    "形容詞",
    [
      "社説",
      "社説の"
    ],
    "/ɛdəˈtɔriəl/",
    "The newspaper published an editorial on climate policy.",
    "その新聞は気候政策についての社説を掲載した。",
    null
  ],
  [
    "educated",
    "B1",
    "形容詞",
    [
      "教育のある"
    ],
    "/ˈɛdʒəkeɪtɪd/",
    "She is an educated reader with a wide range of interests.",
    "彼女は幅広い関心を持つ教養ある読者だ。",
    null
  ],
  [
    "education",
    "A2",
    "名詞",
    [
      "教育",
      "教育学"
    ],
    "/ɛdʒəˈkeɪʃən/",
    "Every child should have access to quality education.",
    "すべての子どもが質の高い教育を受けられるべきだ。",
    null
  ],
  [
    "educational",
    "B1",
    "形容詞",
    [
      "教育の",
      "教育に関する"
    ],
    "/ɛdʒəˈkeɪʃənəl/",
    "The museum offers educational programs for schools.",
    "その博物館は学校向けの教育プログラムを提供している。",
    null
  ],
  [
    "effect",
    "A2",
    "名詞",
    [
      "効果"
    ],
    "/ɪˈfɛkt/",
    "The new timetable had little effect on delays.",
    "新しい時刻表は遅延にほとんど効果がなかった。",
    null
  ],
  [
    "effectively",
    "B1",
    "副詞",
    [
      "効果的に"
    ],
    "/ɪˈfɛktɪvli/",
    "The two departments now work together more effectively.",
    "2つの部署は今ではより効果的に協力している。",
    null
  ],
  [
    "efficiently",
    "B2",
    "副詞",
    [
      "効率よく"
    ],
    "/ɪˈfɪʃəntli/",
    "The new system processes orders more efficiently.",
    "新しいシステムは注文をより効率よく処理する。",
    null
  ],
  [
    "either",
    "A2",
    "副詞・限定詞・名詞",
    [
      "どちらの…も",
      "どちらかの"
    ],
    "/ˈiðɚ/",
    "You can choose either option without paying extra.",
    "追加料金なしでどちらの選択肢も選べる。",
    null
  ],
  [
    "elbow",
    "B2",
    "名詞",
    [
      "ひじ"
    ],
    "/ˈɛlboʊ/",
    "He hurt his elbow when he fell from the bicycle.",
    "彼は自転車から転んで肘を痛めた。",
    null
  ],
  [
    "electric",
    "A2",
    "形容詞",
    [
      "電気の",
      "電気が引き起こす"
    ],
    "/ɪˈlɛktrɪk/",
    "The city plans to replace its buses with electric vehicles.",
    "市はバスを電気自動車に替える予定だ。",
    null
  ],
  [
    "electrical",
    "A2",
    "形容詞",
    [
      "電気と関係のある",
      "電気を扱う"
    ],
    "/ɪˈlɛktrɪkəl/",
    "Only trained staff should repair electrical equipment.",
    "訓練を受けた職員だけが電気機器を修理すべきだ。",
    null
  ],
  [
    "electricity",
    "A2",
    "名詞",
    [
      "電気",
      "電力"
    ],
    "/ɪlɛktˈrɪsəti/",
    "The storm left thousands of homes without electricity.",
    "嵐で何千もの家庭が停電した。",
    null
  ],
  [
    "electronics",
    "B2",
    "名詞",
    [
      "電子機器",
      "電子工学"
    ],
    "/ɪlɛktˈrɑnɪks/",
    "He works in a shop that sells consumer electronics.",
    "彼は家電製品を売る店で働いている。",
    null
  ],
  [
    "elegant",
    "B2",
    "形容詞",
    [
      "上品な"
    ],
    "/ˈɛləgənt/",
    "The hotel combines an elegant design with modern comfort.",
    "そのホテルは上品なデザインと現代的な快適さを兼ね備えている。",
    null
  ],
  [
    "elementary",
    "B2",
    "形容詞",
    [
      "初歩の"
    ],
    "/ɛləˈmɛntri/",
    "The first chapter provides an elementary introduction to coding.",
    "第1章ではプログラミングの初歩を紹介している。",
    null
  ],
  [
    "elsewhere",
    "B2",
    "副詞",
    [
      "ほかの所で"
    ],
    "/ˈɛlswɛr/",
    "If this shop is closed, we can eat elsewhere.",
    "この店が閉まっていたら別の場所で食べられる。",
    null
  ],
  [
    "embrace",
    "B2",
    "動詞",
    [
      "を取り巻く"
    ],
    "/ɛmbˈreɪs/",
    "The organization chose to embrace digital technology.",
    "その団体はデジタル技術を積極的に取り入れることにした。",
    null
  ],
  [
    "emission",
    "B2",
    "名詞",
    [
      "排出",
      "排出物"
    ],
    "/ɪˈmɪʃən/",
    "Each vehicle must meet the new emission standard.",
    "各車両は新しい排出基準を満たさなければならない。",
    null
  ],
  [
    "emotionally",
    "B2",
    "副詞",
    [
      "感情的に",
      "情緒的に"
    ],
    "/ɪˈmoʊʃnəli/",
    "Caring for a sick relative can be emotionally difficult.",
    "病気の親族を世話することは精神的につらい場合がある。",
    null
  ],
  [
    "empire",
    "B2",
    "名詞",
    [
      "帝国"
    ],
    "/ˈɛmpaɪɚ/",
    "The museum describes the rise and fall of the ancient empire.",
    "博物館は古代帝国の盛衰を説明している。",
    null
  ],
  [
    "empty",
    "A2",
    "形容詞・動詞",
    [
      "空の"
    ],
    "/ˈɛmpti/",
    "The restaurant was almost empty when we arrived.",
    "私たちが着いた時、レストランはほとんど空だった。",
    null
  ],
  [
    "ending",
    "A2",
    "名詞",
    [
      "結末"
    ],
    "/ˈɛndɪŋ/",
    "The film has a surprising but satisfying ending.",
    "その映画には驚きがありながら満足できる結末がある。",
    null
  ],
  [
    "energy",
    "A2",
    "名詞",
    [
      "元気"
    ],
    "/ˈɛnɚdʒi/",
    "Walking to work gives me more energy in the morning.",
    "歩いて通勤すると朝にもっと元気が出る。",
    null
  ],
  [
    "engaged",
    "B1",
    "形容詞",
    [
      "取り組んでいる",
      "婚約した"
    ],
    "/ɛnˈgeɪdʒd/",
    "She is fully engaged in planning the conference.",
    "彼女は会議の計画に全面的に取り組んでいる。",
    null
  ],
  [
    "engineer",
    "A2",
    "名詞",
    [
      "技師"
    ],
    "/ˈɛndʒəˈnɪr/",
    "An engineer inspected the bridge after the storm.",
    "技師が嵐の後に橋を点検した。",
    null
  ],
  [
    "engineering",
    "B1",
    "名詞",
    [
      "工学"
    ],
    "/ˈɛndʒəˈnɪrɪŋ/",
    "The university is known for research in environmental engineering.",
    "その大学は環境工学の研究で知られている。",
    null
  ],
  [
    "enhance",
    "B2",
    "動詞",
    [
      "高める",
      "良くする"
    ],
    "/ɛnˈhæns/",
    "Plants can enhance the appearance of an office.",
    "植物は職場の見た目を良くすることができる。",
    null
  ],
  [
    "enjoyable",
    "B2",
    "形容詞",
    [
      "楽しめる"
    ],
    "/ɛnˈdʒɔɪəbəl/",
    "The guide made the long journey enjoyable.",
    "案内人のおかげで長い旅が楽しいものになった。",
    null
  ],
  [
    "enquiry",
    "B2",
    "名詞",
    [
      "問い合わせ"
    ],
    "/ɪnkˈwaɪri/",
    "We received your enquiry about course fees.",
    "受講料についてのお問い合わせを受け取りました。",
    null
  ],
  [
    "enter",
    "A2",
    "動詞",
    [
      "に入る"
    ],
    "/ˈɛntɚ/",
    "Visitors must enter through the main gate.",
    "訪問者は正門から入らなければならない。",
    null
  ],
  [
    "entertain",
    "B1",
    "動詞",
    [
      "を楽しませる",
      "客を呼ぶ"
    ],
    "/ɛntɚˈteɪn/",
    "Street musicians entertain visitors in the square.",
    "大道芸人が広場で観光客を楽しませる。",
    null
  ],
  [
    "entertaining",
    "B2",
    "形容詞",
    [
      "面白い",
      "楽しませる"
    ],
    "/ɛntɚˈteɪnɪŋ/",
    "The speaker gave an entertaining account of her travels.",
    "講演者は旅行について面白く語った。",
    null
  ],
  [
    "entertainment",
    "B1",
    "名詞",
    [
      "娯楽"
    ],
    "/ɛntɚˈteɪnmənt/",
    "The festival provides free entertainment for families.",
    "その祭りは家族向けの無料の娯楽を提供する。",
    null
  ],
  [
    "entrepreneur",
    "B2",
    "名詞",
    [
      "企業家"
    ],
    "/ɑntrəprəˈnɝ/",
    "The young entrepreneur built a successful online business.",
    "その若い起業家は成功するオンライン事業を築いた。",
    null
  ],
  [
    "envelope",
    "B2",
    "名詞",
    [
      "封筒"
    ],
    "/ˈɛnvəloʊp/",
    "Place the form in the envelope provided.",
    "用紙を備え付けの封筒に入れてください。",
    null
  ],
  [
    "episode",
    "B1",
    "名詞",
    [
      "番組の回",
      "エピソード"
    ],
    "/ˈɛpəsoʊd/",
    "The latest episode attracted more than a million viewers.",
    "最新回は100万人を超える視聴者を集めた。",
    null
  ],
  [
    "equally",
    "B1",
    "副詞",
    [
      "均等に",
      "平等に"
    ],
    "/ˈikwəli/",
    "The prize money will be divided equally among the winners.",
    "賞金は受賞者の間で均等に分けられる。",
    null
  ],
  [
    "equip",
    "B2",
    "動詞",
    [
      "備えさせる"
    ],
    "/ɪkˈwɪp/",
    "The grant will equip the laboratory with modern tools.",
    "その助成金で研究室に最新の器具を備えられる。",
    null
  ],
  [
    "era",
    "B2",
    "名詞",
    [
      "時代",
      "代"
    ],
    "/ˈɛrə/",
    "Smartphones changed communication in the digital era.",
    "スマートフォンはデジタル時代の意思疎通を変えた。",
    null
  ],
  [
    "erupt",
    "B2",
    "動詞",
    [
      "噴火する",
      "噴出する"
    ],
    "/ɪˈrʌpt/",
    "The volcano could erupt again without warning.",
    "その火山は予告なく再び噴火する可能性がある。",
    null
  ],
  [
    "especially",
    "A2",
    "副詞",
    [
      "特に"
    ],
    "/əˈspɛʃli/",
    "The path is beautiful, especially in autumn.",
    "その小道は特に秋に美しい。",
    null
  ],
  [
    "essentially",
    "B2",
    "副詞",
    [
      "本質的に",
      "必然的には"
    ],
    "/ɛˈsɛnʃəli/",
    "The two methods are essentially the same.",
    "その2つの方法は本質的に同じだ。",
    null
  ],
  [
    "estate",
    "B2",
    "名詞",
    [
      "土地",
      "不動産"
    ],
    "/ɪˈsteɪt/",
    "The family owns a large estate outside the city.",
    "その家族は市外に広大な土地を所有している。",
    null
  ],
  [
    "ethic",
    "B2",
    "名詞",
    [
      "倫理"
    ],
    "/ˈɛθɪk/",
    "A strong work ethic helped her earn the team's trust.",
    "強い職業倫理が彼女のチームからの信頼につながった。",
    null
  ],
  [
    "ethnic",
    "B2",
    "形容詞",
    [
      "民族の"
    ],
    "/ˈɛθnɪk/",
    "The area is home to several ethnic communities.",
    "その地域には複数の民族共同体が暮らしている。",
    null
  ],
  [
    "evaluation",
    "B2",
    "名詞",
    [
      "評価"
    ],
    "/ɪvæljuˈeɪʃən/",
    "The program will continue after a positive evaluation.",
    "その制度はよい評価を受けた後も継続する。",
    null
  ],
  [
    "even",
    "B2",
    "形容詞",
    [
      "平らな"
    ],
    "/ˈivɪn/",
    "Make sure the surface is clean and even.",
    "表面が清潔で平らか確認してください。",
    null
  ],
  [
    "everyday",
    "A2",
    "形容詞",
    [
      "日常の"
    ],
    "/ˈɛvriˈdeɪ/",
    "The book explains science through everyday examples.",
    "その本は日常的な例を通して科学を説明する。",
    null
  ],
  [
    "everywhere",
    "A2",
    "副詞",
    [
      "至る所に"
    ],
    "/ˈɛvriwɛr/",
    "Spring flowers were growing everywhere.",
    "春の花が至る所に咲いていた。",
    null
  ],
  [
    "evolution",
    "B2",
    "名詞",
    [
      "発展"
    ],
    "/ɛvəˈluʃən/",
    "The exhibition traces the evolution of modern design.",
    "その展示は現代デザインの発展をたどっている。",
    null
  ],
  [
    "exactly",
    "A2",
    "副詞",
    [
      "ちょうど"
    ],
    "/ɪgˈzæktli/",
    "The train arrived at exactly nine o'clock.",
    "電車はちょうど9時に到着した。",
    null
  ],
  [
    "examination",
    "B2",
    "名詞",
    [
      "検査",
      "試験"
    ],
    "/ɪgzæməˈneɪʃən/",
    "A careful examination revealed a small crack.",
    "詳しい検査で小さなひびが見つかった。",
    null
  ],
  [
    "except",
    "A2",
    "接続詞・前置詞",
    [
      "を除いて",
      "を除く"
    ],
    "/ɪkˈsɛpt/",
    "The museum is open every day except Monday.",
    "その博物館は月曜日を除いて毎日開いている。",
    null
  ],
  [
    "excessive",
    "B2",
    "形容詞",
    [
      "過度の"
    ],
    "/ɪkˈsɛsɪv/",
    "Excessive screen time can affect sleep.",
    "過度な画面使用は睡眠に影響することがある。",
    null
  ],
  [
    "excitement",
    "B1",
    "名詞",
    [
      "興奮",
      "興奮させるもの"
    ],
    "/ɪkˈsaɪtmənt/",
    "There was great excitement before the final match.",
    "決勝戦の前には大きな興奮があった。",
    null
  ],
  [
    "exclude",
    "B2",
    "動詞",
    [
      "を除外する",
      "を全く許さない"
    ],
    "/ɪkskˈlud/",
    "The price does not exclude any necessary materials.",
    "その価格は必要な教材を除外していない。",
    null
  ],
  [
    "excuse",
    "B2",
    "名詞・動詞",
    [
      "言い訳",
      "の言い訳をする"
    ],
    "/ɪkskˈjus/",
    "There is no excuse for treating customers rudely.",
    "客に失礼な態度を取る言い訳はない。",
    null
  ],
  [
    "executive",
    "B2",
    "形容詞・名詞",
    [
      "役員",
      "経営幹部"
    ],
    "/ɪgˈzɛkjətɪv/",
    "A senior executive presented the company's strategy.",
    "上級役員が会社の戦略を発表した。",
    null
  ],
  [
    "exit",
    "B2",
    "名詞",
    [
      "出口"
    ],
    "/ˈɛgzɪt/",
    "Use the rear exit in an emergency.",
    "緊急時には後方出口を使ってください。",
    null
  ],
  [
    "exotic",
    "B2",
    "形容詞",
    [
      "珍しい",
      "異国風の"
    ],
    "/ɪgˈzɑtɪk/",
    "The garden contains exotic plants from tropical regions.",
    "その庭には熱帯地域の珍しい植物がある。",
    null
  ],
  [
    "expansion",
    "B2",
    "名詞",
    [
      "拡張"
    ],
    "/ɪksˈpænʃən/",
    "The airport expansion will create new jobs.",
    "空港の拡張は新しい雇用を生むだろう。",
    null
  ],
  [
    "expect",
    "A2",
    "動詞",
    [
      "予想する"
    ],
    "/ɪksˈpɛkt/",
    "We expect demand to increase next year.",
    "私たちは来年需要が増えると予想している。",
    null
  ],
  [
    "expected",
    "B1",
    "形容詞",
    [
      "予想された"
    ],
    "/ɪksˈpɛktəd/",
    "The repairs took longer than expected.",
    "修理は予想より長くかかった。",
    null
  ],
  [
    "expedition",
    "B1",
    "名詞",
    [
      "探検隊",
      "探検"
    ],
    "/ɛkspəˈdɪʃən/",
    "The scientific expedition spent two months in Antarctica.",
    "科学探検隊は南極で2か月を過ごした。",
    null
  ],
  [
    "experience",
    "A2",
    "名詞・動詞",
    [
      "経験",
      "経験したこと"
    ],
    "/ɪksˈpɪriəns/",
    "Working abroad gave her valuable experience.",
    "海外で働いたことで彼女は貴重な経験を得た。",
    null
  ],
  [
    "experienced",
    "B1",
    "形容詞",
    [
      "経験を積んだ"
    ],
    "/ɪksˈpɪriənst/",
    "An experienced guide led us through the forest.",
    "経験豊富な案内人が森を案内してくれた。",
    null
  ],
  [
    "expertise",
    "B2",
    "名詞",
    [
      "専門技術",
      "専門家の調査報告"
    ],
    "/ɛkspɚˈtiz/",
    "The project requires expertise in data security.",
    "その事業にはデータ安全管理の専門知識が必要だ。",
    null
  ],
  [
    "exploit",
    "B2",
    "動詞",
    [
      "搾取する",
      "を開発する"
    ],
    "/ˈɛksplɔɪt/",
    "Some employers exploit workers who do not know their rights.",
    "雇用主の中には権利を知らない労働者を搾取する者がいる。",
    null
  ],
  [
    "exploration",
    "B2",
    "名詞",
    [
      "探査",
      "探検"
    ],
    "/ɛksplɚˈeɪʃən/",
    "Space exploration has produced useful new technology.",
    "宇宙探査は有用な新技術を生み出してきた。",
    null
  ],
  [
    "exposure",
    "B2",
    "名詞",
    [
      "さらされること",
      "さらすこと"
    ],
    "/ɪksˈpoʊʒɚ/",
    "Long exposure to loud noise may damage hearing.",
    "大きな音に長時間さらされると聴力を損なうことがある。",
    null
  ],
  [
    "extension",
    "B2",
    "名詞",
    [
      "延長",
      "内線"
    ],
    "/ɪksˈtɛnʃən/",
    "We requested an extension of the application deadline.",
    "私たちは応募期限の延長を求めた。",
    null
  ],
  [
    "extensive",
    "B2",
    "形容詞",
    [
      "広範囲にわたる"
    ],
    "/ɪksˈtɛnsɪv/",
    "The storm caused extensive damage along the coast.",
    "嵐は沿岸に広範な被害をもたらした。",
    null
  ],
  [
    "extensively",
    "B2",
    "副詞",
    [
      "幅広く"
    ],
    "/ɪksˈtɛnsɪvli/",
    "The topic has been extensively discussed in the media.",
    "その話題はメディアで広く議論されてきた。",
    null
  ],
  [
    "extra",
    "B1",
    "副詞・名詞",
    [
      "割増し料金"
    ],
    "/ˈɛkstrə/",
    "You can pay extra for a larger room.",
    "追加料金を払えばより広い部屋にできる。",
    null
  ],
  [
    "extract",
    "B2",
    "名詞",
    [
      "抽出する"
    ],
    "/ˈɛkstrækt/",
    "The process can extract useful chemicals from waste.",
    "その工程では廃棄物から有用な化学物質を抽出できる。",
    null
  ],
  [
    "fabric",
    "B2",
    "名詞",
    [
      "織物"
    ],
    "/ˈfæbrɪk/",
    "This fabric is light but very strong.",
    "この布地は軽いが非常に丈夫だ。",
    null
  ],
  [
    "fabulous",
    "B2",
    "形容詞",
    [
      "すばらしい"
    ],
    "/ˈfæbjələs/",
    "We had a fabulous view of the coast from our room.",
    "部屋から海岸のすばらしい景色が見えた。",
    null
  ],
  [
    "face",
    "B1",
    "動詞",
    [
      "に直面する",
      "面する"
    ],
    "/feɪs/",
    "Small businesses face serious challenges during a recession.",
    "不況時には小企業が深刻な課題に直面する。",
    null
  ],
  [
    "factory",
    "A2",
    "名詞",
    [
      "工場"
    ],
    "/ˈfæktɚi/",
    "The factory produces parts for electric cars.",
    "その工場は電気自動車の部品を生産している。",
    null
  ],
  [
    "failed",
    "B2",
    "形容詞",
    [
      "失敗した"
    ],
    "/feɪld/",
    "The failed experiment still provided useful information.",
    "失敗した実験からも有用な情報が得られた。",
    null
  ],
  [
    "fair",
    "A2",
    "形容詞",
    [
      "適正なルールに従ったフェアな",
      "はっきりした"
    ],
    "/fɛr/",
    "The judges made a fair decision based on the evidence.",
    "審査員は証拠に基づいて公正な判断をした。",
    null
  ],
  [
    "fairly",
    "B1",
    "副詞",
    [
      "公平に"
    ],
    "/ˈfɛrli/",
    "The manager promised to treat every employee fairly.",
    "管理者は全従業員を公平に扱うと約束した。",
    null
  ],
  [
    "fall",
    "A2",
    "名詞",
    [
      "垂れ下がる",
      "下がる"
    ],
    "/fɔl/",
    "House prices began to fall in the second half of the year.",
    "住宅価格は年の後半に下がり始めた。",
    null
  ],
  [
    "fame",
    "B2",
    "名詞",
    [
      "名声"
    ],
    "/feɪm/",
    "The singer found fame after appearing on television.",
    "その歌手はテレビ出演後に名声を得た。",
    null
  ],
  [
    "fan",
    "A2",
    "名詞",
    [
      "扇風機",
      "扇"
    ],
    "/fæn/",
    "A large fan keeps the room cool.",
    "大きな扇風機が部屋を涼しく保つ。",
    null
  ],
  [
    "fantasy",
    "B2",
    "名詞",
    [
      "空想",
      "空想的作品"
    ],
    "/ˈfæntəsi/",
    "The novel mixes historical fact with fantasy.",
    "その小説は歴史的事実と空想を組み合わせている。",
    null
  ],
  [
    "far",
    "B1",
    "形容詞",
    [
      "遠くに",
      "遠くへ"
    ],
    "/fɑr/",
    "The nearest hospital is not far from here.",
    "最寄りの病院はここから遠くない。",
    null
  ],
  [
    "fare",
    "B2",
    "名詞",
    [
      "運賃"
    ],
    "/fɛr/",
    "The bus fare has increased by ten percent.",
    "バス運賃が10パーセント上がった。",
    null
  ],
  [
    "farm",
    "A2",
    "動詞",
    [
      "栽培する",
      "農業を営む"
    ],
    "/fɑrm/",
    "They farm vegetables without using chemical pesticides.",
    "彼らは化学農薬を使わずに野菜を栽培している。",
    null
  ],
  [
    "farming",
    "A2",
    "名詞",
    [
      "農業"
    ],
    "/ˈfɑrmɪŋ/",
    "Organic farming is becoming more common in the region.",
    "その地域では有機農業がより一般的になっている。",
    null
  ],
  [
    "fashion",
    "A2",
    "名詞",
    [
      "流行",
      "を細工して作る"
    ],
    "/ˈfæʃən/",
    "Loose jackets are back in fashion this year.",
    "今年はゆったりした上着が再び流行している。",
    null
  ],
  [
    "fat",
    "A2",
    "名詞",
    [
      "脂肪分",
      "脂肪"
    ],
    "/fæt/",
    "This product is low in fat and salt.",
    "この製品は脂肪分と塩分が少ない。",
    null
  ],
  [
    "favour",
    "B1",
    "名詞・動詞",
    [
      "お願い",
      "親切"
    ],
    "/ˈfeɪvɚ/",
    "Could you do me a favour and check this translation?",
    "お願いがあるのですが、この翻訳を確認してもらえますか。",
    null
  ],
  [
    "fear",
    "A2",
    "名詞・動詞",
    [
      "恐れ",
      "を恐れる"
    ],
    "/fɪr/",
    "Fear of failure can prevent people from trying.",
    "失敗への恐れは人が挑戦するのを妨げることがある。",
    null
  ],
  [
    "feather",
    "B2",
    "名詞",
    [
      "羽"
    ],
    "/ˈfɛðɚ/",
    "A white feather lay on the path.",
    "白い羽が小道に落ちていた。",
    null
  ],
  [
    "federal",
    "B2",
    "形容詞",
    [
      "連邦の",
      "連邦制の"
    ],
    "/ˈfɛdɚəl/",
    "The federal government announced new safety standards.",
    "連邦政府は新しい安全基準を発表した。",
    null
  ],
  [
    "feel",
    "B2",
    "名詞",
    [
      "に触れる",
      "感じる"
    ],
    "/fil/",
    "The material should feel smooth against your skin.",
    "その素材は肌に触れるとなめらかに感じるはずだ。",
    null
  ],
  [
    "fellow",
    "B2",
    "形容詞",
    [
      "仲間",
      "特別研究員"
    ],
    "/ˈfɛloʊ/",
    "She discussed the idea with her fellow researchers.",
    "彼女は仲間の研究者たちとその考えを話し合った。",
    null
  ],
  [
    "female",
    "A2",
    "形容詞・名詞",
    [
      "女性の",
      "雌の"
    ],
    "/ˈfimeɪl/",
    "The study included equal numbers of male and female participants.",
    "その研究には男女同数の参加者が含まれた。",
    null
  ],
  [
    "fiction",
    "A2",
    "名詞",
    [
      "小説"
    ],
    "/ˈfɪkʃən/",
    "She prefers historical fiction to modern romance.",
    "彼女は現代の恋愛小説より歴史小説を好む。",
    null
  ],
  [
    "field",
    "A2",
    "名詞",
    [
      "分野"
    ],
    "/fild/",
    "New technology is changing the field of medicine.",
    "新技術が医療分野を変えている。",
    null
  ],
  [
    "fight",
    "A2",
    "名詞・動詞",
    [
      "戦う"
    ],
    "/faɪt/",
    "Communities must work together to fight pollution.",
    "地域社会は汚染と闘うため協力しなければならない。",
    null
  ],
  [
    "fighting",
    "B1",
    "名詞",
    [
      "戦闘",
      "戦闘の"
    ],
    "/ˈfaɪtɪŋ/",
    "The agreement brought an end to months of fighting.",
    "その合意で数か月の戦闘が終わった。",
    null
  ],
  [
    "file",
    "B1",
    "名詞・動詞",
    [
      "ファイル",
      "保管する"
    ],
    "/faɪl/",
    "Please file the original document in the blue folder.",
    "原本を青いフォルダーに保管してください。",
    null
  ],
  [
    "film",
    "A2",
    "動詞",
    [
      "撮影する",
      "を映画化する"
    ],
    "/fɪlm/",
    "The team plans to film the interview outdoors.",
    "チームは屋外でインタビューを撮影する予定だ。",
    null
  ],
  [
    "final",
    "A2",
    "名詞",
    [
      "最終の",
      "最終的な"
    ],
    "/ˈfaɪnəl/",
    "The final decision will be made on Friday.",
    "最終決定は金曜日に下される。",
    null
  ],
  [
    "finally",
    "A2",
    "副詞",
    [
      "ついに"
    ],
    "/ˈfaɪnəli/",
    "After three attempts, she finally passed the exam.",
    "3回挑戦した後、彼女はついに試験に合格した。",
    null
  ],
  [
    "finding",
    "B2",
    "名詞",
    [
      "結果"
    ],
    "/ˈfaɪndɪŋ/",
    "The main finding challenges an earlier theory.",
    "主な研究結果は以前の理論に異議を唱えている。",
    null
  ],
  [
    "finger",
    "A2",
    "名詞",
    [
      "指",
      "を指でいじる"
    ],
    "/ˈfɪŋgɚ/",
    "He pointed his finger at the correct line.",
    "彼は正しい行を指で示した。",
    null
  ],
  [
    "finish",
    "A2",
    "名詞",
    [
      "の仕上げをする",
      "表面の仕上げ"
    ],
    "/ˈfɪnɪʃ/",
    "We should finish the report before lunch.",
    "昼食前に報告書を仕上げるべきだ。",
    null
  ],
  [
    "fire",
    "B1",
    "動詞",
    [
      "解雇する",
      "火"
    ],
    "/ˈfaɪɚ/",
    "The company had to fire two employees for serious misconduct.",
    "会社は重大な不正行為を理由に従業員2人を解雇せざるを得なかった。",
    null
  ],
  [
    "firefighter",
    "B2",
    "名詞",
    [
      "消防士"
    ],
    "/ˈfaɪrfaɪtɚ/",
    "A firefighter carried the child to safety.",
    "消防士が子どもを安全な場所へ運んだ。",
    null
  ],
  [
    "firework",
    "B2",
    "名詞",
    [
      "花火",
      "花火大会"
    ],
    "/ˈfaɪrwɝk/",
    "A single firework lit up the night sky.",
    "一発の花火が夜空を照らした。",
    null
  ],
  [
    "firmly",
    "B2",
    "副詞",
    [
      "しっかりと"
    ],
    "/ˈfɝmli/",
    "Hold the handle firmly with both hands.",
    "両手で取っ手をしっかり握ってください。",
    null
  ],
  [
    "first",
    "A2",
    "名詞",
    [
      "最初に",
      "最初の"
    ],
    "/fɝst/",
    "She was the first person to notice the error.",
    "彼女が最初にその誤りに気づいた人だった。",
    null
  ],
  [
    "firstly",
    "A2",
    "副詞",
    [
      "第一に",
      "まず第一に"
    ],
    "/ˈfɝstli/",
    "Firstly, we need to agree on a realistic budget.",
    "第一に、現実的な予算について合意する必要がある。",
    null
  ],
  [
    "fish",
    "A2",
    "動詞",
    [
      "魚",
      "で魚をとる"
    ],
    "/fɪʃ/",
    "Local families fish in the river during summer.",
    "地元の家庭は夏にその川で魚を捕る。",
    null
  ],
  [
    "fishing",
    "A2",
    "名詞",
    [
      "漁業"
    ],
    "/ˈfɪʃɪŋ/",
    "The village depends on fishing and tourism.",
    "その村は漁業と観光に依存している。",
    null
  ],
  [
    "fit",
    "A2",
    "形容詞・動詞",
    [
      "収まる",
      "適合する"
    ],
    "/fɪt/",
    "This table will not fit through the narrow door.",
    "このテーブルは狭いドアを通らない。",
    null
  ],
  [
    "fitness",
    "B1",
    "名詞",
    [
      "体力",
      "健康"
    ],
    "/ˈfɪtnəs/",
    "Regular walking can improve your fitness.",
    "定期的な歩行は体力を向上させる。",
    null
  ],
  [
    "fixed",
    "B1",
    "形容詞",
    [
      "固定した"
    ],
    "/fɪkst/",
    "The contract offers a fixed price for two years.",
    "その契約では2年間の固定価格が提示されている。",
    null
  ],
  [
    "flag",
    "B1",
    "名詞",
    [
      "旗"
    ],
    "/flæg/",
    "A red flag was raised above the beach.",
    "浜辺に赤い旗が掲げられた。",
    null
  ],
  [
    "flame",
    "B2",
    "名詞",
    [
      "炎"
    ],
    "/fleɪm/",
    "Keep paper away from the open flame.",
    "紙を裸火から離してください。",
    null
  ],
  [
    "flash",
    "B2",
    "名詞・動詞",
    [
      "をぱっと照らす"
    ],
    "/flæʃ/",
    "A flash of lightning lit the entire valley.",
    "稲妻の光が谷全体を照らした。",
    null
  ],
  [
    "flat",
    "A2",
    "形容詞",
    [
      "平平らな",
      "空気のはいっていない"
    ],
    "/flæt/",
    "The path is flat and suitable for beginners.",
    "その道は平らで初心者に向いている。",
    null
  ],
  [
    "flavour",
    "B2",
    "名詞",
    [
      "風味",
      "味"
    ],
    "/ˈfleɪvə/",
    "Fresh herbs add flavour to the soup.",
    "新鮮なハーブはスープに風味を加える。",
    null
  ],
  [
    "flour",
    "B1",
    "名詞",
    [
      "小麦粉",
      "粉"
    ],
    "/ˈflaʊɚ/",
    "Mix the flour with water and a little salt.",
    "小麦粉を水と少量の塩で混ぜてください。",
    null
  ],
  [
    "flu",
    "A2",
    "名詞",
    [
      "インフルエンザ"
    ],
    "/flu/",
    "She stayed home for a week because of the flu.",
    "彼女はインフルエンザで1週間自宅にいた。",
    null
  ],
  [
    "fly",
    "A2",
    "名詞",
    [
      "運航する",
      "飛ぶ"
    ],
    "/flaɪ/",
    "Several airlines fly directly to the island.",
    "複数の航空会社がその島へ直行便を運航している。",
    null
  ],
  [
    "flying",
    "A2",
    "形容詞・名詞",
    [
      "飛行",
      "飛行する"
    ],
    "/ˈflaɪɪŋ/",
    "Flying is often faster than taking the train.",
    "飛行機での移動は電車より速いことが多い。",
    null
  ],
  [
    "folding",
    "B2",
    "形容詞",
    [
      "折り畳みの"
    ],
    "/ˈfoʊldɪŋ/",
    "A folding chair is stored behind the door.",
    "折り畳み椅子がドアの後ろに保管されている。",
    null
  ],
  [
    "following",
    "A2",
    "形容詞・名詞・前置詞",
    [
      "次の"
    ],
    "/ˈfɑloʊɪŋ/",
    "Please answer the following three questions.",
    "次の3つの質問に答えてください。",
    null
  ],
  [
    "fond",
    "B2",
    "形容詞",
    [
      "好きで"
    ],
    "/fɑnd/",
    "My grandmother is fond of traditional music.",
    "祖母は伝統音楽が好きだ。",
    null
  ],
  [
    "fool",
    "B2",
    "名詞",
    [
      "ばか者",
      "ばかなまねをする"
    ],
    "/ful/",
    "Only a fool would ignore such a clear warning.",
    "そんな明確な警告を無視するのは愚か者だけだ。",
    null
  ],
  [
    "forbid",
    "B2",
    "動詞",
    [
      "にを禁じる"
    ],
    "/fɚˈbɪd/",
    "The rules forbid visitors from touching the objects.",
    "規則では来場者が展示物に触れることを禁じている。",
    null
  ],
  [
    "foreign",
    "A2",
    "形容詞",
    [
      "海外の",
      "外国の"
    ],
    "/ˈfɔrən/",
    "The company is looking for new foreign markets.",
    "その会社は新しい海外市場を探している。",
    null
  ],
  [
    "forest",
    "A2",
    "名詞",
    [
      "森林",
      "林"
    ],
    "/ˈfɔrəst/",
    "A fire destroyed a large area of forest.",
    "火災で広い森林が焼失した。",
    null
  ],
  [
    "forever",
    "B1",
    "副詞",
    [
      "永遠に"
    ],
    "/fɚˈɛvɚ/",
    "No computer will continue working forever.",
    "永遠に動き続けるコンピューターはない。",
    null
  ],
  [
    "fork",
    "A2",
    "名詞",
    [
      "フォーク"
    ],
    "/fɔrk/",
    "Use a fork to hold the vegetable while cutting it.",
    "野菜を切る時はフォークで押さえてください。",
    null
  ],
  [
    "format",
    "B2",
    "名詞",
    [
      "形式"
    ],
    "/ˈfɔrmæt/",
    "Save the image in a widely supported format.",
    "画像を広く対応している形式で保存してください。",
    null
  ],
  [
    "formation",
    "B2",
    "名詞",
    [
      "形成",
      "形成されたもの"
    ],
    "/fɔrˈmeɪʃən/",
    "Scientists studied the formation of the island.",
    "科学者はその島の形成を研究した。",
    null
  ],
  [
    "formerly",
    "B2",
    "副詞",
    [
      "以前は"
    ],
    "/ˈfɔrmɚli/",
    "The building was formerly used as a school.",
    "その建物は以前、学校として使われていた。",
    null
  ],
  [
    "fortunate",
    "B2",
    "形容詞",
    [
      "幸運な",
      "幸運をもたらす"
    ],
    "/ˈfɔrtʃənət/",
    "We were fortunate to find shelter before the storm.",
    "嵐の前に避難場所を見つけられて幸運だった。",
    null
  ],
  [
    "fortunately",
    "A2",
    "副詞",
    [
      "幸いにも"
    ],
    "/ˈfɔrtʃənətli/",
    "Fortunately, no one was injured in the fire.",
    "幸い、火事でけが人はいなかった。",
    null
  ],
  [
    "forum",
    "B2",
    "名詞",
    [
      "意見交換の場",
      "フォーラム"
    ],
    "/ˈfɔrəm/",
    "The website provides a forum for exchanging practical advice.",
    "そのサイトは実用的な助言を交換する場を提供する。",
    null
  ],
  [
    "forward",
    "A2",
    "形容詞・副詞",
    [
      "前へ",
      "楽しみにして"
    ],
    "/ˈfɔrwɚd/",
    "We look forward to hearing your opinion.",
    "ご意見を伺うのを楽しみにしています。",
    null
  ],
  [
    "fossil",
    "B2",
    "名詞",
    [
      "化石",
      "化石の"
    ],
    "/ˈfɑsəl/",
    "Researchers discovered a rare fossil in the rock.",
    "研究者は岩の中で珍しい化石を発見した。",
    null
  ],
  [
    "founder",
    "B2",
    "名詞",
    [
      "創設者"
    ],
    "/ˈfaʊndɚ/",
    "The founder still advises the company on major decisions.",
    "創設者は今も重要な決定について会社に助言している。",
    null
  ],
  [
    "fraction",
    "B2",
    "名詞",
    [
      "一部"
    ],
    "/ˈfrækʃən/",
    "Only a small fraction of the waste is recycled.",
    "廃棄物のうち再利用されるのはほんの一部だ。",
    null
  ],
  [
    "fragment",
    "B2",
    "名詞",
    [
      "破片"
    ],
    "/ˈfrægmənt/",
    "Archaeologists found a fragment of ancient pottery.",
    "考古学者は古代の陶器の破片を発見した。",
    null
  ],
  [
    "framework",
    "B2",
    "名詞",
    [
      "枠組",
      "骨組み"
    ],
    "/ˈfreɪmwɝk/",
    "The law provides a framework for protecting personal data.",
    "その法律は個人情報を守る枠組みを提供する。",
    null
  ],
  [
    "fraud",
    "B2",
    "名詞",
    [
      "詐欺",
      "詐欺行為"
    ],
    "/frɔd/",
    "The bank introduced new measures to prevent fraud.",
    "銀行は詐欺を防ぐ新しい対策を導入した。",
    null
  ],
  [
    "free",
    "A2",
    "副詞・動詞",
    [
      "独立している",
      "免れている"
    ],
    "/fri/",
    "The campaign aims to free the river from plastic waste.",
    "その運動は川からプラスチックごみをなくすことを目指している。",
    null
  ],
  [
    "freedom",
    "B2",
    "名詞",
    [
      "自由",
      "自由自在"
    ],
    "/ˈfridəm/",
    "Journalists need freedom to report the facts.",
    "記者には事実を報道する自由が必要だ。",
    null
  ],
  [
    "freely",
    "B2",
    "副詞",
    [
      "自由に"
    ],
    "/ˈfrili/",
    "Members can freely express different opinions.",
    "会員は異なる意見を自由に表明できる。",
    null
  ],
  [
    "frequency",
    "B2",
    "名詞",
    [
      "頻度数"
    ],
    "/ˈfrikwənsi/",
    "The frequency of extreme weather events is increasing.",
    "異常気象の発生頻度が増えている。",
    null
  ],
  [
    "fresh",
    "A2",
    "形容詞",
    [
      "塗りたての",
      "初めての"
    ],
    "/frɛʃ/",
    "The café serves fresh bread every morning.",
    "そのカフェは毎朝焼きたてのパンを出す。",
    null
  ],
  [
    "fridge",
    "A2",
    "名詞",
    [
      "冷蔵庫"
    ],
    "/frɪdʒ/",
    "Keep the medicine in the fridge after opening it.",
    "開封後は薬を冷蔵庫に保管してください。",
    null
  ],
  [
    "friendship",
    "B1",
    "名詞",
    [
      "友情",
      "友情の具体例や関係"
    ],
    "/ˈfrɛndʃɪp/",
    "Their friendship continued long after they left school.",
    "彼らの友情は卒業後も長く続いた。",
    null
  ],
  [
    "frog",
    "A2",
    "名詞",
    [
      "カエル"
    ],
    "/frɑg/",
    "A green frog sat beside the pond.",
    "緑色のカエルが池のそばにいた。",
    null
  ],
  [
    "frozen",
    "B1",
    "形容詞",
    [
      "凍った"
    ],
    "/ˈfroʊzən/",
    "The road was frozen and dangerous.",
    "道路は凍っていて危険だった。",
    null
  ],
  [
    "fry",
    "B1",
    "動詞",
    [
      "炒める",
      "揚げる"
    ],
    "/fraɪ/",
    "Fry the vegetables for five minutes over medium heat.",
    "野菜を中火で5分間炒めてください。",
    null
  ],
  [
    "fulfil",
    "B2",
    "動詞",
    [
      "発揮する",
      "果たす"
    ],
    "/fʊlˈfɪl/",
    "The new role allowed her to fulfil her potential.",
    "新しい役割で彼女は自分の可能性を発揮できた。",
    null
  ],
  [
    "full-time",
    "B2",
    "形容詞・副詞",
    [
      "常勤の"
    ],
    "/fʊl taɪm/",
    "She returned to full-time work after the summer.",
    "彼女は夏の後に常勤の仕事へ戻った。",
    null
  ],
  [
    "fully",
    "B2",
    "副詞",
    [
      "完全に",
      "すべて"
    ],
    "/ˈfʊli/",
    "Please read the conditions fully before agreeing.",
    "同意する前に条件をすべて読んでください。",
    null
  ],
  [
    "fun",
    "A2",
    "形容詞",
    [
      "楽しみ"
    ],
    "/fʌn/",
    "The science activity was both useful and fun.",
    "その科学活動は役立つうえに楽しかった。",
    null
  ],
  [
    "fundamentally",
    "B2",
    "副詞",
    [
      "基本的に",
      "本質的に"
    ],
    "/fʌndəˈmɛntəli/",
    "The two plans are fundamentally different.",
    "その2つの計画は根本的に異なる。",
    null
  ],
  [
    "funding",
    "B2",
    "名詞",
    [
      "資金",
      "資金提供"
    ],
    "/ˈfʌndɪŋ/",
    "The research cannot continue without additional funding.",
    "その研究は追加資金なしには続けられない。",
    null
  ],
  [
    "fur",
    "B1",
    "名詞",
    [
      "毛皮",
      "柔らかな毛をした動物"
    ],
    "/fɝ/",
    "The animal's thick fur protects it from the cold.",
    "その動物の厚い毛皮は寒さから身を守る。",
    null
  ],
  [
    "furious",
    "B2",
    "形容詞",
    [
      "激怒した"
    ],
    "/fˈjʊriəs/",
    "Residents were furious about the sudden closure.",
    "住民は突然の閉鎖に激怒した。",
    null
  ],
  [
    "furniture",
    "A2",
    "名詞",
    [
      "家具"
    ],
    "/ˈfɝnɪtʃɚ/",
    "The apartment contains only basic furniture.",
    "その部屋には基本的な家具しかない。",
    null
  ],
  [
    "further",
    "A2",
    "形容詞・副詞",
    [
      "さらに先の",
      "さらに遠く"
    ],
    "/ˈfɝðɚ/",
    "Please contact us if you need further information.",
    "さらに情報が必要ならご連絡ください。",
    null
  ],
  [
    "future",
    "A2",
    "形容詞",
    [
      "将来",
      "将来の可能性"
    ],
    "/fˈjutʃɚ/",
    "Future generations will face the effects of today's choices.",
    "将来の世代は今日の選択の影響に直面する。",
    null
  ],
  [
    "gallery",
    "A2",
    "名詞",
    [
      "美術品陳列場"
    ],
    "/ˈgælɚi/",
    "The gallery displays work by young local artists.",
    "その美術館は地元の若い芸術家の作品を展示している。",
    null
  ],
  [
    "gaming",
    "B2",
    "名詞",
    [
      "ゲーム",
      "ゲームをすること"
    ],
    "/ˈgeɪmɪŋ/",
    "Online gaming can be a social activity.",
    "オンラインゲームは社交的な活動にもなりうる。",
    null
  ],
  [
    "gang",
    "B2",
    "名詞",
    [
      "一団",
      "を一団にまとめる"
    ],
    "/gæŋ/",
    "Police arrested the leader of the gang.",
    "警察はその一団の指導者を逮捕した。",
    null
  ],
  [
    "garage",
    "B1",
    "名詞",
    [
      "車庫",
      "を車庫に入れる"
    ],
    "/gɚˈɑʒ/",
    "The bicycle is stored in the garage.",
    "自転車は車庫に保管されている。",
    null
  ],
  [
    "gas",
    "A2",
    "名詞",
    [
      "ガス",
      "毒ガス"
    ],
    "/gæs/",
    "The country imports most of its natural gas.",
    "その国は天然ガスの大半を輸入している。",
    null
  ],
  [
    "gate",
    "A2",
    "名詞",
    [
      "門"
    ],
    "/geɪt/",
    "Meet me beside the main gate at noon.",
    "正午に正門のそばで会いましょう。",
    null
  ],
  [
    "gay",
    "B2",
    "形容詞",
    [
      "同性愛の"
    ],
    "/geɪ/",
    "The organization supports the rights of gay people.",
    "その団体は同性愛者の権利を支援している。",
    null
  ],
  [
    "gender",
    "B2",
    "名詞",
    [
      "性"
    ],
    "/ˈdʒɛndɚ/",
    "The survey examines differences in pay by gender.",
    "その調査は性別による賃金差を調べている。",
    null
  ],
  [
    "general",
    "A2",
    "形容詞",
    [
      "概して"
    ],
    "/ˈdʒɛnɚəl/",
    "The guide gives a general overview of the subject.",
    "その案内書はその主題の全体像を示している。",
    null
  ],
  [
    "generally",
    "B1",
    "副詞",
    [
      "概して"
    ],
    "/ˈdʒɛnɚəli/",
    "The service is generally reliable, even at busy times.",
    "そのサービスは混雑時でも概して信頼できる。",
    null
  ],
  [
    "genetic",
    "B2",
    "形容詞",
    [
      "遺伝学の",
      "遺伝子の"
    ],
    "/dʒəˈnɛtɪk/",
    "Some diseases have a strong genetic component.",
    "病気の中には遺伝的要因が強いものがある。",
    null
  ],
  [
    "genius",
    "B2",
    "名詞",
    [
      "才能",
      "才能のある人"
    ],
    "/ˈdʒinjəs/",
    "Her solution showed genuine creative genius.",
    "彼女の解決策は真の創造的才能を示した。",
    null
  ],
  [
    "genre",
    "B2",
    "名詞",
    [
      "ジャンル"
    ],
    "/ˈʒɑnrə/",
    "Mystery is the most popular genre among these readers.",
    "この読者たちには推理ものが最も人気のあるジャンルだ。",
    null
  ],
  [
    "gentleman",
    "B1",
    "名詞",
    [
      "紳士"
    ],
    "/ˈdʒɛntəlmən/",
    "An elderly gentleman offered me his seat.",
    "年配の紳士が私に席を譲ってくれた。",
    null
  ],
  [
    "genuinely",
    "B2",
    "副詞",
    [
      "心から"
    ],
    "/ˈdʒɛnjəwənli/",
    "She was genuinely pleased by the team's progress.",
    "彼女はチームの進歩を心から喜んだ。",
    null
  ],
  [
    "ghost",
    "B1",
    "名詞",
    [
      "幽霊"
    ],
    "/goʊst/",
    "Local stories say that a ghost lives in the tower.",
    "地元の話では塔に幽霊が住んでいるという。",
    null
  ],
  [
    "giant",
    "B1",
    "形容詞・名詞",
    [
      "巨大な",
      "巨大な物"
    ],
    "/ˈdʒaɪənt/",
    "The company built a giant battery beside the solar farm.",
    "会社は太陽光発電所のそばに巨大な蓄電池を建設した。",
    null
  ],
  [
    "gift",
    "A2",
    "名詞",
    [
      "生まれつきの才能",
      "天賦の才"
    ],
    "/gɪft/",
    "Her gift for languages became clear at an early age.",
    "彼女の語学の才能は幼い頃から明らかだった。",
    null
  ],
  [
    "gig",
    "B2",
    "名詞",
    [
      "演奏家の一定期間の仕事",
      "ジャズ演奏の仕事"
    ],
    "/gɪg/",
    "The band has a gig at a small club tonight.",
    "そのバンドは今夜、小さなクラブで演奏する。",
    null
  ],
  [
    "glad",
    "B1",
    "形容詞",
    [
      "うれしい",
      "うれしそうな"
    ],
    "/glæd/",
    "I am glad that you decided to join us.",
    "参加を決めてくれてうれしい。",
    null
  ],
  [
    "globalization",
    "B2",
    "名詞",
    [
      "グローバル化",
      "世界規模の一体化"
    ],
    "/gloʊbəlɪˈzeɪʃən/",
    "Globalization has connected producers with customers worldwide.",
    "グローバル化は生産者と世界中の顧客を結びつけた。",
    null
  ],
  [
    "globe",
    "B2",
    "名詞",
    [
      "世界",
      "地球"
    ],
    "/gloʊb/",
    "The news spread rapidly across the globe.",
    "そのニュースは世界中に急速に広まった。",
    null
  ],
  [
    "glove",
    "B1",
    "名詞",
    [
      "手袋",
      "に手袋をはめる"
    ],
    "/glʌv/",
    "Wear a protective glove when handling the chemical.",
    "その薬品を扱う時は保護手袋を着けてください。",
    null
  ],
  [
    "go",
    "B1",
    "名詞",
    [
      "出発する"
    ],
    "/goʊ/",
    "We should go before the roads become busy.",
    "道路が混む前に出発した方がよい。",
    null
  ],
  [
    "goal",
    "A2",
    "名詞",
    [
      "目標"
    ],
    "/goʊl/",
    "Our main goal is to reduce waiting times.",
    "私たちの主な目標は待ち時間を減らすことだ。",
    null
  ],
  [
    "god",
    "A2",
    "名詞",
    [
      "神"
    ],
    "/gɑd/",
    "The ancient people built a temple for their god.",
    "古代の人々は自分たちの神のために神殿を建てた。",
    null
  ],
  [
    "gold",
    "A2",
    "形容詞・名詞",
    [
      "金"
    ],
    "/goʊld/",
    "The medal is made of solid gold.",
    "そのメダルは純金でできている。",
    null
  ],
  [
    "golden",
    "B2",
    "形容詞",
    [
      "金色の",
      "黄金色の"
    ],
    "/ˈgoʊldən/",
    "The setting sun gave the fields a golden colour.",
    "夕日が畑を金色に染めた。",
    null
  ],
  [
    "golf",
    "A2",
    "名詞",
    [
      "ゴルフをする",
      "ゴルフ"
    ],
    "/gɑlf/",
    "He plays golf with his colleagues twice a month.",
    "彼は月2回、同僚とゴルフをする。",
    null
  ],
  [
    "good",
    "A2",
    "名詞",
    [
      "よい",
      "行儀がよい"
    ],
    "/gʊd/",
    "Fresh air is good for your health.",
    "新鮮な空気は健康によい。",
    null
  ],
  [
    "goodness",
    "B2",
    "名詞",
    [
      "優しさ"
    ],
    "/ˈgʊdnəs/",
    "Her goodness was shown through years of volunteer work.",
    "彼女の優しさは長年のボランティア活動に表れていた。",
    null
  ],
  [
    "goods",
    "B1",
    "名詞",
    [
      "商品"
    ],
    "/gʊdz/",
    "The port handles goods from many countries.",
    "その港は多くの国からの商品を扱う。",
    null
  ],
  [
    "gorgeous",
    "B2",
    "形容詞",
    [
      "見事な",
      "豪華な"
    ],
    "/ˈgɔrdʒəs/",
    "The room has a gorgeous view of the mountains.",
    "その部屋からは山々の見事な景色が見える。",
    null
  ],
  [
    "governor",
    "B2",
    "名詞",
    [
      "知事"
    ],
    "/ˈgʌvɚnɚ/",
    "The governor announced emergency support for farmers.",
    "知事は農家への緊急支援を発表した。",
    null
  ],
  [
    "grab",
    "B2",
    "動詞",
    [
      "つかむ"
    ],
    "/græb/",
    "Grab the rail if the bus starts moving.",
    "バスが動き出したら手すりをつかんでください。",
    null
  ],
  [
    "grade",
    "B1",
    "名詞・動詞",
    [
      "を等級分けする",
      "の格づけをする"
    ],
    "/greɪd/",
    "Teachers grade the written work using clear criteria.",
    "教師は明確な基準で作文を採点する。",
    null
  ],
  [
    "graduate",
    "B1",
    "名詞・動詞",
    [
      "卒業する",
      "大学卒業者"
    ],
    "/ˈgrædʒəwət/",
    "She plans to graduate from university next spring.",
    "彼女は来春大学を卒業する予定だ。",
    null
  ],
  [
    "grain",
    "B1",
    "名詞",
    [
      "穀物",
      "粒"
    ],
    "/greɪn/",
    "The bread is made with whole grain.",
    "そのパンは全粒穀物で作られている。",
    null
  ],
  [
    "grand",
    "B2",
    "形容詞",
    [
      "壮大な",
      "重大な"
    ],
    "/grænd/",
    "The ceremony took place in a grand hall.",
    "式典は壮大なホールで行われた。",
    null
  ],
  [
    "graphic",
    "B2",
    "形容詞",
    [
      "生々しい",
      "図表の"
    ],
    "/ˈgræfɪk/",
    "The report contains a graphic description of the disaster.",
    "その報告書には災害の生々しい描写がある。",
    null
  ],
  [
    "graphics",
    "B2",
    "名詞",
    [
      "画像",
      "グラフィックス"
    ],
    "/ˈgræfɪks/",
    "The game uses simple but attractive graphics.",
    "そのゲームは簡潔で魅力的な画像を使っている。",
    null
  ],
  [
    "grass",
    "A2",
    "名詞",
    [
      "芝生"
    ],
    "/græs/",
    "Please keep off the wet grass.",
    "濡れた芝生に入らないでください。",
    null
  ],
  [
    "greatly",
    "B2",
    "副詞",
    [
      "大いに"
    ],
    "/ˈgreɪtli/",
    "Your advice greatly improved the final report.",
    "あなたの助言で最終報告書が大いに改善した。",
    null
  ],
  [
    "greenhouse",
    "B2",
    "名詞",
    [
      "温室"
    ],
    "/ˈgrinhaʊs/",
    "Tomatoes grow well in a warm greenhouse.",
    "トマトは暖かい温室でよく育つ。",
    null
  ],
  [
    "greet",
    "A2",
    "動詞",
    [
      "にあいさつする"
    ],
    "/grit/",
    "Staff greet every visitor at the entrance.",
    "職員は入口ですべての来場者にあいさつする。",
    null
  ],
  [
    "grocery",
    "B2",
    "名詞",
    [
      "食料品店",
      "食料品類"
    ],
    "/ˈgroʊsɚi/",
    "A small grocery opened near our apartment.",
    "私たちのアパートの近くに小さな食料品店が開いた。",
    null
  ],
  [
    "ground",
    "A2",
    "名詞",
    [
      "地面"
    ],
    "/graʊnd/",
    "The children sat on the ground beneath the tree.",
    "子どもたちは木の下の地面に座った。",
    null
  ],
  [
    "guard",
    "B1",
    "名詞・動詞",
    [
      "警備員",
      "守る"
    ],
    "/gɑrd/",
    "A security guard checked our tickets.",
    "警備員が私たちの券を確認した。",
    null
  ],
  [
    "guest",
    "A2",
    "名詞",
    [
      "客"
    ],
    "/gɛst/",
    "Each guest received a guide to the city.",
    "客は一人ひとり市内案内を受け取った。",
    null
  ],
  [
    "guide",
    "A2",
    "名詞・動詞",
    [
      "を案内する",
      "に助言する"
    ],
    "/gaɪd/",
    "This checklist will guide you through the application process.",
    "この確認表が応募手続きを順に案内する。",
    null
  ],
  [
    "guideline",
    "B2",
    "名詞",
    [
      "指針"
    ],
    "/ˈgaɪdlaɪn/",
    "The document provides a clear guideline for safe use.",
    "その文書は安全な使用のための明確な指針を示している。",
    null
  ],
  [
    "gun",
    "A2",
    "名詞",
    [
      "銃"
    ],
    "/gʌn/",
    "The law places strict controls on gun ownership.",
    "その法律は銃の所有を厳しく規制している。",
    null
  ],
  [
    "guy",
    "A2",
    "名詞",
    [
      "男"
    ],
    "/gaɪ/",
    "The guy at the front desk was very helpful.",
    "受付の男性はとても親切だった。",
    null
  ],
  [
    "habit",
    "A2",
    "名詞",
    [
      "習慣"
    ],
    "/ˈhæbət/",
    "Reading before bed became a daily habit.",
    "寝る前の読書が毎日の習慣になった。",
    null
  ],
  [
    "habitat",
    "B2",
    "名詞",
    [
      "生息地"
    ],
    "/ˈhæbətæt/",
    "Wetlands provide an important habitat for birds.",
    "湿地は鳥にとって重要な生息地となる。",
    null
  ],
  [
    "half",
    "A2",
    "副詞",
    [
      "半"
    ],
    "/hæf/",
    "Only half of the participants completed the survey.",
    "参加者の半数しか調査を完了しなかった。",
    null
  ],
  [
    "hall",
    "A2",
    "名詞",
    [
      "ホール"
    ],
    "/hɔl/",
    "The graduation ceremony was held in the main hall.",
    "卒業式は大ホールで行われた。",
    null
  ],
  [
    "hand",
    "B1",
    "動詞",
    [
      "手渡す",
      "手"
    ],
    "/hænd/",
    "Please hand the completed form to the receptionist.",
    "記入済みの用紙を受付係に渡してください。",
    null
  ],
  [
    "hang",
    "B1",
    "動詞",
    [
      "を掛ける"
    ],
    "/hæŋ/",
    "Hang your coat on the hook by the door.",
    "コートをドア脇のフックに掛けてください。",
    null
  ],
  [
    "happily",
    "A2",
    "副詞",
    [
      "楽しく"
    ],
    "/ˈhæpəli/",
    "The children played happily in the garden.",
    "子どもたちは庭で楽しそうに遊んだ。",
    null
  ],
  [
    "happiness",
    "B1",
    "名詞",
    [
      "幸福"
    ],
    "/ˈhæpinəs/",
    "Close friendships can contribute to long-term happiness.",
    "親しい友情は長期的な幸福につながりうる。",
    null
  ],
  [
    "harbour",
    "B2",
    "名詞",
    [
      "港"
    ],
    "/ˈhɑrbɚ/",
    "Fishing boats returned to the harbour before the storm.",
    "漁船は嵐の前に港へ戻った。",
    null
  ],
  [
    "hardly",
    "B1",
    "副詞",
    [
      "ほとんど…ない"
    ],
    "/ˈhɑrdli/",
    "I could hardly recognize the town after twenty years.",
    "20年ぶりでその町をほとんど見分けられなかった。",
    null
  ],
  [
    "hate",
    "B1",
    "名詞",
    [
      "嫌う",
      "憎む"
    ],
    "/heɪt/",
    "I hate wasting food that could be eaten.",
    "私は食べられる物を無駄にするのが嫌いだ。",
    null
  ],
  [
    "have",
    "A2",
    "動詞",
    [
      "ある"
    ],
    "/hæv/",
    "We have enough time to check the results again.",
    "結果をもう一度確認する時間は十分にある。",
    null
  ],
  [
    "head",
    "B1",
    "動詞",
    [
      "率いる",
      "頭"
    ],
    "/hɛd/",
    "She will head the new research team.",
    "彼女が新しい研究チームを率いる。",
    null
  ],
  [
    "headache",
    "A2",
    "名詞",
    [
      "頭痛"
    ],
    "/ˈhɛdeɪk/",
    "Working without a break gave me a headache.",
    "休まずに働いたため頭痛がした。",
    null
  ],
  [
    "headline",
    "B1",
    "名詞",
    [
      "見出し",
      "に見出しをつける"
    ],
    "/ˈhɛdlaɪn/",
    "The election result became the main headline.",
    "選挙結果が主要な見出しになった。",
    null
  ],
  [
    "headquarters",
    "B2",
    "名詞",
    [
      "本社"
    ],
    "/ˈhɛdkwɔrtɚz/",
    "The company moved its headquarters to Singapore.",
    "その会社は本社をシンガポールへ移した。",
    null
  ],
  [
    "heal",
    "B2",
    "動詞",
    [
      "治る",
      "治す"
    ],
    "/hil/",
    "The cut should heal within a few days.",
    "その切り傷は数日で治るはずだ。",
    null
  ],
  [
    "healthcare",
    "B2",
    "名詞",
    [
      "医療",
      "保健医療"
    ],
    "/ˈhɛlθkɛr/",
    "Rural areas need better access to healthcare.",
    "農村地域には医療をより利用しやすくする必要がある。",
    null
  ],
  [
    "hearing",
    "B2",
    "名詞",
    [
      "聴力"
    ],
    "/ˈhirɪŋ/",
    "Loud music can damage your hearing.",
    "大音量の音楽は聴力を損なうことがある。",
    null
  ],
  [
    "heart",
    "A2",
    "名詞",
    [
      "心臓",
      "心"
    ],
    "/hɑrt/",
    "Regular exercise helps keep your heart healthy.",
    "定期的な運動は心臓を健康に保つ。",
    null
  ],
  [
    "heat",
    "A2",
    "名詞・動詞",
    [
      "温める",
      "熱"
    ],
    "/hit/",
    "Heat the soup slowly over a low flame.",
    "弱火でスープをゆっくり温めてください。",
    null
  ],
  [
    "heating",
    "B1",
    "名詞",
    [
      "暖房"
    ],
    "/ˈhitɪŋ/",
    "We turned on the heating when the temperature fell.",
    "気温が下がったので暖房をつけた。",
    null
  ],
  [
    "heaven",
    "B2",
    "名詞",
    [
      "天国",
      "天"
    ],
    "/ˈhɛvən/",
    "The clear mountain air felt like heaven.",
    "澄んだ山の空気は天国のようだった。",
    null
  ],
  [
    "heavily",
    "B1",
    "副詞",
    [
      "激しく",
      "重苦しく"
    ],
    "/ˈhɛvəli/",
    "It rained heavily throughout the night.",
    "夜通し激しく雨が降った。",
    null
  ],
  [
    "heavy",
    "A2",
    "形容詞",
    [
      "重い"
    ],
    "/ˈhɛvi/",
    "This box is too heavy for one person.",
    "この箱は一人で運ぶには重すぎる。",
    null
  ],
  [
    "heel",
    "B2",
    "名詞",
    [
      "かかと",
      "かかとを包む部分"
    ],
    "/hil/",
    "The back of the shoe rubbed against my heel.",
    "靴の後ろがかかとに擦れた。",
    null
  ],
  [
    "height",
    "A2",
    "名詞",
    [
      "高さ"
    ],
    "/haɪt/",
    "The tower reaches a height of eighty metres.",
    "その塔は高さ80メートルに達する。",
    null
  ],
  [
    "helicopter",
    "B1",
    "名詞",
    [
      "ヘリコプター"
    ],
    "/ˈhɛlɪkɑptɚ/",
    "A rescue helicopter landed near the village.",
    "救助ヘリコプターが村の近くに着陸した。",
    null
  ],
  [
    "hell",
    "B2",
    "名詞",
    [
      "地獄",
      "地獄のような場所"
    ],
    "/hɛl/",
    "The trapped miners described the heat as hell.",
    "閉じ込められた鉱員はその暑さを地獄のようだと表現した。",
    null
  ],
  [
    "helmet",
    "B2",
    "名詞",
    [
      "ヘルメット"
    ],
    "/ˈhɛlmət/",
    "Always wear a helmet when riding a bicycle.",
    "自転車に乗る時は必ずヘルメットを着けてください。",
    null
  ],
  [
    "helpful",
    "A2",
    "形容詞",
    [
      "役に立つ"
    ],
    "/ˈhɛlpfəl/",
    "The staff gave us some helpful advice.",
    "職員は私たちに役立つ助言をくれた。",
    null
  ],
  [
    "hence",
    "B2",
    "副詞",
    [
      "それゆえに"
    ],
    "/hɛns/",
    "The road was flooded, hence the long delay.",
    "道路が冠水したため、長い遅れが生じた。",
    null
  ],
  [
    "herb",
    "B2",
    "名詞",
    [
      "草"
    ],
    "/ɝb/",
    "This herb adds a fresh taste to the sauce.",
    "このハーブはソースに爽やかな味を加える。",
    null
  ],
  [
    "hero",
    "A2",
    "名詞",
    [
      "英雄"
    ],
    "/ˈhɪroʊ/",
    "The nurse became a local hero after the rescue.",
    "その看護師は救助後、地元の英雄になった。",
    null
  ],
  [
    "hers",
    "A2",
    "名詞",
    [
      "彼女のもの",
      "彼女の"
    ],
    "/hɚz/",
    "The red umbrella by the door is hers.",
    "ドア脇の赤い傘は彼女のものだ。",
    null
  ],
  [
    "herself",
    "A2",
    "名詞",
    [
      "彼女自身",
      "彼女自ら"
    ],
    "/hɚˈsɛlf/",
    "She taught herself how to repair bicycles.",
    "彼女は自分で自転車の修理を学んだ。",
    null
  ],
  [
    "hidden",
    "B2",
    "形容詞",
    [
      "隠された"
    ],
    "/ˈhɪdən/",
    "The key was hidden beneath a loose stone.",
    "鍵は動く石の下に隠されていた。",
    null
  ],
  [
    "high",
    "A2",
    "副詞・名詞",
    [
      "高い",
      "高い所にある"
    ],
    "/haɪ/",
    "Demand for the new service remains high.",
    "新サービスへの需要は高いままだ。",
    null
  ],
  [
    "highway",
    "B2",
    "名詞",
    [
      "幹線道路"
    ],
    "/ˈhaɪweɪ/",
    "A new highway connects the city and the airport.",
    "新しい幹線道路が市内と空港を結んでいる。",
    null
  ],
  [
    "hilarious",
    "B2",
    "形容詞",
    [
      "とてもおかしい"
    ],
    "/hɪˈlɛriəs/",
    "His account of the mistake was hilarious.",
    "彼の失敗談はとてもおかしかった。",
    null
  ],
  [
    "hill",
    "A2",
    "名詞",
    [
      "丘"
    ],
    "/hɪl/",
    "The house stands on a hill above the town.",
    "その家は町を見下ろす丘に建っている。",
    null
  ],
  [
    "himself",
    "A2",
    "名詞",
    [
      "彼自身"
    ],
    "/hɪmˈsɛlf/",
    "He designed and built the table himself.",
    "彼はそのテーブルを自分で設計し作った。",
    null
  ],
  [
    "hip",
    "B2",
    "名詞",
    [
      "腰"
    ],
    "/hɪp/",
    "She injured her hip in a skiing accident.",
    "彼女はスキー事故で腰を痛めた。",
    null
  ],
  [
    "his",
    "A2",
    "名詞",
    [
      "彼のもの",
      "彼の"
    ],
    "/hɪz/",
    "That blue bicycle is his.",
    "あの青い自転車は彼のものだ。",
    null
  ],
  [
    "historian",
    "B2",
    "名詞",
    [
      "歴史家",
      "歴史学者"
    ],
    "/hɪˈstɔriən/",
    "A local historian explained the building's past.",
    "地元の歴史家がその建物の過去を説明した。",
    null
  ],
  [
    "historic",
    "B1",
    "形容詞",
    [
      "歴史的",
      "歴史に残る"
    ],
    "/hɪˈstɔrɪk/",
    "The leaders signed a historic peace agreement.",
    "指導者たちは歴史的な和平合意に署名した。",
    null
  ],
  [
    "historical",
    "B1",
    "形容詞",
    [
      "歴史上の",
      "史実に基づく"
    ],
    "/hɪˈstɔrɪkəl/",
    "The drama is based on historical events.",
    "その劇は歴史上の出来事に基づいている。",
    null
  ],
  [
    "hit",
    "A2",
    "名詞・動詞",
    [
      "に達する"
    ],
    "/hɪt/",
    "Sales hit a record level in December.",
    "売上は12月に記録的な水準に達した。",
    null
  ],
  [
    "hockey",
    "A2",
    "名詞",
    [
      "ホッケー",
      "アイスホッケー"
    ],
    "/ˈhɑki/",
    "Our school hockey team practises twice a week.",
    "学校のホッケーチームは週2回練習する。",
    null
  ],
  [
    "hold",
    "A2",
    "名詞・動詞",
    [
      "収容できる"
    ],
    "/hoʊld/",
    "The hall can hold up to three hundred people.",
    "そのホールは最大300人を収容できる。",
    null
  ],
  [
    "hole",
    "A2",
    "名詞",
    [
      "穴"
    ],
    "/hoʊl/",
    "Water escaped through a hole in the pipe.",
    "水が管の穴から漏れた。",
    null
  ],
  [
    "hollow",
    "B2",
    "形容詞",
    [
      "空洞のある",
      "低くこもった"
    ],
    "/ˈhɑloʊ/",
    "The old tree was hollow inside.",
    "その古い木は中が空洞だった。",
    null
  ],
  [
    "holy",
    "B2",
    "形容詞",
    [
      "神聖な",
      "神にささげられた"
    ],
    "/ˈhoʊli/",
    "The temple is considered a holy place.",
    "その寺院は神聖な場所と考えられている。",
    null
  ],
  [
    "home",
    "A2",
    "形容詞",
    [
      "ホーム"
    ],
    "/hoʊm/",
    "The home team won by a single point.",
    "地元チームは1点差で勝った。",
    null
  ],
  [
    "homeless",
    "B2",
    "形容詞",
    [
      "家のない"
    ],
    "/ˈhoʊmləs/",
    "The charity provides meals for homeless people.",
    "その慈善団体は住まいのない人に食事を提供する。",
    null
  ],
  [
    "honest",
    "B1",
    "形容詞",
    [
      "正直な"
    ],
    "/ˈɑnəst/",
    "Please give me an honest answer.",
    "正直な答えをください。",
    null
  ],
  [
    "honesty",
    "B2",
    "名詞",
    [
      "誠実"
    ],
    "/ˈɑnəsti/",
    "Customers value honesty in business relationships.",
    "顧客は取引関係で誠実さを重視する。",
    null
  ],
  [
    "honour",
    "B2",
    "名詞・動詞",
    [
      "表彰する",
      "名誉"
    ],
    "/ˈɑnɚ/",
    "The university will honour her contribution to science.",
    "大学は彼女の科学への貢献を表彰する。",
    null
  ],
  [
    "hook",
    "B2",
    "名詞",
    [
      "フック",
      "フックボール"
    ],
    "/hʊk/",
    "Hang the bag on the hook behind the door.",
    "かばんをドアの後ろのフックに掛けてください。",
    null
  ],
  [
    "hope",
    "A2",
    "名詞",
    [
      "だと思う"
    ],
    "/hoʊp/",
    "We hope to complete the repairs by Friday.",
    "金曜日までに修理を終えたいと思う。",
    null
  ],
  [
    "hopefully",
    "B2",
    "副詞",
    [
      "うまくいけば"
    ],
    "/ˈhoʊpfəli/",
    "Hopefully, the weather will improve tomorrow.",
    "うまくいけば明日は天気がよくなるだろう。",
    null
  ],
  [
    "horrible",
    "B1",
    "形容詞",
    [
      "ひどい",
      "ひどくいやな"
    ],
    "/ˈhɔrəbəl/",
    "A horrible smell came from the kitchen.",
    "台所からひどい臭いがした。",
    null
  ],
  [
    "host",
    "B1",
    "名詞・動詞",
    [
      "を主催する"
    ],
    "/hoʊst/",
    "The city will host the international conference.",
    "その都市が国際会議を開催する。",
    null
  ],
  [
    "house",
    "B2",
    "動詞",
    [
      "建物"
    ],
    "/haʊs/",
    "The old building will house a new library.",
    "その古い建物には新しい図書館が入る。",
    null
  ],
  [
    "housing",
    "B2",
    "名詞",
    [
      "住宅",
      "住宅供給"
    ],
    "/ˈhaʊzɪŋ/",
    "The region faces a serious shortage of housing.",
    "その地域は深刻な住宅不足に直面している。",
    null
  ],
  [
    "human",
    "A2",
    "形容詞・名詞",
    [
      "人間の",
      "人間"
    ],
    "/hˈjumən/",
    "Clean water is a basic human need.",
    "清潔な水は人間の基本的な必要だ。",
    null
  ],
  [
    "humorous",
    "B2",
    "形容詞",
    [
      "ユーモアのある",
      "ユーモアが分かる"
    ],
    "/hˈjumɚəs/",
    "The article takes a humorous look at office life.",
    "その記事は職場生活をユーモラスに描いている。",
    null
  ],
  [
    "humour",
    "B2",
    "名詞",
    [
      "ユーモア",
      "ユーモアが分かる力"
    ],
    "/hˈjumɚ/",
    "A little humour made the difficult meeting easier.",
    "少しのユーモアで難しい会議が楽になった。",
    null
  ],
  [
    "hunger",
    "B2",
    "名詞",
    [
      "飢え"
    ],
    "/ˈhʌŋgɚ/",
    "The program aims to reduce child hunger.",
    "その制度は子どもの飢えを減らすことを目指す。",
    null
  ],
  [
    "hunting",
    "B2",
    "名詞",
    [
      "狩猟"
    ],
    "/ˈhʌntɪŋ/",
    "Hunting is strictly controlled in the national park.",
    "国立公園では狩猟が厳しく規制されている。",
    null
  ],
  [
    "hurry",
    "B1",
    "名詞・動詞",
    [
      "急ぐ必要",
      "急ぐ"
    ],
    "/ˈhɝi/",
    "There is no need to hurry; we have plenty of time.",
    "急ぐ必要はない。時間は十分にある。",
    null
  ],
  [
    "hurt",
    "A2",
    "形容詞・名詞・動詞",
    [
      "痛む",
      "傷つける"
    ],
    "/hɝt/",
    "My shoulder still hurt the day after the fall.",
    "転倒の翌日も肩が痛んだ。",
    null
  ],
  [
    "hypothesis",
    "B2",
    "名詞",
    [
      "仮説"
    ],
    "/haɪˈpɑθəsəs/",
    "The experiment did not support the original hypothesis.",
    "実験は当初の仮説を裏付けなかった。",
    null
  ],
  [
    "icon",
    "B2",
    "名詞",
    [
      "アイコン"
    ],
    "/ˈaɪkɑn/",
    "The red icon indicates a connection problem.",
    "赤いアイコンは接続上の問題を示す。",
    null
  ],
  [
    "id",
    "B2",
    "名詞",
    [
      "身分証明書"
    ],
    "/ɪd/",
    "You must show a photo ID at reception.",
    "受付で顔写真付き身分証明書を示す必要がある。",
    null
  ],
  [
    "ideal",
    "A2",
    "形容詞・名詞",
    [
      "理想",
      "理想的な"
    ],
    "/aɪˈdil/",
    "This quiet room is ideal for studying.",
    "この静かな部屋は勉強に理想的だ。",
    null
  ],
  [
    "identical",
    "B2",
    "形容詞",
    [
      "同一の"
    ],
    "/aɪˈdɛntɪkəl/",
    "The two documents are almost identical.",
    "その2つの文書はほぼ同一だ。",
    null
  ],
  [
    "ill",
    "A2",
    "形容詞",
    [
      "悪く",
      "悪"
    ],
    "/ɪl/",
    "Several passengers became ill during the voyage.",
    "航海中に数人の乗客が具合を悪くした。",
    null
  ],
  [
    "illness",
    "A2",
    "名詞",
    [
      "病気"
    ],
    "/ˈɪlnəs/",
    "The illness kept him away from work for a month.",
    "その病気で彼は1か月仕事を休んだ。",
    null
  ],
  [
    "illusion",
    "B2",
    "名詞",
    [
      "錯覚"
    ],
    "/ɪˈluʒən/",
    "The mirrors create an illusion of extra space.",
    "鏡が空間が広いという錯覚を生む。",
    null
  ],
  [
    "illustration",
    "B2",
    "名詞",
    [
      "挿絵"
    ],
    "/ɪləˈstreɪʃən/",
    "The book includes an illustration on every page.",
    "その本は各ページに挿絵がある。",
    null
  ],
  [
    "imaginary",
    "B1",
    "形容詞",
    [
      "架空の"
    ],
    "/ɪˈmædʒənɛri/",
    "The children invented an imaginary island.",
    "子どもたちは架空の島を考え出した。",
    null
  ],
  [
    "immigration",
    "B2",
    "名詞",
    [
      "移民国"
    ],
    "/ɪməˈgreɪʃən/",
    "The debate focused on immigration policy.",
    "討論は移民政策に集中した。",
    null
  ],
  [
    "immune",
    "B2",
    "形容詞",
    [
      "免疫の"
    ],
    "/ɪmˈjun/",
    "Vaccination made most participants immune to the disease.",
    "予防接種で参加者の大半がその病気への免疫を得た。",
    null
  ],
  [
    "impatient",
    "B2",
    "形容詞",
    [
      "待ちかねて"
    ],
    "/ɪmˈpeɪʃənt/",
    "Customers became impatient with the long wait.",
    "客は長い待ち時間にいら立った。",
    null
  ],
  [
    "implement",
    "B2",
    "動詞",
    [
      "を履行する"
    ],
    "/ˈɪmpləmənt/",
    "The council plans to implement the changes next year.",
    "議会は来年その変更を実施する予定だ。",
    null
  ],
  [
    "implication",
    "B2",
    "名詞",
    [
      "影響",
      "含意"
    ],
    "/ɪmpləˈkeɪʃən/",
    "The decision has a serious implication for small businesses.",
    "その決定は小企業に重大な影響を持つ。",
    null
  ],
  [
    "importance",
    "B1",
    "名詞",
    [
      "重要性",
      "重要な地位"
    ],
    "/ɪmˈpɔrtəns/",
    "The course emphasizes the importance of regular review.",
    "その講座は定期的な復習の重要性を強調する。",
    null
  ],
  [
    "impose",
    "B2",
    "動詞",
    [
      "を課する"
    ],
    "/ɪmˈpoʊz/",
    "The government may impose a limit on water use.",
    "政府は水の使用に制限を課すかもしれない。",
    null
  ],
  [
    "impossible",
    "A2",
    "形容詞",
    [
      "不可能な"
    ],
    "/ɪmˈpɑsəbəl/",
    "It is impossible to finish all this work today.",
    "今日この仕事をすべて終えるのは不可能だ。",
    null
  ],
  [
    "impressed",
    "B2",
    "形容詞",
    [
      "感心した"
    ],
    "/ɪmpˈrɛst/",
    "The visitors were impressed by the students' presentation.",
    "来訪者は学生の発表に感心した。",
    null
  ],
  [
    "incentive",
    "B2",
    "名詞",
    [
      "動機"
    ],
    "/ɪnˈsɛntɪv/",
    "The discount gives customers an incentive to order early.",
    "割引は客に早く注文する動機を与える。",
    null
  ],
  [
    "inch",
    "B2",
    "名詞",
    [
      "インチ",
      "を少しずつ動かす"
    ],
    "/ɪntʃ/",
    "Move the shelf an inch to the left.",
    "棚を左へ1インチ動かしてください。",
    null
  ],
  [
    "included",
    "A2",
    "形容詞",
    [
      "を含めて"
    ],
    "/ɪnkˈludəd/",
    "Breakfast and internet access are included in the price.",
    "朝食とインターネット利用は料金に含まれている。",
    null
  ],
  [
    "including",
    "A2",
    "前置詞",
    [
      "を含んで"
    ],
    "/ɪnkˈludɪŋ/",
    "Ten people attended, including three local teachers.",
    "地元の教師3人を含む10人が出席した。",
    null
  ],
  [
    "incorporate",
    "B2",
    "動詞",
    [
      "組み入れる"
    ],
    "/ɪnˈkɔrpɚeɪt/",
    "The design will incorporate several energy-saving features.",
    "その設計はいくつかの省エネ機能を取り入れる。",
    null
  ],
  [
    "incorrect",
    "B2",
    "形容詞",
    [
      "誤った"
    ],
    "/ɪnkɚˈɛkt/",
    "One incorrect figure changed the final total.",
    "一つの誤った数字が最終合計を変えた。",
    null
  ],
  [
    "index",
    "B2",
    "名詞",
    [
      "索引",
      "に索引をつける"
    ],
    "/ˈɪndɛks/",
    "Use the index to find the relevant section.",
    "索引を使って関連する節を見つけてください。",
    null
  ],
  [
    "indication",
    "B2",
    "名詞",
    [
      "兆候",
      "表示"
    ],
    "/ɪndəˈkeɪʃən/",
    "A rising temperature may be an indication of infection.",
    "体温上昇は感染の兆候かもしれない。",
    null
  ],
  [
    "indirect",
    "B1",
    "形容詞",
    [
      "回り道の",
      "遠回しの"
    ],
    "/ɪndɚˈɛkt/",
    "We took an indirect route to avoid traffic.",
    "渋滞を避けるため遠回りの道を通った。",
    null
  ],
  [
    "indoor",
    "B1",
    "形容詞",
    [
      "屋内の"
    ],
    "/ˈɪndɔr/",
    "The centre has an indoor swimming pool.",
    "その施設には屋内プールがある。",
    null
  ],
  [
    "indoors",
    "B1",
    "副詞",
    [
      "屋内に",
      "室内に"
    ],
    "/ˈɪndɔrz/",
    "We stayed indoors during the storm.",
    "嵐の間は屋内にいた。",
    null
  ],
  [
    "inevitably",
    "B2",
    "副詞",
    [
      "必然的に"
    ],
    "/ɪˈnɛvətəbli/",
    "A larger population will inevitably require more housing.",
    "人口が増えれば必然的により多くの住宅が必要になる。",
    null
  ],
  [
    "infer",
    "B2",
    "動詞",
    [
      "を推論する"
    ],
    "/ɪnˈfɝ/",
    "From these results, we can infer that the method works.",
    "この結果から、その方法が有効だと推論できる。",
    null
  ],
  [
    "inflation",
    "B2",
    "名詞",
    [
      "インフレ",
      "インフレーション"
    ],
    "/ɪnfˈleɪʃən/",
    "High inflation has increased the cost of food.",
    "高いインフレで食費が増えた。",
    null
  ],
  [
    "info",
    "B2",
    "名詞",
    [
      "情報"
    ],
    "/ˈɪnfoʊ/",
    "More info is available on the official website.",
    "詳しい情報は公式サイトで入手できる。",
    null
  ],
  [
    "informal",
    "A2",
    "形容詞",
    [
      "略式の"
    ],
    "/ɪnˈfɔrməl/",
    "We had an informal discussion over lunch.",
    "昼食を取りながら非公式の話し合いをした。",
    null
  ],
  [
    "infrastructure",
    "B2",
    "名詞",
    [
      "基盤",
      "インフラ"
    ],
    "/ɪnfrəˈstrʌktʃɚ/",
    "The city is investing in public transport infrastructure.",
    "市は公共交通の基盤に投資している。",
    null
  ],
  [
    "inhabitant",
    "B2",
    "名詞",
    [
      "住人"
    ],
    "/ɪnˈhæbətənt/",
    "Every inhabitant received a warning message.",
    "住民全員が警告メッセージを受け取った。",
    null
  ],
  [
    "inherit",
    "B2",
    "動詞",
    [
      "を受け継ぐ"
    ],
    "/ɪnˈhɛrət/",
    "She will inherit the family business.",
    "彼女は家業を引き継ぐ予定だ。",
    null
  ],
  [
    "injured",
    "B1",
    "形容詞",
    [
      "傷つけられた"
    ],
    "/ˈɪndʒɚd/",
    "Two injured hikers were taken to hospital.",
    "負傷した登山者2人が病院へ運ばれた。",
    null
  ],
  [
    "ink",
    "B2",
    "名詞",
    [
      "のインク",
      "をインクで書く"
    ],
    "/ɪŋk/",
    "The printer has run out of black ink.",
    "プリンターの黒インクが切れた。",
    null
  ],
  [
    "innovative",
    "B2",
    "形容詞",
    [
      "革新的な"
    ],
    "/ˈɪnəveɪtɪv/",
    "The award recognizes innovative teaching methods.",
    "その賞は革新的な教授法を評価する。",
    null
  ],
  [
    "input",
    "B2",
    "名詞",
    [
      "意見",
      "入力"
    ],
    "/ˈɪnpʊt/",
    "We need input from users before changing the design.",
    "設計を変える前に利用者の意見が必要だ。",
    null
  ],
  [
    "inquiry",
    "B2",
    "名詞",
    [
      "調査"
    ],
    "/ɪnkˈwaɪri/",
    "The committee opened an inquiry into the accident.",
    "委員会は事故の調査を開始した。",
    null
  ],
  [
    "insect",
    "A2",
    "名詞",
    [
      "昆虫",
      "虫"
    ],
    "/ˈɪnsɛkt/",
    "Each insect plays a role in the forest ecosystem.",
    "昆虫はそれぞれ森林生態系で役割を果たす。",
    null
  ],
  [
    "insert",
    "B2",
    "動詞",
    [
      "を差し込む",
      "差し込みページ"
    ],
    "/ɪnˈsɝt/",
    "Insert the card with the chip facing upwards.",
    "チップを上向きにしてカードを差し込んでください。",
    null
  ],
  [
    "inside",
    "A2",
    "形容詞・副詞・名詞・前置詞",
    [
      "の中で"
    ],
    "/ɪnˈsaɪd/",
    "The keys were inside the top drawer.",
    "鍵は一番上の引き出しの中にあった。",
    null
  ],
  [
    "inspector",
    "B2",
    "名詞",
    [
      "調査官"
    ],
    "/ɪnsˈpɛktɚ/",
    "A safety inspector visited the factory.",
    "安全検査官が工場を訪れた。",
    null
  ],
  [
    "installation",
    "B2",
    "名詞",
    [
      "取り付け"
    ],
    "/ɪnstəˈleɪʃən/",
    "Installation of the new system took two days.",
    "新システムの設置には2日かかった。",
    null
  ],
  [
    "instantly",
    "B2",
    "副詞",
    [
      "ただちに"
    ],
    "/ˈɪnstəntli/",
    "The audience instantly recognized the song.",
    "観客はその曲をすぐに聞き分けた。",
    null
  ],
  [
    "instead",
    "A2",
    "副詞",
    [
      "その代りとして"
    ],
    "/ɪnsˈtɛd/",
    "We cancelled the drive and took the train instead.",
    "車で行くのをやめ、代わりに電車を使った。",
    null
  ],
  [
    "instructor",
    "A2",
    "名詞",
    [
      "指導者"
    ],
    "/ɪnstˈrʌktɚ/",
    "The instructor demonstrated the correct technique.",
    "指導者が正しい技術を実演した。",
    null
  ],
  [
    "integrate",
    "B2",
    "動詞",
    [
      "を統合する"
    ],
    "/ˈɪntəgreɪt/",
    "Schools should integrate technology into lessons carefully.",
    "学校は慎重に技術を授業へ組み込むべきだ。",
    null
  ],
  [
    "intellectual",
    "B2",
    "形容詞",
    [
      "知的な",
      "知性的な"
    ],
    "/ɪntəˈlɛktʃuəl/",
    "The debate was an interesting intellectual challenge.",
    "その討論は興味深い知的な挑戦だった。",
    null
  ],
  [
    "intended",
    "B2",
    "形容詞",
    [
      "意図した",
      "目指した"
    ],
    "/ɪnˈtɛndɪd/",
    "The medicine had the intended effect.",
    "その薬は意図した効果を上げた。",
    null
  ],
  [
    "interaction",
    "B2",
    "名詞",
    [
      "交流",
      "相互作用"
    ],
    "/ɪntɚˈækʃən/",
    "The activity encourages interaction between students.",
    "その活動は学生どうしの交流を促す。",
    null
  ],
  [
    "interpretation",
    "B2",
    "名詞",
    [
      "解釈"
    ],
    "/ɪntɝprɪˈteɪʃən/",
    "Her interpretation of the poem differed from mine.",
    "彼女の詩の解釈は私のものと異なった。",
    null
  ],
  [
    "interval",
    "B2",
    "名詞",
    [
      "休憩",
      "間隔"
    ],
    "/ˈɪntɚvəl/",
    "There will be a short interval between the talks.",
    "講演の間に短い休憩がある。",
    null
  ],
  [
    "introduction",
    "A2",
    "名詞",
    [
      "入門"
    ],
    "/ɪntrəˈdʌkʃən/",
    "The first unit is an introduction to academic writing.",
    "第1単元は学術的な文章の入門だ。",
    null
  ],
  [
    "invade",
    "B2",
    "動詞",
    [
      "に侵入する",
      "を侵害する"
    ],
    "/ɪnˈveɪd/",
    "Foreign troops threatened to invade the country.",
    "外国軍がその国へ侵攻すると脅した。",
    null
  ],
  [
    "invasion",
    "B2",
    "名詞",
    [
      "侵攻",
      "侵入"
    ],
    "/ɪnˈveɪʒən/",
    "The invasion forced thousands to leave their homes.",
    "侵攻で何千人もの人が家を離れた。",
    null
  ],
  [
    "invent",
    "A2",
    "動詞",
    [
      "を発明する"
    ],
    "/ɪnˈvɛnt/",
    "Students were asked to invent a useful household tool.",
    "学生は役立つ家庭用品を考案するよう求められた。",
    null
  ],
  [
    "invention",
    "A2",
    "名詞",
    [
      "発明",
      "発明品"
    ],
    "/ɪnˈvɛnʃən/",
    "The invention changed the way people communicated.",
    "その発明は人々の意思疎通の方法を変えた。",
    null
  ],
  [
    "investigation",
    "B2",
    "名詞",
    [
      "調査"
    ],
    "/ɪnvɛstəˈgeɪʃən/",
    "A police investigation found evidence of fraud.",
    "警察の調査で詐欺の証拠が見つかった。",
    null
  ],
  [
    "investor",
    "B2",
    "名詞",
    [
      "投資者"
    ],
    "/ɪnˈvɛstɚ/",
    "Each investor received a copy of the report.",
    "投資家はそれぞれ報告書の写しを受け取った。",
    null
  ],
  [
    "invite",
    "A2",
    "動詞",
    [
      "を招待する"
    ],
    "/ɪnˈvaɪt/",
    "We would like to invite you to the opening event.",
    "開会イベントへご招待したいと思います。",
    null
  ],
  [
    "iron",
    "B1",
    "名詞・動詞",
    [
      "鉄"
    ],
    "/ˈaɪɚn/",
    "The bridge is built mainly from iron and stone.",
    "その橋は主に鉄と石で造られている。",
    null
  ],
  [
    "isolate",
    "B2",
    "動詞",
    [
      "特定して切り離す",
      "分離する"
    ],
    "/ˈaɪsəleɪt/",
    "Researchers managed to isolate the cause of the fault.",
    "研究者は不具合の原因を特定して切り離した。",
    null
  ],
  [
    "isolated",
    "B2",
    "形容詞",
    [
      "孤立した"
    ],
    "/ˈaɪsəleɪtəd/",
    "The village remained isolated after the landslide.",
    "土砂崩れ後、その村は孤立したままだった。",
    null
  ],
  [
    "it",
    "B1",
    "名詞",
    [
      "そのことは"
    ],
    "/ɪt/",
    "It is important to back up your files.",
    "ファイルをバックアップすることが重要だ。",
    null
  ],
  [
    "itself",
    "A2",
    "名詞",
    [
      "そのもの"
    ],
    "/ɪtˈsɛlf/",
    "The device turns itself off after ten minutes.",
    "その装置は10分後に自動で電源が切れる。",
    null
  ],
  [
    "jail",
    "B2",
    "名詞・動詞",
    [
      "刑務所",
      "を刑務所に入れる"
    ],
    "/dʒeɪl/",
    "The court sent the offender to jail.",
    "裁判所は犯罪者を刑務所へ送った。",
    null
  ],
  [
    "jam",
    "A2",
    "名詞",
    [
      "渋滞",
      "ジャム"
    ],
    "/dʒæm/",
    "Heavy traffic created a long jam near the bridge.",
    "交通量が多く橋の近くで長い渋滞が起きた。",
    null
  ],
  [
    "jazz",
    "A2",
    "名詞",
    [
      "ジャズ",
      "をジャズふうに演奏する"
    ],
    "/dʒæz/",
    "The café hosts a live jazz performance on Fridays.",
    "そのカフェでは金曜日にジャズの生演奏がある。",
    null
  ],
  [
    "jet",
    "B2",
    "名詞",
    [
      "ジェット機で行く",
      "をジェット機で運ぶ"
    ],
    "/dʒɛt/",
    "A private jet landed at the small airport.",
    "自家用ジェット機が小さな空港に着陸した。",
    null
  ],
  [
    "jewellery",
    "A2",
    "名詞",
    [
      "装身具類"
    ],
    "/ˈdʒuːəlrɪ/",
    "She keeps her jewellery in a locked drawer.",
    "彼女は宝飾品を鍵付きの引き出しに保管している。",
    null
  ],
  [
    "joint",
    "B2",
    "形容詞・名詞",
    [
      "共同の",
      "両院合同の"
    ],
    "/dʒɔɪnt/",
    "The project is a joint effort by two universities.",
    "その事業は2大学の共同の取り組みだ。",
    null
  ],
  [
    "joke",
    "A2",
    "名詞・動詞",
    [
      "冗談",
      "冗談を言う"
    ],
    "/dʒoʊk/",
    "He told a joke to relax the nervous audience.",
    "彼は緊張した観客を和ませるため冗談を言った。",
    null
  ],
  [
    "journalism",
    "B2",
    "名詞",
    [
      "ジャーナリズム",
      "ジャーナリズム科"
    ],
    "/ˈdʒɝnəlɪzəm/",
    "Accurate reporting is central to responsible journalism.",
    "正確な報道は責任あるジャーナリズムの中心だ。",
    null
  ],
  [
    "journalist",
    "A2",
    "名詞",
    [
      "記者",
      "ジャーナリスト"
    ],
    "/ˈdʒɝnələst/",
    "A journalist interviewed residents after the flood.",
    "記者が洪水後に住民へ取材した。",
    null
  ],
  [
    "joy",
    "B2",
    "名詞",
    [
      "喜び",
      "喜びのもと"
    ],
    "/dʒɔɪ/",
    "The children shouted with joy when the snow began.",
    "雪が降り始めると子どもたちは喜びの声を上げた。",
    null
  ],
  [
    "judgement",
    "B2",
    "名詞",
    [
      "判断"
    ],
    "/ˈdʒʌdʒmənt/",
    "Good judgement is essential in an emergency.",
    "緊急時には適切な判断が不可欠だ。",
    null
  ],
  [
    "jump",
    "A2",
    "名詞・動詞",
    [
      "跳ぶ"
    ],
    "/dʒʌmp/",
    "The athlete can jump more than two metres.",
    "その選手は2メートル以上跳べる。",
    null
  ],
  [
    "jury",
    "B2",
    "名詞",
    [
      "陪審員団",
      "審査員団"
    ],
    "/ˈdʒʊri/",
    "The jury reached a decision after three hours.",
    "陪審員団は3時間後に評決へ達した。",
    null
  ],
  [
    "key",
    "B1",
    "動詞",
    [
      "鍵"
    ],
    "/ki/",
    "Clear communication is key to successful teamwork.",
    "明確な意思疎通はチーム成功の鍵だ。",
    null
  ],
  [
    "keyboard",
    "B1",
    "名詞",
    [
      "キーをたたいてを入れる",
      "キーをたたく"
    ],
    "/ˈkibɔrd/",
    "This keyboard is designed for use with tablets.",
    "このキーボードはタブレット用に設計されている。",
    null
  ],
  [
    "kick",
    "B1",
    "名詞・動詞",
    [
      "けられたボール",
      "けられたボールの飛んだ距離"
    ],
    "/kɪk/",
    "He tried to kick the ball into the corner.",
    "彼はボールを隅へ蹴り込もうとした。",
    null
  ],
  [
    "kid",
    "A2",
    "名詞",
    [
      "子ども"
    ],
    "/kɪd/",
    "Every kid in the class received a book.",
    "クラスの子ども全員が本を受け取った。",
    null
  ],
  [
    "kill",
    "A2",
    "動詞",
    [
      "枯らす",
      "殺す"
    ],
    "/kɪl/",
    "The cold weather may kill young plants.",
    "寒い天候で若い植物が枯れるかもしれない。",
    null
  ],
  [
    "killing",
    "B1",
    "名詞",
    [
      "殺害"
    ],
    "/ˈkɪlɪŋ/",
    "The killing of protected animals is illegal.",
    "保護動物の殺害は違法だ。",
    null
  ],
  [
    "kind",
    "B1",
    "形容詞",
    [
      "親切な"
    ],
    "/kaɪnd/",
    "It was kind of you to offer your help.",
    "助けを申し出てくれて親切でした。",
    null
  ],
  [
    "king",
    "A2",
    "名詞",
    [
      "国王",
      "王"
    ],
    "/kɪŋ/",
    "The king addressed the nation on television.",
    "国王はテレビで国民に語りかけた。",
    null
  ],
  [
    "kiss",
    "B1",
    "名詞・動詞",
    [
      "キス",
      "キスをする"
    ],
    "/kɪs/",
    "She gave her daughter a kiss before school.",
    "彼女は登校前に娘へキスをした。",
    null
  ],
  [
    "kit",
    "B2",
    "名詞",
    [
      "身の回り品一式",
      "用具一式"
    ],
    "/kɪt/",
    "The emergency kit contains food, water, and a radio.",
    "非常用品一式には食料、水、ラジオが入っている。",
    null
  ],
  [
    "knee",
    "A2",
    "名詞",
    [
      "ひざ"
    ],
    "/ni/",
    "He wore a support around his injured knee.",
    "彼は痛めた膝にサポーターを着けていた。",
    null
  ],
  [
    "knife",
    "A2",
    "名詞",
    [
      "ナイフ",
      "をナイフで切る"
    ],
    "/naɪf/",
    "Use a sharp knife to slice the tomatoes.",
    "よく切れるナイフでトマトを薄切りにしてください。",
    null
  ],
  [
    "knock",
    "A2",
    "名詞・動詞",
    [
      "ノック",
      "ノックすること"
    ],
    "/nɑk/",
    "Please knock before entering the office.",
    "事務所へ入る前にノックしてください。",
    null
  ],
  [
    "lab",
    "A2",
    "名詞",
    [
      "実験室"
    ],
    "/læb/",
    "The samples were sent to a lab for testing.",
    "試料は検査のため研究室へ送られた。",
    null
  ],
  [
    "labour",
    "B2",
    "名詞",
    [
      "労働",
      "労働者"
    ],
    "/ˈleɪbɚ/",
    "The project requires skilled labour.",
    "その事業には熟練労働力が必要だ。",
    null
  ],
  [
    "ladder",
    "B2",
    "名詞",
    [
      "はしご",
      "にはしごをかける"
    ],
    "/ˈlædɚ/",
    "Use a stable ladder to reach the roof.",
    "屋根へ上がるには安定したはしごを使ってください。",
    null
  ],
  [
    "lady",
    "A2",
    "名詞",
    [
      "女性"
    ],
    "/ˈleɪdi/",
    "An elderly lady asked me for directions.",
    "年配の女性が私に道を尋ねた。",
    null
  ],
  [
    "lake",
    "A2",
    "名詞",
    [
      "湖"
    ],
    "/leɪk/",
    "The lake supplies drinking water to the city.",
    "その湖は市へ飲料水を供給している。",
    null
  ],
  [
    "lamp",
    "A2",
    "名詞",
    [
      "ランプ",
      "明かり"
    ],
    "/læmp/",
    "A desk lamp provides enough light for reading.",
    "机のランプは読書に十分な明かりを提供する。",
    null
  ],
  [
    "land",
    "A2",
    "動詞",
    [
      "着陸する",
      "陸"
    ],
    "/lænd/",
    "The plane will land in about twenty minutes.",
    "飛行機は約20分後に着陸する。",
    null
  ],
  [
    "landing",
    "B2",
    "名詞",
    [
      "着陸",
      "着陸場"
    ],
    "/ˈlændɪŋ/",
    "The pilot made a smooth landing despite the wind.",
    "操縦士は風にもかかわらず滑らかに着陸した。",
    null
  ],
  [
    "lane",
    "B2",
    "名詞",
    [
      "車線"
    ],
    "/leɪn/",
    "Stay in the left lane until the next exit.",
    "次の出口まで左車線にいてください。",
    null
  ],
  [
    "laptop",
    "A2",
    "名詞",
    [
      "ノートパソコン"
    ],
    "/ˈlæptɑp/",
    "My laptop is light enough to carry every day.",
    "私のノートパソコンは毎日持ち運べるほど軽い。",
    null
  ],
  [
    "last",
    "A2",
    "副詞・名詞・動詞",
    [
      "もつ",
      "続く"
    ],
    "/læst/",
    "The battery should last for at least a week.",
    "電池は少なくとも1週間もつはずだ。",
    null
  ],
  [
    "later",
    "A2",
    "形容詞",
    [
      "後で"
    ],
    "/ˈleɪtɚ/",
    "We can discuss the details later.",
    "詳細は後で話し合える。",
    null
  ],
  [
    "laughter",
    "A2",
    "名詞",
    [
      "笑い声",
      "笑い"
    ],
    "/ˈlæftɚ/",
    "The room filled with laughter after his story.",
    "彼の話の後、部屋は笑い声で満ちた。",
    null
  ],
  [
    "law",
    "A2",
    "名詞",
    [
      "法律",
      "法"
    ],
    "/lɔ/",
    "The new law protects customers' personal information.",
    "新しい法律は顧客の個人情報を守る。",
    null
  ],
  [
    "lawyer",
    "A2",
    "名詞",
    [
      "弁護士"
    ],
    "/ˈlɔjɚ/",
    "She consulted a lawyer before signing the contract.",
    "彼女は契約書に署名する前に弁護士へ相談した。",
    null
  ],
  [
    "lay",
    "B1",
    "動詞",
    [
      "を敷設する"
    ],
    "/leɪ/",
    "Workers will lay new cables under the road.",
    "作業員は道路の下に新しいケーブルを敷く。",
    null
  ],
  [
    "lazy",
    "A2",
    "形容詞",
    [
      "怠惰な"
    ],
    "/ˈleɪzi/",
    "It is lazy to copy another person's work.",
    "他人の作品を写すのは怠慢だ。",
    null
  ],
  [
    "leader",
    "A2",
    "名詞",
    [
      "指導者",
      "先導者"
    ],
    "/ˈlidɚ/",
    "A good leader listens before making a decision.",
    "よい指導者は決定前に人の話を聞く。",
    null
  ],
  [
    "leading",
    "B1",
    "形容詞",
    [
      "第一線の",
      "主要な"
    ],
    "/ˈlidɪŋ/",
    "She is a leading expert on renewable energy.",
    "彼女は再生可能エネルギーの第一人者だ。",
    null
  ],
  [
    "leaf",
    "B1",
    "名詞",
    [
      "葉",
      "1枚"
    ],
    "/lif/",
    "A single yellow leaf fell from the tree.",
    "黄色い葉が一枚、木から落ちた。",
    null
  ],
  [
    "leaflet",
    "B2",
    "名詞",
    [
      "ちらし"
    ],
    "/ˈliflət/",
    "The clinic produced a leaflet about healthy eating.",
    "診療所は健康的な食事についてのちらしを作った。",
    null
  ],
  [
    "league",
    "B2",
    "名詞",
    [
      "リーグ"
    ],
    "/lig/",
    "The team moved to the top of the league.",
    "そのチームはリーグ首位に上がった。",
    null
  ],
  [
    "learning",
    "A2",
    "名詞",
    [
      "学習"
    ],
    "/ˈlɝnɪŋ/",
    "Active practice makes learning more effective.",
    "能動的な練習は学習をより効果的にする。",
    null
  ],
  [
    "least",
    "A2",
    "副詞・限定詞・名詞",
    [
      "最も少なく",
      "最も小さい"
    ],
    "/list/",
    "This option causes the least environmental damage.",
    "この選択肢が環境への被害を最も少なくする。",
    null
  ],
  [
    "leave",
    "B2",
    "名詞",
    [
      "出発する",
      "する"
    ],
    "/liv/",
    "The last bus will leave at eleven.",
    "最終バスは11時に出発する。",
    null
  ],
  [
    "legend",
    "B2",
    "名詞",
    [
      "伝説",
      "伝説文学"
    ],
    "/ˈlɛdʒənd/",
    "According to legend, treasure is hidden on the island.",
    "伝説によると島に宝が隠されている。",
    null
  ],
  [
    "lemon",
    "A2",
    "名詞",
    [
      "レモン",
      "レモンの木"
    ],
    "/ˈlɛmən/",
    "Add a slice of lemon to the water.",
    "水にレモンを一切れ加えてください。",
    null
  ],
  [
    "lend",
    "A2",
    "動詞",
    [
      "を貸す",
      "金を貸す"
    ],
    "/lɛnd/",
    "Could you lend me your notes until tomorrow?",
    "明日までノートを貸してもらえますか。",
    null
  ],
  [
    "lens",
    "B2",
    "名詞",
    [
      "レンズ"
    ],
    "/lɛnz/",
    "The camera lens needs careful cleaning.",
    "カメラのレンズは丁寧に掃除する必要がある。",
    null
  ],
  [
    "less",
    "A2",
    "副詞・限定詞・名詞",
    [
      "もっと少ない",
      "いっそう少ない"
    ],
    "/lɛs/",
    "The new model uses less electricity.",
    "新型は使う電気がより少ない。",
    null
  ],
  [
    "licence",
    "B2",
    "名詞",
    [
      "免許",
      "免許状"
    ],
    "/ˈlaɪsəns/",
    "You need a licence to operate this vehicle.",
    "この車両を運転するには免許が必要だ。",
    null
  ],
  [
    "lie",
    "B1",
    "名詞・動詞",
    [
      "ある"
    ],
    "/laɪ/",
    "A small village lies beyond the hills.",
    "丘の向こうに小さな村がある。",
    null
  ],
  [
    "lifestyle",
    "A2",
    "名詞",
    [
      "生き方"
    ],
    "/ˈlaɪfstaɪl/",
    "Regular exercise is part of a healthy lifestyle.",
    "定期的な運動は健康的な生活様式の一部だ。",
    null
  ],
  [
    "lifetime",
    "B2",
    "名詞",
    [
      "一生",
      "一生の"
    ],
    "/ˈlaɪftaɪm/",
    "The journey was a once-in-a-lifetime experience.",
    "その旅は一生に一度の経験だった。",
    null
  ],
  [
    "lift",
    "A2",
    "名詞・動詞",
    [
      "を持ち上げる",
      "上げる"
    ],
    "/lɪft/",
    "Can you help me lift this table?",
    "このテーブルを持ち上げるのを手伝ってもらえますか。",
    null
  ],
  [
    "light",
    "A2",
    "動詞",
    [
      "この世に光を与える人"
    ],
    "/laɪt/",
    "Use this switch to light the entrance.",
    "このスイッチで入口を照らしてください。",
    null
  ],
  [
    "lighting",
    "B2",
    "名詞",
    [
      "照明",
      "照明方法"
    ],
    "/ˈlaɪtɪŋ/",
    "Good lighting makes the room easier to use.",
    "よい照明でその部屋は使いやすくなる。",
    null
  ],
  [
    "like",
    "B1",
    "名詞",
    [
      "らしい",
      "にふさわしい"
    ],
    "/laɪk/",
    "I would like more time to consider the offer.",
    "その申し出を考える時間がもっと欲しい。",
    null
  ],
  [
    "likewise",
    "B2",
    "副詞",
    [
      "同様に"
    ],
    "/ˈlaɪkwaɪz/",
    "The first plan is expensive, and the second is likewise costly.",
    "最初の案は高価で、2番目も同様に費用がかかる。",
    null
  ],
  [
    "limitation",
    "B2",
    "名詞",
    [
      "制約"
    ],
    "/lɪmɪˈteɪʃən/",
    "Cost is the main limitation of this technology.",
    "費用がこの技術の主な制約だ。",
    null
  ],
  [
    "line",
    "B2",
    "動詞",
    [
      "並ぶ",
      "線"
    ],
    "/laɪn/",
    "Tall trees line both sides of the road.",
    "高い木々が道路の両側に並んでいる。",
    null
  ],
  [
    "lip",
    "B1",
    "名詞",
    [
      "くちびる"
    ],
    "/lɪp/",
    "She cut her lip when she fell.",
    "彼女は転んだ時に唇を切った。",
    null
  ],
  [
    "listener",
    "A2",
    "名詞",
    [
      "聞き手"
    ],
    "/ˈlɪsənɚ/",
    "A careful listener notices changes in tone.",
    "注意深い聞き手は口調の変化に気づく。",
    null
  ],
  [
    "literary",
    "B2",
    "形容詞",
    [
      "文学の",
      "文学に通じた"
    ],
    "/ˈlɪtɚɛri/",
    "The city holds an annual literary festival.",
    "その都市は毎年文学祭を開く。",
    null
  ],
  [
    "litre",
    "B2",
    "名詞",
    [
      "リットル"
    ],
    "/ˈliːtə/",
    "The tank holds one litre of water.",
    "その容器には1リットルの水が入る。",
    null
  ],
  [
    "litter",
    "B2",
    "名詞",
    [
      "散らかったくず"
    ],
    "/ˈlɪtɚ/",
    "Visitors are asked to take their litter home.",
    "来訪者はごみを持ち帰るよう求められている。",
    null
  ],
  [
    "little",
    "A2",
    "副詞",
    [
      "ほとんどない",
      "ほとんどなく"
    ],
    "/ˈlɪtəl/",
    "There is little evidence to support the claim.",
    "その主張を裏付ける証拠はほとんどない。",
    null
  ],
  [
    "live",
    "B1",
    "形容詞・副詞",
    [
      "生放送で",
      "生きる"
    ],
    "/laɪv/",
    "The interview will be broadcast live tonight.",
    "そのインタビューは今夜生放送される。",
    null
  ],
  [
    "lively",
    "B2",
    "形容詞",
    [
      "生気にあふれた"
    ],
    "/ˈlaɪvli/",
    "We had a lively discussion about the proposal.",
    "その提案について活発な議論をした。",
    null
  ],
  [
    "living",
    "B1",
    "形容詞・名詞",
    [
      "生活の",
      "生活に適した"
    ],
    "/ˈlɪvɪŋ/",
    "The cost of living has risen sharply.",
    "生活費が急激に上昇した。",
    null
  ],
  [
    "located",
    "B1",
    "形容詞",
    [
      "位置した"
    ],
    "/ˈloʊkeɪtəd/",
    "The hotel is located near the central station.",
    "そのホテルは中央駅の近くに位置している。",
    null
  ],
  [
    "lock",
    "A2",
    "名詞・動詞",
    [
      "を締めつける"
    ],
    "/lɑk/",
    "Remember to lock the door when you leave.",
    "出る時にドアへ鍵をかけるのを忘れないでください。",
    null
  ],
  [
    "logo",
    "B2",
    "名詞",
    [
      "ロゴ"
    ],
    "/ˈloʊgoʊ/",
    "The new logo reflects the company's environmental goals.",
    "新しいロゴは会社の環境目標を表している。",
    null
  ],
  [
    "lonely",
    "B1",
    "形容詞",
    [
      "孤独の"
    ],
    "/ˈloʊnli/",
    "Working from home can sometimes feel lonely.",
    "在宅勤務は時に孤独に感じられる。",
    null
  ],
  [
    "long-term",
    "B2",
    "形容詞・副詞",
    [
      "長期の"
    ],
    "/lɔŋ tɝm/",
    "The policy needs a long-term plan for funding.",
    "その政策には長期的な資金計画が必要だ。",
    null
  ],
  [
    "look",
    "A2",
    "名詞",
    [
      "にふさわしく見える"
    ],
    "/lʊk/",
    "Take a close look at the figures in this column.",
    "この列の数字をよく見てください。",
    null
  ],
  [
    "lorry",
    "A2",
    "名詞",
    [
      "トラック"
    ],
    "/ˈlɔri/",
    "A large lorry blocked the narrow road.",
    "大型トラックが狭い道路をふさいだ。",
    null
  ],
  [
    "lost",
    "A2",
    "形容詞",
    [
      "浪費された",
      "破壊された"
    ],
    "/lɔst/",
    "A volunteer helped us find our lost dog.",
    "ボランティアが迷子の犬を見つけるのを助けてくれた。",
    null
  ],
  [
    "lottery",
    "B2",
    "名詞",
    [
      "宝くじ",
      "富くじ"
    ],
    "/ˈlɑtɚi/",
    "She won a small prize in the local lottery.",
    "彼女は地元の宝くじで小さな賞を当てた。",
    null
  ],
  [
    "loud",
    "A2",
    "形容詞・副詞",
    [
      "大きい",
      "大きな音を出す"
    ],
    "/laʊd/",
    "The music was too loud for conversation.",
    "音楽が大きすぎて会話できなかった。",
    null
  ],
  [
    "loudly",
    "A2",
    "副詞",
    [
      "大声で"
    ],
    "/ˈlaʊdli/",
    "Someone knocked loudly on the front door.",
    "誰かが玄関のドアを大きな音でたたいた。",
    null
  ],
  [
    "lovely",
    "A2",
    "形容詞",
    [
      "美しい"
    ],
    "/ˈlʌvli/",
    "We spent a lovely afternoon by the river.",
    "川辺ですてきな午後を過ごした。",
    null
  ],
  [
    "low",
    "A2",
    "形容詞・副詞・名詞",
    [
      "低い",
      "低い所にある"
    ],
    "/loʊ/",
    "Interest rates remain low this year.",
    "今年は金利が低いままだ。",
    null
  ],
  [
    "luck",
    "A2",
    "名詞",
    [
      "運",
      "幸運"
    ],
    "/lʌk/",
    "We had good luck with the weather.",
    "私たちは天候に恵まれた。",
    null
  ],
  [
    "lucky",
    "A2",
    "形容詞",
    [
      "運がよい"
    ],
    "/ˈlʌki/",
    "You were lucky to catch the final train.",
    "最終電車に間に合って運がよかった。",
    null
  ],
  [
    "lung",
    "B2",
    "名詞",
    [
      "肺"
    ],
    "/lʌŋ/",
    "Smoking can cause serious lung disease.",
    "喫煙は深刻な肺の病気を引き起こすことがある。",
    null
  ],
  [
    "lyric",
    "B2",
    "名詞",
    [
      "歌詞"
    ],
    "/ˈlɪrɪk/",
    "The song has a simple but powerful lyric.",
    "その歌には簡潔で力強い歌詞がある。",
    null
  ],
  [
    "mad",
    "B1",
    "形容詞",
    [
      "夢中になって",
      "怒った"
    ],
    "/mæd/",
    "She was mad at me for missing the meeting.",
    "彼女は私が会議を欠席したことに怒っていた。",
    null
  ],
  [
    "magic",
    "B1",
    "形容詞・名詞",
    [
      "手品",
      "手品の"
    ],
    "/ˈmædʒɪk/",
    "The performance combined music and magic.",
    "その公演は音楽と手品を組み合わせていた。",
    null
  ],
  [
    "magnificent",
    "B2",
    "形容詞",
    [
      "壮大な"
    ],
    "/mægˈnɪfəsənt/",
    "The palace offers a magnificent view of the city.",
    "その宮殿からは街の壮大な景色が見える。",
    null
  ],
  [
    "mail",
    "A2",
    "名詞・動詞",
    [
      "を郵送する(post"
    ],
    "/meɪl/",
    "Please mail the signed form to our office.",
    "署名済みの用紙を当事務所へ郵送してください。",
    null
  ],
  [
    "make",
    "B2",
    "名詞",
    [
      "の資格がある",
      "を生じさせる"
    ],
    "/meɪk/",
    "Small changes can make a big difference.",
    "小さな変化が大きな違いを生むことがある。",
    null
  ],
  [
    "make-up",
    "B2",
    "名詞",
    [
      "化粧"
    ],
    "/meɪk ʌp/",
    "The actor's make-up took more than an hour.",
    "その俳優の化粧には1時間以上かかった。",
    null
  ],
  [
    "making",
    "B2",
    "名詞",
    [
      "意思決定",
      "作ること"
    ],
    "/ˈmeɪkɪŋ/",
    "Careful planning is essential to good decision-making.",
    "慎重な計画は適切な意思決定に不可欠だ。",
    null
  ],
  [
    "male",
    "A2",
    "形容詞・名詞",
    [
      "男性の",
      "雄の"
    ],
    "/meɪl/",
    "The survey included both male and female workers.",
    "その調査には男女の労働者が含まれた。",
    null
  ],
  [
    "mall",
    "B1",
    "名詞",
    [
      "ショッピングモール"
    ],
    "/mɔl/",
    "A new shopping mall opened beside the station.",
    "駅のそばに新しいショッピングモールが開いた。",
    null
  ],
  [
    "manager",
    "A2",
    "名詞",
    [
      "管理者",
      "責任者"
    ],
    "/ˈmænədʒɚ/",
    "The manager approved my request for leave.",
    "管理者は私の休暇申請を承認した。",
    null
  ],
  [
    "manner",
    "A2",
    "名詞",
    [
      "態度"
    ],
    "/ˈmænɚ/",
    "She answered the complaint in a calm manner.",
    "彼女は苦情に落ち着いた態度で答えた。",
    null
  ],
  [
    "manufacture",
    "B2",
    "動詞",
    [
      "を製造する",
      "製造"
    ],
    "/mænjəˈfæktʃɚ/",
    "The factory will manufacture batteries for electric cars.",
    "その工場は電気自動車用の電池を製造する。",
    null
  ],
  [
    "manufacturing",
    "B2",
    "名詞",
    [
      "製造",
      "製造業"
    ],
    "/mænjəˈfæktʃɚɪŋ/",
    "The region has a long history of car manufacturing.",
    "その地域には自動車製造の長い歴史がある。",
    null
  ],
  [
    "map",
    "B2",
    "動詞",
    [
      "地図",
      "を地図にかく"
    ],
    "/mæp/",
    "Researchers plan to map changes in the coastline.",
    "研究者は海岸線の変化を地図化する予定だ。",
    null
  ],
  [
    "marathon",
    "B2",
    "名詞",
    [
      "マラソン競走"
    ],
    "/ˈmɛrəθɑn/",
    "She completed her first marathon last year.",
    "彼女は昨年初めてマラソンを完走した。",
    null
  ],
  [
    "margin",
    "B2",
    "名詞",
    [
      "余白"
    ],
    "/ˈmɑrdʒən/",
    "Write your comments in the right margin.",
    "右の余白にコメントを書いてください。",
    null
  ],
  [
    "mark",
    "A2",
    "名詞・動詞",
    [
      "印"
    ],
    "/mɑrk/",
    "Use a pencil to mark the correct answer.",
    "鉛筆で正解に印を付けてください。",
    null
  ],
  [
    "marker",
    "B2",
    "名詞",
    [
      "標識",
      "印"
    ],
    "/ˈmɑrkɚ/",
    "The red post serves as a boundary marker.",
    "赤い柱が境界標識の役割を果たす。",
    null
  ],
  [
    "market",
    "B1",
    "動詞",
    [
      "市場で売買する"
    ],
    "/ˈmɑrkət/",
    "The company plans to market the product overseas.",
    "会社はその製品を海外で販売する予定だ。",
    null
  ],
  [
    "marketing",
    "B1",
    "名詞",
    [
      "マーケティング",
      "販売促進"
    ],
    "/ˈmɑrkətɪŋ/",
    "The marketing campaign reached younger customers.",
    "販売促進活動は若い顧客に届いた。",
    null
  ],
  [
    "marriage",
    "B1",
    "名詞",
    [
      "結婚生活",
      "結婚"
    ],
    "/ˈmɛrɪdʒ/",
    "Their marriage has lasted for thirty years.",
    "彼らの結婚生活は30年間続いている。",
    null
  ],
  [
    "marry",
    "A2",
    "動詞",
    [
      "結婚する",
      "と結婚する"
    ],
    "/ˈmɛri/",
    "They plan to marry in the autumn.",
    "彼らは秋に結婚する予定だ。",
    null
  ],
  [
    "martial",
    "B2",
    "形容詞",
    [
      "武術の",
      "軍事の"
    ],
    "/ˈmɑrʃəl/",
    "She has practised a martial art since childhood.",
    "彼女は子どもの頃から武術を練習している。",
    null
  ],
  [
    "mass",
    "B2",
    "形容詞・名詞",
    [
      "大量",
      "塊"
    ],
    "/mæs/",
    "A mass of dark clouds covered the sky.",
    "大量の黒い雲が空を覆った。",
    null
  ],
  [
    "massive",
    "B2",
    "形容詞",
    [
      "どっしりした",
      "がっちりした"
    ],
    "/ˈmæsɪv/",
    "The storm caused massive damage to the harbour.",
    "嵐は港に甚大な被害をもたらした。",
    null
  ],
  [
    "master",
    "B2",
    "名詞・動詞",
    [
      "処理する能力のある人"
    ],
    "/ˈmæstɚ/",
    "It takes years of practice to master this technique.",
    "この技術を習得するには何年もの練習が必要だ。",
    null
  ],
  [
    "matching",
    "B2",
    "形容詞",
    [
      "おそろいの"
    ],
    "/ˈmætʃɪŋ/",
    "The twins wore matching blue jackets.",
    "双子はおそろいの青い上着を着ていた。",
    null
  ],
  [
    "mate",
    "B2",
    "名詞・動詞",
    [
      "仲間",
      "学友"
    ],
    "/meɪt/",
    "My old school mate now lives abroad.",
    "昔の学友は今、海外に住んでいる。",
    null
  ],
  [
    "material",
    "A2",
    "形容詞・名詞",
    [
      "教材",
      "材料"
    ],
    "/məˈtɪriəl/",
    "The course material is available online.",
    "講座の教材はオンラインで利用できる。",
    null
  ],
  [
    "mathematics",
    "A2",
    "名詞",
    [
      "数学",
      "数学的処理"
    ],
    "/mæθəˈmætɪks/",
    "Mathematics plays an important role in engineering.",
    "数学は工学で重要な役割を果たす。",
    null
  ],
  [
    "maths",
    "A2",
    "名詞",
    [
      "数学"
    ],
    "/mæθs/",
    "Maths was my favourite subject at school.",
    "数学は学校で一番好きな科目だった。",
    null
  ],
  [
    "matter",
    "A2",
    "名詞・動詞",
    [
      "体",
      "重要性"
    ],
    "/ˈmætɚ/",
    "Your opinion matters to the whole team.",
    "あなたの意見はチーム全体にとって重要だ。",
    null
  ],
  [
    "maximum",
    "B2",
    "形容詞・名詞",
    [
      "最大限",
      "最大値"
    ],
    "/ˈmæksəməm/",
    "The room has a maximum capacity of fifty.",
    "その部屋の最大収容人数は50人だ。",
    null
  ],
  [
    "may",
    "A2",
    "動詞",
    [
      "かもしれない",
      "したかもしれない"
    ],
    "/meɪ/",
    "The delivery may arrive later than expected.",
    "配達は予想より遅く到着するかもしれない。",
    null
  ],
  [
    "mayor",
    "B2",
    "名詞",
    [
      "市長"
    ],
    "/ˈmeɪɚ/",
    "The mayor opened the new community centre.",
    "市長が新しい地域センターを開設した。",
    null
  ],
  [
    "means",
    "B2",
    "名詞",
    [
      "手段"
    ],
    "/minz/",
    "Email remains an efficient means of communication.",
    "メールは効率的な意思疎通の手段であり続けている。",
    null
  ],
  [
    "meanwhile",
    "B1",
    "副詞",
    [
      "その間に"
    ],
    "/ˈminwaɪl/",
    "Dinner was cooking; meanwhile, we prepared the table.",
    "夕食を調理する間に、私たちは食卓を準備した。",
    null
  ],
  [
    "measure",
    "B1",
    "名詞・動詞",
    [
      "測定法"
    ],
    "/ˈmɛʒɚ/",
    "The device can measure changes in air quality.",
    "その装置は空気の質の変化を測定できる。",
    null
  ],
  [
    "measurement",
    "B2",
    "名詞",
    [
      "測定",
      "測定法"
    ],
    "/ˈmɛʒɚmənt/",
    "Each measurement was repeated three times.",
    "各測定は3回繰り返された。",
    null
  ],
  [
    "mechanic",
    "B2",
    "名詞",
    [
      "整備士"
    ],
    "/məˈkænɪk/",
    "A mechanic checked the engine for faults.",
    "整備士がエンジンの不具合を調べた。",
    null
  ],
  [
    "mechanical",
    "B2",
    "形容詞",
    [
      "機械の",
      "機械を必要とする"
    ],
    "/məˈkænɪkəl/",
    "A mechanical problem delayed the train.",
    "機械の問題で電車が遅れた。",
    null
  ],
  [
    "mechanism",
    "B2",
    "名詞",
    [
      "仕組み"
    ],
    "/ˈmɛkənɪzəm/",
    "The exact mechanism is not yet fully understood.",
    "正確な仕組みはまだ完全には理解されていない。",
    null
  ],
  [
    "medal",
    "B2",
    "名詞",
    [
      "メダル"
    ],
    "/ˈmɛdəl/",
    "She won a gold medal in the final race.",
    "彼女は最終レースで金メダルを獲得した。",
    null
  ],
  [
    "media",
    "A2",
    "名詞",
    [
      "メディア"
    ],
    "/ˈmidiə/",
    "The story received little attention in the media.",
    "その話はメディアでほとんど注目されなかった。",
    null
  ],
  [
    "medical",
    "A2",
    "形容詞",
    [
      "医療の",
      "医学の"
    ],
    "/ˈmɛdəkəl/",
    "The patient needs immediate medical attention.",
    "その患者には直ちに医療処置が必要だ。",
    null
  ],
  [
    "medication",
    "B2",
    "名詞",
    [
      "薬"
    ],
    "/mɛdəˈkeɪʃən/",
    "Take this medication after each meal.",
    "この薬を毎食後に服用してください。",
    null
  ],
  [
    "medicine",
    "A2",
    "名詞",
    [
      "医学"
    ],
    "/ˈmɛdəsən/",
    "Modern medicine has greatly improved survival rates.",
    "現代医学は生存率を大きく改善した。",
    null
  ],
  [
    "medium",
    "B1",
    "形容詞・名詞",
    [
      "中くらいの",
      "媒体"
    ],
    "/ˈmidiəm/",
    "Choose a medium size if the large one is too loose.",
    "大きいサイズが緩すぎるなら中サイズを選んでください。",
    null
  ],
  [
    "melt",
    "B2",
    "動詞",
    [
      "溶ける"
    ],
    "/mɛlt/",
    "The snow will melt as the temperature rises.",
    "気温が上がると雪は解ける。",
    null
  ],
  [
    "membership",
    "B2",
    "名詞",
    [
      "全会員",
      "会員数"
    ],
    "/ˈmɛmbɚʃɪp/",
    "Annual membership includes free entry to exhibitions.",
    "年会員資格には展示への無料入場が含まれる。",
    null
  ],
  [
    "memorable",
    "B2",
    "形容詞",
    [
      "忘れられない",
      "きわだった"
    ],
    "/ˈmɛmɚəbəl/",
    "The final concert was a memorable experience.",
    "最後の演奏会は忘れられない経験だった。",
    null
  ],
  [
    "memory",
    "A2",
    "名詞",
    [
      "記憶",
      "記憶している期間"
    ],
    "/ˈmɛmɚi/",
    "Regular review strengthens long-term memory.",
    "定期的な復習は長期記憶を強化する。",
    null
  ],
  [
    "mental",
    "B1",
    "形容詞",
    [
      "心の"
    ],
    "/ˈmɛntəl/",
    "Exercise can support both physical and mental health.",
    "運動は身体と心の両方の健康を支える。",
    null
  ],
  [
    "mention",
    "A2",
    "名詞・動詞",
    [
      "触れる",
      "言及する"
    ],
    "/ˈmɛnʃən/",
    "She did not mention the change during the meeting.",
    "彼女は会議中に変更について触れなかった。",
    null
  ],
  [
    "mess",
    "B1",
    "名詞",
    [
      "雑然としていること"
    ],
    "/mɛs/",
    "The kitchen was a mess after the party.",
    "パーティー後、台所は散らかっていた。",
    null
  ],
  [
    "metal",
    "A2",
    "名詞",
    [
      "金属",
      "に金属をかぶせる"
    ],
    "/ˈmɛtəl/",
    "The frame is made from recycled metal.",
    "その枠は再生金属でできている。",
    null
  ],
  [
    "metaphor",
    "B2",
    "名詞",
    [
      "隠喩"
    ],
    "/ˈmɛtəfɔr/",
    "The writer uses the sea as a metaphor for freedom.",
    "作家は自由の比喩として海を使っている。",
    null
  ],
  [
    "method",
    "A2",
    "名詞",
    [
      "方法"
    ],
    "/ˈmɛθəd/",
    "This method requires less time and fewer materials.",
    "この方法は時間も材料も少なくて済む。",
    null
  ],
  [
    "middle",
    "A2",
    "形容詞・名詞",
    [
      "中央"
    ],
    "/ˈmɪdəl/",
    "A fountain stands in the middle of the square.",
    "広場の中央に噴水がある。",
    null
  ],
  [
    "might",
    "A2",
    "動詞",
    [
      "かもしれないのだが",
      "したかもしれない"
    ],
    "/maɪt/",
    "The road might be closed because of snow.",
    "雪のため道路が閉鎖されているかもしれない。",
    null
  ],
  [
    "mild",
    "B1",
    "形容詞",
    [
      "おだやかな",
      "ものやわらかな"
    ],
    "/maɪld/",
    "The region enjoys mild weather in winter.",
    "その地域は冬も穏やかな天候だ。",
    null
  ],
  [
    "military",
    "B2",
    "形容詞・名詞",
    [
      "軍隊の"
    ],
    "/ˈmɪlətɛri/",
    "The government reduced military spending.",
    "政府は軍事支出を減らした。",
    null
  ],
  [
    "mind",
    "A2",
    "名詞・動詞",
    [
      "〜していただけますか",
      "気にする"
    ],
    "/maɪnd/",
    "Would you mind closing the window?",
    "窓を閉めていただけますか。",
    null
  ],
  [
    "mine",
    "A2",
    "名詞",
    [
      "私のもの",
      "私の"
    ],
    "/maɪn/",
    "The seat by the window is mine.",
    "窓際の席は私のものだ。",
    null
  ],
  [
    "miner",
    "B2",
    "名詞",
    [
      "鉱夫"
    ],
    "/ˈmaɪnɚ/",
    "The miner worked deep beneath the ground.",
    "その鉱員は地下深くで働いた。",
    null
  ],
  [
    "mineral",
    "B2",
    "名詞",
    [
      "鉱物",
      "鉱物質を含む"
    ],
    "/ˈmɪnɚəl/",
    "The water contains several useful mineral substances.",
    "その水には複数の有用な鉱物質が含まれる。",
    null
  ],
  [
    "minimum",
    "B2",
    "形容詞・名詞",
    [
      "最低",
      "最小"
    ],
    "/ˈmɪnəməm/",
    "Applicants need a minimum of two years' experience.",
    "応募者には最低2年の経験が必要だ。",
    null
  ],
  [
    "minister",
    "B2",
    "名詞",
    [
      "大臣"
    ],
    "/ˈmɪnəstɚ/",
    "The health minister announced a new program.",
    "保健大臣は新しい制度を発表した。",
    null
  ],
  [
    "minor",
    "B2",
    "形容詞",
    [
      "劣ったほうの"
    ],
    "/ˈmaɪnɚ/",
    "The accident caused only minor damage.",
    "その事故の被害は軽微だった。",
    null
  ],
  [
    "minority",
    "B2",
    "名詞",
    [
      "少数",
      "少数派"
    ],
    "/maɪˈnɔrəti/",
    "Only a small minority opposed the proposal.",
    "提案に反対したのは少数だけだった。",
    null
  ],
  [
    "mirror",
    "A2",
    "名詞",
    [
      "鏡",
      "姿を映す物"
    ],
    "/ˈmɪrɚ/",
    "She checked her reflection in the mirror.",
    "彼女は鏡で自分の姿を確認した。",
    null
  ],
  [
    "miserable",
    "B2",
    "形容詞",
    [
      "つらい",
      "みじめな"
    ],
    "/ˈmɪzɚəbəl/",
    "Cold rain made the journey miserable.",
    "冷たい雨で旅はつらいものになった。",
    null
  ],
  [
    "missing",
    "A2",
    "形容詞",
    [
      "行方不明の",
      "行方不明者"
    ],
    "/ˈmɪsɪŋ/",
    "Police are searching for the missing child.",
    "警察は行方不明の子どもを捜している。",
    null
  ],
  [
    "mission",
    "B2",
    "名詞",
    [
      "使命"
    ],
    "/ˈmɪʃən/",
    "The team's mission is to provide clean water.",
    "そのチームの使命は清潔な水を提供することだ。",
    null
  ],
  [
    "mistake",
    "B2",
    "動詞",
    [
      "間違い",
      "を間違って考える"
    ],
    "/mɪˈsteɪk/",
    "I made a mistake when writing the address on the envelope.",
    "封筒の宛先、書き間違えちゃった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12747145",
      "license": "CC BY 2.0 FR",
      "attribution": "#12747145 (CK) / #11495413 (small_snow)"
    }
  ],
  [
    "mix",
    "B1",
    "名詞・動詞",
    [
      "を混ぜ合わせる",
      "を混ぜ合わせて作る"
    ],
    "/mɪks/",
    "Mix about four cups of white flour with a pinch of salt.",
    "小麦粉約４カップと塩ひとつまみを混ぜる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2369903",
      "license": "CC BY 2.0 FR",
      "attribution": "#2369903 (dalia26) / #2370041 (wakatyann630)"
    }
  ],
  [
    "mixed",
    "B2",
    "形容詞",
    [
      "間違えた",
      "混ざった"
    ],
    "/mɪkst/",
    "She mixed him up with someone else.",
    "彼女は彼を他の誰かとまちがえた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/316515",
      "license": "CC BY 2.0 FR",
      "attribution": "#316515 (CK) / #87193 (Blanka_Meduzo)"
    }
  ],
  [
    "mixture",
    "B1",
    "名詞",
    [
      "混合物",
      "雨と雪の混合"
    ],
    "/ˈmɪkstʃɚ/",
    "A mixture of snow and rain was falling from the sky.",
    "みぞれが降ってきたよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9867958",
      "license": "CC BY 2.0 FR",
      "attribution": "#9867958 (AlanF_US) / #10699237 (small_snow)"
    }
  ],
  [
    "mobile",
    "A2",
    "形容詞・名詞",
    [
      "携帯電話",
      "移動式の"
    ],
    "/ˈmoʊbəl/",
    "Please don't look at your mobile phone while we're eating.",
    "食事中に携帯を見るのやめなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1021048",
      "license": "CC BY 2.0 FR",
      "attribution": "#1021048 (CK) / #1021046 (bunbuku)"
    }
  ],
  [
    "mode",
    "B2",
    "名詞",
    [
      "ア・ラ・モード",
      "方式"
    ],
    "/moʊd/",
    "He always prefers his pie served a la mode.",
    "彼はいつもアイスをのせたパイの方を選ぶんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6206009",
      "license": "CC BY 2.0 FR",
      "attribution": "#6206009 (CarpeLanam) / #9737900 (bunbuku)"
    }
  ],
  [
    "model",
    "B2",
    "動詞",
    [
      "型",
      "申し分のない"
    ],
    "/ˈmɑdəl/",
    "A new model isn't necessarily any better than the older one.",
    "新型だからといって旧型より良いとは限らない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269276",
      "license": "CC BY 2.0 FR",
      "attribution": "#269276 (CK) / #145287 (KK_kaku_)"
    }
  ],
  [
    "modest",
    "B2",
    "形容詞",
    [
      "謙虚な"
    ],
    "/ˈmɑdəst/",
    "The older he grew, the more modest he became.",
    "彼は年をとるにつれて、一層謙虚になった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/302340",
      "license": "CC BY 2.0 FR",
      "attribution": "#302340 (CM) / #101356 (KK_kaku_)"
    }
  ],
  [
    "modify",
    "B2",
    "動詞",
    [
      "を修正する",
      "変更する"
    ],
    "/ˈmɑdəfaɪ/",
    "We may need to modify the design after testing.",
    "試験後に設計を修正する必要があるかもしれない。",
    null
  ],
  [
    "monitor",
    "B2",
    "名詞・動詞",
    [
      "監視する",
      "確認する"
    ],
    "/ˈmɑnətɚ/",
    "Progress is monitored daily and stored in a database.",
    "進行状況は毎日確認され、データベースに記録されます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269850",
      "license": "CC BY 2.0 FR",
      "attribution": "#269850 (CM) / #144714 (KK_kaku_)"
    }
  ],
  [
    "monkey",
    "A2",
    "名詞",
    [
      "猿に似た顔つきの人"
    ],
    "/ˈmʌŋki/",
    "I'm not talking to you. I'm talking to the monkey.",
    "俺はあんたに話し掛けてるんじゃない、猿に話し掛けてるんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2803668",
      "license": "CC BY 2.0 FR",
      "attribution": "#2803668 (CK) / #188380 (bunbuku)"
    }
  ],
  [
    "monster",
    "B2",
    "名詞",
    [
      "怪物"
    ],
    "/ˈmɑnstɚ/",
    "A monster lay on a rock near the top of the mountain.",
    "１頭の怪物が山の頂上の近くの岩に横になっていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73091",
      "license": "CC BY 2.0 FR",
      "attribution": "#73091 (CK) / #235711 (mookeee)"
    }
  ],
  [
    "monthly",
    "B2",
    "形容詞",
    [
      "毎月の"
    ],
    "/ˈmʌnθli/",
    "The monthly staff meeting is never held on Monday.",
    "月一のスタッフミーティングが月曜に行われることはありませんよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238879",
      "license": "CC BY 2.0 FR",
      "attribution": "#238879 (CM) / #10314716 (bunbuku)"
    }
  ],
  [
    "monument",
    "B2",
    "名詞",
    [
      "記念碑",
      "記念像"
    ],
    "/ˈmɑnjumənt/",
    "A monument has been erected to the memory of the deceased.",
    "故人をしのんで、記念碑が建てられた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/239956",
      "license": "CC BY 2.0 FR",
      "attribution": "#239956 (CM) / #174513 (bunbuku)"
    }
  ],
  [
    "mood",
    "B1",
    "名詞",
    [
      "気分"
    ],
    "/mud/",
    "I'm just not in the mood to go out right now.",
    "今は出かける気分じゃないんだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12421049",
      "license": "CC BY 2.0 FR",
      "attribution": "#12421049 (CK) / #1166933 (bunbuku)"
    }
  ],
  [
    "moon",
    "A2",
    "名詞",
    [
      "月"
    ],
    "/mun/",
    "The earth is about six times as large as the moon.",
    "地球は月の約６倍の大きさである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277126",
      "license": "CC BY 2.0 FR",
      "attribution": "#277126 (CK) / #126964 (bunbuku)"
    }
  ],
  [
    "moral",
    "B2",
    "形容詞・名詞",
    [
      "道徳的な",
      "道徳を守る"
    ],
    "/ˈmɔrəl/",
    "My father was religious and he was a very moral man.",
    "私の父は信仰深くて、とても道徳的な人だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/251699",
      "license": "CC BY 2.0 FR",
      "attribution": "#251699 (CK) / #162814 (tommy__san)"
    }
  ],
  [
    "moreover",
    "B2",
    "副詞",
    [
      "さらに",
      "そのうえ"
    ],
    "/mɔˈroʊvɚ/",
    "The route is shorter; moreover, it is safer.",
    "その経路は短く、さらに安全だ。",
    null
  ],
  [
    "mortgage",
    "B2",
    "名詞",
    [
      "住宅ローン",
      "抵当"
    ],
    "/ˈmɔrgədʒ/",
    "They took out a mortgage to buy their first home.",
    "彼らは初めての家を買うため住宅ローンを組んだ。",
    null
  ],
  [
    "mosque",
    "B2",
    "名詞",
    [
      "モスク"
    ],
    "/mɑsk/",
    "They went to the mosque to pray.",
    "彼らはお祈りをするためにモスクに行きました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7828136",
      "license": "CC BY 2.0 FR",
      "attribution": "#7828136 (CK) / #8654344 (small_snow)"
    }
  ],
  [
    "mostly",
    "A2",
    "副詞",
    [
      "ほとんど",
      "主に"
    ],
    "/ˈmoʊstli/",
    "The pain has mostly gone away.",
    "だいぶ痛みがなくなりました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41146",
      "license": "CC BY 2.0 FR",
      "attribution": "#41146 (CK) / #203904 (bunbuku)"
    }
  ],
  [
    "motion",
    "B2",
    "名詞",
    [
      "動き",
      "スローモーション"
    ],
    "/ˈmoʊʃən/",
    "I want to see the scene in slow motion.",
    "その場面をスローモーションで見たいな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/46190",
      "license": "CC BY 2.0 FR",
      "attribution": "#46190 (CK) / #208930 (bunbuku)"
    }
  ],
  [
    "motivate",
    "B2",
    "動詞",
    [
      "動機づける"
    ],
    "/ˈmoʊtəveɪt/",
    "I don't know what motivated me to come here.",
    "どういうはずみでここに来たのか自分でもわからない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/38922",
      "license": "CC BY 2.0 FR",
      "attribution": "#38922 (CK) / #201712 (bunbuku)"
    }
  ],
  [
    "motivation",
    "B2",
    "名詞",
    [
      "意欲",
      "動機"
    ],
    "/moʊtəˈveɪʃən/",
    "Tom has lost his motivation to work.",
    "トムは仕事へのモチベーションを失っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2718452",
      "license": "CC BY 2.0 FR",
      "attribution": "#2718452 (Hybrid) / #2718743 (tommy_san)"
    }
  ],
  [
    "motor",
    "B2",
    "形容詞・名詞",
    [
      "モーター",
      "モーターの"
    ],
    "/ˈmoʊtɚ/",
    "Then the motor suddenly died.",
    "その時、機械のモーターが急に止まった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/47033",
      "license": "CC BY 2.0 FR",
      "attribution": "#47033 (CK) / #209770 (small_snow)"
    }
  ],
  [
    "motorcycle",
    "A2",
    "名詞",
    [
      "オートバイ",
      "オートバイで行く"
    ],
    "/ˈmoʊtɚsaɪkəl/",
    "Who wants to buy a motorcycle with squeaky brakes?",
    "ブレーキがキーキーいうバイクなんて欲しがる人いるわけ？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327265",
      "license": "CC BY 2.0 FR",
      "attribution": "#327265 (CM) / #76455 (mookeee)"
    }
  ],
  [
    "mount",
    "B2",
    "動詞",
    [
      "取り付ける",
      "設置する"
    ],
    "/maʊnt/",
    "The technician will mount the screen securely on the wall.",
    "技術者がスクリーンを壁にしっかり取り付ける。",
    null
  ],
  [
    "move",
    "B1",
    "名詞",
    [
      "引っ越す"
    ],
    "/muv/",
    "Our current house is too small, so we decided to move.",
    "今の家は狭すぎるので、引っ越す事にした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241756",
      "license": "CC BY 2.0 FR",
      "attribution": "#241756 (CM) / #172719 (bunbuku)"
    }
  ],
  [
    "movement",
    "A2",
    "名詞",
    [
      "運動"
    ],
    "/ˈmuvmənt/",
    "She played a part in the women's lib movement.",
    "彼女は婦人解放運動で積極的な役割をした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/316785",
      "license": "CC BY 2.0 FR",
      "attribution": "#316785 (CK) / #86926 (bunbuku)"
    }
  ],
  [
    "moving",
    "B2",
    "形容詞",
    [
      "感動的な",
      "動いている"
    ],
    "/ˈmuvɪŋ/",
    "Her speech was a moving tribute to the volunteers.",
    "彼女のスピーチはボランティアへの感動的な賛辞だった。",
    null
  ],
  [
    "mud",
    "B1",
    "名詞",
    [
      "泥"
    ],
    "/mʌd/",
    "He was covered in mud from head to foot.",
    "彼は全身泥まみれだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/457945",
      "license": "CC BY 2.0 FR",
      "attribution": "#457945 (sacredceltic) / #102921 (bunbuku)"
    }
  ],
  [
    "multiple",
    "B2",
    "形容詞",
    [
      "多数の部分から成る"
    ],
    "/ˈmʌltəpəl/",
    "The problem has multiple possible causes.",
    "その問題には複数の原因が考えられる。",
    null
  ],
  [
    "multiply",
    "B2",
    "動詞",
    [
      "繁殖する",
      "増大する"
    ],
    "/ˈmʌltəplaɪ/",
    "Warm conditions allow these bacteria to multiply quickly.",
    "暖かい環境ではこの細菌が急速に増殖する。",
    null
  ],
  [
    "murder",
    "B1",
    "名詞・動詞",
    [
      "殺害",
      "殺害する"
    ],
    "/ˈmɝdɚ/",
    "You don't have an alibi for the day of the murder.",
    "殺害当日のアリバイがありませんね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/547381",
      "license": "CC BY 2.0 FR",
      "attribution": "#547381 (Swift) / #10893282 (bunbuku)"
    }
  ],
  [
    "muscle",
    "B1",
    "名詞",
    [
      "筋肉",
      "筋"
    ],
    "/ˈmʌsəl/",
    "ALS slowly destroys the nerves and muscles needed for moving your body.",
    "ＡＬＳは、体を動かすのに必要な神経と筋肉を徐々に破壊してしまう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72262",
      "license": "CC BY 2.0 FR",
      "attribution": "#72262 (CK) / #234885 (e4zh1nmcz)"
    }
  ],
  [
    "musical",
    "A2",
    "形容詞・名詞",
    [
      "音楽の",
      "音楽的な"
    ],
    "/mˈjuzɪkəl/",
    "She showed remarkable musical talent at an early age.",
    "彼女は幼い頃から素晴らしい音楽的才能を示した。",
    null
  ],
  [
    "musician",
    "A2",
    "名詞",
    [
      "音楽家"
    ],
    "/mjuˈzɪʃən/",
    "I didn't know that you used to be a professional musician.",
    "プロのミュージシャンだったなんて知らなかったわ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7503991",
      "license": "CC BY 2.0 FR",
      "attribution": "#7503991 (CK) / #13028709 (small_snow)"
    }
  ],
  [
    "myself",
    "A2",
    "名詞",
    [
      "私自身"
    ],
    "/maɪˈsɛlf/",
    "The bag was too heavy for me to carry by myself.",
    "その鞄はとても重くて、一人では運べなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/48892",
      "license": "CC BY 2.0 FR",
      "attribution": "#48892 (CK) / #211616 (KK_kaku_)"
    }
  ],
  [
    "mysterious",
    "B2",
    "形容詞",
    [
      "不思議な"
    ],
    "/mɪˈstɪriəs/",
    "This place has a mysterious atmosphere.",
    "この場所には不思議な雰囲気がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2105",
      "license": "CC BY 2.0 FR",
      "attribution": "#2105 (CK) / #5291 (bunbuku)"
    }
  ],
  [
    "mystery",
    "B1",
    "名詞",
    [
      "謎"
    ],
    "/ˈmɪstɚi/",
    "It is a mystery how they escaped from prison.",
    "彼らがどうやって脱獄したのかは謎だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/304946",
      "license": "CC BY 2.0 FR",
      "attribution": "#304946 (CM) / #98754 (KK_kaku_)"
    }
  ],
  [
    "myth",
    "B2",
    "名詞",
    [
      "神話",
      "神話的な人"
    ],
    "/mɪθ/",
    "He wrote a novel based on ancient myths.",
    "彼は古代神話に基づく小説を書いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/296138",
      "license": "CC BY 2.0 FR",
      "attribution": "#296138 (CM) / #107548 (tommy__san)"
    }
  ],
  [
    "nail",
    "B1",
    "名詞",
    [
      "爪",
      "くぎ"
    ],
    "/neɪl/",
    "I'm looking for a lipstick to go with this nail polish.",
    "このマニキュアに合う色の口紅を探しているんですけれど。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/60466",
      "license": "CC BY 2.0 FR",
      "attribution": "#60466 (CK) / #223135 (small_snow)"
    }
  ],
  [
    "naked",
    "B2",
    "形容詞",
    [
      "肉眼の"
    ],
    "/ˈneɪkəd/",
    "Some stars are hardly visible to the naked eye.",
    "肉眼ではほとんど見えない星もある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/281024",
      "license": "CC BY 2.0 FR",
      "attribution": "#281024 (CM) / #122978 (KK_kaku_)"
    }
  ],
  [
    "narrative",
    "B1",
    "形容詞・名詞",
    [
      "物語",
      "物語の"
    ],
    "/ˈnærətɪv/",
    "The documentary presents a clear narrative of events.",
    "その記録映画は出来事を明確な物語として示す。",
    null
  ],
  [
    "narrow",
    "A2",
    "形容詞・動詞",
    [
      "狭い"
    ],
    "/ˈnɛroʊ/",
    "That road is too narrow for a car to drive on.",
    "その道は車が通るには狭すぎる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1051740",
      "license": "CC BY 2.0 FR",
      "attribution": "#1051740 (CK) / #1051731 (bunbuku)"
    }
  ],
  [
    "nasty",
    "B2",
    "形容詞",
    [
      "いやな"
    ],
    "/ˈnæsti/",
    "I can't stand that nasty attitude of his any longer.",
    "私は彼のあのいやな態度にはもはや我慢できない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/31630",
      "license": "CC BY 2.0 FR",
      "attribution": "#31630 (CK) / #154037 (mookeee)"
    }
  ],
  [
    "nation",
    "B1",
    "名詞",
    [
      "国民",
      "国"
    ],
    "/ˈneɪʃən/",
    "The nation as a whole is in favor of political reform.",
    "全体として国民は政治改革に賛成である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273797",
      "license": "CC BY 2.0 FR",
      "attribution": "#273797 (CK) / #140776 (bunbuku)"
    }
  ],
  [
    "national",
    "A2",
    "形容詞・名詞",
    [
      "国の",
      "国立の"
    ],
    "/ˈnæʃənəl/",
    "Did you listen to the broadcast of the National Diet's debate?",
    "国会討論の放送を聞きましたか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1341092",
      "license": "CC BY 2.0 FR",
      "attribution": "#1341092 (CK) / #173070 (mookeee)"
    }
  ],
  [
    "native",
    "B1",
    "形容詞・名詞",
    [
      "母語話者の",
      "生まれつきの"
    ],
    "/ˈneɪtɪv/",
    "All the English teachers at my son's school are native speakers.",
    "息子の学校の英語教師はみんなネイティブだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/953088",
      "license": "CC BY 2.0 FR",
      "attribution": "#953088 (CK) / #997180 (mookeee)"
    }
  ],
  [
    "naturally",
    "B1",
    "副詞",
    [
      "自然に",
      "自然の力で"
    ],
    "/ˈnætʃɚəli/",
    "He just naturally avoids everything that is intense, difficult or strenuous.",
    "彼はただ、きついこと、難しいこと、骨の折れることを全て、自然に避けるのです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/847225",
      "license": "CC BY 2.0 FR",
      "attribution": "#847225 (Source_Benedict_1921) / #893242 (thyc244)"
    }
  ],
  [
    "nature",
    "A2",
    "名詞",
    [
      "性質",
      "自然"
    ],
    "/ˈneɪtʃɚ/",
    "It is not in his nature to be hard on other people.",
    "彼は他人につらく当たることができない性格です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/301068",
      "license": "CC BY 2.0 FR",
      "attribution": "#301068 (CM) / #102625 (tommy__san)"
    }
  ],
  [
    "navigation",
    "B2",
    "名詞",
    [
      "航海術"
    ],
    "/ˈnævəˈgeɪʃən/",
    "Early explorers used the stars for navigation.",
    "昔の探検家たちは航海するのに星を利用した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/272150",
      "license": "CC BY 2.0 FR",
      "attribution": "#272150 (CK) / #142420 (bunbuku)"
    }
  ],
  [
    "nearby",
    "B2",
    "形容詞・副詞",
    [
      "近くに",
      "近くの"
    ],
    "/ˈnɪrˈbaɪ/",
    "There's a restaurant I frequent nearby. Let's have lunch there today.",
    "近所に行きつけの店があるから、今日はそこでランチを食べよう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12782009",
      "license": "CC BY 2.0 FR",
      "attribution": "#12782009 (CK) / #179814 (KK_kaku_)"
    }
  ],
  [
    "nearly",
    "A2",
    "副詞",
    [
      "もう少しで",
      "ほとんど"
    ],
    "/ˈnɪrli/",
    "Her brother nearly died in a traffic accident nine years ago.",
    "９年前、彼女のお兄さんは交通事故で危うく命を落とすところでした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72273",
      "license": "CC BY 2.0 FR",
      "attribution": "#72273 (CK) / #234896 (e4zh1nmcz)"
    }
  ],
  [
    "neat",
    "B2",
    "形容詞",
    [
      "きちんと整った"
    ],
    "/nit/",
    "He always keeps his room as neat as a pin.",
    "彼はいつも部屋をきちんと整頓している。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/289208",
      "license": "CC BY 2.0 FR",
      "attribution": "#289208 (CM) / #114463 (bunbuku)"
    }
  ],
  [
    "necessarily",
    "B1",
    "副詞",
    [
      "必ずしも"
    ],
    "/nɛsəˈsɛrəli/",
    "A new model isn't necessarily any better than the older one.",
    "新型だからといって旧型より良いとは限らない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269276",
      "license": "CC BY 2.0 FR",
      "attribution": "#269276 (CK) / #145287 (KK_kaku_)"
    }
  ],
  [
    "necessary",
    "A2",
    "形容詞",
    [
      "必要な"
    ],
    "/ˈnɛsəsɛri/",
    "It wasn't really necessary for me to come here by taxi.",
    "ここに来るのに、別にタクシー使う必要なんかなかったな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10314721",
      "license": "CC BY 2.0 FR",
      "attribution": "#10314721 (CK) / #10314729 (bunbuku)"
    }
  ],
  [
    "necessity",
    "B2",
    "名詞",
    [
      "必要",
      "必要品どうしても必要なもの"
    ],
    "/nəˈsɛsəti/",
    "There is no necessity for you to do that.",
    "そんなことする必要ないよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/71574",
      "license": "CC BY 2.0 FR",
      "attribution": "#71574 (CM) / #10300453 (bunbuku)"
    }
  ],
  [
    "neck",
    "A2",
    "名詞",
    [
      "首"
    ],
    "/nɛk/",
    "Even though the accident was six months ago, my neck still hurts.",
    "事故ったのは半年前なのに、未だに首が痛むよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/892402",
      "license": "CC BY 2.0 FR",
      "attribution": "#892402 (Scott) / #891342 (bunbuku)"
    }
  ],
  [
    "need",
    "A2",
    "名詞・動詞",
    [
      "する必要がある"
    ],
    "/nid/",
    "We have a lot of things that need to be done.",
    "我々のすべきことはたくさんある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4497456",
      "license": "CC BY 2.0 FR",
      "attribution": "#4497456 (CK) / #991790 (mookeee)"
    }
  ],
  [
    "needle",
    "B1",
    "名詞",
    [
      "針",
      "とがった山頂"
    ],
    "/ˈnidəl/",
    "My grandma bent over to pick up a needle and thread.",
    "おばあちゃんは身をかがめて糸の付いた針を拾った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/250266",
      "license": "CC BY 2.0 FR",
      "attribution": "#250266 (CM) / #164243 (bunbuku)"
    }
  ],
  [
    "negative",
    "B2",
    "名詞",
    [
      "否定",
      "否定の"
    ],
    "/ˈnɛgətɪv/",
    "I've been having a lot of negative thoughts lately.",
    "最近、否定的なことばかり考えてしまう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10288759",
      "license": "CC BY 2.0 FR",
      "attribution": "#10288759 (ddnktr) / #13028880 (small_snow)"
    }
  ],
  [
    "negotiate",
    "B2",
    "動詞",
    [
      "協定する",
      "を売却する"
    ],
    "/nəˈgoʊʃieɪt/",
    "The two countries will negotiate a settlement to the crisis.",
    "両国は危機解決に向けて交渉をするでしょう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325614",
      "license": "CC BY 2.0 FR",
      "attribution": "#325614 (CM) / #78104 (mookeee)"
    }
  ],
  [
    "negotiation",
    "B2",
    "名詞",
    [
      "交渉"
    ],
    "/nɪgoʊʃiˈeɪʃən/",
    "The negotiation has entered upon a serious phase.",
    "交渉は大事な局面を迎えた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/240295",
      "license": "CC BY 2.0 FR",
      "attribution": "#240295 (CM) / #174175 (bunbuku)"
    }
  ],
  [
    "neighbourhood",
    "B1",
    "名詞",
    [
      "近所",
      "近所の人々"
    ],
    "/ˈneɪbɚhʊd/",
    "A new clinic opened in our neighbourhood.",
    "近所に新しい診療所が開いた。",
    null
  ],
  [
    "neither",
    "A2",
    "副詞・限定詞・名詞",
    [
      "また…もしない"
    ],
    "/ˈniðɚ/",
    "It was a long war because neither side would give in.",
    "双方が降参しようとしなかったので、長い戦争となった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273973",
      "license": "CC BY 2.0 FR",
      "attribution": "#273973 (CK) / #140600 (bunbuku)"
    }
  ],
  [
    "nerve",
    "B2",
    "名詞",
    [
      "勇気",
      "神経"
    ],
    "/nɝv/",
    "I haven't got the nerve to ask you for a loan.",
    "いくら図々しくても借金は君に頼めないよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66514",
      "license": "CC BY 2.0 FR",
      "attribution": "#66514 (CM) / #229156 (bunbuku)"
    }
  ],
  [
    "nervous",
    "A2",
    "形容詞",
    [
      "緊張した",
      "神経の"
    ],
    "/ˈnɝvəs/",
    "She has the habit of clearing her throat whenever she's nervous.",
    "彼女は自信のないときに咳払いをする癖がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/729928",
      "license": "CC BY 2.0 FR",
      "attribution": "#729928 (darinmex) / #1795104 (Akatsuki)"
    }
  ],
  [
    "net",
    "B1",
    "名詞",
    [
      "網",
      "を網で捕らえる"
    ],
    "/nɛt/",
    "The boy captured the bird with a net.",
    "少年はその鳥を網で捕まえた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267981",
      "license": "CC BY 2.0 FR",
      "attribution": "#267981 (CK) / #146581 (bunbuku)"
    }
  ],
  [
    "network",
    "A2",
    "名詞",
    [
      "人脈",
      "ネットワーク"
    ],
    "/ˈnɛtwɝk/",
    "He's building up a network of acquaintances outside his office.",
    "彼は社外で人脈を築いている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/299004",
      "license": "CC BY 2.0 FR",
      "attribution": "#299004 (CM) / #104686 (mookeee)"
    }
  ],
  [
    "neutral",
    "B2",
    "形容詞",
    [
      "中立の",
      "中立国の"
    ],
    "/ˈnutrəl/",
    "Wouldn't it be great if a gender-neutral pronoun for \"he\" or \"she\" existed in English?",
    "英語に\"he\"や\"she\"に代わる性別中立的な代名詞があれば良いことではないですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/544637",
      "license": "CC BY 2.0 FR",
      "attribution": "#544637 (CK) / #4715122 (anhgosho)"
    }
  ],
  [
    "nevertheless",
    "B2",
    "副詞",
    [
      "それでもやはり"
    ],
    "/nɛvɚðəˈlɛs/",
    "I was very tired, but I was nevertheless unable to sleep.",
    "私は疲れていたのに眠れなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/261396",
      "license": "CC BY 2.0 FR",
      "attribution": "#261396 (CM) / #2256974 (tommy_san)"
    }
  ],
  [
    "newly",
    "B2",
    "副詞",
    [
      "新しく"
    ],
    "/ˈnuli/",
    "Why on earth did you sell your newly-built house?",
    "一体全体どうして新築した家を売ってしまったんですか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/27507",
      "license": "CC BY 2.0 FR",
      "attribution": "#27507 (CK) / #190349 (bunbuku)"
    }
  ],
  [
    "next",
    "B1",
    "名詞",
    [
      "隣の",
      "次の"
    ],
    "/nɛkst/",
    "The man who lives next door to me is a doctor.",
    "私の隣に住んでいる人は医者です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/252100",
      "license": "CC BY 2.0 FR",
      "attribution": "#252100 (Zifre) / #162414 (mookeee)"
    }
  ],
  [
    "nightmare",
    "B2",
    "名詞",
    [
      "悪夢のような経験"
    ],
    "/ˈnaɪtmɛr/",
    "It was a scary movie. I think I'll have nightmares about it tonight.",
    "怖い映画だったな。なんか今晩夢でうなされそう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/892386",
      "license": "CC BY 2.0 FR",
      "attribution": "#892386 (Scott) / #891800 (bunbuku)"
    }
  ],
  [
    "noise",
    "A2",
    "名詞",
    [
      "騒音",
      "音"
    ],
    "/nɔɪz/",
    "It took a long time to accustom myself to the noise.",
    "その騒音に慣れるのに長い時間がかかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/45595",
      "license": "CC BY 2.0 FR",
      "attribution": "#45595 (CM) / #208338 (KK_kaku_)"
    }
  ],
  [
    "noisy",
    "A2",
    "形容詞",
    [
      "やかましい"
    ],
    "/ˈnɔɪzi/",
    "It was so noisy there that I couldn't make myself heard.",
    "そこはとても騒がしかったので、私の言うことを聞き取ってもらえなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/50910",
      "license": "CC BY 2.0 FR",
      "attribution": "#50910 (CK) / #1142001 (bunbuku)"
    }
  ],
  [
    "none",
    "A2",
    "名詞",
    [
      "どれも",
      "だれも"
    ],
    "/nʌn/",
    "We have three spare rooms, none of which can be used.",
    "空き部屋は三つありますが、どれも使用できません。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18335",
      "license": "CC BY 2.0 FR",
      "attribution": "#18335 (Zifre) / #1568240 (bunbuku)"
    }
  ],
  [
    "nor",
    "B1",
    "副詞・接続詞",
    [
      "も",
      "も…ない"
    ],
    "/nɔr/",
    "The ice cream was neither good nor bad. It was just sweet.",
    "アイスは美味しくも不味くもなく、ただ甘かった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11014555",
      "license": "CC BY 2.0 FR",
      "attribution": "#11014555 (CK) / #11014007 (KK_kaku_)"
    }
  ],
  [
    "norm",
    "B2",
    "名詞",
    [
      "標準"
    ],
    "/nɔrm/",
    "Remote work has become the norm in some industries.",
    "一部の業界では在宅勤務が標準になった。",
    null
  ],
  [
    "normal",
    "A2",
    "形容詞・名詞",
    [
      "正常な"
    ],
    "/ˈnɔrməl/",
    "You'll be back to normal in a couple of days.",
    "２、３日したら元どおり元気になるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12812903",
      "license": "CC BY 2.0 FR",
      "attribution": "#12812903 (CK) / #235628 (wakatyann630)"
    }
  ],
  [
    "normally",
    "A2",
    "副詞",
    [
      "正常に"
    ],
    "/ˈnɔrməli/",
    "People normally breathe 12 to 20 times a minute.",
    "人は一分間に通常12回から20回呼吸をする。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/680421",
      "license": "CC BY 2.0 FR",
      "attribution": "#680421 (Source_VOA) / #2099996 (bunbuku)"
    }
  ],
  [
    "northern",
    "B1",
    "形容詞",
    [
      "河にある",
      "北部特有の"
    ],
    "/ˈnɔrðɚn/",
    "My house is in the northern part of the city.",
    "私の家は市の北部にある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/935814",
      "license": "CC BY 2.0 FR",
      "attribution": "#935814 (CK) / #163957 (bunbuku)"
    }
  ],
  [
    "note",
    "B1",
    "動詞",
    [
      "について言う"
    ],
    "/noʊt/",
    "Please put a sticky note on any part that needs changed.",
    "修正が必要な箇所には、付箋を貼っておいてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13569929",
      "license": "CC BY 2.0 FR",
      "attribution": "#13569929 (CK) / #12135714 (small_snow)"
    }
  ],
  [
    "notebook",
    "B2",
    "名詞",
    [
      "ノート"
    ],
    "/ˈnoʊtbʊk/",
    "I copied in my notebook whatever he wrote on the blackboard.",
    "彼が黒板に書くことはすべてノートに写した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/283641",
      "license": "CC BY 2.0 FR",
      "attribution": "#283641 (CK) / #120368 (bunbuku)"
    }
  ],
  [
    "notice",
    "A2",
    "名詞・動詞",
    [
      "通知",
      "届け出"
    ],
    "/ˈnoʊtəs/",
    "You may not set up a roadside stall without prior notice.",
    "届け出なしに路上に出店してはならない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327884",
      "license": "CC BY 2.0 FR",
      "attribution": "#327884 (CM) / #75834 (bunbuku)"
    }
  ],
  [
    "notion",
    "B2",
    "名詞",
    [
      "考え",
      "概念"
    ],
    "/ˈnoʊʃən/",
    "I had no notion that you were coming.",
    "君がくるとは思わなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18043",
      "license": "CC BY 2.0 FR",
      "attribution": "#18043 (Zifre) / #179187 (KK_kaku_)"
    }
  ],
  [
    "novel",
    "A2",
    "名詞",
    [
      "小説"
    ],
    "/ˈnɑvəl/",
    "Novels aren't being read as much as they used to be.",
    "小説は以前ほど読まれていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1164066",
      "license": "CC BY 2.0 FR",
      "attribution": "#1164066 (Chrikaru) / #146939 (tommy__san)"
    }
  ],
  [
    "novelist",
    "B2",
    "名詞",
    [
      "小説家"
    ],
    "/ˈnɑvələst/",
    "He is not so much a novelist as a poet.",
    "彼は小説家というよりはむしろ詩人だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/299559",
      "license": "CC BY 2.0 FR",
      "attribution": "#299559 (CM) / #237321 (mookeee)"
    }
  ],
  [
    "now",
    "B1",
    "接続詞",
    [
      "今"
    ],
    "/naʊ/",
    "A lot of people are now trying to sell their houses.",
    "たくさんの人が今家を売りたがっている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/953077",
      "license": "CC BY 2.0 FR",
      "attribution": "#953077 (CK) / #997168 (mookeee)"
    }
  ],
  [
    "nowadays",
    "B2",
    "副詞",
    [
      "今日では"
    ],
    "/ˈnaʊədeɪz/",
    "Nowadays it is not unusual for a woman to travel alone.",
    "最近では、女性が一人旅をするのは珍しいことではない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/243769",
      "license": "CC BY 2.0 FR",
      "attribution": "#243769 (CK) / #170712 (bunbuku)"
    }
  ],
  [
    "nowhere",
    "A2",
    "副詞",
    [
      "どこにも…ない",
      "どこにもない場所"
    ],
    "/ˈnoʊwɛr/",
    "That kind of talk will get you nowhere.",
    "その手の話は、何の役にも立たないよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/49763",
      "license": "CC BY 2.0 FR",
      "attribution": "#49763 (CM) / #11167365 (bunbuku)"
    }
  ],
  [
    "nuclear",
    "B1",
    "形容詞",
    [
      "核の"
    ],
    "/ˈnukliɚ/",
    "All humanity will suffer if a nuclear war breaks out.",
    "核戦争が起きれば、全人類が被害を受けるだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21731",
      "license": "CC BY 2.0 FR",
      "attribution": "#21731 (minshirui) / #184602 (mookeee)"
    }
  ],
  [
    "number",
    "A2",
    "動詞",
    [
      "数",
      "数の上の優勢"
    ],
    "/ˈnʌmbɚ/",
    "A number of cars are parked in front of my house.",
    "家の前に多数の車が駐車している。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/24169",
      "license": "CC BY 2.0 FR",
      "attribution": "#24169 (CK) / #187032 (bunbuku)"
    }
  ],
  [
    "numerous",
    "B2",
    "形容詞",
    [
      "多数から成る"
    ],
    "/ˈnumɚəs/",
    "We've made numerous improvements to our house since we bought it.",
    "家を購入してからいろいろ手直しをしてきた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7803613",
      "license": "CC BY 2.0 FR",
      "attribution": "#7803613 (CK) / #186990 (bunbuku)"
    }
  ],
  [
    "nursing",
    "B2",
    "名詞",
    [
      "看護"
    ],
    "/ˈnɝsɪŋ/",
    "She is studying nursing at college.",
    "彼女は大学で看護学を学んでいる。",
    null
  ],
  [
    "nut",
    "A2",
    "名詞",
    [
      "ナット"
    ],
    "/nʌt/",
    "Squirrels eat seeds and nuts, as well as insects and mushrooms.",
    "リスは種やナッツ、そして虫やキノコも食べます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2761168",
      "license": "CC BY 2.0 FR",
      "attribution": "#2761168 (Hybrid) / #8933462 (small_snow)"
    }
  ],
  [
    "nutrition",
    "B2",
    "名詞",
    [
      "栄養摂取",
      "栄養分"
    ],
    "/nuˈtrɪʃən/",
    "Good nutrition is essential for children's growth.",
    "よい栄養は子どもの成長に不可欠だ。",
    null
  ],
  [
    "obesity",
    "B2",
    "名詞",
    [
      "肥満"
    ],
    "/oʊˈbisəti/",
    "The campaign raises awareness of childhood obesity.",
    "その運動は子どもの肥満への認識を高める。",
    null
  ],
  [
    "obey",
    "B2",
    "動詞",
    [
      "に従う",
      "命令に従う"
    ],
    "/oʊˈbeɪ/",
    "It's our duty to always obey the law.",
    "我々はいつでも法律に従う義務があります。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/696746",
      "license": "CC BY 2.0 FR",
      "attribution": "#696746 (CK) / #686565 (arihato)"
    }
  ],
  [
    "object",
    "B2",
    "動詞",
    [
      "物"
    ],
    "/ˈɑbdʒɛkt/",
    "She had a little round object in her hand.",
    "彼女は手に小さな丸いものを持っていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/314871",
      "license": "CC BY 2.0 FR",
      "attribution": "#314871 (Hellerick) / #88836 (mookeee)"
    }
  ],
  [
    "objective",
    "B2",
    "形容詞・名詞",
    [
      "目標"
    ],
    "/əbˈdʒɛktɪv/",
    "You seem to have lost sight of original objective.",
    "あなたは最初の目標を見失っているようです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/69400",
      "license": "CC BY 2.0 FR",
      "attribution": "#69400 (CK) / #232032 (bunbuku)"
    }
  ],
  [
    "obligation",
    "B2",
    "名詞",
    [
      "義務"
    ],
    "/ɑbləˈgeɪʃən/",
    "We have a legal obligation to pay our taxes.",
    "私達は税金を払う義務がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/263106",
      "license": "CC BY 2.0 FR",
      "attribution": "#263106 (CK) / #151450 (tommy__san)"
    }
  ],
  [
    "observation",
    "B2",
    "名詞",
    [
      "観察",
      "観察すること"
    ],
    "/ɑbzɚˈveɪʃən/",
    "A careful observation will show you the difference.",
    "注意深く観察すれば違いがわかるでしょう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277656",
      "license": "CC BY 2.0 FR",
      "attribution": "#277656 (CM) / #126335 (bunbuku)"
    }
  ],
  [
    "observe",
    "B2",
    "動詞",
    [
      "を観察する",
      "注意して見る"
    ],
    "/əbˈzɝv/",
    "Just observe your cat and you will get to know him.",
    "猫をよく観察してみなさい。そうすればよくその猫のことがわかりますよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/64235",
      "license": "CC BY 2.0 FR",
      "attribution": "#64235 (CM) / #121921 (bunbuku)"
    }
  ],
  [
    "observer",
    "B2",
    "名詞",
    [
      "観察する人"
    ],
    "/əbˈzɝvɚ/",
    "An independent observer attended the election count.",
    "独立した監視員が開票に立ち会った。",
    null
  ],
  [
    "obstacle",
    "B2",
    "名詞",
    [
      "障害"
    ],
    "/ˈɑbstəkəl/",
    "The obstacles to our progress have been removed at last.",
    "われわれの前進を妨げる障害がやっと取り除かれた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/28882",
      "license": "CC BY 2.0 FR",
      "attribution": "#28882 (CM) / #191719 (mookeee)"
    }
  ],
  [
    "obtain",
    "B2",
    "動詞",
    [
      "手に入れる"
    ],
    "/əbˈteɪn/",
    "Where can I obtain a map of Europe?",
    "ヨーロッパの地図はどこで手に入りますか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/38099",
      "license": "CC BY 2.0 FR",
      "attribution": "#38099 (CM) / #10798120 (bunbuku)"
    }
  ],
  [
    "obvious",
    "B1",
    "形容詞",
    [
      "明白な"
    ],
    "/ˈɑbviəs/",
    "It was obvious that those two women knew each other well.",
    "その二人の女性が互いをよく知っているのは明白だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7768161",
      "license": "CC BY 2.0 FR",
      "attribution": "#7768161 (metcaslix) / #4214938 (User66813)"
    }
  ],
  [
    "obviously",
    "B1",
    "副詞",
    [
      "明らかに"
    ],
    "/ˈɑbviəsli/",
    "Someone is obviously telling a lie.",
    "明らかに誰かが嘘をついている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322994",
      "license": "CC BY 2.0 FR",
      "attribution": "#322994 (CK) / #80721 (bunbuku)"
    }
  ],
  [
    "occasion",
    "B1",
    "名詞",
    [
      "場合",
      "必要"
    ],
    "/əˈkeɪʒən/",
    "He can mask his feeling if the occasion calls for it.",
    "必要な場合があれば彼は自分の感情をかくすことができる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318270",
      "license": "CC BY 2.0 FR",
      "attribution": "#318270 (CM) / #85443 (mookeee)"
    }
  ],
  [
    "occasionally",
    "B2",
    "副詞",
    [
      "たまに"
    ],
    "/əˈkeɪʒənəli/",
    "Instead of just reading books all the time, go outside occasionally and get some exercise.",
    "本ばっかり読んでないで、たまには外で体を動かしてきなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12744870",
      "license": "CC BY 2.0 FR",
      "attribution": "#12744870 (CK) / #894775 (bunbuku)"
    }
  ],
  [
    "occupation",
    "B2",
    "名詞",
    [
      "職業"
    ],
    "/ɑkjəˈpeɪʃən/",
    "Please state your occupation on the form.",
    "用紙に職業を記入してください。",
    null
  ],
  [
    "occupy",
    "B2",
    "動詞",
    [
      "を占める",
      "占める"
    ],
    "/ˈɑkjəpaɪ/",
    "The new offices occupy the top three floors.",
    "新しい事務所は上の3階を占めている。",
    null
  ],
  [
    "occur",
    "B1",
    "動詞",
    [
      "起こる"
    ],
    "/əˈkɝ/",
    "Most car accidents occur due to the inattention of the driver.",
    "自動車事故の多くが、ドライバーの注意散漫が原因で起きている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/471863",
      "license": "CC BY 2.0 FR",
      "attribution": "#471863 (blay_paul) / #469636 (qahwa)"
    }
  ],
  [
    "ocean",
    "A2",
    "名詞",
    [
      "大洋"
    ],
    "/ˈoʊʃən/",
    "We flew over the Pacific Ocean for a few hours.",
    "私たちは太平洋上空を２、３時間飛んだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10742981",
      "license": "CC BY 2.0 FR",
      "attribution": "#10742981 (CK) / #165476 (bunbuku)"
    }
  ],
  [
    "odd",
    "B1",
    "形容詞",
    [
      "奇妙な"
    ],
    "/ɑd/",
    "Don't you think it odd that she was in such a hurry?",
    "彼女があんなに急いでいたのは変だと思わないかい？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/308077",
      "license": "CC BY 2.0 FR",
      "attribution": "#308077 (CM) / #95628 (bunbuku)"
    }
  ],
  [
    "offence",
    "B2",
    "名詞",
    [
      "悪気",
      "犯罪",
      "違反"
    ],
    "/əˈfens/",
    "I'm sorry, I meant no offence.",
    "すいません、悪気はなかったんです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2542353",
      "license": "CC BY 2.0 FR",
      "attribution": "#2542353 (CK) / #3555725 (arnab)"
    }
  ],
  [
    "offend",
    "B2",
    "動詞",
    [
      "を恐らせる"
    ],
    "/əˈfɛnd/",
    "I didn't mean to offend you.",
    "怒らせるつもりはなかったんだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2282414",
      "license": "CC BY 2.0 FR",
      "attribution": "#2282414 (Hybrid) / #9641272 (small_snow)"
    }
  ],
  [
    "offender",
    "B2",
    "名詞",
    [
      "違反者"
    ],
    "/əˈfɛndɚ/",
    "The court ordered the offender to pay a fine.",
    "裁判所は違反者に罰金の支払いを命じた。",
    null
  ],
  [
    "offensive",
    "B2",
    "形容詞",
    [
      "攻撃",
      "攻撃の"
    ],
    "/əˈfɛnsɪv/",
    "The general decided to launch an offensive against the enemy camp.",
    "大将は敵陣に攻撃をかける決断を下した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275731",
      "license": "CC BY 2.0 FR",
      "attribution": "#275731 (CM) / #137505 (KK_kaku_)"
    }
  ],
  [
    "offer",
    "A2",
    "名詞・動詞",
    [
      "提供する",
      "申し出る"
    ],
    "/ˈɔfɚ/",
    "How many flights to New York do you offer a day?",
    "ニューヨーク行きは１日に何便ありますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/35882",
      "license": "CC BY 2.0 FR",
      "attribution": "#35882 (CM) / #198689 (bunbuku)"
    }
  ],
  [
    "officer",
    "A2",
    "名詞",
    [
      "警官"
    ],
    "/ˈɔfəsɚ/",
    "The police officer asked me what my name was.",
    "わたしは警官に名前を聞かれました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2953364",
      "license": "CC BY 2.0 FR",
      "attribution": "#2953364 (CK) / #10899800 (small_snow)"
    }
  ],
  [
    "official",
    "B1",
    "形容詞・名詞",
    [
      "公式の",
      "正式の"
    ],
    "/əˈfɪʃəl/",
    "His official title is Director-General of the Environment Agency.",
    "彼の公式の肩書きは環境庁長官です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/286189",
      "license": "CC BY 2.0 FR",
      "attribution": "#286189 (bluepie88) / #117475 (mookeee)"
    }
  ],
  [
    "oil",
    "A2",
    "名詞",
    [
      "油"
    ],
    "/ɔɪl/",
    "Oil has played an important part in the progress of civilization.",
    "石油は文明の発達において重要な役割を果たしてきた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/272259",
      "license": "CC BY 2.0 FR",
      "attribution": "#272259 (CK) / #142311 (mookeee)"
    }
  ],
  [
    "old-fashioned",
    "B1",
    "形容詞",
    [
      "旧式の"
    ],
    "/oʊld ˈfæʃənd/",
    "It looks like an old-fashioned general store.",
    "昔ながらの雑貨屋という店構えだね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11777043",
      "license": "CC BY 2.0 FR",
      "attribution": "#11777043 (pip) / #11030869 (small_snow)"
    }
  ],
  [
    "once",
    "B1",
    "接続詞",
    [
      "1度"
    ],
    "/wʌns/",
    "We used to go to Boston at least once a month.",
    "月に1度はボストンに行ってたものだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6235922",
      "license": "CC BY 2.0 FR",
      "attribution": "#6235922 (CK) / #11559570 (small_snow)"
    }
  ],
  [
    "ongoing",
    "B2",
    "形容詞",
    [
      "進行中の"
    ],
    "/ˈɑngoʊɪŋ/",
    "The road remains closed because of ongoing repairs.",
    "継続中の修理のため道路は閉鎖されたままだ。",
    null
  ],
  [
    "onto",
    "A2",
    "前置詞",
    [
      "に気づいて"
    ],
    "/ˈɑntu/",
    "It is dangerous to jump onto a moving train.",
    "動いている列車に飛び乗るのは危険である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/280200",
      "license": "CC BY 2.0 FR",
      "attribution": "#280200 (CM) / #123795 (tommy__san)"
    }
  ],
  [
    "opening",
    "B2",
    "名詞",
    [
      "開館",
      "開始"
    ],
    "/ˈoʊpənɪŋ/",
    "The gallery attracted a large crowd on its opening day.",
    "その画廊は開館日に大勢の人を集めた。",
    null
  ],
  [
    "openly",
    "B2",
    "副詞",
    [
      "あからさまに"
    ],
    "/ˈoʊpənli/",
    "He openly confessed his faults.",
    "彼は過ちをあからさまに白状した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/284999",
      "license": "CC BY 2.0 FR",
      "attribution": "#284999 (CM) / #118664 (Blanka_Meduzo)"
    }
  ],
  [
    "opera",
    "B2",
    "名詞",
    [
      "オペラ"
    ],
    "/ˈɑprə/",
    "Have you ever heard this opera sung in Italian?",
    "あなたはこのオペラがイタリア語で歌われるのを聞いたことがありますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/70105",
      "license": "CC BY 2.0 FR",
      "attribution": "#70105 (CK) / #232735 (mookeee)"
    }
  ],
  [
    "operate",
    "B2",
    "動詞",
    [
      "作動する",
      "作用する"
    ],
    "/ˈɑpɚeɪt/",
    "The doctor decided to operate at once.",
    "医者はすぐ手術することにした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/28013",
      "license": "CC BY 2.0 FR",
      "attribution": "#28013 (CK) / #190853 (bunbuku)"
    }
  ],
  [
    "operation",
    "B1",
    "名詞",
    [
      "手術",
      "動いている状態"
    ],
    "/ɑpɚˈeɪʃən/",
    "Her mother is going to undergo a major operation next week.",
    "彼女の母は来週大きな手術を受けることになっている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309751",
      "license": "CC BY 2.0 FR",
      "attribution": "#309751 (CK) / #93955 (bunbuku)"
    }
  ],
  [
    "operator",
    "B2",
    "名詞",
    [
      "電話交換手"
    ],
    "/ˈɑpɚeɪtɚ/",
    "The operator told me to hang up and wait for a moment.",
    "交換手は私に電話を切って少し待つように言った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/240276",
      "license": "CC BY 2.0 FR",
      "attribution": "#240276 (CK) / #236917 (bunbuku)"
    }
  ],
  [
    "opponent",
    "B2",
    "名詞",
    [
      "相手",
      "相手の"
    ],
    "/əˈpoʊnənt/",
    "They did not like the way he threatened his opponents.",
    "対戦相手を脅すという彼のやり方を彼らは気に入らなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/802711",
      "license": "CC BY 2.0 FR",
      "attribution": "#802711 (Source_VOA) / #1766823 (bunbuku)"
    }
  ],
  [
    "opportunity",
    "A2",
    "名詞",
    [
      "機会"
    ],
    "/ɑpɚˈtunəti/",
    "This is a good opportunity to get to know one another.",
    "これはお互いを知る良い機会だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/56027",
      "license": "CC BY 2.0 FR",
      "attribution": "#56027 (CK) / #218712 (bunbuku)"
    }
  ],
  [
    "oppose",
    "B2",
    "動詞",
    [
      "に反対する"
    ],
    "/əˈpoʊz/",
    "More than half of the residents are opposed to the plan.",
    "住民の半数以上はその計画に反対だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1133534",
      "license": "CC BY 2.0 FR",
      "attribution": "#1133534 (CK) / #148078 (tommy__san)"
    }
  ],
  [
    "opposed",
    "B2",
    "形容詞",
    [
      "反対して"
    ],
    "/əˈpoʊzd/",
    "More than half of the residents are opposed to the plan.",
    "住民の半数以上はその計画に反対だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1133534",
      "license": "CC BY 2.0 FR",
      "attribution": "#1133534 (CK) / #148078 (tommy__san)"
    }
  ],
  [
    "opposition",
    "B2",
    "名詞",
    [
      "反対",
      "反対すること"
    ],
    "/ɑpəˈzɪʃən/",
    "They carried on with the construction in the face of strong opposition from the residents.",
    "その工事は住民からの強い反対にもかかわらず、続けられた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/48016",
      "license": "CC BY 2.0 FR",
      "attribution": "#48016 (CK) / #210745 (tommy__san)"
    }
  ],
  [
    "optimistic",
    "B2",
    "形容詞",
    [
      "楽天主義の"
    ],
    "/ɑptəˈmɪstɪk/",
    "How can you be so optimistic?",
    "よくもそう楽天的でいられるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1656252",
      "license": "CC BY 2.0 FR",
      "attribution": "#1656252 (Spamster) / #1656253 (mookeee)"
    }
  ],
  [
    "option",
    "A2",
    "名詞",
    [
      "選択肢"
    ],
    "/ˈɑpʃən/",
    "I am in favor of the option.",
    "私はその意見に賛成だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/254221",
      "license": "CC BY 2.0 FR",
      "attribution": "#254221 (CK) / #160300 (KK_kaku_)"
    }
  ],
  [
    "orchestra",
    "B2",
    "名詞",
    [
      "管弦楽団"
    ],
    "/ˈɔrkəstrə/",
    "Today's performance of the ABC Symphony Orchestra fell short of my expectations.",
    "今日のＡＢＣ交響楽団の演奏は期待はずれだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/242483",
      "license": "CC BY 2.0 FR",
      "attribution": "#242483 (CM) / #171992 (tommy__san)"
    }
  ],
  [
    "ordinary",
    "A2",
    "形容詞",
    [
      "平凡な"
    ],
    "/ˈɔrdənɛri/",
    "I saw at a glance that he was an ordinary man.",
    "彼が平凡な男性であることは一目でわかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/255483",
      "license": "CC BY 2.0 FR",
      "attribution": "#255483 (CK) / #1247655 (bunbuku)"
    }
  ],
  [
    "organ",
    "B2",
    "名詞",
    [
      "臓器",
      "オルガン"
    ],
    "/ˈɔrgən/",
    "The surgeon persuaded me to undergo an organ transplant operation.",
    "外科医は私を説得して、臓器の移植手術を受けることに同意させた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21982",
      "license": "CC BY 2.0 FR",
      "attribution": "#21982 (CK) / #184853 (bunbuku)"
    }
  ],
  [
    "organic",
    "B2",
    "形容詞",
    [
      "有機肥料を用いる"
    ],
    "/ɔrˈgænɪk/",
    "This grocery store only sells organic food.",
    "この食料品店は自然食品のみを売っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4190431",
      "license": "CC BY 2.0 FR",
      "attribution": "#4190431 (Hybrid) / #4587160 (omi31415)"
    }
  ],
  [
    "organization",
    "A2",
    "名詞",
    [
      "団体"
    ],
    "/ɔrgənəˈzeɪʃən/",
    "She has an important role in our organization.",
    "彼女には私たちの団体での重要な役割があります。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2199806",
      "license": "CC BY 2.0 FR",
      "attribution": "#2199806 (CK) / #2199779 (Blanka_Meduzo)"
    }
  ],
  [
    "organize",
    "A2",
    "動詞",
    [
      "を組織する",
      "団体を組織する"
    ],
    "/ˈɔrgənaɪz/",
    "Amnesty International often organizes public protests in support of political prisoners.",
    "国際アムネスティは、政治囚への支援として一般市民による抗議活動を組織することがしばしばある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241411",
      "license": "CC BY 2.0 FR",
      "attribution": "#241411 (CK) / #173061 (wat)"
    }
  ],
  [
    "organized",
    "B1",
    "形容詞",
    [
      "整理された",
      "組織された"
    ],
    "/ˈɔrgənaɪzd/",
    "Always keep your workplace organized.",
    "いつも仕事場をきちんと整理しておきなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1293143",
      "license": "CC BY 2.0 FR",
      "attribution": "#1293143 (CM) / #228721 (bunbuku)"
    }
  ],
  [
    "organizer",
    "B1",
    "名詞",
    [
      "主催者"
    ],
    "/ˈɔrgənaɪzɚ/",
    "The event organizer confirmed the final schedule.",
    "主催者が最終日程を確認した。",
    null
  ],
  [
    "origin",
    "B2",
    "名詞",
    [
      "起源"
    ],
    "/ˈɔrədʒən/",
    "The origin of the universe will probably never be explained.",
    "宇宙の起源はおそらく永遠に説明されないだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/27036",
      "license": "CC BY 2.0 FR",
      "attribution": "#27036 (Swift) / #189880 (tommy__san)"
    }
  ],
  [
    "original",
    "A2",
    "形容詞・名詞",
    [
      "最初の"
    ],
    "/ɚˈɪdʒənəl/",
    "You seem to have lost sight of original objective.",
    "あなたは最初の目標を見失っているようです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/69400",
      "license": "CC BY 2.0 FR",
      "attribution": "#69400 (CK) / #232032 (bunbuku)"
    }
  ],
  [
    "originally",
    "B1",
    "副詞",
    [
      "もともと",
      "本来"
    ],
    "/ɚˈɪdʒənəli/",
    "This poem was originally written in French.",
    "この詩は本来フランス語で書かれていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59042",
      "license": "CC BY 2.0 FR",
      "attribution": "#59042 (CK) / #221716 (small_snow)"
    }
  ],
  [
    "otherwise",
    "B2",
    "副詞",
    [
      "ほかの点では",
      "違ったやり方で"
    ],
    "/ˈʌðɚwaɪz/",
    "The food wasn't very delicious, but otherwise the party was a success.",
    "料理は余りおいしくなかったが、その他の点では、そのパーティーは成功だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1334016",
      "license": "CC BY 2.0 FR",
      "attribution": "#1334016 (CK) / #77924 (mookeee)"
    }
  ],
  [
    "ought",
    "B1",
    "動詞",
    [
      "するはずである",
      "するのが当然である"
    ],
    "/ɔt/",
    "They left at 5 o'clock, so they ought to be home by 6.",
    "彼等は五時に出発したから、六時には帰宅するはずです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/317697",
      "license": "CC BY 2.0 FR",
      "attribution": "#317697 (CK) / #86013 (bunbuku)"
    }
  ],
  [
    "ours",
    "B1",
    "名詞",
    [
      "私たちのもの"
    ],
    "/ˈaʊɚz/",
    "They live in the house opposite to ours.",
    "彼らは向かいの家に住んでいる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/68158",
      "license": "CC BY 2.0 FR",
      "attribution": "#68158 (CK) / #1264135 (bunbuku)"
    }
  ],
  [
    "ourselves",
    "A2",
    "名詞",
    [
      "自分たちみずから",
      "自分たちを"
    ],
    "/aʊɚˈsɛlvz/",
    "It's much cheaper for us to make it ourselves.",
    "自分で作る方がはるかに安いよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8613224",
      "license": "CC BY 2.0 FR",
      "attribution": "#8613224 (Hybrid) / #12001852 (small_snow)"
    }
  ],
  [
    "outcome",
    "B2",
    "名詞",
    [
      "結果"
    ],
    "/ˈaʊtkʌm/",
    "The media has a lot of influence on the outcome of an election.",
    "選挙の結果に及ぼすマスコミの影響力は大きい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273531",
      "license": "CC BY 2.0 FR",
      "attribution": "#273531 (CK) / #141041 (small_snow)"
    }
  ],
  [
    "outdoor",
    "B1",
    "形容詞",
    [
      "野外の"
    ],
    "/ˈaʊtdɔr/",
    "The outdoor concert was canceled due to the storm.",
    "野外コンサートは嵐のために中止になった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/324057",
      "license": "CC BY 2.0 FR",
      "attribution": "#324057 (CK) / #79661 (mookeee)"
    }
  ],
  [
    "outdoors",
    "B1",
    "副詞",
    [
      "戸外で",
      "野外で"
    ],
    "/ˈaʊtˈdɔrz/",
    "No one wants to work outdoors on a cold day.",
    "寒い日に外で仕事したい人なんて、いやしないよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8177628",
      "license": "CC BY 2.0 FR",
      "attribution": "#8177628 (CK) / #10367090 (bunbuku)"
    }
  ],
  [
    "outer",
    "B2",
    "形容詞",
    [
      "中心から遠い"
    ],
    "/ˈaʊtɚ/",
    "The outer wall protects the building from wind.",
    "外壁が建物を風から守る。",
    null
  ],
  [
    "outfit",
    "B2",
    "名詞",
    [
      "服装",
      "衣装"
    ],
    "/ˈaʊtfɪt/",
    "What do you think of this outfit?",
    "この衣装どう思う？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3738731",
      "license": "CC BY 2.0 FR",
      "attribution": "#3738731 (CK) / #8625665 (small_snow)"
    }
  ],
  [
    "outline",
    "B2",
    "名詞・動詞",
    [
      "概要",
      "の概要を述べる"
    ],
    "/ˈaʊtlaɪn/",
    "The introduction gives an outline of the argument.",
    "序論は議論の概要を示す。",
    null
  ],
  [
    "output",
    "B2",
    "名詞",
    [
      "生産高"
    ],
    "/ˈaʊtpʊt/",
    "The factory increased its output without using more energy.",
    "工場はエネルギーを増やさず生産量を上げた。",
    null
  ],
  [
    "outside",
    "A2",
    "形容詞・名詞・前置詞",
    [
      "で",
      "の"
    ],
    "/ˈaʊtˈsaɪd/",
    "It was so cold that no one wanted to go outside.",
    "とても寒かったので誰も外に出たがらなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/37814",
      "license": "CC BY 2.0 FR",
      "attribution": "#37814 (CK) / #200613 (bunbuku)"
    }
  ],
  [
    "outstanding",
    "B2",
    "形容詞",
    [
      "残っている"
    ],
    "/aʊtsˈtændɪŋ/",
    "His ability in mathematics is outstanding.",
    "彼の数学の才能はずば抜けている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/286901",
      "license": "CC BY 2.0 FR",
      "attribution": "#286901 (CM) / #116767 (tommy__san)"
    }
  ],
  [
    "oven",
    "A2",
    "名詞",
    [
      "オーブン"
    ],
    "/ˈʌvən/",
    "I like the smell of bread just out of the oven.",
    "焼きたてのパンの匂いが好きです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3053138",
      "license": "CC BY 2.0 FR",
      "attribution": "#3053138 (CK) / #3052946 (tommy_san)"
    }
  ],
  [
    "overall",
    "B2",
    "形容詞・副詞",
    [
      "全般的な",
      "全面的な"
    ],
    "/ˈoʊvɚɔl/",
    "The overall result was better than expected.",
    "全体的な結果は予想よりよかった。",
    null
  ],
  [
    "overcome",
    "B2",
    "動詞",
    [
      "を参らせる",
      "へとへとにさせる"
    ],
    "/ˈoʊvɚkʌm/",
    "I'm sure that I can overcome any difficulty.",
    "私はどんな困難にも耐えてみせる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7897839",
      "license": "CC BY 2.0 FR",
      "attribution": "#7897839 (CM) / #159219 (bunbuku)"
    }
  ],
  [
    "overnight",
    "B2",
    "副詞",
    [
      "一夜のうちに",
      "短期宿泊用の"
    ],
    "/ˈoʊvɚˈnaɪt/",
    "The delay forced us to stay overnight in an expensive hotel.",
    "その遅れは私たちに高級ホテルでの宿泊を余儀なくさせた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63033",
      "license": "CC BY 2.0 FR",
      "attribution": "#63033 (CK) / #1255133 (bunbuku)"
    }
  ],
  [
    "overseas",
    "B2",
    "形容詞・副詞",
    [
      "海外の"
    ],
    "/ˈoʊvɚˈsiz/",
    "The Board of Trustees voted to divest the organization's overseas holdings.",
    "理事会は海外の持ち株を放棄することを議決しました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325338",
      "license": "CC BY 2.0 FR",
      "attribution": "#325338 (CK) / #78378 (mookeee)"
    }
  ],
  [
    "owe",
    "B2",
    "動詞",
    [
      "のおかげをこうむっている",
      "を与える義務がある"
    ],
    "/oʊ/",
    "I owe what I am today to my uncle.",
    "私の今日があるのは、おじさんのおかげです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/250296",
      "license": "CC BY 2.0 FR",
      "attribution": "#250296 (CM) / #163623 (KK_kaku_)"
    }
  ],
  [
    "own",
    "A2",
    "動詞",
    [
      "それ自身の"
    ],
    "/oʊn/",
    "Each person has his or her own view of the world.",
    "人それぞれに世界観あります。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12459265",
      "license": "CC BY 2.0 FR",
      "attribution": "#12459265 (CK) / #11548158 (small_snow)"
    }
  ],
  [
    "owner",
    "A2",
    "名詞",
    [
      "所有者",
      "店主"
    ],
    "/ˈoʊnɚ/",
    "The man standing over there is the owner of the store.",
    "あそこに立っている人が店の主人です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/71782",
      "license": "CC BY 2.0 FR",
      "attribution": "#71782 (CK) / #234406 (bunbuku)"
    }
  ],
  [
    "ownership",
    "B2",
    "名詞",
    [
      "所有権",
      "所有"
    ],
    "/ˈoʊnɚʃɪp/",
    "He renounced the ownership of the land.",
    "彼はその土地の所有権を放棄した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291187",
      "license": "CC BY 2.0 FR",
      "attribution": "#291187 (CK) / #112490 (small_snow)"
    }
  ],
  [
    "oxygen",
    "B2",
    "名詞",
    [
      "酸素"
    ],
    "/ˈɑksədʒən/",
    "A water molecule has two hydrogen atoms and one oxygen atom.",
    "水分子は、２個の水素原子と１個の酸素原子からなる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270937",
      "license": "CC BY 2.0 FR",
      "attribution": "#270937 (CK) / #143630 (mookeee)"
    }
  ],
  [
    "pace",
    "B2",
    "名詞・動詞",
    [
      "ペース",
      "速度"
    ],
    "/peɪs/",
    "The locals around here really live at a relaxed pace.",
    "こっちの人はのんびりしてるね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61463",
      "license": "CC BY 2.0 FR",
      "attribution": "#61463 (CM) / #224127 (bunbuku)"
    }
  ],
  [
    "pack",
    "A2",
    "名詞・動詞",
    [
      "パック"
    ],
    "/pæk/",
    "How much does a six-pack of beer cost?",
    "ビール６缶パックは、おいくらですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9145558",
      "license": "CC BY 2.0 FR",
      "attribution": "#9145558 (CK) / #9145792 (small_snow)"
    }
  ],
  [
    "package",
    "B1",
    "名詞・動詞",
    [
      "小包",
      "一式"
    ],
    "/ˈpækədʒ/",
    "I'd like you to send this package for me right away.",
    "この小包をすぐ送ってもらいたい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1341395",
      "license": "CC BY 2.0 FR",
      "attribution": "#1341395 (CK) / #221138 (mookeee)"
    }
  ],
  [
    "packet",
    "B2",
    "名詞",
    [
      "小袋",
      "包み"
    ],
    "/ˈpækət/",
    "She opened a packet of rice crackers.",
    "彼女は米菓の小袋を開けた。",
    null
  ],
  [
    "pain",
    "A2",
    "名詞",
    [
      "痛み",
      "に苦痛を与える"
    ],
    "/peɪn/",
    "Please give me some kind of medicine to curb the pain.",
    "痛みを抑える薬を何かください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1009195",
      "license": "CC BY 2.0 FR",
      "attribution": "#1009195 (AOCinJAPAN) / #125672 (bunbuku)"
    }
  ],
  [
    "painful",
    "B1",
    "形容詞",
    [
      "痛い"
    ],
    "/ˈpeɪnfəl/",
    "It's painful to keep sitting for hours.",
    "何時間も座ったままは、つらいよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/24552",
      "license": "CC BY 2.0 FR",
      "attribution": "#24552 (Zifre) / #11015471 (bunbuku)"
    }
  ],
  [
    "painter",
    "A2",
    "名詞",
    [
      "画家"
    ],
    "/ˈpeɪntɚ/",
    "I've wanted to be a painter for a long time.",
    "ずっと前から絵描きになりたいって思ってるんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7714854",
      "license": "CC BY 2.0 FR",
      "attribution": "#7714854 (CK) / #10352431 (bunbuku)"
    }
  ],
  [
    "palace",
    "A2",
    "名詞",
    [
      "王宮の有力者たち"
    ],
    "/ˈpæləs/",
    "The king and his family live in the royal palace.",
    "国王とその家族は王宮に住んでいる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241364",
      "license": "CC BY 2.0 FR",
      "attribution": "#241364 (CK) / #173108 (huizi99)"
    }
  ],
  [
    "pale",
    "B1",
    "形容詞",
    [
      "薄くなる",
      "淡くなる"
    ],
    "/peɪl/",
    "The very thought of snakes makes her turn pale.",
    "ヘビのことを考えるだけで彼女の顔は青くなる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/33909",
      "license": "CC BY 2.0 FR",
      "attribution": "#33909 (al_ex_an_der) / #196730 (mookeee)"
    }
  ],
  [
    "palm",
    "B2",
    "名詞",
    [
      "手のひら"
    ],
    "/pɑm/",
    "I am interested in palm reading.",
    "手相に興味があるんです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/266032",
      "license": "CC BY 2.0 FR",
      "attribution": "#266032 (CK) / #148527 (bunbuku)"
    }
  ],
  [
    "pan",
    "B1",
    "名詞",
    [
      "パンする"
    ],
    "/pæn/",
    "Put the meat in the frying pan after the oil has spread.",
    "フライパンに油が回ったら肉を入れます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/34282",
      "license": "CC BY 2.0 FR",
      "attribution": "#34282 (CM) / #10628761 (bunbuku)"
    }
  ],
  [
    "panel",
    "B2",
    "名詞",
    [
      "パネル",
      "パネル画"
    ],
    "/ˈpænəl/",
    "Some cars have solar panels on the roof.",
    "何台かの車は、屋根にソーラーパネルが付いている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9496001",
      "license": "CC BY 2.0 FR",
      "attribution": "#9496001 (DJ_Saidez) / #9496141 (small_snow)"
    }
  ],
  [
    "panic",
    "B2",
    "名詞",
    [
      "あわてふためき",
      "あわてふためく"
    ],
    "/ˈpænɪk/",
    "There's no need to panic. There's plenty of time.",
    "そんなにあわてることはないよ。時間はたっぷりあるんだから。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41552",
      "license": "CC BY 2.0 FR",
      "attribution": "#41552 (Swift) / #204310 (bunbuku)"
    }
  ],
  [
    "pants",
    "A2",
    "名詞",
    [
      "パンツ",
      "ジーパン"
    ],
    "/pænts/",
    "Those pants are a little too tight in the waist.",
    "そのパンツ、ウエストが少しきつ過ぎるの。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/569076",
      "license": "CC BY 2.0 FR",
      "attribution": "#569076 (darinmex) / #11527177 (small_snow)"
    }
  ],
  [
    "parade",
    "B2",
    "名詞",
    [
      "列を作って行進する",
      "を見せびらかす"
    ],
    "/pɚˈeɪd/",
    "We saw the parade move down the street.",
    "私達はパレードが通りに沿って進んでいくのを見た。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/262835",
      "license": "CC BY 2.0 FR",
      "attribution": "#262835 (CK) / #236688 (mookeee)"
    }
  ],
  [
    "parallel",
    "B2",
    "形容詞・名詞",
    [
      "平行な",
      "平行線"
    ],
    "/ˈpɛrəlɛl/",
    "The two streets run parallel to each other.",
    "２本の道路は平行に走っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11792647",
      "license": "CC BY 2.0 FR",
      "attribution": "#11792647 (sundown) / #235394 (e4zh1nmcz)"
    }
  ],
  [
    "parking",
    "A2",
    "名詞",
    [
      "駐車",
      "駐車場"
    ],
    "/ˈpɑrkɪŋ/",
    "I was fined six thousand yen for a parking violation.",
    "駐車違反で６０００円の罰金をとられた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277686",
      "license": "CC BY 2.0 FR",
      "attribution": "#277686 (CK) / #126306 (KK_kaku_)"
    }
  ],
  [
    "parliament",
    "B2",
    "名詞",
    [
      "議会"
    ],
    "/ˈpɑrləmənt/",
    "The bill will be debated in parliament next week.",
    "その法案は来週議会で審議される。",
    null
  ],
  [
    "part-time",
    "B2",
    "形容詞",
    [
      "パートタイムの",
      "パートタイムで"
    ],
    "/pɑrt taɪm/",
    "My brother has a part-time job in a library.",
    "僕のお兄ちゃんは、図書館でパートしてるんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9166410",
      "license": "CC BY 2.0 FR",
      "attribution": "#9166410 (DJ_Saidez) / #9458350 (small_snow)"
    }
  ],
  [
    "participant",
    "B2",
    "名詞",
    [
      "参加者"
    ],
    "/pɑrˈtɪsəpənt/",
    "The participants were for the most part women.",
    "参加者の大部分は女性だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/245041",
      "license": "CC BY 2.0 FR",
      "attribution": "#245041 (CM) / #169445 (tommy__san)"
    }
  ],
  [
    "participate",
    "B1",
    "動詞",
    [
      "参加する"
    ],
    "/pɑrˈtɪsəpeɪt/",
    "They want to participate in the Olympic Games.",
    "彼らはオリンピックに参加したいと思っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/305547",
      "license": "CC BY 2.0 FR",
      "attribution": "#305547 (CK) / #98155 (mookeee)"
    }
  ],
  [
    "participation",
    "B2",
    "名詞",
    [
      "参加"
    ],
    "/pɑrtɪsəˈpeɪʃən/",
    "Student participation increased after the format changed.",
    "形式変更後に学生の参加が増えた。",
    null
  ],
  [
    "particular",
    "A2",
    "形容詞",
    [
      "好みがうるさい",
      "特定の"
    ],
    "/pɚˈtɪkjəlɚ/",
    "Don't worry, Mom. He isn't particular about food. He eats anything.",
    "心配しないでお母さん。彼は食べ物にはうるさくないから。何でも食べてくれるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63940",
      "license": "CC BY 2.0 FR",
      "attribution": "#63940 (CK) / #226596 (tommy_san)"
    }
  ],
  [
    "particularly",
    "B1",
    "副詞",
    [
      "詳しく"
    ],
    "/pɑrˈtɪkjəlɚli/",
    "It's getting cooler, particularly in the mornings and evenings.",
    "朝晩、涼しくなってきましたね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277840",
      "license": "CC BY 2.0 FR",
      "attribution": "#277840 (CM) / #126152 (small_snow)"
    }
  ],
  [
    "partly",
    "B2",
    "副詞",
    [
      "一部は",
      "部分的に"
    ],
    "/ˈpɑrtli/",
    "I'm sorry. I'm partly responsible for it.",
    "ごめん、僕にも責任があるんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/56390",
      "license": "CC BY 2.0 FR",
      "attribution": "#56390 (CM) / #219074 (bunbuku)"
    }
  ],
  [
    "partnership",
    "B2",
    "名詞",
    [
      "提携"
    ],
    "/ˈpɑrtnɚʃɪp/",
    "The two schools formed a research partnership.",
    "その2校は研究提携を結んだ。",
    null
  ],
  [
    "pass",
    "A2",
    "名詞・動詞",
    [
      "通っている",
      "に合格する"
    ],
    "/pæs/",
    "He is studying hard so that he can pass the examinations.",
    "彼は試験に合格できるように一生懸命勉強をしている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/298264",
      "license": "CC BY 2.0 FR",
      "attribution": "#298264 (CM) / #105424 (mookeee)"
    }
  ],
  [
    "passage",
    "B2",
    "名詞",
    [
      "節"
    ],
    "/ˈpæsədʒ/",
    "I copied a passage from the book into my notebook.",
    "その本の一節をノートに書き写した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/43945",
      "license": "CC BY 2.0 FR",
      "attribution": "#43945 (CK) / #206697 (bunbuku)"
    }
  ],
  [
    "passenger",
    "A2",
    "名詞",
    [
      "乗客"
    ],
    "/ˈpæsəndʒɚ/",
    "Rosa Parks refused to give up her seat for a white passenger.",
    "ローザ・パークスは白人乗客に席を譲ることを拒否した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/676305",
      "license": "CC BY 2.0 FR",
      "attribution": "#676305 (darinmex) / #872693 (thyc244)"
    }
  ],
  [
    "passion",
    "B1",
    "名詞",
    [
      "大好物"
    ],
    "/ˈpæʃən/",
    "She has a passion for cake.",
    "彼女はケーキが大好きなんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/310780",
      "license": "CC BY 2.0 FR",
      "attribution": "#310780 (CK) / #92929 (small_snow)"
    }
  ],
  [
    "passionate",
    "B2",
    "形容詞",
    [
      "熱心な",
      "情熱的な"
    ],
    "/ˈpæʃənət/",
    "Tom doesn't seem to be as passionate about that as Mary seems to be.",
    "トムは、メアリーほどそれについて乗り気ではないようだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6663998",
      "license": "CC BY 2.0 FR",
      "attribution": "#6663998 (CK) / #7298762 (Mari_Taguchi)"
    }
  ],
  [
    "password",
    "B2",
    "名詞",
    [
      "パスワード"
    ],
    "/ˈpæswɝd/",
    "Choose a password that's easy to remember but difficult to guess.",
    "パスワードは、覚えやすく、かつ推測されにくいものにしてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10079884",
      "license": "CC BY 2.0 FR",
      "attribution": "#10079884 (CK) / #3436892 (tommy_san)"
    }
  ],
  [
    "past",
    "A2",
    "副詞",
    [
      "終わった"
    ],
    "/pæst/",
    "We've had all kinds of weather over the past few days.",
    "ここ数日天気がめまぐるしく変わっている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61563",
      "license": "CC BY 2.0 FR",
      "attribution": "#61563 (CK) / #224228 (bunbuku)"
    }
  ],
  [
    "path",
    "B1",
    "名詞",
    [
      "庭内の道",
      "道への道程"
    ],
    "/pæθ/",
    "The path between the two houses was blocked by snow.",
    "２軒の家の間の道は雪で閉ざされていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72882",
      "license": "CC BY 2.0 FR",
      "attribution": "#72882 (CM) / #235504 (arnab)"
    }
  ],
  [
    "patience",
    "B2",
    "名詞",
    [
      "忍耐力",
      "忍耐"
    ],
    "/ˈpeɪʃəns/",
    "You must have a lot of patience to learn foreign languages.",
    "外国語を習うには多くの忍耐力が必要だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21902",
      "license": "CC BY 2.0 FR",
      "attribution": "#21902 (CK) / #184772 (mookeee)"
    }
  ],
  [
    "patient",
    "A2",
    "形容詞・名詞",
    [
      "患者"
    ],
    "/ˈpeɪʃənt/",
    "I have a lot of patients who are older than me.",
    "自分より年上の患者をたくさん診てるんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5187492",
      "license": "CC BY 2.0 FR",
      "attribution": "#5187492 (CK) / #9250777 (small_snow)"
    }
  ],
  [
    "pattern",
    "A2",
    "名詞",
    [
      "様式パターン",
      "を模様をつける"
    ],
    "/ˈpætɚn/",
    "Researchers noticed a clear pattern in the data.",
    "研究者はデータに明確なパターンを見つけた。",
    null
  ],
  [
    "pause",
    "B2",
    "名詞・動詞",
    [
      "ちょっと休止する",
      "ちょっとやめる"
    ],
    "/pɔz/",
    "There was a momentary pause in the talk.",
    "話がちょっと途切れた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326519",
      "license": "CC BY 2.0 FR",
      "attribution": "#326519 (CM) / #77201 (mookeee)"
    }
  ],
  [
    "pay",
    "A2",
    "名詞",
    [
      "をもたらす"
    ],
    "/peɪ/",
    "How much will you pay me if I fix the plumbing?",
    "僕が配管を直したら、幾らくれる？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12925590",
      "license": "CC BY 2.0 FR",
      "attribution": "#12925590 (CK) / #11488284 (small_snow)"
    }
  ],
  [
    "payment",
    "B1",
    "名詞",
    [
      "支払い",
      "支払金"
    ],
    "/ˈpeɪmənt/",
    "The fee includes the payment for professional services needed to complete the survey.",
    "料金には調査をするのに必要な専門的な仕事に対する支払いも含まれています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325752",
      "license": "CC BY 2.0 FR",
      "attribution": "#325752 (CK) / #77967 (mookeee)"
    }
  ],
  [
    "peace",
    "A2",
    "名詞",
    [
      "静けさ"
    ],
    "/pis/",
    "A rifle shot broke the peace of the early morning.",
    "ライフルの発射音が早朝の静けさを破った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/29822",
      "license": "CC BY 2.0 FR",
      "attribution": "#29822 (CM) / #192658 (mookeee)"
    }
  ],
  [
    "peaceful",
    "B1",
    "形容詞",
    [
      "平和な"
    ],
    "/ˈpisfəl/",
    "My uncle lived a happy life and died a peaceful death.",
    "叔父は幸せに暮らし安らかに死んだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/266638",
      "license": "CC BY 2.0 FR",
      "attribution": "#266638 (CK) / #147922 (bunbuku)"
    }
  ],
  [
    "peer",
    "B2",
    "名詞",
    [
      "じっと見つめる"
    ],
    "/pɪr/",
    "She had to peer through the fog to see the sign.",
    "彼女は標識を見るため霧の中をじっと見なければならなかった。",
    null
  ],
  [
    "penalty",
    "B2",
    "名詞",
    [
      "刑罰",
      "罰則"
    ],
    "/ˈpɛnəlti/",
    "We should do away with the death penalty.",
    "我々は死刑を廃止すべきである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/22948",
      "license": "CC BY 2.0 FR",
      "attribution": "#22948 (CK) / #185816 (tommy__san)"
    }
  ],
  [
    "penny",
    "A2",
    "名詞",
    [
      "ペニー"
    ],
    "/ˈpɛni/",
    "A penny saved is a penny earned.",
    "１ペニーの節約は１ペニーの儲け。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73206",
      "license": "CC BY 2.0 FR",
      "attribution": "#73206 (CK) / #235827 (mookeee)"
    }
  ],
  [
    "pension",
    "B2",
    "名詞",
    [
      "年金",
      "に年金を与える"
    ],
    "/ˈpɛnʃən/",
    "It was hard for him to live on his small pension.",
    "少ない年金で生活するのは彼には困難だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267586",
      "license": "CC BY 2.0 FR",
      "attribution": "#267586 (CK) / #146762 (bunbuku)"
    }
  ],
  [
    "per",
    "A2",
    "前置詞",
    [
      "で"
    ],
    "/pɝ/",
    "Typhoon No.11 is moving up north at twenty kilometers per hour.",
    "台風１１号は、毎時２０キロメートルの速さで北上中です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275417",
      "license": "CC BY 2.0 FR",
      "attribution": "#275417 (CM) / #137819 (bunbuku)"
    }
  ],
  [
    "per cent",
    "A2",
    "形容詞・副詞・名詞",
    [
      "パーセント"
    ],
    "/pɝ sɛnt/",
    "I agree with Tom one hundred per cent.",
    "トムに100%賛成です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10739441",
      "license": "CC BY 2.0 FR",
      "attribution": "#10739441 (sundown) / #10737841 (small_snow)"
    }
  ],
  [
    "perceive",
    "B2",
    "動詞",
    [
      "受け取る",
      "認識する"
    ],
    "/pɚˈsiv/",
    "Customers may perceive the change as unfair.",
    "顧客はその変更を不公平だと受け取るかもしれない。",
    null
  ],
  [
    "percentage",
    "B1",
    "名詞",
    [
      "割合"
    ],
    "/pɚˈsɛntədʒ/",
    "A high percentage of residents supported the plan.",
    "住民の高い割合がその計画を支持した。",
    null
  ],
  [
    "perception",
    "B2",
    "名詞",
    [
      "知覚する力"
    ],
    "/pɚˈsɛpʃən/",
    "Advertising can influence our perception of quality.",
    "広告は品質に対する認識へ影響を与えうる。",
    null
  ],
  [
    "perfectly",
    "B1",
    "副詞",
    [
      "申し分なく"
    ],
    "/ˈpɝfəktli/",
    "Don't shout like that. I can hear you perfectly.",
    "そんなに叫ばなくても聞こえます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41521",
      "license": "CC BY 2.0 FR",
      "attribution": "#41521 (CM) / #204279 (KK_kaku_)"
    }
  ],
  [
    "perform",
    "A2",
    "動詞",
    [
      "演奏する"
    ],
    "/pɚˈfɔrm/",
    "I'd like to perform at Carnegie Hall someday.",
    "いつかカーネギーホールで演奏してみたいです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1936394",
      "license": "CC BY 2.0 FR",
      "attribution": "#1936394 (CK) / #2147188 (bunbuku)"
    }
  ],
  [
    "performance",
    "B1",
    "名詞",
    [
      "演奏"
    ],
    "/pɚˈfɔrməns/",
    "Today's performance of the ABC Symphony Orchestra fell short of my expectations.",
    "今日のＡＢＣ交響楽団の演奏は期待はずれだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/242483",
      "license": "CC BY 2.0 FR",
      "attribution": "#242483 (CM) / #171992 (tommy__san)"
    }
  ],
  [
    "perhaps",
    "A2",
    "副詞",
    [
      "おそらく"
    ],
    "/pɚˈhæps/",
    "Perhaps I should take an umbrella with me just in case.",
    "万一に備えて傘を持っていった方がいいだろうな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322528",
      "license": "CC BY 2.0 FR",
      "attribution": "#322528 (CK) / #81187 (bunbuku)"
    }
  ],
  [
    "permanent",
    "B2",
    "形容詞",
    [
      "永久の"
    ],
    "/ˈpɝmənənt/",
    "The banker's pay cut was temporary, not permanent.",
    "銀行員の給与カットは一時的なもので、恒久的なものではなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/681716",
      "license": "CC BY 2.0 FR",
      "attribution": "#681716 (Source_VOA) / #893254 (thyc244)"
    }
  ],
  [
    "permanently",
    "B2",
    "副詞",
    [
      "永久に"
    ],
    "/ˈpɝmənəntli/",
    "The factory closed permanently last winter.",
    "その工場は昨冬、永久に閉鎖した。",
    null
  ],
  [
    "permission",
    "A2",
    "名詞",
    [
      "許可"
    ],
    "/pɚˈmɪʃən/",
    "You must not park your car there without permission.",
    "勝手にそこへ駐車したらいけないのよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322814",
      "license": "CC BY 2.0 FR",
      "attribution": "#322814 (CK) / #10166387 (bunbuku)"
    }
  ],
  [
    "permit",
    "B2",
    "名詞・動詞",
    [
      "を許可する"
    ],
    "/pɚˈmɪt/",
    "If you permit me to speak, I can explain everything.",
    "発言を許していただけるなら、すべてをご説明いたします。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/282689",
      "license": "CC BY 2.0 FR",
      "attribution": "#282689 (CM) / #121317 (KK_kaku_)"
    }
  ],
  [
    "personally",
    "B1",
    "副詞",
    [
      "個人的に",
      "個人に当てつけて"
    ],
    "/ˈpɝsənəli/",
    "Personally, I think that corporal punishment is a necessary evil.",
    "個人的には体罰は必要悪だと思っています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3052512",
      "license": "CC BY 2.0 FR",
      "attribution": "#3052512 (WestofEden) / #3014644 (tommy_san)"
    }
  ],
  [
    "pet",
    "A2",
    "名詞",
    [
      "を愛撫する"
    ],
    "/pɛt/",
    "I'm begging you, could you stop treating me like a pet?",
    "お願いですから犬猫扱いするのやめて貰えますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/328046",
      "license": "CC BY 2.0 FR",
      "attribution": "#328046 (CM) / #75672 (mookeee)"
    }
  ],
  [
    "petrol",
    "A2",
    "名詞",
    [
      "ガソリン"
    ],
    "/ˈpɛtroʊl/",
    "The car was almost out of petrol.",
    "その車はガソリンがほとんど切れていた。",
    null
  ],
  [
    "photograph",
    "A2",
    "動詞",
    [
      "写真",
      "の写真をとる"
    ],
    "/ˈfoʊtəgræf/",
    "You may give this photograph to anyone who wants it.",
    "この写真が欲しい人がいたら誰にでも上げていいですよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/997249",
      "license": "CC BY 2.0 FR",
      "attribution": "#997249 (CK) / #997247 (mookeee)"
    }
  ],
  [
    "photographer",
    "B1",
    "名詞",
    [
      "写真家",
      "写真をとる人"
    ],
    "/fəˈtɑgrəfɚ/",
    "She's a good photographer because she's so observant.",
    "彼女は観察力が鋭いので、写真家として優れている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/313066",
      "license": "CC BY 2.0 FR",
      "attribution": "#313066 (CM) / #90646 (bunbuku)"
    }
  ],
  [
    "photography",
    "B1",
    "名詞",
    [
      "写真撮影",
      "写真術"
    ],
    "/fəˈtɑgrəfi/",
    "Do you have underwater photography equipment?",
    "水中撮影機材はお持ちですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10761063",
      "license": "CC BY 2.0 FR",
      "attribution": "#10761063 (AlanF_US) / #11273600 (small_snow)"
    }
  ],
  [
    "physics",
    "A2",
    "名詞",
    [
      "物理学"
    ],
    "/ˈfɪzɪks/",
    "She gave her entire life to the study of physics.",
    "彼女は物理学の研究に一生を捧げた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/316883",
      "license": "CC BY 2.0 FR",
      "attribution": "#316883 (CM) / #86827 (tommy__san)"
    }
  ],
  [
    "pick",
    "A2",
    "名詞・動詞",
    [
      "受け取る",
      "選ぶ"
    ],
    "/pɪk/",
    "Please come back in half an hour to pick it up.",
    "３０分後に取りに来てください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9649537",
      "license": "CC BY 2.0 FR",
      "attribution": "#9649537 (CK) / #235363 (e4zh1nmcz)"
    }
  ],
  [
    "picture",
    "B2",
    "動詞",
    [
      "絵",
      "を絵に描く"
    ],
    "/ˈpɪktʃɚ/",
    "It took a year and a half to paint that picture.",
    "その絵を描くのにね、1年半かかったんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10325729",
      "license": "CC BY 2.0 FR",
      "attribution": "#10325729 (sundown) / #11604069 (small_snow)"
    }
  ],
  [
    "pill",
    "B2",
    "名詞",
    [
      "錠剤"
    ],
    "/pɪl/",
    "Because of the pills I took, the pain went away.",
    "錠剤のおかげで痛みがなくなった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1303097",
      "license": "CC BY 2.0 FR",
      "attribution": "#1303097 (CK) / #146000 (bunbuku)"
    }
  ],
  [
    "pilot",
    "A2",
    "名詞",
    [
      "パイロット"
    ],
    "/ˈpaɪlət/",
    "The pilot explained to us why the landing was delayed.",
    "パイロットは着陸が遅れた理由を私たちに説明した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/35513",
      "license": "CC BY 2.0 FR",
      "attribution": "#35513 (spockofvulcan) / #198321 (bunbuku)"
    }
  ],
  [
    "pin",
    "B1",
    "名詞・動詞",
    [
      "留め針",
      "ピンで留める"
    ],
    "/pɪn/",
    "Use a pin to attach the notice to the board.",
    "留め針を使って掲示を板に留めてください。",
    null
  ],
  [
    "pipe",
    "B1",
    "名詞",
    [
      "パイプ",
      "パグパイプ"
    ],
    "/paɪp/",
    "He was sitting there with a pipe in his mouth.",
    "彼はパイプをくわえてそこに座っていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/296261",
      "license": "CC BY 2.0 FR",
      "attribution": "#296261 (CK) / #107425 (tommy_san)"
    }
  ],
  [
    "pitch",
    "B2",
    "名詞",
    [
      "を張る"
    ],
    "/pɪtʃ/",
    "This looks like a good place to pitch the tent.",
    "ここ、テントを張るのに良さそう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12229424",
      "license": "CC BY 2.0 FR",
      "attribution": "#12229424 (CK) / #11998585 (small_snow)"
    }
  ],
  [
    "place",
    "B1",
    "動詞",
    [
      "土地"
    ],
    "/pleɪs/",
    "It always takes time to get used to a new place.",
    "新しい土地に慣れるには、時間がかかるものですよね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269213",
      "license": "CC BY 2.0 FR",
      "attribution": "#269213 (CK) / #145350 (bunbuku)"
    }
  ],
  [
    "placement",
    "B2",
    "名詞",
    [
      "職場実習",
      "配置"
    ],
    "/ˈpleɪsmənt/",
    "The course includes a six-week work placement.",
    "その講座には6週間の職場実習が含まれる。",
    null
  ],
  [
    "planet",
    "A2",
    "名詞",
    [
      "惑星"
    ],
    "/ˈplænət/",
    "What would you do if you saw a man from another planet?",
    "もし宇宙人と出会ったらどうするかね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/30931",
      "license": "CC BY 2.0 FR",
      "attribution": "#30931 (CK) / #193763 (mookeee)"
    }
  ],
  [
    "planning",
    "B1",
    "名詞",
    [
      "計画",
      "計画立案"
    ],
    "/ˈplænɪŋ/",
    "Careful planning helped the event run smoothly.",
    "入念な計画のおかげで行事は順調に進んだ。",
    null
  ],
  [
    "plant",
    "A2",
    "動詞",
    [
      "植物"
    ],
    "/plænt/",
    "This kind of plant grows only in the tropical regions.",
    "この種の植物は熱帯地方にのみ育ちます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58601",
      "license": "CC BY 2.0 FR",
      "attribution": "#58601 (CK) / #221278 (bunbuku)"
    }
  ],
  [
    "plastic",
    "A2",
    "形容詞・名詞",
    [
      "プラスチック",
      "ラップ"
    ],
    "/ˈplæstɪk/",
    "I need to wrap my older sister's dinner in plastic wrap.",
    "私はお姉ちゃんの夕飯をラップに包んでしまわないと。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/525827",
      "license": "CC BY 2.0 FR",
      "attribution": "#525827 (CK) / #75504 (mookeee)"
    }
  ],
  [
    "plate",
    "A2",
    "名詞",
    [
      "1皿"
    ],
    "/pleɪt/",
    "Bring me a clean plate and take the dirty one away.",
    "きれいな皿を持って来て汚れたのをさげてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63081",
      "license": "CC BY 2.0 FR",
      "attribution": "#63081 (CM) / #225743 (mookeee)"
    }
  ],
  [
    "platform",
    "A2",
    "名詞",
    [
      "プラットホーム"
    ],
    "/ˈplætfɔrm/",
    "I could hear someone calling my name on the noisy platform.",
    "騒々しい駅のホームで、誰かが私の名前を呼ぶ声が聞こえた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/274310",
      "license": "CC BY 2.0 FR",
      "attribution": "#274310 (CK) / #10175900 (bunbuku)"
    }
  ],
  [
    "pleasant",
    "B1",
    "形容詞",
    [
      "楽しい"
    ],
    "/ˈplɛzənt/",
    "Sometimes it is pleasant to look back on one's childhood.",
    "少年時代を思い出すのも時には楽しいものだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/268062",
      "license": "CC BY 2.0 FR",
      "attribution": "#268062 (CM) / #146500 (arnab)"
    }
  ],
  [
    "please",
    "A2",
    "動詞",
    [
      "どうぞ",
      "〜してください"
    ],
    "/pliz/",
    "Please come back in half an hour to pick it up.",
    "３０分後に取りに来てください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9649537",
      "license": "CC BY 2.0 FR",
      "attribution": "#9649537 (CK) / #235363 (e4zh1nmcz)"
    }
  ],
  [
    "pleased",
    "A2",
    "形容詞",
    [
      "喜んだ",
      "満足した"
    ],
    "/plizd/",
    "I am pleased to help you if I can.",
    "私に出来る事でしたら喜んでお手伝いします。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/249719",
      "license": "CC BY 2.0 FR",
      "attribution": "#249719 (CM) / #164370 (bunbuku)"
    }
  ],
  [
    "pleasure",
    "B1",
    "名詞",
    [
      "喜び"
    ],
    "/ˈplɛʒɚ/",
    "The pain caused by love is much sweeter than any pleasure.",
    "恋の苦悩は他のあらゆる喜びよりも遥かに甘美である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1428390",
      "license": "CC BY 2.0 FR",
      "attribution": "#1428390 (CK) / #77449 (mookeee)"
    }
  ],
  [
    "plot",
    "B1",
    "名詞・動詞",
    [
      "筋",
      "を書き込む"
    ],
    "/plɑt/",
    "The film has a simple but effective plot.",
    "その映画は簡潔だが効果的な筋書きを持つ。",
    null
  ],
  [
    "plus",
    "B1",
    "形容詞・接続詞・名詞・前置詞",
    [
      "とともに"
    ],
    "/plʌs/",
    "The sum of two plus three plus four is nine.",
    "２と３と４の合計は９だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72909",
      "license": "CC BY 2.0 FR",
      "attribution": "#72909 (CM) / #235529 (mookeee)"
    }
  ],
  [
    "pocket",
    "A2",
    "名詞",
    [
      "ポケット",
      "ポケットに似た物"
    ],
    "/ˈpɑkət/",
    "It is rude to speak with your hands in your pockets.",
    "ポケットに手を入れたまま話すのは失礼です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/33467",
      "license": "CC BY 2.0 FR",
      "attribution": "#33467 (CM) / #196289 (small_snow)"
    }
  ],
  [
    "poem",
    "B1",
    "名詞",
    [
      "詩"
    ],
    "/ˈpoʊəm/",
    "It took me an hour to learn the poem by heart.",
    "その詩を暗唱するのに私は１時間かかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/47326",
      "license": "CC BY 2.0 FR",
      "attribution": "#47326 (CK) / #210064 (mookeee)"
    }
  ],
  [
    "poet",
    "B1",
    "名詞",
    [
      "詩人"
    ],
    "/ˈpoʊət/",
    "The well-known poet attempted to commit suicide in his study.",
    "その著名な詩人は自分の書斎で自殺を図ろうとした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1013013",
      "license": "CC BY 2.0 FR",
      "attribution": "#1013013 (CK) / #207835 (KK_kaku_)"
    }
  ],
  [
    "poetry",
    "B1",
    "名詞",
    [
      "詩"
    ],
    "/ˈpoʊətri/",
    "Wine is poetry put into a bottle.",
    "ワインとは、ボトルに詰められた詩である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/553931",
      "license": "CC BY 2.0 FR",
      "attribution": "#553931 (CK) / #5172 (mookeee)"
    }
  ],
  [
    "point",
    "B1",
    "動詞",
    [
      "観点",
      "要点"
    ],
    "/pɔɪnt/",
    "One's point of view depends on the point where one sits.",
    "ものの見方というのは立場に依るものだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/970776",
      "license": "CC BY 2.0 FR",
      "attribution": "#970776 (zipangu) / #971364 (thyc244)"
    }
  ],
  [
    "pointed",
    "B2",
    "形容詞",
    [
      "鋭い",
      "先のとがった"
    ],
    "/ˈpɔɪntɪd/",
    "She asked a pointed question about the missing funds.",
    "彼女は行方不明の資金について鋭い質問をした。",
    null
  ],
  [
    "poison",
    "B1",
    "名詞・動詞",
    [
      "毒",
      "を毒殺する"
    ],
    "/ˈpɔɪzən/",
    "One drop of the poison is enough to kill 160 people.",
    "１滴の毒は１６０人を殺すのに十分である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/376412",
      "license": "CC BY 2.0 FR",
      "attribution": "#376412 (saeb) / #1014814 (mookeee)"
    }
  ],
  [
    "poisonous",
    "B1",
    "形容詞",
    [
      "有毒な"
    ],
    "/ˈpɔɪzənəs/",
    "Are there many poisonous snakes in Australia?",
    "オーストラリアには毒ヘビがたくさんいるんですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8212953",
      "license": "CC BY 2.0 FR",
      "attribution": "#8212953 (CK) / #8781638 (bunbuku)"
    }
  ],
  [
    "pop",
    "A2",
    "形容詞・名詞",
    [
      "ポップ"
    ],
    "/pɑp/",
    "This is the reason that she succeeded as a pop singer.",
    "これが彼女がポップス歌手として成功した理由です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/56339",
      "license": "CC BY 2.0 FR",
      "attribution": "#56339 (CM) / #219023 (bunbuku)"
    }
  ],
  [
    "popularity",
    "B2",
    "名詞",
    [
      "人気"
    ],
    "/pɑpjəˈlɛrəti/",
    "Cassette tapes seem to have given way to compact disks in popularity.",
    "カセットテープは人気の点でＣＤにとって代わられたようだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63736",
      "license": "CC BY 2.0 FR",
      "attribution": "#63736 (CM) / #226392 (arnab)"
    }
  ],
  [
    "pose",
    "B2",
    "動詞",
    [
      "ポーズ",
      "ふりをする"
    ],
    "/poʊz/",
    "It must have been something really big for him to strike a triumphant pose like that.",
    "あいつがガッツポーズするなんて、よっぽど嬉しかったんだろうな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72061",
      "license": "CC BY 2.0 FR",
      "attribution": "#72061 (CM) / #234683 (bunbuku)"
    }
  ],
  [
    "possibly",
    "B1",
    "副詞",
    [
      "ひょっとしたら"
    ],
    "/ˈpɑsəbli/",
    "Possibly the factory will be closed down next week.",
    "たぶん工場は来週閉鎖されるだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/40584",
      "license": "CC BY 2.0 FR",
      "attribution": "#40584 (CK) / #203347 (mookeee)"
    }
  ],
  [
    "poster",
    "A2",
    "名詞",
    [
      "ポスター"
    ],
    "/ˈpoʊstɚ/",
    "The posters were immediately removed from the wall.",
    "ポスターは即刻壁から撤去された。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/33458",
      "license": "CC BY 2.0 FR",
      "attribution": "#33458 (CM) / #196279 (tommy__san)"
    }
  ],
  [
    "pot",
    "B1",
    "名詞",
    [
      "ポット",
      "容器"
    ],
    "/pɑt/",
    "There's almost no coffee left in the pot.",
    "ポットにはほとんどコーヒーは残っていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1066037",
      "license": "CC BY 2.0 FR",
      "attribution": "#1066037 (CK) / #196231 (small_snow)"
    }
  ],
  [
    "potentially",
    "B2",
    "副詞",
    [
      "可能性を秘めて"
    ],
    "/pəˈtɛnʃəli/",
    "The error could be potentially dangerous.",
    "その誤りは危険につながる可能性がある。",
    null
  ],
  [
    "powder",
    "B1",
    "名詞",
    [
      "粉"
    ],
    "/ˈpaʊdɚ/",
    "To make this cake, you'll need baking powder and unsalted butter.",
    "このケーキを作るためには膨らし粉と無塩バターが必要だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9703417",
      "license": "CC BY 2.0 FR",
      "attribution": "#9703417 (CK) / #1166311 (mookeee)"
    }
  ],
  [
    "power",
    "A2",
    "名詞・動詞",
    [
      "影響力のある集団",
      "大国軍事力"
    ],
    "/ˈpaʊɚ/",
    "Japan is one of the greatest economic powers in the world.",
    "日本は世界有数の経済大国である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/281559",
      "license": "CC BY 2.0 FR",
      "attribution": "#281559 (CK) / #122444 (tommy_san)"
    }
  ],
  [
    "prayer",
    "B1",
    "名詞",
    [
      "祈り",
      "祈りの言葉"
    ],
    "/prɛr/",
    "Let's say a prayer before dinner.",
    "夕飯の前にお祈りをしましょう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10018555",
      "license": "CC BY 2.0 FR",
      "attribution": "#10018555 (Nylez) / #13684226 (small_snow)"
    }
  ],
  [
    "precede",
    "B2",
    "動詞",
    [
      "より先に来る",
      "先に来る"
    ],
    "/prɪˈsid/",
    "In English the verb precedes the object.",
    "英語では動詞が目的語の前に来る。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/26371",
      "license": "CC BY 2.0 FR",
      "attribution": "#26371 (Zifre) / #189224 (KK_kaku_)"
    }
  ],
  [
    "precisely",
    "B2",
    "副詞",
    [
      "正確に"
    ],
    "/prɪˈsaɪsli/",
    "Come here at precisely six o'clock.",
    "六時きっかりにここへ来なさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1293160",
      "license": "CC BY 2.0 FR",
      "attribution": "#1293160 (CK) / #77237 (mookeee)"
    }
  ],
  [
    "predictable",
    "B2",
    "形容詞",
    [
      "予想どおりの"
    ],
    "/prɪˈdɪktəbəl/",
    "The ending was too predictable to be exciting.",
    "結末は予想どおりすぎて刺激がなかった。",
    null
  ],
  [
    "preference",
    "B2",
    "名詞",
    [
      "好み",
      "好みの物を選ぶ権利"
    ],
    "/ˈprɛfɚəns/",
    "Music preferences vary from person to person.",
    "音楽の好みは人によって好きずきです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327407",
      "license": "CC BY 2.0 FR",
      "attribution": "#327407 (CM) / #76313 (mookeee)"
    }
  ],
  [
    "prepared",
    "B1",
    "形容詞",
    [
      "準備された",
      "喜んで…する"
    ],
    "/priˈpɛrd/",
    "We have to be prepared to cope with violent storms.",
    "激しい嵐に対処する準備をしておくべきだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238498",
      "license": "CC BY 2.0 FR",
      "attribution": "#238498 (CM) / #175967 (KK_kaku_)"
    }
  ],
  [
    "presentation",
    "B1",
    "名詞",
    [
      "プレゼンテーション",
      "発表"
    ],
    "/prɛzənˈteɪʃən/",
    "It is best to review the material before the presentation.",
    "プレゼンテーションの前に資料に目を通しておくのが一番いい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/34099",
      "license": "CC BY 2.0 FR",
      "attribution": "#34099 (CM) / #237020 (mookeee)"
    }
  ],
  [
    "president",
    "A2",
    "名詞",
    [
      "大統領",
      "米国大統領"
    ],
    "/ˈprɛzədɛnt/",
    "Who do you think will be elected president of the USA?",
    "誰が合衆国の大統領に選ばれると思いますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/276325",
      "license": "CC BY 2.0 FR",
      "attribution": "#276325 (CK) / #136911 (bunbuku)"
    }
  ],
  [
    "press",
    "B1",
    "名詞・動詞",
    [
      "報道陣",
      "押す"
    ],
    "/prɛs/",
    "The spokesman explained the contents of the treaty to the press.",
    "報道担当官が条約の内容を報道陣に説明した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320979",
      "license": "CC BY 2.0 FR",
      "attribution": "#320979 (CK) / #82737 (KK_kaku_)"
    }
  ],
  [
    "price",
    "B2",
    "動詞",
    [
      "値段",
      "の値段を確かめる"
    ],
    "/praɪs/",
    "The actual price was lower than I thought it would be.",
    "実際の値段は思ったより安かった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1003229",
      "license": "CC BY 2.0 FR",
      "attribution": "#1003229 (CK) / #149310 (bunbuku)"
    }
  ],
  [
    "pride",
    "B2",
    "名詞",
    [
      "自尊心"
    ],
    "/praɪd/",
    "Hey, I may have no money, but I still have my pride.",
    "なぁ、金は無いかもしれないけどまだプライドは捨てちゃいないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1629",
      "license": "CC BY 2.0 FR",
      "attribution": "#1629 (Zifre) / #5034 (bunbuku)"
    }
  ],
  [
    "primarily",
    "B2",
    "副詞",
    [
      "主として"
    ],
    "/praɪˈmɛrəli/",
    "This dictionary is primarily intended for high school students.",
    "この辞書は主に高校生を対象としたものです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58832",
      "license": "CC BY 2.0 FR",
      "attribution": "#58832 (CM) / #221508 (KK_kaku_)"
    }
  ],
  [
    "prince",
    "B1",
    "名詞",
    [
      "王子",
      "王"
    ],
    "/prɪns/",
    "The dirty boy turned out to be a prince in disguise.",
    "その汚い少年は変装した王子だとわかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/49465",
      "license": "CC BY 2.0 FR",
      "attribution": "#49465 (CK) / #212186 (huizi99)"
    }
  ],
  [
    "princess",
    "B1",
    "名詞",
    [
      "王女"
    ],
    "/ˈprɪnsɛs/",
    "That girl is under the delusion that she is a princess.",
    "あの少女は自分が王女様だという妄想にとらわれている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/68221",
      "license": "CC BY 2.0 FR",
      "attribution": "#68221 (CK) / #230854 (bunbuku)"
    }
  ],
  [
    "principal",
    "B2",
    "形容詞",
    [
      "校長",
      "長"
    ],
    "/ˈprɪnsəpəl/",
    "The principal shook hands with each of the graduates.",
    "校長は卒業生一人一人と握手をした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1087191",
      "license": "CC BY 2.0 FR",
      "attribution": "#1087191 (CK) / #173566 (bunbuku)"
    }
  ],
  [
    "print",
    "A2",
    "名詞・動詞",
    [
      "絶版",
      "印刷する"
    ],
    "/prɪnt/",
    "This book, which was once a best seller, is now out of print.",
    "この本はかつてはベストセラーだったが、今は絶版になっている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57032",
      "license": "CC BY 2.0 FR",
      "attribution": "#57032 (CK) / #219712 (tommy__san)"
    }
  ],
  [
    "printer",
    "A2",
    "名詞",
    [
      "プリンター"
    ],
    "/ˈprɪntɚ/",
    "Please replace the empty ink cartridge in the printer.",
    "プリンター内の空のインクカートリッジを交換して下さい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/481732",
      "license": "CC BY 2.0 FR",
      "attribution": "#481732 (Benjameno) / #1865480 (bunbuku)"
    }
  ],
  [
    "printing",
    "B1",
    "名詞",
    [
      "印刷",
      "印刷術"
    ],
    "/ˈprɪntɪŋ/",
    "This textbook, having been printed in haste, has a lot of printing mistakes.",
    "この教科書は、急いで印刷したためにミスプリントがたくさんある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59680",
      "license": "CC BY 2.0 FR",
      "attribution": "#59680 (CM) / #222353 (bunbuku)"
    }
  ],
  [
    "prior",
    "B2",
    "形容詞",
    [
      "事前の",
      "前の"
    ],
    "/ˈpraɪɚ/",
    "You may not set up a roadside stall without prior notice.",
    "届け出なしに路上に出店してはならない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327884",
      "license": "CC BY 2.0 FR",
      "attribution": "#327884 (CM) / #75834 (bunbuku)"
    }
  ],
  [
    "prize",
    "A2",
    "名詞",
    [
      "賞"
    ],
    "/praɪz/",
    "Little did she dream that she could win first prize.",
    "１等をとれるなんて彼女は夢にも思わなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73093",
      "license": "CC BY 2.0 FR",
      "attribution": "#73093 (CM) / #235714 (mookeee)"
    }
  ],
  [
    "probability",
    "B2",
    "名詞",
    [
      "可能性",
      "確率"
    ],
    "/prɑbəˈbɪləti/",
    "There is very little probability of an agreement being reached.",
    "協定が結ばれる可能性は極めて少ない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/19244",
      "license": "CC BY 2.0 FR",
      "attribution": "#19244 (CK) / #180577 (KK_kaku_)"
    }
  ],
  [
    "probable",
    "B2",
    "形容詞",
    [
      "ありそうな"
    ],
    "/ˈprɑbəbəl/",
    "It is probable that she will come.",
    "たぶん彼女は来るだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/40564",
      "license": "CC BY 2.0 FR",
      "attribution": "#40564 (Swift) / #203327 (mookeee)"
    }
  ],
  [
    "producer",
    "B1",
    "名詞",
    [
      "生産者"
    ],
    "/prəˈdusɚ/",
    "A local producer supplies the restaurant with cheese.",
    "地元の生産者がレストランへチーズを供給する。",
    null
  ],
  [
    "professor",
    "A2",
    "名詞",
    [
      "教授"
    ],
    "/prəˈfɛsɚ/",
    "We all took for granted that the professor could speak English.",
    "私達はみんな教授は当然英語が話せると思っていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/262860",
      "license": "CC BY 2.0 FR",
      "attribution": "#262860 (CK) / #151696 (mookeee)"
    }
  ],
  [
    "profile",
    "A2",
    "名詞",
    [
      "ゲロフィール"
    ],
    "/ˈproʊfaɪl/",
    "I think that I should probably change my profile picture.",
    "プロフィール写真、変えた方がいいんじゃないかと思うけどな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8178028",
      "license": "CC BY 2.0 FR",
      "attribution": "#8178028 (CK) / #8724460 (small_snow)"
    }
  ],
  [
    "program",
    "A2",
    "名詞・動詞",
    [
      "テレビ番組"
    ],
    "/ˈproʊgræm/",
    "We watched a TV program the other day about your people.",
    "この間あなたたちの国の人についてのテレビを見ました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59899",
      "license": "CC BY 2.0 FR",
      "attribution": "#59899 (CM) / #222569 (mookeee)"
    }
  ],
  [
    "programming",
    "B2",
    "名詞",
    [
      "プログラミング"
    ],
    "/ˈproʊgræmɪŋ/",
    "Each programming language has its advantages and disadvantages.",
    "どのプログラミング言語も一長一短だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10989144",
      "license": "CC BY 2.0 FR",
      "attribution": "#10989144 (CK) / #10989074 (small_snow)"
    }
  ],
  [
    "progressive",
    "B2",
    "形容詞",
    [
      "進歩的な",
      "進歩的な人"
    ],
    "/prəˈgrɛsɪv/",
    "The school introduced a progressive teaching program.",
    "その学校は進歩的な教育制度を導入した。",
    null
  ],
  [
    "promise",
    "A2",
    "名詞・動詞",
    [
      "約束",
      "を約束する"
    ],
    "/ˈprɑməs/",
    "He couldn't fulfill a promise he had made to his father.",
    "彼は父親との約束を果たすことが出来なかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1316751",
      "license": "CC BY 2.0 FR",
      "attribution": "#1316751 (CM) / #100374 (bunbuku)"
    }
  ],
  [
    "promising",
    "B2",
    "形容詞",
    [
      "前途有望な"
    ],
    "/ˈprɑməsɪŋ/",
    "Now he is recognized as one of the most promising writers.",
    "彼は今、最も有望な作家の一人として認められている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/296546",
      "license": "CC BY 2.0 FR",
      "attribution": "#296546 (CK) / #107141 (bunbuku)"
    }
  ],
  [
    "pronounce",
    "A2",
    "動詞",
    [
      "を発音する",
      "を発音記号で示す"
    ],
    "/prəˈnaʊns/",
    "Please tell me how to pronounce this word.",
    "この言葉の発音の仕方を教えて下さい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59394",
      "license": "CC BY 2.0 FR",
      "attribution": "#59394 (CK) / #222069 (bunbuku)"
    }
  ],
  [
    "protein",
    "B2",
    "名詞",
    [
      "蛋白質"
    ],
    "/ˈproʊtin/",
    "Are eggs a good source of protein?",
    "卵にはタンパク質が豊富に含まれているんですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4744158",
      "license": "CC BY 2.0 FR",
      "attribution": "#4744158 (CK) / #8777264 (bunbuku)"
    }
  ],
  [
    "protester",
    "B2",
    "名詞",
    [
      "抗議者"
    ],
    "/ˈproʊtɛstɚ/",
    "Violent clashes broke out between the protesters and the police.",
    "反対派と警察の間で武力衝突が生じた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2961810",
      "license": "CC BY 2.0 FR",
      "attribution": "#2961810 (rsankarpillai) / #2962015 (odango_daisuki)"
    }
  ],
  [
    "proud",
    "B1",
    "形容詞",
    [
      "得意な"
    ],
    "/praʊd/",
    "He is proud of never having been beaten in ping-pong.",
    "彼はピンポンで１度も負けたことのないのを自慢している。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/292575",
      "license": "CC BY 2.0 FR",
      "attribution": "#292575 (CK) / #111112 (bunbuku)"
    }
  ],
  [
    "psychological",
    "B2",
    "形容詞",
    [
      "心理的な",
      "心理学の"
    ],
    "/saɪkəˈlɑdʒɪkəl/",
    "Long isolation can have psychological effects.",
    "長期の孤立は心理的影響をもたらすことがある。",
    null
  ],
  [
    "psychologist",
    "B2",
    "名詞",
    [
      "心理学者"
    ],
    "/saɪˈkɑlədʒəst/",
    "A psychologist helped the team manage stress.",
    "心理学者がチームのストレス管理を助けた。",
    null
  ],
  [
    "pub",
    "A2",
    "名詞",
    [
      "パブ"
    ],
    "/pʌb/",
    "We met for dinner at a pub near the station.",
    "駅近くのパブで夕食を取った。",
    null
  ],
  [
    "public",
    "A2",
    "形容詞・名詞",
    [
      "公共の",
      "公有の"
    ],
    "/ˈpʌblɪk/",
    "This work is in the public domain in the United States.",
    "この著作物は、米国ではパブリックドメインです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7802749",
      "license": "CC BY 2.0 FR",
      "attribution": "#7802749 (Hybrid) / #11255941 (small_snow)"
    }
  ],
  [
    "publication",
    "B2",
    "名詞",
    [
      "出版",
      "出版物"
    ],
    "/pʌblɪˈkeɪʃən/",
    "The book is now ready for publication.",
    "本は現在出版の準備が出来ている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/681582",
      "license": "CC BY 2.0 FR",
      "attribution": "#681582 (Source_VOA) / #1251872 (mookeee)"
    }
  ],
  [
    "publicity",
    "B2",
    "名詞",
    [
      "宣伝",
      "売名"
    ],
    "/pəˈblɪsəti/",
    "That's just a cheap publicity stunt.",
    "それは売名行為だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/42190",
      "license": "CC BY 2.0 FR",
      "attribution": "#42190 (CK) / #204948 (mookeee)"
    }
  ],
  [
    "publishing",
    "B2",
    "名詞",
    [
      "出版業"
    ],
    "/ˈpʌblɪʃɪŋ/",
    "Digital technology has changed the publishing industry.",
    "デジタル技術は出版業界を変えた。",
    null
  ],
  [
    "pull",
    "A2",
    "名詞・動詞",
    [
      "を引っ張って痛める",
      "引っ張る"
    ],
    "/pʊl/",
    "He caught my hand and pulled me to the second floor.",
    "彼は私の手をつかんで二階へ引っ張って行った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/297886",
      "license": "CC BY 2.0 FR",
      "attribution": "#297886 (CM) / #105801 (bunbuku)"
    }
  ],
  [
    "punk",
    "B2",
    "名詞",
    [
      "くだらない",
      "気分がさえない"
    ],
    "/pʌŋk/",
    "I don't really like punk rock very much.",
    "パンクロックはあまり好きじゃないんだよな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6435116",
      "license": "CC BY 2.0 FR",
      "attribution": "#6435116 (CK) / #11668611 (bunbuku)"
    }
  ],
  [
    "pupil",
    "B2",
    "名詞",
    [
      "生徒"
    ],
    "/pˈjupəl/",
    "The teacher handles his pupils well.",
    "あの先生は生徒の扱い方がうまい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/68021",
      "license": "CC BY 2.0 FR",
      "attribution": "#68021 (CK) / #230654 (small_snow)"
    }
  ],
  [
    "purely",
    "B2",
    "副詞",
    [
      "まったく",
      "純粋に"
    ],
    "/pˈjʊrli/",
    "I only found out about it purely by accident.",
    "私がそれに気がついたのはほんの偶然に過ぎません。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/246523",
      "license": "CC BY 2.0 FR",
      "attribution": "#246523 (CK) / #167973 (bunbuku)"
    }
  ],
  [
    "pursuit",
    "B2",
    "名詞",
    [
      "追跡",
      "追求"
    ],
    "/pɚˈsut/",
    "The hounds are in pursuit of the fox.",
    "猟犬たちはそのキツネを追いかけている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325810",
      "license": "CC BY 2.0 FR",
      "attribution": "#325810 (CM) / #77907 (mookeee)"
    }
  ],
  [
    "push",
    "A2",
    "名詞・動詞",
    [
      "押して動かす",
      "を押し進める"
    ],
    "/pʊʃ/",
    "Push the green button and the light will go on.",
    "緑のボタンを押して下さい、すると明かりがつきます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1424468",
      "license": "CC BY 2.0 FR",
      "attribution": "#1424468 (CK) / #77805 (mookeee)"
    }
  ],
  [
    "puzzle",
    "B2",
    "名詞",
    [
      "パズル"
    ],
    "/ˈpʌzəl/",
    "I can't figure out how to solve the puzzle.",
    "そのパズルの解き方がわからないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/44653",
      "license": "CC BY 2.0 FR",
      "attribution": "#44653 (CK) / #160326 (bunbuku)"
    }
  ],
  [
    "qualified",
    "B1",
    "形容詞",
    [
      "資格のある"
    ],
    "/kˈwɑləfaɪd/",
    "He is not qualified for the job.",
    "彼はそのポストの資格を満たしていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291052",
      "license": "CC BY 2.0 FR",
      "attribution": "#291052 (CK) / #992188 (mookeee)"
    }
  ],
  [
    "queen",
    "A2",
    "名詞",
    [
      "女王",
      "女王バチ"
    ],
    "/kwin/",
    "The queen shook hands with each player after the game.",
    "女王は試合後に選手の一人一人と握手をした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267269",
      "license": "CC BY 2.0 FR",
      "attribution": "#267269 (CK) / #147291 (bunbuku)"
    }
  ],
  [
    "question",
    "A2",
    "動詞",
    [
      "問題"
    ],
    "/kˈwɛstʃən/",
    "The person in question is now staying in the Unites States.",
    "問題の人物は目下アメリカに滞在中である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1355366",
      "license": "CC BY 2.0 FR",
      "attribution": "#1355366 (AMIKEMA) / #79860 (KK_kaku_)"
    }
  ],
  [
    "questionnaire",
    "B2",
    "名詞",
    [
      "アンケート"
    ],
    "/kwɛstʃəˈnɛr/",
    "Please fill out this questionnaire and send it to us.",
    "こちらのアンケート用紙に必要事項をご記入いただき、当方までお送りください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61337",
      "license": "CC BY 2.0 FR",
      "attribution": "#61337 (CM) / #9505202 (bunbuku)"
    }
  ],
  [
    "queue",
    "B1",
    "名詞・動詞",
    [
      "列"
    ],
    "/kju/",
    "He was in the queue.",
    "彼はその列の中にいた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291381",
      "license": "CC BY 2.0 FR",
      "attribution": "#291381 (CM) / #112297 (KK_kaku_)"
    }
  ],
  [
    "quietly",
    "A2",
    "副詞",
    [
      "静かに",
      "穏やかに"
    ],
    "/kˈwaɪətli/",
    "She came in quietly so she wouldn't wake up the baby.",
    "赤ん坊を起こさないように、彼女は静かに入ってきた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1513660",
      "license": "CC BY 2.0 FR",
      "attribution": "#1513660 (CK) / #142152 (KK_kaku_)"
    }
  ],
  [
    "quotation",
    "B1",
    "名詞",
    [
      "見積もり",
      "引用"
    ],
    "/kwoʊˈteɪʃən/",
    "We need a firm quotation by Monday.",
    "月曜までに確定見積もりが必要です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238860",
      "license": "CC BY 2.0 FR",
      "attribution": "#238860 (CK) / #175605 (KK_kaku_)"
    }
  ],
  [
    "race",
    "A2",
    "名詞・動詞",
    [
      "人類",
      "競争"
    ],
    "/reɪs/",
    "Nuclear weapons are a threat to the human race.",
    "核兵器は人類にとって脅威だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21723",
      "license": "CC BY 2.0 FR",
      "attribution": "#21723 (AlanF_US) / #184595 (mookeee)"
    }
  ],
  [
    "racing",
    "B1",
    "名詞",
    [
      "ボートレース"
    ],
    "/ˈreɪsɪŋ/",
    "Mountain bike racing has caught on with young Japanese in the past few years.",
    "マウンテンバイクのレースがこの数年、日本の若者の間で流行っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/32877",
      "license": "CC BY 2.0 FR",
      "attribution": "#32877 (CK) / #195702 (KK_kaku_)"
    }
  ],
  [
    "racism",
    "B2",
    "名詞",
    [
      "人種差別"
    ],
    "/ˈreɪsɪzəm/",
    "The organization campaigns against racism in sport.",
    "その団体はスポーツ界の人種差別に反対する活動をしている。",
    null
  ],
  [
    "racist",
    "B2",
    "形容詞・名詞",
    [
      "人種差別主義者",
      "人種差別主義の"
    ],
    "/ˈreɪsɪst/",
    "That politician put his foot in his mouth when he made those racist comments.",
    "あんな人種差別の発言をするなんて、あの政治家も取り返しのつかないことを口にしたものだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66902",
      "license": "CC BY 2.0 FR",
      "attribution": "#66902 (CM) / #229542 (wat)"
    }
  ],
  [
    "radiation",
    "B2",
    "名詞",
    [
      "放射線",
      "放射"
    ],
    "/reɪdiˈeɪʃən/",
    "The equipment measures radiation levels safely.",
    "その装置は放射線量を安全に測定する。",
    null
  ],
  [
    "rail",
    "B2",
    "名詞",
    [
      "レール"
    ],
    "/reɪl/",
    "The car crashed into the guard-rail and rolled down the hill.",
    "車はガードレールに衝突して、丘を転げ落ちて行った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/265542",
      "license": "CC BY 2.0 FR",
      "attribution": "#265542 (CM) / #149016 (tommy__san)"
    }
  ],
  [
    "railway",
    "A2",
    "名詞",
    [
      "線路"
    ],
    "/ˈreɪlweɪ/",
    "Were you going to the railway station when I saw you?",
    "私が会ったとき、あなたは駅へ行くところでしたか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/246657",
      "license": "CC BY 2.0 FR",
      "attribution": "#246657 (CM) / #167841 (bunbuku)"
    }
  ],
  [
    "random",
    "B2",
    "形容詞",
    [
      "手当たりしだいの"
    ],
    "/ˈrændəm/",
    "The people for the experiment were chosen at random.",
    "被験者は無作為に抽出された。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/317882",
      "license": "CC BY 2.0 FR",
      "attribution": "#317882 (CK) / #85830 (tommy_san)"
    }
  ],
  [
    "rank",
    "B2",
    "名詞・動詞",
    [
      "より上位にある"
    ],
    "/ræŋk/",
    "Apes rank above dogs in intelligence.",
    "類人猿は知的には犬より上位である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325997",
      "license": "CC BY 2.0 FR",
      "attribution": "#325997 (CK) / #77722 (mookeee)"
    }
  ],
  [
    "rat",
    "B2",
    "名詞",
    [
      "ネズミ",
      "ネズミをつかまえる"
    ],
    "/ræt/",
    "A bat is no more a bird than a rat is.",
    "ネズミが鳥でないように蝙蝠も鳥ではない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/35799",
      "license": "CC BY 2.0 FR",
      "attribution": "#35799 (CM) / #198606 (wat)"
    }
  ],
  [
    "rating",
    "B2",
    "名詞",
    [
      "評価"
    ],
    "/ˈreɪtɪŋ/",
    "The hotel received a high rating from guests.",
    "そのホテルは宿泊客から高い評価を得た。",
    null
  ],
  [
    "reach",
    "A2",
    "名詞・動詞",
    [
      "に着く"
    ],
    "/ritʃ/",
    "What time will we reach Akita if we take the 9:30 train?",
    "９時半の電車に乗れば、何時に秋田につきますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72276",
      "license": "CC BY 2.0 FR",
      "attribution": "#72276 (CK) / #234900 (e4zh1nmcz)"
    }
  ],
  [
    "realize",
    "A2",
    "動詞",
    [
      "気づく",
      "実現する"
    ],
    "/ˈriəlaɪz/",
    "I didn't realize my wallet was missing until I got home.",
    "家に着くまで、財布がなくなっているのに気がつかなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5565256",
      "license": "CC BY 2.0 FR",
      "attribution": "#5565256 (CK) / #11163395 (small_snow)"
    }
  ],
  [
    "reasonably",
    "B2",
    "副詞",
    [
      "適正に",
      "合理的に"
    ],
    "/ˈrizənəbli/",
    "The meal was reasonably priced and well prepared.",
    "その食事は適正な価格で、よく調理されていた。",
    null
  ],
  [
    "rebuild",
    "B2",
    "動詞",
    [
      "を再建する",
      "再建させる"
    ],
    "/riˈbɪld/",
    "The community raised money to rebuild the school.",
    "地域社会は学校再建のため資金を集めた。",
    null
  ],
  [
    "receive",
    "A2",
    "動詞",
    [
      "を受け取る"
    ],
    "/rəˈsiv/",
    "The winner received a new car from a local car dealer.",
    "優勝者には、地元のカーディーラーから新車が贈呈されました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10948821",
      "license": "CC BY 2.0 FR",
      "attribution": "#10948821 (CM) / #11021642 (small_snow)"
    }
  ],
  [
    "receiver",
    "B2",
    "名詞",
    [
      "受話器"
    ],
    "/rəˈsivɚ/",
    "I put the receiver to my ear.",
    "私は受話器を耳に当てた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/258484",
      "license": "CC BY 2.0 FR",
      "attribution": "#258484 (CK) / #156052 (bunbuku)"
    }
  ],
  [
    "reception",
    "A2",
    "名詞",
    [
      "受付"
    ],
    "/rɪˈsɛpʃən/",
    "Please cover for me at the reception desk for about one hour.",
    "一時間ぐらいの間、私の代わりに受付をやってください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/27756",
      "license": "CC BY 2.0 FR",
      "attribution": "#27756 (CK) / #190596 (bunbuku)"
    }
  ],
  [
    "recession",
    "B2",
    "名詞",
    [
      "不況"
    ],
    "/rɪˈsɛʃən/",
    "A recession is bound to come next year.",
    "来年は不況が避けられませんよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325137",
      "license": "CC BY 2.0 FR",
      "attribution": "#325137 (CM) / #78579 (mookeee)"
    }
  ],
  [
    "recipe",
    "A2",
    "名詞",
    [
      "作り方"
    ],
    "/ˈrɛsəpi/",
    "I read about how to make beef stroganoff in a recipe book.",
    "料理本でビーフストロガノフの作り方を読んだんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10538149",
      "license": "CC BY 2.0 FR",
      "attribution": "#10538149 (CK) / #12990603 (bunbuku)"
    }
  ],
  [
    "reckon",
    "B2",
    "動詞",
    [
      "〜だと思う",
      "見積もる"
    ],
    "/ˈrɛkən/",
    "I reckon the repairs will take about a week.",
    "修理には1週間ほどかかると思う。",
    null
  ],
  [
    "recognition",
    "B2",
    "名詞",
    [
      "気づくこと",
      "認識"
    ],
    "/rɛkəgˈnɪʃən/",
    "She gave me a smile of recognition.",
    "私だとわかって彼女はにっこりとした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/249547",
      "license": "CC BY 2.0 FR",
      "attribution": "#249547 (CK) / #164959 (mookeee)"
    }
  ],
  [
    "recommendation",
    "B1",
    "名詞",
    [
      "推薦状",
      "推薦すること"
    ],
    "/rɛkəmənˈdeɪʃən/",
    "My teacher wrote a recommendation for me.",
    "先生は私のために推薦状を書いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/272977",
      "license": "CC BY 2.0 FR",
      "attribution": "#272977 (CK) / #141593 (small_snow)"
    }
  ],
  [
    "record",
    "A2",
    "名詞・動詞",
    [
      "を録音する"
    ],
    "/rəˈkɔrd/",
    "Please play it back for me after you've finished the recording.",
    "録音が終わったらそれを再生して聞かせてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326488",
      "license": "CC BY 2.0 FR",
      "attribution": "#326488 (CM) / #77231 (mookeee)"
    }
  ],
  [
    "recording",
    "A2",
    "名詞",
    [
      "録音したもの",
      "録音された音"
    ],
    "/rəˈkɔrdɪŋ/",
    "Please play it back for me after you've finished the recording.",
    "録音が終わったらそれを再生して聞かせてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326488",
      "license": "CC BY 2.0 FR",
      "attribution": "#326488 (CM) / #77231 (mookeee)"
    }
  ],
  [
    "recruit",
    "B2",
    "名詞・動詞",
    [
      "新兵を募集する"
    ],
    "/rəˈkrut/",
    "Our basketball team is recruiting tall boys.",
    "うちのバスケット部は背の高い男子を募集している。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/65588",
      "license": "CC BY 2.0 FR",
      "attribution": "#65588 (CM) / #228234 (small_snow)"
    }
  ],
  [
    "recruitment",
    "B2",
    "名詞",
    [
      "採用",
      "募集"
    ],
    "/rəˈkrutmənt/",
    "The company changed its recruitment process.",
    "その会社は採用手続きを変更した。",
    null
  ],
  [
    "recycle",
    "A2",
    "動詞",
    [
      "を再利用する"
    ],
    "/riˈsaɪkəl/",
    "We recycle glass, paper, and metal at home.",
    "私たちは家庭でガラス、紙、金属を再利用する。",
    null
  ],
  [
    "referee",
    "B2",
    "名詞",
    [
      "審判員",
      "の審判をする"
    ],
    "/rɛfɚˈi/",
    "The referee stopped the match because of heavy rain.",
    "審判は大雨のため試合を止めた。",
    null
  ],
  [
    "refugee",
    "B2",
    "名詞",
    [
      "難民"
    ],
    "/ˈrɛfjudʒi/",
    "That boat was full of refugees from Cuba.",
    "そのボートはキューバからの難民で一杯だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/49929",
      "license": "CC BY 2.0 FR",
      "attribution": "#49929 (CK) / #212646 (bunbuku)"
    }
  ],
  [
    "registration",
    "B2",
    "名詞",
    [
      "登録",
      "登録すること"
    ],
    "/rɛdʒɪˈstreɪʃən/",
    "Online registration closes at midnight.",
    "オンライン登録は深夜に締め切られる。",
    null
  ],
  [
    "regularly",
    "B1",
    "副詞",
    [
      "いつも",
      "定期的に"
    ],
    "/ˈrɛgjəlɚli/",
    "I regularly go to bed at nine.",
    "いつも９時には寝ます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66131",
      "license": "CC BY 2.0 FR",
      "attribution": "#66131 (CK) / #228773 (tommy__san)"
    }
  ],
  [
    "regulate",
    "B2",
    "動詞",
    [
      "を規制する",
      "統制する"
    ],
    "/ˈrɛgjəleɪt/",
    "The body helps regulate its own temperature.",
    "身体は自らの体温を調節する。",
    null
  ],
  [
    "reinforce",
    "B2",
    "動詞",
    [
      "補強する"
    ],
    "/riɪnˈfɔrs/",
    "Extra supports reinforce the old bridge.",
    "追加の支柱が古い橋を補強している。",
    null
  ],
  [
    "related",
    "B1",
    "形容詞",
    [
      "関係のある"
    ],
    "/rɪˈleɪtɪd/",
    "Cancer may be related to viruses of some kind.",
    "ガンはある種のウイルスと関係があるかもしれない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63422",
      "license": "CC BY 2.0 FR",
      "attribution": "#63422 (CM) / #226082 (arnab)"
    }
  ],
  [
    "relaxed",
    "B1",
    "形容詞",
    [
      "緊張していない"
    ],
    "/rɪˈlækst/",
    "The locals around here really live at a relaxed pace.",
    "こっちの人はのんびりしてるね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61463",
      "license": "CC BY 2.0 FR",
      "attribution": "#61463 (CM) / #224127 (bunbuku)"
    }
  ],
  [
    "relaxing",
    "B1",
    "形容詞",
    [
      "リラックスできる",
      "くつろいだ"
    ],
    "/rɪˈlæksɪŋ/",
    "A warm bath can be very relaxing after work.",
    "仕事の後の温かい風呂はとてもリラックスできる。",
    null
  ],
  [
    "relieved",
    "B2",
    "形容詞",
    [
      "ほっとする",
      "安心する"
    ],
    "/rɪˈlivd/",
    "We felt relieved when we saw a light in the distance.",
    "遠方に明かりが見えたとき私たちはほっとする思いだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/25795",
      "license": "CC BY 2.0 FR",
      "attribution": "#25795 (CK) / #188649 (bunbuku)"
    }
  ],
  [
    "remark",
    "B2",
    "名詞・動詞",
    [
      "簡単な発言"
    ],
    "/rɪˈmɑrk/",
    "His remark has nothing to do with the subject.",
    "彼の発言はそのテーマとは何の関係もない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/287315",
      "license": "CC BY 2.0 FR",
      "attribution": "#287315 (CM) / #116354 (small_snow)"
    }
  ],
  [
    "remarkably",
    "B2",
    "副詞",
    [
      "驚くほど",
      "著しく"
    ],
    "/rɪˈmɑrkəbli/",
    "The patient recovered remarkably quickly.",
    "その患者は驚くほど速く回復した。",
    null
  ],
  [
    "repeated",
    "B1",
    "形容詞",
    [
      "繰り返して言われる"
    ],
    "/rɪˈpitɪd/",
    "The tragedy must be remembered so that it is not repeated.",
    "同じことが繰り返されないために、その悲劇を忘れてはならない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/44386",
      "license": "CC BY 2.0 FR",
      "attribution": "#44386 (CK) / #123722 (bunbuku)"
    }
  ],
  [
    "reply",
    "A2",
    "名詞・動詞",
    [
      "返事する"
    ],
    "/rɪˈplaɪ/",
    "Being too nervous to reply, he stared at the floor.",
    "あまりにおどおどして返事ができないまま、彼は床を見つめた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/67728",
      "license": "CC BY 2.0 FR",
      "attribution": "#67728 (CM) / #230362 (bunbuku)"
    }
  ],
  [
    "report",
    "A2",
    "動詞",
    [
      "報告"
    ],
    "/riˈpɔrt/",
    "Please hand in the report by the end of the month.",
    "レポートは今月の末日までに提出してください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11642528",
      "license": "CC BY 2.0 FR",
      "attribution": "#11642528 (sundown) / #192333 (bunbuku)"
    }
  ],
  [
    "reporter",
    "A2",
    "名詞",
    [
      "探訪記者"
    ],
    "/rɪˈpɔrtɚ/",
    "He is a reporter for Time magazine.",
    "彼はタイム誌の記者です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291598",
      "license": "CC BY 2.0 FR",
      "attribution": "#291598 (CK) / #112081 (bunbuku)"
    }
  ],
  [
    "reporting",
    "B2",
    "名詞",
    [
      "報道"
    ],
    "/riˈpɔrtɪŋ/",
    "Accurate reporting builds public trust.",
    "正確な報道は社会の信頼を築く。",
    null
  ],
  [
    "researcher",
    "A2",
    "名詞",
    [
      "研究者"
    ],
    "/ˈrisɚtʃɚ/",
    "He was a former university professor and researcher.",
    "彼はかつて大学教授であり、研究者でもあった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/803339",
      "license": "CC BY 2.0 FR",
      "attribution": "#803339 (Source_VOA) / #873954 (thyc244)"
    }
  ],
  [
    "reservation",
    "B1",
    "名詞",
    [
      "予約",
      "予約されたもの"
    ],
    "/rɛzɚˈveɪʃən/",
    "It is necessary that we make a reservation in advance.",
    "前もって予約しておく事が必要です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273612",
      "license": "CC BY 2.0 FR",
      "attribution": "#273612 (CM) / #140960 (bunbuku)"
    }
  ],
  [
    "resign",
    "B2",
    "動詞",
    [
      "辞職する",
      "辞める"
    ],
    "/rɪˈzaɪn/",
    "She decided to resign from her position last month.",
    "彼女は先月、職を辞することにした。",
    null
  ],
  [
    "resolution",
    "B2",
    "名詞",
    [
      "決心すること"
    ],
    "/rɛzəˈluʃən/",
    "He made a resolution to write in his diary every day.",
    "彼は毎日、日記をつける決心をした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1318626",
      "license": "CC BY 2.0 FR",
      "attribution": "#1318626 (CK) / #99810 (bunbuku)"
    }
  ],
  [
    "resort",
    "B2",
    "名詞",
    [
      "最後の手段",
      "行楽地"
    ],
    "/rɪˈzɔrt/",
    "He borrowed some money from his father as a last resort.",
    "彼は、最後の手段として父にお金を借りた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/288135",
      "license": "CC BY 2.0 FR",
      "attribution": "#288135 (CK) / #115535 (tommy__san)"
    }
  ],
  [
    "rest",
    "A2",
    "名詞・動詞",
    [
      "残り",
      "休息"
    ],
    "/rɛst/",
    "I want to live here for the rest of my life.",
    "この先一生ここに住みたいな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10598505",
      "license": "CC BY 2.0 FR",
      "attribution": "#10598505 (CK) / #11601136 (bunbuku)"
    }
  ],
  [
    "restriction",
    "B2",
    "名詞",
    [
      "制限すること",
      "制限されていること"
    ],
    "/riˈstrɪkʃən/",
    "The city introduced a restriction on car traffic.",
    "市は自動車交通への制限を導入した。",
    null
  ],
  [
    "retail",
    "B2",
    "名詞",
    [
      "小売りされる",
      "小売り"
    ],
    "/ˈriteɪl/",
    "The new model will retail for 30,000 yen.",
    "新型は小売価格３万円で販売される。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269278",
      "license": "CC BY 2.0 FR",
      "attribution": "#269278 (CM) / #145285 (mookeee)"
    }
  ],
  [
    "retired",
    "B1",
    "形容詞",
    [
      "引退した",
      "退職者のための"
    ],
    "/rɪˈtaɪrd/",
    "I've retired and I'm going to take it easy for a while.",
    "退職したのでしばらくのんびり暮らすつもりです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275366",
      "license": "CC BY 2.0 FR",
      "attribution": "#275366 (CK) / #137870 (arnab)"
    }
  ],
  [
    "revision",
    "B2",
    "名詞",
    [
      "修正",
      "改訂"
    ],
    "/riˈvɪʒən/",
    "Please put sticky notes on any parts that need revision.",
    "修正が必要な箇所には、付箋を貼っておいてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13569926",
      "license": "CC BY 2.0 FR",
      "attribution": "#13569926 (CK) / #12135714 (small_snow)"
    }
  ],
  [
    "ride",
    "A2",
    "名詞",
    [
      "を乗せて行く",
      "乗せて運ぶ"
    ],
    "/raɪd/",
    "Would you mind giving me a ride to the post office?",
    "郵便局まで乗せていってもらえませんか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/324559",
      "license": "CC BY 2.0 FR",
      "attribution": "#324559 (CK) / #9504356 (bunbuku)"
    }
  ],
  [
    "ridiculous",
    "B2",
    "形容詞",
    [
      "ばかばかしい",
      "おかしな"
    ],
    "/rɪˈdɪkjələs/",
    "Shame on you for getting so flustered. You looked ridiculous.",
    "あんなにおろおろしちゃって恥ずかしいったらありゃしない。馬鹿みたいだったわよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66939",
      "license": "CC BY 2.0 FR",
      "attribution": "#66939 (CK) / #229579 (bunbuku)"
    }
  ],
  [
    "ring",
    "A2",
    "名詞・動詞",
    [
      "指輪",
      "輪"
    ],
    "/rɪŋ/",
    "She found the ring that she had lost during the journey.",
    "彼女は旅行中なくした指輪を見つけた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/317421",
      "license": "CC BY 2.0 FR",
      "attribution": "#317421 (CM) / #86290 (arnab)"
    }
  ],
  [
    "rise",
    "A2",
    "名詞・動詞",
    [
      "立ち上がる"
    ],
    "/raɪz/",
    "The sun rises in the east and sets in the west.",
    "太陽は東から昇り、西へ沈む。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275156",
      "license": "CC BY 2.0 FR",
      "attribution": "#275156 (CK) / #138079 (tommy_san)"
    }
  ],
  [
    "risky",
    "B2",
    "形容詞",
    [
      "危険な"
    ],
    "/ˈrɪski/",
    "It is risky for you to go into that area alone.",
    "君が一人でその地域に行くのは危険だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/17932",
      "license": "CC BY 2.0 FR",
      "attribution": "#17932 (wwkudu) / #179076 (KK_kaku_)"
    }
  ],
  [
    "rival",
    "B2",
    "形容詞・名詞",
    [
      "太刀打ちする",
      "競争相手"
    ],
    "/ˈraɪvəl/",
    "When it comes to good quality wine, no country can rival France.",
    "良質のぶどう酒ではフランスに太刀打ちできる国はない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1411302",
      "license": "CC BY 2.0 FR",
      "attribution": "#1411302 (CK) / #77834 (mookeee)"
    }
  ],
  [
    "rob",
    "B2",
    "動詞",
    [
      "から金品を盗む",
      "からむりやりに取ってしまう"
    ],
    "/rɑb/",
    "Two people tried to rob the small shop.",
    "2人がその小さな店を襲って金品を奪おうとした。",
    null
  ],
  [
    "robbery",
    "B2",
    "名詞",
    [
      "強盗罪"
    ],
    "/ˈrɑbɚi/",
    "The police arrested a suspect in connection with the robbery.",
    "警察はその強盗事件に関連のある容疑者を逮捕した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238215",
      "license": "CC BY 2.0 FR",
      "attribution": "#238215 (CK) / #237018 (mookeee)"
    }
  ],
  [
    "robot",
    "B1",
    "名詞",
    [
      "ロボット"
    ],
    "/ˈroʊbɑt/",
    "Robots have taken the place of men in this factory.",
    "この工場ではロボットが従業員に取って代わった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59311",
      "license": "CC BY 2.0 FR",
      "attribution": "#59311 (CM) / #236859 (mookeee)"
    }
  ],
  [
    "rock",
    "A2",
    "名詞",
    [
      "岩",
      "岩のように強固なもの"
    ],
    "/rɑk/",
    "Seen at a distance, the rock looked like a human face.",
    "少し離れて見ると、その岩は人の顔のようでした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267792",
      "license": "CC BY 2.0 FR",
      "attribution": "#267792 (CK) / #146769 (bunbuku)"
    }
  ],
  [
    "rocket",
    "B2",
    "名詞",
    [
      "ロケット",
      "ロケット弾"
    ],
    "/ˈrɑkət/",
    "They're going to send up a rocket.",
    "彼らはロケットを打ち上げようとしている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9611121",
      "license": "CC BY 2.0 FR",
      "attribution": "#9611121 (CK) / #97577 (arnab)"
    }
  ],
  [
    "romance",
    "B2",
    "名詞",
    [
      "恋愛物語",
      "恋愛事件"
    ],
    "/roʊˈmæns/",
    "The novel combines mystery with romance.",
    "その小説は謎と恋愛を組み合わせている。",
    null
  ],
  [
    "romantic",
    "B1",
    "形容詞",
    [
      "ロマンチックな",
      "ロマンチックな人"
    ],
    "/roʊˈmæntɪk/",
    "I imagined my first kiss would be more romantic.",
    "ファーストキスは、もっとロマンチックなの想像してたのに。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327254",
      "license": "CC BY 2.0 FR",
      "attribution": "#327254 (CK) / #76466 (bunbuku)"
    }
  ],
  [
    "roof",
    "A2",
    "名詞",
    [
      "屋根",
      "屋根に似た物"
    ],
    "/ruf/",
    "The explosion was so powerful that the roof was blown off.",
    "爆発がとてもすさまじかったので、屋根が吹っとんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9432077",
      "license": "CC BY 2.0 FR",
      "attribution": "#9432077 (CK) / #121386 (bunbuku)"
    }
  ],
  [
    "root",
    "B2",
    "名詞",
    [
      "根"
    ],
    "/rut/",
    "We learned at school that the square root of nine is three.",
    "僕らは９の平方根は３だと学校で習った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322003",
      "license": "CC BY 2.0 FR",
      "attribution": "#322003 (CK) / #81712 (bunbuku)"
    }
  ],
  [
    "rope",
    "B1",
    "名詞",
    [
      "ロープ",
      "ロープス"
    ],
    "/roʊp/",
    "Don't let go of the rope until I tell you to.",
    "私がいいって言うまでロープを放さないでね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9637783",
      "license": "CC BY 2.0 FR",
      "attribution": "#9637783 (CK) / #167372 (small_snow)"
    }
  ],
  [
    "rose",
    "B2",
    "名詞",
    [
      "バラの花",
      "バラの木"
    ],
    "/roʊz/",
    "The girl brought me a red and a white rose.",
    "少女は赤いバラと白いバラを１本ずつ私にもってきてくれた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267871",
      "license": "CC BY 2.0 FR",
      "attribution": "#267871 (CK) / #146690 (tommy__san)"
    }
  ],
  [
    "round",
    "A2",
    "形容詞・副詞・名詞・前置詞",
    [
      "を一周して"
    ],
    "/raʊnd/",
    "My dream is to take a round-the-world trip.",
    "夢は、世界一周旅行。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322756",
      "license": "CC BY 2.0 FR",
      "attribution": "#322756 (CK) / #80959 (KK_kaku_)"
    }
  ],
  [
    "rubber",
    "B2",
    "形容詞・名詞",
    [
      "ゴム",
      "ゴムの製品"
    ],
    "/ˈrʌbɚ/",
    "Tom put on some rubber gloves so he wouldn't leave fingerprints.",
    "トムは指紋を残さないようにゴム手袋をつけた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1889708",
      "license": "CC BY 2.0 FR",
      "attribution": "#1889708 (CK) / #2858280 (tommy_san)"
    }
  ],
  [
    "rugby",
    "B1",
    "名詞",
    [
      "ラグビー"
    ],
    "/ˈrʌgbi/",
    "My whole body was one big bruise after the rugby game.",
    "ラグビーの試合後、私の体は全身あざだらけだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/29807",
      "license": "CC BY 2.0 FR",
      "attribution": "#29807 (CK) / #1869159 (bunbuku)"
    }
  ],
  [
    "run",
    "A2",
    "名詞",
    [
      "流れる"
    ],
    "/rʌn/",
    "She came very near to being run over by a car.",
    "彼女は危うく自動車にひかれるところだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/388644",
      "license": "CC BY 2.0 FR",
      "attribution": "#388644 (CK) / #90624 (bunbuku)"
    }
  ],
  [
    "runner",
    "A2",
    "名詞",
    [
      "走者",
      "競走者"
    ],
    "/ˈrʌnɚ/",
    "The runner jumped over the hole in the ground.",
    "その走者は地面に空いた穴を飛び越えた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/681672",
      "license": "CC BY 2.0 FR",
      "attribution": "#681672 (Source_VOA) / #878483 (thyc244)"
    }
  ],
  [
    "running",
    "A2",
    "名詞",
    [
      "走っている",
      "絶え間のない"
    ],
    "/ˈrʌnɪŋ/",
    "It doesn't work so well because the batteries are running down.",
    "電池がなくなってきてるから、うまく動かないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/279225",
      "license": "CC BY 2.0 FR",
      "attribution": "#279225 (CK) / #10004590 (bunbuku)"
    }
  ],
  [
    "sadly",
    "A2",
    "副詞",
    [
      "悲しそうに"
    ],
    "/ˈsædli/",
    "Smiling sadly, she began to talk.",
    "悲しそうに微笑みながら、彼女は話しはじめた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/317755",
      "license": "CC BY 2.0 FR",
      "attribution": "#317755 (CM) / #85957 (bunbuku)"
    }
  ],
  [
    "safe",
    "A2",
    "形容詞",
    [
      "安全な",
      "危険のない"
    ],
    "/seɪf/",
    "This place isn't as safe as it used to be.",
    "この場所は以前ほど安全じゃないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3238912",
      "license": "CC BY 2.0 FR",
      "attribution": "#3238912 (CK) / #11865337 (bunbuku)"
    }
  ],
  [
    "safety",
    "B1",
    "名詞",
    [
      "安全",
      "安全装置"
    ],
    "/ˈseɪfti/",
    "The pilot of an airliner is responsible for the safety of passengers.",
    "旅客機のパイロットは乗客の安全に対し責任がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325526",
      "license": "CC BY 2.0 FR",
      "attribution": "#325526 (CM) / #78192 (mookeee)"
    }
  ],
  [
    "sail",
    "A2",
    "名詞・動詞",
    [
      "ヨットを操る"
    ],
    "/seɪl/",
    "Several yachts were sailing side by side far out at sea.",
    "数艘のヨットが、はるか沖合を並んで航行していた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270981",
      "license": "CC BY 2.0 FR",
      "attribution": "#270981 (CM) / #143586 (bunbuku)"
    }
  ],
  [
    "sailing",
    "A2",
    "名詞",
    [
      "ヨット遊び"
    ],
    "/ˈseɪlɪŋ/",
    "Several yachts were sailing side by side far out at sea.",
    "数艘のヨットが、はるか沖合を並んで航行していた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270981",
      "license": "CC BY 2.0 FR",
      "attribution": "#270981 (CM) / #143586 (bunbuku)"
    }
  ],
  [
    "sailor",
    "B1",
    "名詞",
    [
      "船員"
    ],
    "/ˈseɪlɚ/",
    "Each sailor wore a life jacket on deck.",
    "船員は甲板でそれぞれ救命胴衣を着ていた。",
    null
  ],
  [
    "salary",
    "A2",
    "名詞",
    [
      "給料"
    ],
    "/ˈsælɚi/",
    "I wonder if he can live on such a small salary.",
    "彼はあんな安月給で暮らしていけるのかしら。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/288930",
      "license": "CC BY 2.0 FR",
      "attribution": "#288930 (CM) / #114741 (small_snow)"
    }
  ],
  [
    "sale",
    "A2",
    "名詞",
    [
      "売り上げ",
      "安売り"
    ],
    "/seɪl/",
    "Making such a large sale is a feather in the salesman's cap.",
    "そのように売り上げが大きいとは、セールスマンにとって名誉である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/49749",
      "license": "CC BY 2.0 FR",
      "attribution": "#49749 (CM) / #212466 (mookeee)"
    }
  ],
  [
    "sand",
    "B1",
    "名詞",
    [
      "砂",
      "に砂をまく"
    ],
    "/sænd/",
    "The old man loaded his mule with bags full of sand.",
    "老人はラバに砂のいっぱい入った袋をのせた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326439",
      "license": "CC BY 2.0 FR",
      "attribution": "#326439 (CK) / #77280 (mookeee)"
    }
  ],
  [
    "sauce",
    "A2",
    "名詞",
    [
      "ソース",
      "をソースで味つけする"
    ],
    "/sɔs/",
    "I'd like to have the sauce on the side, please.",
    "ソースは別添えでお願いします。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/51050",
      "license": "CC BY 2.0 FR",
      "attribution": "#51050 (CK) / #11325772 (bunbuku)"
    }
  ],
  [
    "save",
    "A2",
    "動詞",
    [
      "を残しておく"
    ],
    "/seɪv/",
    "She is trying to save as much money as she can.",
    "彼女は出来るだけお金を溜めようと努力している。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309982",
      "license": "CC BY 2.0 FR",
      "attribution": "#309982 (CK) / #88746 (mookeee)"
    }
  ],
  [
    "scandal",
    "B2",
    "名詞",
    [
      "醜聞"
    ],
    "/ˈskændəl/",
    "He is said to have something to do with the political scandal.",
    "彼は汚職と何らかの関係があるといわれています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/294138",
      "license": "CC BY 2.0 FR",
      "attribution": "#294138 (CK) / #109552 (small_snow)"
    }
  ],
  [
    "scary",
    "A2",
    "形容詞",
    [
      "恐ろしい"
    ],
    "/ˈskɛri/",
    "The movie that we watched last night was really scary.",
    "昨日の夜観た映画さ、めちゃめちゃ怖かったんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7796829",
      "license": "CC BY 2.0 FR",
      "attribution": "#7796829 (CK) / #11859248 (bunbuku)"
    }
  ],
  [
    "scenario",
    "B2",
    "名詞",
    [
      "想定",
      "シナリオ"
    ],
    "/sɪˈnɛrioʊ/",
    "Let's consider the worst case scenario.",
    "最悪の場合を考えておこう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13573975",
      "license": "CC BY 2.0 FR",
      "attribution": "#13573975 (CK) / #4776 (bunbuku)"
    }
  ],
  [
    "scholarship",
    "B2",
    "名詞",
    [
      "奨学金"
    ],
    "/ˈskɑlɚʃɪp/",
    "She was able to go to college thanks to the scholarship.",
    "彼女は奨学金のおかげで大学に進学することができた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/315001",
      "license": "CC BY 2.0 FR",
      "attribution": "#315001 (CM) / #88706 (mookeee)"
    }
  ],
  [
    "screening",
    "B2",
    "名詞",
    [
      "検診",
      "上映"
    ],
    "/ˈskrinɪŋ/",
    "Early screening can detect the disease.",
    "早期検診でその病気を発見できる。",
    null
  ],
  [
    "script",
    "B1",
    "名詞",
    [
      "台本"
    ],
    "/skrɪpt/",
    "Please go over the script.",
    "台本に目を通しておいてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275464",
      "license": "CC BY 2.0 FR",
      "attribution": "#275464 (CM) / #137772 (KK_kaku_)"
    }
  ],
  [
    "sculpture",
    "B1",
    "名詞",
    [
      "彫刻",
      "彫刻術"
    ],
    "/ˈskʌlptʃɚ/",
    "A stone sculpture stands in the garden.",
    "庭に石の彫刻が立っている。",
    null
  ],
  [
    "season",
    "A2",
    "名詞",
    [
      "季節",
      "時期"
    ],
    "/ˈsizən/",
    "This year's rainy season is going to be a long one.",
    "今年の梅雨は長引きそうですね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10576636",
      "license": "CC BY 2.0 FR",
      "attribution": "#10576636 (CK) / #3024524 (tommy_san)"
    }
  ],
  [
    "seat",
    "A2",
    "名詞・動詞",
    [
      "席",
      "腰掛け"
    ],
    "/sit/",
    "Please have a seat and wait until your name is called.",
    "名前を呼ばれるまで、椅子にかけてお待ちください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322950",
      "license": "CC BY 2.0 FR",
      "attribution": "#322950 (CK) / #80765 (bunbuku)"
    }
  ],
  [
    "second",
    "A2",
    "副詞",
    [
      "第2の"
    ],
    "/ˈsɛkənd/",
    "He caught my hand and pulled me to the second floor.",
    "彼は私の手をつかんで二階へ引っ張って行った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/297886",
      "license": "CC BY 2.0 FR",
      "attribution": "#297886 (CM) / #105801 (bunbuku)"
    }
  ],
  [
    "secondary",
    "B1",
    "形容詞",
    [
      "二次的な",
      "第2の"
    ],
    "/ˈsɛkəndɛri/",
    "He got all his information from secondary sources.",
    "彼は情報をすべて又聞きで得た。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/299735",
      "license": "CC BY 2.0 FR",
      "attribution": "#299735 (CM) / #103957 (tommy__san)"
    }
  ],
  [
    "secondly",
    "A2",
    "副詞",
    [
      "第二に"
    ],
    "/ˈsɛkəndli/",
    "Secondly, we must consider the environmental cost.",
    "第二に、環境上の費用を考えなければならない。",
    null
  ],
  [
    "secret",
    "A2",
    "形容詞・名詞",
    [
      "ないしょにする",
      "ないしょの話"
    ],
    "/ˈsikrət/",
    "Please tell me the secret to making good jam.",
    "おいしいジャムを作る秘訣を教えてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/65194",
      "license": "CC BY 2.0 FR",
      "attribution": "#65194 (CK) / #227841 (tommy__san)"
    }
  ],
  [
    "secretary",
    "A2",
    "名詞",
    [
      "秘書",
      "秘書官"
    ],
    "/ˈsɛkrətɛri/",
    "He had to let his secretary go because she got married.",
    "秘書が結婚するというので、彼は彼女を手放さなければならなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1316900",
      "license": "CC BY 2.0 FR",
      "attribution": "#1316900 (CK) / #1149232 (mookeee)"
    }
  ],
  [
    "seed",
    "B1",
    "名詞",
    [
      "種"
    ],
    "/sid/",
    "Squirrels eat seeds and nuts, as well as insects and mushrooms.",
    "リスは種やナッツ、そして虫やキノコも食べます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2761168",
      "license": "CC BY 2.0 FR",
      "attribution": "#2761168 (Hybrid) / #8933462 (small_snow)"
    }
  ],
  [
    "seeker",
    "B2",
    "名詞",
    [
      "求職者",
      "探し求める人"
    ],
    "/ˈsikɚ/",
    "Each job seeker received help with applications.",
    "求職者はそれぞれ応募の支援を受けた。",
    null
  ],
  [
    "seem",
    "A2",
    "動詞",
    [
      "見える"
    ],
    "/sim/",
    "You seem to have made considerable progress since our last meeting.",
    "前回君に会ってから、かなり進歩したようだね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10168251",
      "license": "CC BY 2.0 FR",
      "attribution": "#10168251 (AlanF_US) / #1240857 (bunbuku)"
    }
  ],
  [
    "self",
    "B2",
    "名詞",
    [
      "自己",
      "自分"
    ],
    "/sɛlf/",
    "Travel helped him develop a stronger sense of self.",
    "旅を通じて彼はより確かな自己意識を育てた。",
    null
  ],
  [
    "seminar",
    "B2",
    "名詞",
    [
      "セミナー"
    ],
    "/ˈsɛmənɑr/",
    "The professor led a seminar on climate policy.",
    "教授は気候政策についてのゼミを行った。",
    null
  ],
  [
    "servant",
    "B1",
    "名詞",
    [
      "召使"
    ],
    "/ˈsɝvənt/",
    "If you behave like a servant, you'll be treated like a servant.",
    "召使いのように振舞っていると、召使いのように扱われるぞ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/942841",
      "license": "CC BY 2.0 FR",
      "attribution": "#942841 (CK) / #942830 (thyc244)"
    }
  ],
  [
    "set",
    "B1",
    "名詞・動詞",
    [
      "組み立てる"
    ],
    "/sɛt/",
    "It took us half an hour to set up the tent.",
    "テントを組み立てるのに３０分かかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/39126",
      "license": "CC BY 2.0 FR",
      "attribution": "#39126 (CK) / #201915 (bunbuku)"
    }
  ],
  [
    "setting",
    "B1",
    "名詞",
    [
      "設定",
      "環境"
    ],
    "/ˈsɛtɪŋ/",
    "Connection to the server failed. Please check your network settings.",
    "サーバーへの接続に失敗しました。ネットワーク設定を確認してください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13571849",
      "license": "CC BY 2.0 FR",
      "attribution": "#13571849 (CK) / #3049606 (tommy_san)"
    }
  ],
  [
    "settler",
    "B2",
    "名詞",
    [
      "入植者"
    ],
    "/ˈsɛtəlɚ/",
    "Each early settler faced a difficult winter.",
    "初期の入植者は皆、厳しい冬に直面した。",
    null
  ],
  [
    "several",
    "A2",
    "限定詞・名詞",
    [
      "いくつかの"
    ],
    "/ˈsɛvrəl/",
    "Several yachts were sailing side by side far out at sea.",
    "数艘のヨットが、はるか沖合を並んで航行していた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270981",
      "license": "CC BY 2.0 FR",
      "attribution": "#270981 (CM) / #143586 (bunbuku)"
    }
  ],
  [
    "severely",
    "B2",
    "副詞",
    [
      "重度に",
      "ひどく"
    ],
    "/səˈvɪrli/",
    "The severely injured man was dead on arrival at the hospital.",
    "重傷を負った男性は病院に着いた時既に亡くなっていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/266585",
      "license": "CC BY 2.0 FR",
      "attribution": "#266585 (CK) / #147974 (wat)"
    }
  ],
  [
    "sex",
    "B1",
    "名詞",
    [
      "性"
    ],
    "/sɛks/",
    "Same-sex couples should be able to get married.",
    "同性のカップルも結婚できるべきだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1754176",
      "license": "CC BY 2.0 FR",
      "attribution": "#1754176 (Spamster) / #1754195 (mookeee)"
    }
  ],
  [
    "sexual",
    "B1",
    "形容詞",
    [
      "性の"
    ],
    "/ˈsɛkʃuəl/",
    "Sexual harassment has now become a social issue.",
    "今、性的嫌がらせは社会的問題になっています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/51336",
      "license": "CC BY 2.0 FR",
      "attribution": "#51336 (CM) / #10136067 (small_snow)"
    }
  ],
  [
    "sexy",
    "B2",
    "形容詞",
    [
      "セクシーな"
    ],
    "/ˈsɛksi/",
    "There are women who find bald men sexy.",
    "ハゲている男性をセクシーだと思う女性もいます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11746272",
      "license": "CC BY 2.0 FR",
      "attribution": "#11746272 (CK) / #11742192 (bunbuku)"
    }
  ],
  [
    "shake",
    "A2",
    "名詞・動詞",
    [
      "揺れ",
      "揺れる"
    ],
    "/ʃeɪk/",
    "The ground started to shake and the alarm rang.",
    "大地が揺れ始め、警報が鳴り響いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1713903",
      "license": "CC BY 2.0 FR",
      "attribution": "#1713903 (marcelostockle) / #1904275 (Unaden)"
    }
  ],
  [
    "shall",
    "A2",
    "動詞",
    [
      "しましょうか",
      "させましょうか"
    ],
    "/ʃæl/",
    "Shall I ask her to send the book to us?",
    "彼女にその本を送ってくれと頼みましょうか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/308663",
      "license": "CC BY 2.0 FR",
      "attribution": "#308663 (CM) / #95043 (small_snow)"
    }
  ],
  [
    "shaped",
    "B2",
    "形容詞",
    [
      "「…を形した」「…形の」の意を表す"
    ],
    "/ʃeɪpt/",
    "I found a stone shaped like a heart.",
    "ハート形の石を見つけたよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9741199",
      "license": "CC BY 2.0 FR",
      "attribution": "#9741199 (DJ_Saidez) / #9741210 (small_snow)"
    }
  ],
  [
    "sheet",
    "A2",
    "名詞",
    [
      "1枚"
    ],
    "/ʃit/",
    "The box is covered with a large sheet of paper.",
    "その箱は一枚の大きな紙で覆われている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/44462",
      "license": "CC BY 2.0 FR",
      "attribution": "#44462 (CK) / #207210 (mookeee)"
    }
  ],
  [
    "shelf",
    "B1",
    "名詞",
    [
      "たな"
    ],
    "/ʃɛlf/",
    "I can't reach the top shelf unless I stand on a chair.",
    "私、イスの上に乗らないと、一番上の棚に手が届かないのよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7791448",
      "license": "CC BY 2.0 FR",
      "attribution": "#7791448 (CK) / #8919790 (bunbuku)"
    }
  ],
  [
    "shell",
    "B1",
    "名詞",
    [
      "殻",
      "の殻を取る"
    ],
    "/ʃɛl/",
    "The shell of an egg is easily broken.",
    "卵の殻は壊れやすい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325215",
      "license": "CC BY 2.0 FR",
      "attribution": "#325215 (CM) / #78500 (mookeee)"
    }
  ],
  [
    "shiny",
    "B1",
    "形容詞",
    [
      "着古して光る"
    ],
    "/ˈʃaɪni/",
    "The car is waxed and shiny.",
    "その車はワックスがかけられてピカピカしている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12420124",
      "license": "CC BY 2.0 FR",
      "attribution": "#12420124 (CK) / #209576 (bunbuku)"
    }
  ],
  [
    "ship",
    "A2",
    "名詞・動詞",
    [
      "船"
    ],
    "/ʃɪp/",
    "The ship sounded its whistle and pulled away from the dock.",
    "船は汽笛を鳴らして、埠頭を離れました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10136205",
      "license": "CC BY 2.0 FR",
      "attribution": "#10136205 (CK) / #10136241 (small_snow)"
    }
  ],
  [
    "shooting",
    "B2",
    "名詞",
    [
      "銃撃",
      "射撃"
    ],
    "/ˈʃutɪŋ/",
    "The man suddenly started shooting his gun.",
    "その男は突然、銃を撃ち始めた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/45274",
      "license": "CC BY 2.0 FR",
      "attribution": "#45274 (CK) / #208017 (Blanka_Meduzo)"
    }
  ],
  [
    "shore",
    "B2",
    "名詞",
    [
      "海岸",
      "岸"
    ],
    "/ʃɔr/",
    "I saw a fishing boat about a mile off the shore.",
    "海岸から約１マイル沖に漁船が見えた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/22181",
      "license": "CC BY 2.0 FR",
      "attribution": "#22181 (CK) / #185050 (bunbuku)"
    }
  ],
  [
    "short-term",
    "B2",
    "形容詞",
    [
      "短期間の",
      "短期満期の"
    ],
    "/ʃɔrt tɝm/",
    "The loan provides short-term support for small firms.",
    "その融資は小企業へ短期的な支援を提供する。",
    null
  ],
  [
    "shot",
    "B2",
    "名詞",
    [
      "発射音",
      "発砲"
    ],
    "/ʃɑt/",
    "A rifle shot broke the peace of the early morning.",
    "ライフルの発射音が早朝の静けさを破った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/29822",
      "license": "CC BY 2.0 FR",
      "attribution": "#29822 (CM) / #192658 (mookeee)"
    }
  ],
  [
    "shoulder",
    "A2",
    "名詞",
    [
      "肩"
    ],
    "/ˈʃoʊldɚ/",
    "I can't concentrate if you keep tapping me on the shoulder.",
    "ずっと肩を叩かれると集中できない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1951420",
      "license": "CC BY 2.0 FR",
      "attribution": "#1951420 (CK) / #10905948 (SomeHungryBois)"
    }
  ],
  [
    "shout",
    "A2",
    "名詞・動詞",
    [
      "叫ぶ",
      "大声を出す"
    ],
    "/ʃaʊt/",
    "On hearing of the victory, the whole nation shouted for joy.",
    "勝利の知らせに国中が喜びに沸いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267393",
      "license": "CC BY 2.0 FR",
      "attribution": "#267393 (CM) / #147168 (tommy__san)"
    }
  ],
  [
    "shut",
    "A2",
    "形容詞・動詞",
    [
      "を閉める"
    ],
    "/ʃʌt/",
    "Keep your eyes wide open before marriage and half shut afterwards.",
    "結婚前は両目を見開き、結婚したら片目をつぶれ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5168744",
      "license": "CC BY 2.0 FR",
      "attribution": "#5168744 (CK) / #3468911 (arnab)"
    }
  ],
  [
    "shy",
    "B1",
    "形容詞",
    [
      "欠けている"
    ],
    "/ʃaɪ/",
    "My kid is shy around strangers and always hides behind me.",
    "うちの子、人見知りが激しくて、いつも私の後ろに隠れてしまうの。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1355261",
      "license": "CC BY 2.0 FR",
      "attribution": "#1355261 (CK) / #1353839 (bunbuku)"
    }
  ],
  [
    "sibling",
    "B2",
    "名詞",
    [
      "きょうだい"
    ],
    "/ˈsɪblɪŋ/",
    "I've always wondered what it'd be like to have siblings.",
    "兄弟がいるとどんなだろうといつも思う。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1345",
      "license": "CC BY 2.0 FR",
      "attribution": "#1345 (human600) / #4769 (bunbuku)"
    }
  ],
  [
    "side",
    "A2",
    "名詞",
    [
      "端"
    ],
    "/saɪd/",
    "A police car has stopped on the side of the road.",
    "道端にパトカーがとまってます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1223474",
      "license": "CC BY 2.0 FR",
      "attribution": "#1223474 (CK) / #123547 (small_snow)"
    }
  ],
  [
    "signature",
    "B2",
    "名詞",
    [
      "署名"
    ],
    "/ˈsɪgnətʃɚ/",
    "I attached my signature to the document.",
    "私は書類に署名した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/258594",
      "license": "CC BY 2.0 FR",
      "attribution": "#258594 (CK) / #155942 (bunbuku)"
    }
  ],
  [
    "significance",
    "B2",
    "名詞",
    [
      "重要性"
    ],
    "/səgˈnɪfɪkəns/",
    "Few people understood the significance of the discovery.",
    "その発見の重要性を理解した人は少なかった。",
    null
  ],
  [
    "silk",
    "B2",
    "名詞",
    [
      "絹製の"
    ],
    "/sɪlk/",
    "That dress is made out of silk.",
    "そのドレスは絹製です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11059742",
      "license": "CC BY 2.0 FR",
      "attribution": "#11059742 (CK) / #212868 (KK_kaku_)"
    }
  ],
  [
    "silly",
    "B1",
    "形容詞",
    [
      "愚かな"
    ],
    "/ˈsɪli/",
    "It is silly of me to have made the same mistake twice.",
    "また同じ失敗をするなんて、我ながら愚かだと思う。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/32574",
      "license": "CC BY 2.0 FR",
      "attribution": "#32574 (CM) / #195400 (bunbuku)"
    }
  ],
  [
    "silver",
    "A2",
    "形容詞・名詞",
    [
      "銀",
      "銀の食器類"
    ],
    "/ˈsɪlvɚ/",
    "She wore a simple silver necklace to the ceremony.",
    "彼女は式典にシンプルな銀のネックレスを着けた。",
    null
  ],
  [
    "similarity",
    "B1",
    "名詞",
    [
      "類似",
      "類似点"
    ],
    "/sɪməˈlɛrəti/",
    "The similarity between the two designs is striking.",
    "その2つの設計の類似は目を引く。",
    null
  ],
  [
    "simple",
    "A2",
    "形容詞",
    [
      "単純な"
    ],
    "/ˈsɪmpəl/",
    "This work is so simple even a child can do it.",
    "この仕事は単純なので子供にもできる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9955956",
      "license": "CC BY 2.0 FR",
      "attribution": "#9955956 (CK) / #221795 (Blanka_Meduzo)"
    }
  ],
  [
    "since",
    "A2",
    "副詞・接続詞・前置詞",
    [
      "〜して以来",
      "〜なので"
    ],
    "/sɪns/",
    "It's been a long time since we last saw each other.",
    "ほんとうに久しぶりに会いましたね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1448397",
      "license": "CC BY 2.0 FR",
      "attribution": "#1448397 (CK) / #195897 (bunbuku)"
    }
  ],
  [
    "singing",
    "A2",
    "名詞",
    [
      "歌"
    ],
    "/ˈsɪŋɪŋ/",
    "We did a lot of singing and dancing at the party.",
    "パーティでは大いに歌い踊りました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/35614",
      "license": "CC BY 2.0 FR",
      "attribution": "#35614 (CK) / #198423 (bunbuku)"
    }
  ],
  [
    "single",
    "A2",
    "形容詞・名詞",
    [
      "たった一つの"
    ],
    "/ˈsɪŋgəl/",
    "We've not had a single drop of rain for two weeks.",
    "２週間の間たった１滴も雨は降らなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10541821",
      "license": "CC BY 2.0 FR",
      "attribution": "#10541821 (CK) / #235479 (arnab)"
    }
  ],
  [
    "sink",
    "B1",
    "動詞",
    [
      "流し台"
    ],
    "/sɪŋk/",
    "I thought that you were going to fix the sink.",
    "あなたが流し台の修理をしてくれるのだと思っていました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7171988",
      "license": "CC BY 2.0 FR",
      "attribution": "#7171988 (CK) / #2056699 (bunbuku)"
    }
  ],
  [
    "sir",
    "A2",
    "名詞",
    [
      "お客様",
      "〜さん"
    ],
    "/sɝ/",
    "I'm sorry, sir, but a jacket and tie are required.",
    "お客様、申し訳ありませんが、上着とネクタイの着用をお願いいたします。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/64670",
      "license": "CC BY 2.0 FR",
      "attribution": "#64670 (CM) / #227319 (bunbuku)"
    }
  ],
  [
    "size",
    "A2",
    "名詞",
    [
      "サイズ",
      "にサイズを塗る"
    ],
    "/saɪz/",
    "We have the extra-large size, but not in that color.",
    "特大のサイズはあるんですが、その色のは切らしております。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/280536",
      "license": "CC BY 2.0 FR",
      "attribution": "#280536 (CK) / #123461 (bunbuku)"
    }
  ],
  [
    "ski",
    "A2",
    "形容詞・名詞・動詞",
    [
      "スキー",
      "スキーで滑走する"
    ],
    "/ski/",
    "My little sister asked me to teach her how to ski.",
    "妹がスキーを教えてほしいと私に頼んできた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5306949",
      "license": "CC BY 2.0 FR",
      "attribution": "#5306949 (AlanF_US) / #81399 (bunbuku)"
    }
  ],
  [
    "skiing",
    "A2",
    "名詞",
    [
      "スキー",
      "スキー術"
    ],
    "/ˈskiɪŋ/",
    "We're torn between going to a hot spring and going skiing.",
    "今、温泉に行くかスキーに行くかもめているんだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241548",
      "license": "CC BY 2.0 FR",
      "attribution": "#241548 (CM) / #172925 (KK_kaku_)"
    }
  ],
  [
    "skin",
    "A2",
    "名詞",
    [
      "肌"
    ],
    "/skɪn/",
    "Staying up late at night is very bad for your skin.",
    "夜更かしはお肌の大敵だよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/888680",
      "license": "CC BY 2.0 FR",
      "attribution": "#888680 (Scott) / #886071 (bunbuku)"
    }
  ],
  [
    "skull",
    "B2",
    "名詞",
    [
      "頭"
    ],
    "/skʌl/",
    "The helmet protects the skull from injury.",
    "ヘルメットは頭蓋骨をけがから守る。",
    null
  ],
  [
    "sky",
    "A2",
    "名詞",
    [
      "空",
      "を高く打ち上げる"
    ],
    "/skaɪ/",
    "He laid on his back and looked up at the sky.",
    "彼は仰向けになって空を見上げた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/295391",
      "license": "CC BY 2.0 FR",
      "attribution": "#295391 (CM) / #108295 (arnab)"
    }
  ],
  [
    "slave",
    "B2",
    "名詞",
    [
      "奴隷"
    ],
    "/sleɪv/",
    "I refuse to be treated like a slave by you.",
    "お前に隷従する気なんかないからな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/17451",
      "license": "CC BY 2.0 FR",
      "attribution": "#17451 (CK) / #2269262 (tommy_san)"
    }
  ],
  [
    "sleep",
    "A2",
    "名詞",
    [
      "葬られている"
    ],
    "/slip/",
    "The baby was in a deep sleep in his mother's arms.",
    "赤ちゃんは母親の腕の中でぐっすり眠っていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1205592",
      "license": "CC BY 2.0 FR",
      "attribution": "#1205592 (CK) / #142234 (bunbuku)"
    }
  ],
  [
    "slide",
    "B2",
    "名詞・動詞",
    [
      "滑って進む",
      "を滑らせる"
    ],
    "/slaɪd/",
    "The children were sliding on the ice.",
    "子供たちは氷の上を滑っていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/245777",
      "license": "CC BY 2.0 FR",
      "attribution": "#245777 (CK) / #168714 (tommy__san)"
    }
  ],
  [
    "slogan",
    "B2",
    "名詞",
    [
      "標語"
    ],
    "/ˈsloʊgən/",
    "The campaign uses a simple and memorable slogan.",
    "その運動は簡潔で覚えやすい標語を使う。",
    null
  ],
  [
    "slow",
    "B1",
    "動詞",
    [
      "を遅くする"
    ],
    "/sloʊ/",
    "The cold weather slowed the growth of the rice plants.",
    "寒波が稲の発育を遅らせた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326052",
      "license": "CC BY 2.0 FR",
      "attribution": "#326052 (CM) / #1827995 (bunbuku)"
    }
  ],
  [
    "slowly",
    "A2",
    "副詞",
    [
      "遅く"
    ],
    "/ˈsloʊli/",
    "Why is the car in front of us driving so slowly?",
    "前の車、なんでこんなに遅いんだ？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2610092",
      "license": "CC BY 2.0 FR",
      "attribution": "#2610092 (WestofEden) / #1031936 (bunbuku)"
    }
  ],
  [
    "smartphone",
    "A2",
    "名詞",
    [
      "スマートフォン"
    ],
    "/ˈsmɑrtfoʊn/",
    "I've been using this smartphone for five years.",
    "このスマホは五年も使っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10917093",
      "license": "CC BY 2.0 FR",
      "attribution": "#10917093 (CK) / #10917092 (small_snow)"
    }
  ],
  [
    "smell",
    "A2",
    "名詞・動詞",
    [
      "においがする",
      "においがわかる"
    ],
    "/smɛl/",
    "I like the smell of bread just out of the oven.",
    "焼きたてのパンの匂いが好きです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3053138",
      "license": "CC BY 2.0 FR",
      "attribution": "#3053138 (CK) / #3052946 (tommy_san)"
    }
  ],
  [
    "smile",
    "A2",
    "名詞・動詞",
    [
      "笑顔"
    ],
    "/smaɪl/",
    "A smile is the best cure for a bad mood.",
    "笑顔ってね、機嫌をなおす特効薬なのよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8154893",
      "license": "CC BY 2.0 FR",
      "attribution": "#8154893 (AlanF_US) / #9824718 (small_snow)"
    }
  ],
  [
    "smoke",
    "A2",
    "名詞・動詞",
    [
      "たばこを吸う",
      "たばこ"
    ],
    "/smoʊk/",
    "She knew better than to smoke a cigarette in his presence.",
    "彼女は彼の前でたばこを吸うような愚かなことはしなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/316426",
      "license": "CC BY 2.0 FR",
      "attribution": "#316426 (CK) / #87282 (bunbuku)"
    }
  ],
  [
    "smoking",
    "A2",
    "名詞",
    [
      "喫煙"
    ],
    "/ˈsmoʊkɪŋ/",
    "He has given up smoking for the sake of his health.",
    "彼は健康のため禁煙した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/295933",
      "license": "CC BY 2.0 FR",
      "attribution": "#295933 (CK) / #107752 (Blanka_Meduzo)"
    }
  ],
  [
    "so-called",
    "B2",
    "形容詞",
    [
      "いわゆる"
    ],
    "/soʊ kɔld/",
    "The bursting of Japan's so-called bubble economy sent shock waves through international markets.",
    "日本のいわゆるバブル経済崩壊により、国際市場にまで衝撃波が及んだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/281319",
      "license": "CC BY 2.0 FR",
      "attribution": "#281319 (CK) / #3464862 (arnab)"
    }
  ],
  [
    "soap",
    "A2",
    "名詞",
    [
      "石けん"
    ],
    "/soʊp/",
    "Have you ever washed your face with body soap?",
    "ボディーソープで顔洗ったことある？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2806574",
      "license": "CC BY 2.0 FR",
      "attribution": "#2806574 (CK) / #2806556 (tommy_san)"
    }
  ],
  [
    "soccer",
    "A2",
    "名詞",
    [
      "サッカー"
    ],
    "/ˈsɑkɚ/",
    "How many times a week does the soccer team practice?",
    "週に何回そのサッカーチームは練習するんですか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/266412",
      "license": "CC BY 2.0 FR",
      "attribution": "#266412 (CK) / #148147 (bunbuku)"
    }
  ],
  [
    "sock",
    "A2",
    "名詞",
    [
      "短い靴下"
    ],
    "/sɑk/",
    "He selected a pair of socks to match his suit.",
    "彼はスーツにあう靴下を選んだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/290178",
      "license": "CC BY 2.0 FR",
      "attribution": "#290178 (Hautis) / #113495 (mookeee)"
    }
  ],
  [
    "soft",
    "A2",
    "形容詞",
    [
      "柔らかい"
    ],
    "/sɑft/",
    "This blanket feels soft and warm against the skin.",
    "この毛布は肌触りが柔らかく暖かい。",
    null
  ],
  [
    "software",
    "B1",
    "名詞",
    [
      "ソフトウェア"
    ],
    "/ˈsɔftwɛr/",
    "Once you get the hang of it, spreadsheet software is really useful.",
    "表計算ソフトは、覚えておくと何かと便利よ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318350",
      "license": "CC BY 2.0 FR",
      "attribution": "#318350 (CK) / #85363 (bunbuku)"
    }
  ],
  [
    "soil",
    "B1",
    "名詞",
    [
      "土"
    ],
    "/sɔɪl/",
    "Cover the seeds with a bit of soil.",
    "種の上に少し土をかぶせなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10369147",
      "license": "CC BY 2.0 FR",
      "attribution": "#10369147 (sundown) / #148478 (tommy__san)"
    }
  ],
  [
    "solar",
    "B2",
    "形容詞",
    [
      "太陽の",
      "太陽からの"
    ],
    "/ˈsoʊlɚ/",
    "The problem is that solar energy just costs too much.",
    "問題は、太陽光エネルギーはお金がかかりすぎることです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1832980",
      "license": "CC BY 2.0 FR",
      "attribution": "#1832980 (ryanwhiting) / #1832217 (small_snow)"
    }
  ],
  [
    "soldier",
    "A2",
    "名詞",
    [
      "兵士"
    ],
    "/ˈsoʊldʒɚ/",
    "The soldiers got to the foot of the hill before dawn.",
    "兵士達は夜明け前に山の麓に着いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320113",
      "license": "CC BY 2.0 FR",
      "attribution": "#320113 (CK) / #83584 (KK_kaku_)"
    }
  ],
  [
    "sometime",
    "B2",
    "副詞",
    [
      "そのうち"
    ],
    "/ˈsʌmtaɪm/",
    "Come and visit us in Paris sometime soon.",
    "近いうちにパリに会いに来てよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1063432",
      "license": "CC BY 2.0 FR",
      "attribution": "#1063432 (CK) / #1061936 (mookeee)"
    }
  ],
  [
    "somewhat",
    "B2",
    "副詞",
    [
      "幾分か"
    ],
    "/ˈsʌmˈwʌt/",
    "He's somewhat hard of hearing, so please speak louder.",
    "彼はちょっと耳が遠いので、大きな声で話してください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/299598",
      "license": "CC BY 2.0 FR",
      "attribution": "#299598 (CK) / #1226892 (bunbuku)"
    }
  ],
  [
    "somewhere",
    "A2",
    "副詞・名詞",
    [
      "どこかに",
      "どこかへ"
    ],
    "/ˈsʌmwɛr/",
    "Would you like to go out to have a drink somewhere?",
    "どこかで一杯どう？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/38243",
      "license": "CC BY 2.0 FR",
      "attribution": "#38243 (CK) / #201038 (small_snow)"
    }
  ],
  [
    "sophisticated",
    "B2",
    "形容詞",
    [
      "洗練された",
      "世慣れた"
    ],
    "/səˈfɪstəkeɪtɪd/",
    "I felt utterly out of place among those sophisticated people.",
    "ああいう洗練された人々の中で、自分はまったく場違いな気がした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72099",
      "license": "CC BY 2.0 FR",
      "attribution": "#72099 (CM) / #234722 (Sim5634)"
    }
  ],
  [
    "soul",
    "B2",
    "名詞",
    [
      "魂"
    ],
    "/soʊl/",
    "He put all his heart and soul into it.",
    "それに全身全霊を傾けた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/42877",
      "license": "CC BY 2.0 FR",
      "attribution": "#42877 (CM) / #205632 (mookeee)"
    }
  ],
  [
    "southern",
    "B1",
    "形容詞",
    [
      "南部特有の",
      "南部ふうの"
    ],
    "/ˈsʌðɚn/",
    "He lives in the southern part of the city.",
    "彼は市の南部に住んでいます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/297165",
      "license": "CC BY 2.0 FR",
      "attribution": "#297165 (CK) / #106522 (tommy__san)"
    }
  ],
  [
    "speaker",
    "A2",
    "名詞",
    [
      "話者",
      "スピーカー"
    ],
    "/ˈspikɚ/",
    "What can I do to sound more like a native speaker?",
    "もっとネイティブスピーカーみたいに聞こえるには、どうすればいいの？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/954509",
      "license": "CC BY 2.0 FR",
      "attribution": "#954509 (CK) / #2171765 (bunbuku)"
    }
  ],
  [
    "specialize",
    "B2",
    "動詞",
    [
      "専門にする",
      "特殊化する"
    ],
    "/ˈspɛʃəlaɪz/",
    "The clinic will specialize in sports injuries.",
    "その診療所はスポーツ外傷を専門にする。",
    null
  ],
  [
    "specify",
    "B2",
    "動詞",
    [
      "を明確に述べる"
    ],
    "/ˈspɛsəfaɪ/",
    "He didn't specify when he would return.",
    "彼はいつ帰るかはっきり言わなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/289238",
      "license": "CC BY 2.0 FR",
      "attribution": "#289238 (CK) / #114433 (bunbuku)"
    }
  ],
  [
    "spectacular",
    "B2",
    "形容詞",
    [
      "壮観の"
    ],
    "/spɛkˈtækjəlɚ/",
    "The view from the mountain top was spectacular.",
    "山頂からの眺めは壮観だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/245097",
      "license": "CC BY 2.0 FR",
      "attribution": "#245097 (CK) / #169389 (tommy_san)"
    }
  ],
  [
    "spectator",
    "B2",
    "名詞",
    [
      "観客"
    ],
    "/ˈspɛkteɪtɚ/",
    "There were more spectators than I had expected.",
    "予想以上に多くの観客が来ていました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/324703",
      "license": "CC BY 2.0 FR",
      "attribution": "#324703 (CK) / #79014 (tommy_san)"
    }
  ],
  [
    "speculate",
    "B2",
    "動詞",
    [
      "推測する",
      "と推測する"
    ],
    "/ˈspɛkjəleɪt/",
    "Experts refuse to speculate about the cause.",
    "専門家は原因について推測することを拒んでいる。",
    null
  ],
  [
    "speculation",
    "B2",
    "名詞",
    [
      "推測"
    ],
    "/spɛkjəˈleɪʃən/",
    "The announcement ended months of speculation.",
    "その発表で数か月の憶測が終わった。",
    null
  ],
  [
    "speech",
    "A2",
    "名詞",
    [
      "話すこと",
      "話し方"
    ],
    "/spitʃ/",
    "I know from his speech that he is not an American.",
    "話しぶりから彼はアメリカ人ではないことがわかる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326532",
      "license": "CC BY 2.0 FR",
      "attribution": "#326532 (CM) / #77187 (mookeee)"
    }
  ],
  [
    "speed",
    "A2",
    "名詞・動詞",
    [
      "速度"
    ],
    "/spid/",
    "The Hikari runs at a speed of 200 kilometres an hour.",
    "「ひかり」は時速２００キロで走る。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73816",
      "license": "CC BY 2.0 FR",
      "attribution": "#73816 (CM) / #236450 (mookeee)"
    }
  ],
  [
    "spending",
    "B1",
    "名詞",
    [
      "支出",
      "消費"
    ],
    "/ˈspɛndɪŋ/",
    "Public spending on healthcare increased last year.",
    "医療への公的支出は昨年増加した。",
    null
  ],
  [
    "spice",
    "B2",
    "名詞",
    [
      "ぴりっとするもの"
    ],
    "/spaɪs/",
    "Hunger is the best spice.",
    "ひもじい時にまずいものなし。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/3732727",
      "license": "CC BY 2.0 FR",
      "attribution": "#3732727 (CK) / #197452 (mookeee)"
    }
  ],
  [
    "spicy",
    "B1",
    "形容詞",
    [
      "辛い"
    ],
    "/ˈspaɪsi/",
    "It's not all that spicy, so it's easy to eat.",
    "あんまり辛くないから食べやすい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11005323",
      "license": "CC BY 2.0 FR",
      "attribution": "#11005323 (CK) / #11005107 (KK_kaku_)"
    }
  ],
  [
    "spider",
    "A2",
    "名詞",
    [
      "クモ"
    ],
    "/ˈspaɪdɚ/",
    "Seen from an airplane, the island looks like a big spider.",
    "飛行機から見ると、その島は巨大なクモのように見える。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/317975",
      "license": "CC BY 2.0 FR",
      "attribution": "#317975 (mamat) / #85738 (KK_kaku_)"
    }
  ],
  [
    "spill",
    "B2",
    "動詞",
    [
      "こぼれたもの"
    ],
    "/spɪl/",
    "I haven't eaten any seafood since the recent oil spill.",
    "最近の石油流出事故が起きてからというもの、魚介類は一切食べてないんです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8170595",
      "license": "CC BY 2.0 FR",
      "attribution": "#8170595 (CK) / #8959046 (bunbuku)"
    }
  ],
  [
    "spite",
    "B2",
    "名詞",
    [
      "〜にもかかわらず",
      "悪意"
    ],
    "/spaɪt/",
    "She arrived at school on time in spite of the snowstorm.",
    "彼女は吹雪にもかかわらず時間どおりに学校についた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/315266",
      "license": "CC BY 2.0 FR",
      "attribution": "#315266 (CK) / #88441 (bunbuku)"
    }
  ],
  [
    "spoil",
    "B2",
    "動詞",
    [
      "をだいなしにする"
    ],
    "/spɔɪl/",
    "What with the wind and the rain, our walk was spoiled.",
    "風やら雨やらで、我々の散歩は台無しだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/446114",
      "license": "CC BY 2.0 FR",
      "attribution": "#446114 (blay_paul) / #84000 (bunbuku)"
    }
  ],
  [
    "spoken",
    "B1",
    "形容詞",
    [
      "話された",
      "口語の"
    ],
    "/ˈspoʊkən/",
    "I find it difficult to understand French when it's spoken quickly.",
    "フランス語を速く話されちゃうと、理解するのが難しいんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4955344",
      "license": "CC BY 2.0 FR",
      "attribution": "#4955344 (CK) / #8966753 (bunbuku)"
    }
  ],
  [
    "spokesman",
    "B2",
    "名詞",
    [
      "報道担当者",
      "代弁者"
    ],
    "/ˈspoʊksmən/",
    "The spokesman explained the contents of the treaty to the press.",
    "報道担当官が条約の内容を報道陣に説明した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320979",
      "license": "CC BY 2.0 FR",
      "attribution": "#320979 (CK) / #82737 (KK_kaku_)"
    }
  ],
  [
    "spokesperson",
    "B2",
    "名詞",
    [
      "報道担当者"
    ],
    "/ˈspoʊkspɚsən/",
    "A company spokesperson answered reporters' questions.",
    "会社の報道担当者が記者の質問に答えた。",
    null
  ],
  [
    "spokeswoman",
    "B2",
    "名詞",
    [
      "女性スポークスマン"
    ],
    "/ˈspoʊkswʊmən/",
    "The spokeswoman announced a change in policy.",
    "女性報道官が方針変更を発表した。",
    null
  ],
  [
    "sponsor",
    "B2",
    "名詞・動詞",
    [
      "のスポンサーになる",
      "後援者"
    ],
    "/ˈspɑnsɚ/",
    "A local bank agreed to sponsor the festival.",
    "地元銀行が祭りの支援者になることに同意した。",
    null
  ],
  [
    "sponsorship",
    "B2",
    "名詞",
    [
      "後援",
      "資金提供"
    ],
    "/ˈspɑnsɚʃɪp/",
    "Corporate sponsorship covered the event costs.",
    "企業の後援がイベント費用をまかなった。",
    null
  ],
  [
    "spoon",
    "A2",
    "名詞",
    [
      "スプーン",
      "スプーン1杯"
    ],
    "/spun/",
    "Which side of the plate is the spoon supposed to be on?",
    "皿のどちら側にスプーンを置いたらよいでしょうか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2835516",
      "license": "CC BY 2.0 FR",
      "attribution": "#2835516 (CK) / #3460697 (arnab)"
    }
  ],
  [
    "sporting",
    "B2",
    "形容詞",
    [
      "スポーツの",
      "スポーツマンらしい"
    ],
    "/ˈspɔrtɪŋ/",
    "The city will host several sporting events.",
    "その都市はいくつかのスポーツ行事を開催する。",
    null
  ],
  [
    "spring",
    "B2",
    "動詞",
    [
      "温泉",
      "春",
      "ばね"
    ],
    "/sprɪŋ/",
    "We're torn between going to a hot spring and going skiing.",
    "今、温泉に行くかスキーに行くかもめているんだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241548",
      "license": "CC BY 2.0 FR",
      "attribution": "#241548 (CM) / #172925 (KK_kaku_)"
    }
  ],
  [
    "square",
    "A2",
    "形容詞・名詞",
    [
      "平方",
      "角ばった"
    ],
    "/skwɛr/",
    "We learned at school that the square root of nine is three.",
    "僕らは９の平方根は３だと学校で習った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322003",
      "license": "CC BY 2.0 FR",
      "attribution": "#322003 (CK) / #81712 (bunbuku)"
    }
  ],
  [
    "stadium",
    "B1",
    "名詞",
    [
      "スタジアム"
    ],
    "/ˈsteɪdiəm/",
    "When we arrived at the stadium, the game had already started.",
    "スタジアムについた時には、試合はもう始まっていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/51977",
      "license": "CC BY 2.0 FR",
      "attribution": "#51977 (CK) / #214684 (bunbuku)"
    }
  ],
  [
    "stair",
    "A2",
    "名詞",
    [
      "階段",
      "段"
    ],
    "/stɛr/",
    "This elevator is out of order. Please use the stairs.",
    "このエレベーターは故障中です。階段をお使いください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61307",
      "license": "CC BY 2.0 FR",
      "attribution": "#61307 (CK) / #223972 (bunbuku)"
    }
  ],
  [
    "stall",
    "B2",
    "名詞",
    [
      "露店",
      "屋台"
    ],
    "/stɔl/",
    "You may not set up a roadside stall without prior notice.",
    "届け出なしに路上に出店してはならない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327884",
      "license": "CC BY 2.0 FR",
      "attribution": "#327884 (CM) / #75834 (bunbuku)"
    }
  ],
  [
    "stamp",
    "A2",
    "名詞",
    [
      "切手",
      "に切手をはる"
    ],
    "/stæmp/",
    "I have to put a stamp on the envelope.",
    "封筒に切手を貼らなきゃ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/319645",
      "license": "CC BY 2.0 FR",
      "attribution": "#319645 (CK) / #9306376 (bunbuku)"
    }
  ],
  [
    "stance",
    "B2",
    "名詞",
    [
      "立場"
    ],
    "/stæns/",
    "The minister softened her stance on the proposal.",
    "大臣はその提案への立場を和らげた。",
    null
  ],
  [
    "stand",
    "B2",
    "名詞",
    [
      "ある",
      "起立する"
    ],
    "/stænd/",
    "I'll stand behind you if you are going to do it.",
    "やるつもりがあるなら、サポートするよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/17551",
      "license": "CC BY 2.0 FR",
      "attribution": "#17551 (Zifre) / #10846567 (bunbuku)"
    }
  ],
  [
    "star",
    "A2",
    "動詞",
    [
      "星"
    ],
    "/stɑr/",
    "Not a star was to be seen in the sky.",
    "夜空には星一つ見えなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18317",
      "license": "CC BY 2.0 FR",
      "attribution": "#18317 (CM) / #79698 (mookeee)"
    }
  ],
  [
    "start",
    "A2",
    "名詞",
    [
      "始まる"
    ],
    "/stɑrt/",
    "We waited in the movie theater for the film to start.",
    "私たちは映画館の中で映画が始まるのを待った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/682167",
      "license": "CC BY 2.0 FR",
      "attribution": "#682167 (Source_VOA) / #1594397 (bunbuku)"
    }
  ],
  [
    "starve",
    "B2",
    "動詞",
    [
      "飢える",
      "を飢え死にさせる"
    ],
    "/stɑrv/",
    "He didn't like to ask for help even if he was starving.",
    "たとえ飢えかかっていても、彼は助けを求めたがらなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/40741",
      "license": "CC BY 2.0 FR",
      "attribution": "#40741 (CK) / #203503 (bunbuku)"
    }
  ],
  [
    "statue",
    "B1",
    "名詞",
    [
      "像"
    ],
    "/ˈstætʃu/",
    "The right arm of the Statue of Liberty is 42 feet long.",
    "自由の女神の右腕の長さは12.8mである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2947375",
      "license": "CC BY 2.0 FR",
      "attribution": "#2947375 (CK) / #2948407 (tommy_san)"
    }
  ],
  [
    "stay",
    "A2",
    "名詞",
    [
      "いる",
      "滞在する"
    ],
    "/steɪ/",
    "It would be better to stay at home than go out.",
    "外出するより家にいるほうがいい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12740221",
      "license": "CC BY 2.0 FR",
      "attribution": "#12740221 (CK) / #184734 (KK_kaku_)"
    }
  ],
  [
    "steadily",
    "B2",
    "副詞",
    [
      "着実に"
    ],
    "/ˈstɛdəli/",
    "Snow has been falling steadily since this morning.",
    "朝から休みなく雪が降り続いている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277738",
      "license": "CC BY 2.0 FR",
      "attribution": "#277738 (CK) / #126254 (bunbuku)"
    }
  ],
  [
    "steam",
    "B2",
    "名詞",
    [
      "蒸気",
      "水蒸気"
    ],
    "/stim/",
    "We were wakened by the whistle of the steam locomotive at dawn.",
    "明け方、私たちは蒸気機関車の汽笛で目を覚ました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1263685",
      "license": "CC BY 2.0 FR",
      "attribution": "#1263685 (CK) / #1799413 (bunbuku)"
    }
  ],
  [
    "step",
    "A2",
    "名詞・動詞",
    [
      "一歩",
      "一歩の距離"
    ],
    "/stɛp/",
    "The boy was so tired that he couldn't take one more step.",
    "その少年は、一歩も歩けないほど疲れていました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/707082",
      "license": "CC BY 2.0 FR",
      "attribution": "#707082 (papabear) / #11512862 (small_snow)"
    }
  ],
  [
    "sticky",
    "B2",
    "形容詞",
    [
      "付箋の",
      "粘着する"
    ],
    "/ˈstɪki/",
    "Please put a sticky note on any part that needs changed.",
    "修正が必要な箇所には、付箋を貼っておいてください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13569929",
      "license": "CC BY 2.0 FR",
      "attribution": "#13569929 (CK) / #12135714 (small_snow)"
    }
  ],
  [
    "stimulate",
    "B2",
    "動詞",
    [
      "を刺激する"
    ],
    "/ˈstɪmjəleɪt/",
    "Moderate exercise stimulates the circulation of blood.",
    "適度な運動は血液の循環を活発にする。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/278710",
      "license": "CC BY 2.0 FR",
      "attribution": "#278710 (CK) / #125283 (bunbuku)"
    }
  ],
  [
    "stomach",
    "A2",
    "名詞",
    [
      "腹",
      "腹に入れる"
    ],
    "/ˈstʌmək/",
    "Drinking on an empty stomach is bad for your health.",
    "空きっ腹にお酒を飲むのは体に良くない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18337",
      "license": "CC BY 2.0 FR",
      "attribution": "#18337 (Dejo) / #179479 (mookeee)"
    }
  ],
  [
    "stone",
    "A2",
    "名詞",
    [
      "石",
      "に石を投げる"
    ],
    "/stoʊn/",
    "This stone was so heavy that I could not lift it.",
    "この石はとても重かったので持ち上げることができなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58201",
      "license": "CC BY 2.0 FR",
      "attribution": "#58201 (CM) / #220879 (bunbuku)"
    }
  ],
  [
    "storm",
    "A2",
    "名詞",
    [
      "あらし"
    ],
    "/stɔrm/",
    "It was because of the storm that the trains were halted.",
    "列車が止まったのは嵐のせいだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326142",
      "license": "CC BY 2.0 FR",
      "attribution": "#326142 (CM) / #77576 (mookeee)"
    }
  ],
  [
    "straight",
    "A2",
    "形容詞・副詞",
    [
      "回り道をしないで"
    ],
    "/streɪt/",
    "Stop beating around the bush and give it to me straight!",
    "回りくどい言い方はやめてはっきり言ってよ！",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/22320",
      "license": "CC BY 2.0 FR",
      "attribution": "#22320 (CK) / #185189 (bunbuku)"
    }
  ],
  [
    "strange",
    "A2",
    "形容詞",
    [
      "変な",
      "勝手が違った"
    ],
    "/streɪndʒ/",
    "A strange man came up to me and asked for money.",
    "変な人が近づいて来てお金をくれと言った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320334",
      "license": "CC BY 2.0 FR",
      "attribution": "#320334 (CK) / #83382 (small_snow)"
    }
  ],
  [
    "stranger",
    "B1",
    "名詞",
    [
      "経験のない人",
      "慣れていない人"
    ],
    "/ˈstreɪndʒɚ/",
    "I'm a stranger here myself. I'm afraid I can't help you.",
    "私もこの辺りは初めてなんです。お役に立てないと思います。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/262334",
      "license": "CC BY 2.0 FR",
      "attribution": "#262334 (CK) / #152216 (bunbuku)"
    }
  ],
  [
    "stream",
    "B2",
    "名詞",
    [
      "人の流れ",
      "小川"
    ],
    "/strim/",
    "A stream of people came out of the theater.",
    "劇場から続々と人が出てきた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238470",
      "license": "CC BY 2.0 FR",
      "attribution": "#238470 (CM) / #175995 (KK_kaku_)"
    }
  ],
  [
    "strictly",
    "B2",
    "副詞",
    [
      "厳密に"
    ],
    "/ˈstrɪktli/",
    "Strictly speaking, the Earth is not a sphere.",
    "厳密にいえば、地球は球ではない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11151641",
      "license": "CC BY 2.0 FR",
      "attribution": "#11151641 (ddnktr) / #3338346 (tommy_san)"
    }
  ],
  [
    "string",
    "B1",
    "名詞",
    [
      "糸"
    ],
    "/strɪŋ/",
    "The police say there's someone pulling string behind the scenes.",
    "背後で糸を引いている人物がいると警察は言っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/282457",
      "license": "CC BY 2.0 FR",
      "attribution": "#282457 (CM) / #121548 (small_snow)"
    }
  ],
  [
    "stroke",
    "B2",
    "名詞",
    [
      "画",
      "一打ち"
    ],
    "/stroʊk/",
    "How many strokes does the kanji for \"michi\" have?",
    "「道」という漢字の総画数は何画ですか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326746",
      "license": "CC BY 2.0 FR",
      "attribution": "#326746 (Zifre) / #76974 (mookeee)"
    }
  ],
  [
    "strongly",
    "B1",
    "副詞",
    [
      "強く思う",
      "強く"
    ],
    "/ˈstrɔŋli/",
    "I feel strongly that men and women are equal.",
    "男女は平等なんだなって、つくづく感じるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/276820",
      "license": "CC BY 2.0 FR",
      "attribution": "#276820 (CK) / #11110408 (bunbuku)"
    }
  ],
  [
    "studio",
    "B1",
    "名詞",
    [
      "スタジオ",
      "放送スタジオ"
    ],
    "/ˈstudioʊ/",
    "I don't switch on the light in my studio at night.",
    "夜はスタジオの電気をつけないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/323966",
      "license": "CC BY 2.0 FR",
      "attribution": "#323966 (CM) / #10746618 (bunbuku)"
    }
  ],
  [
    "stunning",
    "B2",
    "形容詞",
    [
      "見事な",
      "驚くほど美しい"
    ],
    "/ˈstʌnɪŋ/",
    "The hotel offers a stunning view of the bay.",
    "そのホテルから湾の見事な景色が見える。",
    null
  ],
  [
    "stupid",
    "A2",
    "形容詞",
    [
      "ばかな"
    ],
    "/ˈstupəd/",
    "It would be stupid to climb that mountain in the winter.",
    "冬にあの山に登るのは狂気の沙汰だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/898999",
      "license": "CC BY 2.0 FR",
      "attribution": "#898999 (CK) / #124396 (KK_kaku_)"
    }
  ],
  [
    "submit",
    "B2",
    "動詞",
    [
      "屈服する"
    ],
    "/səbˈmɪt/",
    "I don't think it's always right for local governments to submit to the central government.",
    "地方自治体が中央政府に従うことが必ずしも正しいとは、私は思わない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277255",
      "license": "CC BY 2.0 FR",
      "attribution": "#277255 (CM) / #3467070 (arnab)"
    }
  ],
  [
    "subsequent",
    "B2",
    "形容詞",
    [
      "後の"
    ],
    "/ˈsʌbsəkwənt/",
    "Subsequent tests confirmed the first result.",
    "その後の検査が最初の結果を確認した。",
    null
  ],
  [
    "subsequently",
    "B2",
    "副詞",
    [
      "その後",
      "続いて"
    ],
    "/ˈsʌbsəkwəntli/",
    "He moved abroad and subsequently started a business.",
    "彼は海外へ移り、その後事業を始めた。",
    null
  ],
  [
    "successfully",
    "B1",
    "副詞",
    [
      "うまく"
    ],
    "/səkˈsɛsfəli/",
    "She successfully got him to tell the truth.",
    "彼女はうまく彼から真実を聞きだした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/388366",
      "license": "CC BY 2.0 FR",
      "attribution": "#388366 (CK) / #93159 (bunbuku)"
    }
  ],
  [
    "such",
    "A2",
    "限定詞・名詞",
    [
      "そんな",
      "こんな"
    ],
    "/sʌtʃ/",
    "Trying to do such a thing is a waste of time.",
    "そんなことやっても時間の無駄にすぎない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41633",
      "license": "CC BY 2.0 FR",
      "attribution": "#41633 (CK) / #204391 (mookeee)"
    }
  ],
  [
    "suffering",
    "B2",
    "名詞",
    [
      "苦悩している状態"
    ],
    "/ˈsʌfɚɪŋ/",
    "People are suffering from the contamination of the water supply.",
    "人々は水道水の汚染に苦しんでいる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270476",
      "license": "CC BY 2.0 FR",
      "attribution": "#270476 (CK) / #144090 (KK_kaku_)"
    }
  ],
  [
    "sufficiently",
    "B2",
    "副詞",
    [
      "十分に"
    ],
    "/səˈfɪʃəntli/",
    "The room is sufficiently large for the group.",
    "その部屋はグループに十分な広さがある。",
    null
  ],
  [
    "summary",
    "B1",
    "名詞",
    [
      "要約"
    ],
    "/ˈsʌmɚi/",
    "Please send in your summary by Tuesday.",
    "要約を火曜日までに提出しなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/324917",
      "license": "CC BY 2.0 FR",
      "attribution": "#324917 (CK) / #78799 (mookeee)"
    }
  ],
  [
    "super",
    "B2",
    "形容詞",
    [
      "とても",
      "すごい"
    ],
    "/ˈsupɚ/",
    "The new camera is super easy to use.",
    "その新しいカメラはとても使いやすい。",
    null
  ],
  [
    "supporter",
    "B1",
    "名詞",
    [
      "支持者",
      "扶養する人"
    ],
    "/səˈpɔrtɚ/",
    "Some of Martin Luther King's supporters began to question his belief in peaceful protests.",
    "マーティン・ルーサー・キング牧師の支持者の中には、平和的に抗議するという彼の信念に疑いの念を持つ物も現れ始めた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63066",
      "license": "CC BY 2.0 FR",
      "attribution": "#63066 (CM) / #225728 (KK_kaku_)"
    }
  ],
  [
    "sure",
    "A2",
    "副詞",
    [
      "確信して"
    ],
    "/ʃʊr/",
    "Please be sure to take one dose three times a day.",
    "１日に３度１錠ずつ服用してください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73078",
      "license": "CC BY 2.0 FR",
      "attribution": "#73078 (CK) / #235698 (mookeee)"
    }
  ],
  [
    "surely",
    "B1",
    "副詞",
    [
      "きっと"
    ],
    "/ˈʃʊrli/",
    "She will surely be enjoying a hot bath at this hour.",
    "彼女はきっとこの時間は温泉につかって楽しんでいることでしょう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/310719",
      "license": "CC BY 2.0 FR",
      "attribution": "#310719 (CK) / #92990 (bunbuku)"
    }
  ],
  [
    "surgeon",
    "B2",
    "名詞",
    [
      "外科医"
    ],
    "/ˈsɝdʒən/",
    "The surgeon persuaded me to undergo an organ transplant operation.",
    "外科医は私を説得して、臓器の移植手術を受けることに同意させた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21982",
      "license": "CC BY 2.0 FR",
      "attribution": "#21982 (CK) / #184853 (bunbuku)"
    }
  ],
  [
    "surprise",
    "A2",
    "名詞・動詞",
    [
      "驚き"
    ],
    "/sɚˈpraɪz/",
    "The Tigers lost the game, which was a surprise to us.",
    "タイガースはそのゲームに負けた。それは私達には驚きだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41232",
      "license": "CC BY 2.0 FR",
      "attribution": "#41232 (CK) / #203990 (mookeee)"
    }
  ],
  [
    "surprised",
    "A2",
    "形容詞",
    [
      "驚いた"
    ],
    "/sɚˈpraɪzd/",
    "She was surprised to find many beautiful things in the box.",
    "彼女は、その箱の中にたくさんの美しいものを見つけて、驚いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309918",
      "license": "CC BY 2.0 FR",
      "attribution": "#309918 (CK) / #93789 (mookeee)"
    }
  ],
  [
    "surprising",
    "A2",
    "形容詞",
    [
      "驚くべき"
    ],
    "/sɚˈpraɪzɪŋ/",
    "The idea that air has weight was surprising to the child.",
    "空気に重さがある、という考えはその子にはびっくりするようなことだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18243",
      "license": "CC BY 2.0 FR",
      "attribution": "#18243 (CK) / #179385 (bunbuku)"
    }
  ],
  [
    "survival",
    "B2",
    "名詞",
    [
      "生存",
      "生存者"
    ],
    "/sɚˈvaɪvəl/",
    "This is an example of the survival of the fittest, as it is called.",
    "これはいわゆる適者生存の例である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/55950",
      "license": "CC BY 2.0 FR",
      "attribution": "#55950 (CM) / #218637 (KK_kaku_)"
    }
  ],
  [
    "survivor",
    "B2",
    "名詞",
    [
      "生存者"
    ],
    "/sɚˈvaɪvɚ/",
    "There was only one survivor of the accident.",
    "事故の生存者は一人だけでした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2041424",
      "license": "CC BY 2.0 FR",
      "attribution": "#2041424 (AlanF_US) / #11099266 (small_snow)"
    }
  ],
  [
    "suspend",
    "B2",
    "動詞",
    [
      "を停学にする"
    ],
    "/səˈspɛnd/",
    "He was suspended from school for a week for bad conduct.",
    "彼は素行不良で１週間の停学を受けた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/300802",
      "license": "CC BY 2.0 FR",
      "attribution": "#300802 (CM) / #102892 (KK_kaku_)"
    }
  ],
  [
    "swallow",
    "B2",
    "動詞",
    [
      "を飲み込む",
      "つばを飲み込む"
    ],
    "/ˈswɑloʊ/",
    "I can't swallow these tablets without a drink of water.",
    "水なしじゃ、こういう錠剤は飲み込めないよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270737",
      "license": "CC BY 2.0 FR",
      "attribution": "#270737 (CK) / #9025837 (bunbuku)"
    }
  ],
  [
    "sweep",
    "B2",
    "動詞",
    [
      "を掃く",
      "を掃くように動かす"
    ],
    "/swip/",
    "All you have to do is sweep the floor.",
    "お前は床を掃きさえすればよい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1369535",
      "license": "CC BY 2.0 FR",
      "attribution": "#1369535 (CK) / #226930 (mookeee)"
    }
  ],
  [
    "sweet",
    "A2",
    "形容詞・名詞",
    [
      "美しい",
      "おいしい"
    ],
    "/swit/",
    "God gave her a beautiful face and a sweet voice.",
    "神は彼女に美しい顔と、声を与えた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269663",
      "license": "CC BY 2.0 FR",
      "attribution": "#269663 (CM) / #144901 (bunbuku)"
    }
  ],
  [
    "swim",
    "B1",
    "名詞",
    [
      "ぐるぐる回るように見える"
    ],
    "/swɪm/",
    "Today is hot enough for us to swim in the sea.",
    "今日は暑いから海で泳げるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/242954",
      "license": "CC BY 2.0 FR",
      "attribution": "#242954 (CM) / #171521 (KK_kaku_)"
    }
  ],
  [
    "sympathetic",
    "B2",
    "形容詞",
    [
      "思いやりのある",
      "気に入った"
    ],
    "/sɪmpəˈθɛtɪk/",
    "The girl and her parents were very sympathetic.",
    "少女と両親はとても思いやりがあった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325733",
      "license": "CC BY 2.0 FR",
      "attribution": "#325733 (CK) / #1747672 (mookeee)"
    }
  ],
  [
    "tablet",
    "A2",
    "名詞",
    [
      "錠剤",
      "タブレット端末"
    ],
    "/ˈtæblət/",
    "Take one tablet a day until all of the medicine is gone.",
    "毎日１錠を、薬がなくなるまで飲んで下さい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/322397",
      "license": "CC BY 2.0 FR",
      "attribution": "#322397 (CK) / #81318 (bunbuku)"
    }
  ],
  [
    "tag",
    "B2",
    "名詞・動詞",
    [
      "鬼ごっこ",
      "タッチアウトにすること"
    ],
    "/tæg/",
    "We're playing tag. Do you want to play with us?",
    "鬼ごっこをしてるよ。君も一緒にする？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2050682",
      "license": "CC BY 2.0 FR",
      "attribution": "#2050682 (CK) / #8652527 (small_snow)"
    }
  ],
  [
    "tail",
    "B1",
    "名詞",
    [
      "尾"
    ],
    "/teɪl/",
    "The tail of a fox is longer than that of a rabbit.",
    "きつねの尾はウサギのより長い。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63326",
      "license": "CC BY 2.0 FR",
      "attribution": "#63326 (CK) / #225987 (Sim5634)"
    }
  ],
  [
    "tale",
    "B2",
    "名詞",
    [
      "話"
    ],
    "/teɪl/",
    "That author translated those fairy tales into our language.",
    "その作家がそのおとぎ話を私達の母語に翻訳した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2278861",
      "license": "CC BY 2.0 FR",
      "attribution": "#2278861 (CK) / #210526 (Blanka_Meduzo)"
    }
  ],
  [
    "talented",
    "B1",
    "形容詞",
    [
      "才能のある"
    ],
    "/ˈtæləntɪd/",
    "Don't be discouraged just because you're not all that talented.",
    "あまり才能がないからといってがっかりしてはいけない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1426484",
      "license": "CC BY 2.0 FR",
      "attribution": "#1426484 (CK) / #230325 (bunbuku)"
    }
  ],
  [
    "talk",
    "A2",
    "名詞",
    [
      "話",
      "話し合う"
    ],
    "/tɔk/",
    "Let's spread the map on the table and talk it over.",
    "地図をテーブルに広げて話し合おう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277235",
      "license": "CC BY 2.0 FR",
      "attribution": "#277235 (CK) / #126855 (mookeee)"
    }
  ],
  [
    "tank",
    "B2",
    "名詞",
    [
      "戦車"
    ],
    "/tæŋk/",
    "They invaded the country with tanks and guns.",
    "彼らは戦車と銃器でその国を侵略した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/307023",
      "license": "CC BY 2.0 FR",
      "attribution": "#307023 (CM) / #96682 (mookeee)"
    }
  ],
  [
    "tap",
    "B2",
    "名詞・動詞",
    [
      "蛇口",
      "軽くたたく"
    ],
    "/tæp/",
    "The kitchen tap has been leaking since yesterday.",
    "台所の蛇口は昨日から水漏れしている。",
    null
  ],
  [
    "tape",
    "B1",
    "名詞",
    [
      "テープ",
      "録音用テープ"
    ],
    "/teɪp/",
    "Cassette tapes seem to have given way to compact disks in popularity.",
    "カセットテープは人気の点でＣＤにとって代わられたようだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63736",
      "license": "CC BY 2.0 FR",
      "attribution": "#63736 (CM) / #226392 (arnab)"
    }
  ],
  [
    "taste",
    "A2",
    "名詞・動詞",
    [
      "味がする",
      "味覚"
    ],
    "/teɪst/",
    "This cola has lost its fizz and doesn't taste any good.",
    "このコーラ、炭酸が抜けちゃっておいしくない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1526979",
      "license": "CC BY 2.0 FR",
      "attribution": "#1526979 (CK) / #1526961 (bunbuku)"
    }
  ],
  [
    "teaching",
    "A2",
    "名詞",
    [
      "教え",
      "教えること"
    ],
    "/ˈtitʃɪŋ/",
    "One who is not willing to learn is not worth teaching.",
    "学ぶ気のない者には教えるだけ無駄だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269845",
      "license": "CC BY 2.0 FR",
      "attribution": "#269845 (CM) / #1853534 (bunbuku)"
    }
  ],
  [
    "tear",
    "B2",
    "名詞・動詞",
    [
      "で…を裂いて分ける",
      "裂ける"
    ],
    "/tɛr/",
    "No sooner had she found him than she burst into tears.",
    "彼女は彼を見つけるやいなや、わっと泣き出した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/316500",
      "license": "CC BY 2.0 FR",
      "attribution": "#316500 (CM) / #87208 (bunbuku)"
    }
  ],
  [
    "technological",
    "B2",
    "形容詞",
    [
      "科学技術の"
    ],
    "/tɛknəˈlɑdʒɪkəl/",
    "Rapid technological change creates new kinds of work.",
    "急速な技術変化は新しい仕事を生む。",
    null
  ],
  [
    "teenage",
    "A2",
    "形容詞",
    [
      "10代の"
    ],
    "/ˈtineɪdʒ/",
    "She wrote the song during her teenage years.",
    "彼女は10代の頃にその歌を書いた。",
    null
  ],
  [
    "teens",
    "B2",
    "名詞",
    [
      "10代"
    ],
    "/tinz/",
    "My younger sister got married in her teens.",
    "私の妹は１０代で結婚した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/338272",
      "license": "CC BY 2.0 FR",
      "attribution": "#338272 (nanbanjin) / #162618 (bunbuku)"
    }
  ],
  [
    "temperature",
    "A2",
    "名詞",
    [
      "温度"
    ],
    "/ˈtɛmprətʃɚ/",
    "It is difficult to adapt oneself to sudden changes of temperature.",
    "温度の急激な変化に順応するのは困難である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/25470",
      "license": "CC BY 2.0 FR",
      "attribution": "#25470 (CK) / #188327 (mookeee)"
    }
  ],
  [
    "temple",
    "B2",
    "名詞",
    [
      "寺"
    ],
    "/ˈtɛmpəl/",
    "This temple is said to have been built over 500 years ago.",
    "このお寺は、500年以上も前に建てられたと言われています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58958",
      "license": "CC BY 2.0 FR",
      "attribution": "#58958 (CM) / #221632 (KK_kaku_)"
    }
  ],
  [
    "temporarily",
    "B2",
    "副詞",
    [
      "一時的に"
    ],
    "/tɛmpɚˈɛrəli/",
    "The museum is temporarily closed for repairs.",
    "博物館は修理のため一時的に閉鎖している。",
    null
  ],
  [
    "tension",
    "B2",
    "名詞",
    [
      "緊張",
      "緊張状態"
    ],
    "/ˈtɛnʃən/",
    "His joke eased the tension in the room.",
    "彼の冗談で室内の緊張がほぐれた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/286764",
      "license": "CC BY 2.0 FR",
      "attribution": "#286764 (CM) / #116903 (tommy__san)"
    }
  ],
  [
    "tent",
    "B1",
    "名詞",
    [
      "テント",
      "テント状のもの"
    ],
    "/tɛnt/",
    "It took us half an hour to set up the tent.",
    "テントを組み立てるのに３０分かかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/39126",
      "license": "CC BY 2.0 FR",
      "attribution": "#39126 (CK) / #201915 (bunbuku)"
    }
  ],
  [
    "term",
    "A2",
    "名詞・動詞",
    [
      "学期",
      "用語"
    ],
    "/tɝm/",
    "It's impossible for me to finish my term paper by tomorrow.",
    "明日までに期末レポートを仕上げるなんて不可能だよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9694294",
      "license": "CC BY 2.0 FR",
      "attribution": "#9694294 (CK) / #10788821 (bunbuku)"
    }
  ],
  [
    "terminal",
    "B2",
    "名詞",
    [
      "空港バス発着場"
    ],
    "/ˈtɝmənəl/",
    "The bus now arriving is going to the International Terminal via Domestic Terminal 1.",
    "ただ今到着のバスは、国内線第1ターミナル経由、国際線ターミナル行きです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4871892",
      "license": "CC BY 2.0 FR",
      "attribution": "#4871892 (CK) / #4871844 (tommy_san)"
    }
  ],
  [
    "terms",
    "B2",
    "名詞",
    [
      "〜の観点で",
      "条件",
      "用語"
    ],
    "/tɝmz/",
    "Today we are going to discuss this problem in terms of morality.",
    "今日は道徳の観点からこの問題について討論しようと思います。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63116",
      "license": "CC BY 2.0 FR",
      "attribution": "#63116 (CM) / #171530 (KK_kaku_)"
    }
  ],
  [
    "terribly",
    "B2",
    "副詞",
    [
      "恐ろしく"
    ],
    "/ˈtɛrəbli/",
    "This handmade Italian-made titanium bicycle is terribly light.",
    "この手作りのイタリア製チタン自転車は、恐ろしく軽い。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58677",
      "license": "CC BY 2.0 FR",
      "attribution": "#58677 (CM) / #221353 (bunbuku)"
    }
  ],
  [
    "terrify",
    "B2",
    "動詞",
    [
      "を恐れさせる"
    ],
    "/ˈtɛrəfaɪ/",
    "Sudden loud noises terrify the young dog.",
    "突然の大きな音はその子犬を怖がらせる。",
    null
  ],
  [
    "territory",
    "B2",
    "名詞",
    [
      "敵地",
      "領域"
    ],
    "/ˈtɛrɪtɔri/",
    "The commanding officer led his army into enemy territory.",
    "指揮官は軍を率いて敵地に入った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/246252",
      "license": "CC BY 2.0 FR",
      "attribution": "#246252 (CM) / #168241 (tommy_san)"
    }
  ],
  [
    "terror",
    "B2",
    "名詞",
    [
      "恐怖",
      "手に負えない物"
    ],
    "/ˈtɛrɚ/",
    "Most young people don't know the terror of war.",
    "大多数の若者は戦争の恐怖を知らない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/275828",
      "license": "CC BY 2.0 FR",
      "attribution": "#275828 (CM) / #137408 (tommy__san)"
    }
  ],
  [
    "terrorism",
    "B2",
    "名詞",
    [
      "テロ"
    ],
    "/ˈtɛrɚɪzəm/",
    "We will not tolerate anyone who engages in terrorism.",
    "我々は、誰であろうとテロ活動に携わるものに寛容でいるつもりはない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/23309",
      "license": "CC BY 2.0 FR",
      "attribution": "#23309 (Swift) / #186175 (bunbuku)"
    }
  ],
  [
    "terrorist",
    "B2",
    "名詞",
    [
      "テロリスト"
    ],
    "/ˈtɛrɚɪst/",
    "The terrorists released the hostages.",
    "テロリストは人質を解放した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/681885",
      "license": "CC BY 2.0 FR",
      "attribution": "#681885 (Source_VOA) / #1240894 (mookeee)"
    }
  ],
  [
    "testing",
    "B2",
    "名詞",
    [
      "試験"
    ],
    "/ˈtɛstɪŋ/",
    "The product is ready for safety testing.",
    "その製品は安全試験の準備ができている。",
    null
  ],
  [
    "text",
    "A2",
    "動詞",
    [
      "テキストメッセージ",
      "文章"
    ],
    "/tɛkst/",
    "I don't remember sending that text message.",
    "そんなショートメール、送った覚えないけど。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5045605",
      "license": "CC BY 2.0 FR",
      "attribution": "#5045605 (Hybrid) / #13216401 (small_snow)"
    }
  ],
  [
    "textbook",
    "B2",
    "名詞",
    [
      "教科書"
    ],
    "/ˈtɛkstbʊk/",
    "There is no such a thing as a comprehensive textbook.",
    "すべてを網羅した教科書など存在しない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2242186",
      "license": "CC BY 2.0 FR",
      "attribution": "#2242186 (CM) / #2242226 (tommy_san)"
    }
  ],
  [
    "that",
    "B1",
    "副詞",
    [
      "こと",
      "とは"
    ],
    "/ðæt/",
    "We have a lot of things that need to be done.",
    "我々のすべきことはたくさんある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4497456",
      "license": "CC BY 2.0 FR",
      "attribution": "#4497456 (CK) / #991790 (mookeee)"
    }
  ],
  [
    "theft",
    "B2",
    "名詞",
    [
      "盗み"
    ],
    "/θɛft/",
    "I reported the theft of my car to the police.",
    "警察に車の盗難届を出した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/258387",
      "license": "CC BY 2.0 FR",
      "attribution": "#258387 (CK) / #10674444 (bunbuku)"
    }
  ],
  [
    "theirs",
    "B1",
    "名詞",
    [
      "彼らのもの"
    ],
    "/ðɛrz/",
    "Some have come to meet their friends and others to see theirs off.",
    "友人を迎えに来た人もいれば、見送りに来た人もいる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/324370",
      "license": "CC BY 2.0 FR",
      "attribution": "#324370 (CM) / #79347 (tommy__san)"
    }
  ],
  [
    "theme",
    "B1",
    "名詞",
    [
      "テーマ"
    ],
    "/θim/",
    "The theme park was closed down last month.",
    "そのテーマパークは先月閉園になった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327086",
      "license": "CC BY 2.0 FR",
      "attribution": "#327086 (CK) / #76634 (tatoebane)"
    }
  ],
  [
    "themselves",
    "A2",
    "名詞",
    [
      "彼ら自身"
    ],
    "/ðɛmˈsɛlvz/",
    "My father always said that heaven helps those who help themselves.",
    "父はいつも「天は自ら助くる者を助く」と言っていました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318965",
      "license": "CC BY 2.0 FR",
      "attribution": "#318965 (CK) / #84749 (tommy_san)"
    }
  ],
  [
    "theory",
    "B1",
    "名詞",
    [
      "理論"
    ],
    "/ˈθɪri/",
    "We associate the name of Darwin with the theory of evolution.",
    "私達はダーウィンという名前を聞くと進化論を連想する。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/262804",
      "license": "CC BY 2.0 FR",
      "attribution": "#262804 (CM) / #151751 (tommy__san)"
    }
  ],
  [
    "therapist",
    "B2",
    "名詞",
    [
      "治療専門家"
    ],
    "/ˈθɛrəpəst/",
    "The therapist taught him exercises for his shoulder.",
    "治療専門家は肩の運動を教えた。",
    null
  ],
  [
    "therapy",
    "B2",
    "名詞",
    [
      "治療"
    ],
    "/ˈθɛrəpi/",
    "Will the therapy cause me any pain?",
    "その治療は痛いんですか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/43459",
      "license": "CC BY 2.0 FR",
      "attribution": "#43459 (CK) / #11344288 (bunbuku)"
    }
  ],
  [
    "therefore",
    "B1",
    "副詞",
    [
      "その結果"
    ],
    "/ˈðɛrfɔr/",
    "The evidence was weak; therefore, the case was closed.",
    "証拠が弱かったため、その事件は終了した。",
    null
  ],
  [
    "thesis",
    "B2",
    "名詞",
    [
      "論文"
    ],
    "/ˈθisəs/",
    "Have you already decided what the topic of your thesis will be?",
    "論文のテーマはもう決まったの？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11521644",
      "license": "CC BY 2.0 FR",
      "attribution": "#11521644 (CK) / #994919 (mookeee)"
    }
  ],
  [
    "thick",
    "A2",
    "形容詞",
    [
      "濃い",
      "厚い"
    ],
    "/θɪk/",
    "In addition to a thick fog, there was a heavy swell.",
    "濃霧に加えてうねりも高かった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/282257",
      "license": "CC BY 2.0 FR",
      "attribution": "#282257 (CM) / #121748 (mookeee)"
    }
  ],
  [
    "thief",
    "A2",
    "名詞",
    [
      "泥棒"
    ],
    "/θif/",
    "A thief broke in and made off with all my jewelry.",
    "泥棒が入って、私の宝石類をみんな持っていってしまった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/278618",
      "license": "CC BY 2.0 FR",
      "attribution": "#278618 (CK) / #125375 (bunbuku)"
    }
  ],
  [
    "thin",
    "A2",
    "形容詞",
    [
      "薄い",
      "密集していない"
    ],
    "/θɪn/",
    "The ice is so thin that it won't bear your weight.",
    "氷は非常に薄いので君の体重を支えきれないだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318332",
      "license": "CC BY 2.0 FR",
      "attribution": "#318332 (CK) / #85381 (huizi99)"
    }
  ],
  [
    "thinking",
    "A2",
    "名詞",
    [
      "思考",
      "考えること"
    ],
    "/ˈθɪŋkɪŋ/",
    "Critical thinking is an essential academic skill.",
    "批判的思考は重要な学術技能だ。",
    null
  ],
  [
    "third",
    "A2",
    "名詞",
    [
      "3分の1",
      "3分の1の"
    ],
    "/θɝd/",
    "Only one third of the members turned up at the meeting.",
    "その会合に姿を現したのはメンバーの３分の１だけだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/49154",
      "license": "CC BY 2.0 FR",
      "attribution": "#49154 (CK) / #211877 (tommy__san)"
    }
  ],
  [
    "this",
    "B1",
    "副詞",
    [
      "この",
      "この人"
    ],
    "/ðɪs/",
    "This city is not so busy as it used to be.",
    "この町は以前ほどにぎわっていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57833",
      "license": "CC BY 2.0 FR",
      "attribution": "#57833 (CM) / #220511 (KK_kaku_)"
    }
  ],
  [
    "thorough",
    "B2",
    "形容詞",
    [
      "徹底的な"
    ],
    "/ˈθɝoʊ/",
    "He made a thorough analysis of the problem.",
    "彼はその問題を徹底的に分析した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291350",
      "license": "CC BY 2.0 FR",
      "attribution": "#291350 (CM) / #112328 (bunbuku)"
    }
  ],
  [
    "thoroughly",
    "B2",
    "副詞",
    [
      "すっかり",
      "徹底的に"
    ],
    "/ˈθɝoʊli/",
    "When I reached the summit, I was thoroughly worn out.",
    "私は頂上に着いたとき、すっかり疲れきっていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/259529",
      "license": "CC BY 2.0 FR",
      "attribution": "#259529 (CM) / #155010 (mookeee)"
    }
  ],
  [
    "though",
    "B1",
    "副詞・接続詞",
    [
      "もっとも…ではあるが"
    ],
    "/ðoʊ/",
    "Even though he has a lot of money, he's not happy.",
    "彼は金持ちだが幸せではない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1230749",
      "license": "CC BY 2.0 FR",
      "attribution": "#1230749 (alec) / #108198 (small_snow)"
    }
  ],
  [
    "thought",
    "A2",
    "名詞",
    [
      "考え",
      "考えること"
    ],
    "/θɔt/",
    "At one time it was thought impracticable for man to fly.",
    "人が空を飛ぶのは不可能だと、かつては考えられていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269876",
      "license": "CC BY 2.0 FR",
      "attribution": "#269876 (CM) / #144688 (KK_kaku_)"
    }
  ],
  [
    "threat",
    "B2",
    "名詞",
    [
      "脅し"
    ],
    "/θrɛt/",
    "What he said was nothing less than a threat.",
    "彼の言ったことは脅しにほかならなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/286084",
      "license": "CC BY 2.0 FR",
      "attribution": "#286084 (CM) / #117580 (bunbuku)"
    }
  ],
  [
    "threaten",
    "B2",
    "動詞",
    [
      "を脅す",
      "脅す"
    ],
    "/ˈθrɛtən/",
    "They did not like the way he threatened his opponents.",
    "対戦相手を脅すという彼のやり方を彼らは気に入らなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/802711",
      "license": "CC BY 2.0 FR",
      "attribution": "#802711 (Source_VOA) / #1766823 (bunbuku)"
    }
  ],
  [
    "throat",
    "B1",
    "名詞",
    [
      "のど",
      "のど首"
    ],
    "/θroʊt/",
    "The initial symptoms of the disease are fever and sore throat.",
    "その病気の初期症状は高熱とのどの痛みです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/44314",
      "license": "CC BY 2.0 FR",
      "attribution": "#44314 (CK) / #207064 (bunbuku)"
    }
  ],
  [
    "throughout",
    "B1",
    "副詞・前置詞",
    [
      "じゅう"
    ],
    "/θruˈaʊt/",
    "The summit talks are to be broadcast simultaneously throughout the world.",
    "首脳会談は世界中で同時に放送される予定だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/266178",
      "license": "CC BY 2.0 FR",
      "attribution": "#266178 (CM) / #148381 (KK_kaku_)"
    }
  ],
  [
    "throw",
    "A2",
    "動詞",
    [
      "吐く",
      "投げる"
    ],
    "/θroʊ/",
    "I feel very sick. I think I'm going to throw up.",
    "ひどく気分が悪い。吐きそうだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9634989",
      "license": "CC BY 2.0 FR",
      "attribution": "#9634989 (CK) / #1643728 (mookeee)"
    }
  ],
  [
    "thumb",
    "B2",
    "名詞",
    [
      "親指",
      "を親指を立てて頼む"
    ],
    "/θʌm/",
    "He accidentally hit his thumb with the hammer.",
    "彼は過って親指を金槌で打ち付けた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/294514",
      "license": "CC BY 2.0 FR",
      "attribution": "#294514 (CK) / #109176 (bunbuku)"
    }
  ],
  [
    "thus",
    "B2",
    "副詞",
    [
      "かくかくして"
    ],
    "/ðʌs/",
    "Many women pursue higher education and careers, thus delaying marriage and childbirth.",
    "多くの女性がより高い教養とキャリアを追求し、それ故に結婚と出産を先延ばしにしている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327810",
      "license": "CC BY 2.0 FR",
      "attribution": "#327810 (CK) / #75908 (mookeee)"
    }
  ],
  [
    "tidy",
    "A2",
    "形容詞・動詞",
    [
      "きちんとした",
      "をきちんとする"
    ],
    "/ˈtaɪdi/",
    "I want to keep my room as tidy as possible.",
    "自分の部屋は出来るだけきちんとしておきたい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12805519",
      "license": "CC BY 2.0 FR",
      "attribution": "#12805519 (CK) / #149773 (bunbuku)"
    }
  ],
  [
    "tie",
    "A2",
    "名詞・動詞",
    [
      "ネクタイ",
      "タイになる"
    ],
    "/taɪ/",
    "I think that this tie will go great with that shirt.",
    "このネクタイはあのシャツにとても似合うと思うよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8180382",
      "license": "CC BY 2.0 FR",
      "attribution": "#8180382 (CK) / #1525397 (bunbuku)"
    }
  ],
  [
    "tight",
    "B1",
    "形容詞",
    [
      "すきまのない",
      "漏らない"
    ],
    "/taɪt/",
    "These shoes are so tight that I can't put them on.",
    "この靴はとてもきつくて履けない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59588",
      "license": "CC BY 2.0 FR",
      "attribution": "#59588 (saeb) / #222261 (small_snow)"
    }
  ],
  [
    "till",
    "B1",
    "接続詞・前置詞",
    [
      "まで"
    ],
    "/tɪl/",
    "The meeting will be postponed till the 20th of this month.",
    "会議は今月２０日に延期される。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/22489",
      "license": "CC BY 2.0 FR",
      "attribution": "#22489 (CK) / #185358 (wat)"
    }
  ],
  [
    "time",
    "B2",
    "動詞",
    [
      "時"
    ],
    "/taɪm/",
    "Any time will do so long as it is after six.",
    "６時以降ならいつでも結構です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72415",
      "license": "CC BY 2.0 FR",
      "attribution": "#72415 (CK) / #235038 (e4zh1nmcz)"
    }
  ],
  [
    "timing",
    "B2",
    "名詞",
    [
      "タイミング",
      "時期"
    ],
    "/ˈtaɪmɪŋ/",
    "Good timing was essential to the rescue.",
    "適切なタイミングが救助に不可欠だった。",
    null
  ],
  [
    "tin",
    "B1",
    "名詞",
    [
      "ブリキの",
      "ブリキ"
    ],
    "/tɪn/",
    "Do you know the difference between silver and tin?",
    "銀とブリキの区別がつきますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/387419",
      "license": "CC BY 2.0 FR",
      "attribution": "#387419 (CK) / #179603 (bunbuku)"
    }
  ],
  [
    "tiny",
    "B1",
    "形容詞",
    [
      "とても小さい"
    ],
    "/ˈtaɪni/",
    "It's a tiny country that most people have never heard of.",
    "それは、たいていの人は耳にしたこともない小さな国です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/42719",
      "license": "CC BY 2.0 FR",
      "attribution": "#42719 (CK) / #205474 (tommy__san)"
    }
  ],
  [
    "tip",
    "A2",
    "名詞・動詞",
    [
      "チップ",
      "にチップをやる"
    ],
    "/tɪp/",
    "If a porter carries your luggage, don't forget to tip him.",
    "ポーターに荷物を運んでもらったら、チップを渡すのを忘れちゃだめだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1963270",
      "license": "CC BY 2.0 FR",
      "attribution": "#1963270 (CK) / #1515651 (CHNO)"
    }
  ],
  [
    "tissue",
    "B2",
    "名詞",
    [
      "ティッシュ",
      "組織"
    ],
    "/ˈtɪsju/",
    "Does anyone have a tissue?",
    "誰かティッシュ持ってない？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4828362",
      "license": "CC BY 2.0 FR",
      "attribution": "#4828362 (Hybrid) / #12101375 (bunbuku)"
    }
  ],
  [
    "title",
    "B2",
    "動詞",
    [
      "肩書き"
    ],
    "/ˈtaɪtəl/",
    "His official title is Director-General of the Environment Agency.",
    "彼の公式の肩書きは環境庁長官です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/286189",
      "license": "CC BY 2.0 FR",
      "attribution": "#286189 (bluepie88) / #117475 (mookeee)"
    }
  ],
  [
    "toe",
    "B1",
    "名詞",
    [
      "を斜めに打ち込む"
    ],
    "/toʊ/",
    "He fell into the cesspool and got covered from head to toe.",
    "ころんでこえだめに落ち、頭からどっぷりと浸かってしまった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327009",
      "license": "CC BY 2.0 FR",
      "attribution": "#327009 (CK) / #76711 (bunbuku)"
    }
  ],
  [
    "ton",
    "B2",
    "名詞",
    [
      "トン"
    ],
    "/tʌn/",
    "We used a couple of tons of coal last winter.",
    "うちでは去年の冬、石炭を数トン使った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6341318",
      "license": "CC BY 2.0 FR",
      "attribution": "#6341318 (CK) / #12375533 (YumaSalty)"
    }
  ],
  [
    "tone",
    "B2",
    "名詞",
    [
      "言い方"
    ],
    "/toʊn/",
    "You don't have to use such a harsh tone with me.",
    "そんなトゲトゲしい言い方しなくたっていいだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41554",
      "license": "CC BY 2.0 FR",
      "attribution": "#41554 (Swift) / #204312 (KK_kaku_)"
    }
  ],
  [
    "tongue",
    "B1",
    "名詞",
    [
      "母語",
      "舌"
    ],
    "/tʌŋ/",
    "The foreigner spoke Japanese as if it were her mother tongue.",
    "その外国人はまるで母語のように日本語を話した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/48973",
      "license": "CC BY 2.0 FR",
      "attribution": "#48973 (CM) / #211696 (Blanka_Meduzo)"
    }
  ],
  [
    "tonne",
    "B2",
    "名詞",
    [
      "metric ton メートルトン"
    ],
    "/tʌn/",
    "The truck can carry one tonne of material.",
    "そのトラックは1トンの資材を運べる。",
    null
  ],
  [
    "tool",
    "A2",
    "名詞",
    [
      "道具",
      "道具に使われる人"
    ],
    "/tul/",
    "I'll lend you the tools that you need to do that.",
    "それに必要な道具は貸してあげるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6812349",
      "license": "CC BY 2.0 FR",
      "attribution": "#6812349 (CK) / #11540101 (bunbuku)"
    }
  ],
  [
    "top",
    "A2",
    "形容詞・名詞",
    [
      "首位",
      "頂上"
    ],
    "/tɑp/",
    "At school he was always at the top of his class.",
    "学校では彼はいつもトップだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21608",
      "license": "CC BY 2.0 FR",
      "attribution": "#21608 (CK) / #184480 (small_snow)"
    }
  ],
  [
    "total",
    "B1",
    "形容詞・名詞",
    [
      "総額",
      "合計"
    ],
    "/ˈtoʊtəl/",
    "Can you work out the total cost of the trip?",
    "旅行の総費用を計算してくれますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325557",
      "license": "CC BY 2.0 FR",
      "attribution": "#325557 (CM) / #78161 (mookeee)"
    }
  ],
  [
    "totally",
    "B1",
    "副詞",
    [
      "すっかり",
      "完全に"
    ],
    "/ˈtoʊtəli/",
    "We were totally exhausted from the five-hour trip.",
    "私たちは５時間の旅でぐったりしてしまった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1410972",
      "license": "CC BY 2.0 FR",
      "attribution": "#1410972 (CK) / #166668 (bunbuku)"
    }
  ],
  [
    "touch",
    "A2",
    "名詞・動詞",
    [
      "に影響する",
      "関係する"
    ],
    "/tʌtʃ/",
    "I'll get in touch with you as soon as I arrive.",
    "着いたらすぐ連絡するね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277438",
      "license": "CC BY 2.0 FR",
      "attribution": "#277438 (CK) / #9969751 (bunbuku)"
    }
  ],
  [
    "tough",
    "B2",
    "形容詞",
    [
      "タフな",
      "融通のきかない"
    ],
    "/tʌf/",
    "He won't be easily discouraged, because he's a tough guy.",
    "彼はタフだから少しのことではへこたれない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/291677",
      "license": "CC BY 2.0 FR",
      "attribution": "#291677 (Dejo) / #112001 (bunbuku)"
    }
  ],
  [
    "tour",
    "A2",
    "名詞・動詞",
    [
      "旅行"
    ],
    "/tʊr/",
    "The travel company furnished us with all the details of the tour.",
    "旅行会社は旅行の詳細を全て私たちに教えてくれた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325573",
      "license": "CC BY 2.0 FR",
      "attribution": "#325573 (CM) / #78145 (mookeee)"
    }
  ],
  [
    "tourism",
    "A2",
    "名詞",
    [
      "観光旅行",
      "観光事業"
    ],
    "/ˈtʊrɪzəm/",
    "Tourism generated many new jobs.",
    "観光が多くの新しい仕事を生み出した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/20931",
      "license": "CC BY 2.0 FR",
      "attribution": "#20931 (CK) / #183807 (bunbuku)"
    }
  ],
  [
    "tournament",
    "B2",
    "名詞",
    [
      "トーナメント"
    ],
    "/ˈtʊrnəmənt/",
    "He won the first prize at the chess tournament.",
    "彼はチェスのトーナメントで優勝を勝ち取った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1316819",
      "license": "CC BY 2.0 FR",
      "attribution": "#1316819 (CK) / #111964 (bunbuku)"
    }
  ],
  [
    "towards",
    "A2",
    "前置詞",
    [
      "〜の方へ"
    ],
    "/təˈwɔrdz/",
    "Both parties took a step towards a solution.",
    "両者は解決に向かって一歩踏み出した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325635",
      "license": "CC BY 2.0 FR",
      "attribution": "#325635 (CM) / #78083 (mookeee)"
    }
  ],
  [
    "towel",
    "A2",
    "名詞",
    [
      "タオル",
      "をタオルでふく"
    ],
    "/ˈtaʊəl/",
    "This towel is so soft and fluffy. It feels good!",
    "このタオル、ふわふわで気持ちいいよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1164640",
      "license": "CC BY 2.0 FR",
      "attribution": "#1164640 (Chrikaru) / #978645 (bunbuku)"
    }
  ],
  [
    "tower",
    "A2",
    "名詞",
    [
      "塔"
    ],
    "/ˈtaʊɚ/",
    "Galileo dropped two iron balls from the top of the tower.",
    "ガリレオは二つの鉄の玉を塔のてっぺんから落とした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63504",
      "license": "CC BY 2.0 FR",
      "attribution": "#63504 (CK) / #226164 (tommy__san)"
    }
  ],
  [
    "toy",
    "A2",
    "形容詞・名詞",
    [
      "おもちゃ",
      "おもちゃの"
    ],
    "/tɔɪ/",
    "The boy has taken the toy away from his little sister.",
    "少年は妹のおもちゃを取ってしまった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/268045",
      "license": "CC BY 2.0 FR",
      "attribution": "#268045 (CK) / #146517 (bunbuku)"
    }
  ],
  [
    "trace",
    "B2",
    "動詞",
    [
      "跡",
      "痕跡"
    ],
    "/treɪs/",
    "When I got back, my bag had disappeared without a trace.",
    "戻ってみると私のバッグは影も形もなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/323839",
      "license": "CC BY 2.0 FR",
      "attribution": "#323839 (CM) / #79879 (small_snow)"
    }
  ],
  [
    "track",
    "A2",
    "名詞・動詞",
    [
      "突き止める",
      "跡を追う"
    ],
    "/træk/",
    "The police managed to track down the owner of the car.",
    "警察は車の持ち主を何とか突きとめることができた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/238301",
      "license": "CC BY 2.0 FR",
      "attribution": "#238301 (CK) / #176164 (bunbuku)"
    }
  ],
  [
    "trade",
    "B1",
    "名詞・動詞",
    [
      "貿易をする"
    ],
    "/treɪd/",
    "Trade friction might arise between the two nations at any moment.",
    "今にも両国間に貿易摩擦が生じそうだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/241718",
      "license": "CC BY 2.0 FR",
      "attribution": "#241718 (CM) / #172756 (bunbuku)"
    }
  ],
  [
    "trading",
    "B2",
    "名詞",
    [
      "取引",
      "貿易"
    ],
    "/ˈtreɪdɪŋ/",
    "The insider trading scandal put a lot of people out of business.",
    "インサイダー取引スキャンダルによって多数の人が破産しました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/65749",
      "license": "CC BY 2.0 FR",
      "attribution": "#65749 (CK) / #228393 (mookeee)"
    }
  ],
  [
    "tradition",
    "A2",
    "名詞",
    [
      "伝統"
    ],
    "/trəˈdɪʃən/",
    "This tradition has been passed down from generation to generation.",
    "この伝統は代々受け継がれている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57714",
      "license": "CC BY 2.0 FR",
      "attribution": "#57714 (CK) / #220392 (tommy__san)"
    }
  ],
  [
    "traditional",
    "A2",
    "形容詞",
    [
      "伝統的な"
    ],
    "/trəˈdɪʃənəl/",
    "Traditional Japanese sweets really do go well with Japanese tea.",
    "和菓子にはやっぱり日本茶が合う。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2325070",
      "license": "CC BY 2.0 FR",
      "attribution": "#2325070 (CK) / #2319231 (tommy_san)"
    }
  ],
  [
    "tragedy",
    "B2",
    "名詞",
    [
      "悲劇",
      "悲劇的要素"
    ],
    "/ˈtrædʒədi/",
    "The tragedy must be remembered so that it is not repeated.",
    "同じことが繰り返されないために、その悲劇を忘れてはならない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/44386",
      "license": "CC BY 2.0 FR",
      "attribution": "#44386 (CK) / #123722 (bunbuku)"
    }
  ],
  [
    "tragic",
    "B2",
    "形容詞",
    [
      "悲惨"
    ],
    "/ˈtrædʒɪk/",
    "The accident had a tragic outcome.",
    "その事故は悲惨な結果になった。",
    null
  ],
  [
    "train",
    "A2",
    "動詞",
    [
      "列車"
    ],
    "/treɪn/",
    "How long does it take to get to the train station?",
    "駅に着くのにどのくらいかかりますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/386696",
      "license": "CC BY 2.0 FR",
      "attribution": "#386696 (Mouseneb) / #234128 (bunbuku)"
    }
  ],
  [
    "trainer",
    "A2",
    "名詞",
    [
      "トレーナー"
    ],
    "/ˈtreɪnɚ/",
    "Tom used to be a professional dog trainer.",
    "トムはかつて、プロのドッグトレーナーだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/8456689",
      "license": "CC BY 2.0 FR",
      "attribution": "#8456689 (CK) / #11737509 (bunbuku)"
    }
  ],
  [
    "training",
    "A2",
    "名詞",
    [
      "研修",
      "訓練"
    ],
    "/ˈtreɪnɪŋ/",
    "The training session is scheduled to begin at 4 p.m.",
    "研修会は午後4時開始予定です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/239259",
      "license": "CC BY 2.0 FR",
      "attribution": "#239259 (CM) / #175207 (small_snow)"
    }
  ],
  [
    "trait",
    "B2",
    "名詞",
    [
      "特性"
    ],
    "/treɪt/",
    "He has no redeeming traits.",
    "彼は何の取り柄もない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/476197",
      "license": "CC BY 2.0 FR",
      "attribution": "#476197 (CM) / #109401 (small_snow)"
    }
  ],
  [
    "transfer",
    "B2",
    "名詞・動詞",
    [
      "転校生",
      "転校"
    ],
    "/trænsˈfɝ/",
    "The transfer student in the other class is a super good-looking guy.",
    "隣のクラスの転校生、超イケメンだって。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/893831",
      "license": "CC BY 2.0 FR",
      "attribution": "#893831 (Scott) / #892992 (bunbuku)"
    }
  ],
  [
    "transform",
    "B2",
    "動詞",
    [
      "を変える",
      "を変圧する"
    ],
    "/trænsˈfɔrm/",
    "The project could transform the local economy.",
    "その事業は地域経済を変える可能性がある。",
    null
  ],
  [
    "transition",
    "B2",
    "名詞",
    [
      "過渡期"
    ],
    "/trænˈzɪʃən/",
    "The educational system is in transition.",
    "教育制度は過渡期にある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/19106",
      "license": "CC BY 2.0 FR",
      "attribution": "#19106 (CK) / #180315 (tommy__san)"
    }
  ],
  [
    "translate",
    "B1",
    "動詞",
    [
      "翻訳する",
      "を翻訳する"
    ],
    "/trænzˈleɪt/",
    "It is difficult to translate a poem into another language.",
    "詩を別の言語に翻訳するのは難しい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/263395",
      "license": "CC BY 2.0 FR",
      "attribution": "#263395 (megamanenm) / #151161 (bunbuku)"
    }
  ],
  [
    "translation",
    "B1",
    "名詞",
    [
      "翻訳",
      "翻訳されたもの"
    ],
    "/trænzˈleɪʃən/",
    "Thanks to translation tools, I often visit websites in other countries.",
    "翻訳ツールのおかげで外国のサイトもよく見るようになった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11014559",
      "license": "CC BY 2.0 FR",
      "attribution": "#11014559 (CK) / #11014059 (KK_kaku_)"
    }
  ],
  [
    "transmit",
    "B2",
    "動詞",
    [
      "伝導する",
      "を放送する"
    ],
    "/trænzˈmɪt/",
    "Water transmits sound better than air.",
    "水は空気よりも音をよく伝達する。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270800",
      "license": "CC BY 2.0 FR",
      "attribution": "#270800 (CM) / #143767 (KK_kaku_)"
    }
  ],
  [
    "transport",
    "A2",
    "名詞・動詞",
    [
      "輸送",
      "を輸送する"
    ],
    "/trænsˈpɔrt/",
    "The box was crushed during transport and the contents flew out.",
    "輸送中に箱が拉げて中身がとび出した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/328033",
      "license": "CC BY 2.0 FR",
      "attribution": "#328033 (Delian) / #75685 (mookeee)"
    }
  ],
  [
    "transportation",
    "B2",
    "名詞",
    [
      "交通手段",
      "輸送"
    ],
    "/trænspɚˈteɪʃən/",
    "Today, automobiles have replaced horses as the primary means of transportation.",
    "今日、自動車は、馬に代わる主要な交通手段となっています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11179159",
      "license": "CC BY 2.0 FR",
      "attribution": "#11179159 (CK) / #11179153 (bunbuku)"
    }
  ],
  [
    "trap",
    "B2",
    "名詞・動詞",
    [
      "わな"
    ],
    "/træp/",
    "The enemy is caught like a mouse in a trap.",
    "敵はもう袋のネズミだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/278675",
      "license": "CC BY 2.0 FR",
      "attribution": "#278675 (CM) / #125317 (bunbuku)"
    }
  ],
  [
    "traveller",
    "A2",
    "名詞",
    [
      "旅行者"
    ],
    "/ˈtrævəlɚ/",
    "Each traveller must complete an arrival form.",
    "旅行者はそれぞれ到着用紙に記入しなければならない。",
    null
  ],
  [
    "treasure",
    "B2",
    "名詞",
    [
      "財宝"
    ],
    "/ˈtrɛʒɚ/",
    "It is said that treasure is buried in this area.",
    "この区域に財宝が埋まっているという話だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59605",
      "license": "CC BY 2.0 FR",
      "attribution": "#59605 (CM) / #222278 (bunbuku)"
    }
  ],
  [
    "treat",
    "B1",
    "動詞",
    [
      "治療する"
    ],
    "/trit/",
    "Don't treat me the same way you would treat a child.",
    "僕を子供扱いするなよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1331988",
      "license": "CC BY 2.0 FR",
      "attribution": "#1331988 (CK) / #81697 (bunbuku)"
    }
  ],
  [
    "treatment",
    "B1",
    "名詞",
    [
      "治療法",
      "治療"
    ],
    "/ˈtritmənt/",
    "Luckily, the treatment was only ineffective instead of harmful.",
    "運の良いことに、その治療法に害はなく、効果が無いだけだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/840112",
      "license": "CC BY 2.0 FR",
      "attribution": "#840112 (papabear) / #866784 (thyc244)"
    }
  ],
  [
    "trend",
    "B1",
    "名詞",
    [
      "流行"
    ],
    "/trɛnd/",
    "I gave up keeping up with trends.",
    "流行に付いて行くことはやめた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325463",
      "license": "CC BY 2.0 FR",
      "attribution": "#325463 (CM) / #78250 (mookeee)"
    }
  ],
  [
    "trial",
    "B2",
    "名詞",
    [
      "試行",
      "裁判"
    ],
    "/ˈtraɪəl/",
    "Trial and error is essential to progress.",
    "試行錯誤は進歩に不可欠だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/263501",
      "license": "CC BY 2.0 FR",
      "attribution": "#263501 (CM) / #151055 (KK_kaku_)"
    }
  ],
  [
    "tribe",
    "B2",
    "名詞",
    [
      "族"
    ],
    "/traɪb/",
    "The natives of the North-West Pacific Coast of America were probably descendants of tribes from Asia.",
    "アメリカの太平洋北西海岸沿いに住む原住民は、おそらくアジアから移住した種族の子孫なのである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/67567",
      "license": "CC BY 2.0 FR",
      "attribution": "#67567 (CM) / #230202 (wat)"
    }
  ],
  [
    "trick",
    "B1",
    "名詞・動詞",
    [
      "手品",
      "仕掛け"
    ],
    "/trɪk/",
    "The magician taught us a simple card trick.",
    "その手品師は私たちに簡単なカード手品を教えた。",
    null
  ],
  [
    "trigger",
    "B2",
    "動詞",
    [
      "引き金"
    ],
    "/ˈtrɪgɚ/",
    "I pulled the trigger again and again.",
    "私は連続で引き金を引いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11243550",
      "license": "CC BY 2.0 FR",
      "attribution": "#11243550 (pip) / #10996935 (bunbuku)"
    }
  ],
  [
    "trillion",
    "B2",
    "数詞",
    [
      "兆"
    ],
    "/ˈtrɪljən/",
    "The country's economy is worth over a trillion dollars.",
    "その国の経済規模は1兆ドルを超える。",
    null
  ],
  [
    "trip",
    "B2",
    "動詞",
    [
      "旅行",
      "旅"
    ],
    "/trɪp/",
    "A trip by boat takes more time than one by car.",
    "船での旅行は車でよりも時間がかかる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/561570",
      "license": "CC BY 2.0 FR",
      "attribution": "#561570 (Nm) / #545846 (tsukimori)"
    }
  ],
  [
    "troop",
    "B2",
    "名詞",
    [
      "軍隊",
      "を先頭に立てて分列行進をする"
    ],
    "/trup/",
    "Troops were swiftly called in to put down the riot.",
    "暴動を鎮圧するために直ちに軍隊が派遣された。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/321209",
      "license": "CC BY 2.0 FR",
      "attribution": "#321209 (CM) / #82507 (KK_kaku_)"
    }
  ],
  [
    "tropical",
    "B2",
    "形容詞",
    [
      "熱帯の",
      "熱帯性の"
    ],
    "/ˈtrɑpɪkəl/",
    "Thousands of hectares of tropical rainforest are being lost every day.",
    "何千ヘクタールもの熱帯雨林が毎日失われている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2698884",
      "license": "CC BY 2.0 FR",
      "attribution": "#2698884 (WestofEden) / #1005855 (mookeee)"
    }
  ],
  [
    "trouble",
    "A2",
    "名詞・動詞",
    [
      "困ったこと",
      "問題"
    ],
    "/ˈtrʌbəl/",
    "The trouble is that I have no money on me now.",
    "困ったことに私は今お金の持ち合わせがない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/243450",
      "license": "CC BY 2.0 FR",
      "attribution": "#243450 (CK) / #236844 (mookeee)"
    }
  ],
  [
    "truck",
    "A2",
    "名詞",
    [
      "トラック",
      "をトラックで運ぶ"
    ],
    "/trʌk/",
    "That kid was almost run over when the truck backed up.",
    "その子はトラックがバックしてきた時轢かれそうになった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/47514",
      "license": "CC BY 2.0 FR",
      "attribution": "#47514 (Zifre) / #210249 (bunbuku)"
    }
  ],
  [
    "truly",
    "B2",
    "副詞",
    [
      "まことに"
    ],
    "/ˈtruli/",
    "I can take care of yours truly.",
    "自分のことは自分でできる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/264629",
      "license": "CC BY 2.0 FR",
      "attribution": "#264629 (CK) / #149929 (small_snow)"
    }
  ],
  [
    "trust",
    "B2",
    "名詞・動詞",
    [
      "を信用する"
    ],
    "/trʌst/",
    "I have no idea to what extent I can trust them.",
    "どの程度まで彼らを信じてよいのかわからない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/37473",
      "license": "CC BY 2.0 FR",
      "attribution": "#37473 (CK) / #200272 (bunbuku)"
    }
  ],
  [
    "truth",
    "B1",
    "名詞",
    [
      "真理"
    ],
    "/truθ/",
    "There is a certain amount of truth in what he's saying.",
    "彼が言う事にも一面の真理がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/74002",
      "license": "CC BY 2.0 FR",
      "attribution": "#74002 (Swift) / #237577 (arihato)"
    }
  ],
  [
    "try",
    "B2",
    "名詞",
    [
      "してみる",
      "使ってみる"
    ],
    "/traɪ/",
    "Try on this new suit to see if it fits well.",
    "サイズが合うかどうか、この新しいスーツを着てみて。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/34762",
      "license": "CC BY 2.0 FR",
      "attribution": "#34762 (CK) / #1138945 (bunbuku)"
    }
  ],
  [
    "tsunami",
    "B2",
    "名詞",
    [
      "津波"
    ],
    "/tsuˈnɑmi/",
    "There was an earthquake and, in addition, there was a tsunami.",
    "地震が起こり、さらに津波が襲った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277186",
      "license": "CC BY 2.0 FR",
      "attribution": "#277186 (CM) / #126904 (small_snow)"
    }
  ],
  [
    "tube",
    "B1",
    "名詞",
    [
      "チューブ"
    ],
    "/tub/",
    "The cream comes in a small tube.",
    "そのクリームは小さなチューブに入っている。",
    null
  ],
  [
    "tune",
    "B2",
    "名詞",
    [
      "曲"
    ],
    "/tun/",
    "One of my favorite tunes was playing on the radio.",
    "私の好きな歌がラジオでかかっていた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/250852",
      "license": "CC BY 2.0 FR",
      "attribution": "#250852 (CK) / #163660 (tommy__san)"
    }
  ],
  [
    "tunnel",
    "B2",
    "名詞",
    [
      "トンネル",
      "にトンネルを掘る"
    ],
    "/ˈtʌnəl/",
    "The new tunnel will link Great Britain and France.",
    "その新しいトンネルによってイギリスとフランスが繋がります。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/666046",
      "license": "CC BY 2.0 FR",
      "attribution": "#666046 (bluepie88) / #939168 (thyc244)"
    }
  ],
  [
    "twin",
    "A2",
    "形容詞・名詞",
    [
      "ふたごの",
      "ふたご"
    ],
    "/twɪn/",
    "The twin girls looked so similar that I couldn't tell them apart.",
    "そのふたごの女の子はとてもよく似ていて、私には区別がつかなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12199725",
      "license": "CC BY 2.0 FR",
      "attribution": "#12199725 (CK) / #212676 (bunbuku)"
    }
  ],
  [
    "type",
    "B1",
    "動詞",
    [
      "タイプ",
      "をタイプに打つ"
    ],
    "/taɪp/",
    "This is the same type of car as my father has.",
    "この車は父が持っているのと同じタイプの車だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58700",
      "license": "CC BY 2.0 FR",
      "attribution": "#58700 (CK) / #221375 (bunbuku)"
    }
  ],
  [
    "typical",
    "A2",
    "形容詞",
    [
      "いかにも〜らしい",
      "典型的な"
    ],
    "/ˈtɪpəkəl/",
    "It was typical of him to arrive late.",
    "遅れてやってくるのは、いかにも彼のやりそうなことだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277382",
      "license": "CC BY 2.0 FR",
      "attribution": "#277382 (CM) / #126708 (bunbuku)"
    }
  ],
  [
    "typically",
    "B1",
    "副詞",
    [
      "典型的に"
    ],
    "/ˈtɪpɪkli/",
    "The journey typically takes about two hours.",
    "その旅は通常約2時間かかる。",
    null
  ],
  [
    "tyre",
    "B1",
    "名詞",
    [
      "タイヤ"
    ],
    "/taɪr/",
    "We replaced the damaged tyre before leaving.",
    "出発前に傷んだタイヤを交換した。",
    null
  ],
  [
    "ugly",
    "B1",
    "形容詞",
    [
      "醜い"
    ],
    "/ˈʌgli/",
    "An ugly man knocked on my door.",
    "１人の醜い男が私の家の戸をたたいた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73119",
      "license": "CC BY 2.0 FR",
      "attribution": "#73119 (CK) / #235739 (e4zh1nmcz)"
    }
  ],
  [
    "ultimate",
    "B2",
    "形容詞",
    [
      "究極の"
    ],
    "/ˈʌltəmət/",
    "Our ultimate goal is to establish world peace.",
    "我々の究極の目標は世界平和を樹立することである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/23432",
      "license": "CC BY 2.0 FR",
      "attribution": "#23432 (CK) / #186296 (tommy__san)"
    }
  ],
  [
    "ultimately",
    "B2",
    "副詞",
    [
      "ついに"
    ],
    "/ˈʌltəmətli/",
    "The rebel was ultimately captured and confined to jail.",
    "ついに反逆者は捕らえられ、拘置所に入れられた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/39883",
      "license": "CC BY 2.0 FR",
      "attribution": "#39883 (CM) / #202649 (arnab)"
    }
  ],
  [
    "unable",
    "B1",
    "形容詞",
    [
      "〜できない"
    ],
    "/əˈneɪbəl/",
    "She was choked with tears and was unable to speak.",
    "涙にむせんで何も言えなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/325989",
      "license": "CC BY 2.0 FR",
      "attribution": "#325989 (CM) / #77729 (mookeee)"
    }
  ],
  [
    "unacceptable",
    "B2",
    "形容詞",
    [
      "容認できない",
      "受け入れられない"
    ],
    "/ʌnækˈsɛptəbəl/",
    "The level of pollution is completely unacceptable.",
    "その汚染水準はまったく容認できない。",
    null
  ],
  [
    "uncertainty",
    "B2",
    "名詞",
    [
      "不確実性",
      "不安"
    ],
    "/ənˈsɝtənti/",
    "Economic uncertainty reduced business investment.",
    "経済の不確実性が企業投資を減らした。",
    null
  ],
  [
    "uncomfortable",
    "B1",
    "形容詞",
    [
      "心地よくない"
    ],
    "/ənˈkʌmfɚtəbəl/",
    "I felt uncomfortable and wanted to leave, but I stayed.",
    "居心地が悪くて帰りたかったけど、そのまま残ったよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7708230",
      "license": "CC BY 2.0 FR",
      "attribution": "#7708230 (CK) / #11328059 (bunbuku)"
    }
  ],
  [
    "unconscious",
    "B2",
    "形容詞",
    [
      "意識を失った",
      "無意識の"
    ],
    "/ʌnˈkɑnʃəs/",
    "She was unconscious for a whole day after the accident.",
    "彼女は事故の後丸一日意識不明だった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/314510",
      "license": "CC BY 2.0 FR",
      "attribution": "#314510 (CK) / #89197 (small_snow)"
    }
  ],
  [
    "undergo",
    "B2",
    "動詞",
    [
      "を受ける"
    ],
    "/ʌndɚˈgoʊ/",
    "Her mother is going to undergo a major operation next week.",
    "彼女の母は来週大きな手術を受けることになっている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309751",
      "license": "CC BY 2.0 FR",
      "attribution": "#309751 (CK) / #93955 (bunbuku)"
    }
  ],
  [
    "underground",
    "A2",
    "形容詞・副詞",
    [
      "地下の",
      "地下に"
    ],
    "/ˈʌndɚgraʊnd/",
    "Some vineyards still choose to irrigate using underground water sources.",
    "ワイン畑の中には、未だ地下水を使用した灌漑を選択するところもある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11118224",
      "license": "CC BY 2.0 FR",
      "attribution": "#11118224 (CM) / #11124049 (KF)"
    }
  ],
  [
    "understanding",
    "A2",
    "名詞",
    [
      "理解",
      "理解力"
    ],
    "/ʌndɚˈstændɪŋ/",
    "Nobody contributed to the understanding of dreams as much as Freud.",
    "フロイトほど夢の理解に貢献した人はいない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/34065",
      "license": "CC BY 2.0 FR",
      "attribution": "#34065 (CK) / #196886 (tommy__san)"
    }
  ],
  [
    "undertake",
    "B2",
    "動詞",
    [
      "を引き受ける"
    ],
    "/ˈʌndɚteɪk/",
    "I have half a mind to undertake the work.",
    "その仕事を引き受けようかと思っているんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/47592",
      "license": "CC BY 2.0 FR",
      "attribution": "#47592 (CM) / #210326 (bunbuku)"
    }
  ],
  [
    "underwear",
    "B1",
    "名詞",
    [
      "下着"
    ],
    "/ˈʌndɚwɛr/",
    "Why do we have to wear underwear?",
    "なんでパンツをはかなきゃいけないの？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10022316",
      "license": "CC BY 2.0 FR",
      "attribution": "#10022316 (DJ_Saidez) / #10022313 (Sim5634)"
    }
  ],
  [
    "unemployed",
    "B1",
    "形容詞",
    [
      "失業者",
      "失業した"
    ],
    "/ʌnɛmpˈlɔɪd/",
    "I hear that the number of the unemployed has been increasing recently.",
    "失業者の数が最近、増加しているそうだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/264947",
      "license": "CC BY 2.0 FR",
      "attribution": "#264947 (CM) / #149611 (tommy__san)"
    }
  ],
  [
    "unemployment",
    "B1",
    "名詞",
    [
      "失業",
      "失業者"
    ],
    "/ʌnɪmpˈlɔɪmənt/",
    "The unemployment rate in Japan was 3.4 percent in September of 2015.",
    "2015年9月の日本の失業率は3.4パーセントだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4704215",
      "license": "CC BY 2.0 FR",
      "attribution": "#4704215 (CK) / #4704203 (anhgosho)"
    }
  ],
  [
    "unexpected",
    "B2",
    "形容詞",
    [
      "予期しない"
    ],
    "/ʌnɪksˈpɛktɪd/",
    "A little bit of luck sometimes leads to an unexpected success.",
    "ちょっとした幸運が予期せぬ成功につながるときもある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/40065",
      "license": "CC BY 2.0 FR",
      "attribution": "#40065 (CK) / #202830 (tommy_san)"
    }
  ],
  [
    "unfair",
    "B1",
    "形容詞",
    [
      "不当な",
      "公正でない"
    ],
    "/ənˈfɛr/",
    "Unless Japan eliminates its unfair tariffs, the U.S. will impose sanctions.",
    "日本が不当な関税を撤廃しない限り、合衆国は制裁を科すだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/281172",
      "license": "CC BY 2.0 FR",
      "attribution": "#281172 (CM) / #3465108 (arnab)"
    }
  ],
  [
    "unfold",
    "B2",
    "動詞",
    [
      "を広げる"
    ],
    "/ənˈfoʊld/",
    "Let's unfold the map on the table and discuss it.",
    "地図をテーブルに広げて話し合おう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/963350",
      "license": "CC BY 2.0 FR",
      "attribution": "#963350 (CK) / #126855 (mookeee)"
    }
  ],
  [
    "unfortunate",
    "B2",
    "形容詞",
    [
      "不運な"
    ],
    "/ənˈfɔrtʃənət/",
    "It was unfortunate that it rained yesterday.",
    "昨日はあいにくの雨でしたね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/244558",
      "license": "CC BY 2.0 FR",
      "attribution": "#244558 (CK) / #11156221 (bunbuku)"
    }
  ],
  [
    "unfortunately",
    "A2",
    "副詞",
    [
      "不幸にも"
    ],
    "/ənˈfɔrtʃənətli/",
    "Unfortunately, the food supplies gave out before the end of winter.",
    "残念なことに、冬が終わる前に食料が底をついてしまった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318612",
      "license": "CC BY 2.0 FR",
      "attribution": "#318612 (CK) / #10324288 (bunbuku)"
    }
  ],
  [
    "unhappy",
    "A2",
    "形容詞",
    [
      "不幸な",
      "適切でない"
    ],
    "/ənˈhæpi/",
    "We are never as happy or as unhappy as we imagine.",
    "我々が思っているほどには、それほど我々は幸福でもなければ、不幸でもない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/699411",
      "license": "CC BY 2.0 FR",
      "attribution": "#699411 (CK) / #185953 (Blanka_Meduzo)"
    }
  ],
  [
    "uniform",
    "A2",
    "名詞",
    [
      "制服",
      "に制服を貸与する"
    ],
    "/ˈjunəfɔrm/",
    "When was the last time you wore a uniform?",
    "最後に制服を着たのって、いつ？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6342472",
      "license": "CC BY 2.0 FR",
      "attribution": "#6342472 (CK) / #12608167 (bunbuku)"
    }
  ],
  [
    "union",
    "B1",
    "名詞",
    [
      "労働組合"
    ],
    "/ˈjunjən/",
    "The union is pressing for a ten-percent pay hike.",
    "組合は１０パーセントの賃上げを迫っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273958",
      "license": "CC BY 2.0 FR",
      "attribution": "#273958 (CM) / #140615 (bunbuku)"
    }
  ],
  [
    "unique",
    "B2",
    "形容詞",
    [
      "独特の"
    ],
    "/juˈnik/",
    "This custom is unique to America.",
    "この習慣はアメリカ独特のものである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58579",
      "license": "CC BY 2.0 FR",
      "attribution": "#58579 (CK) / #221256 (tommy__san)"
    }
  ],
  [
    "unit",
    "A2",
    "名詞",
    [
      "設備一式",
      "単位"
    ],
    "/ˈjunət/",
    "Each apartment has its own air-conditioning unit.",
    "各住戸には専用の空調設備がある。",
    null
  ],
  [
    "unite",
    "B2",
    "動詞",
    [
      "あわせ持つ"
    ],
    "/ˈjunaɪt/",
    "If we unite our efforts, we'll be able to finish this.",
    "力を合わせれば、これを終わらせられるだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9056169",
      "license": "CC BY 2.0 FR",
      "attribution": "#9056169 (CM) / #77808 (mookeee)"
    }
  ],
  [
    "united",
    "A2",
    "形容詞",
    [
      "団結した",
      "一体となった"
    ],
    "/juˈnaɪtɪd/",
    "The community remained united during the crisis.",
    "地域社会は危機の間も団結していた。",
    null
  ],
  [
    "unity",
    "B2",
    "名詞",
    [
      "連帯感",
      "団結"
    ],
    "/ˈjunəti/",
    "The crisis created a strong sense of unity.",
    "危機によって強い連帯感が生まれた。",
    null
  ],
  [
    "universal",
    "B2",
    "形容詞",
    [
      "全世界の",
      "普遍的な"
    ],
    "/junəˈvɝsəl/",
    "The egg is a universal symbol of life and rebirth.",
    "「卵」は生命と再生の世界的なシンボルです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1522144",
      "license": "CC BY 2.0 FR",
      "attribution": "#1522144 (LittleBoy) / #2142171 (Blanka_Meduzo)"
    }
  ],
  [
    "universe",
    "B2",
    "名詞",
    [
      "宇宙"
    ],
    "/ˈjunəvɝs/",
    "The origin of the universe will probably never be explained.",
    "宇宙の起源はおそらく永遠に説明されないだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/27036",
      "license": "CC BY 2.0 FR",
      "attribution": "#27036 (Swift) / #189880 (tommy__san)"
    }
  ],
  [
    "unknown",
    "B2",
    "形容詞",
    [
      "無名の"
    ],
    "/ənˈnoʊn/",
    "Many great thinkers who were unknown while alive became famous after death.",
    "生前に無名であった多くの偉大な思想家は、死後に名声を得た。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/847235",
      "license": "CC BY 2.0 FR",
      "attribution": "#847235 (Source_Benedict_1921) / #943488 (thyc244)"
    }
  ],
  [
    "unless",
    "B1",
    "接続詞",
    [
      "でないかぎり"
    ],
    "/ənˈlɛs/",
    "I won't divorce you unless you give me a good reason.",
    "正当な理由がない限り、お前と離婚するつもりはないからな。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1224656",
      "license": "CC BY 2.0 FR",
      "attribution": "#1224656 (CK) / #9258318 (bunbuku)"
    }
  ],
  [
    "unlike",
    "B1",
    "前置詞",
    [
      "らしくない",
      "に似ていない"
    ],
    "/ənˈlaɪk/",
    "It is unlike him to be late.",
    "遅刻するなんて彼らしくない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277412",
      "license": "CC BY 2.0 FR",
      "attribution": "#277412 (CK) / #126641 (tommy__san)"
    }
  ],
  [
    "unlikely",
    "B1",
    "形容詞",
    [
      "考えられない",
      "ありそうもない"
    ],
    "/ənˈlaɪkli/",
    "It is unlikely that such a cool headed person got upset.",
    "あんな冷静な人が取り乱したなんて考えられない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66877",
      "license": "CC BY 2.0 FR",
      "attribution": "#66877 (CM) / #229518 (small_snow)"
    }
  ],
  [
    "unnecessary",
    "B1",
    "形容詞",
    [
      "必要のない"
    ],
    "/ənˈnɛsəsɛri/",
    "We made it cheaper by eliminating unnecessary functions.",
    "ムダな機能を省いて安くしました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12455153",
      "license": "CC BY 2.0 FR",
      "attribution": "#12455153 (CK) / #10899765 (bunbuku)"
    }
  ],
  [
    "unpleasant",
    "B1",
    "形容詞",
    [
      "いやな"
    ],
    "/ənpˈlɛzənt/",
    "This fruit has an unpleasant smell.",
    "この果物はいやなにおいがする。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1192402",
      "license": "CC BY 2.0 FR",
      "attribution": "#1192402 (CK) / #222794 (mookeee)"
    }
  ],
  [
    "unusual",
    "A2",
    "形容詞",
    [
      "珍しい",
      "普通でない"
    ],
    "/ənˈjuʒuəl/",
    "Nowadays it is not unusual for a woman to travel alone.",
    "最近では、女性が一人旅をするのは珍しいことではない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/243769",
      "license": "CC BY 2.0 FR",
      "attribution": "#243769 (CK) / #170712 (bunbuku)"
    }
  ],
  [
    "update",
    "B1",
    "名詞・動詞",
    [
      "を最新のものにする"
    ],
    "/əpˈdeɪt/",
    "How can I update this software?",
    "このソフト、どうやったらアップデートできるの？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4187426",
      "license": "CC BY 2.0 FR",
      "attribution": "#4187426 (Eldad) / #8945972 (bunbuku)"
    }
  ],
  [
    "upon",
    "B1",
    "前置詞",
    [
      "〜するとすぐ",
      "〜の上に"
    ],
    "/əˈpɑn/",
    "Upon arrival, please report to the reception desk.",
    "到着したら受付に申し出てください。",
    null
  ],
  [
    "upper",
    "B2",
    "形容詞",
    [
      "上級の",
      "上流の"
    ],
    "/ˈʌpɚ/",
    "He belongs to the upper class.",
    "彼は上流階級の人だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/299707",
      "license": "CC BY 2.0 FR",
      "attribution": "#299707 (CK) / #103984 (bunbuku)"
    }
  ],
  [
    "upset",
    "B1",
    "形容詞・動詞",
    [
      "混乱した",
      "ろうばいした"
    ],
    "/əpˈsɛt/",
    "It is unlikely that such a cool headed person got upset.",
    "あんな冷静な人が取り乱したなんて考えられない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66877",
      "license": "CC BY 2.0 FR",
      "attribution": "#66877 (CM) / #229518 (small_snow)"
    }
  ],
  [
    "upstairs",
    "A2",
    "形容詞",
    [
      "2階"
    ],
    "/əpsˈtɛrz/",
    "It seems that the burglar broke in through an upstairs window.",
    "泥棒は２階から侵入したらしい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/278626",
      "license": "CC BY 2.0 FR",
      "attribution": "#278626 (CK) / #125366 (small_snow)"
    }
  ],
  [
    "upwards",
    "B2",
    "副詞",
    [
      "上向きに"
    ],
    "/ˈʌpwɚdz/",
    "Prices continued to move upwards throughout the year.",
    "価格は年を通して上昇し続けた。",
    null
  ],
  [
    "urban",
    "B2",
    "形容詞",
    [
      "都市の"
    ],
    "/ˈɝbən/",
    "I've finally gotten used to urban life.",
    "私はやっと都会の生活に慣れてきた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9635059",
      "license": "CC BY 2.0 FR",
      "attribution": "#9635059 (CK) / #158693 (mookeee)"
    }
  ],
  [
    "urge",
    "B2",
    "動詞",
    [
      "を力説する",
      "強く主張する"
    ],
    "/ɝdʒ/",
    "She always urges him to try new things.",
    "彼女はいつも新しいことに挑戦するよう、彼に勧めている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1343842",
      "license": "CC BY 2.0 FR",
      "attribution": "#1343842 (Chrikaru) / #2144971 (bunbuku)"
    }
  ],
  [
    "urgent",
    "B2",
    "形容詞",
    [
      "緊急の"
    ],
    "/ˈɝdʒənt/",
    "If there's anything urgent, you can get in touch with me.",
    "緊急の時は私に連絡すればいいからね。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/30900",
      "license": "CC BY 2.0 FR",
      "attribution": "#30900 (darinmex) / #10346540 (bunbuku)"
    }
  ],
  [
    "usage",
    "B2",
    "名詞",
    [
      "語法"
    ],
    "/ˈjusədʒ/",
    "As an Englishman, he is particularly sensitive to the differences between English and American usage.",
    "英国人なので、彼はとりわけイギリス語法とアメリカ語法の違いに敏感である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/26139",
      "license": "CC BY 2.0 FR",
      "attribution": "#26139 (CK) / #188992 (mookeee)"
    }
  ],
  [
    "use",
    "A2",
    "名詞",
    [
      "を使う",
      "役に立つこと"
    ],
    "/jus/",
    "Man is the only animal that can make use of fire.",
    "人間は火を使うことのできる唯一の動物である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/270259",
      "license": "CC BY 2.0 FR",
      "attribution": "#270259 (CM) / #144306 (bunbuku)"
    }
  ],
  [
    "used",
    "B1",
    "形容詞",
    [
      "慣れている",
      "以前は…した"
    ],
    "/juzd/",
    "This city is not so busy as it used to be.",
    "この町は以前ほどにぎわっていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57833",
      "license": "CC BY 2.0 FR",
      "attribution": "#57833 (CM) / #220511 (KK_kaku_)"
    }
  ],
  [
    "used to",
    "A2",
    "動詞",
    [
      "以前は〜したものだ"
    ],
    "/juzd tu/",
    "This city is not so busy as it used to be.",
    "この町は以前ほどにぎわっていない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57833",
      "license": "CC BY 2.0 FR",
      "attribution": "#57833 (CM) / #220511 (KK_kaku_)"
    }
  ],
  [
    "useless",
    "B2",
    "形容詞",
    [
      "使いものにならない",
      "役に立たない"
    ],
    "/ˈjusləs/",
    "I can't work at all with all these useless calls coming in.",
    "どうでもいい電話ばっかりかかってきて、仕事にならない！",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/38450",
      "license": "CC BY 2.0 FR",
      "attribution": "#38450 (CK) / #201243 (KK_kaku_)"
    }
  ],
  [
    "user",
    "A2",
    "名詞",
    [
      "使用者"
    ],
    "/ˈjuzɚ/",
    "If you have any problems, please refer to the user manual.",
    "お困りの点がありましたら、利用者マニュアルをご参照ください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13571718",
      "license": "CC BY 2.0 FR",
      "attribution": "#13571718 (CK) / #9742450 (bunbuku)"
    }
  ],
  [
    "usual",
    "A2",
    "形容詞",
    [
      "いつもの"
    ],
    "/ˈjuʒəwəl/",
    "I don't have to get up as early as usual tomorrow.",
    "明日は、いつもみたいに早起きしなくていいの。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/6656787",
      "license": "CC BY 2.0 FR",
      "attribution": "#6656787 (CK) / #11516169 (small_snow)"
    }
  ],
  [
    "valid",
    "B2",
    "形容詞",
    [
      "しっかりした根拠のある",
      "有効な"
    ],
    "/ˈvælɪd/",
    "This ticket is valid for only two days after its purchase.",
    "この切符は購入後２日のみ有効である。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/674304",
      "license": "CC BY 2.0 FR",
      "attribution": "#674304 (yessoos) / #220855 (small_snow)"
    }
  ],
  [
    "valley",
    "A2",
    "名詞",
    [
      "谷"
    ],
    "/ˈvæli/",
    "If it snows on the mountain, it's cold in the valley.",
    "山に雪が降ると谷は寒くなります。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10153737",
      "license": "CC BY 2.0 FR",
      "attribution": "#10153737 (CK) / #3083289 (fouafouadougou)"
    }
  ],
  [
    "valuable",
    "B1",
    "形容詞",
    [
      "貴重な",
      "貴重品"
    ],
    "/ˈvæljəbəl/",
    "This old French table is a very valuable piece of furniture.",
    "この古いフランスのテーブルはとても貴重な家具です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/59383",
      "license": "CC BY 2.0 FR",
      "attribution": "#59383 (CM) / #222058 (mookeee)"
    }
  ],
  [
    "value",
    "B1",
    "名詞・動詞",
    [
      "価値",
      "値"
    ],
    "/ˈvælju/",
    "The value of the coins depended on the weight of the metal used.",
    "硬貨の価値は使われた金属の重さによって決まった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/240958",
      "license": "CC BY 2.0 FR",
      "attribution": "#240958 (CM) / #173512 (mookeee)"
    }
  ],
  [
    "van",
    "A2",
    "名詞",
    [
      "バン",
      "小型配送車"
    ],
    "/væn/",
    "They loaded the equipment into a delivery van.",
    "彼らは機材を配送用バンに積み込んだ。",
    null
  ],
  [
    "variation",
    "B2",
    "名詞",
    [
      "ばらつき",
      "変化"
    ],
    "/vɛriˈeɪʃən/",
    "There is considerable variation in regional prices.",
    "地域の価格にはかなりのばらつきがある。",
    null
  ],
  [
    "variety",
    "A2",
    "名詞",
    [
      "いろいろ"
    ],
    "/vɚˈaɪəti/",
    "You can get to her house in a variety of different ways.",
    "彼女の家にはいろいろ違った方法で行ける。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309093",
      "license": "CC BY 2.0 FR",
      "attribution": "#309093 (CM) / #94613 (bunbuku)"
    }
  ],
  [
    "various",
    "B1",
    "形容詞",
    [
      "いろいろな"
    ],
    "/ˈvɛriəs/",
    "Various kinds of flowers will be blooming soon.",
    "いろんな花がもうすぐ咲きますよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/12375617",
      "license": "CC BY 2.0 FR",
      "attribution": "#12375617 (CK) / #11685245 (bunbuku)"
    }
  ],
  [
    "vary",
    "B2",
    "動詞",
    [
      "変わる",
      "に変化をつける"
    ],
    "/ˈvɛri/",
    "The price of gold varies from day to day.",
    "金の値段は日ごとに変わる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18604",
      "license": "CC BY 2.0 FR",
      "attribution": "#18604 (piksea) / #179745 (bunbuku)"
    }
  ],
  [
    "vast",
    "B2",
    "形容詞",
    [
      "大多数の",
      "広大な"
    ],
    "/væst/",
    "The vast majority of children love ice cream.",
    "大多数の子供はアイスが大好きだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1747571",
      "license": "CC BY 2.0 FR",
      "attribution": "#1747571 (belgavox) / #1747576 (mookeee)"
    }
  ],
  [
    "vehicle",
    "A2",
    "名詞",
    [
      "車"
    ],
    "/ˈvihɪkəl/",
    "There are always a lot of vehicles on this road.",
    "この道はいつも多くの車が通る。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/57630",
      "license": "CC BY 2.0 FR",
      "attribution": "#57630 (CM) / #220310 (tommy__san)"
    }
  ],
  [
    "venue",
    "B2",
    "名詞",
    [
      "会場"
    ],
    "/ˈvɛnju/",
    "The organizers changed the venue at short notice.",
    "主催者は直前に会場を変更した。",
    null
  ],
  [
    "version",
    "B1",
    "名詞",
    [
      "版"
    ],
    "/ˈvɝʒən/",
    "I've heard the French version of this song.",
    "この歌のフランス語版を聴いたことがある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1318696",
      "license": "CC BY 2.0 FR",
      "attribution": "#1318696 (CK) / #993691 (mookeee)"
    }
  ],
  [
    "vertical",
    "B2",
    "形容詞",
    [
      "垂直線",
      "垂直の"
    ],
    "/ˈvɝtɪkəl/",
    "Strictly speaking, it was not a vertical line.",
    "厳密に言えば、それは垂直線ではなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/239504",
      "license": "CC BY 2.0 FR",
      "attribution": "#239504 (Zifre) / #174963 (tommy__san)"
    }
  ],
  [
    "very",
    "B2",
    "形容詞",
    [
      "まったく",
      "まったくの"
    ],
    "/ˈvɛri/",
    "She came very near to being run over by a car.",
    "彼女は危うく自動車にひかれるところだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/388644",
      "license": "CC BY 2.0 FR",
      "attribution": "#388644 (CK) / #90624 (bunbuku)"
    }
  ],
  [
    "via",
    "B2",
    "前置詞",
    [
      "経由で"
    ],
    "/ˈvaɪə/",
    "She traveled from Boston to San Francisco via Chicago.",
    "彼女はボストンからシカゴ経由でサンフランシスコへ旅行した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/312173",
      "license": "CC BY 2.0 FR",
      "attribution": "#312173 (CK) / #91540 (bunbuku)"
    }
  ],
  [
    "victim",
    "B1",
    "名詞",
    [
      "犠牲者"
    ],
    "/ˈvɪktəm/",
    "They called on us to do something to help the victims.",
    "彼らは被災者に何か援助するよう私達に求めた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/307464",
      "license": "CC BY 2.0 FR",
      "attribution": "#307464 (CK) / #96241 (bunbuku)"
    }
  ],
  [
    "victory",
    "B2",
    "名詞",
    [
      "勝利"
    ],
    "/ˈvɪktɚi/",
    "On hearing of the victory, the whole nation shouted for joy.",
    "勝利の知らせに国中が喜びに沸いた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/267393",
      "license": "CC BY 2.0 FR",
      "attribution": "#267393 (CM) / #147168 (tommy__san)"
    }
  ],
  [
    "view",
    "A2",
    "名詞・動詞",
    [
      "景色",
      "見方"
    ],
    "/vju/",
    "Let's sit here for a while and look at the view.",
    "ちょっとここに座って景色を眺めようよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61817",
      "license": "CC BY 2.0 FR",
      "attribution": "#61817 (CK) / #10899713 (bunbuku)"
    }
  ],
  [
    "viewer",
    "B1",
    "名詞",
    [
      "テレビを視聴者"
    ],
    "/vˈjuɚ/",
    "Each viewer can choose subtitles or audio description.",
    "視聴者は字幕か音声解説を選べる。",
    null
  ],
  [
    "viewpoint",
    "B2",
    "名詞",
    [
      "観点"
    ],
    "/vˈjupɔɪnt/",
    "The article presents the issue from a local viewpoint.",
    "その記事は問題を地域の観点から示している。",
    null
  ],
  [
    "violence",
    "B2",
    "名詞",
    [
      "暴力"
    ],
    "/ˈvaɪələns/",
    "I hope they don't resort to violence to accomplish their goals.",
    "彼らが目的達成のために暴力に訴えなければいいのですが。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/305034",
      "license": "CC BY 2.0 FR",
      "attribution": "#305034 (CK) / #98666 (mookeee)"
    }
  ],
  [
    "violent",
    "B1",
    "形容詞",
    [
      "激しい"
    ],
    "/ˈvaɪələnt/",
    "There was a violent clash of opinions between the two leaders.",
    "２人の指導者の間には激しい意見の衝突があった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72832",
      "license": "CC BY 2.0 FR",
      "attribution": "#72832 (CM) / #235454 (arnab)"
    }
  ],
  [
    "virtual",
    "B2",
    "形容詞",
    [
      "オンラインの",
      "仮想の"
    ],
    "/ˈvɝtʃuəl/",
    "The team held a virtual meeting online.",
    "チームはオンラインで仮想会議を開いた。",
    null
  ],
  [
    "virus",
    "A2",
    "名詞",
    [
      "ビールス"
    ],
    "/ˈvaɪrəs/",
    "It seems that the computer was infected by a virus.",
    "パソコンがウイルスに感染したようです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2592621",
      "license": "CC BY 2.0 FR",
      "attribution": "#2592621 (WestofEden) / #2515523 (tommy_san)"
    }
  ],
  [
    "visa",
    "B2",
    "名詞",
    [
      "ビザ"
    ],
    "/ˈvizə/",
    "It'll be impossible to get a visa on short notice.",
    "急にビザを取るのは無理だよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/935703",
      "license": "CC BY 2.0 FR",
      "attribution": "#935703 (CK) / #9957965 (bunbuku)"
    }
  ],
  [
    "visible",
    "B2",
    "形容詞",
    [
      "目に見える"
    ],
    "/ˈvɪzəbəl/",
    "Some stars are hardly visible to the naked eye.",
    "肉眼ではほとんど見えない星もある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/281024",
      "license": "CC BY 2.0 FR",
      "attribution": "#281024 (CM) / #122978 (KK_kaku_)"
    }
  ],
  [
    "vision",
    "B2",
    "名詞",
    [
      "将来像",
      "視力"
    ],
    "/ˈvɪʒən/",
    "Do you have a vision of your future?",
    "あなたは自分の将来のビジョンを持っていますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/69262",
      "license": "CC BY 2.0 FR",
      "attribution": "#69262 (CM) / #231896 (bunbuku)"
    }
  ],
  [
    "visual",
    "B2",
    "形容詞",
    [
      "視覚の"
    ],
    "/ˈvɪʒəwəl/",
    "A visual diagram makes the process easier to understand.",
    "視覚的な図で手順が理解しやすくなる。",
    null
  ],
  [
    "vital",
    "B2",
    "形容詞",
    [
      "生命維持に必要な器官"
    ],
    "/ˈvaɪtəl/",
    "Your help is vital to the success of our plan.",
    "我々の計画の成功には、君の援助がどうしても必要だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/23026",
      "license": "CC BY 2.0 FR",
      "attribution": "#23026 (spockofvulcan) / #185894 (KK_kaku_)"
    }
  ],
  [
    "vitamin",
    "B2",
    "名詞",
    [
      "ビタミン"
    ],
    "/ˈvaɪtəmən/",
    "Chicken eggs are richer in vitamin A than quail eggs.",
    "鶏卵は、うずら卵よりビタミンAが豊富です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9241117",
      "license": "CC BY 2.0 FR",
      "attribution": "#9241117 (DJ_Saidez) / #11031134 (small_snow)"
    }
  ],
  [
    "voice",
    "A2",
    "名詞",
    [
      "声",
      "声を出す力"
    ],
    "/vɔɪs/",
    "God gave her a beautiful face and a sweet voice.",
    "神は彼女に美しい顔と、声を与えた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269663",
      "license": "CC BY 2.0 FR",
      "attribution": "#269663 (CM) / #144901 (bunbuku)"
    }
  ],
  [
    "volume",
    "B2",
    "名詞",
    [
      "音量",
      "容量"
    ],
    "/ˈvɑljum/",
    "Please turn down the volume a little bit more.",
    "もう少し小さくして。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/31262",
      "license": "CC BY 2.0 FR",
      "attribution": "#31262 (CK) / #194093 (small_snow)"
    }
  ],
  [
    "voluntary",
    "B2",
    "形容詞",
    [
      "篤志によってできた",
      "任意寄付で維持される"
    ],
    "/ˈvɑləntɛri/",
    "This organization relies entirely on voluntary donations.",
    "この組織は百パーセント寄付に頼っている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/58042",
      "license": "CC BY 2.0 FR",
      "attribution": "#58042 (CM) / #220720 (tommy__san)"
    }
  ],
  [
    "volunteer",
    "B1",
    "名詞・動詞",
    [
      "協力者",
      "志願者"
    ],
    "/vɑlənˈtɪr/",
    "The magician asked for a volunteer from the audience.",
    "そのマジシャンは観客の中から協力者を募った。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/517831",
      "license": "CC BY 2.0 FR",
      "attribution": "#517831 (darinmex) / #1080870 (thyc244)"
    }
  ],
  [
    "vote",
    "B1",
    "名詞・動詞",
    [
      "投票する",
      "投票"
    ],
    "/voʊt/",
    "What criteria do you use in deciding who to vote for?",
    "どんな基準で誰に投票するか決めていますか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/997088",
      "license": "CC BY 2.0 FR",
      "attribution": "#997088 (CK) / #1598454 (bunbuku)"
    }
  ],
  [
    "voting",
    "B2",
    "名詞",
    [
      "投票"
    ],
    "/ˈvoʊtɪŋ/",
    "I still haven't decided who I'm voting for.",
    "誰に投票するか、まだ決めてないんだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11939954",
      "license": "CC BY 2.0 FR",
      "attribution": "#11939954 (sundown) / #11944129 (small_snow)"
    }
  ],
  [
    "wage",
    "B2",
    "名詞",
    [
      "賃金"
    ],
    "/weɪdʒ/",
    "The union bosses are fighting the freeze on wage hikes.",
    "労働組合の幹部は賃上げの凍結に反対して、闘っています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326367",
      "license": "CC BY 2.0 FR",
      "attribution": "#326367 (CM) / #77352 (arnab)"
    }
  ],
  [
    "wait",
    "A2",
    "名詞",
    [
      "待つ",
      "を待ち受ける"
    ],
    "/weɪt/",
    "All we can do is wait for the police to arrive.",
    "警察の到着を待つしかない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/953089",
      "license": "CC BY 2.0 FR",
      "attribution": "#953089 (CK) / #997181 (mookeee)"
    }
  ],
  [
    "wander",
    "B2",
    "動詞",
    [
      "脱線する"
    ],
    "/ˈwɑndɚ/",
    "We can't wander around the park at night.",
    "私たちは夜中に公園を散策するなんてできません。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1955126",
      "license": "CC BY 2.0 FR",
      "attribution": "#1955126 (CK) / #2128080 (Blanka_Meduzo)"
    }
  ],
  [
    "war",
    "A2",
    "名詞",
    [
      "戦争",
      "戦争状態"
    ],
    "/wɔr/",
    "She had to part with her family when the war began.",
    "戦争が始まったとき、彼女は家族と別れなければならなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/273272",
      "license": "CC BY 2.0 FR",
      "attribution": "#273272 (CM) / #141299 (bunbuku)"
    }
  ],
  [
    "warm",
    "B1",
    "動詞",
    [
      "暖かく感じられる",
      "暖かくする"
    ],
    "/wɔrm/",
    "A mother rabbit keeps her babies warm with her own body.",
    "母ウサギは、赤ん坊たちを自分のからだで暖かくしている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320537",
      "license": "CC BY 2.0 FR",
      "attribution": "#320537 (CK) / #83179 (mookeee)"
    }
  ],
  [
    "warming",
    "B2",
    "名詞",
    [
      "温暖化",
      "暖めること"
    ],
    "/ˈwɔrmɪŋ/",
    "Global warming is changing weather patterns worldwide.",
    "地球温暖化は世界中の気象パターンを変えている。",
    null
  ],
  [
    "warn",
    "B1",
    "動詞",
    [
      "に警告する"
    ],
    "/wɔrn/",
    "Just to warn you in advance, today's blog is no fun.",
    "予め断りますが、今日のブログは面白くないよ～。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/328041",
      "license": "CC BY 2.0 FR",
      "attribution": "#328041 (CM) / #75677 (mookeee)"
    }
  ],
  [
    "warning",
    "B1",
    "名詞",
    [
      "警告",
      "警告となるもの"
    ],
    "/ˈwɔrnɪŋ/",
    "He would go fishing in spite of our warning.",
    "私たちの警告を無視して釣りに行くといってきかなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/247510",
      "license": "CC BY 2.0 FR",
      "attribution": "#247510 (CM) / #166992 (bunbuku)"
    }
  ],
  [
    "wash",
    "A2",
    "名詞",
    [
      "を洗う",
      "を洗い落とす"
    ],
    "/wɑʃ/",
    "She used to wash her hair before going to school.",
    "彼女は登校前によく髪を洗ったものだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/315946",
      "license": "CC BY 2.0 FR",
      "attribution": "#315946 (CK) / #87761 (bunbuku)"
    }
  ],
  [
    "washing",
    "A2",
    "名詞",
    [
      "洗うこと"
    ],
    "/ˈwɑʃɪŋ/",
    "Would you like me to help you with washing the dishes?",
    "お皿を洗うの、手伝いましょうか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/999634",
      "license": "CC BY 2.0 FR",
      "attribution": "#999634 (CK) / #1587324 (bunbuku)"
    }
  ],
  [
    "waste",
    "B1",
    "形容詞・名詞・動詞",
    [
      "不毛の:耕されていない",
      "使用されていない"
    ],
    "/weɪst/",
    "Trying to do such a thing is a waste of time.",
    "そんなことやっても時間の無駄にすぎない。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/41633",
      "license": "CC BY 2.0 FR",
      "attribution": "#41633 (CK) / #204391 (mookeee)"
    }
  ],
  [
    "water",
    "B1",
    "動詞",
    [
      "水",
      "海の水"
    ],
    "/ˈwɔtɚ/",
    "The water will come to a boil in 5 minutes or so.",
    "その水は５分かそのぐらいで沸騰します。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/45985",
      "license": "CC BY 2.0 FR",
      "attribution": "#45985 (CK) / #208726 (small_snow)"
    }
  ],
  [
    "wave",
    "A2",
    "名詞・動詞",
    [
      "波",
      "波のような動き"
    ],
    "/weɪv/",
    "Nothing was to be heard except the sound of the waves.",
    "波の音の他は何一つ聞こえなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/282344",
      "license": "CC BY 2.0 FR",
      "attribution": "#282344 (CM) / #121661 (bunbuku)"
    }
  ],
  [
    "way",
    "B2",
    "副詞",
    [
      "はるかに",
      "ずっと"
    ],
    "/weɪ/",
    "The second option is way more expensive than the first.",
    "2つ目の選択肢は1つ目よりはるかに高い。",
    null
  ],
  [
    "weak",
    "A2",
    "形容詞",
    [
      "劣っている",
      "衰えている"
    ],
    "/wik/",
    "They said he was still weak from a recent sickness.",
    "彼は病み上がりで弱っているそうだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/802678",
      "license": "CC BY 2.0 FR",
      "attribution": "#802678 (Source_VOA) / #869818 (thyc244)"
    }
  ],
  [
    "weakness",
    "B2",
    "名詞",
    [
      "欠点",
      "弱さ"
    ],
    "/ˈwiknəs/",
    "Her weakness is that she talks too much.",
    "彼女の欠点はおしゃべりが過ぎるところだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/309215",
      "license": "CC BY 2.0 FR",
      "attribution": "#309215 (CM) / #1644170 (mookeee)"
    }
  ],
  [
    "wealth",
    "B2",
    "名詞",
    [
      "収入源",
      "富"
    ],
    "/wɛlθ/",
    "Mining is one of the main sources of wealth in Chile.",
    "鉱業はチリの主要な収入源の一つである。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1126773",
      "license": "CC BY 2.0 FR",
      "attribution": "#1126773 (CK) / #2955388 (tommy_san)"
    }
  ],
  [
    "wealthy",
    "B2",
    "形容詞",
    [
      "富裕な"
    ],
    "/ˈwɛlθi/",
    "Many people buy lottery tickets with the dream of immediately becoming wealthy.",
    "多くの人が一攫千金を夢見て宝くじを買う。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1212340",
      "license": "CC BY 2.0 FR",
      "attribution": "#1212340 (CK) / #138352 (bunbuku)"
    }
  ],
  [
    "weapon",
    "B1",
    "名詞",
    [
      "武器"
    ],
    "/ˈwɛpən/",
    "The fingerprints left on the weapon match the suspect's.",
    "凶器に残された指紋は容疑者のものと一致する。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/902931",
      "license": "CC BY 2.0 FR",
      "attribution": "#902931 (CK) / #180581 (bunbuku)"
    }
  ],
  [
    "web",
    "A2",
    "名詞",
    [
      "ウェブ",
      "網"
    ],
    "/wɛb/",
    "I work as a web consultant on the side.",
    "副業で、Webコンサルタントの仕事をしています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11697553",
      "license": "CC BY 2.0 FR",
      "attribution": "#11697553 (pip) / #11291000 (small_snow)"
    }
  ],
  [
    "wedding",
    "A2",
    "名詞",
    [
      "結婚式"
    ],
    "/ˈwɛdɪŋ/",
    "The wedding will be held in a 17th century church.",
    "その結婚式は17世紀建立の教会で執り行われます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/562442",
      "license": "CC BY 2.0 FR",
      "attribution": "#562442 (darinmex) / #876594 (thyc244)"
    }
  ],
  [
    "weekly",
    "B2",
    "形容詞",
    [
      "週刊雑誌"
    ],
    "/ˈwikli/",
    "He sat reading a weekly magazine.",
    "彼は座って週刊誌を読んでいた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/296689",
      "license": "CC BY 2.0 FR",
      "attribution": "#296689 (CM) / #106997 (bunbuku)"
    }
  ],
  [
    "weigh",
    "B1",
    "動詞",
    [
      "の重さを計る",
      "重さがある"
    ],
    "/weɪ/",
    "The white ball weighs as much as the red ball.",
    "赤いボールは白いボールと同じ重さです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/680261",
      "license": "CC BY 2.0 FR",
      "attribution": "#680261 (Source_VOA) / #880317 (thyc244)"
    }
  ],
  [
    "weight",
    "A2",
    "名詞",
    [
      "体重"
    ],
    "/weɪt/",
    "The ice is so thin that it won't bear your weight.",
    "氷は非常に薄いので君の体重を支えきれないだろう。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/318332",
      "license": "CC BY 2.0 FR",
      "attribution": "#318332 (CK) / #85381 (huizi99)"
    }
  ],
  [
    "weird",
    "B2",
    "形容詞",
    [
      "おかしな",
      "奇妙な"
    ],
    "/wɪrd/",
    "Is that why you've been acting so weird lately?",
    "だから最近の言動がおかしかったの？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7850320",
      "license": "CC BY 2.0 FR",
      "attribution": "#7850320 (Hybrid) / #8822371 (bunbuku)"
    }
  ],
  [
    "welcome",
    "A2",
    "名詞",
    [
      "歓迎",
      "を歓迎する"
    ],
    "/ˈwɛlkəm/",
    "Whoever wants to join our club will be welcome.",
    "私たちのクラブに入会したい人はだれでも歓迎します。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/247382",
      "license": "CC BY 2.0 FR",
      "attribution": "#247382 (CK) / #167120 (mookeee)"
    }
  ],
  [
    "welfare",
    "B2",
    "名詞",
    [
      "福祉"
    ],
    "/ˈwɛlfɛr/",
    "The policy aims to protect children's welfare.",
    "その政策は子どもの福祉を守ることを目指す。",
    null
  ],
  [
    "western",
    "B1",
    "形容詞",
    [
      "西部の",
      "米国西部の"
    ],
    "/ˈwɛstɚn/",
    "He lives in the western part of town.",
    "彼は町の西部に住んでいる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/301605",
      "license": "CC BY 2.0 FR",
      "attribution": "#301605 (CK) / #102089 (tommy__san)"
    }
  ],
  [
    "wet",
    "A2",
    "形容詞",
    [
      "ぬれた"
    ],
    "/wɛt/",
    "The cat likes fish, but doesn't like getting its paws wet.",
    "その猫は魚が好きなんだけど、足が濡れるのが嫌なのよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10091751",
      "license": "CC BY 2.0 FR",
      "attribution": "#10091751 (CK) / #10091796 (small_snow)"
    }
  ],
  [
    "whatever",
    "B1",
    "限定詞・名詞",
    [
      "どんなことでも"
    ],
    "/wʌˈtɛvɚ/",
    "I copied in my notebook whatever he wrote on the blackboard.",
    "彼が黒板に書くことはすべてノートに写した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/283641",
      "license": "CC BY 2.0 FR",
      "attribution": "#283641 (CK) / #120368 (bunbuku)"
    }
  ],
  [
    "wheat",
    "B2",
    "名詞",
    [
      "小麦"
    ],
    "/wit/",
    "Can you tell barley from wheat?",
    "大麦と小麦って見分けれる？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7352547",
      "license": "CC BY 2.0 FR",
      "attribution": "#7352547 (AlanF_US) / #9171199 (small_snow)"
    }
  ],
  [
    "wheel",
    "A2",
    "名詞",
    [
      "車"
    ],
    "/wil/",
    "You could see the entire city from the top of the Ferris wheel.",
    "観覧車の一番上から街全体が見渡せます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9935070",
      "license": "CC BY 2.0 FR",
      "attribution": "#9935070 (DJ_Saidez) / #9961058 (small_snow)"
    }
  ],
  [
    "whenever",
    "B1",
    "接続詞",
    [
      "するときはいつでも"
    ],
    "/wɛˈnɛvɚ/",
    "She has the habit of clearing her throat whenever she's nervous.",
    "彼女は自信のないときに咳払いをする癖がある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/729928",
      "license": "CC BY 2.0 FR",
      "attribution": "#729928 (darinmex) / #1795104 (Akatsuki)"
    }
  ],
  [
    "whereas",
    "B2",
    "接続詞",
    [
      "であるのに反して"
    ],
    "/wɛˈræz/",
    "This room is bright, whereas the other is rather dark.",
    "この部屋は明るいが、もう一方はかなり暗い。",
    null
  ],
  [
    "wherever",
    "B2",
    "接続詞",
    [
      "いったいどこへ",
      "する所はどこでも"
    ],
    "/wɛˈrɛvɚ/",
    "Wherever he may go, he is sure to make friends.",
    "どこへ行っても、彼は必ず友達を作る。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/38085",
      "license": "CC BY 2.0 FR",
      "attribution": "#38085 (CM) / #200881 (Blanka_Meduzo)"
    }
  ],
  [
    "whether",
    "B1",
    "接続詞",
    [
      "かどうか",
      "であろうと…であろうと"
    ],
    "/ˈwɛðɚ/",
    "It makes no difference to me whether he comes or not.",
    "彼が来ても来なくても、私にとってはどうでもいいことです。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/282982",
      "license": "CC BY 2.0 FR",
      "attribution": "#282982 (CK) / #1144733 (bunbuku)"
    }
  ],
  [
    "while",
    "A2",
    "接続詞・名詞",
    [
      "しばらく",
      "〜する間"
    ],
    "/waɪl/",
    "Let's sit here for a while and look at the view.",
    "ちょっとここに座って景色を眺めようよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/61817",
      "license": "CC BY 2.0 FR",
      "attribution": "#61817 (CK) / #10899713 (bunbuku)"
    }
  ],
  [
    "whisper",
    "B2",
    "名詞・動詞",
    [
      "ささやく",
      "をささやく"
    ],
    "/ˈwɪspɚ/",
    "She whispered to me that she was hungry.",
    "彼女は私に、お腹がすいているとささやいた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/314121",
      "license": "CC BY 2.0 FR",
      "attribution": "#314121 (CK) / #89594 (mookeee)"
    }
  ],
  [
    "whoever",
    "B2",
    "名詞",
    [
      "いったいだれが"
    ],
    "/huˈɛvɚ/",
    "I'd like to speak with whoever is in charge here.",
    "こちらの責任者の方とお話ししたいのですが。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2033859",
      "license": "CC BY 2.0 FR",
      "attribution": "#2033859 (CK) / #8630603 (bunbuku)"
    }
  ],
  [
    "whole",
    "A2",
    "形容詞・名詞",
    [
      "全…"
    ],
    "/hoʊl/",
    "My whole body was one big bruise after the rugby game.",
    "ラグビーの試合後、私の体は全身あざだらけだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/29807",
      "license": "CC BY 2.0 FR",
      "attribution": "#29807 (CK) / #1869159 (bunbuku)"
    }
  ],
  [
    "whom",
    "B2",
    "名詞",
    [
      "だれを"
    ],
    "/hum/",
    "The person whom you contacted is on leave.",
    "あなたが連絡した人は休暇中だ。",
    null
  ],
  [
    "whose",
    "A2",
    "限定詞・名詞",
    [
      "だれの"
    ],
    "/huz/",
    "This book is for students whose native language is not Japanese.",
    "この本は日本語以外の言葉を母語とする学生用です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/56868",
      "license": "CC BY 2.0 FR",
      "attribution": "#56868 (CK) / #219547 (Blanka_Meduzo)"
    }
  ],
  [
    "wide",
    "A2",
    "形容詞",
    [
      "幅の広い"
    ],
    "/waɪd/",
    "Keep your eyes wide open before marriage and half shut afterwards.",
    "結婚前は両目を見開き、結婚したら片目をつぶれ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/5168744",
      "license": "CC BY 2.0 FR",
      "attribution": "#5168744 (CK) / #3468911 (arnab)"
    }
  ],
  [
    "widely",
    "B2",
    "副詞",
    [
      "広く"
    ],
    "/ˈwaɪdli/",
    "Tea is widely grown in India.",
    "茶はインドで広く栽培されている。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/277425",
      "license": "CC BY 2.0 FR",
      "attribution": "#277425 (CM) / #126623 (tommy__san)"
    }
  ],
  [
    "widespread",
    "B2",
    "形容詞",
    [
      "広範囲にわたる"
    ],
    "/ˈwaɪdspˈrɛd/",
    "The earthquake caused widespread damage.",
    "その地震で広範囲に及ぶ被害がでた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/45135",
      "license": "CC BY 2.0 FR",
      "attribution": "#45135 (CK) / #207879 (KK_kaku_)"
    }
  ],
  [
    "wild",
    "A2",
    "形容詞",
    [
      "野生の"
    ],
    "/waɪld/",
    "In Tokyo, wild birds are decreasing in number year by year.",
    "東京では野鳥の数が年々減りつつある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/279723",
      "license": "CC BY 2.0 FR",
      "attribution": "#279723 (CM) / #124271 (tommy__san)"
    }
  ],
  [
    "wildlife",
    "B2",
    "名詞",
    [
      "野生生物"
    ],
    "/ˈwaɪldlaɪf/",
    "The law protects wildlife from illegal hunting.",
    "その法律は野生生物を違法な狩猟から守る。",
    null
  ],
  [
    "will",
    "B1",
    "名詞",
    [
      "するつもりです"
    ],
    "/wɪl/",
    "Any time will do so long as it is after six.",
    "６時以降ならいつでも結構です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72415",
      "license": "CC BY 2.0 FR",
      "attribution": "#72415 (CK) / #235038 (e4zh1nmcz)"
    }
  ],
  [
    "willing",
    "B2",
    "形容詞",
    [
      "乗り気の"
    ],
    "/ˈwɪlɪŋ/",
    "One who is not willing to learn is not worth teaching.",
    "学ぶ気のない者には教えるだけ無駄だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269845",
      "license": "CC BY 2.0 FR",
      "attribution": "#269845 (CM) / #1853534 (bunbuku)"
    }
  ],
  [
    "win",
    "B1",
    "名詞",
    [
      "勝つ"
    ],
    "/wɪn/",
    "Little did she dream that she could win first prize.",
    "１等をとれるなんて彼女は夢にも思わなかった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73093",
      "license": "CC BY 2.0 FR",
      "attribution": "#73093 (CM) / #235714 (mookeee)"
    }
  ],
  [
    "wind",
    "A2",
    "名詞・動詞",
    [
      "風"
    ],
    "/waɪnd/",
    "My hair is a mess because the wind is very strong.",
    "風が強すぎて、髪の毛がぐしゃぐしゃになっちゃった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/889778",
      "license": "CC BY 2.0 FR",
      "attribution": "#889778 (Zifre) / #889774 (bunbuku)"
    }
  ],
  [
    "wing",
    "B1",
    "名詞",
    [
      "羽"
    ],
    "/wɪŋ/",
    "An eagle's wings are more than one meter across.",
    "鷲の羽は広げると１メーターにもなる。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326592",
      "license": "CC BY 2.0 FR",
      "attribution": "#326592 (CM) / #77127 (mookeee)"
    }
  ],
  [
    "winner",
    "A2",
    "名詞",
    [
      "優勝者"
    ],
    "/ˈwɪnɚ/",
    "The winner received a new car from a local car dealer.",
    "優勝者には、地元のカーディーラーから新車が贈呈されました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10948821",
      "license": "CC BY 2.0 FR",
      "attribution": "#10948821 (CM) / #11021642 (small_snow)"
    }
  ],
  [
    "wire",
    "B2",
    "名詞",
    [
      "電線",
      "に電線を取り付ける"
    ],
    "/ˈwaɪɚ/",
    "If you touch that wire, you'll get a shock.",
    "あの電線に触れると感電するよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/67896",
      "license": "CC BY 2.0 FR",
      "attribution": "#67896 (CK) / #230529 (bunbuku)"
    }
  ],
  [
    "wisdom",
    "B2",
    "名詞",
    [
      "知恵",
      "親知らず"
    ],
    "/ˈwɪzdəm/",
    "One of my wisdom teeth is coming in.",
    "親知らずがはえてきました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1231035",
      "license": "CC BY 2.0 FR",
      "attribution": "#1231035 (CK) / #144779 (small_snow)"
    }
  ],
  [
    "wise",
    "B2",
    "形容詞",
    [
      "賢明な"
    ],
    "/waɪz/",
    "I don't think that it would be wise to do that.",
    "そうするのは賢明ではないと思うよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/7230826",
      "license": "CC BY 2.0 FR",
      "attribution": "#7230826 (CK) / #12629530 (bunbuku)"
    }
  ],
  [
    "wish",
    "A2",
    "名詞・動詞",
    [
      "であればよかったのにと思う",
      "であればよいのにと思う"
    ],
    "/wɪʃ/",
    "I wish he could have driven a car a year ago.",
    "１年前、彼に車の運転ができていたらよかったのに。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/73052",
      "license": "CC BY 2.0 FR",
      "attribution": "#73052 (CK) / #235672 (e4zh1nmcz)"
    }
  ],
  [
    "withdraw",
    "B2",
    "動詞",
    [
      "引き出す",
      "撤回する"
    ],
    "/wɪðdˈrɔ/",
    "I have to withdraw some cash from the bank.",
    "銀行でお金をおろさなくちゃ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/18453",
      "license": "CC BY 2.0 FR",
      "attribution": "#18453 (CK) / #179595 (bunbuku)"
    }
  ],
  [
    "within",
    "B1",
    "前置詞",
    [
      "以内に"
    ],
    "/wɪˈðɪn/",
    "The school is located within five minutes' walk of the station.",
    "学校は駅から歩いて５分とかからないところにある。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/21534",
      "license": "CC BY 2.0 FR",
      "attribution": "#21534 (CK) / #184406 (small_snow)"
    }
  ],
  [
    "witness",
    "B2",
    "名詞・動詞",
    [
      "目撃者",
      "を目撃する"
    ],
    "/ˈwɪtnəs/",
    "The witness identified the thief in the police lineup.",
    "目撃者は警察の面通しで窃盗犯を特定した。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/681184",
      "license": "CC BY 2.0 FR",
      "attribution": "#681184 (Source_VOA) / #1764079 (bunbuku)"
    }
  ],
  [
    "wonder",
    "B1",
    "名詞・動詞",
    [
      "と思う:…かしらと思う"
    ],
    "/ˈwʌndɚ/",
    "I wonder if he can live on such a small salary.",
    "彼はあんな安月給で暮らしていけるのかしら。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/288930",
      "license": "CC BY 2.0 FR",
      "attribution": "#288930 (CM) / #114741 (small_snow)"
    }
  ],
  [
    "wood",
    "A2",
    "名詞",
    [
      "木質部"
    ],
    "/wʊd/",
    "The majority of Japanese temples are made out of wood.",
    "日本の寺院の大半は木造だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/505982",
      "license": "CC BY 2.0 FR",
      "attribution": "#505982 (wma) / #1805106 (bunbuku)"
    }
  ],
  [
    "wooden",
    "A2",
    "形容詞",
    [
      "木製の"
    ],
    "/ˈwʊdən/",
    "Please use this wooden box in place of a chair.",
    "いすの代わりにこの木箱を使ってください。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/66482",
      "license": "CC BY 2.0 FR",
      "attribution": "#66482 (CK) / #229124 (bunbuku)"
    }
  ],
  [
    "wool",
    "B1",
    "名詞",
    [
      "羊毛の",
      "羊毛"
    ],
    "/wʊl/",
    "I learned how to spin wool from watching my grandmother.",
    "おばあちゃんのやり方を見ながら、羊毛の紡ぎ方を覚えました。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/253242",
      "license": "CC BY 2.0 FR",
      "attribution": "#253242 (CM) / #1142247 (bunbuku)"
    }
  ],
  [
    "workforce",
    "B2",
    "名詞",
    [
      "全労働力",
      "労働人口"
    ],
    "/ˈwɝkfɔrs/",
    "Women now make up half of the workforce.",
    "現在、女性が労働力の半分を占める。",
    null
  ],
  [
    "working",
    "A2",
    "形容詞",
    [
      "働くこと",
      "勤務している"
    ],
    "/ˈwɝkɪŋ/",
    "My older brother will start working at a bank next year.",
    "来年から兄は銀行に勤めます。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/10918365",
      "license": "CC BY 2.0 FR",
      "attribution": "#10918365 (CK) / #10918361 (small_snow)"
    }
  ],
  [
    "workplace",
    "B2",
    "名詞",
    [
      "職場"
    ],
    "/ˈwɝkpleɪs/",
    "Always keep your workplace organized.",
    "いつも仕事場をきちんと整理しておきなさい。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1293143",
      "license": "CC BY 2.0 FR",
      "attribution": "#1293143 (CM) / #228721 (bunbuku)"
    }
  ],
  [
    "workshop",
    "B2",
    "名詞",
    [
      "講座",
      "作業場"
    ],
    "/ˈwɝkʃɑp/",
    "The library held a writing workshop for teenagers.",
    "図書館は10代向けの作文講座を開いた。",
    null
  ],
  [
    "worldwide",
    "B1",
    "形容詞・副詞",
    [
      "全世界に知れ渡った",
      "世界的な"
    ],
    "/ˈwɝldˈwaɪd/",
    "The service is now available worldwide.",
    "そのサービスは今では世界中で利用できる。",
    null
  ],
  [
    "worm",
    "B2",
    "名詞",
    [
      "虫"
    ],
    "/wɝm/",
    "The early bird catches the worm.",
    "朝起きは三文の徳。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2348",
      "license": "CC BY 2.0 FR",
      "attribution": "#2348 (al_ex_an_der) / #126220 (bunbuku)"
    }
  ],
  [
    "worried",
    "A2",
    "形容詞",
    [
      "心配そうな"
    ],
    "/ˈwɝid/",
    "My sister hasn't come home yet, so my mother is worried.",
    "妹がまだ帰らないので、母は心配しています。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/11015470",
      "license": "CC BY 2.0 FR",
      "attribution": "#11015470 (CK) / #11007632 (small_snow)"
    }
  ],
  [
    "worry",
    "A2",
    "名詞・動詞",
    [
      "心配",
      "心配する"
    ],
    "/ˈwɝi/",
    "Don't worry, Mom. He isn't particular about food. He eats anything.",
    "心配しないでお母さん。彼は食べ物にはうるさくないから。何でも食べてくれるよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/63940",
      "license": "CC BY 2.0 FR",
      "attribution": "#63940 (CK) / #226596 (tommy_san)"
    }
  ],
  [
    "worse",
    "A2",
    "形容詞・副詞・名詞",
    [
      "さらに悪くなった",
      "もっと悪く"
    ],
    "/wɝs/",
    "You should go see a doctor if the symptoms get worse.",
    "症状が悪くなったら医者に診てもらった方がいいよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/13204739",
      "license": "CC BY 2.0 FR",
      "attribution": "#13204739 (Dozyjones) / #1143516 (bunbuku)"
    }
  ],
  [
    "worst",
    "A2",
    "形容詞・副詞・名詞",
    [
      "最悪の",
      "最悪の事態"
    ],
    "/wɝst/",
    "This is one of the worst movies that I've ever seen.",
    "これは自分が今まで見た中で最悪の映画だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9941641",
      "license": "CC BY 2.0 FR",
      "attribution": "#9941641 (CK) / #1750492 (bunbuku)"
    }
  ],
  [
    "worth",
    "B1",
    "形容詞・名詞",
    [
      "〜する価値がある"
    ],
    "/wɝθ/",
    "One who is not willing to learn is not worth teaching.",
    "学ぶ気のない者には教えるだけ無駄だ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/269845",
      "license": "CC BY 2.0 FR",
      "attribution": "#269845 (CM) / #1853534 (bunbuku)"
    }
  ],
  [
    "wound",
    "B2",
    "名詞・動詞",
    [
      "傷"
    ],
    "/waʊnd/",
    "It's not a deep wound. It's just a scratch.",
    "大した怪我じゃないよ。ただの擦り傷だよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9676656",
      "license": "CC BY 2.0 FR",
      "attribution": "#9676656 (DJ_Saidez) / #9839019 (small_snow)"
    }
  ],
  [
    "wow",
    "A2",
    "間投詞",
    [
      "まあ"
    ],
    "/waʊ/",
    "Wow, we're finally in Paris. Where should we visit first?",
    "あーやっとパリだね。最初にどこへ行こうか。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/72082",
      "license": "CC BY 2.0 FR",
      "attribution": "#72082 (CM) / #234705 (Sim5634)"
    }
  ],
  [
    "wrap",
    "B2",
    "動詞",
    [
      "を巻きつける"
    ],
    "/ræp/",
    "I need to wrap my older sister's dinner in plastic wrap.",
    "私はお姉ちゃんの夕飯をラップに包んでしまわないと。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/525827",
      "license": "CC BY 2.0 FR",
      "attribution": "#525827 (CK) / #75504 (mookeee)"
    }
  ],
  [
    "wrist",
    "B2",
    "名詞",
    [
      "手首関節"
    ],
    "/rɪst/",
    "I knew I'd broken my wrist the moment I fell.",
    "私は転んだ瞬間に手首を折ったことが分かった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/327636",
      "license": "CC BY 2.0 FR",
      "attribution": "#327636 (CK) / #76082 (mookeee)"
    }
  ],
  [
    "written",
    "B1",
    "形容詞",
    [
      "書かれた",
      "文書にした"
    ],
    "/ˈrɪtən/",
    "We tried to make out the letters written on the wall.",
    "壁に書かれた文字を判読しようとした。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/320258",
      "license": "CC BY 2.0 FR",
      "attribution": "#320258 (CM) / #83458 (bunbuku)"
    }
  ],
  [
    "wrong",
    "B1",
    "副詞・名詞",
    [
      "誤った"
    ],
    "/rɔŋ/",
    "He was wrong in thinking that she'd come to see him.",
    "彼女が会いにくるだろうと思ったのは彼の勘違いだった。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/1316993",
      "license": "CC BY 2.0 FR",
      "attribution": "#1316993 (CK) / #95490 (mookeee)"
    }
  ],
  [
    "yard",
    "B1",
    "名詞",
    [
      "庭"
    ],
    "/jɑrd/",
    "I tied my dog to the tree in the yard.",
    "犬は庭の木につないだよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/257252",
      "license": "CC BY 2.0 FR",
      "attribution": "#257252 (CK) / #10096595 (bunbuku)"
    }
  ],
  [
    "yet",
    "A2",
    "副詞・接続詞",
    [
      "まだ"
    ],
    "/jɛt/",
    "He has not come yet. Something may have happened to him.",
    "彼はまだ到着していません。彼の身に何か起きたのでしょうか？",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/283293",
      "license": "CC BY 2.0 FR",
      "attribution": "#283293 (CK) / #3069826 (nnaffu)"
    }
  ],
  [
    "young",
    "B1",
    "名詞",
    [
      "若い",
      "若い人たち"
    ],
    "/jʌŋ/",
    "She was robbed her of her bag by a young man.",
    "彼女は若い男にバッグを奪われた。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/265777",
      "license": "CC BY 2.0 FR",
      "attribution": "#265777 (CM) / #148782 (bunbuku)"
    }
  ],
  [
    "yours",
    "A2",
    "名詞",
    [
      "あなたのもの"
    ],
    "/jʊrz/",
    "You're a busy man, so I'll adjust my schedule to yours.",
    "お忙しいでしょうから、私がそちらにスケジュールを合わせますよ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/9042015",
      "license": "CC BY 2.0 FR",
      "attribution": "#9042015 (CK) / #10226949 (bunbuku)"
    }
  ],
  [
    "youth",
    "B1",
    "名詞",
    [
      "年の若いこと",
      "若い男"
    ],
    "/juθ/",
    "The old man often looks back on his youth.",
    "老人はしばしば若いころのことを回顧する。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/326433",
      "license": "CC BY 2.0 FR",
      "attribution": "#326433 (CM) / #77286 (arnab)"
    }
  ],
  [
    "zero",
    "A2",
    "数詞",
    [
      "零"
    ],
    "/ˈzɪroʊ/",
    "Last night, the temperature went down to ten degrees below zero.",
    "昨夜は-10℃まで冷え込んだ。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/2655081",
      "license": "CC BY 2.0 FR",
      "attribution": "#2655081 (CK) / #2655078 (tommy_san)"
    }
  ],
  [
    "zone",
    "B2",
    "名詞",
    [
      "領域",
      "地帯"
    ],
    "/zoʊn/",
    "You need to get out of your comfort zone.",
    "コンフォートゾーンから、抜け出すことが必要です。",
    {
      "name": "Tatoeba",
      "url": "https://tatoeba.org/en/sentences/show/4297220",
      "license": "CC BY 2.0 FR",
      "attribution": "#4297220 (Hybrid) / #12700744 (small_snow)"
    }
  ]
]

export const expandedVocabulary: VocabularyEntry[] = rows.map((row) => ({
  id: row[0],
  word: row[0],
  level: row[1],
  partOfSpeech: row[2],
  meaningsJa: row[3],
  pronunciation: row[4],
  exampleSentence: row[5],
  exampleTranslationJa: row[6],
  ...(row[7] ? { exampleSource: row[7] } : {}),
}))
