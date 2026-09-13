// レッスンデータ → PDF(jsPDF + IPAexゴシック)。日本語対応のため public/fonts のフォントを遅延ロードする。

import { jsPDF } from 'jspdf'
import { illustrationAlt } from '../../content/illustrations'
import type { GrammarExample, GrammarLesson, GrammarUnit, LessonBlock } from '../../content/types'

const FONT_NAME = 'IPAexGothic'
const FONT_FILE = 'ipaexg.ttf'

let fontBase64: string | null = null

async function loadFontBase64(): Promise<string> {
  if (fontBase64) return fontBase64
  const res = await fetch(`${import.meta.env.BASE_URL}fonts/ipaexg.ttf`)
  if (!res.ok) throw new Error('フォントの読み込みに失敗しました')
  const buf = await res.arrayBuffer()
  const bytes = new Uint8Array(buf)
  let binary = ''
  const CHUNK = 0x8000
  for (let i = 0; i < bytes.length; i += CHUNK) {
    binary += String.fromCharCode(...bytes.subarray(i, i + CHUNK))
  }
  fontBase64 = btoa(binary)
  return fontBase64
}

const PAGE_W = 210
const PAGE_H = 297
const MARGIN = 18
const CONTENT_W = PAGE_W - MARGIN * 2

class PdfWriter {
  doc: jsPDF
  y = MARGIN

  constructor(doc: jsPDF) {
    this.doc = doc
  }

  private ensureSpace(height: number) {
    if (this.y + height > PAGE_H - MARGIN) {
      this.doc.addPage()
      this.y = MARGIN
    }
  }

  text(text: string, size: number, opts: { indent?: number; gapAfter?: number; color?: [number, number, number] } = {}) {
    const { indent = 0, gapAfter = 2, color = [30, 30, 30] } = opts
    this.doc.setFontSize(size)
    this.doc.setTextColor(...color)
    const lineHeight = size * 0.55
    const lines: string[] = this.doc.splitTextToSize(text, CONTENT_W - indent)
    for (const line of lines) {
      this.ensureSpace(lineHeight)
      this.doc.text(line, MARGIN + indent, this.y)
      this.y += lineHeight
    }
    this.y += gapAfter
  }

  heading(text: string, size: number) {
    this.gap(3)
    this.text(text, size, { gapAfter: 3, color: [20, 60, 120] })
  }

  gap(mm: number) {
    this.y += mm
  }

  rule() {
    this.ensureSpace(6)
    this.doc.setDrawColor(200)
    this.doc.line(MARGIN, this.y, PAGE_W - MARGIN, this.y)
    this.y += 5
  }
}

function writeExample(w: PdfWriter, ex: GrammarExample) {
  w.text(ex.en, 11, { indent: 4, gapAfter: 0.5 })
  if (ex.ja) w.text(ex.ja, 9.5, { indent: 4, gapAfter: 0.5, color: [90, 90, 90] })
  if (ex.note) w.text(`※ ${ex.note}`, 9, { indent: 4, gapAfter: 0.5, color: [120, 120, 120] })
  w.gap(2)
}

function writeBlock(w: PdfWriter, block: LessonBlock) {
  switch (block.type) {
    case 'explanation':
      if (block.title) w.heading(block.title, 13)
      // RichText の簡易変換: 強調記号を除去、箇条書きは・に
      for (const para of block.body.split(/\n\n+/)) {
        const clean = para.replace(/\*\*(.+?)\*\*/g, '$1')
        if (clean.split('\n').every((l) => l.trim().startsWith('- '))) {
          for (const line of clean.split('\n')) {
            w.text(`・${line.trim().slice(2)}`, 10.5, { indent: 2, gapAfter: 1 })
          }
          w.gap(1.5)
        } else {
          w.text(clean, 10.5, { gapAfter: 2.5 })
        }
      }
      break
    case 'examples':
      w.heading(block.title ?? '例文', 13)
      block.items.forEach((ex) => writeExample(w, ex))
      break
    case 'timeline':
      if (block.title) w.heading(block.title, 13)
      for (const t of block.timelines) {
        const parts: string[] = []
        if (t.title) parts.push(`【${t.title}】`)
        if (t.rangeLabel) parts.push(`継続: ${t.rangeLabel}${t.arrowToNow ? '(今まで続く)' : ''}`)
        if (t.pointLabel) parts.push(`時点: ${t.pointLabel}`)
        if (t.caption) parts.push(t.caption)
        w.text(parts.join(' '), 10, { indent: 2, gapAfter: 2, color: [80, 80, 80] })
      }
      break
    case 'table': {
      if (block.title) w.heading(block.title, 13)
      w.text(block.headers.join(' | '), 10, { indent: 2, gapAfter: 1, color: [20, 60, 120] })
      for (const row of block.rows) {
        w.text(row.join(' | '), 10, { indent: 2, gapAfter: 1 })
      }
      w.gap(2)
      break
    }
    case 'contrast':
      w.heading(block.title ?? '比較', 13)
      for (const side of [block.left, block.right]) {
        w.text(`◆ ${side.label}`, 11, { gapAfter: 1.5, color: [20, 60, 120] })
        side.items.forEach((ex) => writeExample(w, ex))
        if (side.pointJa) w.text(`→ ${side.pointJa}`, 9.5, { indent: 4, gapAfter: 2, color: [90, 90, 90] })
      }
      if (block.note) w.text(`※ ${block.note}`, 9.5, { gapAfter: 2, color: [120, 120, 120] })
      break
    case 'structure':
      if (block.title) w.heading(block.title, 13)
      w.text(block.parts.map((p) => `[${p.label}] ${p.text}`).join(' → '), 10.5, { indent: 2, gapAfter: 1.5 })
      if (block.caption) w.text(block.caption, 9.5, { indent: 2, gapAfter: 2, color: [90, 90, 90] })
      break
    case 'illustration':
      w.text(`図: ${block.alt || illustrationAlt(block.kind, block.labels)}`, 10, {
        indent: 2,
        gapAfter: 1.5,
        color: [80, 80, 80],
      })
      if (block.caption) w.text(block.caption, 9.5, { indent: 2, gapAfter: 2, color: [90, 90, 90] })
      break
  }
}

function writeLesson(w: PdfWriter, lesson: GrammarLesson) {
  w.heading(`${lesson.title}(${lesson.level}・約${lesson.minutes}分)`, 16)
  w.text(`目標: ${lesson.objective}`, 10.5, { gapAfter: 3 })

  lesson.blocks.forEach((b) => writeBlock(w, b))

  w.heading('理解度チェック', 13)
  lesson.quiz.forEach((q, i) => {
    w.text(`問題${i + 1}: ${q.prompt}`, 10.5, { gapAfter: 1 })
    if (q.sentence) w.text(q.sentence, 10.5, { indent: 4, gapAfter: 1 })
    if (q.sentenceJa) w.text(q.sentenceJa, 9.5, { indent: 4, gapAfter: 1, color: [90, 90, 90] })
    q.choices.forEach((c, j) => w.text(`${j + 1}. ${c}`, 10, { indent: 6, gapAfter: 0.5 }))
    w.text(`正解: ${q.correctIndex + 1}. ${q.choices[q.correctIndex]}`, 10, { indent: 4, gapAfter: 0.5, color: [20, 100, 60] })
    w.text(`解説: ${q.explanation}`, 9.5, { indent: 4, gapAfter: 2, color: [90, 90, 90] })
  })

  w.heading('まとめ', 13)
  lesson.summary.forEach((s) => w.text(`・${s}`, 10.5, { indent: 2, gapAfter: 1 }))
  w.gap(4)
}

async function createDoc(): Promise<{ doc: jsPDF; writer: PdfWriter }> {
  const doc = new jsPDF({ unit: 'mm', format: 'a4' })
  doc.addFileToVFS(FONT_FILE, await loadFontBase64())
  doc.addFont(FONT_FILE, FONT_NAME, 'normal')
  doc.setFont(FONT_NAME)
  return { doc, writer: new PdfWriter(doc) }
}

export async function lessonToPdf(lesson: GrammarLesson): Promise<jsPDF> {
  const { doc, writer } = await createDoc()
  writeLesson(writer, lesson)
  return doc
}

export async function unitsToPdf(units: GrammarUnit[], title: string): Promise<jsPDF> {
  const { doc, writer } = await createDoc()
  writer.heading(title, 20)
  writer.rule()
  units.forEach((unit) => {
    writer.heading(`${unit.title}(${unit.level})`, 17)
    unit.lessons.forEach((l) => {
      writer.rule()
      writeLesson(writer, l)
    })
  })
  return doc
}
