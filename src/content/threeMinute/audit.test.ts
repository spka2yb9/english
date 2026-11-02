import { describe, expect, it } from 'vitest'
import { allLessons, findLesson, grammarUnits } from '../grammar/index.ts'
import { LESSON_ANIMATIONS } from '../grammar/animations.ts'
import { lessonIllustrations } from '../grammar/illustrations.ts'

function textValues(value: unknown): string[] {
  if (typeof value === 'string') return [value]
  if (Array.isArray(value)) return value.flatMap(textValues)
  if (value && typeof value === 'object') return Object.values(value).flatMap(textValues)
  return []
}

function explanation(lessonId: string, title: string) {
  const lesson = findLesson(lessonId)
  const block = lesson?.blocks.find((item) => item.type === 'explanation' && item.title === title)
  if (!block || block.type !== 'explanation') throw new Error(`${lessonId}: ${title} がありません`)
  return block
}

describe('3分間English の解説・図の監査で見つかった不正確さ', () => {
  it('内部ユニット番号(U01 など)が教材本文に残っていない', () => {
    for (const text of textValues(grammarUnits)) {
      expect(text).not.toMatch(/U\d\d/)
    }
  })

  it('be動詞の図は、場所を補語(C)として扱わない', () => {
    const lesson = findLesson('u01-l1')
    const structure = lesson?.blocks.find((block) => block.type === 'structure')
    if (!structure || structure.type !== 'structure') throw new Error('u01-l1 の構造図がありません')
    expect(structure.caption).toContain('飾り(M)')
    expect(structure.caption).toContain('SVになります')
  })

  it('三単現は「三人称・単数・現在」の略だと本文で説明する', () => {
    expect(explanation('u01-l2', '三単現の -s').body).toContain('三人称・単数・現在')
    expect(explanation('u01-l2', '三単現の -s').body).toContain('1人称')
    expect(explanation('u01-l2', '三単現の -s').body).toContain('2人称')
  })

  it('アニメーションの見出しが、同じ話の解説見出しと重複しない', () => {
    const normalize = (text: string) => text.replace(/[はがでをに]/g, '')
    for (const lesson of allLessons) {
      const animation = LESSON_ANIMATIONS[lesson.id]
      if (!animation) continue
      for (const block of lesson.blocks) {
        if (block.type !== 'explanation' || !block.title) continue
        expect(normalize(block.title), lesson.id).not.toBe(normalize(animation.title))
      }
    }
  })

  it('現在進行形のアニメーションは、開始の瞬間を現在形として説明する', () => {
    expect(LESSON_ANIMATIONS['u02-l1'].steps[0].note).not.toBe('料理を始めました。')
    expect(LESSON_ANIMATIONS['u02-l1'].steps[0].note).toContain('開始の瞬間')
  })

  it('現在完了と過去形のアニメーションは、別場面であることを明示する', () => {
    expect(LESSON_ANIMATIONS['u11-l5'].steps[2].note).toContain('別の場面')
  })

  it('will と be going to の対比で「必ず will」と断定しない', () => {
    const lesson = findLesson('u12-l2')
    const block = lesson?.blocks.find((item) => item.type === 'contrast' && item.note?.includes('その場の決定'))
    if (!block || block.type !== 'contrast' || !block.note) throw new Error('u12-l2 の対比がありません')
    expect(block.note).not.toContain('必ず will')
    expect(block.note).toContain('自然です')
  })

  it('受動態の誤答解説は「城が何かを建てた」と誤読させない', () => {
    const lesson = findLesson('u13-l1')
    const question = lesson?.quiz.find((item) => item.id === 'u13-l1-q1')
    expect(question?.choiceNotes?.[0]).not.toContain('城が(何かを)建てた')
    expect(question?.choiceNotes?.[0]).toContain('受動の意味にならず')
  })

  it('have + 物 + 過去分詞の図は、過去完了を「自分で切った」と断定しない', () => {
    const lesson = findLesson('u24-l1')
    const structure = lesson?.blocks.find((block) => block.type === 'structure')
    if (!structure || structure.type !== 'structure') throw new Error('u24-l1 の構造図がありません')
    expect(structure.caption).not.toContain('過去完了(自分で切った)')
    expect(structure.caption).toContain('過去完了の文')
  })

  it('同格の that と関係代名詞の that の対比に、曖昧な例を置かない', () => {
    const lesson = findLesson('u29-l1')
    const contrast = lesson?.blocks.find((block) => block.type === 'contrast')
    if (!contrast || contrast.type !== 'contrast') throw new Error('u29-l1 の対比がありません')
    const examples = contrast.right.items.map((item) => item.en)
    expect(examples).not.toContain('the fact that he tried to hide')
    expect(examples).toContain('the evidence that she collected')
  })

  it('過去完了のタイムラインに、基準になる過去の点も描く', () => {
    const lesson = findLesson('u31-l1')
    const timeline = lesson?.blocks.find((block) => block.type === 'timeline')
    if (!timeline || timeline.type !== 'timeline') throw new Error('u31-l1 のタイムラインがありません')
    expect(timeline.timelines.length).toBeGreaterThanOrEqual(4)
    expect(timeline.timelines.some((item) => item.pointLabel?.includes('駅に到着'))).toBe(true)
  })

  it('形容詞と副詞を日本語訳の「〜な」「〜に」だけで判断させない', () => {
    const lesson = findLesson('u05-l2')
    const contrast = lesson?.blocks.find((block) => block.type === 'contrast')
    if (!contrast || contrast.type !== 'contrast' || !contrast.note) throw new Error('u05-l2 の対比がありません')
    expect(contrast.note).not.toContain('日本語訳が「〜な」なら')
    expect(contrast.note).toContain('訳だけで決めず')
  })

  it('比較級の挿絵ラベルは、キャプションの Ken is taller than Mia. と順番をそろえる', () => {
    expect(lessonIllustrations['u07-l1'].labels).toEqual(['Ken', 'taller than', 'Mia'])
  })

  it('句動詞の挿絵は、代名詞の位置を入れ替えて見せる', () => {
    expect(lessonIllustrations['u33-l3'].kind).toBe('swap-cards')
    expect(lessonIllustrations['u33-l3'].labels).toEqual(['turn it off', 'turn off it'])
  })
})
