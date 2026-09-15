// コンテンツデータセットの自動検証。
// 重複・欠損・不正な参照(highlight が en に含まれない等)を機械的に検出する。

import { describe, expect, it } from 'vitest'
import { allLessons, grammarUnits } from './grammar'
import { EXAMPLES_PER_LESSON, lessonExpansions } from './grammar/expansions'
import { PATTERN_FOCUS_TITLE, examplePatterns } from './grammar/patterns'
import { lessonIllustrations } from './grammar/illustrations'
import { grammarRoadmap } from './grammar/roadmap'
import {
  lessonStructures,
  patternAnimations,
  patternBlocks,
  patternExamples,
  patternQuiz,
  patternShowcases,
  roleBlocks,
  roleExampleSentence,
  roleGuides,
  skeletonAnimation,
  wordOrderAnimation,
  wordOrderBlocks,
  wordOrderExamples,
  wordOrderQuiz,
} from './grammar/structures'
import { PATTERN_LABELS, PATTERN_ORDER } from './grammar/patterns/types'
import { ROLE_LABELS, ROLE_MEANINGS, ROLE_ORDER } from './grammar/structures/roles'
import { ILLUSTRATIONS } from './illustrations'
import { allVocabulary } from './vocabulary'
import { ipaEntries, minimalPairs, pronunciationTopics } from './pronunciation/data'
import { readingPassages } from './reading'
import { canDoDescriptors } from './cando'
import { basicWords } from './basicWords'
import {
  REQUIRED_QUIZ_COUNT,
  checkAudioText,
  checkExampleLength,
  checkPassage,
  checkQuestion,
  findNearDuplicates,
  unknownWordRatio,
} from './validation'
import { canDoCoverage, grammarLessonSummaries, readingPassageCount, vocabularyCount } from './summary'
import type { BreakdownPart, GrammarExample, LessonBlock, QuizQuestion, SentencePattern } from './types'

const PATTERN_SET = new Set<SentencePattern>(PATTERN_ORDER)
const ROLE_SET = new Set(ROLE_ORDER)

/** 構造図の区画が英文を過不足なく分けているか(区画を連結すると元の英文に戻るか)。 */
function checkBreakdownParts(parts: BreakdownPart[], sentence: string, where: string): void {
  expect(parts.length, `${where}: 区画の数`).toBeGreaterThan(1)
  expect(parts.map((part) => part.text).join(' '), `${where}: 区画の連結`).toBe(sentence)
  for (const part of parts) {
    expect(ROLE_SET.has(part.role), `${where}: ${part.text} / ${part.role}`).toBe(true)
    expect(part.text.trim().length, `${where}: 空の区画`).toBeGreaterThan(0)
  }
}

/** breakdown / expansion のブロックを検査する。使えるブロック種別をここで限定する。 */
function checkStructureBlock(block: LessonBlock, where: string, patterns: SentencePattern[]): void {
  switch (block.type) {
    case 'breakdown':
      expect(checkAudioText(block.sentence, `${where}:${block.title ?? ''}`), block.sentence).toEqual([])
      checkBreakdownParts(block.parts, block.sentence, `${where}:${block.sentence}`)
      if (block.pattern) patterns.push(block.pattern)
      if (block.skeleton) {
        expect(checkAudioText(block.skeleton, `${where}:骨格`), block.skeleton).toEqual([])
      }
      if (block.skeletonPattern) patterns.push(block.skeletonPattern)
      // 骨格は修飾語(M)を外した形なので、骨格があるなら文型も付ける。
      if (block.skeletonPattern && !block.pattern) {
        expect(block.skeleton, `${where}: 骨格のある文型`).toBeTruthy()
      }
      break
    case 'expansion':
      expect(block.steps.length, `${where}: 段階の数`).toBeGreaterThan(1)
      for (const step of block.steps) {
        expect(checkAudioText(step.en, `${where}:${step.en}`), step.en).toEqual([])
        expect(step.ja?.length, `${where}: ${step.en} の和訳`).toBeGreaterThan(0)
        // focus は強調表示に使うため、対象の英文に実在する部分文字列でなければならない。
        if (step.focus) {
          expect(step.en.includes(step.focus), `${where}: ${step.en} / ${step.focus}`).toBe(true)
        }
      }
      break
    default:
      throw new Error(`${where}: 構造データに使えないブロック種別です(${block.type})`)
  }
  for (const pattern of patterns) expect(PATTERN_SET.has(pattern), `${where}: ${pattern}`).toBe(true)
}

/** 例文1文の検査(文型バッジ・注記・ハイライト)。 */
function checkExample(example: GrammarExample, where: string): void {
  expect(example.ja?.length, `${where} の和訳`).toBeGreaterThan(0)
  expect(example.pattern, `${where} の文型`).toBeTruthy()
  expect(PATTERN_SET.has(example.pattern!), `${where}: ${example.pattern}`).toBe(true)
  expect(example.patternNote?.length, `${where} の文型注記`).toBeGreaterThan(0)
  if (example.highlight) {
    expect(example.en.includes(example.highlight), `${where}: ${example.highlight}`).toBe(true)
  }
}

/** 選択問題の検査(構造検査 + 音声 + 記録先のID衝突なし)。 */
function checkQuiz(questions: readonly QuizQuestion[], where: string): void {
  const lessonQuizIds = new Set(allLessons.flatMap((lesson) => lesson.quiz.map((q) => q.id)))
  const ids: string[] = []
  for (const question of questions) {
    ids.push(question.id)
    expect(checkQuestion(question, where), `${where}: ${question.id}`).toEqual([])
    expect(question.audioEn, question.id).toBeTruthy()
    expect(lessonQuizIds.has(question.id), `${question.id} がレッスンのクイズIDと衝突`).toBe(false)
  }
  expect(new Set(ids).size, `${where}: 問題IDの重複`).toBe(ids.length)
}

describe('ダッシュボード用サマリーの検証', () => {
  // summary.ts はホームが教材本体を読み込まないための生成ファイル。
  // ズレたら npm run summary で再生成する。
  it('文法サマリーが全レッスンと一致する', () => {
    expect(grammarLessonSummaries).toEqual(
      allLessons.map(({ id, title, minutes }) => ({ id, title, minutes })),
    )
  })

  it('語彙件数が実データと一致する', () => {
    expect(vocabularyCount).toBe(allVocabulary.length)
  })

  it('多読の件数が実データと一致する', () => {
    expect(readingPassageCount).toBe(readingPassages.length)
  })
})

describe('生成コンテンツの検証ハーネス', () => {
  // 教師レビューを行わないため、機械的に落とせる欠陥はここで全部落とす。
  it('全多読本文が構造・レベル・音声適合の検査を通る', () => {
    for (const passage of readingPassages) {
      expect(checkPassage(passage), passage.id).toEqual([])
    }
  })

  it('多読本文どうしが内容重複していない', () => {
    const issues = findNearDuplicates(
      readingPassages.map((p) => ({ id: p.id, text: p.paragraphs.join(' ') })),
    )
    expect(issues).toEqual([])
  })

  it('多読本文の未習語率が1割未満に収まる', () => {
    // 既習 = 4,500見出し語 + A1相当の基本語
    const known = new Set<string>(basicWords)
    for (const entry of allVocabulary) known.add(entry.word.toLowerCase())
    for (const passage of readingPassages) {
      const ratio = unknownWordRatio(passage.paragraphs.join(' '), known)
      expect(ratio, `${passage.id} の未習語率`).toBeLessThan(0.1)
    }
  })

  it('can-do 記述子IDの参照がすべて解決する', () => {
    const ids = new Set(canDoDescriptors.map((d) => d.id))
    for (const passage of readingPassages) {
      for (const id of passage.canDo) expect(ids.has(id), `${passage.id} → ${id}`).toBe(true)
    }
    for (const id of Object.keys(canDoCoverage)) expect(ids.has(id), id).toBe(true)
  })

  it('すべての can-do 記述子に対応コンテンツがある', () => {
    const uncovered = canDoDescriptors.filter((d) => (canDoCoverage[d.id] ?? 0) === 0)
    expect(uncovered.map((d) => d.id)).toEqual([])
  })
})

describe('文法コンテンツの検証', () => {
  it('レッスンIDが一意である', () => {
    const ids = allLessons.map((l) => l.id)
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('ユニットIDが一意である', () => {
    const ids = grammarUnits.map((u) => u.id)
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('全レッスンが15分以内・クイズとまとめを持つ', () => {
    expect(grammarUnits).toHaveLength(33)
    expect(allLessons).toHaveLength(116)
    for (const lesson of allLessons) {
      expect(lesson.minutes, lesson.id).toBeGreaterThanOrEqual(3)
      expect(lesson.minutes, lesson.id).toBeLessThanOrEqual(15)
      expect(lesson.quiz.length, `${lesson.id} のクイズ`).toBe(REQUIRED_QUIZ_COUNT[lesson.level])
      expect(lesson.summary.length, `${lesson.id} のまとめ`).toBeGreaterThanOrEqual(2)
      expect(lesson.summary.length, `${lesson.id} のまとめ`).toBeLessThanOrEqual(5)
      expect(lesson.blocks.length, `${lesson.id} のブロック`).toBeGreaterThanOrEqual(3)
    }
  })

  it('全レッスンが十分な音声付き例文と意味のある視覚ブロックを持つ', () => {
    for (const lesson of allLessons) {
      const examples = lesson.blocks.find((block) => block.type === 'examples')
      expect(examples?.type, `${lesson.id}: 例文ブロック`).toBe('examples')
      if (examples?.type === 'examples') {
        // 10文にそろえる。この10文がそのままセクション内の並べ替え10問の母集団になる。
        expect(examples.items.length, `${lesson.id}: 例文数`).toBe(EXAMPLES_PER_LESSON)
        expect(new Set(examples.items.map((item) => item.en.toLowerCase())).size, `${lesson.id}: 例文の重複`).toBe(
          EXAMPLES_PER_LESSON,
        )
        for (const example of examples.items) {
          expect(example.en.trim().split(/\s+/).length, `${lesson.id}: ${example.en} の語数`).toBeGreaterThanOrEqual(4)
          expect(example.ja?.length, `${lesson.id}: ${example.en} の和訳`).toBeGreaterThan(0)
          expect(/[.!?]$/.test(example.en), `${lesson.id}: ${example.en}`).toBe(true)
        }
        // 多読と同じ考え方で、文法例文にもレベル逸脱の検査をかける(上限ではなく下限)。
        expect(checkExampleLength(lesson.level, examples.items, lesson.id)).toEqual([])
      }
      expect(
        lesson.blocks.some((block) => ['timeline', 'contrast', 'structure'].includes(block.type)),
        `${lesson.id}: 図解(タイムライン・対比・構造図)`,
      ).toBe(true)
    }
  })

  it('全118レッスンに補強解説と追加例文3つがある', () => {
    const lessonIds = allLessons.map((lesson) => lesson.id).sort()
    const expansionIds = Object.keys(lessonExpansions).sort()
    expect(expansionIds).toEqual(lessonIds)
    for (const expansion of Object.values(lessonExpansions)) {
      expect(expansion.explanationTitle.length).toBeGreaterThan(0)
      expect(expansion.explanationBody.length).toBeGreaterThan(100)
      expect(expansion.examples).toHaveLength(3)
      for (const example of expansion.examples) {
        expect(example.ja?.length).toBeGreaterThan(0)
        expect(checkAudioText(example.en, example.en)).toEqual([])
      }
    }
  })

  it('全レッスンに挿絵が1つあり、ラベル本数が図の仕様と一致する', () => {
    const lessonIds = allLessons.map((lesson) => lesson.id).sort()
    expect(Object.keys(lessonIllustrations).sort()).toEqual(lessonIds)

    for (const [id, illustration] of Object.entries(lessonIllustrations)) {
      const spec = ILLUSTRATIONS[illustration.kind]
      expect(spec, `${id}: 未知の図 ${illustration.kind}`).toBeTruthy()
      expect(illustration.labels.length, `${id}: ${illustration.kind} のラベル本数`).toBe(spec.labels)
      for (const label of illustration.labels) {
        expect(label.trim().length, `${id}: 空のラベル`).toBeGreaterThan(0)
      }
      expect(illustration.caption.length, `${id}: 図の説明文`).toBeGreaterThan(10)
    }

    for (const lesson of allLessons) {
      const found = lesson.blocks.filter((block) => block.type === 'illustration')
      expect(found.length, `${lesson.id}: 挿絵ブロック`).toBe(1)
      expect(found[0]?.type === 'illustration' ? found[0].sceneId : undefined, `${lesson.id}: 専用シーンID`).toBe(lesson.id)
      expect(found[0]?.type === 'illustration' ? found[0].alt.length : 0, `${lesson.id}: 個別alt`).toBeGreaterThan(20)
    }
  })

  it('前提レッスンが実在し、必ず自分より前に置かれている', () => {
    const order = new Map(allLessons.map((lesson, index) => [lesson.id, index]))
    for (const lesson of allLessons) {
      for (const prereq of lesson.prereqs ?? []) {
        expect(order.has(prereq), `${lesson.id} の前提 ${prereq}`).toBe(true)
        expect(order.get(prereq)!, `${lesson.id} の前提 ${prereq} の順序`).toBeLessThan(order.get(lesson.id)!)
      }
    }
  })

  it('全クイズが構造検査(選択肢・正解位置・誤答注記・音声)を通る', () => {
    for (const lesson of allLessons) {
      for (const question of lesson.quiz) {
        expect(checkQuestion(question, lesson.id), question.id).toEqual([])
        expect(question.audioEn, question.id).toBeTruthy()
      }
    }
  })

  it('クイズIDが全体で一意である', () => {
    const ids = allLessons.flatMap((lesson) => lesson.quiz.map((q) => q.id))
    expect(new Set(ids).size).toBe(ids.length)
  })

  it('ハイライトは対象の英文に実在する部分文字列である', () => {
    for (const lesson of allLessons) {
      for (const block of lesson.blocks) {
        const items =
          block.type === 'examples'
            ? block.items
            : block.type === 'contrast'
              ? [...block.left.items, ...block.right.items]
              : []
        for (const item of items) {
          if (item.highlight) {
            expect(item.en.includes(item.highlight), `${lesson.id}: ${item.en} / ${item.highlight}`).toBe(true)
          }
        }
      }
    }
  })
})

describe('5文型の検証', () => {
  const PATTERNS = new Set(['SV', 'SVC', 'SVO', 'SVOO', 'SVOC'])

  it('文型表の全エントリが有効な文型と注記を持つ', () => {
    for (const [en, entry] of Object.entries(examplePatterns)) {
      expect(PATTERNS.has(entry.pattern), `${en}: ${entry.pattern}`).toBe(true)
      expect(entry.note.length, `${en} の注記`).toBeGreaterThan(0)
    }
  })

  it('全例文と対比の英文に文型と注記が付く', () => {
    for (const lesson of allLessons) {
      for (const block of lesson.blocks) {
        const items =
          block.type === 'examples'
            ? block.items
            : block.type === 'contrast'
              ? [...block.left.items, ...block.right.items]
              : []
        for (const item of items) {
          expect(item.pattern, `${lesson.id}: ${item.en}`).toBeTruthy()
          expect(PATTERNS.has(item.pattern!), `${lesson.id}: ${item.en} / ${item.pattern}`).toBe(true)
          expect(item.patternNote?.length, `${lesson.id}: ${item.en} の文型注記`).toBeGreaterThan(0)
        }
      }
    }
  })

  it('各レッスンに「文型の視点」ブロックが1つある', () => {
    for (const lesson of allLessons) {
      const focusBlocks = lesson.blocks.filter(
        (block) => block.type === 'explanation' && block.title === PATTERN_FOCUS_TITLE,
      )
      expect(focusBlocks.length, `${lesson.id} の文型の視点`).toBe(1)
      if (focusBlocks[0]?.type === 'explanation') {
        expect(focusBlocks[0].body.length, `${lesson.id} の文型の視点の本文`).toBeGreaterThan(20)
      }
    }
  })
})

describe('英文の構造データの検証', () => {
  it('構造データの参照先レッスンが実在し、差し込み後も本文が残っている', () => {
    const lessonIds = new Set(allLessons.map((lesson) => lesson.id))
    for (const id of Object.keys(lessonStructures)) {
      expect(lessonIds.has(id), `構造データの参照先 ${id}`).toBe(true)
    }

    for (const lesson of allLessons) {
      const structure = lessonStructures[lesson.id]
      if (!structure) continue
      // 差し込み後も「文型の視点」は1つだけ・元の例文10文もそのまま残る。
      const focus = lesson.blocks.filter((block) => block.type === 'explanation' && block.title === PATTERN_FOCUS_TITLE)
      expect(focus.length, `${lesson.id}: 差し込み後の文型の視点`).toBe(1)
      const examples = lesson.blocks.filter((block) => block.type === 'examples')
      expect(examples[0]?.type === 'examples' ? examples[0].items.length : 0, `${lesson.id}: 例文数`).toBe(
        EXAMPLES_PER_LESSON,
      )
      for (const block of structure.blocks) {
        checkStructureBlock(block, lesson.id, [])
      }
    }
  })

  it('構造データの追加問題が構造検査(選択肢・正解位置・誤答注記・音声)を通る', () => {
    const ids: string[] = []
    for (const [lessonId, structure] of Object.entries(lessonStructures)) {
      for (const question of structure.quiz ?? []) {
        ids.push(question.id)
        const issues = checkQuestion(question, lessonId)
        expect(issues, `${lessonId}: ${question.id}`).toEqual([])
        expect(question.audioEn, question.id).toBeTruthy()
      }
    }
    expect(ids.length, '構造チェック問題の総数').toBeGreaterThan(0)
    // 既存の理解度チェックと同じ記録先(選択問題の正誤)に乗るため、IDは全体で一意にする。
    expect(new Set(ids).size, '構造チェック問題IDの重複').toBe(ids.length)
    const lessonQuizIds = new Set(allLessons.flatMap((lesson) => lesson.quiz.map((q) => q.id)))
    for (const id of ids) expect(lessonQuizIds.has(id), `${id} が既存クイズと衝突`).toBe(false)
  })

  it('学習導線の各ステップが既存セクションを指し、番号が1から連番になっている', () => {
    const lessonIds = new Set(allLessons.map((lesson) => lesson.id))
    expect(grammarRoadmap.length).toBeGreaterThanOrEqual(7)
    grammarRoadmap.forEach((step, index) => {
      expect(step.number, `${step.id} の番号`).toBe(index + 1)
      expect(step.title.length, step.id).toBeGreaterThan(0)
      expect(step.lead.length, `${step.id} の導入文`).toBeGreaterThan(20)
      expect(step.points.length, `${step.id} の到達点`).toBeGreaterThanOrEqual(2)
      expect(step.lessonIds.length, `${step.id} のリンク`).toBeGreaterThan(0)
      for (const id of step.lessonIds) expect(lessonIds.has(id), `${step.id} → ${id}`).toBe(true)
      for (const block of step.blocks ?? []) checkStructureBlock(block, step.id, [])
    })
  })

  it('構造図で使う役割の凡例がすべて定義されている', () => {
    for (const role of ROLE_ORDER) {
      expect(ROLE_MEANINGS[role]?.length, role).toBeGreaterThan(0)
    }
    // S / V / O / C が骨格、M が修飾語。凡例の順序を固定する。
    expect(ROLE_ORDER).toEqual(['S', 'V', 'O', 'C', 'M'])
  })

  it('全レッスンの構造図が表示できる形になっている', () => {
    // UIがブロック種別ごとに描画するため、未知の種別が混ざると何も出ないまま終わる。
    const renderable = new Set(['breakdown', 'expansion'])
    for (const lesson of allLessons) {
      for (const block of lesson.blocks) {
        if (block.type === 'breakdown' || block.type === 'expansion') {
          expect(renderable.has(block.type), `${lesson.id}: ${block.type}`).toBe(true)
          checkStructureBlock(block, lesson.id, [])
        }
      }
    }
  })

  it('構造図の文型ラベルが5文型の表記でそろう', () => {
    // バッジは PATTERN_LABELS の短い名称を出すため、未定義の文型があると読み上げも崩れる。
    for (const lesson of allLessons) {
      for (const block of lesson.blocks) {
        if (block.type !== 'breakdown') continue
        for (const pattern of [block.pattern, block.skeletonPattern]) {
          if (pattern) expect(PATTERN_LABELS[pattern], `${lesson.id}: ${pattern}`).toBeTruthy()
        }
      }
    }
  })
})

describe('英文の作られ方ページの検証', () => {
  // 旧 u01-l4(英語の語順 SVO)と旧 u01-l5(5文型)を統合したページの内容。
  // レッスンではないため lesson の合成を通らず、文型バッジはデータ側で付けている。
  const GUIDE_BLOCK_TYPES = new Set(['explanation', 'examples', 'structure', 'contrast', 'breakdown', 'expansion'])

  function checkGuideBlock(block: LessonBlock, where: string): void {
    expect(GUIDE_BLOCK_TYPES.has(block.type), `${where}: 未知のブロック種別 ${block.type}`).toBe(true)
    switch (block.type) {
      case 'breakdown':
      case 'expansion':
        checkStructureBlock(block, where, [])
        break
      case 'explanation':
        expect(block.body.length, `${where} の本文`).toBeGreaterThan(20)
        break
      case 'examples':
        for (const item of block.items) checkExample(item, `${where}: ${item.en}`)
        break
      case 'contrast':
        for (const item of [...block.left.items, ...block.right.items]) checkExample(item, `${where}: ${item.en}`)
        break
      default:
        break
    }
  }

  it('統合した2セクションがレッスンから削除されている', () => {
    // 内容はページへ移したので、カリキュラムには残さない。
    const ids = new Set(allLessons.map((lesson) => lesson.id))
    expect(ids.has('u01-l4')).toBe(false)
    expect(ids.has('u01-l5')).toBe(false)
    expect(ids.has('u01-l3')).toBe(true)
  })

  it('S / V / O / C / M の意味をページの先頭で説明している', () => {
    expect(new Set(roleGuides.map((guide) => guide.role))).toEqual(new Set(ROLE_ORDER))
    expect(roleGuides.length).toBe(5)
    for (const guide of roleGuides) {
      expect(ROLE_LABELS[guide.role]?.length, guide.role).toBeGreaterThan(0)
      expect(ROLE_MEANINGS[guide.role]?.length, guide.role).toBeGreaterThan(0)
      expect(guide.note.length, `${guide.role} の説明`).toBeGreaterThan(10)
      // 例は、その役割を実際に担っている語句を英文から抜き出したもの。
      // O は2つあるので「me / a book」のように並べて示す。
      for (const part of guide.example.split(' / ')) {
        expect(guide.sentence.includes(part), `${guide.role}: ${part}`).toBe(true)
      }
    }
    expect(roleExampleSentence).toContain('gave')
  })

  it('ページの本文ブロックが構造検査を通る', () => {
    for (const block of [roleBlocks, wordOrderBlocks, patternBlocks]) {
      for (const item of block) checkGuideBlock(item, item.type)
    }
  })

  it('語順と5文型の例文が、文型バッジと注記を持って並ぶ', () => {
    expect(wordOrderExamples.length).toBeGreaterThanOrEqual(10)
    expect(patternExamples.length).toBeGreaterThanOrEqual(10)
    for (const example of [...wordOrderExamples, ...patternExamples]) checkExample(example, example.en)
    // 5文型の例文は SV / SVC / SVO / SVOO / SVOC を網羅する。
    const covered = new Set(patternExamples.map((example) => example.pattern))
    expect(covered).toEqual(new Set(PATTERN_ORDER))
  })

  it('5文型それぞれに、代表例と図解用の2Dアニメーションがある', () => {
    expect(patternShowcases.map((showcase) => showcase.pattern)).toEqual(PATTERN_ORDER)
    for (const showcase of patternShowcases) {
      expect(showcase.skeleton.length, showcase.pattern).toBeGreaterThan(0)
      expect(showcase.example.ja.length, showcase.pattern).toBeGreaterThan(0)
      expect(showcase.example.note.length, `${showcase.pattern} の説明`).toBeGreaterThan(10)
    }
    // アニメーションは全5文型にあり、既存のレッスン挿絵と同じ3段階の形式で作る。
    expect(Object.keys(patternAnimations).sort()).toEqual([...PATTERN_ORDER].sort())
    for (const [pattern, animation] of Object.entries(patternAnimations)) {
      expect(animation.title.length, pattern).toBeGreaterThan(0)
      expect(animation.mode, pattern).toBe('sentence')
      expect(animation.steps, pattern).toHaveLength(3)
      for (const step of animation.steps) {
        expect(step.sentence.includes('|'), `${pattern}: ${step.sentence}`).toBe(true)
        expect(step.note.length, `${pattern} の注記`).toBeGreaterThan(5)
      }
    }
    for (const animation of [wordOrderAnimation, skeletonAnimation]) {
      expect(animation.steps).toHaveLength(3)
      for (const step of animation.steps) {
        expect(step.sentence.includes('|'), step.sentence).toBe(true)
        expect(step.note.length).toBeGreaterThan(5)
      }
    }
  })

  it('統合した理解度チェックが構造検査を通る', () => {
    // 旧セクションの問題(IDを roadmap-* に付け替え)を削らずに引き継ぐ。
    expect(wordOrderQuiz.length).toBeGreaterThanOrEqual(8)
    expect(patternQuiz.length).toBeGreaterThanOrEqual(8)
    checkQuiz(wordOrderQuiz, 'roadmap-page')
    checkQuiz(patternQuiz, 'roadmap-page')
  })
})

describe('語彙データセットの検証', () => {
  // B2到達には6,500〜7,500語が要る。4,500語から増補し、8,000語で区切りとした。
  // 語を足したらこの数も一緒に上げる(減っていないことを見張るための数)。
  it('見出し語がそろい、IDと見出し語が一意である', () => {
    expect(allVocabulary).toHaveLength(8000)
    expect(new Set(allVocabulary.map((e) => e.id)).size).toBe(allVocabulary.length)
    expect(new Set(allVocabulary.map((e) => e.word.toLowerCase())).size).toBe(allVocabulary.length)
  })

  it('必須項目が欠けていない', () => {
    for (const entry of allVocabulary) {
      expect(entry.word.length, entry.id).toBeGreaterThan(0)
      expect(entry.partOfSpeech.length, entry.id).toBeGreaterThan(0)
      expect(entry.meaningsJa.length, entry.id).toBeGreaterThan(0)
      expect(entry.exampleSentence.length, entry.id).toBeGreaterThan(0)
      expect(entry.exampleTranslationJa.length, entry.id).toBeGreaterThan(0)
      expect(['A2', 'B1', 'B2'], entry.id).toContain(entry.level)
    }
  })

  it('発音がIPA表記になっている', () => {
    for (const entry of allVocabulary) {
      expect(/^\/.+\/$/.test(entry.pronunciation), `${entry.id}: ${entry.pronunciation}`).toBe(true)
    }
  })

  it('例文が見出し語を含み、TTSに渡せる形式である', () => {
    for (const entry of allVocabulary) {
      // 語形変化(buried など)を許容するため、語幹の前方一致で見る
      const head = entry.word.toLowerCase().split(' ')[0]
      const stem = head.slice(0, Math.max(3, head.length - 3))
      expect(entry.exampleSentence.toLowerCase().includes(stem), `${entry.id}: ${entry.exampleSentence}`).toBe(true)
      expect(checkAudioText(entry.exampleSentence, entry.id)).toEqual([])
    }
  })

  it('外部出典の例文にはライセンスとリンクが付く', () => {
    for (const entry of allVocabulary) {
      if (!entry.exampleSource) continue
      expect(entry.exampleSource.name.length, entry.id).toBeGreaterThan(0)
      expect(entry.exampleSource.license.length, entry.id).toBeGreaterThan(0)
      expect(entry.exampleSource.url.startsWith('http'), entry.id).toBe(true)
    }
  })

  it('全語に「覚えるヒント」がある', () => {
    for (const entry of allVocabulary) {
      expect(entry.mnemonic?.length, entry.id).toBeGreaterThan(0)
    }
  })

  it('全語にコロケーションがあり、少なくとも1件が見出し語を含む', () => {
    for (const entry of allVocabulary) {
      expect(entry.collocations?.length, entry.id).toBeGreaterThan(0)
      // 行ごと別の語から取り違える事故を落とす。be laid off のような不規則形を含む言い回しは
      // 残したいので、全件ではなく「1件以上が見出し語を含む」を条件にする。
      // 新規に書き足す分は scripts/collocations.mjs が全件に見出し語を要求する。
      const head = entry.word.toLowerCase().split(' ')[0]
      const stem = head.slice(0, Math.max(3, head.length - 3))
      const hit = entry.collocations!.some((collocation) => collocation.toLowerCase().includes(stem))
      expect(hit, `${entry.id}: ${entry.collocations!.join(' / ')}`).toBe(true)
    }
  })
})

describe('発音コンテンツの検証', () => {
  it('IPA項目が一意で、例語と説明を持つ', () => {
    expect(new Set(ipaEntries.map((e) => e.symbol)).size).toBe(ipaEntries.length)
    for (const entry of ipaEntries) {
      expect(entry.examples.length, entry.symbol).toBeGreaterThanOrEqual(2)
      expect(entry.ja.length, entry.symbol).toBeGreaterThan(0)
      expect(entry.tip.length, entry.symbol).toBeGreaterThan(0)
      expect(['vowel', 'diphthong', 'consonant'], entry.symbol).toContain(entry.type)
    }
  })

  it('最小対が対になる2語とコツを持つ', () => {
    expect(minimalPairs.length).toBeGreaterThanOrEqual(13)
    for (const pair of minimalPairs) {
      expect(pair.a.word).not.toBe(pair.b.word)
      expect(pair.a.ipa.length, pair.a.word).toBeGreaterThan(0)
      expect(pair.b.ipa.length, pair.b.word).toBeGreaterThan(0)
      expect(pair.tip.length, pair.focus).toBeGreaterThan(0)
    }
  })

  it('発音トピックが本文と例文を持つ', () => {
    expect(new Set(pronunciationTopics.map((t) => t.id)).size).toBe(pronunciationTopics.length)
    for (const topic of pronunciationTopics) {
      expect(topic.body.length, topic.id).toBeGreaterThan(50)
      expect(topic.examples.length, topic.id).toBeGreaterThanOrEqual(2)
      for (const example of topic.examples) {
        expect(checkAudioText(example.en, topic.id)).toEqual([])
      }
    }
  })
})
