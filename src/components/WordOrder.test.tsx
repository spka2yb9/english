import { describe, expect, it, vi } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { findLesson } from '../content/grammar'
import { WordOrder } from './WordOrder'

const lesson = findLesson('u01-l1')!

function renderWordOrder() {
  render(<WordOrder lesson={lesson} />)
  return screen.getAllByRole('button').filter((b) => b.className.includes('token'))
}

const answerLine = () => document.querySelector('.practice-answer-line')?.textContent

describe('セクション内の並べ替え', () => {
  it('選んだ語は使用済みになり、解答欄に一度だけ入る', () => {
    const tokens = renderWordOrder()
    const first = tokens[0]
    const word = first.textContent as string

    fireEvent.click(first)

    expect(first.getAttribute('aria-pressed')).toBe('true')
    expect(first.className).toContain('used')
    expect(answerLine()).toBe(word)
  })

  it('もう一度押すと取り消せる', () => {
    const tokens = renderWordOrder()
    fireEvent.click(tokens[0])
    fireEvent.click(tokens[1])
    expect(answerLine()).toBe(`${tokens[0].textContent} ${tokens[1].textContent}`)

    fireEvent.click(tokens[0])
    expect(answerLine()).toBe(tokens[1].textContent)
    expect(tokens[0].getAttribute('aria-pressed')).toBe('false')
  })

  it('語を押しても他の語の並びは変わらない', () => {
    const tokens = renderWordOrder()
    const before = tokens.map((b) => b.textContent)
    fireEvent.click(tokens[0])
    const after = screen
      .getAllByRole('button')
      .filter((b) => b.className.includes('token'))
      .map((b) => b.textContent)
    expect(after).toEqual(before)
  })

  it('何も選んでいなければ採点できない', () => {
    const tokens = renderWordOrder()
    expect((screen.getByRole('button', { name: '採点する' }) as HTMLButtonElement).disabled).toBe(true)
    fireEvent.click(tokens[0])
    expect((screen.getByRole('button', { name: '採点する' }) as HTMLButtonElement).disabled).toBe(false)
  })

  it('正しい順に並べると正解になり、次の問題へ進める', () => {
    renderWordOrder()
    // 出題文はレッスンの掲載順なので、1問目の正解文は分かっている
    const answer = 'I am a nurse.'
    for (const word of answer.split(' ')) {
      const token = screen
        .getAllByRole('button')
        .find((b) => b.className.includes('token') && !b.className.includes('used') && b.textContent === word)
      fireEvent.click(token as HTMLElement)
    }
    expect(answerLine()).toBe(answer)

    fireEvent.click(screen.getByRole('button', { name: '採点する' }))
    expect(document.querySelector('.quiz-verdict')?.textContent).toBe('正解!')
    expect(screen.getByRole('button', { name: '次の問題へ' })).toBeTruthy()
  })

  it('10問すべて解くと結果が出る', () => {
    renderWordOrder()
    for (let i = 0; i < 10; i++) {
      const token = screen.getAllByRole('button').find((b) => b.className.includes('token'))
      fireEvent.click(token as HTMLElement)
      fireEvent.click(screen.getByRole('button', { name: '採点する' }))
      fireEvent.click(screen.getByRole('button', { name: i === 9 ? '結果を見る' : '次の問題へ' }))
    }
    expect(document.querySelector('.quiz-result-score')?.textContent).toContain('10問中')
  })
})
