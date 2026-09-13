import { beforeEach, describe, expect, it } from 'vitest'
import {
  poolFor,
  recordPracticeAnswer,
  selectPracticeSentences,
  getPracticeStats,
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

describe('音声練習セッション', () => {
  beforeEach(() => localStorage.clear())

  it('指定件数の文を重複なく返す', () => {
    const picked = selectPracticeSentences('dictation', 8)
    expect(picked).toHaveLength(8)
    expect(new Set(picked.map((s) => s.id)).size).toBe(8)
  })

  it('回答を記録するとSRSの履歴が残る', () => {
    recordPracticeAnswer('dictation', 'v:abandon', true)
    expect(getPracticeStats('dictation')['v:abandon']).toMatchObject({ seen: 1, known: 1, streak: 1 })
  })
})
