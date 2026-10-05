// 学習した日の記録(トータル)と、マスコット「イングバード」のほめ言葉。
//
// 数えるのは「何かしら学習した日」の合計で、連続日数(ストリーク)ではない。
// 休んだ日で減るものが無いので、久しぶりの学習も「来たこと」自体をほめられる。
// 記録は1日1エントリ(YYYY-MM-DD の配列)。1件13バイトなので、年単位でも数KBにしかならない。

import { daysBetween, todayString } from './dates'
import { KEYS, loadJson, saveJson } from './storage'

/** recordStudyDay が新しい学習日を記録したときに発火する。detail は StudyRecord。 */
export const STUDY_RECORDED_EVENT = 'eng:study-recorded'

export type PraiseKind = 'first' | 'milestone' | 'return' | 'daily' | 'done' | 'encourage'

export type Praise = {
  kind: PraiseKind
  title: string
  message: string
  /** 紙吹雪を出すか(はじめての日・節目・久しぶり) */
  confetti: boolean
  /** マスコットの動き */
  mood: 'idle' | 'happy' | 'cheer'
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
function describeGap(gap: number): string {
  if (gap < 7) return `${gap}日ぶり`
  if (gap < 30) return `${Math.floor(gap / 7)}週間ぶり`
  if (gap < 365) return `${Math.floor(gap / 30)}か月ぶり`
  return `${Math.floor(gap / 365)}年ぶり`
}

/** 節目ごとのひと言。無い節目は「トータルN日」の定型文でほめる。 */
const MILESTONE_WORDS: Record<number, string> = {
  3: '3日は「習慣の芽」。もう立派なスタートだよ!',
  5: '5日ぶん!片手で数えられるところから、ちゃんと伸びてる!',
  7: '1週間ぶんの日が集まったよ。いいリズムになってきたね!',
  10: '2ケタ突入!ここまで来たら、もう戻る必要なんてないよ!',
  14: '2週間ぶん!きみの毎日に、英語の場所ができてきたね。',
  20: '20日ぶん!気づいたら当たり前になってきてない?',
  30: '30日ぶん=1か月分!おつかれさま。すごい積み上げだよ!',
  50: '50日!100日が見えてきた!ここからが本番だよ!',
  75: '75日ぶん!もうベテランの顔になってきたね!',
  100: '100日!3ケタだよ!これはもう、きみの習慣だね!',
  150: '150日ぶん!? ここまで来ると、やらない日を数えるほうが難しいよ!',
  200: '200日!積み上げ方が半端ない。イングバードも誇らしいよ!',
  250: '250日ぶん!きみの中に、英語の土台ができてるよ!',
  300: '300日ぶん!あと少しで1年!すごい景色だよ!',
  365: '365日ぶん=1年!? きみ、伝説だよ!',
  500: '500日ぶん!? ことばが出ないよ。すごすぎる!',
  730: '730日ぶん=2年!? もう英語がきみの一部だね!',
  1000: '1000日ぶん=4ケタ!? イングバードは感涙だよ!',
}

/**
 * いまの学習状況に合わせたほめ言葉。
 * 優先順位は「はじめて > 節目 > 久しぶり > 今日ぶん > 今日はもう学習ずみ > 今日はこれから」。
 * `justRecorded` は今まさに記録した直後かどうか(メッセージの言い回しだけが変わる)。
 * `rng` を使い回しの少ない言い回しの抽選に使う。
 */
export function praiseFor(
  status: StudyStatus,
  justRecorded = false,
  rng: () => number = Math.random,
): Praise {
  const pick = <T>(items: readonly T[]): T => items[Math.min(items.length - 1, Math.floor(rng() * items.length))]

  if (!status.studiedToday) {
    // 久しぶりでも、来た時点で歓迎する。まだ学習はこれからでも、来たことは勝利。
    if ((status.daysSinceLast ?? 0) >= 3) {
      return {
        kind: 'encourage',
        mood: 'happy',
        confetti: false,
        title: `${describeGap(status.daysSinceLast ?? 0)}だね、待ってたよ!`,
        message: '来てくれただけで、もう今日の勝利。1問から、いっしょにやろう!',
      }
    }
    const [title, message] = pick(ENCOURAGE_PRAISES)
    return { kind: 'encourage', mood: 'happy', confetti: false, title, message }
  }

  if (status.totalDays === 1) {
    return {
      kind: 'first',
      mood: 'cheer',
      confetti: true,
      title: '1日目、はじまった!',
      message: 'これがきみの最初の学習日。1日でもやったら、それはもう積み上がってるんだよ。',
    }
  }

  if (isMilestone(status.totalDays)) {
    // 久しぶりの復帰と節目が重なった日は、両方を祝う(休んでいた日は減らないことも伝える)
    const back = (status.lastGap ?? 0) >= 3
    return {
      kind: 'milestone',
      mood: 'cheer',
      confetti: true,
      title: `${status.totalDays}日目に到達!`,
      message: back
        ? `${describeGap(status.lastGap ?? 0)}の復帰で、しかも${status.totalDays}日目!休んでいた日は、ここまでの記録を1日も減らしていないよ。`
        : (MILESTONE_WORDS[status.totalDays] ??
          `トータル${status.totalDays}日ぶんの英語が、きみの中に積み上がってるよ。えらい!`),
    }
  }

  if ((status.lastGap ?? 0) >= 3) {
    return {
      kind: 'return',
      mood: 'cheer',
      confetti: true,
      title: `${describeGap(status.lastGap ?? 0)}!おかえり!`,
      message: '久しぶりでも、来ただけで今日は花丸。休んでいた日は、これまでの日を1日も減らさないよ。',
    }
  }

  const [title, message] = pick(justRecorded ? DAILY_PRAISES : DONE_PRAISES)
  return {
    kind: justRecorded ? 'daily' : 'done',
    mood: justRecorded ? 'cheer' : 'happy',
    confetti: false,
    title,
    message,
  }
}

const DAILY_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日の1日ぶん、ゲット!', 'やったね!1問でも1セッションでも、今日もちゃんと前に進んでる。えらい!'],
  ['きた!今日も学習日!', 'その1日はきみのもの。積み上がった日は、あとから消えないよ。'],
  ['Nice! 今日もいけたね!', '小さくても、やった日はやった日。いいペースだよ!'],
]

const DONE_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日はもう学習ずみ!', 'のぞきに来てくれてうれしいな。明日も1問でいいからね。'],
  ['今日のぶんは、もう積み上がってる!', 'まだやる?それなら大歓迎。もっと大きくなっちゃうね!'],
]

const ENCOURAGE_PRAISES: ReadonlyArray<readonly [string, string]> = [
  ['今日はまだ、これから!', '1問だけでも、今日は学習日になるよ。まずは1つ、いってみる?'],
  ['会いに来てくれてありがとう', '連続じゃなくてトータルだから、休んだ日で減るものはないよ。1問やってみる?'],
]
