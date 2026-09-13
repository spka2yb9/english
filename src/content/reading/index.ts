import type { ReadingPassage } from '../types.ts'
import { passages } from './passages.ts'
import { a2Passages } from './passages-a2.ts'
import { b1Passages } from './passages-b1.ts'
import { b2Passages } from './passages-b2.ts'
import { b2PassagesB } from './passages-b2b.ts'
import { b2PassagesC } from './passages-b2c.ts'
import { a2PassagesB } from './passages-a2b.ts'
import { a2PassagesC } from './passages-a2c.ts'
import { b1PassagesB } from './passages-b1b.ts'
import { b1PassagesC } from './passages-b1c.ts'

export const readingPassages: ReadingPassage[] = [
  ...passages,
  ...a2Passages,
  ...b1Passages,
  ...b2Passages,
  ...a2PassagesB,
  ...b1PassagesB,
  ...b2PassagesB,
  ...a2PassagesC,
  ...b1PassagesC,
  ...b2PassagesC,
].sort((a, b) =>
  a.id.localeCompare(b.id),
)

const passageMap = new Map(readingPassages.map((p) => [p.id, p]))

export function findPassage(id: string): ReadingPassage | undefined {
  return passageMap.get(id)
}

export function passagesByLevel(level: ReadingPassage['level']): ReadingPassage[] {
  return readingPassages.filter((p) => p.level === level)
}
