// 語彙セッションの状態機械(純粋関数)。
// 仕様: 10語を出題 → わからなかった語だけを再出題 → 0語になるまで繰り返す。

export type VocabSessionState = {
  /** 1周目 = 1 */
  round: number
  /** 現在の周で出題する語ID */
  queue: string[]
  /** queue 内の現在位置 */
  index: number
  /** 現在の周でわからなかった語ID */
  unknownThisRound: string[]
  /** セッション全体でわからないと答えた回数(語ごとの重複含む) */
  totalUnknownAnswers: number
  finished: boolean
}

export function startSession(wordIds: string[]): VocabSessionState {
  return {
    round: 1,
    queue: wordIds,
    index: 0,
    unknownThisRound: [],
    totalUnknownAnswers: 0,
    finished: wordIds.length === 0,
  }
}

export function currentWordId(state: VocabSessionState): string | null {
  if (state.finished || state.index >= state.queue.length) return null
  return state.queue[state.index]
}

/** 「わかる(known=true) / わからない(known=false)」の回答を反映した新しい状態を返す。 */
export function answer(state: VocabSessionState, known: boolean): VocabSessionState {
  if (state.finished) return state
  const id = state.queue[state.index]
  const unknownThisRound = known ? state.unknownThisRound : [...state.unknownThisRound, id]
  const totalUnknownAnswers = state.totalUnknownAnswers + (known ? 0 : 1)
  const nextIndex = state.index + 1

  if (nextIndex < state.queue.length) {
    return { ...state, index: nextIndex, unknownThisRound, totalUnknownAnswers }
  }
  // 周の終わり: わからない語が残っていれば次の周へ、なければ完了
  if (unknownThisRound.length === 0) {
    return { ...state, index: nextIndex, unknownThisRound, totalUnknownAnswers, finished: true }
  }
  return {
    round: state.round + 1,
    queue: unknownThisRound,
    index: 0,
    unknownThisRound: [],
    totalUnknownAnswers,
    finished: false,
  }
}
