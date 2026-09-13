import { readFileSync, readdirSync } from 'node:fs'
import { join } from 'node:path'

const vocabularyDirectory = new URL('../src/content/vocabulary/', import.meta.url)
const oxfordPath = process.argv[2] ?? '/tmp/oxford-5000.csv'

const existingWords = new Set()
for (const file of readdirSync(vocabularyDirectory).filter((name) => /^batch\d+\.ts$/.test(name))) {
  const source = readFileSync(new URL(file, vocabularyDirectory), 'utf8')
  for (const match of source.matchAll(/\bword:\s*(['"])(.*?)\1/g)) {
    existingWords.add(normalizeWord(match[2]))
  }
}

const levelRank = new Map([
  ['a2', 0],
  ['b1', 1],
  ['b2', 2],
])
const candidates = new Map()

for (const line of readFileSync(oxfordPath, 'utf8').split(/\r?\n/).slice(1)) {
  const [word, level, transcription, , wordClass] = line.split(';')
  const normalized = normalizeWord(word)
  if (!normalized || !levelRank.has(level)) continue

  const previous = candidates.get(normalized)
  if (!previous) {
    candidates.set(normalized, {
      word: word.trim(),
      levels: new Set([level]),
      transcriptions: new Set(transcription ? [transcription] : []),
      classes: new Set(wordClass ? [wordClass] : []),
    })
    continue
  }

  previous.levels.add(level)
  if (transcription) previous.transcriptions.add(transcription)
  if (wordClass) previous.classes.add(wordClass)
}

const missing = [...candidates.entries()].filter(([word]) => !existingWords.has(word))
const byLevel = { a2: 0, b1: 0, b2: 0 }
for (const [, candidate] of missing) {
  const lowestLevel = [...candidate.levels].sort(
    (left, right) => levelRank.get(left) - levelRank.get(right),
  )[0]
  byLevel[lowestLevel] += 1
}

console.log(
  JSON.stringify(
    {
      existing: existingWords.size,
      oxfordA2ToB2: candidates.size,
      overlap: candidates.size - missing.length,
      missing: missing.length,
      union: new Set([...existingWords, ...candidates.keys()]).size,
      missingByLowestLevel: byLevel,
      neededForThreeThousand: Math.max(0, 3000 - existingWords.size),
      source: join(process.cwd(), oxfordPath),
    },
    null,
    2,
  ),
)

function normalizeWord(word) {
  return word.trim().toLowerCase().replace(/\s+/g, ' ')
}
