// ホームのイングバードが話すひとことを選ぶ。
// 励まし(状況に合わせて組み立てる)・学習のコツ・英会話フレーズの3つを、
// 順番を混ぜながら、一巡するまで同じセリフを出さないように選ぶ。

import {
  ENCOURAGE_BODIES,
  ENCOURAGE_CLOSINGS,
  ENCOURAGE_LINES,
  TIME_GREETINGS,
  type EncourageBranch,
} from '../content/ingbird/encouragement'
import { PHRASES, TIP_LINES } from '../content/ingbird/talk'
import type { TalkKind, TalkLine } from '../content/ingbird/types'
import { describeGap, type IngbirdMood, type StudyStatus } from './studyDays'

/** 種類ごとの気分。その場面に合う表情だけを使う。 */
const MOODS: Record<TalkKind, readonly IngbirdMood[]> = {
  encourage: ['happy', 'cheer', 'proud', 'wave', 'shy', 'sing'],
  tip: ['think', 'curious', 'proud', 'happy'],
  phrase: ['sing', 'happy', 'cheer', 'proud', 'wow'],
}

/**
 * 種類の出現比率。励まし4 : フレーズ4 : コツ2。
 * 1回目のタップだけは必ず励ましにして、最初の体験を「自分に向けた言葉」にする。
 * 抽選は「直前と同じ種類を引かない」重み付きで行う(連続を避けつつ、山札の端で崩れない)。
 */
const CATEGORY_POOL: readonly TalkKind[] = [
  'encourage',
  'encourage',
  'encourage',
  'encourage',
  'phrase',
  'phrase',
  'phrase',
  'phrase',
  'tip',
  'tip',
]

/** 励ましの中での作り方の比率。単体のセリフ3 : 組み立て4 : 時間帯のあいさつ1。 */
const ENCOURAGE_SOURCES: readonly ('line' | 'composed' | 'greeting')[] = [
  'line',
  'line',
  'line',
  'composed',
  'composed',
  'composed',
  'composed',
  'greeting',
]

export type TalkState = {
  lastKind: TalkKind | null
  /** プールごとの、まだ出していない番号。 */
  bags: Record<string, number[]>
  /** プールごとに最後に出した番号。巡の変わり目で同じものを続けない。 */
  lastIndex: Record<string, number>
  started: boolean
}

export function createTalkState(): TalkState {
  return { lastKind: null, bags: {}, lastIndex: {}, started: false }
}

/** 0〜size-1 をシャッフルした山を作る。 */
function fillBag(bag: number[], size: number, rng: () => number): void {
  for (let i = 0; i < size; i += 1) bag.push(i)
  for (let i = bag.length - 1; i > 0; i -= 1) {
    const j = Math.floor(rng() * (i + 1))
    const swap = bag[i]
    bag[i] = bag[j]
    bag[j] = swap
  }
}

/** 山から1つ引く。山が空になったら作り直すが、直前と同じ番号は避ける。 */
function draw(state: TalkState, key: string, size: number, rng: () => number): number {
  let bag = state.bags[key]
  if (!bag) {
    bag = []
    state.bags[key] = bag
  }
  if (bag.length === 0) {
    fillBag(bag, size, rng)
    const last = state.lastIndex[key]
    const tail = bag.length - 1
    if (tail > 0 && last !== undefined && bag[tail] === last) {
      bag[tail] = bag[tail - 1]
      bag[tail - 1] = last
    }
  }
  const index = bag.pop() ?? 0
  state.lastIndex[key] = index
  return index
}

/** 時間帯。朝5〜11時、昼11〜17時、夕17〜22時、それ以外は夜。 */
export function timeBucket(hour: number): keyof typeof TIME_GREETINGS {
  if (hour >= 5 && hour < 11) return 'morning'
  if (hour >= 11 && hour < 17) return 'day'
  if (hour >= 17 && hour < 22) return 'evening'
  return 'night'
}

/** いまの学習状況に合わせた励ましの分岐。 */
export function encourageBranch(status: StudyStatus): EncourageBranch {
  if (status.totalDays === 0) return 'noDays'
  if (status.studiedToday) return (status.lastGap ?? 0) >= 3 ? 'backDone' : 'todayDone'
  return (status.daysSinceLast ?? 0) >= 3 ? 'back' : 'todayNotYet'
}

function fill(text: string, values: Record<string, string>): string {
  return text.replace(/\{(\w+)\}/g, (_, key: string) => values[key] ?? '')
}

function pickMood(kind: TalkKind, rng: () => number): IngbirdMood {
  const pool = MOODS[kind]
  return pool[Math.min(pool.length - 1, Math.floor(rng() * pool.length))]
}

function nextKind(state: TalkState, rng: () => number): TalkKind {
  if (!state.started) {
    state.started = true
    state.lastKind = 'encourage'
    return 'encourage'
  }
  // 直前と同じ種類は候補から外す。候補は常に残る(2種類以上あるため)。
  const candidates = CATEGORY_POOL.filter((kind) => kind !== state.lastKind)
  const kind = candidates[Math.floor(rng() * candidates.length)] ?? candidates[0] ?? 'encourage'
  state.lastKind = kind
  return kind
}

function composedEncourage(state: TalkState, status: StudyStatus, rng: () => number, mood: IngbirdMood): TalkLine {
  const branch = encourageBranch(status)
  const bodies = ENCOURAGE_BODIES[branch]
  const values: Record<string, string> = {
    days: String(status.totalDays),
    gap: describeGap(status.studiedToday ? (status.lastGap ?? 0) : (status.daysSinceLast ?? 0)),
    next: status.next ? String(status.next.at) : '',
    remaining: status.next ? String(status.next.remaining) : '',
  }

  // 節目を使い切った後の日は {next}/{remaining} が埋まらないため、別の本文を引き直す。
  let index = draw(state, `encourage-body-${branch}`, bodies.length, rng)
  for (let attempt = 0; attempt < 8 && fill(bodies[index], values).includes('{'); attempt += 1) {
    index = draw(state, `encourage-body-${branch}`, bodies.length, rng)
  }
  let body = fill(bodies[index], values)
  if (body.includes('{')) {
    const fallback = bodies.findIndex((candidate) => !candidate.includes('{'))
    body = fill(bodies[fallback === -1 ? 0 : fallback], values)
  }

  const closing = ENCOURAGE_CLOSINGS[draw(state, 'encourage-closing', ENCOURAGE_CLOSINGS.length, rng)]
  return { id: `c-${branch}-${index + 1}`, kind: 'encourage', mood, text: `${body} ${closing}` }
}

function encourageLine(state: TalkState, status: StudyStatus, hour: number, rng: () => number): TalkLine {
  const mood = pickMood('encourage', rng)
  const source = ENCOURAGE_SOURCES[draw(state, 'encourage-source', ENCOURAGE_SOURCES.length, rng)]

  if (source === 'greeting') {
    const bucket = timeBucket(hour)
    const index = draw(state, `greeting-${bucket}`, TIME_GREETINGS[bucket].length, rng)
    return { id: `g-${bucket}-${index + 1}`, kind: 'encourage', mood, text: TIME_GREETINGS[bucket][index] }
  }

  if (source === 'line') {
    const index = draw(state, 'encourage-line', ENCOURAGE_LINES.length, rng)
    return { id: `e${index + 1}`, kind: 'encourage', mood, text: ENCOURAGE_LINES[index] }
  }

  return composedEncourage(state, status, rng, mood)
}

/**
 * 画面を開いたときの最初のひとこと。進捗に合わせて組み立てた本文から必ず選ぶ。
 * タップして聞く場合は nextTalk を使う。
 */
export function firstTalk(state: TalkState, status: StudyStatus, rng: () => number = Math.random): TalkLine {
  state.started = true
  state.lastKind = 'encourage'
  return composedEncourage(state, status, rng, pickMood('encourage', rng))
}

/**
 * 次のひとことを選ぶ。`hour` と `rng` はテストから固定できる。
 * 状態を更新するので、呼び出し側は同じ state を持ち続ける。
 */
export function nextTalk(
  state: TalkState,
  status: StudyStatus,
  hour: number = new Date().getHours(),
  rng: () => number = Math.random,
): TalkLine {
  const kind = nextKind(state, rng)

  if (kind === 'phrase') {
    const index = draw(state, 'phrase', PHRASES.length, rng)
    const phrase = PHRASES[index]
    return {
      id: phrase.id,
      kind: 'phrase',
      mood: pickMood('phrase', rng),
      text: phrase.en,
      ja: phrase.ja,
      note: phrase.note,
      scene: phrase.scene,
      speech: { text: phrase.en, locale: 'en-US' },
    }
  }

  if (kind === 'tip') {
    const index = draw(state, 'tip', TIP_LINES.length, rng)
    return { id: TIP_LINES[index].id, kind: 'tip', mood: pickMood('tip', rng), text: TIP_LINES[index].text }
  }

  return encourageLine(state, status, hour, rng)
}
