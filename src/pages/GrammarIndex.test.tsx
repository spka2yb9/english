import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { GrammarIndex } from './GrammarIndex'

describe('GrammarIndex', () => {
  it('「英文の作られ方から学ぶ」を、カード全体がリンクの専用ページとして案内する', () => {
    render(
      <MemoryRouter>
        <GrammarIndex />
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: '英文法' })).toBeInTheDocument()
    // 見出しと説明文を含むカード全体が、1つのリンクになっている。
    const card = screen.getByRole('link', { name: '英文の作られ方から学ぶ' })
    expect(card).toHaveAttribute('href', '/grammar/roadmap')
    expect(card).toHaveTextContent('5文型は暗記の対象ではなく')
    expect(document.querySelectorAll('.roadmap-cta .btn-primary')).toHaveLength(0)
    // ステップの並びは専用ページにだけ置く。
    expect(document.querySelectorAll('.roadmap-step')).toHaveLength(0)
  })

  it('冒頭に5文型の見取り図を置き、詳細ページへ案内する', () => {
    render(
      <MemoryRouter>
        <GrammarIndex />
      </MemoryRouter>,
    )

    expect(
      screen.getByRole('heading', { level: 2, name: '5文型は、動詞のあとに何が続くかで決まる' }),
    ).toBeInTheDocument()
    for (const label of ['第1文型 SV', '第2文型 SVC', '第3文型 SVO', '第4文型 SVOO', '第5文型 SVOC']) {
      expect(screen.getByText(label)).toBeInTheDocument()
    }
    expect(screen.getByRole('link', { name: /5文型と英文の作られ方を詳しく見る/ })).toHaveAttribute(
      'href',
      '/grammar/roadmap',
    )
  })

  it('レベル別のセクション一覧を残し、既存のリンクを壊さない', () => {
    render(
      <MemoryRouter>
        <GrammarIndex />
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 2, name: 'レベル別のセクション一覧' })).toBeInTheDocument()
    expect(screen.getByRole('heading', { level: 3, name: 'A2 — 基礎の確認' })).toBeInTheDocument()
    // 既存のユニットカードと完了マークはそのまま残す。
    expect(document.querySelectorAll('.unit-card').length).toBe(33)
    expect(screen.getByRole('link', { name: /be動詞の現在形/ })).toHaveAttribute('href', '/grammar/u01-l1')
  })
})
