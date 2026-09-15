import { beforeEach, describe, expect, it } from 'vitest'
import { KEYS } from './storage'
import {
  drawPracticeSentence,
  getPracticeStats,
  poolFor,
  recordPracticeAnswer,
} from './practice'

describe('音声練習の母集団', () => {
  it('ディクテーションはTTSで安定して読める文だけを使う', () => {
    const pool = poolFor('dictation')
    expect(pool.length).toBeGreaterThan(500)
    expect(pool.every((s) => !/[0-9]/.test(s.en))).toBe(true)
    expect(pool.every((s) => s.en.split(' ').length <= 14)).toBe(true)
  })

  it('音読は全文が対象', () => {
    expect(poolFor('shadowing').length).toBeGreaterThan(poolFor('dictation').length)
  })
})

describe('音声練習の出題', () => {
  beforeEach(() => localStorage.clear())

  it('実施回数の少ない文から順に出す(1周目は未実施の文だけ)', () => {
    const pool = poolFor('dictation')
    const stats = { [pool[0].id]: 1, [pool[1].id]: 1 }
    const done = new Set([pool[0].id, pool[1].id])
    for (let i = 0; i < 20; i++) {
      const sentence = drawPracticeSentence('dictation', stats)
      expect(sentence && done.has(sentence.id)).toBe(false)
    }
  })

  it('同じ文が2問続かない', () => {
    const pool = poolFor('dictation')
    const first = drawPracticeSentence('dictation', {}, () => 0)
    expect(first?.id).toBe(pool[0].id)
    // pool[0] は実施回数1、ほかは0なので候補から外れる
    const second = drawPracticeSentence('dictation', { [pool[0].id]: 1 }, () => 0)
    expect(second?.id).toBe(pool[1].id)
  })

  it('全員が同じ回数になったら次の周が始まる', () => {
    const pool = poolFor('dictation')
    const stats = Object.fromEntries(pool.map((s) => [s.id, 1]))
    expect(drawPracticeSentence('dictation', stats, () => 0)?.id).toBe(pool[0].id)
  })

  it('記録するのは実施回数だけ', () => {
    recordPracticeAnswer('dictation', 'v:abandon')
    recordPracticeAnswer('dictation', 'v:abandon')
    expect(getPracticeStats('dictation')['v:abandon']).toBe(2)
    expect(localStorage.getItem(`${KEYS.practiceStats}.dictation`)).toBe('{"v:abandon":2}')
  })

  it('旧形式(WordStatオブジェクト)の履歴は実施回数として読み替える', () => {
    localStorage.setItem(`${KEYS.practiceStats}.dictation`, JSON.stringify({ 'v:abandon': { seen: 3, known: 2 } }))
    expect(getPracticeStats('dictation')['v:abandon']).toBe(3)
  })
})
