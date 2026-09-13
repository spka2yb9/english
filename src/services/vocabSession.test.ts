import { describe, expect, it } from 'vitest'
import { answer, currentWordId, startSession, type VocabSessionState } from './vocabSession'

const TEN = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10']

/** known/unknown のパターンで1周分回答する */
function answerRound(state: VocabSessionState, knownFor: (id: string) => boolean): VocabSessionState {
  let s = state
  const round = s.round
  while (!s.finished && s.round === round) {
    const id = currentWordId(s)!
    s = answer(s, knownFor(id))
  }
  return s
}

describe('vocabSession', () => {
  it('10語で開始し、最初の語を出題する', () => {
    const s = startSession(TEN)
    expect(s.round).toBe(1)
    expect(s.queue).toHaveLength(10)
    expect(s.finished).toBe(false)
    expect(currentWordId(s)).toBe('w1')
  })

  it('空リストなら即座に完了', () => {
    const s = startSession([])
    expect(s.finished).toBe(true)
    expect(currentWordId(s)).toBeNull()
  })

  it('全問わかる → 1周で完了', () => {
    const s = answerRound(startSession(TEN), () => true)
    expect(s.finished).toBe(true)
    expect(s.round).toBe(1)
    expect(s.totalUnknownAnswers).toBe(0)
  })

  it('わからなかった語だけが2周目に出題される', () => {
    const unknown = new Set(['w2', 'w5', 'w9'])
    const s = answerRound(startSession(TEN), (id) => !unknown.has(id))
    expect(s.finished).toBe(false)
    expect(s.round).toBe(2)
    expect(s.queue).toEqual(['w2', 'w5', 'w9'])
    expect(s.index).toBe(0)
  })

  it('わかった語は同じサイクルで再出題されない', () => {
    const unknown = new Set(['w2', 'w5', 'w9'])
    let s = answerRound(startSession(TEN), (id) => !unknown.has(id))
    // 2周目のキューにわかった語が含まれない
    for (const id of ['w1', 'w3', 'w4', 'w6', 'w7', 'w8', 'w10']) {
      expect(s.queue).not.toContain(id)
    }
  })

  it('わからない語が0になるまで繰り返す(3語 → 1語 → 完了)', () => {
    // 1周目: w2, w5, w9 がわからない
    let s = answerRound(startSession(TEN), (id) => !['w2', 'w5', 'w9'].includes(id))
    // 2周目: w5 だけまだわからない
    s = answerRound(s, (id) => id !== 'w5')
    expect(s.finished).toBe(false)
    expect(s.round).toBe(3)
    expect(s.queue).toEqual(['w5'])
    // 3周目: 全部わかる → 完了
    s = answerRound(s, () => true)
    expect(s.finished).toBe(true)
    expect(s.totalUnknownAnswers).toBe(4) // 3 + 1
  })

  it('完了後の answer は状態を変えない', () => {
    const s = answerRound(startSession(['a']), () => true)
    expect(s.finished).toBe(true)
    expect(answer(s, false)).toBe(s)
  })
})
