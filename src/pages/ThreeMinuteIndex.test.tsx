import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { ThreeMinuteIndex } from './ThreeMinuteIndex'

describe('ThreeMinuteIndex', () => {
  it('冒頭に5文型の導入を置き、英文法の116話をレベル・ユニット別に並べる', () => {
    render(
      <MemoryRouter>
        <ThreeMinuteIndex />
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: '3分間English' })).toBeInTheDocument()
    expect(screen.getByText('117話')).toBeInTheDocument()

    // 最初に読むのは5文型の導入。英文法の最初の話より前に置く。
    const intro = screen.getByRole('link', { name: /5文型の地図/ })
    expect(intro).toHaveAttribute('href', '/three-minute/intro-patterns')
    expect(intro).toHaveTextContent('S / V / O / C / M')
    const firstLesson = screen.getByRole('link', { name: /be動詞の現在形/ })
    expect(intro.compareDocumentPosition(firstLesson) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy()

    expect(document.querySelectorAll('.tm-lesson-list a')).toHaveLength(116)
    expect(firstLesson).toHaveAttribute('href', '/three-minute/u01-l1')
    expect(screen.getByRole('heading', { level: 3, name: 'A2 — 基礎の確認' })).toBeInTheDocument()
  })
})
