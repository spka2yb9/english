import type { BreakdownPart, SentencePattern } from '../content/types'
import { PATTERN_LABELS, PATTERN_MEANINGS } from '../content/grammar/patterns/types'
import { roleAccessibleLabel } from '../content/grammar/structures/roles'
import { AudioButton } from './AudioButton'

type Props = {
  sentence: string
  ja?: string
  /** この文全体の5文型。 */
  pattern?: SentencePattern
  parts: BreakdownPart[]
  /** 「the book = very useful」のような意味上の関係 */
  relation?: string
  /** 修飾語(M)を外した骨格 */
  skeleton?: string
  skeletonPattern?: SentencePattern
  caption?: string
}

function patternLabel(pattern: SentencePattern): string {
  return `${PATTERN_LABELS[pattern]}。${PATTERN_MEANINGS[pattern]}`
}

/**
 * 英文を S / V / O / C / M の区画に分けて見せる構造図。
 * 語句を意味のまとまりごとに区切り、それぞれが文の中で何をしているかを示す。
 */
export function SentenceBreakdown({ sentence, ja, pattern, parts, relation, skeleton, skeletonPattern, caption }: Props) {
  return (
    <div className="breakdown">
      <p className="breakdown-sentence" lang="en">
        {pattern && (
          <span className="example-pattern" aria-label={patternLabel(pattern)}>
            {pattern}
          </span>
        )}
        {sentence}
        <span className="example-audio">
          <AudioButton text={sentence} />
          <AudioButton text={sentence} slow />
        </span>
      </p>
      {ja && <p className="example-ja">{ja}</p>}

      <ul className="breakdown-parts" lang="en">
        {parts.map((part, index) => (
          <li key={index} className={`breakdown-part role-${part.role}`}>
            <span className="role-badge" aria-label={roleAccessibleLabel(part.role)}>
              {part.role}
            </span>
            <span className="breakdown-text">{part.text}</span>
            {part.note && (
              <span className="breakdown-note" lang="ja">
                {part.note}
              </span>
            )}
          </li>
        ))}
      </ul>

      {relation && (
        <p className="breakdown-relation">
          <span className="breakdown-label">意味の関係</span>
          <span lang="en">{relation}</span>
        </p>
      )}

      {skeleton && (
        <p className="breakdown-skeleton">
          <span className="breakdown-label">骨格</span>
          <span lang="en">{skeleton}</span>
          {skeletonPattern && (
            <span className="example-pattern" aria-label={patternLabel(skeletonPattern)}>
              {skeletonPattern}
            </span>
          )}
        </p>
      )}

      {caption && <p className="breakdown-caption">{caption}</p>}
    </div>
  )
}
