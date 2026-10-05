import { fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { Ingbird } from './Ingbird'
import { IngbirdCard } from './IngbirdCard'
import { IngbirdPraise } from './IngbirdPraise'
import { todayString, shiftDate } from '../services/dates'
import { KEYS, saveJson } from '../services/storage'
import { recordStudyDay } from '../services/studyDays'

beforeEach(() => {
  localStorage.clear()
  vi.spyOn(Math, 'random').mockReturnValue(0) // 言い回しの抽選を固定する
})

afterEach(() => {
  vi.restoreAllMocks()
})

function renderCard() {
  return render(
    <MemoryRouter>
      <IngbirdCard />
    </MemoryRouter>,
  )
}

describe('Ingbird', () => {
  it('マスコットは気分に応じた見た目を持ち、装飾利用では読み上げから外れる', () => {
    const { container } = render(<Ingbird mood="cheer" decorative />)
    const svg = container.querySelector('svg')
    expect(svg).toHaveAttribute('data-mood', 'cheer')
    expect(svg).toHaveAttribute('aria-hidden', 'true')
    expect(svg?.querySelector('.ingbird-sparkles')).not.toBeNull()
  })
})

describe('IngbirdCard', () => {
  it('学習日は連続ではなくトータルで表示する', () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -8), shiftDate(today, -5), today])
    const { container } = renderCard()
    expect(container.querySelector('.ingbird-total')?.textContent).toBe('3日')
    expect(screen.getByText(/今日の学習: ずみ/)).toBeInTheDocument()
  })

  it('久しぶりの学習日もほめる', () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -5), today])
    renderCard()
    expect(screen.getByText(/5日ぶり!おかえり!/)).toBeInTheDocument()
    expect(screen.getByText(/減らさない/)).toBeInTheDocument()
  })

  it('まだ学習していない日は、1問から誘う(久しぶりでも責めない)', () => {
    saveJson(KEYS.studyDays, [shiftDate(todayString(), -4)])
    renderCard()
    expect(screen.getByText(/4日ぶりだね、待ってたよ!/)).toBeInTheDocument()
    expect(screen.getByRole('link', { name: '1セッション始める' })).toBeInTheDocument()
    expect(screen.getByText(/連続日数ではなく/)).toBeInTheDocument()
  })

  it('記録がなければ0日として迎える', () => {
    const { container } = renderCard()
    expect(container.querySelector('.ingbird-total')?.textContent).toBe('0日')
    expect(screen.getByText('今日はまだ、これから!')).toBeInTheDocument()
  })
})

describe('IngbirdPraise', () => {
  it('新しい学習日を記録すると、トータル日数つきでほめ、閉じられる', async () => {
    render(<IngbirdPraise />)
    expect(screen.queryByRole('status')).toBeNull()

    recordStudyDay()
    const toast = await screen.findByRole('status')
    expect(toast).toHaveTextContent('1日目、はじまった!')
    expect(toast).toHaveTextContent('学習日 1日（トータル）')

    fireEvent.click(screen.getByRole('button', { name: 'メッセージを閉じる' }))
    expect(screen.queryByRole('status')).toBeNull()
  })

  it('同じ日の2回目以降は出し直さない', async () => {
    render(<IngbirdPraise />)
    recordStudyDay()
    await screen.findByRole('status')
    recordStudyDay()
    expect(screen.getAllByRole('status')).toHaveLength(1)
  })
})
