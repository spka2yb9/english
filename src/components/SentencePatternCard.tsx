import type { LessonAnimation } from '../content/grammar/animations'
import { PATTERN_LABELS } from '../content/grammar/patterns/types'
import type { PatternShowcase } from '../content/grammar/structures'
import { EnglishExample } from './EnglishExample'
import { GrammarAnimation } from './GrammarAnimation'

/** 5文型を1つずつ見せるカード。2Dアニメーションと代表例を上下に並べる。 */
export function SentencePatternCard({ showcase, animation }: { showcase: PatternShowcase; animation: LessonAnimation }) {
  return (
    <article className="pattern-card">
      <div className="pattern-card-head">
        <span className="pattern-card-name">{PATTERN_LABELS[showcase.pattern]}</span>
        <span className="pattern-card-skeleton">
          骨組み <span lang="en">{showcase.skeleton}</span>
        </span>
      </div>

      <GrammarAnimation sceneId={`pattern-${showcase.pattern}`} animation={animation} />

      <EnglishExample
        text={showcase.example.en}
        translation={showcase.example.ja}
        pattern={showcase.pattern}
        note={showcase.example.note}
      />
      {showcase.relation && (
        <p className="pattern-card-relation">
          <span className="breakdown-label">意味の関係</span>
          <span lang="en">{showcase.relation}</span>
        </p>
      )}
    </article>
  )
}
