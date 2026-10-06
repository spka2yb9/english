// イングバードのつぶやき抽選の検証。
// 種類の巡り方・一巡するまでの重複のなさ・状況に合わせた励まし・決定性を見る。

import { describe, expect, it } from 'vitest'
import { PHRASES, TIP_LINES } from '../content/ingbird/talk'
import { ENCOURAGE_BODIES } from '../content/ingbird/encouragement'
import {
  createTalkState,
  encourageBranch,
  firstTalk,
  nextTalk,
  timeBucket,
  type TalkState,
} from './ingbirdTalk'
import type { StudyStatus } from './studyDays'
import type { TalkLine } from '../content/ingbird/types'

function status(partial: Partial<StudyStatus> = {}): StudyStatus {
  return {
    totalDays: 10,
    studiedToday: true,
    lastDate: '2026-01-10',
    daysSinceLast: 0,
    lastGap: 1,
    next: { at: 14, remaining: 4 },
    ...partial,
  }
}

/** テスト用の決定的な乱数(サービス本体と同じ実装を小さく持つ)。 */
function mulberry32(seed: number): () => number {
  let a = seed >>> 0
  return () => {
    a = (a + 0x6d2b79f5) >>> 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

function drawMany(count: number, state: TalkState = createTalkState(), studyStatus = status(), hour = 10): TalkLine[] {
  const rng = mulberry32(20261006)
  return Array.from({ length: count }, () => nextTalk(state, studyStatus, hour, rng))
}

describe('時間帯と状況の分岐', () => {
  it('時間帯は朝・昼・夕・夜に分かれる', () => {
    expect(timeBucket(5)).toBe('morning')
    expect(timeBucket(10)).toBe('morning')
    expect(timeBucket(11)).toBe('day')
    expect(timeBucket(16)).toBe('day')
    expect(timeBucket(17)).toBe('evening')
    expect(timeBucket(21)).toBe('evening')
    expect(timeBucket(22)).toBe('night')
    expect(timeBucket(4)).toBe('night')
  })

  it('学習状況から励ましの型を選ぶ', () => {
    expect(encourageBranch(status({ totalDays: 0, studiedToday: false, lastDate: null, daysSinceLast: null, lastGap: null }))).toBe('noDays')
    expect(encourageBranch(status({ studiedToday: true, lastGap: 1 }))).toBe('todayDone')
    expect(encourageBranch(status({ studiedToday: true, lastGap: 9 }))).toBe('backDone')
    expect(encourageBranch(status({ studiedToday: false, daysSinceLast: 0, lastGap: 1 }))).toBe('todayNotYet')
    expect(encourageBranch(status({ studiedToday: false, daysSinceLast: 5 }))).toBe('back')
  })
})

describe('つぶやきの抽選', () => {
  it('最初は必ず励ましから始める', () => {
    const line = nextTalk(createTalkState(), status())
    expect(line.kind).toBe('encourage')
    expect(line.text.length).toBeGreaterThan(5)
  })

  it('画面を開いたときのひとことは、進捗に合わせた本文から必ず選ぶ', () => {
    const fresh = status({ totalDays: 0, studiedToday: false, lastDate: null, daysSinceLast: null, lastGap: null })
    const first = firstTalk(createTalkState(), fresh, mulberry32(1))
    expect(first.kind).toBe('encourage')
    expect(first.id.startsWith('c-noDays-')).toBe(true)
    expect(first.text.includes('{')).toBe(false)

    const done = status({ totalDays: 7, studiedToday: true, lastGap: 1 })
    const second = firstTalk(createTalkState(), done, mulberry32(2))
    expect(second.id.startsWith('c-todayDone-')).toBe(true)

    const back = status({ totalDays: 30, studiedToday: false, daysSinceLast: 10, lastGap: 1 })
    const third = firstTalk(createTalkState(), back, mulberry32(3))
    expect(third.id.startsWith('c-back-')).toBe(true)
  })

  it('励まし・フレーズ・コツの3種類が混ざり、偏りすぎない', () => {
    const lines = drawMany(600)
    const count = { encourage: 0, tip: 0, phrase: 0 }
    for (const line of lines) count[line.kind] += 1
    expect(count.encourage, '励まし').toBeGreaterThan(150)
    expect(count.phrase, 'フレーズ').toBeGreaterThan(150)
    expect(count.tip, 'コツ').toBeGreaterThan(50)
    // 同じ種類が連続しない(山札の作り直しと入れ替えで避ける)
    for (let i = 1; i < lines.length; i += 1) {
      expect(lines[i].kind === lines[i - 1].kind, `${i}番目で同じ種類が連続`).toBe(false)
    }
  })

  it('フレーズは一巡するまで同じものを出さない', () => {
    const phrases = drawMany(4000).filter((line) => line.kind === 'phrase')
    expect(phrases.length).toBeGreaterThanOrEqual(PHRASES.length)
    const firstCycle = phrases.slice(0, PHRASES.length)
    expect(new Set(firstCycle.map((line) => line.id)).size).toBe(PHRASES.length)
  })

  it('コツも一巡するまで同じものを出さない', () => {
    const tips = drawMany(3000).filter((line) => line.kind === 'tip')
    expect(tips.length).toBeGreaterThanOrEqual(TIP_LINES.length)
    expect(new Set(tips.slice(0, TIP_LINES.length).map((line) => line.id)).size).toBe(TIP_LINES.length)
  })

  it('フレーズには英文・和訳・使いどころ・読み上げがそろう', () => {
    const phrase = drawMany(40).find((line) => line.kind === 'phrase')
    expect(phrase).toBeDefined()
    expect(phrase!.text.length).toBeGreaterThan(2)
    expect(phrase!.ja!.length).toBeGreaterThan(1)
    expect(phrase!.note!.length).toBeGreaterThan(5)
    expect(phrase!.scene!.length).toBeGreaterThan(1)
    expect(phrase!.speech).toEqual({ text: phrase!.text, locale: 'en-US' })
  })

  it('励ましとコツは日本語で、プレースホルダが残らない', () => {
    for (const line of drawMany(400)) {
      if (line.kind === 'phrase') continue
      expect(line.speech, line.id).toBeUndefined()
      expect(line.text.includes('{'), `${line.id}: ${line.text}`).toBe(false)
      expect(line.text.length, line.id).toBeGreaterThan(5)
      expect(line.text.length, line.id).toBeLessThanOrEqual(160)
    }
  })

  it('久しぶりの日は「N日ぶり」を織り込んで励ます', () => {
    const cold = status({ totalDays: 20, studiedToday: false, daysSinceLast: 8, lastGap: 1 })
    const lines = drawMany(300, createTalkState(), cold)
    const composed = lines.filter((line) => line.id.startsWith('c-back-'))
    expect(composed.length).toBeGreaterThan(0)
    expect(composed.some((line) => line.text.includes('週間ぶり'))).toBe(true)
    for (const line of composed) expect(line.text.includes('{'), line.text).toBe(false)
  })

  it('節目を使い切った後でも、空欄のない励ましを返す', () => {
    const endgame = status({ totalDays: 1200, studiedToday: false, daysSinceLast: 1, lastGap: 1, next: null })
    for (const line of drawMany(300, createTalkState(), endgame)) {
      expect(line.text.includes('{'), `${line.id}: ${line.text}`).toBe(false)
    }
  })

  it('0日目の人には、はじまりの励ましを返す', () => {
    const fresh = status({ totalDays: 0, studiedToday: false, lastDate: null, daysSinceLast: null, lastGap: null })
    const lines = drawMany(200, createTalkState(), fresh)
    const composed = lines.filter((line) => line.id.startsWith('c-noDays-'))
    expect(composed.length).toBeGreaterThan(0)
    for (const line of composed) {
      const body = ENCOURAGE_BODIES.noDays.find((text) => line.text.startsWith(text))
      expect(body, line.text).toBeDefined()
    }
  })

  it('同じ状態と乱数なら、同じ順番で話す(決定的)', () => {
    const a = drawMany(60, createTalkState())
    const b = drawMany(60, createTalkState())
    expect(a.map((line) => line.id)).toEqual(b.map((line) => line.id))
    expect(a.map((line) => line.text)).toEqual(b.map((line) => line.text))
  })
})
