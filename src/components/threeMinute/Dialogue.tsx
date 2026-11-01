import type { ThreeMinuteLine, ThreeMinuteSection } from '../../content/threeMinute'
import { AudioButton } from '../AudioButton'
import { GrammarAnimation } from '../GrammarAnimation'
import { Ingbird } from '../Ingbird'
import { LessonBlocks } from '../LessonBlocks'
import { RichText } from '../RichText'
import { renderHighlighted } from '../textRendering'
import { Hiyoko } from './Hiyoko'
import type { IngbirdAppearance } from './useIngbirdAppearance'
import './three-minute.css'

const SPEAKER_LABELS = {
  ingbird: 'イングバード先生',
  hiyoko: 'ヒヨコ君',
} as const

function SpeakerBubble({ line, appearance }: { line: ThreeMinuteLine; appearance: IngbirdAppearance }) {
  const isIngbird = line.speaker === 'ingbird'
  return (
    <div className={`tm-turn tm-turn-${line.speaker}`}>
      <div className="tm-avatar" aria-hidden="true">
        {isIngbird ? (
          <Ingbird
            mood={line.mood ?? 'happy'}
            evolution={appearance.evolution}
            outfit={appearance.outfit}
            size={64}
            decorative
          />
        ) : (
          <Hiyoko mood={line.mood ?? 'happy'} size={64} decorative />
        )}
      </div>
      <div className="tm-bubble-wrap">
        <p className="tm-speaker">{SPEAKER_LABELS[line.speaker]}</p>
        <div className="tm-bubble">
          <RichText text={line.text} />
          {line.en && (
            <div className="tm-en-card">
              <p className="tm-en" lang="en">
                {renderHighlighted(line.en, line.highlight)}
              </p>
              {line.ja && <p className="tm-ja">{line.ja}</p>}
              <span className="tm-en-audio">
                <AudioButton text={line.en} />
                <AudioButton text={line.en} slow />
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

/**
 * 会話パートを上から順に描く。
 * 文法ページの教材ブロックは、発言の間に「ホワイトボード」として挟み込む。
 */
export function ThreeMinuteDialogue({
  section,
  appearance,
}: {
  section: ThreeMinuteSection
  appearance: IngbirdAppearance
}) {
  return (
    <div className="tm-dialogue" role="group" aria-label="イングバード先生とヒヨコ君の会話">
      {section.parts.map((part, index) => {
        if (part.kind === 'line') return <SpeakerBubble key={index} line={part.line} appearance={appearance} />
        if (part.kind === 'animation') {
          return (
            <div className="tm-scene tm-scene-animation" key={index}>
              <p className="tm-scene-label">
                <span aria-hidden="true">✦</span> うごいてわかる
              </p>
              <GrammarAnimation sceneId={section.lessonId} animation={part.animation} />
            </div>
          )
        }
        return (
          <div className="tm-scene" key={index}>
            <p className="tm-scene-label">
              <span aria-hidden="true">✎</span> {part.label}
            </p>
            <div className="tm-scene-body">
              <LessonBlocks blocks={[part.block]} collapseExamplesAfter={5} />
            </div>
          </div>
        )
      })}
    </div>
  )
}
