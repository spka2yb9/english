import { describe, expect, it } from 'vitest'
import { allLessons } from '../grammar/index.ts'
import { buildMistake, buildThreeMinuteSection } from './build.ts'

describe('3分間English の会話スクリプト', () => {
  it('英文法の全116セクションを、先生と生徒の会話に変換する', () => {
    expect(allLessons).toHaveLength(116)

    for (const lesson of allLessons) {
      const section = buildThreeMinuteSection(lesson)

      expect(section.lessonId).toBe(lesson.id)
      expect(section.parts.length).toBeGreaterThan(10)
      expect(section.parts.some((part) => part.kind === 'line' && part.line.speaker === 'ingbird')).toBe(true)
      expect(section.parts.some((part) => part.kind === 'line' && part.line.speaker === 'hiyoko')).toBe(true)
      expect(section.parts.some((part) => part.kind === 'animation')).toBe(true)
      expect(section.parts.every((part) => part.kind !== 'line' || part.line.text.trim() !== '')).toBe(true)
    }
  })

  it('図表・例文・まとめを落とさず、最後に4択のクイズを4問だけ置く', () => {
    for (const lesson of allLessons) {
      const section = buildThreeMinuteSection(lesson)
      const visualCount = lesson.blocks.filter((block) => block.type !== 'explanation').length
      const renderedVisualCount = section.parts.filter((part) => part.kind === 'block').length

      expect(renderedVisualCount).toBe(visualCount)
      expect(section.quiz).toHaveLength(4)
      expect(section.quiz.every((question) => question.choices.length === 4)).toBe(true)
      for (const point of lesson.summary) {
        expect(
          section.parts.some((part) => part.kind === 'line' && part.line.text.includes(point)),
        ).toBe(true)
      }
      // 解説の書き出しも、会話の中に必ず残す(説明の抜け落ちを防ぐ)。
      for (const block of lesson.blocks) {
        if (block.type !== 'explanation') continue
        const firstSentence = block.body.split(/\n\n+/)[0]?.split(/(?<=[。！？])/)[0]?.trim()
        if (!firstSentence) continue
        expect(
          section.parts.some((part) => part.kind === 'line' && part.line.text.includes(firstSentence)),
        ).toBe(true)
      }
    }
  })

  it('1話の読了目安は3〜5分に収まる', () => {
    for (const lesson of allLessons) {
      const section = buildThreeMinuteSection(lesson)
      expect(section.minutes).toBeGreaterThanOrEqual(3)
      expect(section.minutes).toBeLessThanOrEqual(5)
    }
  })

  it('つまずき例は、誤答・正解・理由がそろい、全話に1つある', () => {
    let count = 0
    for (const lesson of allLessons) {
      const mistake = buildMistake(lesson)
      if (!mistake) continue
      count += 1
      expect(mistake.wrong.trim()).not.toBe('')
      expect(mistake.right.trim()).not.toBe('')
      expect(mistake.wrong.trim()).not.toBe(mistake.right.trim())
      expect(mistake.note.trim()).not.toBe('')
      expect(mistake.prompt.trim()).not.toBe('')
    }
    expect(count).toBe(116)
  })
})
