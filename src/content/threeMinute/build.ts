import { findUnit } from '../grammar/index.ts'
import { LESSON_ANIMATIONS } from '../grammar/animations.ts'
import type { GrammarLesson, LessonBlock, QuizQuestion } from '../types'
import { COMEDY_BEATS } from './comedy.ts'
import { collectTerms } from './glossary.ts'
import type { ThreeMinuteLine, ThreeMinuteMood, ThreeMinutePart, ThreeMinuteSection, ThreeMinuteSpeaker, ThreeMinuteTerm } from './types'

const INGBIRD: ThreeMinuteSpeaker = 'ingbird'
const HIYOKO: ThreeMinuteSpeaker = 'hiyoko'

function hash(text: string): number {
  let value = 0
  for (let index = 0; index < text.length; index += 1) {
    value = (value * 31 + text.charCodeAt(index)) | 0
  }
  return Math.abs(value)
}

function pick<T>(items: readonly T[], seed: number): T {
  return items[seed % items.length]
}

function shorten(text: string, max = 42): string {
  return text.length > max ? `${text.slice(0, max - 1)}…` : text
}

/** 英文を語の途中で切らずに短くする。 */
function shortHighlight(text: string, max = 30): string {
  if (text.length <= max) return text
  const words = text.split(/\s+/)
  let result = ''
  for (const word of words) {
    const next = result ? `${result} ${word}` : word
    if (next.length > max) break
    result = next
  }
  return result ? `${result}…` : `${text.slice(0, max - 1)}…`
}

/** 本文の見出しを、会話の流れに合う言い方へ直す。 */
function normalizeSpokenText(text: string): string {
  return text
    .replace(/\*\*日本語ではこう考える。\*\*\s*/g, 'ここで、日本語との違いを見ておこう。')
    .replace(/\*\*日本語ではこう考える[：:]\*\*\s*/g, 'ここで、日本語との違いを見ておこう。')
    .trim()
}

/** 見出しの入れ子引用符を『』に変え、吹き出しの中で読みやすくする。 */
function quoteTitle(title: string): string {
  return title.replace(/「/g, '『').replace(/」/g, '』')
}

const REACTION_KEYS_TO_SKIP = new Set([
  'S',
  'V',
  'O',
  'C',
  'M',
  'in',
  'on',
  'at',
  'to',
  'so',
  'not',
  'it',
  'I',
  'You',
  'We',
  'They',
  'He',
  'She',
])

/** 強調された語のうち、生徒が復唱しても意味のあるものだけを取り出す。 */
function keyPhrase(text: string): string | undefined {
  const matches = [...text.matchAll(/\*\*(.+?)\*\*/g)]
  for (const match of matches) {
    const key = match[1]?.trim()
    if (!key) continue
    if (key.length > 20) continue
    // 「日本語ではこう考える。」のような、本文の見出しを復唱しない。
    if (/[。！？]$/.test(key)) continue
    if (/日本語ではこう考える|文型の視点/.test(key)) continue
    if (REACTION_KEYS_TO_SKIP.has(key)) continue
    if (/^[A-Za-z]$/.test(key)) continue
    return key
  }
  return undefined
}

const KEY_REACTIONS = [
  (key: string) => `つまり、**${key}** がポイントなんだね!`,
  (key: string) => `「${key}」を意識してみるね!`,
  (key: string) => `${key}…! ちゃんと覚えるね!`,
  (key: string) => `なるほど、**${key}** なんだね!`,
  (key: string) => `「${key}」、メモメモ…。`,
]

const PLAIN_REACTIONS = [
  'ふむふむ、なるほど〜!',
  'ちゅん! メモメモ…。',
  'えっ、そうなんだ!',
  'わかった気がする!',
  'むむむ…ちょっと考えちゃうな。',
  'へえ〜、おもしろい!',
  'そういうことかぁ!',
  'ぼく、だんだん見えてきたよ!',
  'ちゅん! なるほどね!',
  'えへへ、ちょっとわかってきた!',
  'ふむふむ、先生の話、おもしろい!',
  'ぼくのノート、いっぱいになったよ!',
  'むむ、ここは大事そうだね!',
  'そうなんだ! 知らなかった!',
]

function previousStudentLine(parts: ThreeMinutePart[]): string {
  for (let index = parts.length - 1; index >= 0; index -= 1) {
    const part = parts[index]
    if (part.kind === 'line' && part.line.speaker === HIYOKO) return part.line.text
  }
  return ''
}

/** 生徒の相づち。本文のキーワードがあれば復唱し、なければ短い反応を返す。 */
function studentReaction(text: string, seed: number, previous = ''): string {
  const key = keyPhrase(text)
  if (key) {
    for (let offset = 0; offset < KEY_REACTIONS.length; offset += 1) {
      const candidate = KEY_REACTIONS[(seed + offset) % KEY_REACTIONS.length](key)
      if (candidate !== previous) return candidate
    }
  }
  for (let offset = 0; offset < PLAIN_REACTIONS.length; offset += 1) {
    const candidate = PLAIN_REACTIONS[(seed + offset) % PLAIN_REACTIONS.length]
    if (candidate !== previous) return candidate
  }
  return PLAIN_REACTIONS[0]
}

/** 解説本文を、吹き出し1つぶんの長さに区切る。箇条書きは1つのまとまりとして残す。 */
function splitExplanation(body: string): string[] {
  const paragraphs = body
    .split(/\n\n+/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean)
  const chunks: string[] = []

  for (const paragraph of paragraphs) {
    const lines = paragraph.split('\n')
    if (lines.length > 1 && lines.every((line) => line.trim().startsWith('- '))) {
      chunks.push(paragraph)
      continue
    }

    const sentences = lines.flatMap((line) => line.match(/[^。！？]+[。！？]?/g) ?? [line])
    let buffer = ''
    for (const sentence of sentences) {
      const piece = sentence.trim()
      if (!piece) continue
      if (buffer && buffer.length + piece.length > 170) {
        chunks.push(buffer)
        buffer = piece
      } else {
        buffer += piece
      }
    }
    if (buffer) chunks.push(buffer)
  }

  return chunks
}

const ANIMATION_INTROS = [
  'ここで、うごく図を見てみよう! 3つの場面を順番に見るよ。',
  'お待ちかね、アニメの時間! 3コマで動きを追いかけるよ。',
  '図が動くと、文法の動きが見えるよ。3つの場面を見てみよう。',
  'ここで3段階のアニメ! 順番に動かして確かめよう。',
]

const ANIMATION_REACTIONS = [
  'わーい! 再生ボタン、おしちゃお♪',
  'ちゅん! 動く図、だいすき!',
  'やった、アニメだ! 3つとも見る!',
  '再生ボタン、ぽちっとな♪',
]

const ANIMATION_AFTER = [
  'うごくと、頭の中がすっきりするね!',
  '動くと、どの部分が変わるのか見やすいね!',
  '3つ並べると、文法の流れがつかめるね!',
  'ちゅん! 目で追うと、忘れにくいね!',
]

const EXAMPLE_TIPS = [
  '音声を聞いて、ゆっくり声に出してみてね。形が耳と口に残るよ。',
  '英文を指でなぞって、語順をたしかめてみよう。',
  '音声のあとを追いかけるように、声に出してみてね。',
]

const TABLE_TIPS = [
  '行を横に見ると、違いがひと目でわかるよ。',
  '表は、となりどうしを比べるとわかりやすいよ。',
  '気になるところを、指で追いながら見てみて。',
]


const BLOCK_LABELS: Record<LessonBlock['type'], string> = {
  explanation: '先生の説明',
  examples: '例文でチェック',
  table: '表でチェック',
  contrast: 'くらべてみよう',
  structure: '文の組み立て',
  breakdown: '文の解剖図',
  expansion: '文が育つようす',
  timeline: '時間の流れ',
  illustration: 'イメージでわかる',
}

function estimateMinutes(parts: ThreeMinutePart[]): number {
  let spokenChars = 0
  let visualBlocks = 0
  for (const part of parts) {
    if (part.kind === 'line') {
      spokenChars += part.line.text.length + (part.line.en?.length ?? 0)
    } else if (part.kind === 'block') {
      visualBlocks += 1
    }
  }
  // 会話は1分あたり約850字。図表は読むというより見るので、1ブロック0.12分として足す。
  return Math.max(3, Math.round(spokenChars / 850 + visualBlocks * 0.12))
}

function fillBlank(sentence: string, choice: string): string {
  return sentence
    .replace(/_{2,}/, choice)
    .replace(/\s+([.,!?;:])/g, '$1')
    .replace(/\s{2,}/g, ' ')
    .trim()
}

function isEnglishSentence(text: string): boolean {
  return /[A-Za-z]/.test(text) && text.trim().split(/\s+/).length >= 2
}

export type Mistake = {
  wrong: string
  right: string
  note: string
  prompt: string
  sentenceJa?: string
}

/** 空所のない問題でも、文そのものを選ぶ問題なら「つまずき例」に使える。 */
const SENTENCE_CHOICE_PROMPT =
  /正しい文|正しい否定文|正しい疑問文|どちらの文が正しい|自然な文|自然な英文|最も自然な文|正しい語順の文|1文にした正しい文|状況に合う文|会話の流れに合う文|書き換えたものとして正しい|倒置形に書き換えた/

/**
 * クイズの誤答選択肢を、ヒヨコ君の「つまずき」として会話に使う。
 * 誤りを選ぶ問題は、正解が誤文なので使わない(誤答選択肢が正しい文になってしまう)。
 */
export function buildMistake(lesson: GrammarLesson): Mistake | undefined {
  const candidates = lesson.quiz
    .map((question, index) => ({ question, index }))
    .filter(({ question }) => !/誤り|間違い|不自然/.test(question.prompt))
  const preferred = candidates.filter(({ index }) => index >= 4)
  const ordered = [...preferred, ...candidates]

  for (const { question } of ordered) {
    const wrongIndex = question.choices.findIndex(
      (_, index) => index !== question.correctIndex && question.choiceNotes?.[index],
    )
    if (wrongIndex < 0) continue

    const wrongChoice = question.choices[wrongIndex]
    const rightChoice = question.choices[question.correctIndex]
    let wrong = ''
    let right = ''

    if (question.sentence?.includes('___')) {
      wrong = fillBlank(question.sentence, wrongChoice)
      right = question.audioEn ?? fillBlank(question.sentence, rightChoice)
    } else if (
      SENTENCE_CHOICE_PROMPT.test(question.prompt) &&
      isEnglishSentence(wrongChoice) &&
      isEnglishSentence(rightChoice)
    ) {
      wrong = wrongChoice
      right = question.audioEn ?? rightChoice
    } else {
      // 句動詞を選ぶ問題のように、選択肢が文でない問題は会話の「つまずき例」にしない。
      continue
    }

    const note = (question.choiceNotes?.[wrongIndex] ?? question.explanation).trim()
    return {
      wrong,
      right,
      note: /[。.!?]$/.test(note) ? note : `${note}。`,
      prompt: question.prompt,
      sentenceJa: question.sentenceJa,
    }
  }

  return undefined
}

/** 10問のセクションでは、範囲が偏らないように4問を選ぶ。 */
function pickQuizQuestions(quiz: QuizQuestion[]): QuizQuestion[] {
  if (quiz.length <= 4) return quiz
  const last = quiz.length - 1
  const indices = [0, Math.floor(last / 3), Math.floor((last * 2) / 3), last]
  return [...new Set(indices)].map((index) => quiz[index])
}

function textValues(value: unknown): string[] {
  if (typeof value === 'string') return [value]
  if (Array.isArray(value)) return value.flatMap(textValues)
  if (value && typeof value === 'object') return Object.values(value).flatMap(textValues)
  return []
}

function lessonTexts(lesson: GrammarLesson): string[] {
  return textValues({
    title: lesson.title,
    objective: lesson.objective,
    blocks: lesson.blocks,
    summary: lesson.summary,
  })
}

function partTexts(parts: ThreeMinutePart[]): string[] {
  return parts.flatMap((part) => {
    if (part.kind === 'line') return [part.line.text]
    if (part.kind === 'block') return textValues(part.block)
    return [part.animation.title, ...part.animation.steps.map((step) => step.note)]
  })
}

// どの話にも出る基本語は、用語メモを埋め尽くさないように後回しにする。
// タイトルの用語は基本語でも必ず残す。
const BASIC_TERMS = new Set(['主語', '動詞', '名詞', '形容詞', '副詞', '単数', '複数', '時制'])

function collectSectionTerms(lesson: GrammarLesson, parts: ThreeMinutePart[]): ThreeMinuteTerm[] {
  // タイトルの用語 → 文型メモの用語 → 本文の用語の順に優先する。
  // 文型メモは専門用語が集中するので、ここを外すと用語メモの役に立たない。
  const titleTerms = collectTerms([lesson.title], 3)
  const focus = lesson.blocks.find((block) => block.type === 'explanation' && block.title === '文型の視点')
  const focusTerms =
    focus && focus.type === 'explanation'
      ? collectTerms([focus.body], 8).filter((entry) => !BASIC_TERMS.has(entry.term))
      : []
  const bodyTerms = collectTerms([...lessonTexts(lesson), ...partTexts(parts)], 12).filter(
    (entry) => !BASIC_TERMS.has(entry.term),
  )
  const merged: ThreeMinuteTerm[] = []
  for (const entry of [...titleTerms, ...focusTerms, ...bodyTerms]) {
    if (merged.some((term) => term.term === entry.term)) continue
    merged.push({ term: entry.term, plain: entry.plain })
    if (merged.length >= 12) break
  }
  return merged
}

/**
 * 英文法の1セクションを、イングバード先生とヒヨコ君の会話へ組み替える。
 *
 * 元の教材ブロックはすべて順番に登場させ、説明文・例文・表・図・まとめの情報量を落とさない。
 * 会話の合間には、文法ページと同じ3段階アニメーションを1回だけ差し込む。
 */
export function buildThreeMinuteSection(lesson: GrammarLesson): ThreeMinuteSection {
  const unit = findUnit(lesson.unitId)
  const parts: ThreeMinutePart[] = []
  let seed = hash(lesson.id)
  let flavor = hash(`${lesson.id}:flavor`)

  const say = (
    speaker: ThreeMinuteSpeaker,
    text: string,
    mood: ThreeMinuteMood = 'happy',
    extra?: Pick<ThreeMinuteLine, 'en' | 'ja' | 'highlight'>,
  ) => {
    parts.push({ kind: 'line', line: { speaker, text, mood, ...extra } })
  }

  const react = (mood: ThreeMinuteMood = 'happy') => {
    const last = parts.at(-1)
    const teacherText = last && last.kind === 'line' ? last.line.text : ''
    const text = studentReaction(teacherText, seed, previousStudentLine(parts))
    seed += 1
    say(HIYOKO, text, mood)
  }

  const addAnimation = () => {
    const animation = LESSON_ANIMATIONS[lesson.id]
    if (!animation) return false
    say(INGBIRD, pick(ANIMATION_INTROS, flavor), 'cheer')
    flavor += 1
    say(HIYOKO, pick(ANIMATION_REACTIONS, flavor), 'cheer')
    flavor += 1
    parts.push({ kind: 'animation', animation })
    say(HIYOKO, pick(ANIMATION_AFTER, flavor), 'happy')
    flavor += 1
    say(INGBIRD, 'でしょ? もう一度見たいときは、下のステップを押してね。', 'happy')
    return true
  }

  say(INGBIRD, 'やっほー、ヒヨコ君! 今日もいっしょに英語のひみつをのぞいてみよう♪', 'cheer')
  say(HIYOKO, 'ちゅん! 今日はなにを教えてくれるの? わくわく!', 'curious')
  say(INGBIRD, `今日のテーマは「${lesson.title}」だよ。`, 'happy')
  say(INGBIRD, `今日はね、${lesson.objective}`, 'happy')
  say(HIYOKO, pick([
    'ふむふむ…ちょっと大きい目標だけど、ぼく、がんばるよ!',
    'ちゅん! 今日の目標、しっかり覚えたよ!',
    'なるほど…つまり、今日も一個賢くなれるってことだね!',
    'ふむふむ、ゴールは見えた! 出発進行!',
  ], flavor), 'cheer')
  flavor += 1

  // 最初に、その話の中心用語に対する「見当違い」を1つ入れる。
  // 先生のツッコミで正しいルールを先に示してから、本文の詳しい説明へ進む。
  const comedy = COMEDY_BEATS[lesson.id]
  if (comedy) {
    say(HIYOKO, comedy.student, comedy.studentMood ?? 'curious')
    say(INGBIRD, comedy.teacher, comedy.teacherMood ?? 'proud')
  }

  let animationAdded = false

  for (const block of lesson.blocks) {
    seed += 1
    flavor += 1

    switch (block.type) {
      case 'explanation': {
        // 「文型の視点」はS/V/O/C/Mの専門的な補足。会話で読み上げず、
        // 5文型の地図を思い出す短い前置きのあと、ホワイトボードの「文型メモ」として見せる。
        if (block.title === '文型の視点') {
          say(INGBIRD, 'ここで、5文型の地図を思い出してみよう。今日の文は、動詞(V)のあとに何が続くかで型が決まるよ。', 'happy')
          say(HIYOKO, 'S・V・O・C・M…また出てきた! 5文型の地図、まだ頭にあるかな…。', 'think')
          say(
            INGBIRD,
            '大丈夫。むずかしく見えたら、まずは「動詞のあとに目的語(O)がある? 補語(C)がある?」だけ見ればいい。細かい言葉は下の用語メモにまとめておくね。',
            'proud',
          )
          // 白板の見出しは「文型メモ」に統一する。教材側の「文型の視点」は内部名なので出さない。
          parts.push({ kind: 'block', block: { ...block, title: undefined }, label: '文型メモ' })
          say(INGBIRD, '今の説明で、今日の文の骨格はつかめたかな? むずかしかったら、いったん読み飛ばしてOK。例文でまた確かめよう。', 'happy')
          say(HIYOKO, 'うん! まずは動詞のあとを見るんだね!', 'cheer')
          break
        }

        if (block.title) {
          say(INGBIRD, `まずは「${quoteTitle(block.title)}」の話から見てみよう。`, 'happy')
        }
        const chunks = splitExplanation(block.body)
        chunks.forEach((chunk, index) => {
          say(INGBIRD, normalizeSpokenText(chunk), index % 2 === 0 ? 'happy' : 'think')
          react(index % 3 === 0 ? 'curious' : 'happy')
        })
        if (!animationAdded) animationAdded = addAnimation()
        break
      }

      case 'examples': {
        const exampleTitle = block.title && block.title !== '例文' ? `「${quoteTitle(block.title)}」` : ''
        say(INGBIRD, `例文でたしかめよう!${exampleTitle}`, 'cheer')
        const first = block.items[0]
        if (first) {
          say(INGBIRD, 'たとえば、こんなふうに言うよ。', 'happy', {
            en: first.en,
            ja: first.ja,
            highlight: first.highlight,
          })
        }
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(
          HIYOKO,
          first?.highlight ? `「${shortHighlight(first.highlight)}」が今日の主役なんだね!` : '音声も聞けるんだね! 聞いてみよう♪',
          'curious',
        )
        say(INGBIRD, first?.note ?? pick(EXAMPLE_TIPS, seed), 'happy')
        break
      }

      case 'table': {
        say(
          INGBIRD,
          block.title ? `「${quoteTitle(block.title)}」を表にまとめたよ。` : '表にまとめると、こんなふうになるよ。',
          'happy',
        )
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        const row = block.rows[0]
        let reaction = '表を見ると、違いがひと目でわかるね!'
        if (row && row.length === 2) {
          reaction = `「${shorten(row[0], 24)}」は「${shorten(row[1], 40)}」なんだね!`
        } else if (row && row.length >= 3 && block.headers.length >= 2) {
          reaction = `「${shorten(block.headers[0], 12)}」が「${shorten(row[0], 20)}」のとき、「${shorten(block.headers[1], 12)}」は「${shorten(row[1], 40)}」なんだね!`
        }
        say(HIYOKO, reaction, 'curious')
        say(INGBIRD, pick(TABLE_TIPS, seed), 'happy')
        break
      }

      case 'contrast': {
        say(INGBIRD, `似ているけれど違う2つを、くらべてみよう。${block.title ? `「${quoteTitle(block.title)}」` : ''}`, 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, `「${block.left.label}」と「${block.right.label}」、どこが違うの?`, 'wow')
        say(
          INGBIRD,
          block.note ?? `左は「${block.left.label}」、右は「${block.right.label}」。例文の形を見比べてごらん。`,
          'happy',
        )
        break
      }

      case 'structure': {
        say(
          INGBIRD,
          block.title ? `「${quoteTitle(block.title)}」を、ならべて見てみよう。` : '文の組み立てを、ならべて見てみよう。',
          'happy',
        )
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, block.title ? `「${quoteTitle(block.title)}」、ブロックで見るとわかりやすいね!` : 'わっ、ブロックみたい! ならべると形が見えるね!', 'wow')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        break
      }

      case 'breakdown': {
        say(
          INGBIRD,
          block.title ? `「${quoteTitle(block.title)}」を、S・V・O・C の席で見てみよう。` : '長い文も、役割ごとに分ければこわくないよ。',
          'happy',
        )
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, block.title ? `「${quoteTitle(block.title)}」! ラベルがついてる!` : 'S、V、O、C…ってラベルがついてる!', 'curious')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        if (block.skeleton) say(INGBIRD, `修飾語を外すと、骨格は「${block.skeleton}」だけになるよ。`, 'proud')
        break
      }

      case 'expansion': {
        say(INGBIRD, block.title ? `「${quoteTitle(block.title)}」で、文が育つようすを見てみよう。` : '短い文が、どうやって長くなるのかな?', 'curious')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, '文がどんどん長くなっても、骨格は変わらないんだね!', 'wow')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        break
      }

      case 'timeline': {
        say(INGBIRD, block.title ? `「${quoteTitle(block.title)}」を、時間の線で見てみよう。` : '時間の流れを、線で見てみよう。', 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, '「今」の位置がわかると、時制も見やすいね!', 'curious')
        const caption = block.timelines.map((timeline) => timeline.caption).find(Boolean)
        if (caption) say(INGBIRD, caption, 'happy')
        break
      }

      case 'illustration': {
        // 挿絵ブロックは「うごいてわかる」と同じ3段階アニメーションを描く。
        // 3分間ページでは同じ図を二重に見せず、アニメーション1回にまとめる。
        // 挿絵のキャプションだけは、図の補足として会話に残す。
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        break
      }
    }
  }

  if (!animationAdded) addAnimation()

  const mistake = buildMistake(lesson)
  if (mistake) {
    say(
      INGBIRD,
      mistake.sentenceJa
        ? `${mistake.sentenceJa} この場面なら、どう言う?`
        : 'ここで、ヒヨコ君にちょっとチャレンジ! この文、どう言う?',
      'cheer',
    )
    say(HIYOKO, 'えっとね…ぼくなら、こう言うかな?', 'think', { en: mistake.wrong })
    say(INGBIRD, `おしい! でもね、${mistake.note}`, 'happy')
    say(INGBIRD, 'この場面では、こう言うよ。', 'proud', { en: mistake.right })
    say(HIYOKO, 'ちゅん…! もう一回言ってみるね。', 'cheer', { en: mistake.right })
    say(INGBIRD, 'せいかーい! とってもいい声だよ♪', 'cheer')
  }

  say(INGBIRD, '今日のポイントを、いっしょに振り返ろう!', 'cheer')
  lesson.summary.forEach((point, index) => {
    say(INGBIRD, point, 'happy')
    say(HIYOKO, studentReaction(point, seed + 100 + index, previousStudentLine(parts)), index % 2 === 0 ? 'curious' : 'happy')
  })
  say(HIYOKO, pick([
    'ちゅん! 今日もいっぱい覚えたよ! ありがとう、イングバード先生!',
    'ちゅん! 今日の話、ぼくのノートに全部書いたよ!',
    'ありがとう、先生! なんか、前より英語が見える気がする!',
    '今日も勉強できた! えへへ、ちょっと自信ついちゃった!',
  ], flavor), 'cheer')
  flavor += 1
  say(INGBIRD, 'えらいえらい! それじゃあ、最後に4問だけ挑戦してみよう。落ち着いてやれば大丈夫だよ♪', 'proud')

  return {
    lessonId: lesson.id,
    title: lesson.title,
    level: lesson.level,
    unitId: lesson.unitId,
    unitTitle: unit?.title ?? '',
    objective: lesson.objective,
    minutes: estimateMinutes(parts),
    parts,
    terms: collectSectionTerms(lesson, parts),
    quiz: pickQuizQuestions(lesson.quiz),
  }
}
