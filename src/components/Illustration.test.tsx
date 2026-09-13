import { act, fireEvent, render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it, vi } from 'vitest'
import { Illustration } from './Illustration'
import { lessonIllustrations } from '../content/grammar/illustrations'
import { LESSON_ANIMATIONS } from '../content/grammar/animations'
import { allLessons } from '../content/grammar'

function renderLesson(sceneId = 'u01-l1') {
  return render(<Illustration sceneId={sceneId} {...lessonIllustrations[sceneId]} />)
}

afterEach(() => { vi.useRealTimers(); vi.unstubAllGlobals() })

describe('Illustration', () => {
  it('全117セクションに内容に合った3段階のアニメーションがある', () => {
    expect(Object.keys(LESSON_ANIMATIONS).sort()).toEqual(allLessons.map((lesson) => lesson.id).sort())
    for (const animation of Object.values(LESSON_ANIMATIONS)) {
      expect(animation.steps).toHaveLength(3)
      for (const step of animation.steps) {
        expect(step.sentence.length).toBeGreaterThan(0)
        expect(step.note.length).toBeGreaterThan(5)
      }
    }
  })

  it('全セクションの全段階を表示でき、図と説明を読み上げられる', () => {
    for (const [sceneId, animation] of Object.entries(LESSON_ANIMATIONS)) {
      const { container, unmount } = renderLesson(sceneId)
      for (let index = 0; index < 3; index++) {
        fireEvent.click(screen.getByRole('button', { name: new RegExp(`^ステップ${index + 1}:`) }))
        const step = animation.steps[index]
        expect(container.querySelector('.grammar-animation-sentence')).toHaveTextContent(step.sentence.replaceAll('|', ' '))
        expect(screen.getByRole('img')).toHaveAccessibleName(expect.stringContaining(step.note))
        expect(container.querySelector('[data-scene]')).toHaveAttribute('data-scene', sceneId)
      }
      unmount()
    }
  })

  it('既定では停止しており、再生を一時停止・再開し、最後で停止して再生し直せる', () => {
    vi.useFakeTimers()
    renderLesson()
    act(() => vi.advanceTimersByTime(10000))
    expect(screen.getByRole('button', { name: /^ステップ1:/ })).toHaveAttribute('aria-current', 'step')
    fireEvent.click(screen.getByRole('button', { name: '再生' }))
    act(() => vi.advanceTimersByTime(4200))
    expect(screen.getByRole('button', { name: /^ステップ2:/ })).toHaveAttribute('aria-current', 'step')
    fireEvent.click(screen.getByRole('button', { name: '一時停止' }))
    act(() => vi.advanceTimersByTime(10000))
    expect(screen.getByRole('button', { name: /^ステップ2:/ })).toHaveAttribute('aria-current', 'step')
    fireEvent.click(screen.getByRole('button', { name: '再生' }))
    act(() => vi.advanceTimersByTime(4200))
    act(() => vi.advanceTimersByTime(4200))
    expect(screen.getByRole('button', { name: '次へ' })).toBeDisabled()
    fireEvent.click(screen.getByRole('button', { name: 'もう一度' }))
    expect(screen.getByRole('button', { name: /^ステップ1:/ })).toHaveAttribute('aria-current', 'step')
  })

  it('動きを減らす設定では自動再生せず、手動で段階を読める', () => {
    vi.useFakeTimers()
    vi.stubGlobal('matchMedia', () => ({ matches: true, addEventListener: vi.fn(), removeEventListener: vi.fn() }))
    renderLesson()
    expect(screen.getByRole('button', { name: '再生' })).toBeInTheDocument()
    act(() => vi.advanceTimersByTime(10000))
    expect(screen.getByRole('button', { name: /^ステップ1:/ })).toHaveAttribute('aria-current', 'step')
    fireEvent.click(screen.getByRole('button', { name: '次へ' }))
    expect(screen.getByRole('button', { name: /^ステップ2:/ })).toHaveAttribute('aria-current', 'step')
  })

  it('画面外では進まず、表示されたときに再生する', () => {
    vi.useFakeTimers()
    let intersect: (entries: { isIntersecting: boolean }[]) => void = () => {}
    const disconnect = vi.fn()
    vi.stubGlobal('IntersectionObserver', class {
      constructor(callback: typeof intersect) { intersect = callback }
      observe = vi.fn()
      disconnect = disconnect
    })
    const { unmount } = renderLesson()
    act(() => vi.advanceTimersByTime(8400))
    expect(screen.getByRole('button', { name: /^ステップ1:/ })).toHaveAttribute('aria-current', 'step')
    fireEvent.click(screen.getByRole('button', { name: '再生' }))
    act(() => intersect([{ isIntersecting: true }]))
    act(() => vi.advanceTimersByTime(4200))
    expect(screen.getByRole('button', { name: /^ステップ2:/ })).toHaveAttribute('aria-current', 'step')
    act(() => intersect([{ isIntersecting: false }]))
    act(() => vi.advanceTimersByTime(8400))
    expect(screen.getByRole('button', { name: /^ステップ2:/ })).toHaveAttribute('aria-current', 'step')
    unmount()
    expect(disconnect).toHaveBeenCalledOnce()
  })

  it('同じ単語の要素を保持したまま疑問文の語順へ移動する', () => {
    const { container } = renderLesson()
    const is = [...container.querySelectorAll('.ga-word')].find((node) => node.querySelector('.ga-word-text')?.textContent === 'is')!
    const initialTransform = (is as SVGElement).style.transform
    fireEvent.click(screen.getByRole('button', { name: /^ステップ3:/ }))
    const moved = [...container.querySelectorAll('.ga-word')].find((node) => node.querySelector('.ga-word-text')?.textContent === 'Is')!
    expect(moved).toBe(is)
    expect((moved as SVGElement).style.transform).not.toBe(initialTransform)
  })
})
