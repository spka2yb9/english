// ダウンロード用エントリポイント。個別レッスン / ユニット / 全カリキュラムに対応。

import type { GrammarLesson } from '../../content/types'
import { grammarUnits } from '../../content/grammar'
import { lessonToMarkdown, unitsToMarkdown } from './markdown'

function downloadBlob(content: string, filename: string) {
  const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  a.click()
  URL.revokeObjectURL(url)
}

export function downloadLessonMarkdown(lesson: GrammarLesson) {
  downloadBlob(lessonToMarkdown(lesson), `${lesson.id}-${lesson.title}.md`)
}

export function downloadAllMarkdown() {
  downloadBlob(unitsToMarkdown(grammarUnits, '英文法 Reach B2 全カリキュラム'), '英文法A2-B2全カリキュラム.md')
}

export async function downloadLessonPdf(lesson: GrammarLesson) {
  const { lessonToPdf } = await import('./pdf')
  const doc = await lessonToPdf(lesson)
  doc.save(`${lesson.id}-${lesson.title}.pdf`)
}

export async function downloadAllPdf() {
  const { unitsToPdf } = await import('./pdf')
  const doc = await unitsToPdf(grammarUnits, '英文法 Reach B2 全カリキュラム')
  doc.save('英文法A2-B2全カリキュラム.pdf')
}
