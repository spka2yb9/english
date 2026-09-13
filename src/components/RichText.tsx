import { renderBold } from './textRendering'

// 解説本文の軽量レンダラ。段落(\n\n)、箇条書き("- ")、**強調** のみサポート。
// 外部Markdownライブラリは使わない(この3機能で十分なため)。

export function RichText({ text }: { text: string }) {
  const paragraphs = text.split(/\n\n+/)
  return (
    <>
      {paragraphs.map((para, i) => {
        const lines = para.split('\n')
        const isList = lines.every((l) => l.trim().startsWith('- '))
        if (isList) {
          return (
            <ul key={i}>
              {lines.map((l, j) => (
                <li key={j}>{renderBold(l.trim().slice(2))}</li>
              ))}
            </ul>
          )
        }
        return <p key={i}>{renderBold(para)}</p>
      })}
    </>
  )
}
