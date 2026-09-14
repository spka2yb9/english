import { render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { EnglishExample } from './EnglishExample'

describe('EnglishExample の文型表示', () => {
  it('文型バッジと文型注記を読み上げ可能な形で表示する', () => {
    render(
      <EnglishExample
        text="He gave me a book."
        translation="彼は私に本をくれました。"
        pattern="SVOO"
        patternNote="人 → もの の2つの目的語を取る第4文型。"
      />,
    )

    expect(screen.getByText('SVOO')).toBeInTheDocument()
    expect(screen.getByText('人 → もの の2つの目的語を取る第4文型。')).toBeInTheDocument()
    // バッジは型名だけでなく「第4文型」の読み上げラベルを持つ
    expect(screen.getByLabelText(/第4文型 SVOO/)).toBeInTheDocument()
  })

  it('文型が付いていなければバッジを出さない', () => {
    render(<EnglishExample text="She is a nurse." />)
    expect(screen.queryByText('SVC')).toBeNull()
    expect(document.querySelector('.example-pattern')).toBeNull()
  })
})
