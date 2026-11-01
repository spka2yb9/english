import { render, screen, within } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { beforeEach, describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { DEFAULT_OUTFIT } from '../content/ingbird/outfits'
import { KEYS } from '../services/storage'
import { ThreeMinuteLessonPage } from './ThreeMinuteLesson'

describe('ThreeMinuteLessonPage', () => {
  beforeEach(() => {
    localStorage.clear()
  })
  it('会話・アニメーション・4問の理解度チェックを表示する', () => {
    render(
      <MemoryRouter initialEntries={['/three-minute/u01-l1']}>
        <Routes>
          <Route path="/three-minute/:lessonId" element={<ThreeMinuteLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: 'be動詞の現在形' })).toBeInTheDocument()
    // 先生と生徒の吹き出しが交互に並ぶ。
    expect(document.querySelectorAll('.tm-turn-ingbird').length).toBeGreaterThan(5)
    expect(document.querySelectorAll('.tm-turn-hiyoko').length).toBeGreaterThan(5)
    // 文法ページのアニメーションをそのまま使う。
    expect(document.querySelector('.grammar-animation')).not.toBeNull()
    // 問題演習は最後の4問だけ。
    expect(screen.getByRole('heading', { level: 2, name: '理解度チェック' })).toBeInTheDocument()
    expect(screen.getByText('問題 1 / 4')).toBeInTheDocument()
    expect(within(screen.getByRole('group', { name: '選択肢' })).getAllByRole('button')).toHaveLength(4)
  })

  it('5文型の導入は、5つのアニメーションと8問の理解度チェックを表示する', () => {
    render(
      <MemoryRouter initialEntries={['/three-minute/intro-patterns']}>
        <Routes>
          <Route path="/three-minute/:lessonId" element={<ThreeMinuteLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: '5文型の地図' })).toBeInTheDocument()
    // 英語の語順に1つ、5文型それぞれに1つ。合計6つのアニメーションで確かめる。
    expect(document.querySelectorAll('.grammar-animation')).toHaveLength(6)
    expect(screen.getAllByText('S / V / O / C / M の役割').length).toBeGreaterThan(0)
    expect(screen.getByRole('heading', { level: 2, name: '理解度チェック' })).toBeInTheDocument()
    expect(screen.getByText('問題 1 / 8')).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /次のお話: be動詞の現在形/ })).toHaveAttribute(
      'href',
      '/three-minute/u01-l1',
    )
  })

  it('保存済みの着せかえと進化段階を、先生の姿に反映する', () => {
    localStorage.setItem(
      KEYS.ingbirdOutfit,
      JSON.stringify({ ...DEFAULT_OUTFIT, glasses: 'round', hat: 'beanie' }),
    )
    localStorage.setItem(KEYS.studyDays, JSON.stringify(['2026-01-01', '2026-01-02', '2026-01-03']))

    render(
      <MemoryRouter initialEntries={['/three-minute/u01-l1']}>
        <Routes>
          <Route path="/three-minute/:lessonId" element={<ThreeMinuteLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    const teacher = document.querySelector('.tm-turn-ingbird .ingbird')
    expect(teacher).toHaveAttribute('data-glasses', 'round')
    expect(teacher).toHaveAttribute('data-hat', 'beanie')
    expect(teacher).toHaveAttribute('data-evolution', '1')
  })

  it('例文は5文まで表示し、残りをアコーディオンに畳む', () => {
    render(
      <MemoryRouter initialEntries={['/three-minute/u01-l1']}>
        <Routes>
          <Route path="/three-minute/:lessonId" element={<ThreeMinuteLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    const more = document.querySelector('.tm-scene .example-more')
    expect(more).not.toBeNull()
    expect(more).not.toHaveAttribute('open')
    expect(document.querySelectorAll('.tm-scene .block-examples > .example').length).toBe(5)
    const hiddenCount = more?.querySelectorAll('.example').length ?? 0
    expect(hiddenCount).toBeGreaterThan(0)
    expect(screen.getByText(new RegExp(`あと${hiddenCount}文`))).toBeInTheDocument()
  })
})
