import { describe, expect, it } from 'vitest'
import { findLesson } from '../../content/grammar'
import { classifyIntent, createSectionChat, normalizeQuestion } from './matcher'
import type { ChatReply } from './types'

function lesson(id: string) {
  const found = findLesson(id)
  if (!found) throw new Error(`レッスンが見つかりません: ${id}`)
  return found
}

function ask(id: string, question: string): ChatReply {
  return createSectionChat(lesson(id), () => 0).reply(question)
}

/** 回答に含まれる全文(引用・注記まで)を1つの文字列にする。 */
function textOf(reply: ChatReply): string {
  if (reply.kind === 'fallback') return reply.message
  return [reply.lead, ...reply.quotes.flatMap((quote) => [quote.label, quote.en ?? '', quote.ja ?? '', quote.note ?? '', quote.text ?? ''])].join('\n')
}

describe('正規化と意図判定', () => {
  it('全角・大文字・短縮形をそろえる', () => {
    expect(normalizeQuestion('ＡＭ と ＩＳ の違いは?')).toBe('am と is の違いは')
    expect(normalizeQuestion("She isn't busy.")).toBe('she is not busy')
    expect(normalizeQuestion('Why?\n')).toBe('why')
  })

  it('言い回しから意図を拾う', () => {
    expect(classifyIntent('何文型?')?.intent).toBe('pattern')
    expect(classifyIntent('SVOってどこ?')?.intent).toBe('pattern')
    expect(classifyIntent('主語はどれ?')?.intent).toBe('structure')
    expect(classifyIntent('I am a nurse. の意味は?')?.intent).toBe('meaning')
    expect(classifyIntent('三単現って何?')?.intent).toBe('concept')
    expect(classifyIntent('なぜそうなるの?')?.intent).toBe('concept')
    expect(classifyIntent('まとめを教えて')?.intent).toBe('summary')
    expect(classifyIntent('今日の天気')).toBeNull()
  })

  it('あいさつに実質的な質問が続くときは、質問の意図を優先する', () => {
    expect(classifyIntent('こんにちは、まとめを教えて')?.intent).toBe('summary')
    expect(classifyIntent('こんにちは')?.intent).toBe('greeting')
  })
})

describe('言い回しの揺れに耐える', () => {
  function expectIntent(id: string, question: string, intent: string, contains?: string) {
    const reply = ask(id, question)
    expect(reply.kind, question).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent, question).toBe(intent)
    if (contains) expect(textOf(reply), question).toContain(contains)
  }

  it('まとめの聞き方いろいろ', () => {
    for (const question of ['要点は?', 'おさらいしたい', 'テストに出るところは?', '覚えておくべきことは?', '振り返りたい']) {
      expectIntent('u01-l1', question, 'summary')
    }
  })

  it('例文の聞き方いろいろ', () => {
    for (const question of ['たとえば?', '具体的な例は?', 'どんな例がある?', '英文の例をください']) {
      expectIntent('u01-l2', question, 'example')
    }
  })

  it('理由の聞き方いろいろ', () => {
    for (const question of [
      'なぜ三人称単数で-sを付けるの?',
      'どうして三単現が必要なの?',
      'なんで三単現だと-sが付くの?',
      '三単現の理由を教えて',
    ]) {
      expectIntent('u01-l2', question, 'concept', '3人称')
    }
  })

  it('使い分けの聞き方いろいろ', () => {
    for (const question of ['-s が付くときと付かないときの区別は?', 'どっちに-sを付けるの?', '三単現の使い分けを教えて']) {
      expectIntent('u01-l2', question, 'difference', '主語')
    }
  })

  it('文型の聞き方いろいろ', () => {
    for (const question of ['SVOってどこ?', '5文型で見ると?', 'このセクションの例文の文型は?']) {
      expectIntent('u01-l1', question, 'pattern')
    }
  })

  it('全角・記号入りの質問でも同じ答えに着地する', () => {
    expectIntent('u01-l1', 'Ｉ ａｍ ａ ｎｕｒｓｅ．の和訳', 'meaning', '看護師')
    expectIntent('u01-l1', '「My brother is not busy now.」を訳して', 'meaning', '忙しく')
  })

  it('英語の質問にも答える', () => {
    expectIntent('u01-l1', 'give me a hint', 'quiz')
    expectIntent('u01-l1', 'What will I learn here?', 'overview')
  })

  it('セクション外の質問は答えない', () => {
    for (const question of ['おすすめの映画は?', '今日の天気は?', '明日の予定を教えて']) {
      const reply = ask('u01-l1', question)
      expect(reply.kind, question).toBe('fallback')
    }
  })
})

describe('曖昧な入力(一語・体言止め)', () => {
  it('用語をひとつだけ聞いても、その説明に着地する', () => {
    const cases = [
      ['u01-l1', 'be動詞', 'be動詞'],
      ['u01-l2', '三単現', '3人称'],
      ['u01-l2', '例文', 'works'],
      ['u01-l1', '文型', 'SV'],
      ['u02-l1', '現在進行形', '進行'],
      ['u11-l1', '現在完了', '完了'],
    ] as const
    for (const [id, term, expected] of cases) {
      const reply = ask(id, term)
      expect(reply.kind, term).toBe('answer')
      if (reply.kind !== 'answer') continue
      expect(textOf(reply), term).toContain(expected)
    }
  })

  it('「〇〇とは」「〇〇なに」「〇〇って何」でも答える', () => {
    for (const question of ['三単現とは?', '三単現なに?', '三単現って何?', '三単現について教えて']) {
      const reply = ask('u01-l2', question)
      expect(reply.kind, question).toBe('answer')
      if (reply.kind === 'answer') expect(textOf(reply), question).toContain('3人称')
    }
  })

  it('短い英語の語だけでも答える(not / is)', () => {
    for (const word of ['not', 'is']) {
      const reply = ask('u01-l1', word)
      expect(reply.kind, word).toBe('answer')
    }
  })
})

describe('返答の返答(文脈)', () => {
  it('「もっと詳しく」で同じ解説の続きを話す', () => {
    const chat = createSectionChat(lesson('u01-l2'), () => 0)
    const first = chat.reply('三単現の-sはなぜ必要?')
    expect(first.kind).toBe('answer')

    const more = chat.reply('もっと詳しく')
    expect(more.kind).toBe('answer')
    if (more.kind !== 'answer') return
    expect(more.lead).toContain('続き')
    expect(textOf(more)).toContain('-')
  })

  it('「この文の文型は?」は直前の例文から解決する', () => {
    const chat = createSectionChat(lesson('u01-l1'), () => 0)
    chat.reply('"I am a nurse." の意味は?')

    const follow = chat.reply('この文の文型は?')
    expect(follow.kind).toBe('answer')
    if (follow.kind !== 'answer') return
    expect(follow.intent).toBe('pattern')
    expect(textOf(follow)).toContain('SVC')
  })

  it('「他には?」で関連するQAを引く', () => {
    const chat = createSectionChat(lesson('u01-l1'), () => 0)
    chat.reply('"I am a nurse." の意味は?')

    const other = chat.reply('他には?')
    expect(other.kind).toBe('answer')
  })

  it('「もう一度」で同じ回答を言い直す', () => {
    const chat = createSectionChat(lesson('u01-l1'), () => 0)
    chat.reply('まとめを教えて')

    const again = chat.reply('もう一度')
    expect(again.kind).toBe('answer')
    if (again.kind !== 'answer') return
    expect(again.lead).toContain('もう一度')
    expect(textOf(again)).toContain('do / does')
  })

  it('回答のあとの「なぜ?」は、直前の話題の解説を引く', () => {
    const chat = createSectionChat(lesson('u01-l1'), () => 0)
    chat.reply('"I am a nurse." の意味は?')

    const why = chat.reply('なぜ?')
    expect(why.kind).toBe('answer')
    if (why.kind !== 'answer') return
    expect(why.intent).toBe('concept')
  })

  it('文脈がなければ、フォローアップの言葉は答えられないと言う', () => {
    expect(ask('u01-l1', 'もっと詳しく').kind).toBe('fallback')
  })
})

describe('u01-l1(be動詞の現在形)への質問', () => {
  it('このセクションで何を学ぶか', () => {
    const reply = ask('u01-l1', 'このセクションで何を学ぶの?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('overview')
    expect(textOf(reply)).toContain('am / is / are')
  })

  it('まとめを聞くと、まとめの要点を引用する', () => {
    const reply = ask('u01-l1', 'まとめを教えて')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('summary')
    expect(textOf(reply)).toContain('do / does は使わない')
  })

  it('例文の意味は、和訳つきで答える', () => {
    const reply = ask('u01-l1', '"I am a nurse." の意味は?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('meaning')
    expect(textOf(reply)).toContain('看護師')
  })

  it('英語で聞いても答える', () => {
    const reply = ask('u01-l1', 'What does "My brother is not busy now." mean?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(textOf(reply)).toContain('忙しく')
  })

  it('例文の文型を答える', () => {
    const reply = ask('u01-l1', '"I am a nurse." は何文型?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('pattern')
    expect(textOf(reply)).toContain('SVC')
  })

  it('文型の視点をまとめて答える', () => {
    const reply = ask('u01-l1', '文型の視点を教えて')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('pattern')
    expect(reply.lead).toContain('SVC')
  })

  it('構造図から主語を答える', () => {
    const reply = ask('u01-l1', '主語はどれ?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('structure')
    expect(textOf(reply)).toContain('She')
  })

  it('表から使い分けを答える(am と is の違い)', () => {
    const reply = ask('u01-l1', 'amとisの違いは?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(textOf(reply)).toContain('am')
    expect(textOf(reply)).toContain('is')
  })

  it('you のときの be動詞を答える', () => {
    const reply = ask('u01-l1', 'youのときのbe動詞は?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(textOf(reply)).toContain('are')
  })

  it('クイズのヒントは考え方を返し、答えそのものは言わない', () => {
    const reply = ask('u01-l1', 'クイズのヒントをちょうだい')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('quiz')
    expect(textOf(reply)).toContain('考え方')

    const answer = ask('u01-l1', '答えを教えて')
    expect(answer.kind).toBe('answer')
    if (answer.kind !== 'answer') return
    expect(answer.intent).toBe('quiz')
    expect(answer.lead).toContain('言わない')
  })

  it('あいさつと機能説明に答える', () => {
    const greeting = ask('u01-l1', 'こんにちは')
    expect(greeting.kind).toBe('answer')
    if (greeting.kind === 'answer') expect(greeting.intent).toBe('greeting')

    const capability = ask('u01-l1', '何ができるの?')
    expect(capability.kind).toBe('answer')
    if (capability.kind === 'answer') expect(capability.intent).toBe('capability')
  })

  it('セクションの外の質問は、正直に答えられないと言う', () => {
    const reply = ask('u01-l1', '今日の天気は?')
    expect(reply.kind).toBe('fallback')
    if (reply.kind !== 'fallback') return
    expect(reply.message).toContain('見つけられなかった')
    expect(reply.suggestions.length).toBeGreaterThan(0)
  })
})

describe('u01-l2(三単現)の対比', () => {
  it('対比の違いを、両側のラベルつきで答える', () => {
    const reply = ask('u01-l2', '「-s が付く」と「-s が付かない」の違いは?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('difference')
    expect(textOf(reply)).toContain('3人称単数')
  })

  it('対比の中の例文の意味も答える', () => {
    const reply = ask('u01-l2', '"She likes music." の意味は?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(textOf(reply)).toContain('音楽が好き')
  })

  it('なぜ -s を付けるのかを解説から答える', () => {
    const reply = ask('u01-l2', 'なぜ三人称単数で-sを付けるの?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('concept')
    expect(textOf(reply)).toContain('3人称')
  })

  it('例文の一覧を返す', () => {
    const reply = ask('u01-l2', '例文を教えて')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('example')
    expect(reply.quotes.length).toBeGreaterThanOrEqual(3)
    expect(textOf(reply)).toContain('works')
  })
})

describe('u02-l1(現在進行形)の構造図', () => {
  it('主語(S)を分解図から答える', () => {
    const reply = ask('u02-l1', 'この文の主語は?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('structure')
    expect(textOf(reply)).toContain('主語(S)')
  })

  it('骨格だけを見せられる', () => {
    const reply = ask('u02-l1', '"I am playing tennis." の骨格は?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('structure')
    expect(textOf(reply)).toContain('I play tennis.')
  })

  it('文型を答える', () => {
    const reply = ask('u02-l1', '"I am playing tennis." は何文型?')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('pattern')
    expect(textOf(reply)).toContain('SVO')
  })

  it('文の分解を見せる', () => {
    const reply = ask('u02-l1', '文を分解して')
    expect(reply.kind).toBe('answer')
    if (reply.kind !== 'answer') return
    expect(reply.intent).toBe('structure')
    expect(textOf(reply)).toContain('am playing')
  })
})
