import { describe, expect, it } from 'vitest'
import { sample, shuffle, weightedSample } from './shuffle'

/** 決定的な疑似乱数(テスト用)。mulberry32。 */
function seededRng(seed: number): () => number {
  let s = seed >>> 0
  return () => {
    s = (s + 0x6d2b79f5) >>> 0
    let t = Math.imul(s ^ (s >>> 15), 1 | s)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
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

describe('weightedSample', () => {
  const heavy = Array.from({ length: 10 }, (_, i) => `h${i}`)
  const light = Array.from({ length: 10 }, (_, i) => `l${i}`)
  const weightOf = (item: string) => (item.startsWith('h') ? 3 : 1)

  it('重複なしで指定件数を返す', () => {
    const result = weightedSample([...heavy, ...light], weightOf, 5, seededRng(7))
    expect(result).toHaveLength(5)
    expect(new Set(result).size).toBe(5)
  })

  it('重みが大きい要素ほど多く選ばれる', () => {
    let pickedHeavy = 0
    let pickedLight = 0
    for (let seed = 1; seed <= 200; seed++) {
      for (const item of weightedSample([...heavy, ...light], weightOf, 5, seededRng(seed))) {
        if (item.startsWith('h')) pickedHeavy++
        else pickedLight++
      }
    }
    // 重み 3:1 なら出現回数もおよそ 3:1 になる
    expect(pickedHeavy).toBeGreaterThan(pickedLight * 2)
  })

  it('重みが全て同じなら、どの要素も同確率で選ばれる', () => {
    const items = Array.from({ length: 20 }, (_, i) => `w${i}`)
    const counts = new Map<string, number>()
    for (let seed = 1; seed <= 200; seed++) {
      for (const item of weightedSample(items, () => 1, 5, seededRng(seed))) {
        counts.set(item, (counts.get(item) ?? 0) + 1)
      }
    }
    expect(counts.size).toBe(items.length)
    const values = [...counts.values()]
    expect(Math.max(...values)).toBeLessThan(Math.min(...values) * 3)
  })

  it('空配列・0件要求でも動作する', () => {
    expect(weightedSample([], () => 1, 5, seededRng(1))).toEqual([])
    expect(weightedSample([1, 2, 3], () => 1, 0, seededRng(1))).toEqual([])
  })
})
