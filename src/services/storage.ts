// localStorage の型付きラッパー。ストレージ不可・破損データでもアプリは動作する。

import { progressKeys, schedulePush } from './sync'

export function loadJson<T>(key: string, fallback: T): T {
  try {
    const raw = localStorage.getItem(key)
    if (raw === null) return fallback
    return JSON.parse(raw) as T
  } catch {
    return fallback
  }
}

export function saveJson(key: string, value: unknown): void {
  try {
    localStorage.setItem(key, JSON.stringify(value))
    schedulePush() // 同期がオフなら即 return するだけ
  } catch {
    // ストレージ不可(プライベートモード等)でも学習は継続できる
  }
}

/**
 * 指定した接頭辞で始まる進捗キーを消す(音声練習のようなモード別キーもまとめて消えるように接頭辞で指定する)。
 * 同期の設定(トークン・保存先 Gist)は残すので、サインインしたままリセットでき、
 * 空になった状態がそのまま Gist にも反映される。
 */
export function resetProgress(prefixes: readonly string[]): void {
  try {
    for (const key of progressKeys()) {
      if (prefixes.some((prefix) => key.startsWith(prefix))) localStorage.removeItem(key)
    }
    schedulePush()
  } catch {
    // ストレージ不可なら消すものが無いだけ
  }
}

export const KEYS = {
  grammarProgress: 'eng.grammar.completed', // string[] レッスンID
  vocabStats: 'eng.vocab.stats', // Record<wordId, WordStat>
  vocabDaily: 'eng.vocab.daily', // VocabDay[] 1日1行の学習ログ(旧形式は { date, count })
  grammarItemStats: 'eng.grammar.items', // Record<questionId, WordStat> 文法問題のSRS
  practiceStats: 'eng.practice.stats', // Record<sentenceId, number> 音声練習の文の実施回数(周回の位置を兼ねる)
  readingDone: 'eng.reading.done', // string[] 読了した本文ID
  readingOpen: 'eng.reading.open', // string[] 多読一覧で開いているレベル
} as const
