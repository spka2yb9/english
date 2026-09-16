// 間隔反復によるセッション語彙の選択。
// シンプルで説明可能なスケジューリング(docs/learning-design.md 参照):
//   - 「わかる」が続くほど次の出題間隔を倍にする(1 → 2 → 4 → 8 … 日、上限60日)
//   - 「わからない」と答えた語は再学習中(lapsed)になり、日をまたがず次のセッションで最優先に戻る。
//     セッション内で「わかる」に変わっても、次のセッションでもう一度正解するまで再学習中のまま
//   - 予定日を過ぎた語だけを復習候補にし、残りは未出題語から補う
//   - 復習に使う枠は半分まで。残りは必ず未出題語(新出語)に回す
//   - 選ぶときにレベルを見て重み付けする(A2 → B1 → B2 の順に優先。`LEVEL_WEIGHTS`)。
//     新出語の先頭は一番低いレベルから取り、未出題の A2 が残っている限り必ず出る
//     復習の必要性(再学習中・予定日超過)はレベルより常に優先する

// node のスクリプト(--experimental-strip-types)からも読み込めるよう、拡張子を明示する。
import { shuffle, weightedSample } from './shuffle.ts'

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

/**
 * 出題のレベル重み。レベルの低い語ほど大きく、優先して出題される。
 * 対象プールの大半が B2 なので、語数差を打ち消す意図で A2 を B2 の3倍にしてある。
 */
export const LEVEL_WEIGHTS: Record<string, number> = { A2: 3, B1: 2, B2: 1 }

/** レベルが分からない語の重み。既存の均等抽選と同じ扱いになる。 */
const UNKNOWN_LEVEL_WEIGHT = 1

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
 * レベルを低い順に並べたもの。未出題語の枠はこの順に確保する。
 */
const LEVEL_ORDER = ['A2', 'B1', 'B2']

/**
 * 未出題語から slots 件を選ぶ。
 * 先頭の1語は「未出題が残っている一番低いレベル」から取り、残りはレベル重み付きの抽選で埋める。
 * levelOf を渡さないときは均等抽選。
 */
function pickNewWords(
  unseen: readonly string[],
  slots: number,
  weightOf: (id: string) => number,
  levelOf: ((id: string) => string | undefined) | undefined,
  rng: () => number,
): string[] {
  if (slots <= 0) return []
  if (!levelOf) return weightedSample(unseen, () => 1, slots, rng)
  const lowest = LEVEL_ORDER.find((level) => unseen.some((id) => levelOf(id) === level))
  if (lowest === undefined) return weightedSample(unseen, weightOf, slots, rng)
  const guaranteed = weightedSample(
    unseen.filter((id) => levelOf(id) === lowest),
    weightOf,
    1,
    rng,
  )
  const rest = unseen.filter((id) => !guaranteed.includes(id))
  return [...guaranteed, ...weightedSample(rest, weightOf, slots - guaranteed.length, rng)]
}

/**
 * セッションの語を選択する。
 * 復習(再学習中 → 予定日超過)に半分の枠を使い、残りは必ず未出題語(新出語)に回す。
 * 新出語の先頭は一番低いレベルから取り、残りはレベルの低い語ほど選ばれやすくする。
 * 予定日前の語は、それでも足りないときだけ補充する。
 */
export function selectSessionWords(
  allIds: readonly string[],
  stats: WordStats,
  now: number = Date.now(),
  count: number = SESSION_SIZE,
  rng: () => number = Math.random,
  levelOf?: (id: string) => string | undefined,
): string[] {
  const weightOf = (id: string) => {
    const level = levelOf?.(id)
    return (level !== undefined ? LEVEL_WEIGHTS[level] : undefined) ?? UNKNOWN_LEVEL_WEIGHT
  }
  const seen = allIds.filter((id) => stats[id])
  const unseen = allIds.filter((id) => !stats[id])

  // 同点候補を Fisher–Yates で先に混ぜてからスコア順にする。
  // sort の比較関数内で乱数を使うと推移律を壊し、偏りや実装依存の結果を生む。
  const scored = shuffle(seen, rng)
    .map((id) => ({
      id,
      score: reviewScore(stats[id], now),
      weight: weightOf(id),
      days: Math.max(0, (now - stats[id].lastAt) / DAY),
    }))
    .sort((a, b) => b.score - a.score)

  // 復習(再学習中+予定日超過)に使う枠の上限。残りは必ず未出題語に回す。
  // ここを上限なしにすると、再学習中の語が5語を占めて新出語が1語も出なくなる。
  const reviewSlots = Math.ceil(count / 2)

  // 再学習中(直近で「わからない」と答えた)語を枠の限り戻す。
  // 枠に全員収まるときは全員戻し、収まらないときはレベル重みに経過日数を掛けて選ぶ。
  const lapsed = scored.filter((c) => isLapsed(stats[c.id]))
  const picked =
    lapsed.length <= reviewSlots
      ? lapsed.map((c) => c.id)
      : weightedSample(lapsed, (c) => c.weight * (1 + c.days), reviewSlots, rng).map((c) => c.id)
  // 予定日を過ぎた語は、残りの復習枠にレベルの低い語から入れる。
  const due = scored
    .filter((c) => c.score >= 1 && !isLapsed(stats[c.id]))
    .sort((a, b) => b.weight - a.weight || b.score - a.score)
  picked.push(...due.slice(0, Math.max(0, reviewSlots - picked.length)).map((c) => c.id))
  // 残りの枠は未出題語。先頭は一番低いレベル(A2 → B1 → B2)の語を確保する。
  picked.push(...pickNewWords(unseen, count - picked.length, weightOf, levelOf, rng))

  // まだ足りなければ、予定日前の語もレベルの低い語から、延滞している順に補充する
  const pickedIds = new Set(picked)
  const surplus = [...scored].sort((a, b) => b.weight - a.weight || b.score - a.score)
  for (const candidate of surplus) {
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
