// 「イングバードにきく」のモンキーテスト。
//
// 大量の質問を機械生成して投げ、次を検査する:
// 1. ハード不変条件(壊れたら不具合):
//    - 例外を投げない / 回答の形が正しい(引用が空でない・プレースホルダが残っていない)
//    - 回答の引用は必ずそのセクションの教材データ由来である(捏造していない)
//    - 同じ質問を新しい会話で2回投げたら同じ回答(決定的)
//    - 文脈フォローアップの約束(「もっと詳しく」は必ず答える、「それの意味は?」は直前が英文+和訳なら意味で答える)
// 2. ソフト品質(このテストが失敗一覧を出すので、人が見て直す):
//    - 質問の言い回しを揺らしても、元のQAの引用で答える(表記ゆれ・丁寧語・同義の言い換え)
//    - 範囲外の質問(未知語・他言語)には答えない
//
// 乱数はシード固定で再現できる。出力は MONKEY 行に集計、MONKEY_FAILURES に代表例。

import { describe, expect, it } from 'vitest'
import { allLessons } from '../../content/grammar'
import type { GrammarLesson } from '../../content/types'
import { buildSectionQa } from './corpus'
import { createSectionChat, normalizeQuestion } from './matcher'
import type { ChatReply, QaEntry } from './types'

/** 決定的な乱数(シード固定で再現可能)。 */
function mulberry32(seed: number): () => number {
  let state = seed >>> 0
  return () => {
    state = (state + 0x6d2b79f5) >>> 0
    let t = state
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

function replyText(reply: ChatReply): string {
  if (reply.kind === 'fallback') return reply.message
  return [
    reply.lead,
    ...reply.quotes.flatMap((quote) => [quote.label, quote.en ?? '', quote.ja ?? '', quote.note ?? '', quote.text ?? '']),
    ...reply.followups,
  ].join('\n')
}

function snippetsOf(entry: QaEntry): string[] {
  const lines = entry.answer.quotes
    .flatMap((quote) => [quote.en ?? '', quote.ja ?? '', quote.text ?? ''])
    .flatMap((text) => text.split('\n'))
    .map((line) => line.trim())
    .filter((line) => line.length >= 6)
  return [...new Set(lines)].sort((a, b) => b.length - a.length).slice(0, 3)
}

/** 引用の照合用に、表記ゆれ(全角半角・大小・空白・句読点・Markdown/JSON記号)を落とす。 */
function canonical(text: string): string {
  return text
    .normalize('NFKC')
    .toLowerCase()
    .replace(/[*_`\\]/g, '')
    .replace(/[\s「」『』（）()[\]【】。、．，！？!?…・:：;；"“”'’→|]/g, '')
}

function lessonSource(lesson: GrammarLesson): string {
  return canonical(JSON.stringify(lesson))
}

/** 引用の断片が教材データに実在するか(生成時の結合記号で分割して検査)。 */
function quoteIsFromLesson(lessonSourceText: string, quote: { en?: string; ja?: string; note?: string; text?: string }): boolean {
  const raw = [quote.en ?? '', quote.ja ?? '', quote.note ?? '', quote.text ?? ''].filter(Boolean).join('\n')
  const fragments = raw
    .split(/\n| → | \| | — |・|: |\/|（|）|\(|\)|「|」|『|』/)
    .map((fragment) => fragment.replace(/^\s*\d+\.\s*/, '').trim())
    .filter((fragment) => fragment.length >= 4)
  // 生成時に複数の文を並べた引用(クイズ一覧など)は、文単位に分けて実在を確認する
  const pieceExists = (piece: string): boolean =>
    lessonSourceText.includes(canonical(piece)) ||
    piece
      .split(/[。．.!?！？]/)
      .map((sentence) => sentence.trim())
      .filter((sentence) => sentence.length >= 4)
      .every((sentence) => lessonSourceText.includes(canonical(sentence)))
  return fragments.every(pieceExists)
}

/** 意味を保つ範囲の表記ゆれ・言い換えを作る。 */
const MUTATIONS: ReadonlyArray<(question: string) => string> = [
  (question) => question.replace(/[?？]$/, ''),
  (question) => `  ${question}  `,
  (question) => `ねえ、${question}`,
  (question) => `すみません、${question}`,
  (question) => `ちょっと教えて、${question}`,
  (question) => question.replace(/[?？]$/, '。'),
  (question) => question.replace(/\s+/g, ' ').trim(),
  (question) => (question.length <= 10 ? question.replace(/(?<=[一-龯ァ-ヶ])とは\??$/, 'って何?') : question),
  (question) => question.replace(/の意味は\??$/, 'の意味を教えて'),
  (question) => question.replace(/の違いは\??$/, 'の使い分けは?'),
  (question) => question.replace(/例文/gu, '例'),
  (question) => question.replace(/を教えて\??$/, 'は何?'),
  (question) => question.replace(/って何\??$/, 'とは?'),
]

type Failure = { category: string; lesson: string; question: string; actual: string }

const NONSENSE_JA = ['ぴよぴよ', 'ぬるぽ', 'わくわく', 'もぐもぐ', 'きらきら', 'どきどき']
const NONSENSE_EN = ['blorptastic', 'zorblatt', 'flibbertigibbet', 'kerfuffle', 'what is the president of france?', 'write me a poem', 'translate this to klingon', 'how do i cook pasta?']

describe('イングバードにきくのモンキーテスト', () => {
  it(
    '大量の質問で、壊れず・捏造せず・文脈に一貫して答える',
    () => {
      const rnd = mulberry32(20261006)
      const hardFailures: Failure[] = []
      const softFailures: Failure[] = []
      const metrics = {
        base: 0,
        baseOk: 0,
        mutation: 0,
        mutationOk: 0,
        outOfScope: 0,
        outOfScopeFallback: 0,
        chatty: 0,
        chattyFallback: 0,
        replies: 0,
      }
      const sampleOutOfScope: string[] = []

      const checkShape = (lessonId: string, question: string, reply: ChatReply, category: string): boolean => {
        metrics.replies += 1
        const text = replyText(reply)
        if (text.includes('{') || text.includes('}')) {
          hardFailures.push({ category: `${category}/プレースホルダ`, lesson: lessonId, question, actual: text.slice(0, 80) })
          return false
        }
        if (reply.kind === 'answer') {
          if (reply.quotes.length === 0) {
            hardFailures.push({ category: `${category}/引用なし`, lesson: lessonId, question, actual: reply.lead.slice(0, 80) })
            return false
          }
          if (!reply.lead.trim() || reply.followups.length === 0) {
            hardFailures.push({ category: `${category}/形`, lesson: lessonId, question, actual: reply.lead.slice(0, 80) })
            return false
          }
          for (const quote of reply.quotes) {
            if (!quote.en && !quote.ja && !quote.note && !quote.text) {
              hardFailures.push({ category: `${category}/空引用`, lesson: lessonId, question, actual: JSON.stringify(quote).slice(0, 80) })
              return false
            }
          }
        } else if (reply.suggestions.length === 0) {
          hardFailures.push({ category: `${category}/候補なし`, lesson: lessonId, question, actual: reply.message.slice(0, 80) })
          return false
        }
        return true
      }

      for (const lesson of allLessons) {
        const entries = buildSectionQa(lesson)
        if (entries.length === 0) continue
        const source = lessonSource(lesson)
        const chat = createSectionChat(lesson, () => 0)
        const questionCount = new Map<string, number>()
        for (const entry of entries) {
          for (const question of entry.questions) {
            const key = normalizeQuestion(question)
            questionCount.set(key, (questionCount.get(key) ?? 0) + 1)
          }
        }
        const uniqueEntries = entries.filter(
          (entry) =>
            entry.intent !== 'greeting' &&
            entry.intent !== 'capability' &&
            entry.answer.quotes.length > 0 &&
            entry.questions.some((question) => (questionCount.get(normalizeQuestion(question)) ?? 0) === 1),
        )
        const sample = uniqueEntries
          .map((entry) => ({ entry, sort: rnd() }))
          .sort((a, b) => a.sort - b.sort)
          .slice(0, 24)
          .map((item) => item.entry)

        for (const entry of sample) {
          const question = entry.questions.filter((candidate) => (questionCount.get(normalizeQuestion(candidate)) ?? 0) === 1)[
            Math.floor(rnd() * entry.questions.filter((candidate) => (questionCount.get(normalizeQuestion(candidate)) ?? 0) === 1).length)
          ]
          const snippets = snippetsOf(entry)

          // === base: 登録済みの言い回し ===
          chat.reset()
          const baseReply = chat.reply(question)
          metrics.base += 1
          if (!checkShape(lesson.id, question, baseReply, 'base')) continue
          if (baseReply.kind !== 'answer') {
            hardFailures.push({ category: 'base/フォールバック', lesson: lesson.id, question, actual: 'fallback' })
            continue
          }
          for (const quote of baseReply.quotes) {
            if (!quoteIsFromLesson(source, quote)) {
              hardFailures.push({ category: 'base/捏造', lesson: lesson.id, question, actual: JSON.stringify(quote).slice(0, 100) })
            }
          }
          const baseOk = baseReply.intent === entry.intent && snippets.some((snippet) => replyText(baseReply).includes(snippet))
          if (baseOk) metrics.baseOk += 1
          else
            softFailures.push({
              category: 'base/不一致',
              lesson: lesson.id,
              question,
              actual: `${baseReply.intent}/${replyText(baseReply).replace(/\n/g, ' ').slice(0, 70)}`,
            })

          // === mutation: 表記ゆれ・丁寧語・言い換え(2通り) ===
          for (let attempt = 0; attempt < 2; attempt += 1) {
            const mutationIndex = Math.floor(rnd() * MUTATIONS.length)
            const mutation = MUTATIONS[mutationIndex](question)
            if (mutation === question) continue
            chat.reset()
            const mutated = chat.reply(mutation)
            metrics.mutation += 1
            if (!checkShape(lesson.id, mutation, mutated, 'mutation')) continue
            if (mutated.kind !== 'answer') {
              softFailures.push({ category: 'mutation/フォールバック', lesson: lesson.id, question: mutation, actual: 'fallback' })
            } else {
              for (const quote of mutated.quotes) {
                if (!quoteIsFromLesson(source, quote)) {
                  hardFailures.push({ category: 'mutation/捏造', lesson: lesson.id, question: mutation, actual: JSON.stringify(quote).slice(0, 100) })
                }
              }
              const ok = mutated.intent === entry.intent && snippets.some((snippet) => replyText(mutated).includes(snippet))
              if (ok) metrics.mutationOk += 1
              else
                softFailures.push({
                  category: 'mutation/不一致',
                  lesson: lesson.id,
                  question: mutation,
                  actual: `${mutated.intent}/${replyText(mutated).replace(/\n/g, ' ').slice(0, 70)}`,
                })
            }
          }
        }

        // === 文脈フォローアップ ===
        const FOLLOWUPS = ['もっと詳しく', 'もう一度', 'それの意味は?', 'この文の文型は?', '他には?', 'なぜ?', '例文は?', 'まとめは?']
        for (let chain = 0; chain < 5 && sample.length > 0; chain += 1) {
          const entry = sample[Math.floor(rnd() * sample.length)]
          const question = entry.questions[0]
          chat.reset()
          const first = chat.reply(question)
          metrics.chatty += 1
          if (!checkShape(lesson.id, question, first, 'chain')) continue
          const firstHasExample = first.kind === 'answer' && first.quotes.some((quote) => quote.en && quote.ja)
          const follow = FOLLOWUPS[Math.floor(rnd() * FOLLOWUPS.length)]
          const reply = chat.reply(follow)
          if (!checkShape(lesson.id, `${question} → ${follow}`, reply, 'chain')) continue
          if (reply.kind === 'fallback') {
            metrics.chattyFallback += 1
          } else {
            for (const quote of reply.quotes) {
              if (!quoteIsFromLesson(source, quote)) {
                hardFailures.push({
                  category: 'chain/捏造',
                  lesson: lesson.id,
                  question: `${question} → ${follow}`,
                  actual: JSON.stringify(quote).slice(0, 100),
                })
              }
            }
          }
          // ハード不変条件: 「もっと詳しく」「もう一度」は必ず答える
          if ((follow === 'もっと詳しく' || follow === 'もう一度') && reply.kind !== 'answer') {
            hardFailures.push({ category: 'chain/フォロー無応答', lesson: lesson.id, question: `${question} → ${follow}`, actual: 'fallback' })
          }
          // ハード不変条件: 直前が英文+和訳なら「それの意味は?」は意味で答える
          if (follow === 'それの意味は?' && firstHasExample && (reply.kind !== 'answer' || reply.intent !== 'meaning')) {
            hardFailures.push({
              category: 'chain/意味解決',
              lesson: lesson.id,
              question: `${question} → ${follow}`,
              actual: reply.kind === 'answer' ? reply.intent : 'fallback',
            })
          }
        }

        // === 範囲外の質問 ===
        for (let index = 0; index < 10; index += 1) {
          const nonsense = rnd() < 0.5 ? `${NONSENSE_JA[Math.floor(rnd() * NONSENSE_JA.length)]}とは?` : NONSENSE_EN[Math.floor(rnd() * NONSENSE_EN.length)]
          chat.reset()
          const reply = chat.reply(nonsense)
          metrics.outOfScope += 1
          if (!checkShape(lesson.id, nonsense, reply, 'out-of-scope')) continue
          if (reply.kind === 'fallback') {
            metrics.outOfScopeFallback += 1
          } else if (sampleOutOfScope.length < 30) {
            sampleOutOfScope.push(`${lesson.id} "${nonsense}" -> ${reply.intent}/${replyText(reply).replace(/\n/g, ' ').slice(0, 60)}`)
          }
        }
      }

      // === 決定性: 同じ質問を別の会話で2回 ===
      let determinism = 0
      for (const lesson of allLessons) {
        const entries = buildSectionQa(lesson)
        const entry = entries.find((candidate) => candidate.questions[0] && candidate.answer.quotes.length > 0)
        if (!entry) continue
        const question = entry.questions[0]
        const a = createSectionChat(lesson, () => 0).reply(question)
        const b = createSectionChat(lesson, () => 0).reply(question)
        determinism += 1
        if (replyText(a) !== replyText(b) || a.kind !== b.kind || (a.kind === 'answer' && b.kind === 'answer' && a.intent !== b.intent)) {
          hardFailures.push({ category: 'determinism', lesson: lesson.id, question, actual: '2回で回答が違う' })
        }
      }

      const report = {
        ...metrics,
        determinism,
        baseRate: metrics.base > 0 ? `${((metrics.baseOk / metrics.base) * 100).toFixed(1)}%` : '-',
        mutationRate: metrics.mutation > 0 ? `${((metrics.mutationOk / metrics.mutation) * 100).toFixed(1)}%` : '-',
        outOfScopeFallbackRate: metrics.outOfScope > 0 ? `${((metrics.outOfScopeFallback / metrics.outOfScope) * 100).toFixed(1)}%` : '-',
        chattyFallbackRate: metrics.chatty > 0 ? `${((metrics.chattyFallback / metrics.chatty) * 100).toFixed(1)}%` : '-',
        hardFailures: hardFailures.length,
        softFailures: softFailures.length,
      }
      console.log(`MONKEY ${JSON.stringify(report)}`)
      if (sampleOutOfScope.length > 0) console.log(`MONKEY_OUT_OF_SCOPE_ANSWERS:\n${sampleOutOfScope.join('\n')}`)
      const byCategory = new Map<string, number>()
      for (const failure of hardFailures) byCategory.set(failure.category, (byCategory.get(failure.category) ?? 0) + 1)
      console.log(
        `MONKEY_HARD_CATEGORIES: ${[...byCategory.entries()]
          .sort((a, b) => b[1] - a[1])
          .map(([category, count]) => `${category}=${count}`)
          .join(' ')}`,
      )
      const softByCategory = new Map<string, number>()
      for (const failure of softFailures) softByCategory.set(failure.category, (softByCategory.get(failure.category) ?? 0) + 1)
      console.log(
        `MONKEY_SOFT_CATEGORIES: ${[...softByCategory.entries()]
          .sort((a, b) => b[1] - a[1])
          .map(([category, count]) => `${category}=${count}`)
          .join(' ')}`,
      )
      if (hardFailures.length > 0)
        console.log(
          `MONKEY_HARD_FAILURES:\n${hardFailures
            .slice(0, 60)
            .map((failure) => `${failure.category} ${failure.lesson} "${failure.question}" -> ${failure.actual}`)
            .join('\n')}`,
        )
      if (softFailures.length > 0)
        console.log(`MONKEY_SOFT_FAILURES:\n${softFailures.slice(0, 60).map((failure) => `${failure.category} ${failure.lesson} "${failure.question}" -> ${failure.actual}`).join('\n')}`)

      expect(hardFailures).toEqual([])
      expect(metrics.baseOk / metrics.base).toBeGreaterThanOrEqual(0.99)
      expect(metrics.mutationOk / metrics.mutation).toBeGreaterThanOrEqual(0.99)
      expect(metrics.outOfScopeFallback / metrics.outOfScope).toBeGreaterThanOrEqual(0.98)
    },
    300_000,
  )
})
