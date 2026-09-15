// レッスンごとの図の補足説明。画面では animations.ts の3段階の2Dアニメーションを表示する。
// kind / labels は従来の教材データとの互換性のために保持する。
// 補強コンテンツ(expansions)と同じく、ここで全レッスン分をまとめて持ち、合成時に差し込む。
// ラベルは図に描き込むので短く保つ(目安: 英語15字・日本語8字まで)。

import type { GrammarUnit, IllustrationKind, LessonBlock } from '../types'
import { LESSON_ANIMATIONS } from './animations.ts'

export type LessonIllustration = {
  kind: IllustrationKind
  labels: string[]
  /** 図の下に置く一文(日本語)。 */
  caption: string
}

export const lessonIllustrations: Record<string, LessonIllustration> = {
  // U01 文の基本
  'u01-l1': {
    kind: 'equals',
    labels: ['She', 'is', 'a nurse'],
    caption: '「She is a nurse.」は「She = a nurse」。be動詞は左右をイコールでつなぐ働きです。',
  },
  'u01-l2': {
    kind: 'repeat-cycle',
    labels: ['He walks to work.', 'いつものこと'],
    caption: '現在形は「いつもくり返していること」を表します。-s が付くのは he / she / it のときだけです。',
  },
  'u01-l3': {
    kind: 'helper-verb',
    labels: ['Does', 'play', 'plays'],
    caption: '疑問文・否定文では does が時制と三単現を引き受けるので、動詞は原形に戻ります。',
  },

  // U02 時制の基礎
  'u02-l1': {
    kind: 'clock-moment',
    labels: ['She is cooking.', '今この瞬間'],
    caption: '現在進行形は「今まさに進行中」であることを表します。be動詞と -ing はセットです。',
  },
  'u02-l2': {
    kind: 'two-cards',
    labels: ['I walk to work.', "I'm walking now."],
    caption: 'いつもの習慣なら現在形、今だけの動作なら現在進行形を選びます。',
  },
  'u02-l3': {
    kind: 'calendar-day',
    labels: ['I visited Kyoto.', 'last summer'],
    caption: '過去形は「終わった出来事」。いつのことかは last summer などの語句が示します。',
  },
  'u02-l4': {
    kind: 'clock-moment',
    labels: ['She was cooking.', '過去のその時点'],
    caption: '過去のある時点で進行中だった動作は was / were + -ing で表します。',
  },
  'u02-l5': {
    kind: 'now-to-future',
    labels: ['今決めた', "I'll help you."],
    caption: 'will は「今その場で決めたこと」や、これからの予測を伝えます。',
  },
  'u02-l6': {
    kind: 'calendar-day',
    labels: ['We are going to move.', 'もう決めた予定'],
    caption: 'be going to は前から決めていた予定や、目の前に根拠がある予測に使います。',
  },

  // U03 名詞と冠詞の基礎
  'u03-l1': {
    kind: 'count-vs-mass',
    labels: ['three apples', 'some water'],
    caption: '数えられる名詞は複数形にでき、数えられない名詞は形を変えず量で表します。',
  },
  'u03-l2': {
    kind: 'one-vs-the',
    labels: ['どれか1つ = a', 'あの1つ = the'],
    caption: 'たくさんある中の「どれか1つ」が a / an。次の語の発音が母音なら an を使います。',
  },
  'u03-l3': {
    kind: 'filter-group',
    labels: ['books', 'the book'],
    caption: 'お互いに「どれのことか」が分かるまで絞れているとき、the を付けます。',
  },
  'u03-l4': {
    kind: 'count-vs-mass',
    labels: ['many books', 'much water'],
    caption: '数えられる名詞は many、数えられない名詞は much。会話では a lot of が万能です。',
  },

  // U04 代名詞と限定詞
  'u04-l1': {
    kind: 'action',
    labels: ['I', 'know', 'him'],
    caption: '主語の位置では I、動詞のあと(目的語)では me / him のように形が変わります。',
  },
  'u04-l2': {
    kind: 'near-far',
    labels: ['this / these', 'that / those'],
    caption: '近いものは this / these、遠いものは that / those。複数なら these / those です。',
  },
  'u04-l3': {
    kind: 'one-vs-the',
    labels: ['a red one', 'it'],
    caption: '「同じ種類のどれか」は one / ones、「まさにそのもの」は it で受けます。',
  },

  // U05 形容詞と副詞の基礎
  'u05-l1': {
    kind: 'tag-noun',
    labels: ['a car', 'a red car'],
    caption: '形容詞は名詞の前か、be動詞のあとに置いて様子を説明します。',
  },
  'u05-l2': {
    kind: 'tag-noun',
    labels: ['drives', 'drives carefully'],
    caption: '副詞は動詞や形容詞に説明を足します。多くは形容詞 + -ly の形です。',
  },
  'u05-l3': {
    kind: 'scale',
    labels: ['never', 'sometimes', 'always'],
    caption: '頻度の副詞は「どのくらいよくするか」を表し、一般動詞の前に置きます。',
  },

  // U06 疑問文をつくる
  'u06-l1': {
    kind: 'question-mark',
    labels: ['どこで働くの?', 'Where'],
    caption: '尋ねたい部分を疑問詞に変えて文の先頭へ出し、そのあとは疑問文の語順にします。',
  },
  'u06-l2': {
    kind: 'question-mark',
    labels: ['どのくらい?', 'How long'],
    caption: 'How のあとに形容詞・副詞を足すと「どのくらい〜か」を尋ねられます。',
  },
  'u06-l3': {
    kind: 'helper-verb',
    labels: ['Who', 'broke it?', 'did break'],
    caption: '主語を尋ねる疑問文では do / does / did を使わず、そのまま動詞を続けます。',
  },

  // U07 比較
  'u07-l1': {
    kind: 'bars-compare',
    labels: ['Mia', 'taller than', 'Ken'],
    caption: '「Ken is taller than Mia.」高い方を主語にすると比較級の文になります。',
  },
  'u07-l2': {
    kind: 'podium',
    labels: ['Ken', 'Mia', 'Ryo'],
    caption: '3つ以上の中で一番なら the tallest のように the + 最上級を使います。',
  },
  'u07-l3': {
    kind: 'equals',
    labels: ['Ken', 'is as tall as', 'Mia'],
    caption: 'as ... as は「同じくらい」。not as ... as なら「〜ほど…ない」になります。',
  },
  'u07-l4': {
    kind: 'scale',
    labels: ['not enough', 'enough', 'too much'],
    caption: 'enough は「足りている」、too は「行きすぎ」。度合いのどこにあるかで選びます。',
  },

  // U08 前置詞
  'u08-l1': {
    kind: 'point-surface-box',
    labels: ['at 7:00', 'on Monday', 'in April'],
    caption: '時刻は点(at)、曜日や日付は面(on)、月や年は箱の中(in)というイメージです。',
  },
  'u08-l2': {
    kind: 'point-surface-box',
    labels: ['at the door', 'on the desk', 'in the box'],
    caption: '場所も同じイメージ。地点は at、接している面は on、囲まれた中は in です。',
  },
  'u08-l3': {
    kind: 'path-move',
    labels: ['home', 'through the park', 'school'],
    caption: '移動は「どこから・どんな経路で・どこへ」を前置詞で描きます。',
  },
  'u08-l4': {
    kind: 'linked-pair',
    labels: ['listen', 'to music'],
    caption: 'listen to のように、動詞・形容詞と前置詞はセットのまま覚えます。',
  },

  // U09 助動詞の基礎
  'u09-l1': {
    kind: 'gate-allow',
    labels: ['I can swim.', "I can't drive."],
    caption: '助動詞のあとは必ず原形。否定も疑問も do を使わず can 自身が作ります。',
  },
  'u09-l2': {
    kind: 'gate-allow',
    labels: ["don't have to", "mustn't"],
    caption: "don't have to は「しなくてよい」、mustn't は「してはいけない」。意味が正反対です。",
  },
  'u09-l3': {
    kind: 'scale',
    labels: ['should', 'had better', 'must'],
    caption: 'アドバイスから義務まで、伝えたい強さで選びます。had better は警告に近い響きです。',
  },
  'u09-l4': {
    kind: 'scale',
    labels: ['might', 'may', 'will'],
    caption: '同じ未来のことでも、どのくらい確信があるかで助動詞を選び分けます。',
  },

  // U10 不定詞と動名詞の基礎
  'u10-l1': {
    kind: 'now-to-future',
    labels: ['want / decide', 'to go abroad'],
    caption: 'to不定詞は「これから向かうこと」。矢印のイメージで捉えます。',
  },
  'u10-l2': {
    kind: 'linked-pair',
    labels: ['enjoy', 'reading'],
    caption: 'enjoy / finish / mind のあとには動名詞(-ing)がくっつきます。',
  },
  'u10-l3': {
    kind: 'arrow-vs-loop',
    labels: ['want to go', 'enjoy going'],
    caption: 'to不定詞は「これから」、動名詞は「していること」。動詞ごとに相性が決まっています。',
  },
  'u10-l4': {
    kind: 'linked-pair',
    labels: ['good at', 'cooking'],
    caption: '前置詞のあとは必ず動名詞。to不定詞は置けません。',
  },

  // U11 現在完了
  'u11-l1': {
    kind: 'bridge-past-now',
    labels: ['過去の出来事', '今の状態'],
    caption: '現在完了は、過去の出来事と今を1本の橋でつなぐ形です。',
  },
  'u11-l2': {
    kind: 'steps',
    labels: ['一度目', '二度目', '三度目'],
    caption: '「〜したことがある」は経験。ever / never や回数の表現と一緒に使います。',
  },
  'u11-l3': {
    kind: 'bridge-past-now',
    labels: ['since 2019', '今も続く'],
    caption: '「ずっと〜している」の継続。for は期間の長さ、since は始まった時点を示します。',
  },
  'u11-l4': {
    kind: 'two-cards',
    labels: ['already sent', 'not sent yet'],
    caption: 'just / already / yet は「今どうなっているか」という完了・結果を伝えます。',
  },
  'u11-l5': {
    kind: 'two-cards',
    labels: ['I lost my key.', "I've lost my key."],
    caption: '今とつながっているかどうかが、過去形と現在完了の分かれ目です。',
  },
  'u11-l6': {
    kind: 'steps',
    labels: ['経験', '継続', '完了'],
    caption: '文中の手がかりから3つの用法を見分け、過去形とも区別します。',
  },

  // U12 未来表現の発展
  'u12-l1': {
    kind: 'calendar-day',
    labels: ['I am meeting Ken.', 'tomorrow at three'],
    caption: '現在進行形は「もう手配が済んだ予定」を自然に伝えられます。',
  },
  'u12-l2': {
    kind: 'scale',
    labels: ['will', 'be going to', '現在進行形'],
    caption: '「いつ・どこまで決まっているか」で3つの未来表現を選び分けます。',
  },
  'u12-l3': {
    kind: 'now-to-future',
    labels: ['when he arrives', "I'll call you."],
    caption: '時・条件の節の中は未来のことでも現在形。will は主節に置きます。',
  },

  // U13 受動態
  'u13-l1': {
    kind: 'spotlight-swap',
    labels: ['They clean it.', '受動態へ', 'It is cleaned.'],
    caption: '「される側」を主語に置くと、動詞は be動詞 + 過去分詞になります。',
  },
  'u13-l2': {
    kind: 'dots-omit',
    labels: ['The room was cleaned by someone.', 'The room was cleaned.'],
    caption: '誰がしたかが分からない・重要でないときは by句を省きます。',
  },
  'u13-l3': {
    kind: 'two-cards',
    labels: ['will be cleaned', 'has been cleaned'],
    caption: '助動詞や完了形と組み合わせても、be + 過去分詞の部分は変わりません。',
  },
  'u13-l4': {
    kind: 'spotlight-swap',
    labels: ['話題は行為者', '視点を移す', '話題はされた側'],
    caption: '何を話題の中心にしたいかで、能動態と受動態を選びます。',
  },

  // U14 関係詞
  'u14-l1': {
    kind: 'tag-noun',
    labels: ['the man', 'who lives next door'],
    caption: '名詞のあとに who / which / that を続けて、説明を足します。',
  },
  'u14-l2': {
    kind: 'dots-omit',
    labels: ['the book which I read', 'the book I read'],
    caption: '目的語だった関係代名詞は省略できます。会話では省くのが自然です。',
  },
  'u14-l3': {
    kind: 'tag-noun',
    labels: ['the town', 'where I grew up'],
    caption: '所有は whose、場所は where、時は when で説明を続けます。',
  },
  'u14-l4': {
    kind: 'filter-group',
    labels: ['my friends', 'who live here'],
    caption: 'カンマなしは「絞り込む」用法。カンマがあると付け足しの説明になります。',
  },
  'u14-l5': {
    kind: 'two-cards',
    labels: ['who / which', 'whose / where'],
    caption: '人か物か、格は何か、カンマがあるか。この順で確かめて関係詞を選びます。',
  },

  // U15 条件文
  'u15-l1': {
    kind: 'two-roads',
    labels: ['If it rains,', 'we stay home.', 'we go out.'],
    caption: 'いつでも成り立つ話は現在形どうし、これから起こりうる話は will を使います。',
  },
  'u15-l2': {
    kind: 'thought-cloud',
    labels: ['時間がない', "If I had time, I'd go."],
    caption: '現実とは違う想像は If + 過去形, would + 原形で表します。',
  },
  'u15-l3': {
    kind: 'two-cards',
    labels: ['unless', 'in case'],
    caption: 'unless は「〜しない限り」、in case は「〜に備えて」、as long as は「〜しさえすれば」。',
  },
  'u15-l4': {
    kind: 'two-roads',
    labels: ['どちらの話?', 'If I have time', 'If I had time'],
    caption: '現実的な話なら第1条件文、想像の話なら第2条件文を選びます。',
  },

  // U16 接続詞と文の結合
  'u16-l1': {
    kind: 'cause-effect',
    labels: ['It rained.', 'so', 'we stayed in.'],
    caption: 'because は理由、so は結果、although は「〜だけれども」を導きます。',
  },
  'u16-l2': {
    kind: 'earlier-later',
    labels: ['I waited', 'until he came'],
    caption: '時の接続詞で出来事の順序を示します。未来のことでも節の中は現在形です。',
  },
  'u16-l3': {
    kind: 'two-cards',
    labels: ['both A and B', 'neither A nor B'],
    caption: 'both は両方、either はどちらか、neither はどちらも〜ない、を表します。',
  },

  // U17 現在完了進行形
  'u17-l1': {
    kind: 'bridge-past-now',
    labels: ['2時間前に開始', '今も続く'],
    caption: 'have been + -ing は「始まって今も続いている動作」を表します。',
  },
  'u17-l2': {
    kind: 'two-cards',
    labels: ["I've painted it.", "I've been painting."],
    caption: 'やり終えた結果なら現在完了、続けている動作なら現在完了進行形です。',
  },

  // U18 過去完了と時制の整理
  'u18-l1': {
    kind: 'earlier-later',
    labels: ['had left(先)', 'arrived(あと)'],
    caption: '過去のある時点より前に起きたことは had + 過去分詞で表します。',
  },
  'u18-l2': {
    kind: 'two-cards',
    labels: ['過去形(順番どおり)', '過去完了(さらに前)'],
    caption: '前後関係が明らかなら過去形で十分。ずらしたいときだけ過去完了を使います。',
  },
  'u18-l3': {
    kind: 'steps',
    labels: ['背景', '出来事', 'その前'],
    caption: '過去進行形で背景、過去形で出来事、過去完了でその前の事情を語ります。',
  },

  // U19 人の言葉を伝える・丁寧に質問する
  'u19-l1': {
    kind: 'speech-relay',
    labels: ['I am tired.', 'said', 'he was tired'],
    caption: '人の発言を伝えるときは、時制・代名詞・時の表現を一段ずらします。',
  },
  'u19-l2': {
    kind: 'speech-relay',
    labels: ['Are you busy?', 'asked', 'if I was busy'],
    caption: '質問は asked if / asked + 疑問詞、指示やお願いは told / asked + 人 + to不定詞で伝えます。',
  },
  'u19-l3': {
    kind: 'speech-relay',
    labels: ['Be careful!', 'warned', 'me to be careful'],
    caption: 'say / tell だけに頼らず promise / suggest / warn を使うと、発言の意図まで伝わります。',
  },
  'u19-l4': {
    kind: 'box-in-slot',
    labels: ['where he lives', 'Do you know ...?'],
    caption: '文の中に入れた疑問文は「主語 + 動詞」の語順に戻します。',
  },

  // U20 助動詞の発展
  'u20-l1': {
    kind: 'scale',
    labels: ["can't", 'might', 'must'],
    caption: '根拠の強さに合わせて、今のことを「〜のはずがない」から「〜に違いない」まで表します。',
  },
  'u20-l2': {
    kind: 'scale',
    labels: ["can't have", 'might have', 'must have'],
    caption: '助動詞 + have + 過去分詞で、過去の出来事を推量します。',
  },
  'u20-l3': {
    kind: 'thought-cloud',
    labels: ['しなかった', 'I should have called.'],
    caption: '実際にはしなかったことへの後悔は should have + 過去分詞で表します。',
  },
  'u20-l4': {
    kind: 'repeat-cycle',
    labels: ['I used to swim here.', '昔のくり返し'],
    caption: 'used to は「昔はよくしたが、今はしない」ことを表します。',
  },

  // U21 動名詞・不定詞の発展
  'u21-l1': {
    kind: 'arrow-vs-loop',
    labels: ['stopped to rest', 'stopped raining'],
    caption: 'to不定詞は「これからすること」、動名詞は「していたこと」。意味が変わります。',
  },
  'u21-l2': {
    kind: 'handoff',
    labels: ['I', 'to wash the car', 'him'],
    caption: 'want / ask / tell + 人 + to不定詞で「人に〜してほしい」を表します。',
  },
  'u21-l3': {
    kind: 'box-in-slot',
    labels: ['to use this app', 'It is easy ...'],
    caption: '主語が長くなるときは仮主語の It で始め、内容を後ろに回します。',
  },

  // U22 第3条件文と wish
  'u22-l1': {
    kind: 'thought-cloud',
    labels: ['実際は遅れた', "If I'd left earlier, ..."],
    caption: '過去の非現実は If + had + 過去分詞, would have + 過去分詞で表します。',
  },
  'u22-l2': {
    kind: 'thought-cloud',
    labels: ['時間がない', 'I wish I had more time.'],
    caption: '今のことは wish + 過去形、過去のことは wish + had + 過去分詞です。',
  },
  'u22-l3': {
    kind: 'steps',
    labels: ['現実', '今の仮定', '過去の仮定'],
    caption: '現実的な話か、今の非現実か、過去の非現実かで第1〜第3条件文を選びます。',
  },

  // U23 仮定法の発展
  'u23-l1': {
    kind: 'earlier-later',
    labels: ['過去の仮定', '今の結果'],
    caption: '条件は過去、結果は今。混合条件文は時間のずれた2つを組み合わせます。',
  },
  'u23-l2': {
    kind: 'two-cards',
    labels: ['provided that', 'on condition that'],
    caption: 'if 以外にも provided / on condition that / suppose で条件を表せます。',
  },
  'u23-l3': {
    kind: 'thought-cloud',
    labels: ['今の状況', "I'd rather stay home."],
    caption: "would rather + 原形は自分の希望、would rather + 主語 + 過去形は別の人への希望を表します。It's time + 主語 + 過去形は「もう〜する時間だ」です。",
  },

  // U24 使役と知覚
  'u24-l1': {
    kind: 'handoff',
    labels: ['I', 'my hair cut', 'stylist'],
    caption: 'have / get + 物 + 過去分詞で「〜してもらう」「〜される」を表します。',
  },
  'u24-l2': {
    kind: 'scale',
    labels: ['let', 'have / get', 'make'],
    caption: '許可・依頼・強制と強さが変わります。make / let のあとは原形です。',
  },
  'u24-l3': {
    kind: 'eye-ear',
    labels: ['I saw him cross.', '原形か -ing か'],
    caption: '一部始終を見たなら原形、途中の一場面なら -ing を続けます。',
  },

  // U25 分詞
  'u25-l1': {
    kind: 'feeling-source',
    labels: ['a boring movie', 'I am bored.'],
    caption: '感情を引き起こす側は -ing、感じる側は -ed を使います。',
  },
  'u25-l2': {
    kind: 'tag-noun',
    labels: ['the man', 'standing there'],
    caption: '分詞を名詞の後ろに置くと、関係詞節より短く説明を足せます。',
  },
  'u25-l3': {
    kind: 'dots-omit',
    labels: ['Because I was tired, I left.', 'Being tired, I left.'],
    caption: '接続詞と主語を省いて -ing で始めると分詞構文になります。',
  },

  // U26 受動態の発展
  'u26-l1': {
    kind: 'box-in-slot',
    labels: ['that he is a genius', 'It is said ...'],
    caption: '「〜と言われている」は It is said that ... と He is said to ... の2通りで表せます。',
  },
  'u26-l2': {
    kind: 'two-cards',
    labels: ['to be done', 'being done'],
    caption: '不定詞や動名詞の位置でも、be + 過去分詞の形で「される」を表します。',
  },
  'u26-l3': {
    kind: 'two-cards',
    labels: ['be broken(状態)', 'get broken(出来事)'],
    caption: 'get + 過去分詞は「〜される」という出来事を、会話らしく表します。',
  },

  // U27 関係詞の発展
  'u27-l1': {
    kind: 'tag-noun',
    labels: ['the house', 'in which he lived'],
    caption: '前置詞を関係代名詞の前に置くと、書き言葉らしいフォーマルな形になります。',
  },
  'u27-l2': {
    kind: 'box-in-slot',
    labels: ['what he said', 'I believe ...'],
    caption: 'what は先行詞を自分の中に含む関係詞。whatever は「何でも」を表します。',
  },
  'u27-l3': {
    kind: 'tag-noun',
    labels: ['文全体', ', which surprised me'],
    caption: 'カンマ + which なら、直前の文の内容全体を受けてコメントを足せます。',
  },

  // U28 談話標識と文章構成
  'u28-l1': {
    kind: 'cause-effect',
    labels: ['It rained.', 'However,', 'we went out.'],
    caption: 'however は文をつなぐ副詞、although は節、despite は名詞を続けます。',
  },
  'u28-l2': {
    kind: 'cause-effect',
    labels: ['売上が落ちた', 'Therefore,', '値下げした'],
    caption: 'therefore は結果、moreover は追加、such as は例示を示します。',
  },
  'u28-l3': {
    kind: 'steps',
    labels: ['First,', 'Then,', 'In short,'],
    caption: '順序 → 展開 → 要約の流れを標識で示すと、話の構造が伝わります。',
  },

  // U29 名詞節
  'u29-l1': {
    kind: 'box-in-slot',
    labels: ['that she is right', 'I think ...'],
    caption: 'that節は「〜ということ」という名詞のかたまり。think のあとでは省略できます。',
  },
  'u29-l2': {
    kind: 'question-mark',
    labels: ['来るかどうか', 'whether'],
    caption: '「〜かどうか」は whether / if。文の中では「主語 + 動詞」の語順に戻します。',
  },
  'u29-l3': {
    kind: 'box-in-slot',
    labels: ['that he passed', 'It is true ...'],
    caption: '主語が長いときは仮主語の it を先に置き、内容を後ろに回します。',
  },

  // U30 強調・倒置・省略
  'u30-l1': {
    kind: 'spotlight-swap',
    labels: ['Ken broke it.', 'スポットライト', 'It was Ken that'],
    caption: 'It is ... that や What ... is で、一番伝えたい部分を前に出して強調します。',
  },
  'u30-l2': {
    kind: 'swap-cards',
    labels: ['I have never seen it.', 'Never have I seen it.'],
    caption: '否定語を文頭に出すと、そのあとが疑問文の語順になります。',
  },
  'u30-l3': {
    kind: 'dots-omit',
    labels: ['Yes, I think it will rain.', 'Yes, I think so.'],
    caption: '繰り返しになる部分は so / not や助動詞で置きかえます。',
  },

  // U31 紛らわしい構造の整理
  'u31-l1': {
    kind: 'steps',
    labels: ['過去形', '現在完了', '過去完了'],
    caption: '時を表す語句が「今」とつながっているかを見て、時制を選びます。',
  },
  'u31-l2': {
    kind: 'two-cards',
    labels: ['by(〜までに)', 'until(〜まで)'],
    caption: 'by は期限の一点、until は続く期間。during は名詞、while は節を続けます。',
  },
  'u31-l3': {
    kind: 'two-cards',
    labels: ['so + 形容詞', 'such + 名詞'],
    caption: '後ろに来る形を手がかりに so / such、another / other、rise / raise を選びます。',
  },

  // U32 時制と条件の総仕上げ
  'u32-l1': {
    kind: 'now-to-future',
    labels: ['今', 'will have done'],
    caption: '未来のある時点で進行中なら will be doing、終わっているなら will have done です。',
  },
  'u32-l2': {
    kind: 'earlier-later',
    labels: ['過去のある時点', 'was going to'],
    caption: '過去のある時点から先を見ていた気持ちは was going to / would / was about to で表します。',
  },
  'u32-l3': {
    kind: 'swap-cards',
    labels: ['If I had known, ...', 'Had I known, ...'],
    caption: 'if を省くと、Had + 主語 + 過去分詞のように助動詞が前に出ます。',
  },
  'u32-l4': {
    kind: 'bars-compare',
    labels: ['practice more', 'the better', 'you get'],
    caption: '「〜すればするほど…」は the + 比較級を2つ並べて表します。',
  },

  // U33 日本語話者が最後まで残す誤り
  'u33-l1': {
    kind: 'one-vs-the',
    labels: ['初出 = a / an', '既知 = the'],
    caption: '初めて出すか、お互いに分かっているか。この2つの問いで冠詞を選びます。',
  },
  'u33-l2': {
    kind: 'count-vs-mass',
    labels: ['a few books', 'a little water'],
    caption: 'few / little は「ほとんどない」、a few / a little は「少しある」。数えられるかで選びます。',
  },
  'u33-l3': {
    kind: 'linked-pair',
    labels: ['turn off', 'the light'],
    caption: '分離できる句動詞では、代名詞は turn it off のように必ず間に置きます。',
  },
}

/** 挿絵を最初の解説ブロックの直後へ差し込む。UI・Markdown・PDF は合成後の同じデータを使う。 */
export function applyLessonIllustrations(units: GrammarUnit[]): GrammarUnit[] {
  return units.map((unit) => ({
    ...unit,
    lessons: unit.lessons.map((lesson) => {
      const illustration = lessonIllustrations[lesson.id]
      if (!illustration) throw new Error(`${lesson.id}: 挿絵がありません。`)
      const animation = LESSON_ANIMATIONS[lesson.id]
      if (!animation) throw new Error(`${lesson.id}: アニメーションがありません。`)

      let inserted = false
      const blocks = lesson.blocks.flatMap<LessonBlock>((block) => {
        if (inserted || block.type !== 'explanation') return [block]
        inserted = true
        return [
          block,
          {
            type: 'illustration',
            sceneId: lesson.id,
            alt: `${animation.title}の2Dアニメーション。${animation.steps.map((step, i) => `${i + 1}. ${step.sentence.replaceAll('|', ' ')} — ${step.note}`).join(' ')}`,
            ...illustration,
          },
        ]
      })

      if (!inserted) throw new Error(`${lesson.id}: 挿絵を差し込む解説ブロックがありません。`)
      return { ...lesson, blocks }
    }),
  }))
}
