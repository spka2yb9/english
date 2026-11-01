import { allLessons, findLesson, nextLesson } from '../grammar/index.ts'
import { buildThreeMinuteSection } from './build.ts'
import { THREE_MINUTE_PATTERN_INTRO_ID, THREE_MINUTE_PATTERN_INTRO_TITLE } from './ids.ts'
import { patternIntroSection } from './patternIntro.ts'
import type { ThreeMinuteSection } from './types'

export type { ThreeMinuteLine, ThreeMinuteMood, ThreeMinutePart, ThreeMinuteSection, ThreeMinuteSpeaker } from './types'
export { buildThreeMinuteSection, patternIntroSection }
export { THREE_MINUTE_PATTERN_INTRO_ID, THREE_MINUTE_PATTERN_INTRO_TITLE }

/** 一覧の件数表示に使う。会話スクリプトは開いたときに組み立てる。 */
export const threeMinuteLessonCount = allLessons.length + 1

export function getThreeMinuteSection(lessonId: string): ThreeMinuteSection | undefined {
  if (lessonId === THREE_MINUTE_PATTERN_INTRO_ID) return patternIntroSection
  const lesson = findLesson(lessonId)
  return lesson ? buildThreeMinuteSection(lesson) : undefined
}

/** 一覧の並び順(5文型の導入 → 英文法の116話)で、次のお話を返す。 */
export function nextThreeMinuteSection(lessonId: string): { id: string; title: string } | undefined {
  if (lessonId === THREE_MINUTE_PATTERN_INTRO_ID) {
    const first = allLessons[0]
    return first ? { id: first.id, title: first.title } : undefined
  }
  const next = nextLesson(lessonId)
  return next ? { id: next.id, title: next.title } : undefined
}
