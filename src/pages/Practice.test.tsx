import { beforeEach, describe, expect, it, vi } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { Practice } from './Practice'

describe('音声練習ページ', () => {
  beforeEach(() => localStorage.clear())

  it('音読・シャドーイングが最初から始まっている', () => {
    render(<Practice />)
    expect(screen.getByRole('heading', { level: 1 }).textContent).toBe('音声練習')
    expect(screen.getByRole('button', { name: '音読・シャドーイング' }).getAttribute('aria-pressed')).toBe('true')
    expect(screen.getByRole('button', { name: '次へ' })).toBeTruthy()
  })

  it('モードは音読とディクテーションの2つだけ', () => {
    render(<Practice />)
    const labels = screen
      .getAllByRole('button')
      .filter((b) => b.className.includes('mode-switch-btn'))
      .map((b) => b.textContent)
    expect(labels).toEqual(['音読・シャドーイング', 'ディクテーション'])
  })

  it('ディクテーションに切り替えると解答欄が出る', () => {
    render(<Practice />)
    fireEvent.click(screen.getByRole('button', { name: 'ディクテーション' }))
    expect(document.querySelector('.practice-input')).toBeTruthy()
    // 音声だけが手がかりなので、英文は表示しない
    expect(document.querySelector('.practice-en')).toBeNull()
  })

  it('ディクテーションの採点は空欄では押せない', () => {
    render(<Practice />)
    fireEvent.click(screen.getByRole('button', { name: 'ディクテーション' }))
    expect((screen.getByRole('button', { name: '採点する' }) as HTMLButtonElement).disabled).toBe(true)
    fireEvent.change(document.querySelector('.practice-input') as HTMLTextAreaElement, {
      target: { value: 'anything' },
    })
    expect((screen.getByRole('button', { name: '採点する' }) as HTMLButtonElement).disabled).toBe(false)
  })
})
