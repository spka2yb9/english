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

  it('節目と久しぶりが重なったら節目を優先し、復帰も祝う', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04']) recordStudyDay(day)
    const fifth = recordStudyDay('2026-09-20') // 16日ぶりだが5日目
    expect(fifth.praise.kind).toBe('milestone')
    expect(fifth.praise.title).toContain('5日目')
    expect(fifth.praise.message).toContain('復帰')
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

describe('イングバードの気分と豊富な言い回し', () => {
  const titlesFor = (make: (rng: () => number) => { title: string; mood: string }, samples = 20): { titles: Set<string>; moods: Set<string> } => {
    const titles = new Set<string>()
    const moods = new Set<string>()
    for (let index = 0; index < samples; index += 1) {
      const praise = make(() => index / samples)
      titles.add(praise.title)
      moods.add(praise.mood)
    }
    return { titles, moods }
  }

  it('今日ぶんの日は、多くの言い回しと気分から選ぶ', () => {
    recordStudyDay('2026-09-10')
    recordStudyDay('2026-09-11')
    const status = getStudyStatus('2026-09-11')
    const { titles, moods } = titlesFor((rng) => praiseFor(status, true, rng))
    expect(titles.size).toBeGreaterThanOrEqual(10)
    expect([...moods].every((mood) => ['cheer', 'happy', 'proud', 'sing'].includes(mood))).toBe(true)
    expect(moods.size).toBeGreaterThanOrEqual(3)
  })

  it('0日の日は、はじめの1日を誘う候補をたくさん持つ', () => {
    const status = getStudyStatus('2026-09-10')
    const { titles, moods } = titlesFor((rng) => praiseFor(status, false, rng))
    expect(titles.size).toBeGreaterThanOrEqual(8)
    expect([...moods].every((mood) => ['curious', 'wave', 'happy', 'think'].includes(mood))).toBe(true)
  })

  it('少しあいた日も、責めずに誘う候補を持っている', () => {
    recordStudyDay('2026-09-09')
    const status = getStudyStatus('2026-09-10') // 1日あけて、今日はまだ
    expect(status.daysSinceLast).toBe(1)
    const { titles } = titlesFor((rng) => praiseFor(status, false, rng))
    expect(titles.size).toBeGreaterThanOrEqual(8)
  })

  it('久しぶりの復帰は、どの言い回しでも「減らさない」ことを伝える', () => {
    recordStudyDay('2026-09-01')
    recordStudyDay('2026-09-10') // 9日ぶり
    const status = getStudyStatus('2026-09-10')
    expect(status.lastGap).toBe(9)
    for (let index = 0; index < 20; index += 1) {
      const praise = praiseFor(status, true, () => index / 20)
      expect(praise.kind).toBe('return')
      expect(praise.title).toContain('1週間ぶり')
      expect(praise.message).toContain('減らさない')
      expect(['wave', 'happy', 'proud']).toContain(praise.mood)
    }
  })

  it('節目は何度でも特別で、言い回しも気分も複数ある', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04']) recordStudyDay(day)
    recordStudyDay('2026-09-05')
    const status = getStudyStatus('2026-09-05')
    const { titles } = titlesFor((rng) => praiseFor(status, true, rng))
    expect(titles.size).toBeGreaterThanOrEqual(2)
    for (let index = 0; index < 20; index += 1) {
      const praise = praiseFor(status, true, () => index / 20)
      expect(praise.kind).toBe('milestone')
      expect(praise.title).toContain('5日目')
      expect(['party', 'proud', 'cheer']).toContain(praise.mood)
    }
  })

  it('復帰と節目が重なった日は、どの言い回しでも復帰を祝う', () => {
    for (const day of ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04']) recordStudyDay(day)
    const status = recordStudyDay('2026-09-20').status // 16日ぶりに5日目
    expect(status.totalDays).toBe(5)
    expect(status.lastGap).toBe(16)
    for (let index = 0; index < 20; index += 1) {
      const praise = praiseFor(status, true, () => index / 20)
      expect(praise.kind).toBe('milestone')
      expect(praise.title).toContain('5日目')
      expect(praise.message).toContain('復帰')
    }
  })
})
