import { describe, expect, it } from 'vitest'
import { findLesson, grammarUnits } from '../../content/grammar'
import { buildSectionQa, intentsOf } from './corpus'
import { createSectionChat } from './matcher'

const lessons = grammarUnits.flatMap((unit) => unit.lessons)

describe('セクションQAコーパス', () => {
  it(
    '全セクションで、空でないQAが十分な数でき、IDが一意になる',
    () => {
    for (const lesson of lessons) {
      const entries = buildSectionQa(lesson)
      expect(entries.length, lesson.id).toBeGreaterThanOrEqual(15)
      expect(new Set(entries.map((entry) => entry.id)).size, lesson.id).toBe(entries.length)
      for (const entry of entries) {
        expect(entry.questions.length, `${lesson.id}/${entry.id}`).toBeGreaterThan(0)
        expect(entry.answer.lead.length, `${lesson.id}/${entry.id}`).toBeGreaterThan(0)
        for (const question of entry.questions) {
          expect(question, `${lesson.id}/${entry.id}`).not.toContain('{')
          expect(question.trim().length, `${lesson.id}/${entry.id}`).toBeGreaterThan(1)
        }
        // あいさつ・機能説明は引用を持たない(セクションの内容を答えないため)
        if (entry.intent === 'greeting' || entry.intent === 'capability') continue
        expect(entry.answer.quotes.length, `${lesson.id}/${entry.id}`).toBeGreaterThan(0)
        for (const quote of entry.answer.quotes) {
          expect(Boolean(quote.en || quote.ja || quote.note || quote.text), `${lesson.id}/${entry.id}`).toBe(true)
        }
      }
    }
  },
    30_000,
  )

  it('どのセクションにも目標・まとめ・クイズ・文型・あいさつの入口がある', () => {
    for (const lesson of lessons) {
      const intents = intentsOf(buildSectionQa(lesson))
      for (const intent of ['overview', 'summary', 'quiz', 'pattern', 'capability'] as const) {
        expect(intents.get(intent) ?? 0, `${lesson.id}:${intent}`).toBeGreaterThan(0)
      }
    }
  })

  it('カリキュラム用語のQAが、本文に現れる用語から生成される', () => {
    for (const [id, term] of [
      ['u01-l1', 'be動詞'],
      ['u01-l2', '三単現'],
      ['u11-l1', '現在完了'],
      ['u13-l1', '受動態'],
    ] as const) {
      const lesson = findLesson(id)
      expect(lesson, id).toBeDefined()
      if (!lesson) continue
      const termQa = buildSectionQa(lesson).find((entry) => entry.id.endsWith(`:termqa:${term}`))
      expect(termQa, `${id}:${term}`).toBeDefined()
      expect(termQa?.questions, `${id}:${term}`).toContain(term)
    }
  })

  it('全セクションでエンジンを作れ、質問候補が3つ以上返る', () => {
    // 116セクション全部で索引を作るとテストが重いので、レベルごとに代表を選ぶ
    const sample = ['u01-l1', 'u01-l2', 'u02-l1', 'u11-l1', 'u13-l1', 'u23-l1', 'u30-l1', 'u33-l1']
      .map((id) => findLesson(id))
      .filter((lesson) => lesson !== undefined)
    expect(sample.length).toBeGreaterThanOrEqual(6)
    for (const lesson of sample) {
      const chat = createSectionChat(lesson)
      expect(chat.size, lesson.id).toBeGreaterThanOrEqual(15)
      expect(chat.suggestions().length, lesson.id).toBeGreaterThanOrEqual(3)
    }
  })
})
