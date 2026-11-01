import { beforeEach, describe, expect, it } from 'vitest'
import {
  allOutfitEntries,
  changeOutfit,
  daysToNextOutfitUnlock,
  DEFAULT_OUTFIT,
  isOutfitUnlocked,
  itemsUnlockedAt,
  nextOutfitUnlocks,
  OUTFIT_ITEMS,
  OUTFIT_SLOT_ORDER,
  OUTFIT_TOTAL,
  unlockedOutfitCount,
} from '../content/ingbird/outfits'
import { KEYS } from './storage'
import { getOutfit, saveOutfit } from './ingbirdWardrobe'

beforeEach(() => {
  localStorage.clear()
})

describe('着せかえの保存', () => {
  it('保存がなければ既定の姿になる', () => {
    expect(getOutfit()).toEqual(DEFAULT_OUTFIT)
  })

  it('保存した内容をそのまま読み戻せる', () => {
    const outfit = { glasses: 'sunglasses', hat: 'crown', effect: 'sakura', accessory: 'scarf', shoes: 'sneakers' } as const
    saveOutfit(outfit)
    expect(getOutfit()).toEqual(outfit)
  })

  it('壊れた保存データは、枠ごとに既定へ戻す', () => {
    localStorage.setItem(KEYS.ingbirdOutfit, JSON.stringify({ glasses: 'laser', hat: 'crown', effect: 42 }))
    expect(getOutfit()).toEqual({ ...DEFAULT_OUTFIT, hat: 'crown' })
  })

  it('JSONとして読めない値でも既定に戻る', () => {
    localStorage.setItem(KEYS.ingbirdOutfit, '{oops')
    expect(getOutfit()).toEqual(DEFAULT_OUTFIT)
  })

  it('知らない選択肢には着せかえない', () => {
    expect(changeOutfit(DEFAULT_OUTFIT, 'hat', 'space')).toEqual(DEFAULT_OUTFIT)
  })

  it('カタログは枠ごとにIDが一意で、ラベルと説明と解放日数がある', () => {
    expect(OUTFIT_TOTAL).toBeGreaterThanOrEqual(190)
    for (const items of Object.values(OUTFIT_ITEMS)) {
      expect(new Set(items.map((item) => item.id)).size).toBe(items.length)
      for (const item of items) {
        expect(item.label.length).toBeGreaterThan(0)
        expect(item.description.length).toBeGreaterThan(2)
        expect(Number.isInteger(item.unlockDays)).toBe(true)
        expect(item.unlockDays).toBeGreaterThanOrEqual(0)
      }
    }
  })

  it('アイテムは学習日トータルで解放され、1000日で全部そろう', () => {
    expect(unlockedOutfitCount(0)).toBeGreaterThan(0)
    expect(unlockedOutfitCount(0)).toBeLessThan(OUTFIT_TOTAL)
    expect(unlockedOutfitCount(1000)).toBe(OUTFIT_TOTAL)
    const all = OUTFIT_SLOT_ORDER.flatMap((slot) => OUTFIT_ITEMS[slot])
    expect(all.some((item) => isOutfitUnlocked(item, 0))).toBe(true)
    expect(all.some((item) => !isOutfitUnlocked(item, 0))).toBe(true)
  })

  it('次の解放アイテムは、同じ日に複数あればまとめて返す', () => {
    const next = nextOutfitUnlocks(0)
    expect(next.map(({ item }) => item.id).sort()).toEqual(['round', 'sparkle'])
    expect(next.every(({ item }) => item.unlockDays === 1)).toBe(true)
    expect(nextOutfitUnlocks(1000)).toEqual([])

    const at4 = nextOutfitUnlocks(4)
    expect(at4.length).toBeGreaterThan(0)
    expect(at4.every(({ item }) => item.unlockDays === 5)).toBe(true)
  })

  it('ダークファンタジー系は300日以降で解放される', () => {
    const dark = allOutfitEntries().filter(({ item }) => item.theme === 'dark')
    expect(dark.length).toBeGreaterThanOrEqual(30)
    expect(dark.every(({ item }) => item.unlockDays >= 300)).toBe(true)
    expect(dark.some(({ item }) => item.unlockDays === 300)).toBe(true)
    expect(dark.some(({ item }) => item.unlockDays === 1000)).toBe(true)
  })

  it('その日に新しく解放されるアイテムだけを返す', () => {
    expect(itemsUnlockedAt(2).map(({ item }) => item.id).sort()).toEqual(['beanie', 'drizzle', 'scarf'])
    expect(itemsUnlockedAt(4).map(({ item }) => item.id).sort()).toEqual(['bowtie', 'sneakers'])
    expect(itemsUnlockedAt(6).map(({ item }) => item.id).sort()).toEqual(['ribbon', 'straw', 'tinted'])
    expect(itemsUnlockedAt(19)).toEqual([])
    expect(itemsUnlockedAt(0).length).toBeGreaterThan(0)
  })

  it('次の解放までの残り日数を出す', () => {
    expect(daysToNextOutfitUnlock(0)).toBe(1)
    expect(daysToNextOutfitUnlock(4)).toBe(1)
    expect(daysToNextOutfitUnlock(1000)).toBeNull()
  })
})
