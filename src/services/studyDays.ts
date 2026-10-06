// 学習した日の記録(トータル)と、マスコット「イングバード」のほめ言葉。
//
// 数えるのは「何かしら学習した日」の合計で、連続日数(ストリーク)ではない。
// 休んだ日で減るものが無いので、久しぶりの学習も「来たこと」自体をほめられる。
// 記録は1日1エントリ(YYYY-MM-DD の配列)。1件13バイトなので、年単位でも数KBにしかならない。
//
// ほめ言葉は「種類 × 言い回し候補」で持つ。同じ状況でも毎回ちがう言葉が出るように、
// それぞれ10前後の候補を用意し、マスコットの気分(表情・アニメーション)も一緒に選ぶ。

import { daysBetween, todayString } from './dates'
import { KEYS, loadJson, saveJson } from './storage'

/** recordStudyDay が新しい学習日を記録したときに発火する。detail は StudyRecord。 */
export const STUDY_RECORDED_EVENT = 'eng:study-recorded'

export type PraiseKind = 'first' | 'milestone' | 'return' | 'daily' | 'done' | 'encourage'

/**
 * マスコットの気分。Ingbird コンポーネントの data-mood と対応する。
 * idle(いつも) / happy(うれしい) / cheer(はりきる) / party(お祝い) / proud(誇らしい) /
 * wave(おかえり) / curious(きになる) / wow(びっくり) / sleepy(ねむい) / shy(てれる) /
 * think(考え中) / sing(ごきげん)。
 */
export type IngbirdMood =
  | 'idle'
  | 'happy'
  | 'cheer'
  | 'party'
  | 'proud'
  | 'wave'
  | 'curious'
  | 'wow'
  | 'sleepy'
  | 'shy'
  | 'think'
  | 'sing'

export type Praise = {
  kind: PraiseKind
  title: string
  message: string
  /** 紙吹雪を出すか(はじめての日・節目・久しぶり) */
  confetti: boolean
  /** マスコットの動き */
  mood: IngbirdMood
}

export type StudyStatus = {
  /** 学習した日の合計(トータル)。連続日数ではない。 */
  totalDays: number
  studiedToday: boolean
  /** 最後に学習した日。記録が無ければ null。 */
  lastDate: string | null
  /** 最後の学習日から今日までの日数(今日なら0)。記録が無ければ null。 */
  daysSinceLast: number | null
  /** 最後の学習日の、その前回からの間隔。「N日ぶり!」の判定に使う(totalDays < 2 なら null)。 */
  lastGap: number | null
  /** 次の節目と、そこまでの残り日数。全部使い切っていれば null。 */
  next: { at: number; remaining: number } | null
}

export type StudyRecord = { date: string; status: StudyStatus; praise: Praise }

/** ほめ方が特別になる節目。1日目と3日目以降を細かく置き、あとは長期の区切り。 */
export const MILESTONES = [1, 3, 5, 7, 10, 14, 20, 30, 50, 75, 100, 150, 200, 250, 300, 365, 500, 730, 1000] as const

const DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/

/** 保存された学習日。重複・不正な値は読むときに落とし、古い順に並べる。 */
export function getStudyDays(): string[] {
  const raw = loadJson<unknown>(KEYS.studyDays, [])
  if (!Array.isArray(raw)) return []
  const days = new Set<string>()
  for (const value of raw) if (typeof value === 'string' && DATE_PATTERN.test(value)) days.add(value)
  return [...days].sort()
}

function statusOf(days: readonly string[], today: string): StudyStatus {
  const lastDate = days.at(-1) ?? null
  const lastGap = days.length < 2 ? null : daysBetween(days[days.length - 2], days[days.length - 1])
  const nextAt = MILESTONES.find((milestone) => milestone > days.length) ?? null
  return {
    totalDays: days.length,
    studiedToday: days.includes(today),
    lastDate,
    daysSinceLast: lastDate === null ? null : Math.max(0, daysBetween(lastDate, today)),
    lastGap,
    next: nextAt === null ? null : { at: nextAt, remaining: nextAt - days.length },
  }
}

export function getStudyStatus(today: string = todayString()): StudyStatus {
  return statusOf(getStudyDays(), today)
}

export function isMilestone(totalDays: number): boolean {
  return (MILESTONES as readonly number[]).includes(totalDays)
}

/**
 * 「今日は学習した」ことを記録する。学習エリアを問わず、何か1つ進んだ時点で呼ぶ。
 * 同じ日に何度呼んでも日は増えず、イベントも最初の1回だけ発火する。
 */
export function recordStudyDay(today: string = todayString()): StudyRecord {
  const days = getStudyDays()
  const isNewDay = !days.includes(today)
  // 端末の時計が戻って today が末尾より前になっても、Set と sort で1日1件を保つ。
  const nextDays = isNewDay ? [...new Set([...days, today])].sort() : days
  if (isNewDay) saveJson(KEYS.studyDays, nextDays)
  const status = statusOf(nextDays, today)
  const record: StudyRecord = { date: today, status, praise: praiseFor(status, isNewDay) }
  if (isNewDay && typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent<StudyRecord>(STUDY_RECORDED_EVENT, { detail: record }))
  }
  return record
}

/** 「5日ぶり」「1週間ぶり」「1か月ぶり」…の言い方。 */
export function describeGap(gap: number): string {
  if (gap < 7) return `${gap}日ぶり`
  if (gap < 30) return `${Math.floor(gap / 7)}週間ぶり`
  if (gap < 365) return `${Math.floor(gap / 30)}か月ぶり`
  return `${Math.floor(gap / 365)}年ぶり`
}

/** 種類ごとに選べる気分。その場面に合う表情だけを使う。 */
const MOOD_POOLS: Record<PraiseKind, readonly IngbirdMood[]> = {
  first: ['party', 'wow', 'cheer'],
  milestone: ['party', 'proud', 'cheer'],
  return: ['wave', 'happy', 'proud'],
  daily: ['cheer', 'happy', 'proud', 'sing'],
  done: ['happy', 'proud', 'shy', 'wave'],
  encourage: ['curious', 'wave', 'happy', 'think'],
}

/** はじめての1日。 */
const FIRST_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['1日目、はじまった!', 'これがきみの最初の学習日。1日でもやったら、それはもう積み上がってるんだよ。'],
  ['記念すべき1日目!', 'はじめの1日をえらんだきみに、イングバードから拍手を送るよ!'],
  ['0→1の日だよ!', '何もないところから1日を作るのが、いちばんすごい。今日はその日!'],
  ['ようこそ、学習日のはじまり!', 'ここから日は増えても減らない。トータルの積み上げが、いまスタートしたよ!'],
  ['1日ぶん、光った!', 'きみの英語のタイムラインに、今日が刻まれたよ。うれしいな!'],
]

/** 今日ぶんを積んだ日。 */
const DAILY_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日の1日ぶん、ゲット!', 'やったね!1問でも1セッションでも、今日もちゃんと前に進んでる。えらい!'],
  ['きた!今日も学習日!', 'その1日はきみのもの。積み上がった日は、あとから消えないよ。'],
  ['Nice! 今日もいけたね!', '小さくても、やった日はやった日。いいペースだよ!'],
  ['今日も1日ぶん、追加!', 'ちいさな1日でも、トータルはちゃんと大きくなる。えらい!'],
  ['その1問が、今日を作った!', '1問でも1セッションでも、今日はもう学習日。積み上げは裏切らないよ。'],
  ['いい日にしよう!', '今日のぶんを置いていこう。明日のきみが「やってあってよかった」って言うよ。'],
  ['コツコツ、きた!', '毎日じゃなくていい。来た日に1つずつで、ちゃんと強くなるよ。'],
  ['今日の花丸、決定!', 'やった日は必ず残る。休んだ日に消えるものは、何もないんだ。'],
  ['ナイス1日!', 'その調子。今日の1日は、きみの英語の一部になったよ。'],
  ['きたきた、今日も!', '積み上げの音が聞こえるよ。1日ぶん、しっかり乗った!'],
  ['小さな前進、おめでとう!', '大きなことをしなくて大丈夫。今日も1歩、前に進んだね。'],
  ['今日のきみ、えらい!', '「やる」を選んだ時点で、もう勝ちなんだよ。1日ぶん、受け取って!'],
  ['日めくり成功!', 'トータルの日がまた1つ増えたよ。そのぶん、未来のきみがラクになる。'],
  ['学習日、ゲットだね!', 'この1日は誰にも取られない。今夜はちょっと自分をほめてね。'],
]

/** 今日はもう学習ずみで、のぞきに来た日。 */
const DONE_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日はもう学習ずみ!', 'のぞきに来てくれてうれしいな。明日も1問でいいからね。'],
  ['今日のぶんは、もう積み上がってる!', 'まだやる?それなら大歓迎。もっと大きくなっちゃうね!'],
  ['もう学習ずみの日だね!', 'それでも会いに来てくれてうれしい。次は明日、1問からでいいよ。'],
  ['えらい日に来てくれたね', '今日のノルマは達成ずみ。コーヒーでも飲みながら、ゆっくりしてね。'],
  ['おかわり、ありがとう!', '今日のぶんはもう十分。でも来てくれたから、ちょっとだけ羽を振っておくよ。'],
  ['二度目の訪問だね!', '勉強しなくても、のぞきに来るだけでえらい。明日も待ってるよ。'],
  ['ちゃんと休むのも作戦!', '今日はもう花丸。休む日があるから、積み上げは長く続くんだよ。'],
  ['その余裕、いいね!', '焦らなくて大丈夫。学習日は減らないから、今日はゆっくりね。'],
  ['見に来てくれてありがとう!', '今日のぶんは達成ずみ。また明日、いっしょにやろう!'],
  ['えらい人がまた来た!', '今日はもう合格。未来のきみに、ちゃんと1日を渡してあるよ。'],
]

/** まだ1日も学習していない日の誘い。 */
const WELCOME_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日はまだ、これから!', '1問だけでも、今日は学習日になるよ。まずは1つ、いってみる?'],
  ['はじめましての1日にしよう!', 'まだ0日だからこそ、今日やると最初の1日になるよ。1問でいいんだ。'],
  ['いっしょに、はじめよう!', 'むずかしいことは後回し。1問だけ、タップしてみよう?'],
  ['今日、記念日にできるよ!', '今日1つ進めば、この日がきみの1日目になる。わくわくしない?'],
  ['1問だけ、試してみる?', 'はじめの1日は、いちばん大きな1日。イングバードも応援してるよ!'],
  ['英語のタイムライン、はじめる?', '最初の1日を作ると、ここからトータルが増えていくよ。'],
  ['完璧じゃなくていいんだよ', '1問やったら、それだけで今日は勝ち。30秒から始めよう!'],
  ['ウォームアップしよう!', '30秒で終わる1問から。やってみたら、きっと気分がいいよ。'],
  ['まだ間に合うよ!', '今日が終わる前に、1問だけ。最初の1日、作っちゃおう!'],
  ['こんにちは、イングバードだよ!', '今日は何をする?1問だけでも、ちゃんと学習日になるよ。'],
]

/** 学習したことはあるけれど、今日はまだの日の誘い(1〜2日あいても責めない)。 */
const GENTLE_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日はまだみたいだね', '1問だけで大丈夫。前のきみが残した日は、ちゃんとここにあるよ。'],
  ['お待ちしてました!', '1日あいたって平気。トータルは減らないから、今日もゆるく1ついこう。'],
  ['今日のぶん、まだ空いてるよ', '30秒の1問でいい。埋めたら、きみの1日になる!'],
  ['続き、いこっか!', '1日休んでも、積み上げはそのまま。今日も1つだけ足そう?'],
  ['今日も会いに来てくれた!', 'それだけでうれしい。よかったら1問、いっしょにやってみよう。'],
  ['のんびりでOK!', '毎日じゃなくていいよ。今日来た日は、今日ぶんを足せる日。'],
  ['1問クエスト、出すね!', 'むずかしくないやつにしたよ。タップ1つで受けてみて!'],
  ['今日の1日、つくる?', '前までの日は消えない。今日を足すかどうかは、きみが決めていいんだ。'],
  ['ちいさくやろう!', '1問だけなら、疲れててもできそう?できたら今日は花丸だよ。'],
  ['きみのペースでいいんだよ', '来てくれたから、1問だけ紹介するね。やるかどうかは、ゆっくり決めてね。'],
]

/** 久しぶりに学習した日の見出し(「N日ぶり!」を含む)。 */
const RETURN_TITLES: ReadonlyArray<(gap: string) => string> = [
  (gap) => `${gap}!おかえり!`,
  (gap) => `${gap}の再会、うれしい!`,
  (gap) => `おかえりなさい!${gap}だね!`,
  (gap) => `${gap}、ちゃんと戻ってきたね!`,
]

/** 久しぶりだけど、まだ学習はこれからの日の見出し(「N日ぶり」を含む)。 */
const WELCOME_BACK_TITLES: ReadonlyArray<(gap: string) => string> = [
  (gap) => `${gap}だね、待ってたよ!`,
  (gap) => `${gap}。会えてうれしいな!`,
  (gap) => `${gap}、今日も来てくれた!`,
  (gap) => `${gap}だって、来たからもう勝ち!`,
]

/** 久しぶりの復帰を祝う本文。どの候補でも「減らない」ことを伝える。 */
const RETURN_BODIES: readonly string[] = [
  '久しぶりでも、来ただけで今日は花丸。休んでいた日は、これまでの日を1日も減らさないよ。',
  '間があいても、積み上げた日は消えない。今日からまた足していけばいいんだ。減らさないよ。',
  '戻ってきたのがいちばんえらい。休んだ日は、これまでの記録を1日も減らさないからね。',
  'ブランクは敵じゃないよ。トータルは減らさないし、今日の1日はちゃんと足される。',
  'また会えてうれしい!やらなかった日で減るものは、ここには何もない。減らさないよ。',
  '久しぶりの1日は、いつもの1日より価値がある。減らさないどころか、今日また増えたよ。',
  'おかえり!ここは休んだ日で失うものが無い場所。積み上げは減らさないよ。',
  '間が空いた日も、きみの学習日にはカウントしない。だから減らさない。今日が新しく増えるだけ。',
  '来る日も来ない日もあっていい。大事なのは戻ってきたことで、記録は1日も減らさないよ。',
  'おかえりなさい。久しぶりでも、トータルの日は減らさないし、今日ぶんはちゃんと積めるよ。',
]

/** 節目+久しぶりの復帰が重なった日の本文。「復帰」を含む。 */
const MILESTONE_BACK_BODIES: readonly string[] = [
  '{gap}の復帰で、しかも{days}日目!休んでいた日は、ここまでの記録を1日も減らしていないよ。',
  'おかえり!{gap}の復帰が、ちょうど{days}日目に重なったよ。休んだ日で減ったものは何もない。',
  '{gap}の復帰と{days}日目が重なった!間があっても積み上げは減っていないから、堂々と祝おう。',
  '復帰の日が{days}日目の記念日!久しぶりでも、積み上げはちゃんとここに残ってるよ。',
]

/** 節目の見出し(`${days}日目` を含む)。 */
const MILESTONE_TITLES: ReadonlyArray<(days: number) => string> = [
  (days) => `${days}日目に到達!`,
  (days) => `${days}日目、おめでとう!`,
  (days) => `祝・${days}日目!`,
  (days) => `${days}日目だよ、すごい!`,
]

/** 節目ごとのひと言(各2候補)。 */
const MILESTONE_WORDS: Record<number, readonly string[]> = {
  3: ['3日は「習慣の芽」。もう立派なスタートだよ!', '3日ぶん!はじめた人が最初にくじける壁を、もう越えてるよ!'],
  5: ['5日ぶん!片手で数えられるところから、ちゃんと伸びてる!', '5日!1週間の入口だよ。いい弾みになってるね!'],
  7: ['1週間ぶんの日が集まったよ。いいリズムになってきたね!', '7日ぶん!まる1週間、英語がきみの中に続いてるよ!'],
  10: ['2ケタ突入!ここまで来たら、もう戻る必要なんてないよ!', '10日ぶん!2ケタの積み上げは、本物の習慣の入口だね!'],
  14: ['2週間ぶん!きみの毎日に、英語の場所ができてきたね。', '14日ぶん!2週間ずっと、よく続けてるね。たいした集中力だよ!'],
  20: ['20日ぶん!気づいたら当たり前になってきてない?', '20日!もう「特別なこと」じゃなくなってきた頃だね。'],
  30: ['30日ぶん=1か月分!おつかれさま。すごい積み上げだよ!', '1か月ぶんの日!これはもう、きちんとした習慣だよ!'],
  50: ['50日!100日が見えてきた!ここからが本番だよ!', '50日ぶん!100日まであと半分。いい走りだよ!'],
  75: ['75日ぶん!もうベテランの顔になってきたね!', '75日!3か月ぶんの積み上げ。自信を持っていいよ!'],
  100: ['100日!3ケタだよ!これはもう、きみの習慣だね!', '100日ぶん!3ケタの景色を見た人は少ないよ。誇っていい!'],
  150: ['150日ぶん!? ここまで来ると、やらない日を数えるほうが難しいよ!', '150日!もはや英語はきみの日常そのものだね!'],
  200: ['200日!積み上げ方が半端ない。イングバードも誇らしいよ!', '200日ぶん!この数字は、毎日の小さな決断の集まりだよ!'],
  250: ['250日ぶん!きみの中に、英語の土台ができてるよ!', '250日!ここまで続く人はなかなかいないよ。尊敬する!'],
  300: ['300日ぶん!あと少しで1年!すごい景色だよ!', '300日!1年が見えてきたね。ここからの1日も大事にしよう!'],
  365: ['365日ぶん=1年!? きみ、伝説だよ!', '1年ぶんの日!四季を一周して、ちゃんとここにいるね!'],
  500: ['500日ぶん!? ことばが出ないよ。すごすぎる!', '500日!もう数えるのをやめてもいいくらい、立派な積み上げだよ!'],
  730: ['730日ぶん=2年!? もう英語がきみの一部だね!', '2年ぶん!ここまで来ると、英語が生活の一部になってるね!'],
  1000: ['1000日ぶん=4ケタ!? イングバードは感涙だよ!', '4ケタの日!この積み上げは、きみの一生の財産だよ!'],
}

/** 専用のひと言が無い節目の定型文。 */
const MILESTONE_GENERIC: readonly string[] = [
  'トータル{days}日ぶんの英語が、きみの中に積み上がってるよ。えらい!',
  '{days}日ぶん!その1日ずつの合計が、今のきみを作ってるよ。',
  '祝{days}日!小さな1日の積み重ねが、こんなに大きくなったね。',
  '{days}日ぶんの積み上げに、イングバードから拍手を送るよ!',
]

function fill(text: string, values: Record<string, string>): string {
  return text.replace(/\{(\w+)\}/g, (_, key: string) => values[key] ?? '')
}

/**
 * いまの学習状況に合わせたほめ言葉。
 * 優先順位は「はじめて > 節目 > 久しぶり > 今日ぶん > 今日はもう学習ずみ > 今日はこれから」。
 * `justRecorded` は今まさに記録した直後かどうか(メッセージの言い回しだけが変わる)。
 * `rng` は言い回しと気分の抽選に使う。
 */
export function praiseFor(
  status: StudyStatus,
  justRecorded = false,
  rng: () => number = Math.random,
): Praise {
  const pick = <T>(items: readonly T[]): T => items[Math.min(items.length - 1, Math.floor(rng() * items.length))]
  const mood = (kind: PraiseKind): IngbirdMood => pick(MOOD_POOLS[kind])

  if (!status.studiedToday) {
    // 久しぶりでも、来た時点で歓迎する。まだ学習はこれからでも、来たことは勝利。
    if (status.daysSinceLast === null) {
      const [title, message] = pick(WELCOME_PRAISES)
      return { kind: 'encourage', mood: mood('encourage'), confetti: false, title, message }
    }
    if (status.daysSinceLast >= 3) {
      const gap = describeGap(status.daysSinceLast)
      return { kind: 'encourage', mood: mood('return'), confetti: false, title: pick(WELCOME_BACK_TITLES)(gap), message: pick(RETURN_BODIES) }
    }
    const [title, message] = pick(GENTLE_PRAISES)
    return { kind: 'encourage', mood: mood('encourage'), confetti: false, title, message }
  }

  if (status.totalDays === 1) {
    const [title, message] = pick(FIRST_PRAISES)
    return { kind: 'first', mood: mood('first'), confetti: true, title, message }
  }

  if (isMilestone(status.totalDays)) {
    const days = status.totalDays
    // 久しぶりの復帰と節目が重なった日は、両方を祝う(休んでいた日は減らないことも伝える)
    const back = (status.lastGap ?? 0) >= 3
    const message = back
      ? fill(pick(MILESTONE_BACK_BODIES), { gap: describeGap(status.lastGap ?? 0), days: String(days) })
      : fill(pick(MILESTONE_WORDS[days] ?? MILESTONE_GENERIC), { days: String(days) })
    return { kind: 'milestone', mood: mood('milestone'), confetti: true, title: pick(MILESTONE_TITLES)(days), message }
  }

  if ((status.lastGap ?? 0) >= 3) {
    const gap = describeGap(status.lastGap ?? 0)
    return { kind: 'return', mood: mood('return'), confetti: true, title: pick(RETURN_TITLES)(gap), message: pick(RETURN_BODIES) }
  }

  const [title, message] = pick(justRecorded ? DAILY_PRAISES : DONE_PRAISES)
  return {
    kind: justRecorded ? 'daily' : 'done',
    mood: mood(justRecorded ? 'daily' : 'done'),
    confetti: false,
    title,
    message,
  }
}
