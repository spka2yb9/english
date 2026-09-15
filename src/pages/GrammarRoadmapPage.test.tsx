import { render, screen, within } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { grammarRoadmap } from '../content/grammar/roadmap'
import { patternQuiz, patternShowcases, wordOrderQuiz } from '../content/grammar/structures'
import { PATTERN_ORDER } from '../content/grammar/patterns/types'
import { GrammarRoadmapPage } from './GrammarRoadmapPage'

function renderPage() {
  render(
    <MemoryRouter initialEntries={['/grammar/roadmap']}>
      <GrammarRoadmapPage />
    </MemoryRouter>,
  )
}

describe('GrammarRoadmapPage', () => {
  it('最初に S / V / O / C / M の意味を示す', () => {
    renderPage()

    expect(screen.getByRole('heading', { level: 2, name: 'S / V / O / C / M とは' })).toBeInTheDocument()
    const items = document.querySelectorAll('.role-guide-item')
    expect(items).toHaveLength(5)
    // 表示順は S → V → O → C → M。
    expect([...items].map((item) => item.querySelector('.role-badge')?.textContent)).toEqual([
      'S',
      'V',
      'O',
      'C',
      'M',
    ])
    // 記号の意味は、日本語名を含む読み上げラベルで示す。
    const names = ['主語', '動詞', '目的語', '補語', '修飾語']
    for (const [index, name] of names.entries()) {
      expect(within(items[index] as HTMLElement).getByLabelText(new RegExp(name))).toBeTruthy()
    }
  })

  it('5文型それぞれに2Dアニメーション付きのカードを出す', () => {
    renderPage()

    const cards = document.querySelectorAll('.pattern-card')
    expect(cards).toHaveLength(PATTERN_ORDER.length)
    expect(patternShowcases.map((showcase) => showcase.pattern)).toEqual(PATTERN_ORDER)

    // レッスンの挿絵と同じ再生UI(3段階・再生ボタン・段階ボタン)を使う。
    for (const [index, pattern] of PATTERN_ORDER.entries()) {
      const card = cards[index] as HTMLElement
      const animation = card.querySelector('.grammar-animation')
      expect(animation, pattern).not.toBeNull()
      expect(animation).toHaveAttribute('data-scene', `pattern-${pattern}`)
      expect(within(card).getByRole('button', { name: '再生' })).toBeInTheDocument()
      expect(within(card).getAllByRole('button', { name: /^ステップ\d:/ })).toHaveLength(3)
      expect(card.textContent).toContain('骨組み')
    }
  })

  it('統合した語順と5文型の理解度チェックを出す', () => {
    renderPage()

    expect(screen.getByRole('heading', { level: 2, name: '理解度チェック（記号と語順）' })).toBeInTheDocument()
    expect(screen.getByRole('heading', { level: 2, name: '理解度チェック（5文型）' })).toBeInTheDocument()
    // Quiz は1ブロックにつき1つ。統合した問題数をそのまま出題する。
    expect(screen.getAllByRole('group', { name: '選択肢' })).toHaveLength(2)
    expect(screen.getByText(`問題 1 / ${wordOrderQuiz.length}`)).toBeInTheDocument()
    expect(screen.getByText(`問題 1 / ${patternQuiz.length}`)).toBeInTheDocument()
  })

  it('統合した例文で並べ替え（産出練習）を出す', () => {
    renderPage()

    expect(screen.getByRole('heading', { level: 2, name: '並べ替え' })).toBeInTheDocument()
    // 旧セクションが持っていた並べ替え10問を、ページの例文から作り直す。
    expect(screen.getByText('問題 1 / 10')).toBeInTheDocument()
    expect(document.querySelectorAll('.practice-card .token').length).toBeGreaterThan(3)
  })

  it('STEP 1〜7 を既存セクションへのリンク付きで示す', () => {
    renderPage()

    expect(screen.getByRole('heading', { level: 1, name: '英文の作られ方から学ぶ' })).toBeInTheDocument()
    expect(document.querySelectorAll('.roadmap-step')).toHaveLength(grammarRoadmap.length)
    expect(document.querySelectorAll('.roadmap-step').length).toBeGreaterThanOrEqual(7)

    // 各STEPから、既存のレッスン(/grammar/:lessonId)へそのまま進める。
    for (const step of document.querySelectorAll('.roadmap-step')) {
      const links = within(step as HTMLElement).getAllByRole('link')
      expect(links.length).toBeGreaterThan(0)
      for (const link of links) {
        expect(link.getAttribute('href')).toMatch(/^\/grammar\/u\d+-l\d+$/)
      }
    }
  })

  it('削除したセクションへのリンクを残さない', () => {
    renderPage()

    const hrefs = [...document.querySelectorAll('a')].map((anchor) => anchor.getAttribute('href'))
    expect(hrefs).not.toContain('/grammar/u01-l4')
    expect(hrefs).not.toContain('/grammar/u01-l5')
  })

  it('読み進める順番(動詞 → 主語 → 骨格 → 修飾)を本文で示す', () => {
    renderPage()

    const intro = document.querySelector('.roadmap-intro')?.textContent ?? ''
    expect(intro).toContain('動詞(V)を探し')
    expect(intro).toContain('主語(S)を探し')
    expect(intro).toContain('修飾語(M)を確かめます')
  })

  it('パンくずと、レベル別一覧へ戻る導線を持つ', () => {
    renderPage()

    expect(screen.getByRole('navigation', { name: 'パンくず' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: '英文法' })).toHaveAttribute('href', '/grammar')
    expect(screen.getByRole('link', { name: /レベル別のセクション一覧へ/ })).toHaveAttribute('href', '/grammar')
  })
})
