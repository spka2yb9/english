import { fireEvent, render, screen, within } from '@testing-library/react'
import { beforeEach, describe, expect, it, vi } from 'vitest'

const { speakMock } = vi.hoisted(() => ({
  speakMock: vi.fn(() => Promise.resolve()),
}))

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: {
    isSupported: () => true,
    speak: (...args: unknown[]) => speakMock(...(args as [])),
    stop: vi.fn(),
  },
}))

import * as quizModule from '../content/pronunciation/quiz'
import { Pronunciation } from './Pronunciation'

beforeEach(() => {
  speakMock.mockClear()
})

describe('Pronunciation', () => {
  it('発音表の例語の音声を再生する', () => {
    render(<Pronunciation />)
    fireEvent.click(screen.getByRole('button', { name: '音声を再生: see' }))
    expect(speakMock).toHaveBeenCalledWith('see', { rate: 1.0 })
  })
})

describe('発音記号の穴埋め演習', () => {
  it('出題語の音声を聞いてから4択に答えると、正誤と正しい発音記号を表示する', () => {
    const { container } = render(<Pronunciation />)
    // 例語の表にも同じ単語の再生ボタンがあるので、演習セクション内だけを見る。
    const quiz = within(container.querySelector('.ipa-quiz-section')!)
    const word = quiz.getByText(/に入る記号を選んでください。$/).textContent!.match(/「(.+?)」/)![1]
    // 出題はランダムなので、表示されている空所入りの発音記号から元データを一意に特定する。
    const shown = container.querySelector('.quiz-sentence')!.textContent
    const item = quizModule.ipaQuizWords.find(
      (w) => w.word === word && `/${w.ipa.replace(/\[[^\]]*\]/, '___')}/` === shown,
    )!

    fireEvent.click(quiz.getByRole('button', { name: `音声を再生: ${word}` }))
    expect(speakMock).toHaveBeenCalledWith(word, { rate: 1.0 })

    fireEvent.click(quiz.getByRole('button', { name: quizModule.blankSymbol(item.ipa) }))

    expect(screen.getByText('正解!')).toBeInTheDocument()
    expect(screen.getByText(new RegExp(`^${word} は /`))).toBeInTheDocument()
  })
})
