// 生成コンテンツの検証ルール(純粋関数)。
// 教師レビューを行わない前提のため、機械的に落とせる欠陥はここで全部落とす。
// content.test.ts(既存コンテンツのCIゲート)と scripts/validate-batch.mjs(生成物の取り込み前検査)で共用する。

import type { CefrLevel, QuizQuestion, ReadingPassage } from './types.ts'

export type Issue = { where: string; message: string }

/** レベルごとの1文あたり平均語数の上限。これを超える本文は読み手のレベルに合っていない。 */
export const MAX_AVG_SENTENCE_WORDS: Record<'A2' | 'B1' | 'B2', number> = { A2: 14, B1: 20, B2: 26 }

/**
 * 文法レッスンの例文に課す1文あたり平均語数の下限。
 * B2の構文(倒置・cleft・分詞構文・関係詞の発展)は長い文を制御するための道具なので、
 * 短文だけで練習させるとレベル相当のインプットにならない。下限を置いているレベルだけを持つ。
 */
export const MIN_AVG_EXAMPLE_WORDS: Partial<Record<CefrLevel, number>> = { B2: 12 }

/** 文法レッスンの例文が、そのレベルの下限平均語数を満たしているか。 */
export function checkExampleLength(
  level: CefrLevel,
  examples: readonly { en: string }[],
  where: string,
): Issue[] {
  const floor = MIN_AVG_EXAMPLE_WORDS[level]
  if (floor === undefined || examples.length === 0) return []
  const average = examples.reduce((sum, example) => sum + words(example.en).length, 0) / examples.length
  if (average < floor) {
    return [{ where, message: `例文の平均語数 ${average.toFixed(1)}語が ${level} の下限 ${floor}語を下回っています` }]
  }
  return []
}

/** レベルごとに課すクイズの問題数。B2は到達判定に足る演習量を確保するため多く取る。 */
export const REQUIRED_QUIZ_COUNT: Record<CefrLevel, number> = {
  A2: 4,
  'A2+': 4,
  B1: 4,
  'B1+': 4,
  B2: 10,
}

/** 音声に渡せない文字。TTSが記号を読み上げたり無音になったりする。 */
const FORBIDDEN_AUDIO_CHARACTERS = ['(', ')', '[', ']', '_', '*', '#', '/']

export function checkAudioText(text: string, where: string): Issue[] {
  const issues: Issue[] = []
  for (const character of FORBIDDEN_AUDIO_CHARACTERS) {
    if (text.includes(character)) issues.push({ where, message: `音声用テキストに ${character} が含まれています` })
  }
  // 大文字で始まる複数語だけを「文」とみなす。an apple のような句や発音の例語には句読点を求めない。
  const trimmed = text.trim()
  const looksLikeSentence = /^[A-Z]/.test(trimmed) && trimmed.includes(' ')
  if (looksLikeSentence && !/[.!?]$/.test(trimmed)) {
    issues.push({ where, message: '文末の句読点がありません' })
  }
  return issues
}

/** 選択肢問題の構造チェック。誤答解説の欠落はレビュワー不在では致命的なので必須にする。 */
export function checkQuestion(question: QuizQuestion, where: string): Issue[] {
  const issues: Issue[] = []
  const at = `${where}:${question.id}`

  if (question.choices.length < 3) issues.push({ where: at, message: '選択肢が3つ未満です' })
  if (new Set(question.choices).size !== question.choices.length) {
    issues.push({ where: at, message: '選択肢が重複しています' })
  }
  if (question.correctIndex < 0 || question.correctIndex >= question.choices.length) {
    issues.push({ where: at, message: 'correctIndex が選択肢の範囲外です' })
  }
  if (question.explanation.trim().length < 10) issues.push({ where: at, message: '解説が短すぎます' })
  if (!question.choiceNotes) {
    issues.push({ where: at, message: '誤答注記(choiceNotes)がありません' })
  } else {
    if (question.choiceNotes.length !== question.choices.length) {
      issues.push({ where: at, message: 'choiceNotes の数が選択肢と一致しません' })
    }
    question.choiceNotes.forEach((note, index) => {
      if (index !== question.correctIndex && !note) {
        issues.push({ where: at, message: `誤答 ${index + 1} の理由が書かれていません` })
      }
    })
  }
  if (question.audioEn) issues.push(...checkAudioText(question.audioEn, at))
  return issues
}

function words(text: string): string[] {
  return text.trim().split(/\s+/).filter(Boolean)
}

function sentences(text: string): string[] {
  return text.split(/(?<=[.!?])\s+/).filter((s) => s.trim().length > 0)
}

/** 本文がそのレベルの読み手に合っているか(平均文長)と、音声に渡せるかを見る。 */
export function checkPassage(passage: ReadingPassage): Issue[] {
  const issues: Issue[] = []
  const at = passage.id

  if (passage.paragraphs.length !== passage.paragraphsJa.length) {
    issues.push({ where: at, message: '段落と和訳の数が一致しません' })
  }
  for (const [index, paragraph] of passage.paragraphs.entries()) {
    issues.push(...checkAudioText(paragraph, `${at}:p${index + 1}`))
  }

  const allSentences = passage.paragraphs.flatMap(sentences)
  const averageWords = allSentences.reduce((sum, s) => sum + words(s).length, 0) / Math.max(allSentences.length, 1)
  const limit = MAX_AVG_SENTENCE_WORDS[passage.level]
  if (averageWords > limit) {
    issues.push({ where: at, message: `平均文長 ${averageWords.toFixed(1)}語が ${passage.level} の上限 ${limit}語を超えています` })
  }

  if (passage.questions.length < 4) issues.push({ where: at, message: '設問が4問未満です' })
  for (const question of passage.questions) issues.push(...checkQuestion(question, at))
  if (passage.canDo.length === 0) issues.push({ where: at, message: 'can-do 記述子が紐づいていません' })
  if (passage.glossary.length < 4) issues.push({ where: at, message: '語注が4件未満です' })

  return issues
}

/**
 * 近似重複の検出。生成モデルは同じ発想の文を量産するため、完全一致だけでは足りない。
 * 3-gram の Jaccard 係数が threshold 以上のペアを返す。
 */
export function findNearDuplicates(texts: { id: string; text: string }[], threshold = 0.6): Issue[] {
  const grams = texts.map(({ id, text }) => {
    const tokens = words(text.toLowerCase().replace(/[.,!?;:]/g, ''))
    const set = new Set<string>()
    for (let i = 0; i + 2 < tokens.length; i++) set.add(tokens.slice(i, i + 3).join(' '))
    return { id, set }
  })

  const issues: Issue[] = []
  for (let i = 0; i < grams.length; i++) {
    for (let j = i + 1; j < grams.length; j++) {
      const a = grams[i].set
      const b = grams[j].set
      if (a.size === 0 || b.size === 0) continue
      let shared = 0
      for (const gram of a) if (b.has(gram)) shared++
      const jaccard = shared / (a.size + b.size - shared)
      if (jaccard >= threshold) {
        issues.push({ where: grams[i].id, message: `${grams[j].id} と内容が重複しています(一致度 ${jaccard.toFixed(2)})` })
      }
    }
  }
  return issues
}

/**
 * 既習語のカバー率。未習語が多すぎる本文はレベル逸脱として落とす。
 * known には見出し語(4,500語)と、レベルによらず前提とする最基本語を渡す。
 */
export function unknownWordRatio(text: string, known: Set<string>): number {
  // 文中の大文字始まりは固有名詞とみなし、語彙負荷には数えない(文頭は除外できないので通常語として扱う)
  const candidates: string[] = []
  for (const sentence of sentences(text)) {
    words(sentence).forEach((raw, index) => {
      const token = raw.replace(/[^A-Za-z']/g, '')
      if (token.length === 0) return
      if (index > 0 && /^[A-Z]/.test(token)) return
      candidates.push(token.toLowerCase())
    })
  }
  if (candidates.length === 0) return 0
  const unknown = candidates.filter((token) => !stemCandidates(token).some((stem) => known.has(stem)))
  return unknown.length / candidates.length
}

/**
 * 語形変化を戻した候補。既習語との照合にだけ使う簡易版で、辞書は引かない。
 * 不規則変化(took, bought など)は basicWords 側に形のまま載せる。
 */
export function stemCandidates(token: string): string[] {
  const forms = [token]
  const add = (form: string) => {
    if (form.length >= 2) forms.push(form)
  }
  if (token.endsWith('ies')) add(`${token.slice(0, -3)}y`)
  if (token.endsWith('ier')) add(`${token.slice(0, -3)}y`)
  if (token.endsWith('iest')) add(`${token.slice(0, -4)}y`)
  if (token.endsWith('es')) add(token.slice(0, -2))
  if (token.endsWith('s')) add(token.slice(0, -1))
  if (token.endsWith('ed')) {
    add(token.slice(0, -2))
    add(token.slice(0, -1))
  }
  if (token.endsWith('ing')) {
    add(token.slice(0, -3))
    add(`${token.slice(0, -3)}e`)
  }
  if (token.endsWith('ly')) add(token.slice(0, -2))
  if (token.endsWith('er')) {
    add(token.slice(0, -2))
    add(token.slice(0, -1))
  }
  if (token.endsWith('est')) add(token.slice(0, -3))
  // 子音を重ねる変化: stopped → stop, running → run
  const doubled = token.match(/^(.*[aeiou])([bdgklmnprt])\2(ed|ing)$/)
  if (doubled) add(doubled[1] + doubled[2])
  return forms
}
