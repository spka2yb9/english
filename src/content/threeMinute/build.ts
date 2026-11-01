import { findUnit } from '../grammar/index.ts'
import { LESSON_ANIMATIONS } from '../grammar/animations.ts'
import type { GrammarLesson, LessonBlock, QuizQuestion } from '../types'
import type { ThreeMinuteLine, ThreeMinuteMood, ThreeMinutePart, ThreeMinuteSection, ThreeMinuteSpeaker } from './types'

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

function firstBold(text: string): string | undefined {
  const match = text.match(/\*\*(.+?)\*\*/)
  return match?.[1]?.trim()
}

/** 生徒の相づち。本文のキーワードがあれば、それを復唱して会話に戻す。 */
function studentReaction(text: string, seed: number): string {
  const key = firstBold(text)
  if (key && key.length <= 28) {
    return pick(
      [
        `つまり、**${key}** がポイントなんだね!`,
        `「${key}」を意識してみるね!`,
        `${key}…! ちゃんと覚えるね!`,
        `なるほど、**${key}** なんだね!`,
      ],
      seed,
    )
  }
  return pick(
    [
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
    ],
    seed,
  )
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

const TABLE_TIPS = [
  '行を横に見ると、違いがひと目でわかるよ。',
  '表は、となりどうしを比べるとわかりやすいよ。',
  '気になるところを、指で追いながら見てみて。',
]

const EXAMPLE_TIPS = [
  '音声を聞いて、ゆっくり声に出してみてね。形が耳と口に残るよ。',
  '英文を指でなぞって、語順をたしかめてみよう。',
  '音声のあとを追いかけるように、声に出してみてね。',
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

  const say = (
    speaker: ThreeMinuteSpeaker,
    text: string,
    mood: ThreeMinuteMood = 'happy',
    extra?: Pick<ThreeMinuteLine, 'en' | 'ja' | 'highlight'>,
  ) => {
    parts.push({ kind: 'line', line: { speaker, text, mood, ...extra } })
  }

  const addAnimation = () => {
    const animation = LESSON_ANIMATIONS[lesson.id]
    if (!animation) return false
    say(INGBIRD, 'ここで、うごく図を見てみよう! 3つの場面を順番に見るよ。', 'cheer')
    say(HIYOKO, 'わーい! 再生ボタン、おしちゃお♪', 'cheer')
    parts.push({ kind: 'animation', animation })
    say(HIYOKO, 'うごくと、頭の中がすっきりするね!', 'happy')
    say(INGBIRD, 'でしょ? もう一度見たいときは、下のステップを押してね。', 'happy')
    return true
  }

  say(INGBIRD, 'やっほー、ヒヨコ君! 今日もいっしょに英語のひみつをのぞいてみよう♪', 'cheer')
  say(HIYOKO, 'ちゅん! 今日はなにを教えてくれるの? わくわく!', 'curious')
  say(INGBIRD, `今日のテーマは「${lesson.title}」だよ。`, 'happy')
  say(INGBIRD, `今日はね、${lesson.objective}`, 'happy')
  say(HIYOKO, 'ふむふむ…ちょっと大きい目標だけど、ぼく、がんばるよ!', 'cheer')

  let animationAdded = false

  for (const block of lesson.blocks) {
    seed += 1

    switch (block.type) {
      case 'explanation': {
        if (block.title) {
          say(INGBIRD, `まずは「${block.title}」から見てみよう。`, 'happy')
        }
        const chunks = splitExplanation(block.body)
        chunks.forEach((chunk, index) => {
          say(INGBIRD, chunk, index % 2 === 0 ? 'happy' : 'think')
          say(HIYOKO, studentReaction(chunk, seed + index), index % 3 === 0 ? 'curious' : 'happy')
        })
        if (!animationAdded) animationAdded = addAnimation()
        break
      }

      case 'examples': {
        const exampleTitle = block.title && block.title !== '例文' ? `「${block.title}」` : ''
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
          first?.highlight ? `「${first.highlight}」が今日の主役なんだね!` : '音声も聞けるんだね! 聞いてみよう♪',
          'curious',
        )
        say(INGBIRD, first?.note ?? pick(EXAMPLE_TIPS, seed), 'happy')
        break
      }

      case 'table': {
        say(
          INGBIRD,
          block.title ? `「${block.title}」を表にまとめたよ。` : '表にまとめると、こんなふうになるよ。',
          'happy',
        )
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        const row = block.rows[0]
        say(
          HIYOKO,
          row && row.length >= 2 ? `「${row[0]}」は「${row[1]}」なんだね!` : '表を見ると、違いがひと目でわかるね!',
          'curious',
        )
        say(INGBIRD, pick(TABLE_TIPS, seed), 'happy')
        break
      }

      case 'contrast': {
        say(INGBIRD, `似ているけれど違う2つを、くらべてみよう。${block.title ? `「${block.title}」` : ''}`, 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, 'えっ、どこが違うの? 見た目はそっくりだよ〜。', 'wow')
        say(
          INGBIRD,
          block.note ?? `左は「${block.left.label}」、右は「${block.right.label}」。例文の形を見比べてごらん。`,
          'happy',
        )
        break
      }

      case 'structure': {
        say(INGBIRD, '文の組み立てを、ならべて見てみよう。', 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, 'わっ、ブロックみたい! ならべると形が見えるね!', 'wow')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        break
      }

      case 'breakdown': {
        say(INGBIRD, '長い文も、役割ごとに分ければこわくないよ。', 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, 'S、V、O、C…ってラベルがついてる!', 'curious')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        if (block.skeleton) say(INGBIRD, `修飾語を外すと、骨格は「${block.skeleton}」だけになるよ。`, 'proud')
        break
      }

      case 'expansion': {
        say(INGBIRD, '短い文が、どうやって長くなるのかな?', 'curious')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, '文がどんどん長くなっても、骨格は変わらないんだね!', 'wow')
        if (block.caption) say(INGBIRD, block.caption, 'happy')
        break
      }

      case 'timeline': {
        say(INGBIRD, '時間の流れを、線で見てみよう。', 'happy')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, '「今」の位置がわかると、時制も見やすいね!', 'curious')
        const caption = block.timelines.map((timeline) => timeline.caption).find(Boolean)
        if (caption) say(INGBIRD, caption, 'happy')
        break
      }

      case 'illustration': {
        say(INGBIRD, '絵でイメージをつかもう!', 'cheer')
        parts.push({ kind: 'block', block, label: BLOCK_LABELS[block.type] })
        say(HIYOKO, 'わぁ、絵で見るとイメージしやすいね!', 'wow')
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
    say(HIYOKO, studentReaction(point, seed + 100 + index), index % 2 === 0 ? 'curious' : 'happy')
  })
  say(HIYOKO, 'ちゅん! 今日もいっぱい覚えたよ! ありがとう、イングバード先生!', 'cheer')
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
    quiz: pickQuizQuestions(lesson.quiz),
  }
}
