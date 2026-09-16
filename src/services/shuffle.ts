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

/**
 * 重み付きで重複なしに count 件抽出する。重みが大きい要素ほど選ばれやすい。
 * 要素ごとに `rng^(1/重み)` を振り、大きい順に取る(Efraimidis–Spirakis 法)。
 * 重みが全て同じなら sample と同じ確率になる。
 */
export function weightedSample<T>(
  items: readonly T[],
  weightOf: (item: T) => number,
  count: number,
  rng: () => number = Math.random,
): T[] {
  if (count <= 0) return []
  return items
    .map((item) => ({ item, key: rng() ** (1 / Math.max(weightOf(item), 0.001)) }))
    .sort((a, b) => b.key - a.key)
    .slice(0, count)
    .map((entry) => entry.item)
}
