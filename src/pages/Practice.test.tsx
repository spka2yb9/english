import { beforeEach, describe, expect, it, vi } from 'vitest'
import { fireEvent, render, screen } from '@testing-library/react'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1.0,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { Practice } from './Practice'
import { KEYS } from '../services/storage'

const progress = () => document.querySelector('.quiz-progress')?.textContent ?? ''
const shownSentence = () => document.querySelector('.practice-en')?.textContent ?? ''
const savedCounts = (mode: string) =>
  Object.values(JSON.parse(localStorage.getItem(`${KEYS.practiceStats}.${mode}`) ?? '{}') as Record<string, number>)

describe('音声練習ページ', () => {
  beforeEach(() => localStorage.clear())

  it('音読・シャドーイングが最初から始まっている', () => {
    render(<Practice />)
    expect(screen.getByRole('heading', { level: 1 }).textContent).toBe('音声練習')
    expect(screen.getByRole('button', { name: '音読・シャドーイング' }).getAttribute('aria-pressed')).toBe('true')
    expect(screen.getByRole('button', { name: '次の文へ' })).toBeTruthy()
    expect(progress()).toContain('1問目')
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

  it('何問でも続き、完了画面は出ない', () => {
    render(<Practice />)
    const first = shownSentence()
    expect(first).not.toBe('')

    // 8問を超えて続けても終わらない
    for (let i = 0; i < 12; i++) {
      fireEvent.click(screen.getByRole('button', { name: '次の文へ' }))
      expect(shownSentence()).not.toBe('')
      expect(document.querySelector('.vocab-complete')).toBeNull()
    }

    expect(progress()).toContain('13問目')
  })

  it('直前と同じ文は続けて出さない', () => {
    render(<Practice />)
    for (let i = 0; i < 5; i++) {
      const before = shownSentence()
      fireEvent.click(screen.getByRole('button', { name: '次の文へ' }))
      expect(shownSentence()).not.toBe(before)
    }
  })

  it('ディクテーションは採点後も次の問題へ続く', () => {
    render(<Practice />)
    fireEvent.click(screen.getByRole('button', { name: 'ディクテーション' }))

    fireEvent.change(document.querySelector('.practice-input') as HTMLTextAreaElement, {
      target: { value: 'zzz' },
    })
    fireEvent.click(screen.getByRole('button', { name: '採点する' }))
    expect(screen.getByText('不正解')).toBeTruthy()

    fireEvent.click(screen.getByRole('button', { name: '次の問題へ' }))
    expect(progress()).toContain('2問目')
    expect((document.querySelector('.practice-input') as HTMLTextAreaElement).value).toBe('')
    expect((screen.getByRole('button', { name: '採点する' }) as HTMLButtonElement).disabled).toBe(true)
    expect(document.querySelector('.vocab-complete')).toBeNull()
  })

  it('モードを切り替えると出題が1問目に戻る', () => {
    render(<Practice />)
    fireEvent.click(screen.getByRole('button', { name: '次の文へ' }))
    expect(progress()).toContain('2問目')

    fireEvent.click(screen.getByRole('button', { name: 'ディクテーション' }))
    expect(progress()).toContain('1問目')
  })

  it('実施回数を文ごとに記録し、モード別に持つ', () => {
    render(<Practice />)
    fireEvent.click(screen.getByRole('button', { name: '次の文へ' }))
    fireEvent.click(screen.getByRole('button', { name: '次の文へ' }))
    expect(savedCounts('shadowing')).toEqual([1, 1])
    expect(localStorage.getItem(`${KEYS.practiceStats}.dictation`)).toBeNull()

    fireEvent.click(screen.getByRole('button', { name: 'ディクテーション' }))
    fireEvent.change(document.querySelector('.practice-input') as HTMLTextAreaElement, {
      target: { value: 'zzz' },
    })
    fireEvent.click(screen.getByRole('button', { name: '採点する' }))
    expect(savedCounts('dictation')).toEqual([1])
  })
})
