import { useState } from 'react'
import type { IngbirdOutfit } from '../../content/ingbird/outfits'
import { evolutionFor, type IngbirdEvolution } from '../../services/ingbirdEvolution'
import { getOutfit } from '../../services/ingbirdWardrobe'
import { getStudyStatus } from '../../services/studyDays'

export type IngbirdAppearance = {
  evolution: IngbirdEvolution
  outfit: IngbirdOutfit
}

/**
 * 保存済みの着せかえと学習日トータルの進化段階を、画面を開いた時点で1回だけ読む。
 * 英文法チャットやホームと同じ姿で先生を表示するために使う。
 */
export function useIngbirdAppearance(): IngbirdAppearance {
  const [appearance] = useState<IngbirdAppearance>(() => ({
    evolution: evolutionFor(getStudyStatus().totalDays),
    outfit: getOutfit(),
  }))
  return appearance
}
