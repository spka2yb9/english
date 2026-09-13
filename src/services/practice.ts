// 音声練習セッションの組み立て。語彙と同じSRS(vocabSelection)を、文にもそのまま使う。
// 新しいスケジューラは作らない — 対象がIDで表せるなら同じ仕組みで足りる。

import { KEYS, loadJson, saveJson } from './storage.ts'
import { recordAnswer, selectSessionWords, type WordStats } from './vocabSelection.ts'
import { dictationSentences, sentenceBank, type BankSentence } from './sentenceBank.ts'

export type PracticeMode = 'shadowing' | 'dictation'

export const PRACTICE_SIZE = 8

/** モードごとに出題できる文の母集団。ディクテーションはTTSで安定して読める文だけに絞る。 */
export function poolFor(mode: PracticeMode): BankSentence[] {
  return mode === 'dictation' ? dictationSentences : sentenceBank
}

function statsKey(mode: PracticeMode): string {
  return `${KEYS.practiceStats}.${mode}`
}

export function getPracticeStats(mode: PracticeMode): WordStats {
  return loadJson<WordStats>(statsKey(mode), {})
}

export function recordPracticeAnswer(mode: PracticeMode, sentenceId: string, correct: boolean): void {
  saveJson(statsKey(mode), recordAnswer(getPracticeStats(mode), sentenceId, correct))
}

/** SRSで次に出す文を選ぶ。 */
export function selectPracticeSentences(mode: PracticeMode, count: number = PRACTICE_SIZE): BankSentence[] {
  const pool = poolFor(mode)
  const ids = selectSessionWords(
    pool.map((s) => s.id),
    getPracticeStats(mode),
    Date.now(),
    Math.min(count, pool.length),
  )
  const byId = new Map(pool.map((s) => [s.id, s]))
  return ids.map((id) => byId.get(id)).filter((s): s is BankSentence => s !== undefined)
}
