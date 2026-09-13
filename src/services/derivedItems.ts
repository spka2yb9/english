// 既存の英文から演習問題を実行時に組み立てる。
// 問題データを新規に持たないので、バンドルサイズを増やさずに演習量だけを増やせる。

import type { GrammarExample, GrammarLesson } from '../content/types.ts'
import { shuffle } from './shuffle.ts'

/** 並べ替えの素材になる英文。文バンクの文でもレッスンの例文でも渡せる。 */
export type WordOrderSentence = { en: string; ja: string }

export type WordOrderItem = {
  /** シャッフル済みの語(学習者が並べ替える) */
  tokens: string[]
  answer: string
  ja: string
}

/** 1セクションあたりの並べ替え問題数。例文10文がそのまま母集団になる。 */
export const LESSON_WORD_ORDER_SIZE = 10

/** 3語以下は並べ替えにならない。 */
const MIN_TOKENS = 4

/** タップ回数が現実的に収まる上限。超える文は候補の後ろへ回し、10問に足りないときだけ使う。 */
const COMFORTABLE_MAX_TOKENS = 16

function tokenCount(en: string): number {
  return en.trim().split(/\s+/).length
}

/** 並べ替え問題。元の語順に戻せれば正解。 */
export function buildWordOrderItem(
  sentence: WordOrderSentence,
  rng: () => number = Math.random,
): WordOrderItem {
  const tokens = sentence.en.trim().split(/\s+/)
  // 元の順序と同じ並びを出しても演習にならないため、2語以上あれば必ずずらす
  let shuffled = shuffle(tokens, rng)
  for (let attempt = 0; attempt < 5 && tokens.length > 1 && shuffled.join(' ') === tokens.join(' '); attempt++) {
    shuffled = shuffle(tokens, rng)
  }
  return { tokens: shuffled, answer: sentence.en, ja: sentence.ja }
}

/**
 * セクション1つぶんの並べ替え問題に使う英文を、そのセクション自身の例文から選ぶ。
 * 出題順は教材の掲載順のままにして、学んだ流れでそのまま産出練習へ移れるようにする。
 * 文バンク(語彙4,500語を含む)を経由しないので、文法ページのチャンクは軽いままになる。
 */
export function lessonWordOrderSentences(lesson: GrammarLesson): WordOrderSentence[] {
  const seen = new Set<string>()
  const candidates: WordOrderSentence[] = []

  for (const block of lesson.blocks) {
    const items: GrammarExample[] =
      block.type === 'examples'
        ? block.items
        : block.type === 'contrast'
          ? [...block.left.items, ...block.right.items]
          : []
    for (const item of items) {
      const key = item.en.toLowerCase()
      if (!item.ja || seen.has(key) || tokenCount(item.en) < MIN_TOKENS) continue
      seen.add(key)
      candidates.push({ en: item.en, ja: item.ja })
    }
  }

  return [
    ...candidates.filter((s) => tokenCount(s.en) <= COMFORTABLE_MAX_TOKENS),
    ...candidates.filter((s) => tokenCount(s.en) > COMFORTABLE_MAX_TOKENS),
  ].slice(0, LESSON_WORD_ORDER_SIZE)
}
