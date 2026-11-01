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
  it('英文法と同じ116話を、レベル・ユニット別に並べる', () => {
    render(
      <MemoryRouter>
        <ThreeMinuteIndex />
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: '3分間English' })).toBeInTheDocument()
    expect(document.querySelectorAll('.tm-lesson-list a')).toHaveLength(116)
    expect(screen.getByRole('link', { name: /be動詞の現在形/ })).toHaveAttribute(
      'href',
      '/three-minute/u01-l1',
    )
    expect(screen.getByRole('heading', { level: 3, name: 'A2 — 基礎の確認' })).toBeInTheDocument()
  })
})
