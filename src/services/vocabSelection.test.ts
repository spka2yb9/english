import { describe, expect, it } from 'vitest'
import {
  intervalDays,
  masteryOf,
  recordAnswer,
  reviewScore,
  selectSessionWords,
  type WordStat,
  type WordStats,
} from './vocabSelection'

function seededRng(seed: number): () => number {
  let s = seed >>> 0
  return () => {
    s = (s + 0x6d2b79f5) >>> 0
    let t = Math.imul(s ^ (s >>> 15), 1 | s)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

const NOW = 1_700_000_000_000
const DAY = 86_400_000
const POOL = Array.from({ length: 50 }, (_, i) => `w${i}`)

describe('selectSessionWords', () => {
  it('十分な語があれば重複なしで10語を返す', () => {
    const result = selectSessionWords(POOL, {}, NOW, 10, seededRng(1))
    expect(result).toHaveLength(10)
    expect(new Set(result).size).toBe(10)
  })

  it('プールが10語未満なら全語を返す', () => {
    const result = selectSessionWords(['a', 'b', 'c'], {}, NOW, 10, seededRng(1))
    expect([...result].sort()).toEqual(['a', 'b', 'c'])
  })

  it('予定日を過ぎた語を再出題し、まだ予定日前の語は出さない', () => {
    const stats: WordStats = {}
    // w0: 直近で間違えた(間隔1日 → 3日経過で延滞)。w1: 3連続正解(間隔8日 → まだ予定日前)
    stats.w0 = { seen: 3, known: 0, unknown: 3, lastAt: NOW - 3 * DAY, streak: 0 }
    stats.w1 = { seen: 3, known: 3, unknown: 0, lastAt: NOW - 3 * DAY, streak: 3 }
    const result = selectSessionWords(POOL, stats, NOW, 10, seededRng(1))
    expect(result).toContain('w0')
    expect(result).not.toContain('w1')
  })

  it('予定日前の語しかなければ、未出題語で埋める', () => {
    const stats: WordStats = {}
    for (let i = 0; i < 20; i++) {
      stats[`w${i}`] = { seen: 4, known: 4, unknown: 0, lastAt: NOW, streak: 4 }
    }
    const result = selectSessionWords(POOL, stats, NOW, 10, seededRng(3))
    expect(result).toHaveLength(10)
    expect(result.filter((id) => stats[id])).toHaveLength(0)
  })

  it('未出題語もセッションに含まれる', () => {
    const stats: WordStats = {}
    for (let i = 0; i < 20; i++) {
      stats[`w${i}`] = { seen: 1, known: 0, unknown: 1, lastAt: NOW - DAY, streak: 0 }
    }
    const result = selectSessionWords(POOL, stats, NOW, 10, seededRng(1))
    const unseenPicked = result.filter((id) => !stats[id])
    expect(unseenPicked.length).toBeGreaterThan(0)
  })
})

describe('レベルの重み付け', () => {
  const levelOf = (id: string) => (id.startsWith('a') ? 'A2' : id.startsWith('b') ? 'B1' : 'B2')
  const A2 = Array.from({ length: 30 }, (_, i) => `a${i}`)
  const B2 = Array.from({ length: 30 }, (_, i) => `c${i}`)

  it('未出題語はレベルの低い語ほど選ばれやすい', () => {
    let a2 = 0
    let b2 = 0
    for (let seed = 1; seed <= 100; seed++) {
      const picked = selectSessionWords([...A2, ...B2], {}, NOW, 5, seededRng(seed), levelOf)
      a2 += picked.filter((id) => levelOf(id) === 'A2').length
      b2 += picked.filter((id) => levelOf(id) === 'B2').length
    }
    // 同数のプールでも、重み 3:1 の A2 の方が多く出る
    expect(a2).toBeGreaterThan(b2 * 1.5)
  })

  it('予定日を過ぎた語はレベルの低い語から先に出す', () => {
    const stats: WordStats = {}
    // 全語が同じ条件で延滞している状態
    for (const id of [...A2, ...B2]) {
      stats[id] = { seen: 1, known: 0, unknown: 1, lastAt: NOW - 3 * DAY, streak: 0 }
    }
    const picked = selectSessionWords([...A2, ...B2], stats, NOW, 5, seededRng(1), levelOf)
    expect(picked).toHaveLength(5)
    expect(picked.every((id) => levelOf(id) === 'A2')).toBe(true)
  })

  it('再学習中の語はレベルに関係なく最優先で戻る', () => {
    let stats: WordStats = {}
    stats = recordAnswer(stats, 'c0', false, NOW) // B2 を間違えた
    for (let i = 0; i < 10; i++) {
      stats[`a${i}`] = { seen: 4, known: 4, unknown: 0, lastAt: NOW, streak: 4 } // A2 は予定日前
    }
    const picked = selectSessionWords([...A2.slice(0, 10), 'c0'], stats, NOW, 5, seededRng(1), levelOf)
    expect(picked).toContain('c0')
  })

  it('再学習中が枠を超えるときは、レベルの低い語と古い取りこぼしが優先される', () => {
    // A2 3語と B2 10語は1日前、B2 1語は30日前に間違えた状態
    const fresh = [...A2.slice(0, 3), ...B2.slice(0, 10)]
    let stats: WordStats = {}
    for (const id of fresh) stats = recordAnswer(stats, id, false, NOW - DAY)
    stats = recordAnswer(stats, 'c10', false, NOW - 30 * DAY)

    const appearances = new Map<string, number>()
    const sessions = 200
    for (let seed = 1; seed <= sessions; seed++) {
      const picked = selectSessionWords([...fresh, 'c10'], stats, NOW, 5, seededRng(seed), levelOf)
      for (const id of picked) appearances.set(id, (appearances.get(id) ?? 0) + 1)
    }
    const rate = (id: string) => appearances.get(id) ?? 0
    const a2PerWord = A2.slice(0, 3).reduce((sum, id) => sum + rate(id), 0) / 3
    const b2PerWord = B2.slice(0, 10).reduce((sum, id) => sum + rate(id), 0) / 10
    // 同じ経過日数なら A2 の方が出やすい
    expect(a2PerWord).toBeGreaterThan(b2PerWord * 2)
    // 古い取りこぼしは、新しい B2 より優先して戻る
    expect(rate('c10')).toBeGreaterThan(b2PerWord)
  })

  it('levelOf を渡さなければ従来どおりレベルを見ない(音声練習の互換)', () => {
    let a2 = 0
    let b2 = 0
    for (let seed = 1; seed <= 200; seed++) {
      const picked = selectSessionWords([...A2, ...B2], {}, NOW, 5, seededRng(seed))
      a2 += picked.filter((id) => levelOf(id) === 'A2').length
      b2 += picked.filter((id) => levelOf(id) === 'B2').length
    }
    // 同数のプールなので偏らない
    expect(Math.abs(a2 - b2) / (a2 + b2)).toBeLessThan(0.15)
  })
})

describe('intervalDays', () => {
  it('連続正解のたびに間隔が倍になる', () => {
    const base = { seen: 1, known: 1, unknown: 0, lastAt: NOW }
    expect(intervalDays({ ...base, streak: 0 })).toBe(1)
    expect(intervalDays({ ...base, streak: 1 })).toBe(2)
    expect(intervalDays({ ...base, streak: 3 })).toBe(8)
  })

  it('間隔には上限がある', () => {
    expect(intervalDays({ seen: 20, known: 20, unknown: 0, lastAt: NOW, streak: 20 })).toBe(60)
  })

  it('streak 未記録の古い履歴は正誤差から推定する', () => {
    expect(intervalDays({ seen: 3, known: 3, unknown: 0, lastAt: NOW })).toBe(8)
    expect(intervalDays({ seen: 4, known: 2, unknown: 2, lastAt: NOW })).toBe(1)
  })
})

describe('reviewScore', () => {
  it('予定日で1.0になり、延滞するほど大きくなる', () => {
    const stat = { seen: 2, known: 2, unknown: 0, lastAt: NOW - 2 * DAY, streak: 1 } // 間隔2日
    expect(reviewScore(stat, NOW)).toBe(1)
    expect(reviewScore({ ...stat, lastAt: NOW - 6 * DAY }, NOW)).toBe(3)
    expect(reviewScore({ ...stat, lastAt: NOW - DAY }, NOW)).toBeLessThan(1)
  })

  it('正解を重ねた語ほど、同じ経過日数での優先度が低い', () => {
    const fresh = { seen: 1, known: 0, unknown: 1, lastAt: NOW - 4 * DAY, streak: 0 }
    const mature = { seen: 5, known: 5, unknown: 0, lastAt: NOW - 4 * DAY, streak: 5 }
    expect(reviewScore(mature, NOW)).toBeLessThan(reviewScore(fresh, NOW))
  })
})

describe('recordAnswer', () => {
  it('回答を集計し、元の stats を変更しない', () => {
    const stats: WordStats = { a: { seen: 1, known: 1, unknown: 0, lastAt: 100, streak: 1 } }
    const next = recordAnswer(stats, 'a', false, NOW)
    expect(next.a).toEqual({ seen: 2, known: 1, unknown: 1, lastAt: NOW, streak: 0, lapsed: true })
    expect(stats.a.seen).toBe(1)
  })

  it('未知の語は新規レコードを作る', () => {
    const next = recordAnswer({}, 'b', true, NOW)
    expect(next.b).toEqual({ seen: 1, known: 1, unknown: 0, lastAt: NOW, streak: 1, lapsed: false })
  })

  it('「わかる」で連続記録が伸び、「わからない」でリセットされる', () => {
    let stats: WordStats = {}
    stats = recordAnswer(stats, 'c', true, NOW)
    stats = recordAnswer(stats, 'c', true, NOW)
    expect(stats.c.streak).toBe(2)
    stats = recordAnswer(stats, 'c', false, NOW)
    expect(stats.c.streak).toBe(0)
  })
})

describe('わからなかった語の再学習', () => {
  it('「わからない」直後は、経過0でも延滞語より優先される', () => {
    const lapsed = recordAnswer({}, 'x', false, NOW).x
    const overdue: WordStat = { seen: 1, known: 1, unknown: 0, lastAt: NOW - 30 * DAY, streak: 1 }
    expect(reviewScore(lapsed, NOW)).toBeGreaterThan(reviewScore(overdue, NOW))
  })

  it('次の10問に必ず入る(未出題語より先に選ばれる)', () => {
    let stats: WordStats = {}
    // セッションで w0〜w3 を間違え、その周回で「わかる」に直した状態
    for (const id of ['w0', 'w1', 'w2', 'w3']) {
      stats = recordAnswer(stats, id, false, NOW)
      stats = recordAnswer(stats, id, true, NOW)
    }
    const picked = selectSessionWords(POOL, stats, NOW, 10, seededRng(3))
    expect(picked).toEqual(expect.arrayContaining(['w0', 'w1', 'w2', 'w3']))
  })

  it('わからなかった語が半分を超えても、全部が次のセッションに戻る', () => {
    let stats: WordStats = {}
    const missed = POOL.slice(0, 8)
    for (const id of missed) stats = recordAnswer(stats, id, false, NOW)
    const picked = selectSessionWords(POOL, stats, NOW, 10, seededRng(5))
    expect(picked).toEqual(expect.arrayContaining(missed))
  })

  it('別セッションでもう一度正解すると再学習を抜け、通常の間隔に戻る', () => {
    let stats = recordAnswer({}, 'y', false, NOW)
    stats = recordAnswer(stats, 'y', true, NOW) // 同じセッション内の再出題 → まだ抜けない
    expect(stats.y.lapsed).toBe(true)
    stats = recordAnswer(stats, 'y', true, NOW + DAY) // 次のセッション → 抜ける
    expect(stats.y.lapsed).toBe(false)
    expect(reviewScore(stats.y, NOW + DAY)).toBe(0)
  })

  it('何度も「わかる」が続く語は、しばらく出題されない', () => {
    let stats: WordStats = {}
    for (let i = 0; i < 8; i += 1) stats = recordAnswer(stats, 'z', true, NOW + i * DAY)
    expect(intervalDays(stats.z)).toBe(60) // 上限60日まで伸びる
    expect(reviewScore(stats.z, NOW + 8 * DAY + 30 * DAY)).toBeLessThan(1)
  })
})

describe('学習状況の分類', () => {
  it('別セッションで3回続けて「わかる」になると定着になる', () => {
    let stats: WordStats = {}
    for (let i = 0; i < 3; i += 1) stats = recordAnswer(stats, 'w', true, NOW + i * DAY)
    expect(masteryOf(stats.w)).toBe('mastered')
  })

  it('2回目までは学習中のまま', () => {
    let stats = recordAnswer({}, 'w', true, NOW)
    stats = recordAnswer(stats, 'w', true, NOW + DAY)
    expect(masteryOf(stats.w)).toBe('learning')
  })

  it('定着した語でも「わからない」と答えると苦手に落ちる', () => {
    let stats: WordStats = {}
    for (let i = 0; i < 3; i += 1) stats = recordAnswer(stats, 'w', true, NOW + i * DAY)
    stats = recordAnswer(stats, 'w', false, NOW + 3 * DAY)
    expect(masteryOf(stats.w)).toBe('weak')
  })

  it('再学習を抜けたばかりの語は学習中(正解が積み上がるまで定着にしない)', () => {
    let stats = recordAnswer({}, 'w', false, NOW)
    stats = recordAnswer(stats, 'w', true, NOW + DAY)
    stats = recordAnswer(stats, 'w', true, NOW + 2 * DAY)
    expect(masteryOf(stats.w)).toBe('learning')
  })
})
