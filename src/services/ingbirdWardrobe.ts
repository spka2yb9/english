// 着せかえの保存。見た目だけの設定で、学習の進捗には影響しない。
// 壊れた値・知らないIDは、枠ごとに既定へ戻して読む(全部リセットしない)。

import {
  DEFAULT_OUTFIT,
  isOutfitId,
  type IngbirdOutfit,
  type OutfitSlot,
} from '../content/ingbird/outfits'
import { KEYS, loadJson, saveJson } from './storage'

/** 保存された着せかえを読む。不正な値は枠ごとに既定値へ。 */
export function getOutfit(): IngbirdOutfit {
  const raw = loadJson<Partial<Record<OutfitSlot, unknown>>>(KEYS.ingbirdOutfit, {})
  const pick = (slot: OutfitSlot): string => {
    const value = raw?.[slot]
    if (typeof value === 'string' && isOutfitId(slot, value)) return value
    return DEFAULT_OUTFIT[slot]
  }
  return {
    glasses: pick('glasses') as IngbirdOutfit['glasses'],
    hat: pick('hat') as IngbirdOutfit['hat'],
    effect: pick('effect') as IngbirdOutfit['effect'],
    accessory: pick('accessory') as IngbirdOutfit['accessory'],
    shoes: pick('shoes') as IngbirdOutfit['shoes'],
  }
}

/** 着せかえを保存する。 */
export function saveOutfit(outfit: IngbirdOutfit): void {
  saveJson(KEYS.ingbirdOutfit, outfit)
}
