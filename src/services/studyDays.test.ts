import { beforeEach, describe, expect, it, vi } from 'vitest'
import { KEYS, saveJson } from './storage'
import {
  STUDY_RECORDED_EVENT,
  getStudyDays,
  getStudyStatus,
  isMilestone,
  praiseFor,
  recordStudyDay,
} from './studyDays'

beforeEach(() => {
  localStorage.clear()
})

describe('学習日の記録(トータル)', () => {
  it('同じ日に何度記録しても1日として数える', () => {
    const first = recordStudyDay('2026-09-10')
    expect(first.status.totalDays).toBe(1)
    expect(first.praise.kind).toBe('first')

    const second = recordStudyDay('2026-09-10')
    expect(second.status.totalDays).toBe(1)
    expect(second.status.studiedToday).toBe(true)
    expect(getStudyDays()).toEqual(['2026-09-10'])
  })

  it('日をまたぐとトータルが増える(連続していなくても数える)', () => {
    recordStudyDay('2026-09-10')
    const next = recordStudyDay('2026-09-12') // 1日空いても日数は減らない
    expect(next.status.totalDays).toBe(2)
    expect(next.status.studiedToday).toBe(true)
    expect(next.status.daysSinceLast).toBe(0)
    expect(next.praise.kind).toBe('daily')
  })

  it('新しい学習日のときだけイベントで知らせる', () => {
    const listener = vi.fn()
    window.addEventListener(STUDY_RECORDED_EVENT, listener)
    try {
      recordStudyDay('2026-09-10')
      recordStudyDay('2026-09-10')
      recordStudyDay('2026-09-11')
    } finally {
      window.removeEventListener(STUDY_RECORDED_EVENT, listener)
    }
    expect(listener).toHaveBeenCalledTimes(2)
  })

  it('重複・不正な値・壊れたデータは無視する', () => {
    saveJson(KEYS.studyDays, ['2026-09-02', '2026-09-02', 'bad', 42, '2026-09-01'])
    expect(getStudyDays()).toEqual(['2026-09-01', '2026-09-02'])

    localStorage.setItem(KEYS.studyDays, '{not json')
    expect(getStudyDays()).toEqual([])
    expect(getStudyStatus('2026-09-10').totalDays).toBe(0)
  })

  it('記録がなければ0日から始まる', () => {
    const status = getStudyStatus('2026-09-10')
    expect(status.totalDays).toBe(0)
    expect(status.lastDate).toBeNull()
    expect(status.daysSinceLast).toBeNull()
    expect(status.next).toEqual({ at: 1, remaining: 1 })
    expect(praiseFor(status, false, () => 0).kind).toBe('encourage')
  })

  it('次の節目とそこまでの残り日数を示す', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03']) recordStudyDay(day)
    expect(getStudyStatus('2026-09-03').next).toEqual({ at: 5, remaining: 2 })
    expect(isMilestone(3)).toBe(true)
    expect(isMilestone(4)).toBe(false)
    expect(isMilestone(100)).toBe(true)
  })
})

describe('イングバードのほめ方', () => {
  it('節目は特別にほめる', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04']) recordStudyDay(day)
    const fifth = recordStudyDay('2026-09-05')
    expect(fifth.praise.kind).toBe('milestone')
    expect(fifth.praise.confetti).toBe(true)
    expect(fifth.praise.title).toContain('5日目')
  })

  it('久しぶりでも「来たこと」をほめる(連続日数は求めない)', () => {
    recordStudyDay('2026-09-01')
    const back = recordStudyDay('2026-09-06') // 5日ぶり
    expect(back.status.totalDays).toBe(2) // 空いた日は数えないし、減りもしない
    expect(back.status.lastGap).toBe(5)
    expect(back.praise.kind).toBe('return')
    expect(back.praise.title).toContain('5日ぶり')
    expect(back.praise.message).toContain('減らさない')
  })

  it('1か月ぶりは「1か月ぶり」と言う', () => {
    recordStudyDay('2026-09-01')
    const back = recordStudyDay('2026-10-01')
    expect(back.praise.title).toContain('1か月ぶり')
  })

  it('節目と久しぶりが重なったら節目を優先する', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04']) recordStudyDay(day)
    const fifth = recordStudyDay('2026-09-20') // 16日ぶりだが5日目
    expect(fifth.praise.kind).toBe('milestone')
  })

  it('学習ずみの日に再訪したら、それもほめる', () => {
    recordStudyDay('2026-09-10')
    recordStudyDay('2026-09-11')
    const praise = praiseFor(getStudyStatus('2026-09-11'), false, () => 0)
    expect(praise.kind).toBe('done')
    expect(praise.confetti).toBe(false)
  })

  it('まだ学習していない日は、久しぶりでも責めずに迎える', () => {
    recordStudyDay('2026-09-01')
    const status = getStudyStatus('2026-09-04') // 3日空けて訪問
    expect(status.studiedToday).toBe(false)
    expect(status.daysSinceLast).toBe(3)
    const praise = praiseFor(status, false, () => 0)
    expect(praise.kind).toBe('encourage')
    expect(praise.title).toContain('3日ぶり')
    expect(praise.confetti).toBe(false)
  })

  it('言い回しの抽選は候補の外を返さない', () => {
    recordStudyDay('2026-09-10')
    recordStudyDay('2026-09-11')
    const praise = praiseFor(getStudyStatus('2026-09-11'), true, () => 1) // rng が 1 を返しても範囲内
    expect(praise.kind).toBe('daily')
    expect(praise.title.length).toBeGreaterThan(0)
  })
})
