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

// 英文法ページは一時的に非公開にしているため、ルートのテストも停止する。
// 再開するときは以下の describe を戻す。
/*
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
*/

describe('3分間Englishのルーティング', () => {
  it('/three-minute は会話形式の英文法一覧を表示する', async () => {
    visit('/three-minute')
    expect(await screen.findByRole('heading', { level: 1, name: '3分間English' })).toBeInTheDocument()
  })

  it('/three-minute/:lessonId は先生と生徒の会話を表示する', async () => {
    visit('/three-minute/u01-l1')
    expect(await screen.findByRole('heading', { level: 1, name: 'be動詞の現在形' })).toBeInTheDocument()
    expect(document.querySelectorAll('.tm-turn').length).toBeGreaterThan(10)
  })
})
