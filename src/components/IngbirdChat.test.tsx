import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { findLesson } from '../content/grammar'
import { IngbirdChat } from './IngbirdChat'

function renderChat(id = 'u01-l1') {
  const lesson = findLesson(id)
  if (!lesson) throw new Error(`レッスンが見つかりません: ${id}`)
  return render(<IngbirdChat lesson={lesson} thinkingMs={0} rng={() => 0} />)
}

function open() {
  fireEvent.click(screen.getByRole('button', { name: 'イングバードにこのセクションを質問する' }))
  return screen.getByRole('dialog')
}

function ask(question: string) {
  fireEvent.change(screen.getByRole('textbox', { name: '質問を入力' }), { target: { value: question } })
  fireEvent.click(screen.getByRole('button', { name: '送る' }))
}

describe('IngbirdChat', () => {
  it('右下のボタンから開くと、このセクションのあいさつと質問候補が出る', async () => {
    renderChat()
    expect(screen.queryByRole('dialog')).toBeNull()

    const dialog = open()
    expect(dialog).toHaveTextContent('be動詞の現在形')
    expect(dialog).toHaveTextContent('ぜんぶ読んであるよ')
    expect(screen.getByRole('button', { name: '何を習うの?' })).toBeInTheDocument()
    await waitFor(() => expect(screen.getByRole('textbox', { name: '質問を入力' })).toHaveFocus())
  })

  it('質問すると、コーパスから引用つきで答える', async () => {
    renderChat()
    open()
    ask('まとめを教えて')

    expect(await screen.findByText(/do \/ does は使わない/)).toBeInTheDocument()
    expect(screen.getByText('まとめ')).toBeInTheDocument() // 引用の見出し
  })

  it('セクションで扱っていない質問には、正直に答えられないと伝えて候補を出す', async () => {
    renderChat()
    open()
    ask('今日の天気は?')

    expect(await screen.findByText(/見つけられなかった/)).toBeInTheDocument()
    // 候補チップは引き続き押せる
    expect(screen.getByRole('button', { name: '例文を教えて' })).toBeInTheDocument()
  })

  it('候補チップをタップすると、その場で質問が送られる', async () => {
    renderChat()
    open()
    fireEvent.click(screen.getByRole('button', { name: '何を習うの?' }))

    expect(await screen.findByText('何を習うの?')).toBeInTheDocument() // ユーザーの吹き出し
    expect(await screen.findByText(/am \/ is \/ are/)).toBeInTheDocument() // 目標の引用
  })

  it('対比のあるセクションでは、使い分けの質問に例文つきで答える', async () => {
    renderChat('u01-l2')
    open()
    ask('-s が付くときと付かないときの区別は?')

    expect(await screen.findByText('-s が付く(3人称単数)')).toBeInTheDocument()
  })

  it('閉じるボタンで閉じられる', () => {
    renderChat()
    open()
    fireEvent.click(screen.getByRole('button', { name: 'チャットを閉じる' }))
    expect(screen.queryByRole('dialog')).toBeNull()
  })
})
