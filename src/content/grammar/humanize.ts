import type { GrammarUnit } from '../types'

// 教材本文には「U01で学んだ」「現在進行形(U02)」のような内部ユニット番号が残っている。
// 学習者にとっては意味不明なので、表示・書き出しの直前にユニット名・レッスン名へ置き換える。

function mapStrings<T>(value: T, replace: (text: string) => string): T {
  if (typeof value === 'string') return replace(value) as T
  if (Array.isArray(value)) return value.map((item) => mapStrings(item, replace)) as T
  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value).map(([key, item]) => [key, mapStrings(item, replace)]),
    ) as T
  }
  return value
}

export function humanizeCurriculumRefs(units: GrammarUnit[]): GrammarUnit[] {
  const unitTitles = new Map(units.map((unit) => [unit.id, unit.title]))
  const lessonTitles = new Map(units.flatMap((unit) => unit.lessons.map((lesson) => [lesson.id, lesson.title])))

  const replace = (text: string) =>
    text
      // 先にレッスン単位の参照(U01-l2)を置き換える。
      .replace(/U(\d{2})-l(\d+)/g, (_, unitNumber: string, lessonNumber: string) => {
        const id = `u${unitNumber}-l${lessonNumber}`
        return `「${lessonTitles.get(id) ?? `ユニット${Number(unitNumber)}のレッスン${Number(lessonNumber)}`}」`
      })
      // 残ったユニット参照(U01)をユニット名にする。
      .replace(/U(\d{2})/g, (_, unitNumber: string) => {
        const id = `u${unitNumber}`
        return `「${unitTitles.get(id) ?? `ユニット${Number(unitNumber)}`}」`
      })
      // 「「文の基本」 で学んだ」のように、置換後の引用符と助詞の間に残る空白を詰める。
      .replace(/」\s+(?=[でをにのはがも、。])/g, '」')

  return mapStrings(units, replace)
}
