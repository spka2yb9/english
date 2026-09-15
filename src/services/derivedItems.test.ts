import { describe, expect, it } from 'vitest'
import { allLessons, findLesson } from '../content/grammar'
import { LESSON_WORD_ORDER_SIZE, buildWordOrderItem, lessonWordOrderSentences } from './derivedItems'

const sentence = { en: 'She is tired today.', ja: '彼女は今日疲れています。' }

describe('並べ替え問題', () => {
  it('同じ語を過不足なく含み、元の並びとは異なる', () => {
    const item = buildWordOrderItem(sentence, () => 0)
    expect([...item.tokens].sort()).toEqual(['She', 'is', 'tired', 'today.'].sort())
    expect(item.tokens.join(' ')).not.toBe(sentence.en)
    expect(item.answer).toBe(sentence.en)
  })
})

describe('セクションごとの並べ替え出題', () => {
  it('全セクションが10問ぶんの例文を出せる', () => {
    for (const lesson of allLessons) {
      expect(lessonWordOrderSentences(lesson), lesson.id).toHaveLength(LESSON_WORD_ORDER_SIZE)
    }
  })

  it('そのセクション自身の例文だけを、掲載順のまま使う', () => {
    const lesson = findLesson('u01-l1')!
    const picked = lessonWordOrderSentences(lesson)
    const own = new Set(
      lesson.blocks.flatMap((block) => (block.type === 'examples' ? block.items.map((i) => i.en) : [])),
    )
    for (const s of picked) expect(own.has(s.en), s.en).toBe(true)
    expect(picked[0].en).toBe('I am a nurse.')
  })

  it('3語以下の文は並べ替えにならないので除く', () => {
    const lesson = findLesson('u01-l1')!
    // u01-l1 の Are you hungry? は3語
    expect(lessonWordOrderSentences(lesson).map((s) => s.en)).not.toContain('Are you hungry?')
  })

  it('重複した英文は一度しか出さない', () => {
    for (const lesson of allLessons) {
      const picked = lessonWordOrderSentences(lesson).map((s) => s.en.toLowerCase())
      expect(new Set(picked).size, lesson.id).toBe(picked.length)
    }
  })
})
