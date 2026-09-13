import { beforeEach, describe, expect, it } from 'vitest'
import {
  fillDays,
  getCompletedLessons,
  getTodayVocabCount,
  getVocabHistory,
  getVocabStats,
  markLessonCompleted,
  recordVocabAnswer,
  saveVocabStats,
  shiftDate,
} from './progress'
import { KEYS, loadJson } from './storage'

beforeEach(() => {
  localStorage.clear()
})

describe('文法進捗の永続化', () => {
  it('完了レッスンを保存・復元できる', () => {
    expect(getCompletedLessons().size).toBe(0)
    markLessonCompleted('u01-l1')
    markLessonCompleted('u01-l2')
    markLessonCompleted('u01-l1') // 重複はセットに吸収される
    const completed = getCompletedLessons()
    expect(completed.size).toBe(2)
    expect(completed.has('u01-l1')).toBe(true)
  })

  it('完了を取り消せる', () => {
    markLessonCompleted('u01-l1')
    markLessonCompleted('u01-l1', false)
    expect(getCompletedLessons().has('u01-l1')).toBe(false)
  })

  it('破損データでも空状態にフォールバックする', () => {
    localStorage.setItem(KEYS.grammarProgress, '{not json')
    expect(getCompletedLessons().size).toBe(0)
  })
})

describe('語彙統計の永続化', () => {
  it('stats を保存・復元できる', () => {
    saveVocabStats({ achieve: { seen: 2, known: 1, unknown: 1, lastAt: 123 } })
    expect(getVocabStats().achieve.unknown).toBe(1)
  })

  it('答えるたびに当日の練習数と定着語数を記録する', () => {
    expect(getTodayVocabCount()).toBe(0)
    recordVocabAnswer({ a: { seen: 3, known: 3, unknown: 0, lastAt: 1, streak: 3 } })
    recordVocabAnswer({
      a: { seen: 3, known: 3, unknown: 0, lastAt: 1, streak: 3 },
      b: { seen: 1, known: 0, unknown: 1, lastAt: 2, streak: 0, lapsed: true },
    })
    expect(getTodayVocabCount()).toBe(2)
    const history = getVocabHistory()
    expect(history).toHaveLength(1) // 同じ日は1行にまとまる
    expect(history[0].mastered).toBe(1) // b は苦手なので定着に入らない
  })

  it('日付が変わると今日の練習数は0から始まる', () => {
    localStorage.setItem(KEYS.vocabDaily, JSON.stringify([{ date: '2000-01-01', count: 99, mastered: 5 }]))
    expect(getTodayVocabCount()).toBe(0)
  })

  it('旧形式の日次データは捨てて空の履歴にする', () => {
    localStorage.setItem(KEYS.vocabDaily, JSON.stringify({ date: '2000-01-01', count: 99 }))
    expect(getVocabHistory()).toEqual([])
    expect(getTodayVocabCount()).toBe(0)
  })
})

describe('グラフ用の日次系列', () => {
  const days = [
    { date: '2026-08-30', count: 10, mastered: 4 },
    { date: '2026-09-02', count: 5, mastered: 9 },
  ]

  it('記録のない日を埋め、定着語数は前日の値を延長する', () => {
    expect(fillDays(days, 30, '2026-09-03')).toEqual([
      { date: '2026-08-30', count: 10, mastered: 4 },
      { date: '2026-08-31', count: 0, mastered: 4 },
      { date: '2026-09-01', count: 0, mastered: 4 },
      { date: '2026-09-02', count: 5, mastered: 9 },
      { date: '2026-09-03', count: 0, mastered: 9 },
    ])
  })

  it('maxDays より古い記録は窓の外に出し、定着語数の始点として引き継ぐ', () => {
    const series = fillDays(days, 2, '2026-09-03')
    expect(series.map((d) => d.date)).toEqual(['2026-09-02', '2026-09-03'])
    expect(series[0].mastered).toBe(9)
  })

  it('記録が1日もなければ空を返す', () => {
    expect(fillDays([], 30, '2026-09-03')).toEqual([])
  })

  it('月をまたぐ日付をずらせる', () => {
    expect(shiftDate('2026-03-01', -1)).toBe('2026-02-28')
    expect(shiftDate('2024-02-28', 1)).toBe('2024-02-29') // うるう年
  })
})

describe('loadJson', () => {
  it('未保存キーはフォールバックを返す', () => {
    expect(loadJson('missing-key', 'fallback')).toBe('fallback')
  })
})
