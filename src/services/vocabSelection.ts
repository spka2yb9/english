// 間隔反復によるセッション語彙の選択。
// シンプルで説明可能なスケジューリング(docs/learning-design.md 参照):
//   - 「わかる」が続くほど次の出題間隔を倍にする(1 → 2 → 4 → 8 … 日、上限60日)
//   - 「わからない」と答えた語は再学習中(lapsed)になり、日をまたがず次のセッションで最優先に戻る。
//     セッション内で「わかる」に変わっても、次のセッションでもう一度正解するまで再学習中のまま
//   - 予定日を過ぎた語だけを復習候補にし、残りは未出題語から補う

import { shuffle, sample } from './shuffle'

export type WordStat = {
  seen: number
  known: number
  unknown: number
  /** epoch ms */
  lastAt: number
  /** 連続で「わかる」と答えた回数。次の出題間隔を決める。 */
  streak?: number
  /** 再学習中。「わからない」で立ち、別セッションでもう一度正解すると降りる。 */
  lapsed?: boolean
}

export type WordStats = Record<string, WordStat>

export const SESSION_SIZE = 5

const DAY = 86_400_000
const FIRST_INTERVAL_DAYS = 1
const MAX_INTERVAL_DAYS = 60
/** 再学習を抜けるのに必要な連続正解数。1回目はわからなかった直後の周回で稼げてしまうため2。 */
const RELEARN_STREAK = 2
/** 再学習中の語に与える優先度。延滞スコア(日数/間隔)より確実に大きい値。 */
const LAPSE_SCORE = 1000

/** streak 未記録の古い履歴は正誤の差から推定する。 */
function streakOf(stat: WordStat): number {
  return stat.streak ?? Math.max(0, stat.known - stat.unknown)
}

/** 次の出題までの日数。連続正解ごとに倍増する。 */
export function intervalDays(stat: WordStat): number {
  return Math.min(FIRST_INTERVAL_DAYS * 2 ** streakOf(stat), MAX_INTERVAL_DAYS)
}

/** 再学習中(直近で「わからない」と答え、まだ抜けていない)か。 */
export function isLapsed(stat: WordStat): boolean {
  return stat.lapsed === true
}

export type Mastery = 'mastered' | 'learning' | 'weak'

/** 定着とみなす連続正解数。3回で次の出題が8日後になり、短期記憶では答えられない。 */
const MASTERED_STREAK = 3

/** 進捗表示用の3分類。出題の選択には使わない。 */
export function masteryOf(stat: WordStat): Mastery {
  if (isLapsed(stat) || stat.unknown > stat.known) return 'weak'
  return streakOf(stat) >= MASTERED_STREAK ? 'mastered' : 'learning'
}

/**
 * 復習優先度。1.0 で予定日ちょうど、1.0未満はまだ早い、大きいほど延滞している。
 * 再学習中の語は間隔を待たず常に最優先(古い取りこぼしほど上)。
 */
export function reviewScore(stat: WordStat, now: number): number {
  const days = Math.max(0, (now - stat.lastAt) / DAY)
  if (isLapsed(stat)) return LAPSE_SCORE + days
  return days / intervalDays(stat)
}

/**
 * セッションの語を選択する。
 * 再学習中の語を上限なしで先に入れ、予定日を過ぎた語で半分まで埋め、残りを未出題語から選ぶ。
 * 未出題語が尽きたら、予定日前の語も延滞順に補充する。
 */
export function selectSessionWords(
  allIds: readonly string[],
  stats: WordStats,
  now: number = Date.now(),
  count: number = SESSION_SIZE,
  rng: () => number = Math.random,
): string[] {
  const seen = allIds.filter((id) => stats[id])
  const unseen = allIds.filter((id) => !stats[id])

  // 同点候補を Fisher–Yates で先に混ぜてからスコア順にする。
  // sort の比較関数内で乱数を使うと推移律を壊し、偏りや実装依存の結果を生む。
  const scored = shuffle(seen, rng)
    .map((id) => ({ id, score: reviewScore(stats[id], now) }))
    .sort((a, b) => b.score - a.score)

  // 再学習中(直近で「わからない」と答えた)語は、新出語の枠を削ってでも次のセッションに戻す
  const picked = scored
    .filter((c) => isLapsed(stats[c.id]))
    .slice(0, count)
    .map((c) => c.id)
  const due = scored.filter((c) => c.score >= 1 && !isLapsed(stats[c.id]))
  picked.push(...due.slice(0, Math.max(0, Math.ceil(count / 2) - picked.length)).map((c) => c.id))
  picked.push(...sample(unseen, Math.max(0, count - picked.length), rng))

  // まだ足りなければ、予定日前の語も延滞している順に補充する
  const pickedIds = new Set(picked)
  for (const candidate of scored) {
    if (picked.length >= count) break
    if (pickedIds.has(candidate.id)) continue
    picked.push(candidate.id)
    pickedIds.add(candidate.id)
  }

  return shuffle(picked, rng)
}

export function recordAnswer(stats: WordStats, id: string, known: boolean, now: number = Date.now()): WordStats {
  const prev = stats[id] ?? { seen: 0, known: 0, unknown: 0, lastAt: 0 }
  const streak = known ? streakOf(prev) + 1 : 0
  return {
    ...stats,
    [id]: {
      seen: prev.seen + 1,
      known: prev.known + (known ? 1 : 0),
      unknown: prev.unknown + (known ? 0 : 1),
      lastAt: now,
      streak,
      // セッション内の再出題で「わかる」になっただけでは抜けない(RELEARN_STREAK 回で降りる)
      lapsed: known ? isLapsed(prev) && streak < RELEARN_STREAK : true,
    },
  }
}
