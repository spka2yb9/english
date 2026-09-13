import type { ReactNode } from 'react'

export function renderHighlighted(text: string, highlight?: string): ReactNode {
  if (!highlight) return text
  const index = text.toLowerCase().indexOf(highlight.toLowerCase())
  if (index === -1) return text
  return (
    <>
      {text.slice(0, index)}
      <mark className="hl">{text.slice(index, index + highlight.length)}</mark>
      {text.slice(index + highlight.length)}
    </>
  )
}

export function renderBold(text: string): ReactNode {
  const parts = text.split(/\*\*(.+?)\*\*/g)
  if (parts.length === 1) return text
  return parts.map((part, index) => (index % 2 === 1 ? <strong key={index}>{part}</strong> : part))
}
