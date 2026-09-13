import { describe, expect, it } from 'vitest'
import { grammarUnits } from '../../content/grammar'
import { lessonToMarkdown, unitToMarkdown, unitsToMarkdown } from './markdown'

describe('grammar Markdown export', () => {
  const unit = grammarUnits[0]
  const lesson = unit.lessons[0]

  it('同じレッスンデータから目標・例文・クイズ・まとめを生成する', () => {
    const markdown = lessonToMarkdown(lesson)
    expect(markdown).toContain(`# ${lesson.title}`)
    expect(markdown).toContain('## このセクションの目標')
    expect(markdown).toContain(lesson.objective)
    expect(markdown).toContain('## 理解度チェック')
    expect(markdown).toContain('**正解:**')
    expect(markdown).toContain('## まとめ')
  })

  it('挿絵ブロックを図の説明テキストとして出力する', () => {
    const markdown = lessonToMarkdown(lesson)
    expect(markdown).toContain('**図:** be動詞で主語と説明をつなぐの2Dアニメーション。')
    expect(markdown).toContain('1. She is a nurse.')
    expect(markdown).toContain('2. She is not a nurse.')
    expect(markdown).toContain('3. Is she a nurse?')
    expect(markdown).toContain('be動詞は左右をイコールでつなぐ働きです。')
  })

  it('ユニット・全体の教材をまとめて生成する', () => {
    expect(unitToMarkdown(unit)).toContain(unit.title)
    const full = unitsToMarkdown(grammarUnits, '英文法 Reach B2')
    expect(full).toContain('# 英文法 Reach B2')
    expect(full).toContain(grammarUnits.at(-1)!.title)
  })
})
