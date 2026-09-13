// 学習進捗のローカル永続化(文法の完了レッスン・文法問題のSRS・語彙統計・語彙の日次ログ)

import { KEYS, loadJson, saveJson } from './storage'
import { flushPush } from './sync'
import { masteryOf, recordAnswer } from './vocabSelection'
import type { WordStats } from './vocabSelection'

export function getCompletedLessons(): Set<string> {
  return new Set(loadJson<string[]>(KEYS.grammarProgress, []))
}

/**
 * 完了ボタンの操作。`completed=false` で取り消す。
 * セクション完了は区切りなので、保存の3秒まとめを待たずその場で Gist へ送る。
 */
export function markLessonCompleted(lessonId: string, completed = true): void {
  const lessons = getCompletedLessons()
  if (completed) lessons.add(lessonId)
  else lessons.delete(lessonId)
  saveJson(KEYS.grammarProgress, [...lessons])
  flushPush()
}

export function getGrammarItemStats(): WordStats {
  return loadJson<WordStats>(KEYS.grammarItemStats, {})
}

/**
 * 文法問題1問ぶんの正誤を記録する。設定ページの進捗集計とGist同期がこの `grammarItemStats` を読む。
 *
 * 置き場所が `practice.ts` ではなく進捗側なのは、`practice.ts` が文バンク(語彙・多読を含む)を
 * import しており、文法ページから読むとルート分割したチャンクに数百KB持ち込んでしまうため。
 */
export function recordGrammarItemAnswer(questionId: string, correct: boolean): void {
  saveJson(KEYS.grammarItemStats, recordAnswer(getGrammarItemStats(), questionId, correct))
}

export function getVocabStats(): WordStats {
  return loadJson<WordStats>(KEYS.vocabStats, {})
}

export function saveVocabStats(stats: WordStats): void {
  saveJson(KEYS.vocabStats, stats)
}

/** 1日1行の学習ログ。折れ線・棒グラフの元データ。 */
export type VocabDay = {
  /** YYYY-MM-DD */
  date: string
  /** その日に答えた語数 */
  count: number
  /** その日の終わりに定着していた語数 */
  mastered: number
}

/** 保持する日数。1日1行なので4か月分でも数KB。 */
const HISTORY_DAYS = 120

function dateString(d: Date): string {
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}

function todayString(): string {
  return dateString(new Date())
}

/** YYYY-MM-DD を days 日ずらす。月末・うるう年は Date に任せる。 */
export function shiftDate(date: string, days: number): string {
  const d = new Date(`${date}T00:00:00`)
  d.setDate(d.getDate() + days)
  return dateString(d)
}

export function getVocabHistory(): VocabDay[] {
  const raw = loadJson<VocabDay[]>(KEYS.vocabDaily, [])
  return Array.isArray(raw) ? raw : [] // 旧形式({date,count})は1日分なので捨てる
}

export function getTodayVocabCount(): number {
  const last = getVocabHistory().at(-1)
  return last?.date === todayString() ? last.count : 0
}

/** 1語答えるごとに呼ぶ。当日の行に練習語数を足し、その時点の定着語数で上書きする。 */
export function recordVocabAnswer(stats: WordStats): void {
  const days = getVocabHistory()
  const date = todayString()
  const mastered = Object.values(stats).filter((s) => masteryOf(s) === 'mastered').length
  const last = days.at(-1)
  if (last?.date === date) days[days.length - 1] = { date, count: last.count + 1, mastered }
  else days.push({ date, count: 1, mastered })
  saveJson(KEYS.vocabDaily, days.slice(-HISTORY_DAYS))
}

/**
 * 記録開始日(または maxDays 日前)から今日までを1日1行に埋めた系列。グラフの横軸用。
 * 記録のない日は練習0語とし、定着語数は前日の値を延長する。
 */
export function fillDays(days: readonly VocabDay[], maxDays: number, today: string = todayString()): VocabDay[] {
  if (days.length === 0) return []
  const earliest = shiftDate(today, -(maxDays - 1))
  const start = days[0].date > earliest ? days[0].date : earliest
  const byDate = new Map(days.map((d) => [d.date, d]))

  // 窓の外(start より前)の記録は、定着語数の始点としてだけ使う
  let mastered = 0
  for (const day of days) {
    if (day.date >= start) break
    mastered = day.mastered
  }

  const filled: VocabDay[] = []
  for (let date = start; date <= today; date = shiftDate(date, 1)) {
    const entry = byDate.get(date)
    if (entry) mastered = entry.mastered
    filled.push({ date, count: entry?.count ?? 0, mastered })
  }
  return filled
}
