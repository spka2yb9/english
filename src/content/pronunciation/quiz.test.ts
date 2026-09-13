import { describe, expect, it } from 'vitest'
import { ipaEntries } from './data'
import { blankSymbol, buildIpaQuestions, ipaQuizWords, similarSymbols } from './quiz'

const WORDS_PER_SYMBOL = 10

describe('発音記号の穴埋め演習データ', () => {
  it('全記号を10語ずつカバーする', () => {
    const counts = new Map(ipaEntries.map((e) => [e.symbol, 0]))
    for (const item of ipaQuizWords) {
      const symbol = blankSymbol(item.ipa)
      expect(counts.has(symbol), `未知の記号 ${symbol} (${item.word})`).toBe(true)
      counts.set(symbol, (counts.get(symbol) ?? 0) + 1)
    }
    expect([...counts].filter(([, n]) => n !== WORDS_PER_SYMBOL)).toEqual([])
  })

  it('空所は1か所で、答えと同じ記号が空所の外に見えていない', () => {
    for (const item of ipaQuizWords) {
      expect(item.ipa.match(/\[/g)?.length, item.word).toBe(1)
      expect(item.ipa.match(/\]/g)?.length, item.word).toBe(1)
      const visible = item.ipa.replace(/\[[^\]]*\]/, '')
      expect(visible.includes(blankSymbol(item.ipa)), `${item.word} は答えが見えている`).toBe(false)
    }
  })

  it('全記号に誤答候補が3件以上あり、正解自身を含まない', () => {
    for (const entry of ipaEntries) {
      const similar = similarSymbols(entry.symbol)
      expect(similar.length, entry.symbol).toBeGreaterThanOrEqual(3)
      expect(similar, entry.symbol).not.toContain(entry.symbol)
      expect(new Set(similar).size, entry.symbol).toBe(similar.length)
      expect(similar.filter((s) => !ipaEntries.some((e) => e.symbol === s)), entry.symbol).toEqual([])
    }
  })

  it('同じ語と記号の組み合わせが重複しない', () => {
    const keys = ipaQuizWords.map((item) => `${item.word}/${item.ipa}`)
    expect(new Set(keys).size).toBe(keys.length)
  })
})

describe('buildIpaQuestions', () => {
  it('正解を含む4択と、空所入りの発音記号を作る', () => {
    const questions = buildIpaQuestions(ipaQuizWords.length)
    expect(questions).toHaveLength(ipaQuizWords.length)
    for (const q of questions) {
      expect(q.choices).toHaveLength(4)
      expect(new Set(q.choices).size).toBe(4)
      expect(q.sentence).toContain('___')
      expect(q.sentence).not.toContain(q.choices[q.correctIndex])
      expect(q.audioEn).toBeTruthy()
    }
  })

  it('誤答は混同しやすい記号から作る', () => {
    for (const q of buildIpaQuestions(ipaQuizWords.length)) {
      const answer = q.choices[q.correctIndex]
      const wrong = q.choices.filter((c) => c !== answer)
      expect(wrong.every((c) => similarSymbols(answer).includes(c)), `${q.id}: ${wrong}`).toBe(true)
    }
  })

  it('出題語の音声を設問で再生できる', () => {
    for (const q of buildIpaQuestions(ipaQuizWords.length)) {
      expect(q.prompt).toContain(q.promptAudio)
    }
  })
})
