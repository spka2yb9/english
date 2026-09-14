import type { ContrastSide, LessonBlock } from '../content/types'
import { EnglishExample } from './EnglishExample'
import { Illustration } from './Illustration'
import { RichText } from './RichText'
import { Timeline } from './Timeline'

/** レッスンのコンテンツブロック列を描画する。 */
export function LessonBlocks({ blocks }: { blocks: LessonBlock[] }) {
  return (
    <>
      {blocks.map((block, i) => (
        <Block key={i} block={block} />
      ))}
    </>
  )
}

function Block({ block }: { block: LessonBlock }) {
  switch (block.type) {
    case 'explanation':
      return (
        <section className="block block-explanation">
          {block.title && <h3>{block.title}</h3>}
          <RichText text={block.body} />
        </section>
      )
    case 'examples':
      return (
        <section className="block block-examples">
          {block.title && <h3>{block.title}</h3>}
          {block.items.map((ex, i) => (
            <EnglishExample
              key={i}
              text={ex.en}
              translation={ex.ja}
              highlight={ex.highlight}
              note={ex.note}
              pattern={ex.pattern}
              patternNote={ex.patternNote}
            />
          ))}
        </section>
      )
    case 'timeline':
      return (
        <section className="block block-timeline">
          {block.title && <h3>{block.title}</h3>}
          <div className="timeline-group">
            {block.timelines.map((t, i) => (
              <Timeline key={i} spec={t} />
            ))}
          </div>
        </section>
      )
    case 'table':
      return (
        <section className="block block-table">
          {block.title && <h3>{block.title}</h3>}
          <div
            className="table-scroll"
            role="region"
            aria-label={`${block.title ?? '文法表'}（横にスクロールできます）`}
            tabIndex={0}
          >
            <table>
              <thead>
                <tr>
                  {block.headers.map((h, i) => (
                    <th key={i}>{h}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {block.rows.map((row, i) => (
                  <tr key={i}>
                    {row.map((cell, j) => (
                      <td key={j}>{cell}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )
    case 'contrast':
      return (
        <section className="block block-contrast">
          {block.title && <h3>{block.title}</h3>}
          <div className="contrast-grid">
            <ContrastPanel side={block.left} />
            <ContrastPanel side={block.right} />
          </div>
          {block.note && <p className="contrast-note">{block.note}</p>}
        </section>
      )
    case 'structure':
      return (
        <section className="block block-structure">
          {block.title && <h3>{block.title}</h3>}
          {/* 文構造だけでなく at → on → in のような段階図にも使うため、見出しがあればそれを読み上げる。 */}
          <div className="structure-row" role="img" aria-label={`${block.title ?? '文構造'}: ${block.parts.map((p) => `${p.label}「${p.text}」`).join(' → ')}`}>
            {block.parts.map((part, i) => (
              <div className="structure-part" key={i}>
                <span className="structure-label">{part.label}</span>
                <span className="structure-text" lang="en">
                  {part.text}
                </span>
              </div>
            ))}
          </div>
          {block.caption && <p className="structure-caption">{block.caption}</p>}
        </section>
      )
    case 'illustration':
      return (
        <figure className="block block-illustration">
          <Illustration sceneId={block.sceneId} kind={block.kind} labels={block.labels} alt={block.alt} />
          {block.caption && <figcaption className="illustration-caption">{block.caption}</figcaption>}
        </figure>
      )
  }
}

function ContrastPanel({ side }: { side: ContrastSide }) {
  return (
    <div className="contrast-panel">
      <h4>{side.label}</h4>
      {side.items.map((ex, i) => (
        <EnglishExample
          key={i}
          text={ex.en}
          translation={ex.ja}
          highlight={ex.highlight}
          note={ex.note}
          pattern={ex.pattern}
          patternNote={ex.patternNote}
        />
      ))}
      {side.pointJa && <p className="contrast-point">{side.pointJa}</p>}
    </div>
  )
}
