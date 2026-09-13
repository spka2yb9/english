/** Fisher-Yates シャッフル。元配列は変更しない。rng は注入可能(テスト用)。 */
export function shuffle<T>(items: readonly T[], rng: () => number = Math.random): T[] {
  const result = [...items]
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1))
    ;[result[i], result[j]] = [result[j], result[i]]
  }
  return result
}

/** 重複なしで count 件をランダム抽出。 */
export function sample<T>(items: readonly T[], count: number, rng: () => number = Math.random): T[] {
  return shuffle(items, rng).slice(0, count)
}
