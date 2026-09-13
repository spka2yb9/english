import { describe, expect, it } from 'vitest'
import { checkPassage, checkQuestion, findNearDuplicates, unknownWordRatio } from './validation'
import type { QuizQuestion, ReadingPassage } from './types'

const question: QuizQuestion = {
  id: 'q1',
  prompt: '正しい文を選んでください。',
  choices: ['She is busy.', 'She are busy.', 'She be busy.'],
  correctIndex: 0,
  explanation: '主語が三人称単数なので is を使います。',
  choiceNotes: [null, 'are は複数主語に使います。', '原形の be は使えません。'],
}

describe('設問の検証', () => {
  it('整った設問は問題を報告しない', () => {
    expect(checkQuestion(question, 'test')).toEqual([])
  })

  it('誤答注記の欠落を検出する', () => {
    const issues = checkQuestion({ ...question, choiceNotes: undefined }, 'test')
    expect(issues.map((i) => i.message)).toContain('誤答注記(choiceNotes)がありません')
  })

  it('選択肢の重複と範囲外の正解を検出する', () => {
    const issues = checkQuestion({ ...question, choices: ['a', 'a', 'b'], correctIndex: 5 }, 'test')
    expect(issues.map((i) => i.message)).toEqual(
      expect.arrayContaining(['選択肢が重複しています', 'correctIndex が選択肢の範囲外です']),
    )
  })
})

describe('本文の検証', () => {
  const passage: ReadingPassage = {
    id: 'p1',
    level: 'A2',
    title: 'Test',
    titleJa: 'テスト',
    minutes: 12,
    paragraphs: ['She works at a bank. He walks to school every day.'],
    paragraphsJa: ['彼女は銀行で働いています。彼は毎日歩いて学校へ行きます。'],
    glossary: [
      { word: 'bank', ja: '銀行' },
      { word: 'walk', ja: '歩く' },
      { word: 'every', ja: '毎〜' },
      { word: 'school', ja: '学校' },
    ],
    questions: [question, question, question, question],
    canDo: ['R-A2-1'],
  }

  it('整った本文は問題を報告しない', () => {
    expect(checkPassage(passage)).toEqual([])
  })

  it('レベルに対して文が長すぎる本文を検出する', () => {
    const long = 'The committee that had been established to review the proposal decided that further consultation with the residents affected by the change would be necessary before any final decision could reasonably be taken.'
    const issues = checkPassage({ ...passage, paragraphs: [long], paragraphsJa: ['(略)'] })
    expect(issues.some((i) => i.message.includes('平均文長'))).toBe(true)
  })

  it('段落と和訳の数の不一致を検出する', () => {
    const issues = checkPassage({ ...passage, paragraphsJa: [] })
    expect(issues.some((i) => i.message.includes('和訳の数'))).toBe(true)
  })
})

describe('近似重複の検出', () => {
  it('言い回しが違っても内容が重なる文を検出する', () => {
    const issues = findNearDuplicates([
      { id: 'a', text: 'The library on Maple Street opens at nine in the morning.' },
      { id: 'b', text: 'The library on Maple Street opens at nine in the evening.' },
      { id: 'c', text: 'Volunteers repair broken toasters and lamps at the community hall.' },
    ])
    expect(issues).toHaveLength(1)
    expect(issues[0].where).toBe('a')
  })
})

describe('未習語率', () => {
  it('既習語だけの文は0になる', () => {
    expect(unknownWordRatio('She works at a bank.', new Set(['she', 'work', 'at', 'a', 'bank']))).toBe(0)
  })

  it('未習語の割合を返す', () => {
    expect(unknownWordRatio('She works at a bank.', new Set(['she', 'at', 'a']))).toBeCloseTo(0.4)
  })
})
