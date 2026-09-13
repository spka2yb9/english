import { fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { Layout } from './Layout'

function renderLayout() {
  return render(
    <MemoryRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<p>学習コンテンツ</p>} />
          <Route path="pronunciation" element={<p>発音記号コンテンツ</p>} />
        </Route>
      </Routes>
    </MemoryRouter>,
  )
}

describe('Layout', () => {
  beforeEach(() => {
    vi.spyOn(window, 'scrollTo').mockImplementation(() => undefined)
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('メニューボタンでドロワーを開閉し、ARIA 状態を更新する', () => {
    renderLayout()
    const menu = screen.getByRole('button', { name: 'メニューを開く' })

    fireEvent.click(menu)
    expect(screen.getByRole('button', { name: 'メニューを閉じる' })).toHaveAttribute('aria-expanded', 'true')
    expect(screen.getByRole('navigation', { name: 'メインナビゲーション' })).toHaveClass('open')

    fireEvent.keyDown(window, { key: 'Escape' })
    expect(screen.getByRole('button', { name: 'メニューを開く' })).toHaveAttribute('aria-expanded', 'false')
  })

  it('本文へのスキップリンクとフォーカス可能な main を持つ', () => {
    renderLayout()
    expect(screen.getByRole('link', { name: '本文へ移動' })).toHaveAttribute('href', '#main-content')
    expect(screen.getByRole('main')).toHaveAttribute('id', 'main-content')
    expect(screen.getByRole('main')).toHaveAttribute('tabindex', '-1')
  })

  it('ページ遷移時に画面を一番上へ戻す', () => {
    renderLayout()
    const scrollTo = vi.mocked(window.scrollTo)
    scrollTo.mockClear()

    fireEvent.click(screen.getByRole('link', { name: '発音記号' }))

    expect(screen.getByText('発音記号コンテンツ')).toBeInTheDocument()
    expect(scrollTo).toHaveBeenCalledWith({ top: 0, left: 0, behavior: 'instant' })
  })
})
