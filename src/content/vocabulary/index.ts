// 語彙データセットの集約。バッチファイル(約130語/ファイル)を結合する。
// NOTE: コンテンツ生成が完了したバッチから順に import を追加する(TASKS.md 参照)。

import type { VocabularyEntry } from '../types'
import { batch00 } from './batch00.ts'
import { batch01 } from './batch01.ts'
import { batch02 } from './batch02.ts'
import { batch03 } from './batch03.ts'
import { batch04 } from './batch04.ts'
import { batch06 } from './batch06.ts'
import { batch07 } from './batch07.ts'
import { batch08 } from './batch08.ts'
import { plus01 } from './plus01.ts'
import { plus02 } from './plus02.ts'
import { plus03 } from './plus03.ts'
import { plus04 } from './plus04.ts'
import { plus05 } from './plus05.ts'
import { plus06 } from './plus06.ts'
import { plus07 } from './plus07.ts'
import { plus08 } from './plus08.ts'
import { plus09 } from './plus09.ts'
import { plus10 } from './plus10.ts'
import { plus11 } from './plus11.ts'
import { plus12 } from './plus12.ts'
import { plus13 } from './plus13.ts'
import { plus14 } from './plus14.ts'
import { plus15 } from './plus15.ts'
import { plus16 } from './plus16.ts'
import { plus17 } from './plus17.ts'
import { plus18 } from './plus18.ts'
import { plus19 } from './plus19.ts'
import { plus20 } from './plus20.ts'
import { plus21 } from './plus21.ts'
import { plus22 } from './plus22.ts'
import { plus23 } from './plus23.ts'
import { plus24 } from './plus24.ts'
import { plus25 } from './plus25.ts'
import { plus26 } from './plus26.ts'
import { plus27 } from './plus27.ts'
import { plus28 } from './plus28.ts'
import { plus29 } from './plus29.ts'
import { plus30 } from './plus30.ts'
import { plus31 } from './plus31.ts'
import { plus32 } from './plus32.ts'
import { plus33 } from './plus33.ts'
import { plus34 } from './plus34.ts'
import { plus35 } from './plus35.ts'
import { plus36 } from './plus36.ts'
import { plus37 } from './plus37.ts'
import { plus38 } from './plus38.ts'
import { plus39 } from './plus39.ts'
import { plus40 } from './plus40.ts'
import { plus41 } from './plus41.ts'
import { plus42 } from './plus42.ts'
import { plus43 } from './plus43.ts'
import { plus44 } from './plus44.ts'
import { plus45 } from './plus45.ts'
import { plus46 } from './plus46.ts'
import { plus47 } from './plus47.ts'
import { expandedVocabulary } from './expanded.ts'
import { extendedVocabulary } from './extended.ts'
import { supplementalVocabulary } from './supplemental.ts'
import { vocabularyNotes } from './notes.ts'
import { vocabularyCollocations } from './collocations.ts'

export const allVocabulary: VocabularyEntry[] = [
  ...batch00,
  ...batch01,
  ...batch02,
  ...batch03,
  ...batch04,
  ...batch06,
  ...batch07,
  ...batch08,
  ...expandedVocabulary,
  ...supplementalVocabulary,
  ...extendedVocabulary,
  ...plus01,
  ...plus02,
  ...plus03,
  ...plus04,
  ...plus05,
  ...plus06,
  ...plus07,
  ...plus08,
  ...plus09,
  ...plus10,
  ...plus11,
  ...plus12,
  ...plus13,
  ...plus14,
  ...plus15,
  ...plus16,
  ...plus17,
  ...plus18,
  ...plus19,
  ...plus20,
  ...plus21,
  ...plus22,
  ...plus23,
  ...plus24,
  ...plus25,
  ...plus26,
  ...plus27,
  ...plus28,
  ...plus29,
  ...plus30,
  ...plus31,
  ...plus32,
  ...plus33,
  ...plus34,
  ...plus35,
  ...plus36,
  ...plus37,
  ...plus38,
  ...plus39,
  ...plus40,
  ...plus41,
  ...plus42,
  ...plus43,
  ...plus44,
  ...plus45,
  ...plus46,
  ...plus47,
].map((entry) => ({
  ...entry,
  ...(vocabularyNotes[entry.id] ? { mnemonic: vocabularyNotes[entry.id] } : {}),
  // 自前の collocations を持つエントリ(batch*.ts / extended.ts)が優先。後付け分は不足を埋めるだけ。
  ...(entry.collocations?.length ? {} : vocabularyCollocations[entry.id] ? { collocations: vocabularyCollocations[entry.id] } : {}),
}))

const vocabMap = new Map(allVocabulary.map((e) => [e.id, e]))

export function findWord(id: string): VocabularyEntry | undefined {
  return vocabMap.get(id)
}
