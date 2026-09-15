// 音声練習の出題。記録するのは文ごとの実施回数だけで、その回数が少ない文から順に1周ずつ回す。
// 周回の位置を別に持たないので、実施回数さえ同期すれば端末をまたいでも続きの文から回せる。
// 問題数や終わりは決めない — 声に出す・書き取る反復の場なので、続けたいだけ続けられる。

import { KEYS, loadJson, saveJson } from './storage.ts'
import { dictationSentences, sentenceBank, type BankSentence } from './sentenceBank.ts'

export type PracticeMode = 'shadowing' | 'dictation'

/** 文IDごとの実施回数。周回の位置はこの数だけから決まる。 */
export type PracticeStats = Record<string, number>

/** モードごとに出題できる文の母集団。ディクテーションはTTSで安定して読める文だけに絞る。 */
export function poolFor(mode: PracticeMode): BankSentence[] {
  return mode === 'dictation' ? dictationSentences : sentenceBank
}

function statsKey(mode: PracticeMode): string {
  return `${KEYS.practiceStats}.${mode}`
}

/** 旧形式(WordStatオブジェクト)で残っている履歴も、実施回数として読み替える。 */
function countOf(value: unknown): number {
  if (typeof value === 'number') return value
  if (typeof value === 'object' && value !== null) {
    const seen = (value as { seen?: unknown }).seen
    if (typeof seen === 'number') return seen
  }
  return 0
}

export function getPracticeStats(mode: PracticeMode): PracticeStats {
  const raw = loadJson<Record<string, unknown>>(statsKey(mode), {})
  return Object.fromEntries(Object.entries(raw).map(([id, value]) => [id, countOf(value)]))
}

/** 1文の実施回数を1つ増やす。周回はこの回数だけを見て決まるので、ほかに記録するものはない。 */
export function recordPracticeAnswer(mode: PracticeMode, sentenceId: string): void {
  const stats = getPracticeStats(mode)
  saveJson(statsKey(mode), { ...stats, [sentenceId]: (stats[sentenceId] ?? 0) + 1 })
}

/**
 * 次の1文を引く。実施回数が最も少ない文(まだその周で出していない文)が候補になり、
 * 同数のものの中ではランダムに選ぶ。全員が同じ回数になったら次の周が始まる。
 * 直前の文は実施回数が1つ多いので、同じ文が2問続くことはない。
 */
export function drawPracticeSentence(
  mode: PracticeMode,
  stats: PracticeStats,
  rng: () => number = Math.random,
): BankSentence | undefined {
  const pool = poolFor(mode)
  if (pool.length === 0) return undefined

  let min = Infinity
  for (const sentence of pool) {
    const count = stats[sentence.id] ?? 0
    if (count < min) min = count
  }

  const candidates = pool.filter((sentence) => (stats[sentence.id] ?? 0) === min)
  return candidates[Math.floor(rng() * candidates.length)]
}
