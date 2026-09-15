import { render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'

vi.mock('./services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import App from './App'

/** BrowserRouter は window.location を見るため、履歴を進めてから描画する。 */
function visit(path: string) {
  window.history.pushState({}, '', path)
  render(<App />)
}

describe('英文法のルーティング', () => {
  it('/grammar/roadmap は英文の作られ方のページを表示する(:lessonId と解釈しない)', async () => {
    visit('/grammar/roadmap')
    expect(await screen.findByRole('heading', { level: 1, name: '英文の作られ方から学ぶ' })).toBeInTheDocument()
    expect(screen.queryByText('レッスンが見つかりません')).toBeNull()
  })

  it('/grammar/:lessonId はこれまでどおりレッスンを表示する', async () => {
    visit('/grammar/u01-l1')
    expect(await screen.findByRole('heading', { level: 1, name: 'be動詞の現在形' })).toBeInTheDocument()
  })
})
