// セクション内Q&Aのコーパス生成。
//
// 「イングバードにきく」の頭脳はこのコーパス。レッスンの全ブロック(解説・表・構造・例文・対比・
// タイムライン・構造図・展開・挿絵)、クイズ、まとめ、目標を、質問の言い回し候補つきのQAに変換する。
// 生成は決定的で、教材を変えればQAも即座に変わる(別ファイルの二重管理をしない)。
//
// 1つのQAは2種類の文字列を持つ:
// - questions: 質問の言い回し候補。チップ表示にも使う。
// - terms: 検索専用の語(英文・本文・英単語)。索引にだけ載せ、質問候補としては表示しない。

import type { GrammarExample, GrammarLesson, SentenceRole } from '../../content/types'
import { CURRICULUM_TERMS } from './intents'
import { CAPABILITY_LEAD, GREETING_LEAD, PHRASINGS, QUIZ_REFUSAL, THANKS_LEAD } from './phrasings'
import type { QaEntry, QaIntent, QaQuote } from './types'

const ROLE_LABEL: Record<SentenceRole, string> = {
  S: '主語(S)',
  V: '動詞(V)',
  O: '目的語(O)',
  C: '補語(C)',
  M: '修飾語(M)',
}

/** テンプレートに値を流し込む。値が欠けるテンプレートは捨てる(「の意味は?」のような壊れた質問を作らない)。 */
function render(template: string, vars: Record<string, string>): string | null {
  let missing = false
  const text = template.replace(/\{(\w+)\}/g, (_, key: string) => {
    const value = vars[key]
    if (value === undefined || value === '') {
      missing = true
      return ''
    }
    return value
  })
  return missing ? null : text.replace(/\s+/g, ' ').trim()
}

function cleanText(text: string): string {
  return text.replace(/\s+/g, ' ').trim()
}

/**
 * 言い回し候補(questions)と検索専用語(terms)を作る。
 * terms には教材本文や英文をそのまま渡し、日本語のbigramや英単語として索引に載せる。
 */
function renderQa(
  templates: readonly string[],
  vars: Record<string, string>,
  terms: ReadonlyArray<string | undefined> = [],
): { questions: string[]; terms: string[] } {
  const questions: string[] = []
  for (const template of templates) {
    const question = render(template, vars)
    if (question) questions.push(question)
  }
  return {
    questions: [...new Set(questions)],
    terms: [...new Set(terms.filter((term): term is string => Boolean(term && term.trim())).map(cleanText))],
  }
}

function splitParagraphs(body: string): string[] {
  return body
    .replace(/\*\*/g, '')
    .split(/\n{2,}/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean)
}

/** 文中の英単語。解説のどの段落がその語を扱っているかを判定器が拾えるようにする。 */
function englishWords(text: string): string[] {
  const found = text.match(/[A-Za-z][A-Za-z'-]*/g) ?? []
  const seen = new Set<string>()
  const words: string[] = []
  for (const word of found) {
    const key = word.toLowerCase()
    if (key.length < 2 || seen.has(key)) continue
    seen.add(key)
    words.push(key)
    if (words.length >= 16) break
  }
  return words
}

function sideText(side: { pointJa?: string; items: GrammarExample[] }): string {
  return [side.pointJa, ...side.items.map((item) => `${item.en}${item.ja ? ` — ${item.ja}` : ''}`)]
    .filter(Boolean)
    .join('\n')
}

function exampleQuote(item: GrammarExample, label = '例文'): QaQuote {
  return { label, en: item.en, ja: item.ja, note: item.note }
}

function countOccurrences(text: string, needle: string): number {
  let count = 0
  let index = text.indexOf(needle)
  while (index !== -1) {
    count += 1
    index = text.indexOf(needle, index + needle.length)
  }
  return count
}

/**
 * レッスン1つぶんのQAコーパスを作る。
 * 目安としてA2の1セクションで40〜70件、B2の長いセクションで100件規模になる。
 */
export function buildSectionQa(lesson: GrammarLesson): QaEntry[] {
  const entries: QaEntry[] = []
  const add = (entry: QaEntry) => entries.push(entry)
  const topic = lesson.title
  const allExamples: GrammarExample[] = lesson.blocks.flatMap((block) =>
    block.type === 'examples'
      ? block.items
      : block.type === 'contrast'
        ? [...block.left.items, ...block.right.items]
        : [],
  )
  const defaultFollowups = ['例文を教えて', '文型は?', 'まとめを教えて', 'クイズのヒントをちょうだい']

  // 全体像
  add({
    id: `${lesson.id}:overview`,
    intent: 'overview',
    subject: lesson.title,
    ...renderQa(PHRASINGS.overview, { topic }, [lesson.objective]),
    answer: {
      lead: `このセクションは「${lesson.title}」(${lesson.level}・目安${lesson.minutes}分)だよ。`,
      quotes: [{ label: 'このセクションの目標', text: lesson.objective }],
      followups: ['例文を教えて', 'まとめを教えて', 'クイズは何問?'],
    },
    priority: 7,
  })

  // まとめ
  if (lesson.summary.length > 0) {
    add({
      id: `${lesson.id}:summary`,
      intent: 'summary',
      ...renderQa(PHRASINGS.summary, {}, lesson.summary),
      answer: {
        lead: `このセクションの要点は${lesson.summary.length}つ。ここだけは持って帰ろう!`,
        quotes: [{ label: 'まとめ', text: lesson.summary.join('\n') }],
        followups: ['クイズのヒントをちょうだい', '例文を教えて'],
      },
      priority: 9,
    })
  }

  // クイズ(答えそのものは言わず、考え方を返す)
  const quiz = [
    ...lesson.quiz.map((question) => ({ question, label: '理解度チェック' })),
    ...(lesson.structureQuiz ?? []).map((question) => ({ question, label: '構造チェック' })),
  ]
  if (quiz.length > 0) {
    add({
      id: `${lesson.id}:quiz:list`,
      intent: 'quiz',
      ...renderQa(PHRASINGS.quizList, {}),
      answer: {
        lead: `このセクションのクイズは${quiz.length}問(${[...new Set(quiz.map((item) => item.label))].join('・')})。`,
        quotes: [
          {
            label: '問題',
            text: quiz
              .slice(0, 6)
              .map((item, index) => `${index + 1}. ${item.question.prompt}${item.question.sentence ? ` ${item.question.sentence}` : ''}`)
              .join('\n'),
          },
        ],
        followups: ['ヒントをちょうだい', 'まとめを教えて'],
      },
      priority: 8,
    })
    for (const { question, label } of quiz) {
      add({
        id: `${lesson.id}:quiz:${question.id}`,
        intent: 'quiz',
        subject: question.sentence ?? question.prompt,
        ...renderQa(PHRASINGS.quizHint, {}, [
          ...PHRASINGS.quizAnswer,
          question.sentence,
          ...(question.sentence ? englishWords(question.sentence) : []),
        ]),
        answer: {
          lead: QUIZ_REFUSAL,
          quotes: [
            {
              label: `${label}の問題`,
              text: [question.prompt, question.sentence, question.sentenceJa].filter(Boolean).join(' '),
            },
            { label: '考え方', text: question.explanation },
          ],
          followups: ['クイズは何問?', 'まとめを教えて'],
        },
        priority: 6,
      })
      // 誤答の理由(「他の選択肢はなぜダメ?」)。正解は言わない方針は同じ
      const wrongNotes = (question.choiceNotes ?? [])
        .map((note, index) => (note ? `・${question.choices[index]} — ${note}` : null))
        .filter((line): line is string => Boolean(line))
      if (wrongNotes.length > 0) {
        add({
          id: `${lesson.id}:quiz-notes:${question.id}`,
          intent: 'note',
          subject: question.sentence ?? question.prompt,
          ...renderQa(PHRASINGS.quizNotes, {}, [
            question.sentence,
            question.sentenceJa,
            ...(question.sentence ? englishWords(question.sentence) : []),
          ]),
          answer: {
            lead: 'ほかの選択肢がなぜダメかというと、こういう理由だよ。正解は自分で選んでね。',
            quotes: [
              { label: '間違いの理由', text: wrongNotes.join('\n') },
              { label: `${label}の問題`, text: [question.prompt, question.sentence].filter(Boolean).join(' ') },
            ],
            followups: ['ヒントをちょうだい', 'まとめを教えて'],
          },
          priority: 6,
        })
      }
    }
  }

  // ブロックごとのQA
  lesson.blocks.forEach((block, blockIndex) => {
    switch (block.type) {
      case 'explanation': {
        splitParagraphs(block.body).forEach((paragraph, index) => {
          add({
            id: `${lesson.id}:concept:${blockIndex}-${index}`,
            intent: 'concept',
            subject: block.title ?? englishWords(paragraph).slice(0, 3).join(' '),
            ...renderQa(PHRASINGS.concept, { title: block.title ?? '' }, [
              paragraph,
              ...englishWords(paragraph),
            ]),
            answer: {
              lead: block.title
                ? `「${block.title}」のところだね。セクションの解説ではこう言っているよ。`
                : 'セクションの解説ではこう言っているよ。',
              quotes: [{ label: block.title ?? '解説', text: paragraph }],
              followups: ['例文で確認したい', 'まとめを教えて'],
            },
            priority: block.title === '文型の視点' ? 6 : 5,
          })
        })
        break
      }

      case 'examples': {
        const items = block.items
        if (items.length > 0) {
          add({
            id: `${lesson.id}:example:${blockIndex}`,
            intent: 'example',
            subject: topic,
            ...renderQa(
              PHRASINGS.example,
              { topic },
              items.flatMap((item) => [item.en, item.ja, ...englishWords(item.en)]),
            ),
            answer: {
              lead: `このセクションの例文をいくつか挙げるね${block.title ? `(「${block.title}」より)` : ''}。`,
              quotes: items.slice(0, 3).map((item) => exampleQuote(item)),
              followups: ['意味をもう一度確認したい', '文型は?'],
            },
            priority: 8,
          })
          add({
            id: `${lesson.id}:pronunciation:${blockIndex}`,
            intent: 'pronunciation',
            subject: items[0].en,
            ...renderQa(PHRASINGS.pronunciation, {}, items.slice(0, 3).flatMap((item) => englishWords(item.en))),
            answer: {
              lead: '発音は、英文の横の 🔊 ボタンで何度でも聞けるよ。ゆっくりの再生もあるから、聞き取れるまで試してみて。',
              quotes: [exampleQuote(items[0])],
              followups: ['例文を教えて', 'まとめを教えて'],
            },
            priority: 5,
          })
        }
        items.forEach((item, itemIndex) => {
          add({
            id: `${lesson.id}:meaning:${blockIndex}-${itemIndex}`,
            intent: 'meaning',
            subject: item.en,
            ...renderQa(PHRASINGS.meaning, { en: item.en }, [
              item.ja,
              item.note,
              ...englishWords(item.en),
            ]),
            answer: {
              lead: `"${item.en}" だね!このセクションの例文では、こうなっているよ。`,
              quotes: [exampleQuote(item)],
              followups: [`"${item.en}" は何文型?`, 'ほかの例文も見たい', 'まとめを教えて'],
            },
            priority: 7,
          })
          if (item.ja) {
            add({
              id: `${lesson.id}:ja2en:${blockIndex}-${itemIndex}`,
              intent: 'meaning',
              subject: item.ja,
              ...renderQa(PHRASINGS.meaningJa, { ja: item.ja, en: item.en }, [item.en, ...englishWords(item.en)]),
              answer: {
                lead: `「${item.ja}」を英語にすると、こうなるよ。`,
                quotes: [exampleQuote(item)],
                followups: [`"${item.en}" の意味は?`, '発音を聞きたい', 'まとめを教えて'],
              },
              priority: 6,
            })
          }
          add({
            id: `${lesson.id}:say:${blockIndex}-${itemIndex}`,
            intent: 'pronunciation',
            subject: item.en,
            ...renderQa(PHRASINGS.pronunciationItem, { en: item.en }, [item.ja]),
            answer: {
              lead: '英文の横の 🔊 ボタンで聞けるよ。ゆっくりの再生もあるから、聞き取れるまで試してみて。',
              quotes: [exampleQuote(item)],
              followups: ['例文を教えて', 'まとめを教えて'],
            },
            priority: 5,
          })
          if (item.highlight) {
            add({
              id: `${lesson.id}:term:${blockIndex}-${itemIndex}`,
              intent: 'meaning',
              subject: item.highlight,
              ...renderQa(PHRASINGS.term, { term: item.highlight, en: item.en }, [item.ja, item.note]),
              answer: {
                lead: `"${item.highlight}" についてだね。この例文の中で使われているよ。`,
                quotes: [exampleQuote(item)],
                followups: [`"${item.en}" の意味は?`, 'まとめを教えて'],
              },
              priority: 5,
            })
          }
          if (item.pattern) {
            add({
              id: `${lesson.id}:pattern:${blockIndex}-${itemIndex}`,
              intent: 'pattern',
              subject: item.en,
              ...renderQa(PHRASINGS.pattern, { en: item.en, pattern: item.pattern }, [item.patternNote]),
              answer: {
                lead: `"${item.en}" は ${item.pattern} の文型だよ。`,
                quotes: [
                  { label: '文型', text: `${item.pattern}${item.patternNote ? ` — ${item.patternNote}` : ''}` },
                  exampleQuote(item),
                ],
                followups: ['文型の視点を教えて', '構造を分解して'],
              },
              priority: 7,
            })
          }
          if (item.note) {
            add({
              id: `${lesson.id}:note:${blockIndex}-${itemIndex}`,
              intent: 'note',
              subject: item.en,
              ...renderQa(PHRASINGS.note, {}, [item.en, item.note, ...englishWords(item.note)]),
              answer: {
                lead: 'この文のワンポイントだよ。',
                quotes: [{ label: '注意', text: item.note }, exampleQuote(item)],
                followups: ['例文を教えて', 'まとめを教えて'],
              },
              priority: 4,
            })
          }
        })
        break
      }

      case 'contrast': {
        const { left, right } = block
        add({
          id: `${lesson.id}:diff:${blockIndex}`,
          intent: 'difference',
          subject: `${left.label} ${right.label}`,
          ...renderQa([...PHRASINGS.difference, ...PHRASINGS.differenceGeneric], { left: left.label, right: right.label }, [
            sideText(left),
            sideText(right),
            block.note,
          ]),
          answer: {
            lead: `${left.label} と ${right.label} の違いだね。セクションではこう整理しているよ。`,
            quotes: [
              { label: left.label, text: sideText(left) },
              { label: right.label, text: sideText(right) },
              ...(block.note ? [{ label: 'ポイント', text: block.note }] : []),
            ],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 9,
        })
        for (const side of [left, right]) {
          add({
            id: `${lesson.id}:diff:${blockIndex}:${side.label}`,
            // 「いつ使うの?」など片側の使い方を答えるQA。比較そのものではなく解説なので concept。
            intent: 'concept',
            subject: side.label,
            questions: [
              `${side.label}はいつ使うの?`,
              `${side.label}のときは?`,
              `${side.label}側の例は?`,
              `${side.label}を使う場面は?`,
            ],
            answer: {
              lead: `「${side.label}」だね。`,
              quotes: [{ label: side.label, text: sideText(side) }],
              followups: ['違いをまとめて', '例文を教えて'],
            },
            priority: 6,
          })
        }
        // 対比の中の英文も例文なので、意味と文型を単独で聞けるようにする
        ;[...left.items, ...right.items].forEach((item, itemIndex) => {
          add({
            id: `${lesson.id}:diff-example:${blockIndex}-${itemIndex}`,
            intent: 'meaning',
            subject: item.en,
            ...renderQa(PHRASINGS.meaning, { en: item.en }, [...englishWords(item.en), item.ja, item.note]),
            answer: {
              lead: `"${item.en}" だね!対比の中の例文では、こうなっているよ。`,
              quotes: [{ label: itemIndex < left.items.length ? left.label : right.label, en: item.en, ja: item.ja, note: item.note }],
              followups: ['違いをまとめて', 'まとめを教えて'],
            },
            priority: 5,
          })
          if (item.ja) {
            add({
              id: `${lesson.id}:diff-ja2en:${blockIndex}-${itemIndex}`,
              intent: 'meaning',
              subject: item.ja,
              ...renderQa(PHRASINGS.meaningJa, { ja: item.ja, en: item.en }, [item.en, ...englishWords(item.en)]),
              answer: {
                lead: `「${item.ja}」を英語にすると、こうなるよ。`,
                quotes: [exampleQuote(item, itemIndex < left.items.length ? left.label : right.label)],
                followups: [`"${item.en}" の意味は?`, '違いをまとめて'],
              },
              priority: 5,
            })
          }
          if (item.pattern) {
            add({
              id: `${lesson.id}:diff-pattern:${blockIndex}-${itemIndex}`,
              intent: 'pattern',
              subject: item.en,
              ...renderQa(PHRASINGS.pattern, { en: item.en, pattern: item.pattern }),
              answer: {
                lead: `"${item.en}" は ${item.pattern} の文型だよ。`,
                quotes: [
                  { label: '文型', text: `${item.pattern}${item.patternNote ? ` — ${item.patternNote}` : ''}` },
                  { label: '例文', en: item.en, ja: item.ja },
                ],
                followups: ['違いをまとめて', '文型の視点を教えて'],
              },
              priority: 6,
            })
          }
        })
        break
      }

      case 'table': {
        add({
          id: `${lesson.id}:table:${blockIndex}`,
          intent: 'table',
          subject: block.title ?? block.headers.join(' '),
          ...renderQa(
            block.title
              ? [...PHRASINGS.table, ...PHRASINGS.differenceGeneric, `${block.title}は?`, `${block.title}って何?`]
              : [...PHRASINGS.table, ...PHRASINGS.differenceGeneric],
            {},
            [block.title, ...block.rows.flat()],
          ),
          answer: {
            lead: block.title ? `「${block.title}」の表だよ。` : 'この表を見てね。',
            quotes: [
              {
                label: block.title ?? '表',
                text: [block.headers.join(' | '), ...block.rows.map((row) => row.join(' | '))].join('\n'),
              },
            ],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 5,
        })
        block.rows.forEach((row, rowIndex) => {
          const cells = row.filter((cell) => /[A-Za-z]/.test(cell))
          if (cells.length === 0) return
          add({
            id: `${lesson.id}:table:${blockIndex}:${rowIndex}`,
            intent: 'concept',
            subject: row.join(' '),
            questions: [
              `${row.join('、')}の使い方は?`,
              ...cells.map((cell) => `${cell}はどんなとき?`),
              ...cells.map((cell) => `${cell}の使い方は?`),
              ...(block.headers[1]
                ? row[0]
                    .split(/[/、,]/)
                    .map((word) => word.trim())
                    .filter((word) => word.length >= 2)
                    .flatMap((word) => [`${word}の${block.headers[1]}は?`, `${word}のときの${block.headers[1]}は?`])
                : []),
            ],
            answer: {
              lead: row[0] ? `「${row[0]}」のところだね。` : '表の一部だね。',
              quotes: [{ label: block.title ?? '表', text: row.join(' → ') }],
              followups: ['表を見せて', 'まとめを教えて'],
            },
            priority: 4,
          })
          // 列見出しに沿った質問(「goの過去形は?」「Iの短縮形は?」)
          for (let column = 1; column < Math.min(block.headers.length, row.length); column += 1) {
            const heading = block.headers[column]
            const value = row[column]
            if (!heading || !/[A-Za-z]/.test(value)) continue
            // 見出しの言葉がそのまま質問の意図になる(「〜の例は?」→ example、「〜の意味は?」→ meaning)
            const intent = heading.includes('例')
              ? ('example' as const)
              : heading.includes('意味') || heading.includes('訳')
                ? ('meaning' as const)
                : ('concept' as const)
            add({
              id: `${lesson.id}:table:${blockIndex}:${rowIndex}:c${column}`,
              intent,
              subject: value,
              questions: [`${row[0]}の${heading}は?`, `${row[0]}の${heading}を教えて`],
              terms: [row.join('、')],
              answer: {
                lead: `「${row[0]}」の${heading}は「${value}」だよ。`,
                quotes: [{ label: block.title ?? '表', text: row.join(' → ') }],
                followups: ['表を見せて', '例文を教えて'],
              },
              priority: 5,
            })
          }
        })
        break
      }

      case 'structure': {
        add({
          id: `${lesson.id}:structure:${blockIndex}`,
          intent: 'structure',
          subject: block.title ?? block.parts.map((part) => part.text).join(' '),
          ...renderQa(PHRASINGS.structure, { topic }, [
            ...block.parts.flatMap((part) => englishWords(part.text)),
            block.title,
            block.caption,
          ]),
          answer: {
            lead: block.title ? `「${block.title}」の構造だね。` : 'この構造を見てね。',
            quotes: [
              { label: '構造', text: block.parts.map((part) => `${part.label} → ${part.text}`).join('\n') },
              ...(block.caption ? [{ label: 'ポイント', text: block.caption }] : []),
            ],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 6,
        })
        break
      }

      case 'breakdown': {
        add({
          id: `${lesson.id}:breakdown:${blockIndex}`,
          intent: 'structure',
          subject: block.sentence,
          ...renderQa(
            PHRASINGS.structure,
            {},
            [
              `"${block.sentence}"の構造は?`,
              ...englishWords(block.sentence),
              block.caption,
              block.relation,
            ],
          ),
          answer: {
            lead: `"${block.sentence}" を分解するね。`,
            quotes: [
              { label: '文', en: block.sentence, ja: block.ja },
              {
                label: '分解',
                text: block.parts
                  .map((part) => `${ROLE_LABEL[part.role]}: ${part.text}${part.note ? `(${part.note})` : ''}`)
                  .join('\n'),
              },
              ...(block.relation ? [{ label: '意味の関係', text: block.relation }] : []),
              ...(block.skeleton ? [{ label: '骨格', en: block.skeleton }] : []),
            ],
            followups: ['骨格だけ見せて', 'まとめを教えて'],
          },
          priority: 6,
        })
        // 分解対象の文も例文なので、意味を単独で聞けるようにする(「それの意味は?」の宛先)
        if (block.ja) {
          add({
            id: `${lesson.id}:breakdown-meaning:${blockIndex}`,
            intent: 'meaning',
            subject: block.sentence,
            ...renderQa(PHRASINGS.meaning, { en: block.sentence }, [block.ja, ...englishWords(block.sentence)]),
            answer: {
              lead: `"${block.sentence}" だね!このセクションの例文では、こうなっているよ。`,
              quotes: [{ label: '文', en: block.sentence, ja: block.ja }],
              followups: [`"${block.sentence}" は何文型?`, '構造を分解して', 'まとめを教えて'],
            },
            priority: 7,
          })
        }
        block.parts.forEach((part, partIndex) => {
          const label = ROLE_LABEL[part.role]
          add({
            id: `${lesson.id}:role:${blockIndex}-${partIndex}`,
            intent: 'structure',
            subject: part.text,
            questions: [`${label}はどれ?`, `${label}はどこ?`, `この文の${label}は?`, `${label}を見つけるには?`, `"${block.sentence}"の${label}は?`],
            terms: [part.note, ...englishWords(part.text)].filter((term): term is string => Boolean(term)),
            answer: {
              lead: `${label}は "${part.text}" だね。`,
              quotes: [
                { label: '分解', text: `${label}: ${part.text}${part.note ? `(${part.note})` : ''}` },
                { label: '文', en: block.sentence, ja: block.ja },
              ],
              followups: ['構造を分解して', '骨格だけ見せて'],
            },
            priority: 7,
          })
        })
        if (block.pattern) {
          add({
            id: `${lesson.id}:breakdown-pattern:${blockIndex}`,
            intent: 'pattern',
            subject: block.sentence,
            ...renderQa(PHRASINGS.pattern, { en: block.sentence, pattern: block.pattern }),
            answer: {
              lead: `"${block.sentence}" は ${block.pattern} の文型だよ。`,
              quotes: [
                { label: '文型', text: block.pattern },
                { label: '文', en: block.sentence, ja: block.ja },
              ],
              followups: ['骨格だけ見せて', '構造を分解して'],
            },
            priority: 7,
          })
        }
        if (block.skeleton) {
          add({
            id: `${lesson.id}:skeleton:${blockIndex}`,
            intent: 'structure',
            subject: block.skeleton,
            ...renderQa(PHRASINGS.skeleton, {}, [block.skeleton, ...englishWords(block.skeleton)]),
            answer: {
              lead: '修飾語を外した骨格だけだと、こうなるよ。',
              quotes: [
                { label: '骨格', en: block.skeleton },
                ...(block.skeletonPattern ? [{ label: '文型', text: block.skeletonPattern }] : []),
              ],
              followups: ['構造を分解して', 'まとめを教えて'],
            },
            priority: 8,
          })
        }
        break
      }

      case 'expansion': {
        add({
          id: `${lesson.id}:expansion:${blockIndex}`,
          intent: 'expansion',
          subject: block.steps[0]?.en,
          ...renderQa(
            PHRASINGS.expansion,
            {},
            [
              ...block.steps.flatMap((step) => [step.en, step.ja, step.note, ...englishWords(step.en)]),
              block.caption,
            ],
          ),
          answer: {
            lead: block.title ? `「${block.title}」の変化だね。` : '文が段階的に伸びる過程を見てみよう。',
            quotes: [
              {
                label: '変化',
                text: block.steps.map((step, index) => `${index + 1}. ${step.en}${step.note ? ` — ${step.note}` : ''}`).join('\n'),
              },
              ...(block.caption ? [{ label: 'ポイント', text: block.caption }] : []),
            ],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 6,
        })
        break
      }

      case 'timeline': {
        const lines = block.timelines.flatMap((timeline) =>
          [timeline.title, timeline.pointLabel, timeline.rangeLabel, timeline.caption].filter(
            (line): line is string => Boolean(line),
          ),
        )
        if (lines.length > 0) {
          add({
            id: `${lesson.id}:timeline:${blockIndex}`,
            intent: 'timeline',
            ...renderQa(PHRASINGS.timeline, {}, [block.title, ...lines]),
            answer: {
              lead: '時間のイメージはこんな感じだよ。',
              quotes: [{ label: block.title ?? 'タイムライン', text: lines.join('\n') }],
              followups: ['例文を教えて', 'まとめを教えて'],
            },
            priority: 5,
          })
        }
        break
      }

      case 'illustration': {
        add({
          id: `${lesson.id}:illustration:${blockIndex}`,
          intent: 'illustration',
          subject: block.alt,
          ...renderQa(PHRASINGS.illustration, {}, [block.alt, block.caption, ...block.labels]),
          answer: {
            lead: 'この図の説明だよ。',
            quotes: [
              {
                label: block.alt,
                text: [...block.labels, block.caption].filter(Boolean).join('\n'),
              },
            ],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 4,
        })
        break
      }

      default:
        break
    }
  })

  // 5文型の集計(例文が持つ pattern は合成時に付与されている)
  const patterned = allExamples.filter((example): example is GrammarExample & { pattern: NonNullable<GrammarExample['pattern']> } => Boolean(example.pattern))
  if (patterned.length > 0) {
    const counts = new Map<string, number>()
    for (const example of patterned) counts.set(example.pattern, (counts.get(example.pattern) ?? 0) + 1)
    const summaryLine = [...counts.entries()].map(([pattern, count]) => `${pattern}×${count}`).join(' / ')
    add({
      id: `${lesson.id}:pattern:all`,
      intent: 'pattern',
      subject: '文型',
      ...renderQa(PHRASINGS.patternGeneric, {}, patterned.flatMap((example) => [example.en, ...englishWords(example.en)])),
      answer: {
        lead: `このセクションの例文の文型は ${summaryLine}。代表的な文で見てみよう。`,
        quotes: patterned
          .slice(0, 3)
          .map((example) => ({ label: example.pattern, en: example.en, ja: example.ja, note: example.patternNote })),
        followups: ['構造を分解して', 'まとめを教えて'],
      },
      priority: 8,
    })
  }

  // カリキュラム用語のQA。
  // 「三単現」「現在完了」のような一語の質問(曖昧な入力)にも、その用語を説明している段落で答える。
  const termParagraphs: Array<{ label: string; text: string }> = []
  for (const block of lesson.blocks) {
    if (block.type !== 'explanation') continue
    for (const paragraph of splitParagraphs(block.body)) {
      termParagraphs.push({ label: block.title ?? '解説', text: paragraph })
    }
  }
  for (const line of lesson.summary) termParagraphs.push({ label: 'まとめ', text: line })
  const lessonOutline = [lesson.title, lesson.objective, ...lesson.summary].join('\n')
  for (const term of CURRICULUM_TERMS) {
    const needle = term.toLowerCase()
    const inOutline = lessonOutline.toLowerCase().includes(needle)
    const scored = termParagraphs
      .map((paragraph) => ({
        paragraph,
        // 見出しに用語がある段落は、その用語を説明している段落とみなして強く優先する
        score: countOccurrences(paragraph.text.toLowerCase(), needle) * 2 + (paragraph.label.toLowerCase().includes(needle) ? 3 : 0),
      }))
      .filter((row) => row.score > 0)
      .sort((a, b) => b.score - a.score)
    const best = scored[0]
    if (!best && !inOutline) continue
    // 本文に無くてもタイトル・目標に現れる用語は、目標を引用して名前だけでも答える
    const quote: { label: string; text: string } = best
      ? { label: best.paragraph.label, text: best.paragraph.text }
      : { label: 'このセクションの目標', text: lesson.objective }
    add({
      id: `${lesson.id}:termqa:${term}`,
      intent: 'concept',
      subject: term,
      ...renderQa(PHRASINGS.vagueTerm, { term }, [term]),
      answer: {
        lead: `「${term}」だね。このセクションではこう説明しているよ。`,
        quotes: [quote],
        followups: ['例文を教えて', 'まとめを教えて', 'クイズのヒントをちょうだい'],
      },
      priority: 9,
    })
    // 用語を使った例文(「現在完了の例文は?」)は、説明段落の英単語と重なる例文を引く
    const relatedWords = new Set(englishWords(quote.text))
    const samples = allExamples
      .filter((item) => englishWords(item.en).some((word) => relatedWords.has(word)))
      .slice(0, 3)
    add({
      id: `${lesson.id}:term-examples:${term}`,
      intent: 'example',
      subject: term,
      ...renderQa(PHRASINGS.termExamples, { term }, [term]),
      answer: {
        lead: samples.length > 0 ? `「${term}」に関係する例文だよ。` : 'このセクションの例文だよ。',
        quotes: (samples.length > 0 ? samples : allExamples.slice(0, 2)).map((item) => exampleQuote(item)),
        followups: ['違いをまとめて', 'まとめを教えて'],
      },
      priority: 8,
    })
  }

  // 活用形のQA(本文の「study → studies」のような変化を拾い、形を聞けるようにする)
  const formPairs = new Map<string, { left: string; right: string; paragraph: { label: string; text: string } }>()
  for (const paragraph of termParagraphs) {
    for (const match of paragraph.text.matchAll(/\b([A-Za-z][A-Za-z']*)\s*(?:→|->)\s*([A-Za-z][A-Za-z']*)\b/g)) {
      const key = `${match[1].toLowerCase()}=>${match[2].toLowerCase()}`
      if (!formPairs.has(key)) formPairs.set(key, { left: match[1], right: match[2], paragraph })
    }
  }
  let formIndex = 0
  for (const { left, right, paragraph } of formPairs.values()) {
    formIndex += 1
    add({
      id: `${lesson.id}:form:${formIndex}`,
      intent: 'concept',
      subject: left,
      ...renderQa(PHRASINGS.form, { left, right, topic }, [
        paragraph.text,
        paragraph.label,
        right,
        left,
        ...englishWords(paragraph.text),
      ]),
      answer: {
        lead: `${left} は ${right} に変わるよ。`,
        quotes: [{ label: paragraph.label, text: paragraph.text }],
        followups: ['なぜ変わるの?', 'まとめを教えて'],
      },
      priority: 9,
    })
  }

  // 同じ段落で一緒に説明される用語どうしの違い(対比ブロックが無いセクションでも比較に答える)
  const paired = new Set<string>()
  let pairCount = 0
  for (const paragraph of termParagraphs) {
    if (pairCount >= 12) break
    if (paragraph.label === 'まとめ') continue
    const present = CURRICULUM_TERMS.filter((term) => paragraph.text.toLowerCase().includes(term.toLowerCase()))
      .sort((a, b) => b.length - a.length)
      .slice(0, 4)
    for (let a = 0; a < present.length && pairCount < 12; a += 1) {
      for (let b = a + 1; b < present.length && pairCount < 12; b += 1) {
        const left = present[a]
        const right = present[b]
        if (left.includes(right) || right.includes(left)) continue
        const key = `${left}|${right}`
        if (paired.has(key)) continue
        paired.add(key)
        pairCount += 1
        add({
          id: `${lesson.id}:termpair:${pairCount}`,
          intent: 'difference',
          subject: `${left} ${right}`,
          ...renderQa(PHRASINGS.difference, { left, right }),
          answer: {
            lead: `${left} と ${right} だね。このセクションでは、この段落で一緒に説明しているよ。`,
            quotes: [{ label: paragraph.label, text: paragraph.text }],
            followups: ['例文を教えて', 'まとめを教えて'],
          },
          priority: 7,
        })
      }
    }
  }

  // あいさつ・お礼・機能説明(セクションに依存しない)
  add({
    id: 'smalltalk:greeting',
    intent: 'greeting',
    ...renderQa(PHRASINGS.greeting, {}),
    answer: { lead: GREETING_LEAD, quotes: [], followups: defaultFollowups.slice(0, 3) },
    priority: 10,
  })
  add({
    id: 'smalltalk:thanks',
    intent: 'greeting',
    ...renderQa(PHRASINGS.thanks, {}),
    answer: { lead: THANKS_LEAD, quotes: [], followups: [] },
    priority: 10,
  })
  add({
    id: 'smalltalk:capability',
    intent: 'capability',
    ...renderQa(PHRASINGS.capability, {}),
    answer: { lead: CAPABILITY_LEAD, quotes: [], followups: defaultFollowups },
    priority: 10,
  })

  return entries
}

/** QAの意図(intent)だけを取り出す(テスト・集計用)。 */
export function intentsOf(entries: readonly QaEntry[]): Map<QaIntent, number> {
  const counts = new Map<QaIntent, number>()
  for (const entry of entries) counts.set(entry.intent, (counts.get(entry.intent) ?? 0) + 1)
  return counts
}
