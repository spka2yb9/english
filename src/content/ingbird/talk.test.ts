// イングバードのつぶやきコーパスの自動検証。
// 学習者に見せる文なので、空欄・重複・読み上げられない文字を機械的に落とす。

import { describe, expect, it } from 'vitest'
import { PHRASE_SCENES } from './phrases'
import { TIPS } from './tips'
import {
  ENCOURAGE_BODIES,
  ENCOURAGE_CLOSINGS,
  ENCOURAGE_LINES,
  TIME_GREETINGS,
  type EncourageBranch,
} from './encouragement'
import { PHRASES, TALK_COUNTS, TIP_LINES } from './talk'
import { checkAudioText } from '../validation'

const BRANCHES: EncourageBranch[] = ['noDays', 'todayDone', 'todayNotYet', 'back', 'backDone']
const ALLOWED_SLOTS = new Set(['days', 'gap', 'next', 'remaining'])

describe('イングバードのつぶやきコーパス', () => {
  it('フレーズ・コツ・励ましに十分な量がある(膨大であること)', () => {
    expect(TALK_COUNTS.scenes, '場面数').toBeGreaterThanOrEqual(20)
    expect(TALK_COUNTS.phrases, 'フレーズ数').toBeGreaterThanOrEqual(300)
    expect(TALK_COUNTS.tips, 'コツの数').toBeGreaterThanOrEqual(120)
    expect(TALK_COUNTS.encourageLines, '単体の励まし').toBeGreaterThanOrEqual(80)
    expect(TALK_COUNTS.bodies, '組み立て用の本文').toBeGreaterThanOrEqual(100)
    expect(TALK_COUNTS.closings, '締めの一文').toBeGreaterThanOrEqual(24)
    expect(TALK_COUNTS.greetings, '時間帯のあいさつ').toBeGreaterThanOrEqual(20)
    // 組み合わせで作れる励ましの総数。1つの状況で数千通りになる。
    const combos = TALK_COUNTS.bodies * TALK_COUNTS.closings + TALK_COUNTS.encourageLines + TALK_COUNTS.greetings
    expect(combos, '励ましの組み合わせ').toBeGreaterThanOrEqual(3000)
  })

  it('どの場面にも一定数のフレーズがあり、場面名が重複しない', () => {
    const labels = PHRASE_SCENES.map((scene) => scene.label)
    expect(new Set(labels).size).toBe(labels.length)
    for (const scene of PHRASE_SCENES) {
      expect(scene.phrases.length, `${scene.label} の件数`).toBeGreaterThanOrEqual(12)
    }
  })

  it('フレーズは英文・和訳・使いどころがそろい、IDが一意で、読み上げられる', () => {
    const ids = new Set<string>()
    const english = new Set<string>()
    const japanese = new Set<string>()
    for (const phrase of PHRASES) {
      expect(ids.has(phrase.id), `${phrase.id} が重複`).toBe(false)
      ids.add(phrase.id)
      expect(phrase.en.trim().length, `${phrase.id} の英文`).toBeGreaterThan(2)
      expect(phrase.ja.trim().length, `${phrase.id} の和訳`).toBeGreaterThan(1)
      expect(phrase.note.trim().length, `${phrase.id} の使いどころ`).toBeGreaterThan(5)
      expect(english.has(phrase.en), `${phrase.en} が重複`).toBe(false)
      english.add(phrase.en)
      expect(japanese.has(phrase.ja), `${phrase.ja} が重複`).toBe(false)
      japanese.add(phrase.ja)
      // TTSに渡せない記号が無いこと(文末の句読点・禁止文字)
      expect(checkAudioText(phrase.en, phrase.id)).toEqual([])
    }
  })

  it('コツは重複がなく、読める長さに収まっている', () => {
    const seen = new Set<string>()
    expect(TIP_LINES.length).toBe(TIPS.length)
    for (const tip of TIPS) {
      expect(seen.has(tip), `コツが重複: ${tip}`).toBe(false)
      seen.add(tip)
      expect(tip.length, `長すぎるコツ: ${tip}`).toBeLessThanOrEqual(90)
      expect(tip.trim().length).toBeGreaterThan(10)
      expect(tip.includes('{'), `プレースホルダが残っている: ${tip}`).toBe(false)
    }
  })

  it('励ましの素材は重複がなく、使える差し込みスロットだけを使う', () => {
    const groups = [
      ['単体', ENCOURAGE_LINES],
      ['締め', ENCOURAGE_CLOSINGS],
      ...BRANCHES.map((branch) => [branch, ENCOURAGE_BODIES[branch]] as const),
      ...Object.entries(TIME_GREETINGS),
    ] as const
    for (const [label, lines] of groups) {
      const seen = new Set<string>()
      for (const line of lines) {
        expect(seen.has(line), `${label} で重複: ${line}`).toBe(false)
        seen.add(line)
        expect(line.trim().length, `${label} に空の文`).toBeGreaterThan(3)
        for (const slot of line.matchAll(/\{(\w+)\}/g)) {
          expect(ALLOWED_SLOTS.has(slot[1]), `${label} に未知のスロット: ${line}`).toBe(true)
        }
      }
    }
  })

  it('どの状況にも組み立て用の本文が十分にある', () => {
    for (const branch of BRANCHES) {
      expect(ENCOURAGE_BODIES[branch].length, branch).toBeGreaterThanOrEqual(20)
    }
  })
})
