// 全レッスン横断の自己整合テスト。
//
// コーパスが持つ質問(言い回し候補)を実際に投げ、そのQAの意図と引用が返るかを確かめる。
// 手書きの eval.test.ts が「ユーザーらしい揺れた質問」を担当するのに対し、こちらは
// 全レッスン・全QAの網羅的な回帰網。次の2段階で厳しさを変える:
// - 意図: 質問文自身がそのQAの意図を強く示すときだけ一致を要求する
// - 引用: その言い回しが1つのQAだけに登録されていて、質問文の意図がそのQAと近いとき要求する
//   (「例文を教えて」のように複数のQAに共有された言い回しは、どれが答えて正解なので緩める)

import { describe, expect, it } from 'vitest'
import { allLessons } from '../../content/grammar'
import { buildSectionQa } from './corpus'
import { INTENT_AFFINITY } from './intents'
import { classifyIntent, createSectionChat, normalizeQuestion } from './matcher'
import type { ChatReply, QaIntent } from './types'

function replyText(reply: ChatReply): string {
  if (reply.kind === 'fallback') return reply.message
  return [
    reply.lead,
    ...reply.quotes.flatMap((quote) => [quote.label, quote.en ?? '', quote.ja ?? '', quote.note ?? '', quote.text ?? '']),
  ].join('\n')
}

function snippetsOf(entry: ReturnType<typeof buildSectionQa>[number]): string[] {
  const lines = entry.answer.quotes
    .flatMap((quote) => [quote.en ?? '', quote.ja ?? '', quote.text ?? ''])
    .flatMap((text) => text.split('\n'))
    .map((line) => line.trim())
    .filter((line) => line.length >= 6)
  return [...new Set(lines)].sort((a, b) => b.length - a.length).slice(0, 3)
}

function closeIntent(a: QaIntent | undefined, b: QaIntent): boolean {
  if (!a) return true
  return a === b || (INTENT_AFFINITY[a]?.includes(b) ?? false) || (INTENT_AFFINITY[b]?.includes(a) ?? false)
}

describe('全レッスンのQA自己整合', () => {
  it(
    '各QAの代表的な質問に、その意図と引用で答える',
    () => {
      let passed = 0
      let total = 0
      const failures: string[] = []
      const byCategory = new Map<string, number>()
      for (const lesson of allLessons) {
        const entries = buildSectionQa(lesson)
        if (entries.length === 0) continue
        const questionCount = new Map<string, number>()
        for (const entry of entries) {
          for (const question of entry.questions) {
            const key = normalizeQuestion(question)
            questionCount.set(key, (questionCount.get(key) ?? 0) + 1)
          }
        }
        const chat = createSectionChat(lesson, () => 0)
        for (const entry of entries) {
          if (entry.intent === 'greeting' || entry.intent === 'capability') continue
          if (entry.answer.quotes.length === 0 || entry.questions.length === 0) continue
          // 最も具体的な言い回し(長いもの)を1つ代表にする
          const question = entry.questions.reduce((longest, candidate) =>
            candidate.length > longest.length ? candidate : longest,
          )
          const snippets = snippetsOf(entry)
          const signaled = classifyIntent(question)?.intent
          const unique = (questionCount.get(normalizeQuestion(question)) ?? 0) === 1
          const strictQuote = unique && closeIntent(signaled, entry.intent)
          total += 1
          chat.reset()
          const reply = chat.reply(question)
          const okIntent = signaled !== entry.intent || (reply.kind === 'answer' && reply.intent === entry.intent)
          const okQuote = !strictQuote || (reply.kind === 'answer' && snippets.some((snippet) => replyText(reply).includes(snippet)))
          if (okIntent && okQuote) {
            passed += 1
            continue
          }
          const kind = entry.id.includes(':diff:')
            ? 'diff-side'
            : entry.id.includes(':termpair:')
              ? 'termpair'
              : entry.id.includes(':table:')
                ? 'table'
                : entry.id.includes(':illustration:')
                  ? 'illustration'
                  : entry.id.split(':')[1] ?? entry.id
          const key = `${kind}/${okIntent ? 'quote' : 'intent'}`
          byCategory.set(key, (byCategory.get(key) ?? 0) + 1)
          if (failures.length < 80) {
            const actual = reply.kind === 'answer' ? `${reply.intent}/${replyText(reply).replace(/\n/g, ' ').slice(0, 70)}` : 'fallback'
            failures.push(`${lesson.id} ${entry.id} [${entry.intent}] Q="${question}" -> ${actual}`)
          }
        }
      }
      const accuracy = passed / total
      console.log(`BULK ${passed}/${total} = ${(accuracy * 100).toFixed(1)}%`)
      console.log(
        `BULK_CATEGORIES: ${[...byCategory.entries()]
          .sort((a, b) => b[1] - a[1])
          .map(([key, count]) => `${key}=${count}`)
          .join(' ')}`,
      )
      if (failures.length > 0) console.log(`BULK_FAILURES:\n${failures.join('\n')}`)
      expect(accuracy).toBeGreaterThanOrEqual(0.9)
    },
    240_000,
  )
})
