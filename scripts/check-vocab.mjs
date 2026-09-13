// 語彙エントリの自己点検。content.test.ts が落ちる前に、どの語の何が足りないかを一覧する。
import { allVocabulary } from '../src/content/vocabulary/index.ts'

const bad = []
const seenId = new Set(), seenWord = new Set()
for (const e of allVocabulary) {
  const miss = []
  if (!e.mnemonic?.length) miss.push('mnemonic')
  if (!e.collocations?.length) miss.push('collocations')
  else {
    const head = e.word.toLowerCase().split(' ')[0]
    const stem = head.slice(0, Math.max(3, head.length - 3))
    if (!e.collocations.some((c) => c.toLowerCase().includes(stem))) miss.push(`stem "${stem}"`)
  }
  {
    const head = e.word.toLowerCase().split(' ')[0]
    const stem = head.slice(0, Math.max(3, head.length - 3))
    if (!e.exampleSentence.toLowerCase().includes(stem)) miss.push(`example lacks "${stem}"`)
  }
  // 英語で書くべき欄に日本語が混ざる事故を落とす(コロケーションに「〜技術」と書いてしまう類)
  // café や £ は英文に出てよい。落としたいのは日本語が紛れ込んだ事故だけ。
  const cjk = (t) => /[\u3000-\u30ff\u4e00-\u9fff\uff00-\uffef]/.test(t)
  if (cjk(e.exampleSentence)) miss.push('example has Japanese')
  for (const c of e.collocations ?? []) if (cjk(c)) miss.push(`collocation has Japanese: ${c}`)
  for (const w of e.relatedWords ?? []) if (cjk(w)) miss.push(`relatedWord has Japanese: ${w}`)
  if (!e.pronunciation?.length) miss.push('pronunciation')
  if (!['A2', 'B1', 'B2'].includes(e.level)) miss.push('level')
  if (seenId.has(e.id)) miss.push('dup id')
  if (seenWord.has(e.word.toLowerCase())) miss.push('dup word')
  seenId.add(e.id); seenWord.add(e.word.toLowerCase())
  if (miss.length) bad.push(`${e.id}: ${miss.join(', ')}`)
}
console.log(`total ${allVocabulary.length}, bad ${bad.length}`)
for (const b of bad) console.log(' ', b)

// 訳文に英単語が残る事故(「彼女は politics から」)は自動判定できない。
// hyphen や synonym のように英語を引くのが正しい語もあるので、目で見る一覧として出すだけにする。
const eyeball = allVocabulary.filter((e) => /[A-Za-z]{3,}/.test(e.exampleTranslationJa))
console.log(`\n訳文に英字を含む ${eyeball.length} 件(正当なものも含む。目で確認する)`)
for (const e of eyeball) console.log(' ', e.id, '::', e.exampleTranslationJa)
