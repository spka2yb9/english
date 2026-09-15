import { fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { beforeEach, describe, expect, it, vi } from 'vitest'

vi.mock('../services/sync', async () => {
  const actual = await vi.importActual<typeof import('../services/sync')>('../services/sync')
  return { ...actual, signedIn: () => false, push: vi.fn(), schedulePush: vi.fn() }
})

import { KEYS, saveJson } from '../services/storage'
import { Settings } from './Settings'

// jsdom は <dialog> の showModal/close を実装していないので、open 属性だけ再現する。
beforeEach(() => {
  HTMLDialogElement.prototype.showModal = function showModal() {
    this.open = true
  }
  HTMLDialogElement.prototype.close = function close() {
    this.open = false
    this.dispatchEvent(new Event('close'))
  }
  localStorage.clear()
  vi.stubGlobal('location', { ...window.location, reload: vi.fn() })
})

function renderPage() {
  return render(
    <MemoryRouter>
      <Settings />
    </MemoryRouter>,
  )
}

describe('Settings', () => {
  it('進捗がなければリセットボタンを出さない', () => {
    renderPage()
    expect(screen.queryByRole('button', { name: '選んだ進捗をリセットする' })).toBeNull()
    expect(screen.getByText('まだ保存された進捗はありません。')).toBeInTheDocument()
  })

  it('エリアを1つも選んでいなければリセットできない', () => {
    saveJson(KEYS.grammarProgress, ['u01-l1'])
    renderPage()
    expect(screen.getByRole('button', { name: '選んだ進捗をリセットする' })).toBeDisabled()
    expect(screen.getByRole('checkbox', { name: '多読' })).toBeDisabled() // 記録のないエリアは選べない
  })

  it('確認ダイアログでキャンセルすると進捗が残る', () => {
    saveJson(KEYS.grammarProgress, ['u01-l1', 'u01-l2'])
    renderPage()

    fireEvent.click(screen.getByRole('checkbox', { name: '文法' }))
    fireEvent.click(screen.getByRole('button', { name: '選んだ進捗をリセットする' }))
    expect(screen.getByRole('heading', { name: '選んだ進捗をリセットしますか?' })).toBeVisible()

    fireEvent.click(screen.getByRole('button', { name: 'キャンセル' }))
    expect(localStorage.getItem(KEYS.grammarProgress)).not.toBeNull()
  })

  it('選んだエリアだけを消し、ほかのエリアと同期の設定は残す', () => {
    saveJson(KEYS.grammarProgress, ['u01-l1'])
    saveJson(KEYS.grammarItemStats, { 'u01-l1-q1': { seen: 1 } })
    saveJson(`${KEYS.practiceStats}.dictation`, { s1: 1 }) // 動的キーも消える
    saveJson(KEYS.vocabStats, { apple: { seen: 1 } })
    saveJson(KEYS.readingDone, ['r01'])
    localStorage.setItem('eng.sync.token', 'ghp_dummy')

    renderPage()
    fireEvent.click(screen.getByRole('checkbox', { name: '文法' }))
    fireEvent.click(screen.getByRole('checkbox', { name: '音声練習' }))
    fireEvent.click(screen.getByRole('button', { name: '選んだ進捗をリセットする' }))
    fireEvent.click(screen.getByRole('button', { name: 'リセットする' }))

    expect(localStorage.getItem(KEYS.grammarProgress)).toBeNull()
    expect(localStorage.getItem(KEYS.grammarItemStats)).toBeNull()
    expect(localStorage.getItem(`${KEYS.practiceStats}.dictation`)).toBeNull()
    expect(localStorage.getItem(KEYS.vocabStats)).not.toBeNull()
    expect(localStorage.getItem(KEYS.readingDone)).not.toBeNull()
    expect(localStorage.getItem('eng.sync.token')).toBe('ghp_dummy')
  })
})
