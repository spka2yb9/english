import { PATTERN_LABELS, PATTERN_MEANINGS } from '../content/grammar/patterns/types'
import type { SentencePattern } from '../content/types'
import { AudioButton } from './AudioButton'
import { renderHighlighted } from './textRendering'

type Props = {
  text: string
  translation?: string
  /** text 内の部分文字列を視覚的にハイライト */
  highlight?: string
  note?: string
  /** 5文型のバッジ(SV / SVC / SVO / SVOO / SVOC)。合成時に付与される。 */
  pattern?: SentencePattern
  /** 文型についての短い日本語注記。 */
  patternNote?: string
  /** スロー再生ボタンも表示 */
  slow?: boolean
}

/** 学習用英文の標準表示: 文型バッジ + 英文 + 音声 + 和訳 + 文型注記 + 補足 */
export function EnglishExample({ text, translation, highlight, note, pattern, patternNote, slow = true }: Props) {
  return (
    <div className="example">
      <p className="example-en" lang="en">
        {pattern && (
          <span className="example-pattern" aria-label={`${PATTERN_LABELS[pattern]}。${PATTERN_MEANINGS[pattern]}`}>
            {pattern}
          </span>
        )}
        {renderHighlighted(text, highlight)}
        <span className="example-audio">
          <AudioButton text={text} />
          {slow && <AudioButton text={text} slow />}
        </span>
      </p>
      {translation && <p className="example-ja">{translation}</p>}
      {patternNote && <p className="example-pattern-note">{patternNote}</p>}
      {note && <p className="example-note">{note}</p>}
    </div>
  )
}
