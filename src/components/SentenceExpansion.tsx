import type { ExpansionStep } from '../content/types'
import { AudioButton } from './AudioButton'
import { renderHighlighted } from './textRendering'

type Props = {
  steps: ExpansionStep[]
  caption?: string
}

/**
 * 英文が段階的に変わる過程を示す図。
 * 足された語句(focus)を強調し、骨格が変わらないことを目で追えるようにする。
 */
export function SentenceExpansion({ steps, caption }: Props) {
  return (
    <div className="expansion">
      <ol className="expansion-steps">
        {steps.map((step, index) => (
          <li key={index} className="expansion-step">
            <p className="expansion-en" lang="en">
              {renderHighlighted(step.en, step.focus)}
              <span className="example-audio">
                <AudioButton text={step.en} />
                <AudioButton text={step.en} slow />
              </span>
            </p>
            {step.ja && <p className="example-ja">{step.ja}</p>}
            {step.note && <p className="expansion-note">{step.note}</p>}
          </li>
        ))}
      </ol>
      {caption && <p className="expansion-caption">{caption}</p>}
    </div>
  )
}
