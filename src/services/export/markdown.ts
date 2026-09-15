// レッスンデータ → 人間可読な Markdown。UI と同一のコンテンツソースから生成する。

import { illustrationAlt } from '../../content/illustrations'
import { PATTERN_LABELS } from '../../content/grammar/patterns/types'
import type { GrammarExample, GrammarLesson, GrammarUnit, LessonBlock, QuizQuestion, TimelineSpec } from '../../content/types'

export function lessonToMarkdown(lesson: GrammarLesson): string {
  const parts: string[] = []
  parts.push(`# ${lesson.title}`)
  parts.push(`**レベル:** ${lesson.level} ・ **目安:** 約${lesson.minutes}分`)
  parts.push(`## このセクションの目標\n\n${lesson.objective}`)

  for (const block of lesson.blocks) {
    parts.push(blockToMarkdown(block))
  }

  if (lesson.structureQuiz && lesson.structureQuiz.length > 0) {
    parts.push(quizToMarkdown('構造チェック', lesson.structureQuiz))
  }
  parts.push(quizToMarkdown('理解度チェック', lesson.quiz))

  parts.push(`## まとめ\n\n${lesson.summary.map((s) => `- ${s}`).join('\n')}`)
  return parts.join('\n\n')
}

function quizToMarkdown(title: string, questions: QuizQuestion[]): string {
  const parts: string[] = [`## ${title}`]
  questions.forEach((q, i) => {
    const lines: string[] = [`### 問題${i + 1}`, q.prompt]
    if (q.sentence) lines.push(`> ${q.sentence}${q.sentenceJa ? `\n> ${q.sentenceJa}` : ''}`)
    lines.push(q.choices.map((c, j) => `${j + 1}. ${c}`).join('\n'))
    lines.push(`**正解:** ${q.correctIndex + 1}. ${q.choices[q.correctIndex]}`)
    lines.push(`**解説:** ${q.explanation}`)
    if (q.choiceNotes) {
      const notes = q.choiceNotes
        .map((note, j) => (note && j !== q.correctIndex ? `- ${q.choices[j]} — ${note}` : null))
        .filter(Boolean)
      if (notes.length > 0) lines.push(notes.join('\n'))
    }
    parts.push(lines.join('\n\n'))
  })
  return parts.join('\n\n')
}

function exampleToMarkdown(ex: GrammarExample): string {
  const label = ex.pattern ? `【${PATTERN_LABELS[ex.pattern]}】` : ''
  const lines = [`> ${label}**${ex.en}**`]
  if (ex.ja) lines.push(`> ${ex.ja}`)
  if (ex.patternNote) lines.push(`> ${ex.patternNote}`)
  if (ex.note) lines.push(`> ※ ${ex.note}`)
  return lines.join('\n')
}

function timelineToAscii(t: TimelineSpec): string {
  // 0〜130 を 40 文字の軸にマップする簡易表現
  const WIDTH = 40
  const cell = (v: number) => Math.max(0, Math.min(WIDTH - 1, Math.round((v / 130) * (WIDTH - 1))))
  const axis = Array(WIDTH).fill('─')
  const nowPos = cell(100)
  axis[nowPos] = '┃'
  if (t.range) {
    const from = cell(t.range[0])
    const to = cell(t.arrowToNow ? 100 : t.range[1])
    for (let i = from; i <= to; i++) axis[i] = '═'
    if (t.arrowToNow) axis[to] = '▶'
  }
  if (t.point !== undefined) axis[cell(t.point)] = '●'
  const labels: string[] = []
  if (t.pointLabel) labels.push(`● = ${t.pointLabel}`)
  if (t.rangeLabel) labels.push(`═ = ${t.rangeLabel}`)
  return [
    t.title ? `**${t.title}**` : null,
    '```',
    `過去 ${axis.join('')} 未来`,
    `${' '.repeat(5 + nowPos)}↑今`,
    '```',
    labels.join(' / ') || null,
    t.caption ?? null,
  ]
    .filter(Boolean)
    .join('\n')
}

function blockToMarkdown(block: LessonBlock): string {
  switch (block.type) {
    case 'explanation':
      return [block.title ? `## ${block.title}` : null, block.body].filter(Boolean).join('\n\n')
    case 'examples':
      return [block.title ? `## ${block.title}` : '## 例文', block.items.map(exampleToMarkdown).join('\n\n')].join('\n\n')
    case 'timeline':
      return [block.title ? `## ${block.title}` : null, block.timelines.map(timelineToAscii).join('\n\n')]
        .filter(Boolean)
        .join('\n\n')
    case 'table': {
      const header = `| ${block.headers.join(' | ')} |`
      const sep = `| ${block.headers.map(() => '---').join(' | ')} |`
      const rows = block.rows.map((r) => `| ${r.join(' | ')} |`).join('\n')
      return [block.title ? `## ${block.title}` : null, [header, sep, rows].join('\n')].filter(Boolean).join('\n\n')
    }
    case 'contrast': {
      const side = (label: string, items: GrammarExample[], point?: string) =>
        [`### ${label}`, items.map(exampleToMarkdown).join('\n\n'), point ? `→ ${point}` : null].filter(Boolean).join('\n\n')
      return [
        block.title ? `## ${block.title}` : '## 比較',
        side(block.left.label, block.left.items, block.left.pointJa),
        side(block.right.label, block.right.items, block.right.pointJa),
        block.note ? `※ ${block.note}` : null,
      ]
        .filter(Boolean)
        .join('\n\n')
    }
    case 'structure': {
      const row = block.parts.map((p) => `[${p.label}] ${p.text}`).join(' → ')
      return [block.title ? `## ${block.title}` : null, '```', row, '```', block.caption ?? null].filter(Boolean).join('\n\n')
    }
    case 'breakdown': {
      const lines: string[] = [
        `> ${block.pattern ? `【${PATTERN_LABELS[block.pattern]}】` : ''}**${block.sentence}**`,
      ]
      if (block.ja) lines.push(`> ${block.ja}`)
      lines.push('', block.parts.map((p) => `[${p.role}] ${p.text}`).join(' / '))
      if (block.relation) lines.push(`意味の関係: ${block.relation}`)
      if (block.skeleton) {
        const pattern = block.skeletonPattern ? `(${PATTERN_LABELS[block.skeletonPattern]})` : ''
        lines.push(`骨格: ${block.skeleton}${pattern}`)
      }
      if (block.caption) lines.push(`※ ${block.caption}`)
      return [block.title ? `## ${block.title}` : null, lines.join('\n')].filter(Boolean).join('\n\n')
    }
    case 'expansion': {
      const steps = block.steps.map((step, i) =>
        [
          `${i + 1}. **${step.en}**${step.focus ? `(注目: ${step.focus})` : ''}`,
          step.ja ? `   ${step.ja}` : null,
          step.note ? `   ${step.note}` : null,
        ]
          .filter(Boolean)
          .join('\n'),
      )
      return [block.title ? `## ${block.title}` : null, steps.join('\n'), block.caption ? `※ ${block.caption}` : null]
        .filter(Boolean)
        .join('\n\n')
    }
    case 'illustration':
      return [
        `**図:** ${block.alt || illustrationAlt(block.kind, block.labels)}`,
        block.caption ?? null,
      ]
        .filter(Boolean)
        .join('\n\n')
  }
}

export function unitToMarkdown(unit: GrammarUnit): string {
  return [`# ${unit.title}(${unit.level})`, ...unit.lessons.map(lessonToMarkdown)].join('\n\n---\n\n')
}

export function unitsToMarkdown(units: GrammarUnit[], title: string): string {
  return [`# ${title}`, ...units.map(unitToMarkdown)].join('\n\n---\n\n')
}
