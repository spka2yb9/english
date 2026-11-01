import { describe, expect, it } from 'vitest'
import { patternAnimations, patternQuiz, wordOrderAnimation, wordOrderQuiz } from '../grammar/structures/index.ts'
import { allLessons } from '../grammar/index.ts'
import { buildMistake, buildThreeMinuteSection } from './build.ts'
import { THREE_MINUTE_PATTERN_INTRO_ID } from './ids.ts'
import { getThreeMinuteSection, nextThreeMinuteSection, patternIntroSection, threeMinuteLessonCount } from './index.ts'

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

describe('3分間English の5文型の導入', () => {
  it('116話の前に、S / V / O / C / M と5文型を学ぶ1話を置く', () => {
    expect(threeMinuteLessonCount).toBe(117)
    expect(getThreeMinuteSection(THREE_MINUTE_PATTERN_INTRO_ID)).toBe(patternIntroSection)
    expect(patternIntroSection.title).toBe('5文型の地図')
    expect(patternIntroSection.unitTitle).toBe('はじめに')
    expect(patternIntroSection.parts.length).toBeGreaterThan(60)
    // 導入の次は、英文法の最初のセクションへ進む。
    expect(nextThreeMinuteSection(THREE_MINUTE_PATTERN_INTRO_ID)).toEqual({
      id: 'u01-l1',
      title: 'be動詞の現在形',
    })
  })

  it('役割表と5文型の早見表で、S/V/O/C/M と5つすべてを説明する', () => {
    const tables = patternIntroSection.parts.flatMap((part) =>
      part.kind === 'block' && part.block.type === 'table' ? [part.block] : [],
    )
    const roleTable = tables.find((table) => table.title === 'S / V / O / C / M の役割')
    expect(roleTable?.rows.map((row) => row[0])).toEqual(['S', 'V', 'O', 'C', 'M'])

    const summary = tables.find((table) => table.title === '5文型 早見表')
    expect(summary?.rows.map((row) => row[0])).toEqual([
      '第1文型 SV',
      '第2文型 SVC',
      '第3文型 SVO',
      '第4文型 SVOO',
      '第5文型 SVOC',
    ])
  })

  it('5つの文型すべてにアニメーションと例文を付ける', () => {
    const animations = patternIntroSection.parts.flatMap((part) =>
      part.kind === 'animation' ? [part.animation] : [],
    )
    expect(animations.map((animation) => animation.title)).toEqual([
      wordOrderAnimation.title,
      patternAnimations.SV.title,
      patternAnimations.SVC.title,
      patternAnimations.SVO.title,
      patternAnimations.SVOO.title,
      patternAnimations.SVOC.title,
    ])

    for (const pattern of ['SV', 'SVC', 'SVO', 'SVOO', 'SVOC'] as const) {
      const examples = patternIntroSection.parts.flatMap((part) =>
        part.kind === 'block' && part.block.type === 'examples'
          ? part.block.items.filter((item) => item.pattern === pattern)
          : [],
      )
      expect(examples.length, pattern).toBeGreaterThanOrEqual(1)
    }
  })

  it('5文型を見分ける8問を持ち、IDは英文法のクイズと重ならない', () => {
    expect(patternIntroSection.quiz).toHaveLength(8)
    expect(patternIntroSection.quiz.every((question) => question.choices.length === 4)).toBe(true)
    expect(patternIntroSection.quiz.every((question) => question.choiceNotes?.length === 4)).toBe(true)

    const ids = patternIntroSection.quiz.map((question) => question.id)
    expect(new Set(ids).size).toBe(ids.length)
    const lessonQuizIds = new Set([
      ...allLessons.flatMap((lesson) => lesson.quiz.map((question) => question.id)),
      ...patternQuiz.map((question) => question.id),
      ...wordOrderQuiz.map((question) => question.id),
    ])
    for (const id of ids) expect(lessonQuizIds.has(id)).toBe(false)

    const correctChoices = patternIntroSection.quiz.map((question) => question.choices[question.correctIndex])
    for (const label of [
      'SV(第1文型)',
      'SVC(第2文型)',
      'SVO(第3文型)',
      'SVOO(第4文型)',
      'SVOC(第5文型)',
    ]) {
      expect(correctChoices, label).toContain(label)
    }
  })
})
