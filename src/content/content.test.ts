// コンテンツデータセットの自動検証。
// 重複・欠損・不正な参照(highlight が en に含まれない等)を機械的に検出する。

import { describe, expect, it } from 'vitest'
import { allLessons, grammarUnits } from './grammar'
import { EXAMPLES_PER_LESSON, lessonExpansions } from './grammar/expansions'
import { PATTERN_FOCUS_TITLE, examplePatterns } from './grammar/patterns'
import { lessonIllustrations } from './grammar/illustrations'
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
    expect(allLessons).toHaveLength(118)
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
