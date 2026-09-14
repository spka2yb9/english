import { AudioButton } from './AudioButton'
import { renderHighlighted } from './textRendering'

type Props = {
  text: string
  translation?: string
  /** text 内の部分文字列を視覚的にハイライト */
  highlight?: string
  note?: string
  /** スロー再生ボタンも表示 */
  slow?: boolean
}

/** 学習用英文の標準表示: 英文 + 音声 + 和訳 + ハイライト */
export function EnglishExample({ text, translation, highlight, note, slow = true }: Props) {
  return (
    <div className="example">
      <p className="example-en" lang="en">
        {renderHighlighted(text, highlight)}
        <span className="example-audio">
          <AudioButton text={text} />
          {slow && <AudioButton text={text} slow />}
        </span>
      </p>
      {translation && <p className="example-ja">{translation}</p>}
      {note && <p className="example-note">{note}</p>}
    </div>
  )
}
