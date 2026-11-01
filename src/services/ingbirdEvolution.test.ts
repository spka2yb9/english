import { describe, expect, it } from 'vitest'
import { EVOLUTIONS, evolutionFor, evolutionInfo } from './ingbirdEvolution'

describe('イングバードの進化', () => {
  it('学習日トータルの節目で段階が上がる', () => {
    expect(evolutionFor(0)).toBe(0)
    expect(evolutionFor(2)).toBe(0)
    expect(evolutionFor(3)).toBe(1)
    expect(evolutionFor(6)).toBe(1)
    expect(evolutionFor(7)).toBe(2)
    expect(evolutionFor(29)).toBe(2)
    expect(evolutionFor(30)).toBe(3)
    expect(evolutionFor(99)).toBe(3)
    expect(evolutionFor(100)).toBe(4)
    expect(evolutionFor(364)).toBe(4)
    expect(evolutionFor(365)).toBe(5)
    expect(evolutionFor(1000)).toBe(5)
  })

  it('段階は下がらず、休んでも失わない(トータル日数の関数)', () => {
    let previous = 0
    for (let days = 0; days <= 400; days += 1) {
      const stage = evolutionFor(days)
      expect(stage).toBeGreaterThanOrEqual(previous)
      previous = stage
    }
  })

  it('一覧は連番で、ラベルと説明がそろっている', () => {
    EVOLUTIONS.forEach((info, index) => {
      expect(info.stage).toBe(index)
      expect(info.label.length).toBeGreaterThan(0)
      expect(info.description.length).toBeGreaterThan(5)
      if (index > 0) expect(info.minDays).toBeGreaterThan(EVOLUTIONS[index - 1].minDays)
    })
    expect(evolutionInfo(4)).toBe(EVOLUTIONS[4])
  })
})
