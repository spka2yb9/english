import { describe, expect, it, vi, beforeEach } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

const { speakMock, stopMock } = vi.hoisted(() => ({
  speakMock: vi.fn(() => new Promise<void>(() => {})), // 再生中のまま
  stopMock: vi.fn(),
}))

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: {
    isSupported: () => true,
    speak: (...args: unknown[]) => speakMock(...(args as [])),
    stop: stopMock,
  },
}))

import { AudioButton } from './AudioButton'

beforeEach(() => {
  speakMock.mockClear()
  stopMock.mockClear()
})

describe('AudioButton', () => {
  it('クリックで共有 speech service に正しい英文を渡す', () => {
    render(<AudioButton text="I have lived here for five years." />)
    const button = screen.getByRole('button', { name: /I have lived here for five years\./ })
    fireEvent.click(button)
    expect(speakMock).toHaveBeenCalledWith('I have lived here for five years.', { rate: 1.0 })
  })

  it('スローボタンは SLOW_RATE で再生する', () => {
    render(<AudioButton text="Hello." slow />)
    fireEvent.click(screen.getByRole('button'))
    expect(speakMock).toHaveBeenCalledWith('Hello.', { rate: 0.5 })
  })

  it('再生中にもう一度押すと停止する', () => {
    render(<AudioButton text="Hello." />)
    const button = screen.getByRole('button')
    fireEvent.click(button) // 再生開始(未解決 Promise で再生中のまま)
    fireEvent.click(button) // 停止
    expect(stopMock).toHaveBeenCalled()
  })

  it('キーボード操作可能な button 要素で、ARIA ラベルを持つ', () => {
    render(<AudioButton text="Good morning." />)
    const button = screen.getByRole('button')
    expect(button.tagName).toBe('BUTTON')
    expect(button.getAttribute('aria-label')).toContain('Good morning.')
  })
})
