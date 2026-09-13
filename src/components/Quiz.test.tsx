import { afterEach, describe, expect, it, vi } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'
import type { QuizQuestion } from '../content/types'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { Quiz } from './Quiz'

const questions: QuizQuestion[] = [
  {
    id: 'q1',
    prompt: '正しい文を選んでください。',
    choices: ['I have been to London twice.', 'I have gone to London twice.', 'I went to London since 2020.', 'I am been to London.'],
    correctIndex: 0,
    explanation: '経験を表すときは have been to を使います。',
    choiceNotes: [null, 'have gone to は「行ってしまって今いない」の意味です。', 'since と過去形は一緒に使えません。', 'be 動詞と been は重ねられません。'],
    audioEn: 'I have been to London twice.',
  },
  {
    id: 'q2',
    prompt: '空所に入る語を選んでください。',
    sentence: 'She ___ in Tokyo since 2019.',
    choices: ['lives', 'has lived', 'lived', 'is living'],
    correctIndex: 1,
    explanation: 'since があるので現在完了を使います。',
  },
]

describe('Quiz', () => {
  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('選択肢を並べ替えて表示し、正誤判定は元データのインデックスで行う', () => {
    // rng=0 の Fisher-Yates は [0,1,2,3] を [1,2,3,0] にする
    vi.spyOn(Math, 'random').mockReturnValue(0)
    render(<Quiz questions={questions} />)
    const rendered = screen.getAllByRole('button').map((b) => b.textContent)
    expect(rendered).toEqual([
      questions[0].choices[1],
      questions[0].choices[2],
      questions[0].choices[3],
      questions[0].choices[0],
    ])
    // 表示位置が変わっても、正解の文を選べば正解になる
    fireEvent.click(screen.getByRole('button', { name: questions[0].choices[0] }))
    expect(screen.getByText('正解!')).toBeTruthy()
  })

  it('回答後に即時フィードバックと解説を表示し、選択肢を無効化する', () => {
    render(<Quiz questions={questions} />)
    fireEvent.click(screen.getByRole('button', { name: 'I have gone to London twice.' }))
    expect(screen.getByText('不正解')).toBeTruthy()
    expect(screen.getByText('経験を表すときは have been to を使います。')).toBeTruthy()
    // 誤答の理由も表示される
    expect(screen.getByText(/行ってしまって今いない/)).toBeTruthy()
    // 回答後は選択肢が押せない
    const choice = screen.getByRole('button', { name: 'I have been to London twice.' }) as HTMLButtonElement
    expect(choice.disabled).toBe(true)
  })

  it('正解するとその旨を表示する', () => {
    render(<Quiz questions={questions} />)
    fireEvent.click(screen.getByRole('button', { name: 'I have been to London twice.' }))
    expect(screen.getByText('正解!')).toBeTruthy()
  })

  it('全問回答すると結果と正解数を表示し onComplete を呼ぶ', () => {
    const onComplete = vi.fn()
    render(<Quiz questions={questions} onComplete={onComplete} />)
    // 1問目: 正解
    fireEvent.click(screen.getByRole('button', { name: 'I have been to London twice.' }))
    fireEvent.click(screen.getByRole('button', { name: '次の問題へ' }))
    // 2問目: 不正解
    fireEvent.click(screen.getByRole('button', { name: 'lives' }))
    fireEvent.click(screen.getByRole('button', { name: '結果を見る' }))
    expect(screen.getByText('2問中 1問正解')).toBeTruthy()
    expect(onComplete).toHaveBeenCalledWith(1)
  })
})
