// 既存教材のクリーンな英文を一箇所に集約する。
// 音読・ディクテーション・和文英訳・並べ替えは、新規執筆をせずすべてここから作る。

import { allLessons } from '../content/grammar/index.ts'
import { allVocabulary } from '../content/vocabulary/index.ts'

export type BankLevel = 'A2' | 'B1' | 'B2'

export type BankSentence = {
  /** g:<lessonId>:<n> または v:<wordId> */
  id: string
  en: string
  ja: string
  level: BankLevel
  /** 学習の焦点(文法のハイライト語句、語彙の見出し語)。穴埋めに使う。 */
  focus?: string
  origin: 'grammar' | 'vocabulary'
}

/** A2+ / B1+ は近い基準レベルに丸める。 */
function baseLevel(level: string): BankLevel {
  if (level.startsWith('A2')) return 'A2'
  if (level.startsWith('B1')) return 'B1'
  return 'B2'
}

/**
 * TTSで安定して読める文か。
 * 数字・略語・記号は音声化が環境ごとにぶれるため、ディクテーションからは外す。
 */
export function isTtsFriendly(en: string): boolean {
  if (/[0-9]/.test(en)) return false
  if (/[()[\]/*_#—–"“”]/.test(en)) return false
  if (/\b[A-Z]{2,}\b/.test(en)) return false // 略語は綴り読みされる
  if (/\b[A-Z][a-z]{0,3}\.\s/.test(en)) return false // Mr. Dr. などの略号
  const words = en.trim().split(/\s+/)
  return words.length >= 4 && words.length <= 14
}

function grammarSentences(): BankSentence[] {
  const result: BankSentence[] = []
  for (const lesson of allLessons) {
    let n = 0
    for (const block of lesson.blocks) {
      const items =
        block.type === 'examples'
          ? block.items
          : block.type === 'contrast'
            ? [...block.left.items, ...block.right.items]
            : []
      for (const item of items) {
        if (!item.ja) continue
        result.push({
          id: `g:${lesson.id}:${n++}`,
          en: item.en,
          ja: item.ja,
          level: baseLevel(lesson.level),
          ...(item.highlight ? { focus: item.highlight } : {}),
          origin: 'grammar',
        })
      }
    }
  }
  return result
}

function vocabularySentences(): BankSentence[] {
  return allVocabulary.map((entry) => ({
    id: `v:${entry.id}`,
    en: entry.exampleSentence,
    ja: entry.exampleTranslationJa,
    level: entry.level,
    focus: entry.word,
    origin: 'vocabulary' as const,
  }))
}

/** 重複英文は最初の1件だけ残す(同じ文を別モードで何度も出さない)。 */
export const sentenceBank: BankSentence[] = (() => {
  const seen = new Set<string>()
  return [...grammarSentences(), ...vocabularySentences()].filter((s) => {
    const key = s.en.toLowerCase()
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
})()

export const dictationSentences: BankSentence[] = sentenceBank.filter((s) => isTtsFriendly(s.en))

const bankMap = new Map(sentenceBank.map((s) => [s.id, s]))

export function findSentence(id: string): BankSentence | undefined {
  return bankMap.get(id)
}
