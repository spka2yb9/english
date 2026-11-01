// イングバードの進化段階。学習日のトータルだけで決まる、見た目のごほうび。
// 連続日数ではないので、休んだ日があっても段階が下がることはない。

export type IngbirdEvolution = 0 | 1 | 2 | 3 | 4 | 5

export type EvolutionInfo = {
  stage: IngbirdEvolution
  /** この段階に入る学習日数(トータル)。 */
  minDays: number
  /** カードに出す短い名前。 */
  label: string
  /** 何が変わるかの説明。 */
  description: string
}

/** 段階の一覧。stage は配列の添字と一致させている。 */
export const EVOLUTIONS: readonly EvolutionInfo[] = [
  { stage: 0, minDays: 0, label: 'ふつう', description: 'まだふつうのイングバード。' },
  { stage: 1, minDays: 3, label: 'きらめき', description: '羽のまわりに金色のきらめきが出るよ。' },
  { stage: 2, minDays: 7, label: 'ゴールド覚醒', description: '頭に金色の羽が立ち、金色のオーラをまとうよ。' },
  { stage: 3, minDays: 30, label: '雷光', description: 'オーラが大きくなり、雷が走るよ。' },
  { stage: 4, minDays: 100, label: '異次元', description: '目が光り、岩が浮かぶ。異次元の風格。' },
  { stage: 5, minDays: 365, label: '伝説', description: '環が輝く、伝説のイングバード。' },
]

/** 学習日トータルから進化段階を求める。 */
export function evolutionFor(totalDays: number): IngbirdEvolution {
  let stage: IngbirdEvolution = 0
  for (const info of EVOLUTIONS) if (totalDays >= info.minDays) stage = info.stage
  return stage
}

/** 段階の表示情報。 */
export function evolutionInfo(stage: IngbirdEvolution): EvolutionInfo {
  return EVOLUTIONS[stage]
}
