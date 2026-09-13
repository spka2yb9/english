import { fireEvent, render, screen, within } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { KEYS, loadJson } from '../services/storage'
import { ReadingIndex, ReadingPassagePage } from './Reading'

function doneIds(): string[] {
  return loadJson<string[]>(KEYS.readingDone, [])
}

/** クイズを最後まで解き進める。 */
function finishQuiz() {
  for (;;) {
    const group = screen.queryByRole('group', { name: '選択肢' })
    if (!group) return
    fireEvent.click(within(group).getAllByRole('button')[0])
    fireEvent.click(screen.getByRole('button', { name: /次の問題へ|結果を見る/ }))
  }
}

describe('ReadingPassagePage', () => {
  it('クイズを解いただけでは読了にならず、ボタンで読了と取り消しができる', () => {
    localStorage.removeItem(KEYS.readingDone)
    render(
      <MemoryRouter initialEntries={['/reading/r-a2-03']}>
        <Routes>
          <Route path="/reading/:passageId" element={<ReadingPassagePage />} />
          <Route path="/reading" element={<p>多読一覧</p>} />
        </Routes>
      </MemoryRouter>,
    )

    finishQuiz()
    // 読了は本人の宣言で決める。クイズの完了で勝手に記録してはいけない。
    expect(doneIds()).toEqual([])

    fireEvent.click(screen.getByRole('button', { name: 'この本文を読了にする' }))
    expect(doneIds()).toEqual(['r-a2-03'])

    fireEvent.click(screen.getByRole('button', { name: '✓ 読了済み（取り消す）' }))
    expect(doneIds()).toEqual([])
  })
})

describe('ReadingIndex', () => {
  it('レベルの開閉状態を localStorage に保存し、再表示で復元する', () => {
    localStorage.clear()
    const { unmount } = render(
      <MemoryRouter>
        <ReadingIndex />
      </MemoryRouter>,
    )
    // 既定は最初の未読了レベル(A2)だけ開く
    expect(screen.getByText('A2').closest('details')).toHaveAttribute('open')
    expect(screen.getByText('B1').closest('details')).not.toHaveAttribute('open')

    // jsdom は summary クリックで details を開かないので、ブラウザ相当の状態変化を直接起こす
    const b1 = screen.getByText('B1').closest('details') as HTMLDetailsElement
    b1.open = true
    fireEvent(b1, new Event('toggle'))
    expect(loadJson<string[]>(KEYS.readingOpen, [])).toEqual(['A2', 'B1'])
    unmount()

    render(
      <MemoryRouter>
        <ReadingIndex />
      </MemoryRouter>,
    )
    expect(screen.getByText('B1').closest('details')).toHaveAttribute('open')
  })
})
