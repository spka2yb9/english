import { describe, expect, it } from 'vitest'
import { diffAnswer, isAnswerCorrect, normalizeAnswer } from './answerCheck'

describe('normalizeAnswer', () => {
  it('大小文字・句読点・余分な空白を無視する', () => {
    expect(normalizeAnswer('  She IS tired, today. ')).toBe('she is tired today')
  })

  it('短縮形を展開する', () => {
    expect(normalizeAnswer("I'm not busy")).toBe(normalizeAnswer('I am not busy'))
    expect(normalizeAnswer("She can't swim")).toBe(normalizeAnswer('She cannot swim'))
  })

  it('TTSの開始キュー Ready を取り除く', () => {
    expect(normalizeAnswer('Ready. This room is not cold.')).toBe('this room is not cold')
  })

  it('所有格の s は残す', () => {
    expect(normalizeAnswer("the boy's book")).toBe("the boy's book")
  })
})

describe('isAnswerCorrect', () => {
  it('表記ゆれを吸収して判定する', () => {
    expect(isAnswerCorrect("she isn't busy", 'She is not busy.')).toBe(true)
    expect(isAnswerCorrect('she is busy', 'She is not busy.')).toBe(false)
  })

  it('空入力は不正解', () => {
    expect(isAnswerCorrect('   ', 'She is not busy.')).toBe(false)
  })

  it('別解も正解として扱う', () => {
    expect(isAnswerCorrect('I will go', 'I am going to go', ['I will go'])).toBe(true)
  })
})

describe('diffAnswer', () => {
  it('一致した語を ok として返す', () => {
    expect(diffAnswer('she is busy', 'She is busy.').every((t) => t.status === 'ok')).toBe(true)
  })

  it('抜けた語を missing として示し、後続をずらさない', () => {
    const diff = diffAnswer('she busy today', 'She is busy today.')
    expect(diff.map((t) => `${t.word}:${t.status}`)).toEqual([
      'she:ok',
      'is:missing',
      'busy:ok',
      'today:ok',
    ])
  })

  it('余分な語を extra として示す', () => {
    const diff = diffAnswer('she is very busy', 'She is busy.')
    expect(diff.find((t) => t.status === 'extra')?.word).toBe('very')
  })
})
