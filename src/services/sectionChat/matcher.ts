// セクション内Q&Aの判定器。
//
// 入力された質問文から「どのQAに答えてほしいか」を選ぶ。精度のための仕掛け:
// 1. 正規化 — NFKC・小文字化・短縮形の展開(isn't → is not)・記号の除去
// 2. トークン化 — 英単語(軽い語幹化つき)・日本語の文字bigram・文法用語の辞書語
// 3. 重み — コーパス全体の出現頻度から idf を計算し、珍しい語ほど強く効かせる
// 4. 意図判定 — 重み付き語彙(INTENT_TERMS)で「何を聞かれているか」を分類
// 5. 意図による絞り込み — 意図が明確なら、その意図のQAを優先して誤爆を防ぐ
// 6. フレーズ加点 — 例文や用語がそのまま質問に含まれていれば大きく加点
// 7. 曖昧な入力 — 一語(「三単現」)や体言止めは、用語QAへの直接一致と
//    短い質問向けの緩い足切りで拾う
// 8. 文脈フォローアップ — 「もっと詳しく」「それって?」「他には?」は直前に答えたQAから解決する
//
// 一致しなければ正直に「答えられない」を返す。これがこの機能の信頼性の源。

import type { GrammarLesson } from '../../content/types'
import { buildSectionQa } from './corpus'
import { CURRICULUM_TERMS, EN_TERM_SYNONYMS, FOLLOWUP_PATTERNS, INTENT_AFFINITY, INTENT_TERMS, TERM_SYNONYMS } from './intents'
import { FALLBACK_NOTE, FOLLOWUP_LEADS, SMALL_TALK_LEADS } from './phrasings'
import type { ChatReply, QaEntry, QaIntent } from './types'

/** これ未満しか一致しなければ答えない。 */
const ANSWER_MIN = 0.34
/** 意図判定を採用する最低スコア。 */
const INTENT_MIN = 0.9
/** 意図つきの候補がこのスコア以上なら、その意図の中だけで答える。 */
const INTENT_LOCK_MIN = 0.42
/** 意図ロックが全体1位を覆すための最小差。負ける量が大きい候補は、質問文の完全一致などが強い証拠とみなす。 */
const INTENT_LOCK_MARGIN = 0.12
/** 「もっと詳しく」「他には?」などを返答の返答とみなす最大の長さ。これを超える質問は内容語を含む通常の質問。 */
const FOLLOWUP_MAX_LENGTH = 14
/** これ未満の idf(=「教えて」のようなどこにでもある語)は内容語とみなさない。 */
const IDF_FLOOR = 1
/** 短い質問(一語・体言止め)では足切りを緩める。「not」「is」のような語も拾う。 */
const SHORT_QUERY_FLOOR = 0.5
/** コーパスに無い語の罰則。未知語が多い質問は、たまたま一致した1語で答えない。 */
const UNKNOWN_PENALTY = 2
/** 罰則の上限(長い未知語をbigramで数えても過剰に罰しない)。 */
const UNKNOWN_PENALTY_MAX = 6
/** 直前の話題との重なりに与える加点(短い質問のときだけ)。 */
const CONTEXT_BONUS = 0.12
/** 関連QAとみなす最低の重なり。 */
const RELATED_MIN = 0.25

/** 短縮形の展開。canonical 側も質問側も同じ展開を通す。 */
const CONTRACTIONS: ReadonlyArray<readonly [RegExp, string]> = [
  [/\bcan't\b/g, 'can not'],
  [/\bwon't\b/g, 'will not'],
  [/\bdon't\b/g, 'do not'],
  [/\bdoesn't\b/g, 'does not'],
  [/\bdidn't\b/g, 'did not'],
  [/\bisn't\b/g, 'is not'],
  [/\baren't\b/g, 'are not'],
  [/\bwasn't\b/g, 'was not'],
  [/\bweren't\b/g, 'were not'],
  [/\bhaven't\b/g, 'have not'],
  [/\bhasn't\b/g, 'has not'],
  [/\bhadn't\b/g, 'had not'],
  [/\bi'm\b/g, 'i am'],
  [/\bit's\b/g, 'it is'],
  [/\bthat's\b/g, 'that is'],
  [/\bwhat's\b/g, 'what is'],
  [/\blet's\b/g, 'let us'],
  [/\bi'll\b/g, 'i will'],
  [/\byou're\b/g, 'you are'],
  [/\bthey're\b/g, 'they are'],
  [/\bwe're\b/g, 'we are'],
  [/\bhe's\b/g, 'he is'],
  [/\bshe's\b/g, 'she is'],
]

/** 軽い語幹化。「am / is / are の違い」のような使い分けを壊さないよう、原形もトークンとして残す。 */
const STEMS: Record<string, string> = {
  am: 'be', is: 'be', are: 'be', was: 'be', were: 'be', been: 'be', being: 'be',
  does: 'do', did: 'do', done: 'do',
  has: 'have', had: 'have',
  goes: 'go', went: 'go', gone: 'go',
  studies: 'study', studied: 'study',
  watches: 'watch', watched: 'watch',
  plays: 'play', played: 'play',
  works: 'work', worked: 'work',
  likes: 'like', liked: 'like',
  sleeps: 'sleep', slept: 'sleep',
  takes: 'take', took: 'take',
  leaves: 'leave', left: 'leave',
  boils: 'boil', boiled: 'boil',
  says: 'say', said: 'say',
  tells: 'tell', told: 'tell',
  writes: 'write', wrote: 'write', written: 'write',
  reads: 'read',
  buys: 'buy', bought: 'buy',
  brings: 'bring', brought: 'bring',
  teaches: 'teach', taught: 'teach',
  learns: 'learn', learned: 'learn', learnt: 'learn',
  runs: 'run', ran: 'run',
  comes: 'come', came: 'come',
  gets: 'get', got: 'get',
  makes: 'make', made: 'make',
}

/** 日本語の辞書語。意図語彙とカリキュラム用語の全体を使う。 */
const JAPANESE_TERMS: readonly string[] = [
  ...new Set([
    ...Object.values(INTENT_TERMS).flatMap((terms) => terms.map(([term]) => term)),
    ...CURRICULUM_TERMS,
    ...Object.keys(TERM_SYNONYMS),
  ]),
].filter((term) => term.length >= 2 && /[ぁ-んァ-ヶ一-龯]/.test(term))

const ASCII_TERM = /^[a-z]/

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}

const termRegexCache = new Map<string, RegExp>()

function containsTerm(normalized: string, term: string): boolean {
  if (ASCII_TERM.test(term)) {
    let regex = termRegexCache.get(term)
    if (!regex) {
      regex = new RegExp(`(^|[^a-z])${escapeRegExp(term).replace(/ /g, '\\s+')}([^a-z]|$)`)
      termRegexCache.set(term, regex)
    }
    return regex.test(normalized)
  }
  return normalized.includes(term)
}

/** 質問文の正規化。canonical(コーパス側)と入力の両方に同じ処理を通す。 */
export function normalizeQuestion(text: string): string {
  let normalized = text.normalize('NFKC').toLowerCase().replace(/[’‘`]/g, "'")
  for (const [pattern, replacement] of CONTRACTIONS) normalized = normalized.replace(pattern, replacement)
  normalized = normalized
    .replace(/[。、．，！？!?…・「」『』（）()[\]【】〈〉《》:：;；"“”/\\.,]/g, ' ')
    .replace(/[-–—]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
  // 丁寧な前置き・呼びかけは、質問の中身ではないので落とす(「すみません、which one?」)
  const FILLER = /^(?:すみません|すいません|ねえ|ねぇ|ちょっと教えて|教えてください|お願いします|あの|その|えっと|ええと|please|hi|hello|hey) /
  for (let index = 0; index < 2 && FILLER.test(normalized); index += 1) normalized = normalized.replace(FILLER, '')
  return normalized
}

function stemOf(word: string): string {
  if (STEMS[word]) return STEMS[word]
  if (word.length <= 3) return word
  if (word.endsWith('ies')) return `${word.slice(0, -3)}y`
  if (word.endsWith('ing')) return word.slice(0, -3)
  if (word.endsWith('ed')) return word.slice(0, -2)
  if (word.endsWith('es')) return word.slice(0, -2)
  if (word.endsWith('s') && !word.endsWith('ss')) return word.slice(0, -1)
  return word
}

/** 「不可算名詞」の中の「可算名詞」のように、否定接頭辞つきの語を誤って拾わない。 */
function includesJapaneseTerm(text: string, term: string): boolean {
  let index = text.indexOf(term)
  while (index !== -1) {
    const previous = text[index - 1]
    if (previous !== '不' && previous !== '非' && previous !== '無') return true
    index = text.indexOf(term, index + 1)
  }
  return false
}

/** トークン化。英単語は en:、日本語は bigram を ja:、辞書語は term: の接頭辞で区別する。 */
export function tokenize(text: string): string[] {
  const normalized = normalizeQuestion(text)
  const tokens = new Set<string>()
  for (const match of normalized.matchAll(/[a-z][a-z0-9']*/g)) {
    const word = match[0].replace(/'s$/, '')
    if (word.length < 2) continue
    tokens.add(`en:${word}`)
    const stem = stemOf(word)
    if (stem !== word) tokens.add(`en:${stem}`)
  }
  for (const match of normalized.matchAll(/[ぁ-んァ-ヶ一-龯ー]+/g)) {
    const run = match[0]
    if (run.length === 1) {
      tokens.add(`ja:${run}`)
      continue
    }
    for (let i = 0; i < run.length - 1; i += 1) tokens.add(`ja:${run.slice(i, i + 2)}`)
  }
  for (const term of JAPANESE_TERMS) {
    if (includesJapaneseTerm(normalized, term)) tokens.add(`term:${term}`)
  }
  // かな・口語の言い方は、用語の辞書トークンに寄せる(「受け身」→ 受動態)
  for (const [alias, canonical] of Object.entries(TERM_SYNONYMS)) {
    if (normalized.includes(alias)) tokens.add(`term:${canonical}`)
  }
  // 一語の曖昧な入力(「不可算」)は、その語で始まる用語に寄せる(不可算 → 不可算名詞)
  if (/^[ぁ-んァ-ヶ一-龯ー]{2,}$/.test(normalized)) {
    for (const term of CURRICULUM_TERMS) {
      if (term.length > normalized.length && term.startsWith(normalized)) tokens.add(`term:${term}`)
    }
  }
  // 英語の文法用語も日本語の用語に寄せる(subject → 主語)
  for (const [alias, canonical] of Object.entries(EN_TERM_SYNONYMS)) {
    if (containsTerm(normalized, alias)) tokens.add(`term:${canonical}`)
  }
  return [...tokens]
}

export type IntentMatch = { intent: QaIntent; score: number }

/** 質問の意図を分類する。語彙は intents.ts の INTENT_TERMS。 */
export function classifyIntent(text: string): IntentMatch | null {
  const normalized = normalizeQuestion(text)
  // 「彼は疲れているに違いありません」の「違い」は対比の意図ではない(慣用句をマスクする)
  const idiomMasked = normalized.replace(/に違い(?:ません|ない|なく|あり)/g, ' ')
  const scores: IntentMatch[] = []
  for (const intent of Object.keys(INTENT_TERMS) as QaIntent[]) {
    let score = 0
    const target = intent === 'difference' ? idiomMasked : normalized
    for (const [term, weight] of INTENT_TERMS[intent]) {
      if (containsTerm(target, term)) score += weight
    }
    if (score > 0) scores.push({ intent, score })
  }
  if (scores.length === 0) return null
  scores.sort((a, b) => b.score - a.score)

  let best = scores[0]
  // 「こんにちは、まとめは?」のように実質的な質問が同居するときは、質問の意図を優先する
  if ((best.intent === 'greeting' || best.intent === 'capability') && scores[1] && scores[1].score >= 1) {
    best = scores[1]
  }
  if (best.score < INTENT_MIN) return null
  // 英語を含まない「意味」は、英文の和訳ではなく用語の解説として扱う。
  // ただし「この文の意味は?」のような指示語つきと、「〜は英語で?」の英作文は、英文の意味を聞いている
  const referential = FOLLOWUP_PATTERNS.referential.some((term) => normalized.includes(term))
  if (best.intent === 'meaning' && !/[a-z]/.test(normalized) && !referential && !/(英語|英訳|えいご)/.test(normalized)) {
    best = { intent: 'concept', score: best.score * 0.6 }
  }
  return best
}

type Doc = {
  entry: QaEntry
  tokens: Set<string>
  normalizedQuestions: string[]
}

export type SectionChat = {
  reply(question: string): ChatReply
  /** 最初に出す質問候補(タップ用)。コーパスに存在する意図から選ぶ。 */
  suggestions(): string[]
  /** 直前の話題(返答の返答の文脈)を忘れて、新しい会話を始める。 */
  reset(): void
  /** コーパスのQA数(テスト・デバッグ用) */
  size: number
}

const SUGGESTION_INTENTS: readonly QaIntent[] = ['overview', 'example', 'difference', 'pattern', 'structure', 'summary', 'quiz']

/** フォローアップで「この意図の中から探す」対象になる意図。 */
const FOLLOWUP_ASK_INTENTS: readonly QaIntent[] = ['meaning', 'pattern', 'structure', 'example', 'concept', 'difference']

/**
 * レッスン1つぶんの質問応答エンジンを作る。
 * コーパスと索引はここで一度だけ構築し、以降の質問は索引との照合だけで答える。
 * `rng` はあいさつなどの言い回しの抽選に使う(テストでは固定値を渡す)。
 */
export function createSectionChat(lesson: GrammarLesson, rng: () => number = Math.random): SectionChat {
  const entries = buildSectionQa(lesson)
  const docs: Doc[] = entries.map((entry) => ({
    entry,
    tokens: new Set([...entry.questions, ...(entry.terms ?? []), entry.subject ?? ''].flatMap((text) => tokenize(text))),
    normalizedQuestions: entry.questions.map((question) => normalizeQuestion(question)).filter((question) => question.length >= 2),
  }))

  const df = new Map<string, number>()
  const postings = new Map<string, number[]>()
  docs.forEach((doc, index) => {
    for (const token of doc.tokens) {
      df.set(token, (df.get(token) ?? 0) + 1)
      const list = postings.get(token)
      if (list) list.push(index)
      else postings.set(token, [index])
    }
  })
  // 教材内容(検索語・主題・引用)に現れるトークン。質問テンプレートだけに現れる語
  // (translate など)と区別し、未知語まじりの質問の裏づけに使う。
  const contentTokens = new Set<string>()
  for (const doc of docs) {
    const quoteText = doc.entry.answer.quotes
      .flatMap((quote) => [quote.label, quote.en, quote.ja, quote.note, quote.text])
      .filter((text): text is string => Boolean(text))
      .join(' ')
    for (const token of tokenize([...(doc.entry.terms ?? []), doc.entry.subject ?? '', quoteText].join(' '))) {
      contentTokens.add(token)
    }
  }
  // 教材に実在する日本語のかたまり(繰り返し語の判定に使う)
  const japaneseRuns = new Set<string>()
  const collectRuns = (text: string) => {
    for (const match of text.normalize('NFKC').matchAll(/[ぁ-んァ-ヶ一-龯ー]+/g)) japaneseRuns.add(match[0])
  }
  for (const doc of docs) {
    for (const question of doc.entry.questions) collectRuns(question)
    for (const term of doc.entry.terms ?? []) collectRuns(term)
    if (doc.entry.subject) collectRuns(doc.entry.subject)
    for (const quote of doc.entry.answer.quotes) {
      for (const text of [quote.en, quote.ja, quote.note, quote.text]) if (text) collectRuns(text)
    }
  }
  const runsHaystack = `|${[...japaneseRuns].join('|')}|`
  const idf = (token: string) => Math.log(1 + (docs.length + 1) / ((df.get(token) ?? 0) + 0.5))
  const pick = <T>(items: readonly T[]): T => items[Math.min(items.length - 1, Math.floor(rng() * items.length))]

  /** 直前に答えたQA。返答の返答(「もっと詳しく」「それって?」)の解決に使う。 */
  let lastDoc: Doc | null = null

  const smallTalkLead = (doc: Doc): string | null => {
    if (doc.entry.id === 'smalltalk:greeting') return pick(SMALL_TALK_LEADS.greeting)
    if (doc.entry.id === 'smalltalk:thanks') return pick(SMALL_TALK_LEADS.thanks)
    if (doc.entry.id === 'smalltalk:capability') return pick(SMALL_TALK_LEADS.capability)
    return null
  }

  const answerFrom = (doc: Doc, leadOverride?: string, confidence = 1): ChatReply => ({
    kind: 'answer',
    intent: doc.entry.intent,
    confidence,
    lead: leadOverride ?? smallTalkLead(doc) ?? doc.entry.answer.lead,
    quotes: doc.entry.answer.quotes,
    followups: doc.entry.answer.followups,
  })

  /** 直前のQAと索引語が重なるQAを探す(「もっと詳しく」「他には」の解決)。 */
  const relatedEntry = (from: Doc, intents?: readonly QaIntent[]): { doc: Doc; score: number } | null => {
    const seeds = [...from.tokens].filter((token) => idf(token) >= 1).sort((a, b) => idf(b) - idf(a)).slice(0, 12)
    if (seeds.length === 0) return null
    const total = seeds.reduce((sum, token) => sum + idf(token), 0)
    let best: { doc: Doc; score: number } | null = null
    for (const doc of docs) {
      if (doc === from) continue
      if (doc.entry.intent === 'greeting' || doc.entry.intent === 'capability') continue
      if (intents && !intents.includes(doc.entry.intent)) continue
      let matched = 0
      for (const token of seeds) if (doc.tokens.has(token)) matched += idf(token)
      const score = matched / total
      if (score > (best?.score ?? 0)) best = { doc, score }
    }
    return best && best.score >= RELATED_MIN ? best : null
  }

  /** 同じ解説ブロックの次の段落(「もっと詳しく」で続きがあれば引く)。 */
  const nextParagraph = (from: Doc): Doc | null => {
    const match = /^(.*:concept:\d+)-(\d+)$/.exec(from.entry.id)
    if (!match) return null
    const nextId = `${match[1]}-${Number(match[2]) + 1}`
    return docs.find((doc) => doc.entry.id === nextId) ?? null
  }

  /** 返答の返答を、直前の話題から解決する。解決できなければ null(通常の検索へ)。 */
  const resolveFollowUp = (normalized: string, question: string): { doc: Doc; lead: string } | null => {
    const from = lastDoc
    if (!from) return null
    const has = (patterns: readonly string[]) => patterns.some((pattern) => normalized.includes(pattern))
    // 「別の時制で描く」のような内容語を含む長い質問を、フォローアップと誤解しない
    const followUpish = normalized.length <= FOLLOWUP_MAX_LENGTH

    if (followUpish && has(FOLLOWUP_PATTERNS.repeat)) return { doc: from, lead: FOLLOWUP_LEADS.repeat }
    if (followUpish && has(FOLLOWUP_PATTERNS.deepen)) {
      const next = nextParagraph(from)
      if (next) return { doc: next, lead: FOLLOWUP_LEADS.deepen }
      const related = relatedEntry(from)
      return related ? { doc: related.doc, lead: FOLLOWUP_LEADS.deepenFallback } : { doc: from, lead: FOLLOWUP_LEADS.repeat }
    }
    if (followUpish && has(FOLLOWUP_PATTERNS.related)) {
      const related = relatedEntry(from)
      return related ? { doc: related.doc, lead: FOLLOWUP_LEADS.related } : null
    }
    if (has(FOLLOWUP_PATTERNS.referential)) {
      const intent = classifyIntent(question)
      const wanted = intent && FOLLOWUP_ASK_INTENTS.includes(intent.intent) ? [intent.intent] : undefined
      // 「それの意味は?」の宛先。直前が意味QAならそのQA自身(例文+和訳)が答え。
      // 文型・構造QAなどの場合は、引用の英文と subject が一致する意味QAを探す。
      if (wanted?.[0] === 'meaning') {
        if (from.entry.intent === 'meaning' && from.entry.answer.quotes.some((quote) => quote.en && quote.ja)) {
          return { doc: from, lead: FOLLOWUP_LEADS.referExample }
        }
        const example = from.entry.answer.quotes.find((quote) => quote.en && quote.ja)
        if (example?.en) {
          const normalizedEn = normalizeQuestion(example.en)
          const match = docs.find(
            (doc) =>
              doc.entry.intent === 'meaning' &&
              doc.entry.subject &&
              normalizeQuestion(doc.entry.subject) === normalizedEn,
          )
          if (match) return { doc: match, lead: FOLLOWUP_LEADS.referExample }
        }
        const meaning = relatedEntry(from, ['meaning'])
        if (meaning) return { doc: meaning.doc, lead: FOLLOWUP_LEADS.referExample }
      }
      if (wanted && wanted.includes(from.entry.intent)) return { doc: from, lead: FOLLOWUP_LEADS.refer }
      const related = relatedEntry(from, wanted)
      if (!related) return null
      const lead =
        wanted?.[0] === 'pattern' ? FOLLOWUP_LEADS.referPattern
        : wanted?.[0] === 'structure' ? FOLLOWUP_LEADS.referStructure
        : wanted?.[0] === 'example' ? FOLLOWUP_LEADS.referExample
        : wanted?.[0] === 'concept' ? FOLLOWUP_LEADS.referWhy
        : FOLLOWUP_LEADS.refer
      return { doc: related.doc, lead }
    }
    return null
  }

  const phraseBonus = (doc: Doc, normalizedQuery: string): number => {
    let bonus = 0
    const subject = doc.entry.subject ? normalizeQuestion(doc.entry.subject) : ''
    if (subject.length >= 2) {
      // 質問が主語を含む(全文一致) / 主語が質問を含む(「三単現」のような一語の質問)
      if (normalizedQuery.includes(subject)) {
        bonus += subject.includes(' ') || subject.length >= 8 ? 0.3 : subject.length >= 4 ? 0.18 : 0.08
      } else if (normalizedQuery.length >= 2 && subject.includes(normalizedQuery)) {
        bonus += normalizedQuery.length >= 6 ? 0.25 : 0.12
      }
    }
    if (doc.normalizedQuestions.some((question) => question.length >= 6 && normalizedQuery.includes(question))) {
      bonus += 0.15
    }
    // 質問文がそのまま一致する(「三単現」のような一語を含む)ときは強い証拠
    if (doc.normalizedQuestions.some((question) => question === normalizedQuery)) {
      bonus += 0.3
    }
    return Math.min(0.6, bonus)
  }

  const suggestions = (): string[] => {
    const out: string[] = []
    for (const intent of SUGGESTION_INTENTS) {
      // 同じ意図の中では、代表（優先度が高い）QAから1問だけ選ぶ
      const entry = entries
        .filter((candidate) => candidate.intent === intent && candidate.answer.quotes.length > 0)
        .sort((a, b) => b.priority - a.priority || (a.id < b.id ? -1 : 1))[0]
      if (!entry) continue
      // チップは押しやすさ優先。短すぎず長すぎない言い回しを選ぶ。
      const comfortable = entry.questions.filter((question) => question.length >= 6 && question.length <= 22)
      const pool =
        comfortable.length > 0
          ? comfortable
          : entry.questions.filter((question) => question.length >= 4 && question.length <= 30)
      const question = (pool.length > 0 ? pool : entry.questions).reduce((shortest, candidate) =>
        candidate.length < shortest.length ? candidate : shortest,
      )
      if (question.length <= 30 && !out.includes(question)) out.push(question)
      if (out.length >= 4) break
    }
    return out
  }

  const fallback = (): ChatReply => ({
    kind: 'fallback',
    message: `${pick(SMALL_TALK_LEADS.fallback)}\n${FALLBACK_NOTE}`,
    suggestions: suggestions(),
  })

  const reply = (question: string): ChatReply => {
    const normalized = normalizeQuestion(question)
    if (normalized.length === 0) return fallback()

    const followUp = resolveFollowUp(normalized, question)
    if (followUp) {
      lastDoc = followUp.doc
      return answerFrom(followUp.doc, followUp.lead)
    }

    // 文脈がないときの「もっと詳しく」「他には?」「もう一度」は、答える対象がない。
    // ただし「三単現をもう一度」のように用語・英文などの内容語が一緒にあるなら、
    // その話題についての質問として普通に答える。
    if (
      !lastDoc &&
      normalized.length <= FOLLOWUP_MAX_LENGTH &&
      (FOLLOWUP_PATTERNS.deepen.some((pattern) => normalized.includes(pattern)) ||
        FOLLOWUP_PATTERNS.related.some((pattern) => normalized.includes(pattern)) ||
        ['もう一度', 'もう一回', '言い換えて'].some((pattern) => normalized.includes(pattern)))
    ) {
      const contentTokens = tokenize(question).filter((token) => token.startsWith('term:') || token.startsWith('en:'))
      if (contentTokens.length === 0) return fallback()
    }

    // 内容語だけを使う。「明日の予定を教えて」のように未知語+よくある言い回しだけの質問に、
    // 全QAが共通で持つ「教えて」だけで一致してしまうのを防ぐ。
    // かなの別名が質問全体なら(「げんざいかんりょう」)、用語の辞書トークン1つに寄せる。
    const aliasTerm = Object.entries(TERM_SYNONYMS).find(([alias]) => normalized === alias)?.[1]
    const rawTokens = [...new Set(aliasTerm ? [`term:${aliasTerm}`] : tokenize(question))]
    const floor = rawTokens.length <= 3 ? SHORT_QUERY_FLOOR : IDF_FLOOR
    // 未知の日本語bigramが半分以上を占めるかたまりは、未知語の一部とみなす。
    // その隣のbigramも索引語にしない(「わくわくとは?」の「くと」のように、
    // たまたま本文に現れた断片で答えてしまうのを防ぐ)。
    const contaminated = new Set<string>()
    for (const match of normalized.matchAll(/[ぁ-んァ-ヶ一-龯ー]+/g)) {
      const run = match[0]
      let total = 0
      let unknown = 0
      for (let index = 0; index < run.length - 1; index += 1) {
        total += 1
        if ((df.get(`ja:${run.slice(index, index + 2)}`) ?? 0) === 0) unknown += 1
      }
      if (unknown < 2 || unknown * 2 < total) continue
      for (let index = 0; index < run.length - 1; index += 1) {
        if ((df.get(`ja:${run.slice(index, index + 2)}`) ?? 0) !== 0) continue
        if (index > 0) contaminated.add(`ja:${run.slice(index - 1, index + 1)}`)
        if (index + 2 < run.length) contaminated.add(`ja:${run.slice(index + 1, index + 3)}`)
      }
    }
    const weights = new Map<string, number>()
    let unknownWeight = 0
    for (const token of rawTokens) {
      if ((df.get(token) ?? 0) === 0) {
        unknownWeight += UNKNOWN_PENALTY
        continue
      }
      if (token.startsWith('ja:') && contaminated.has(token)) continue
      const weight = idf(token)
      if (weight < floor) continue
      weights.set(token, weight)
    }
    unknownWeight = Math.min(unknownWeight, UNKNOWN_PENALTY_MAX)
    if (weights.size === 0) return fallback()
    // かな・英語の別名(うけみ → 受動態)が当たったら、その語の未知扱いを解除する
    const synonymMatched =
      Object.keys(TERM_SYNONYMS).some((alias) => normalized.includes(alias)) ||
      Object.keys(EN_TERM_SYNONYMS).some((alias) => containsTerm(normalized, alias))
    if (synonymMatched) unknownWeight = Math.min(unknownWeight, 1)
    const knownWeight = [...weights.values()].reduce((sum, weight) => sum + weight, 0)
    // 未知語が内容語より重い質問は、コーパスの外の話なので答えない
    if (unknownWeight > knownWeight) return fallback()
    // 未知の英単語を含む質問は、既知の内容が十分に強いときだけ答える(translate this to French 対策)
    let unknownEnglish = 0
    for (const token of rawTokens) {
      if (token.startsWith('en:') && (df.get(token) ?? 0) === 0) unknownEnglish += 1
    }
    if (!synonymMatched && unknownEnglish > 0 && knownWeight < unknownWeight * 3) return fallback()
    // 未知の英単語があるときは、質問テンプレート(「translate "..."」など)の語だけで
    // 一致した候補を信じない。教材内容に現れる語での裏づけを要求する。
    if (!synonymMatched && unknownEnglish > 0) {
      // 教材内容(検索語・引用・主題)に裏づけられた語が2つ以上ないと、質問テンプレートの
      // 語だけで偶然一致した候補とみなす(「translate this to French」対策)。
      const families = new Set<string>()
      for (const [token, weight] of weights) {
        // 機能語(the / of / is など)は例文にも現れるだけで、話題の裏づけにはならない
        if (!contentTokens.has(token) || weight < 2) continue
        families.add(token.startsWith('en:') ? `en:${stemOf(token.slice(3))}` : token)
      }
      if (families.size < 2) return fallback()
      // 翻訳の依頼は、対象の文・語を名指ししているときだけ受ける
      // (「translate this to klingon」が this と to だけで通るのを防ぐ)
      if (/\btranslat(e|ion)\b/.test(normalized)) {
        const anchored = docs.some((doc) => {
          const subject = doc.entry.subject ?? ''
          if (subject.length >= 4 && containsTerm(normalized, subject)) return true
          return doc.normalizedQuestions.some((registered) => registered.length >= 6 && normalized.includes(registered))
        })
        if (!anchored) return fallback()
      }
    }
    // 「どきどき」「きらきら」のような繰り返し語は、このセクションに実在しなければ答えない
    for (const match of normalized.matchAll(/[ぁ-んァ-ヶ一-龯ー]+/g)) {
      const repeated = /^(..)(?:\1)+/.exec(match[0])
      if (repeated && !runsHaystack.includes(repeated[0])) return fallback()
    }
    // 未知の日本語の塊は、カリキュラム用語か登録済みの言い回しに裏づけられていない限り答えない
    if (contaminated.size > 0) {
      const hasCurriculumTerm = rawTokens.some(
        (token) => token.startsWith('term:') && CURRICULUM_TERMS.includes(token.slice(5)),
      )
      if (!hasCurriculumTerm) {
        const anchored = docs.some((doc) => {
          const subject = doc.entry.subject ?? ''
          if (subject.length >= 4 && containsTerm(normalized, subject)) return true
          return doc.normalizedQuestions.some((registered) => registered.length >= 5 && normalized.includes(registered))
        })
        if (!anchored) return fallback()
      }
    }
    const totalWeight = knownWeight + unknownWeight
    if (knownWeight / totalWeight < 0.6) return fallback()
    // 未知語が多い質問では、意図のショートカットを弱める(「ソクラテスとは?」に答えないため)
    const knownRatio = knownWeight / totalWeight

    const candidateIndexes = new Set<number>()
    for (const token of weights.keys()) {
      for (const index of postings.get(token) ?? []) candidateIndexes.add(index)
    }
    if (candidateIndexes.size === 0) return fallback()

    const intent = classifyIntent(question)
    // 質問中の英文語の重み(候補がこれを取りこぼしたら減点する)
    let enWeight = 0
    for (const [token, weight] of weights) if (token.startsWith('en:')) enWeight += weight
    // 質問が要求している用語(辞書トークン)。用語QAはこれを手がかりに優先する
    const termRequested = new Set(
      [...weights.keys()].filter((token) => token.startsWith('term:')).map((token) => token.slice(5)),
    )
    // 短い質問は直前の話題に寄せる(「例文は?」「なぜ?」の返答の返答)
    const contextTokens = lastDoc && weights.size <= 3 ? [...lastDoc.tokens].filter((token) => idf(token) >= 1) : []

    const scoreOf = (doc: Doc): number => {
      let matched = 0
      let matchedEn = 0
      for (const [token, weight] of weights) {
        if (!doc.tokens.has(token)) continue
        matched += weight
        if (token.startsWith('en:')) matchedEn += weight
      }
      const coverage = matched / totalWeight
      const intentScore = intent
        ? doc.entry.intent === intent.intent
          ? 1
          : INTENT_AFFINITY[intent.intent]?.includes(doc.entry.intent)
            ? 0.35
            : 0
        : 0
      const phrase = phraseBonus(doc, normalized)
      // 「ねえ、」などの前置きが付いても、登録済みの言い回しを丸ごと含むなら同じだけ強い
      // 入力がそのQAの言い回し候補と完全に一致するなら、検索語の一致より強い証拠
      const exactBonus = doc.normalizedQuestions.some((question) => question === normalized) ? 0.45 : 0
      // 「ねえ、」などの前置きが付いても、登録済みの言い回しを丸ごと含むなら同じだけ強い
      const anchoredByQuestion = doc.normalizedQuestions.some(
        (question) => question.length >= 5 && normalized.includes(question),
      )
      const anchorBonus = anchoredByQuestion && !exactBonus ? 0.35 : 0
      // 活用形QAは「その語の形」を聞かれている QA。語が含まれていれば強く優先する
      const formBonus =
        doc.entry.id.includes(':form:') &&
        doc.entry.subject &&
        normalized.includes(normalizeQuestion(doc.entry.subject))
          ? 0.22
          : 0
      // 用語QAは「その用語を聞かれている」QA。質問が要求する用語と一致したら強く優先する
      const termBonus =
        doc.entry.id.includes(':termqa:') && doc.entry.subject && termRequested.has(doc.entry.subject) ? 0.12 : 0
      // 「AとBの違い」のように複数の用語が要求されたときは、AもBも扱うQAを優先する
      let termCoverage = 0
      if (termRequested.size > 1) {
        const haystack = [doc.entry.subject ?? '', ...doc.entry.questions].map(normalizeQuestion).join(' ')
        let covered = 0
        for (const term of termRequested) if (includesJapaneseTerm(haystack, normalizeQuestion(term))) covered += 1
        termCoverage = covered / termRequested.size
      }
      // 比較QA(「AとBの違い」)は、主題そのものに要求された用語が入っている方を優先する。
      // ただし「一般動詞」と「動詞」のように部分重複する用語は、長い方だけ数える。
      let subjectTerms = 0
      if (doc.entry.intent === 'difference' && termRequested.size > 1 && doc.entry.subject) {
        const subject = normalizeQuestion(doc.entry.subject)
        const longest = [...termRequested].filter(
          (term) => ![...termRequested].some((other) => other !== term && other.length > term.length && other.includes(term)),
        )
        for (const term of longest) if (includesJapaneseTerm(subject, normalizeQuestion(term))) subjectTerms += 1
      }
      let context = 0
      if (contextTokens.length > 0) {
        let overlap = 0
        for (const token of contextTokens) if (doc.tokens.has(token)) overlap += 1
        context = CONTEXT_BONUS * (overlap / contextTokens.length)
      }
      return (
        0.55 * coverage +
        0.4 * intentScore * knownRatio +
        0.15 * phrase +
        exactBonus +
        anchorBonus +
        formBonus +
        termBonus +
        0.2 * termCoverage +
        Math.min(0.36, 0.12 * subjectTerms) +
        context +
        // 英文の語を取りこぼした候補は、例文の取り違えとみなして減点
        (enWeight > 0 ? -0.12 * (1 - matchedEn / enWeight) : 0) +
        0.02 * (doc.entry.priority / 10)
      )
    }

    const ranked = [...candidateIndexes]
      .map((index) => ({ doc: docs[index], score: scoreOf(docs[index]) }))
      .sort(
        (a, b) =>
          b.score - a.score ||
          b.doc.entry.priority - a.doc.entry.priority ||
          (a.doc.entry.id < b.doc.entry.id ? -1 : 1),
      )

    let best = ranked[0]
    // 意図が明確で、その意図に十分よい候補があれば、その意図の中だけで答える(誤爆防止)。
    // ただし全体1位が「登録済みの言い回しそのもの」なら、その完全一致を最優先する。
    // また全体1位との差が大きい候補でしかないなら、その意図の解釈は弱いとみなして上書きしない。
    const bestIsExact = best.doc.normalizedQuestions.some((question) => question === normalized)
    const bestIsAnchored =
      bestIsExact || best.doc.normalizedQuestions.some((question) => question.length >= 5 && normalized.includes(question))
    if (intent && !bestIsAnchored) {
      const sameIntent = ranked.filter((candidate) => candidate.doc.entry.intent === intent.intent)
      // 質問で最も特徴的な語を無視した候補に、意図だけを理由に答えさせない
      // ("He plays tennis." の意味を、別の例文の意味QAに答えさせない)。
      // テンプレート由来の語(use など)は焦点とみなさず、教材内容に裏づけられた語を使う。
      let topToken = ''
      let topWeight = 0
      let fallbackToken = ''
      let fallbackWeight = 0
      for (const [token, weight] of weights) {
        if (weight > fallbackWeight) {
          fallbackToken = token
          fallbackWeight = weight
        }
        if (contentTokens.has(token) && weight > topWeight) {
          topToken = token
          topWeight = weight
        }
      }
      if (!topToken) topToken = fallbackToken
      const leaderCoversTop = sameIntent.length > 0 && sameIntent[0].doc.tokens.has(topToken)
      // 全体1位が特徴語を捉えていて、意図の候補が捉えていないときだけ、
      // 「別の候補の方が質問の焦点に合う」とみなしてロックを見送る。
      const bestCoversTop = best.doc.tokens.has(topToken)
      if (
        (leaderCoversTop || !bestCoversTop) &&
        sameIntent.length > 0 &&
        sameIntent[0].score >= INTENT_LOCK_MIN &&
        sameIntent[0].score >= best.score - INTENT_LOCK_MARGIN
      ) {
        best = sameIntent[0]
      }
    }

    if (!best || best.score < ANSWER_MIN) return fallback()
    // あいさつ・機能説明は「直前の話題」にしない(次に「もっと詳しく」と来ても困らない)
    if (best.doc.entry.intent !== 'greeting' && best.doc.entry.intent !== 'capability') lastDoc = best.doc
    return answerFrom(best.doc, undefined, Math.min(1, best.score))
  }

  return { reply, suggestions, reset: () => (lastDoc = null), size: entries.length }
}
