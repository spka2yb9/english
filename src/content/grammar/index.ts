// 文法カリキュラムの集約。ユニットファイルは各レベルのディレクトリに配置する。
// NOTE: コンテンツ生成が完了したユニットから順に import を追加する(TASKS.md 参照)。

import type { CefrLevel, GrammarLesson, GrammarUnit } from '../types'
import { u01 } from './a2/u01.ts'
import { u02 } from './a2/u02.ts'
import { u03 } from './a2/u03.ts'
import { u04 } from './a2/u04.ts'
import { u05 } from './a2/u05.ts'
import { u06 } from './a2/u06.ts'
import { u07 } from './a2plus/u07.ts'
import { u08 } from './a2plus/u08.ts'
import { u09 } from './a2plus/u09.ts'
import { u10 } from './a2plus/u10.ts'
import { u11 } from './b1/u11.ts'
import { u12 } from './b1/u12.ts'
import { u13 } from './b1/u13.ts'
import { u14 } from './b1/u14.ts'
import { u15 } from './b1/u15.ts'
import { u16 } from './b1/u16.ts'
import { u17 } from './b1plus/u17.ts'
import { u18 } from './b1plus/u18.ts'
import { u19 } from './b1plus/u19.ts'
import { u20 } from './b1plus/u20.ts'
import { u21 } from './b1plus/u21.ts'
import { u22 } from './b1plus/u22.ts'
import { u23 } from './b2/u23.ts'
import { u24 } from './b2/u24.ts'
import { u25 } from './b2/u25.ts'
import { u26 } from './b2/u26.ts'
import { u27 } from './b2/u27.ts'
import { u28 } from './b2/u28.ts'
import { u29 } from './b2/u29.ts'
import { u30 } from './b2/u30.ts'
import { u31 } from './b2/u31.ts'
import { u32 } from './b2/u32.ts'
import { u33 } from './b2/u33.ts'
import { applyLessonExpansions } from './expansions/index.ts'
import { applyLessonIllustrations } from './illustrations.ts'
import { applyLessonPatterns } from './patterns/index.ts'

const baseGrammarUnits: GrammarUnit[] = [
  u01, u02, u03, u04, u05, u06,
  u07, u08, u09, u10,
  u11, u12, u13, u14, u15, u16,
  u17, u18, u19, u20, u21, u22,
  u23, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33,
]

export const grammarUnits: GrammarUnit[] = applyLessonIllustrations(
  applyLessonPatterns(applyLessonExpansions(baseGrammarUnits)),
)

export const LEVEL_ORDER: CefrLevel[] = ['A2', 'A2+', 'B1', 'B1+', 'B2']

export const allLessons: GrammarLesson[] = grammarUnits.flatMap((u) => u.lessons)

const lessonMap = new Map(allLessons.map((l) => [l.id, l]))

export function findLesson(id: string): GrammarLesson | undefined {
  return lessonMap.get(id)
}

export function findUnit(id: string): GrammarUnit | undefined {
  return grammarUnits.find((u) => u.id === id)
}

/** レッスンの次のレッスン(カリキュラム順) */
export function nextLesson(id: string): GrammarLesson | undefined {
  const idx = allLessons.findIndex((l) => l.id === id)
  return idx >= 0 ? allLessons[idx + 1] : undefined
}

export function unitsByLevel(level: CefrLevel): GrammarUnit[] {
  return grammarUnits.filter((u) => u.level === level)
}
