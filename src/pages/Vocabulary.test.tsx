import { fireEvent, render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

// 2語目は「絵のない語」の代表。8,000語すべてに絵がそろったので未登録の語は実データに
// もう無い。1語だけ絵を外したマップに差し替えて、絵がないときの表示を確かめる。
const { WITHOUT_IMAGE } = vi.hoisted(() => ({ WITHOUT_IMAGE: 'abandon' }))

vi.mock('../content/vocabulary/illustrations', async importOriginal => {
  const original = await importOriginal<typeof import('../content/vocabulary/illustrations')>()
  const { [WITHOUT_IMAGE]: _omitted, ...rest } = original.vocabularyIllustrations
  return { ...original, vocabularyIllustrations: rest }
})

vi.mock('../services/vocabSelection', async importOriginal => ({
  ...await importOriginal<typeof import('../services/vocabSelection')>(),
  selectSessionWords: () => ['absorb', WITHOUT_IMAGE],
}))
vi.mock('../components/AudioButton', () => ({ AudioButton: () => null }))

import { Vocabulary } from './Vocabulary'

/** 完了画面の「ホームに戻る」が Link なので Router 配下で描画する。 */
function renderVocabulary() {
  return render(
    <MemoryRouter>
      <Vocabulary />
    </MemoryRouter>,
  )
}

beforeEach(() => {
  localStorage.clear()
  vi.spyOn(window, 'scrollTo').mockImplementation(() => undefined)
})

afterEach(() => vi.restoreAllMocks())

describe('Vocabulary memory illustration', () => {
  it('回答後に該当単語の絵を覚えるヒント内へ表示する', () => {
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))
    expect(screen.queryByRole('img')).not.toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: 'わからない' }))
    const image = screen.getByRole('img', { name: /植物の根が/ })
    expect(image).toHaveAttribute('src', '/images/vocabulary/absorb.svg')
    expect(image.closest('details')).toHaveTextContent('覚えるヒント')
    expect(image.closest('details')).toHaveAttribute('open')
    fireEvent.click(screen.getByRole('button', { name: '次へ' }))
    expect(screen.queryByRole('img')).not.toBeInTheDocument()
    fireEvent.click(screen.getByRole('button', { name: 'わかる' }))
    expect(screen.queryByRole('img')).not.toBeInTheDocument()
    expect(screen.getByText('覚えるヒント')).toBeInTheDocument()
  })

  it('画像を読めなくても文章のヒントと次へ進む操作を残す', () => {
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))
    fireEvent.click(screen.getByRole('button', { name: 'わかる' }))
    fireEvent.error(screen.getByRole('img', { name: /植物の根が/ }))
    expect(screen.queryByRole('img')).not.toBeInTheDocument()
    expect(screen.getByText('記憶のコツ:')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: '次へ' })).toBeEnabled()
  })
})

describe('Vocabulary keyboard', () => {
  it('A/D で選択して F で決定、解説中の F で次の語に進む', async () => {
    const user = userEvent.setup()
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))

    await user.keyboard('d')
    expect(screen.getByRole('button', { name: 'わからない' })).toHaveFocus()
    await user.keyboard('a')
    expect(screen.getByRole('button', { name: 'わかる' })).toHaveFocus()

    await user.keyboard('f')
    expect(screen.getByText('「わかる」と答えました')).toBeInTheDocument()

    await user.keyboard('f')
    expect(screen.queryByRole('button', { name: '次へ' })).not.toBeInTheDocument()
    expect(screen.getByText('2 / 2語')).toBeInTheDocument()
  })

  it('選択していない F は何も決定しない', async () => {
    const user = userEvent.setup()
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))

    await user.keyboard('f')
    expect(screen.getByRole('button', { name: 'わかる' })).toBeInTheDocument()
    expect(screen.queryByText('「わかる」と答えました')).not.toBeInTheDocument()
  })
})

describe('Vocabulary scroll', () => {
  it('次の語に進むと画面を一番上へ戻す', () => {
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))
    fireEvent.click(screen.getByRole('button', { name: 'わかる' }))

    const scrollTo = vi.mocked(window.scrollTo)
    scrollTo.mockClear()
    fireEvent.click(screen.getByRole('button', { name: '次へ' }))

    expect(screen.getByText('2 / 2語')).toBeInTheDocument()
    expect(scrollTo).toHaveBeenCalledWith({ top: 0, left: 0, behavior: 'instant' })
  })

  it('解説を表示しただけではスクロール位置を変えない', () => {
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))

    const scrollTo = vi.mocked(window.scrollTo)
    scrollTo.mockClear()
    fireEvent.click(screen.getByRole('button', { name: 'わからない' }))

    expect(scrollTo).not.toHaveBeenCalled()
  })
})

describe('Vocabulary completion', () => {
  it('全問終わるとホームに戻るリンクを表示する', () => {
    renderVocabulary()
    fireEvent.click(screen.getByRole('button', { name: '5語クイズを始める' }))
    fireEvent.click(screen.getByRole('button', { name: 'わかる' }))
    fireEvent.click(screen.getByRole('button', { name: '次へ' }))
    fireEvent.click(screen.getByRole('button', { name: 'わかる' }))
    fireEvent.click(screen.getByRole('button', { name: '次へ' }))

    expect(screen.getByText('5語すべて確認できました!')).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'ホームに戻る' })).toHaveAttribute('href', '/')
    expect(screen.getByRole('button', { name: 'もう一度5語に挑戦する' })).toBeInTheDocument()
  })
})
