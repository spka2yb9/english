import { allLessons, findLesson } from '../grammar/index.ts'
import { buildThreeMinuteSection } from './build.ts'
import type { ThreeMinuteSection } from './types'

export type { ThreeMinuteLine, ThreeMinuteMood, ThreeMinutePart, ThreeMinuteSection, ThreeMinuteSpeaker } from './types'
export { buildThreeMinuteSection }

/** 一覧の件数表示に使う。会話スクリプトは開いたときに組み立てる。 */
export const threeMinuteLessonCount = allLessons.length

export function getThreeMinuteSection(lessonId: string): ThreeMinuteSection | undefined {
  const lesson = findLesson(lessonId)
  return lesson ? buildThreeMinuteSection(lesson) : undefined
}
