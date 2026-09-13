import { describe, expect, it } from 'vitest'
import { sample, shuffle } from './shuffle'

/** 決定的な疑似乱数(テスト用) */
function seededRng(seed: number): () => number {
  let s = seed
  return () => {
    s = (s * 1664525 + 1013904223) % 4294967296
    return s / 4294967296
  }
}

describe('shuffle', () => {
  it('元配列を変更せず、同じ要素の順列を返す', () => {
    const original = [1, 2, 3, 4, 5]
    const result = shuffle(original, seededRng(1))
    expect(original).toEqual([1, 2, 3, 4, 5])
    expect([...result].sort()).toEqual([1, 2, 3, 4, 5])
  })

  it('rng によって順序が変わる(恒等でないシャッフルが存在する)', () => {
    const items = Array.from({ length: 20 }, (_, i) => i)
    const a = shuffle(items, seededRng(1))
    const b = shuffle(items, seededRng(42))
    expect(a).not.toEqual(b)
  })

  it('空配列・1要素でも動作する', () => {
    expect(shuffle([])).toEqual([])
    expect(shuffle(['a'])).toEqual(['a'])
  })
})

describe('sample', () => {
  it('重複なしで指定件数を返す', () => {
    const items = Array.from({ length: 100 }, (_, i) => `w${i}`)
    const result = sample(items, 10, seededRng(7))
    expect(result).toHaveLength(10)
    expect(new Set(result).size).toBe(10)
    for (const w of result) expect(items).toContain(w)
  })

  it('要素数より多く要求しても全件のみ返す', () => {
    expect(sample([1, 2, 3], 10, seededRng(1))).toHaveLength(3)
  })
})
