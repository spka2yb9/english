import { fireEvent, render, screen, within } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { getGrammarItemStats } from '../services/progress'
import { KEYS } from '../services/storage'
import { GrammarLessonPage } from './GrammarLesson'

describe('GrammarLessonPage', () => {
  it('次のレッスンへ移動するとクイズ状態を初期化する', () => {
    render(
      <MemoryRouter initialEntries={['/grammar/u01-l1']}>
        <Routes>
          <Route path="/grammar/:lessonId" element={<GrammarLessonPage />} />
          <Route path="/grammar" element={<p>文法一覧</p>} />
        </Routes>
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: 'be動詞の現在形' })).toBeInTheDocument()
    const choices = within(screen.getByRole('group', { name: '選択肢' })).getAllByRole('button')
    fireEvent.click(choices[0])
    expect(document.querySelector('.quiz-feedback')).not.toBeNull()

    // 産出練習はセクション内で完結させる。演習ページには置かない。
    expect(screen.getByRole('heading', { level: 2, name: '並べ替え' })).toBeInTheDocument()
    expect(document.querySelectorAll('.token-list .token')).toHaveLength(4)

    fireEvent.click(screen.getByRole('link', { name: /次のセクション:/ }))
    expect(screen.getByRole('heading', { level: 1, name: '一般動詞の現在形と三単現' })).toBeInTheDocument()
    expect(document.querySelector('.quiz-feedback')).toBeNull()
    expect(screen.getByText('問題 1 / 4')).toBeInTheDocument()
  })

  it('レッスン内で解いた問題の正誤をSRSへ記録する', () => {
    localStorage.removeItem(KEYS.grammarItemStats)
    render(
      <MemoryRouter initialEntries={['/grammar/u01-l1']}>
        <Routes>
          <Route path="/grammar/:lessonId" element={<GrammarLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    const choices = within(screen.getByRole('group', { name: '選択肢' })).getAllByRole('button')
    fireEvent.click(choices[0])

    // 記録が落ちると、設定ページの進捗集計とGist同期から文法クイズの実績が消える。
    expect(Object.keys(getGrammarItemStats())).toEqual(['u01-l1-q1'])
  })

  it('構造データのあるセクションは構造図と「構造チェック」を、既存の理解度チェックと分けて出す', () => {
    render(
      <MemoryRouter initialEntries={['/grammar/u05-l1']}>
        <Routes>
          <Route path="/grammar/:lessonId" element={<GrammarLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(screen.getByRole('heading', { level: 1, name: '形容詞の位置と使い方' })).toBeInTheDocument()
    // 構造図(S / V / O / C / M の区画)が本文に入る。
    expect(document.querySelectorAll('.breakdown-parts').length).toBeGreaterThan(0)
    // 既存のクイズを置き換えず、構造チェックを別セクションとして追加する。
    expect(screen.getByRole('heading', { level: 2, name: '構造チェック' })).toBeInTheDocument()
    expect(screen.getByRole('heading', { level: 2, name: '理解度チェック' })).toBeInTheDocument()
    expect(screen.getAllByRole('group', { name: '選択肢' })).toHaveLength(2)
  })

  it('構造データのないセクションには構造チェックを出さない', () => {
    render(
      <MemoryRouter initialEntries={['/grammar/u01-l1']}>
        <Routes>
          <Route path="/grammar/:lessonId" element={<GrammarLessonPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(screen.queryByRole('heading', { level: 2, name: '構造チェック' })).toBeNull()
    expect(screen.getAllByRole('group', { name: '選択肢' })).toHaveLength(1)
  })
})
