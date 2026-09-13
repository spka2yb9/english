import type { TimelineSpec } from '../content/types'

// タイムライン図。軸: 0(過去)〜100(現在)〜130(未来)。
const AXIS_MAX = 130
const NOW = 100

const pos = (v: number) => `${(Math.min(v, AXIS_MAX) / AXIS_MAX) * 100}%`

export function Timeline({ spec }: { spec: TimelineSpec }) {
  const hasFuture = (spec.point ?? 0) > NOW || (spec.range?.[1] ?? 0) > NOW
  return (
    <figure className="timeline" role="img" aria-label={timelineAlt(spec)}>
      {spec.title && <figcaption className="timeline-title">{spec.title}</figcaption>}
      <div className="timeline-axis">
        <div className="timeline-line" />
        <div className="timeline-now" style={{ left: pos(NOW) }}>
          <span className="timeline-now-label">今</span>
        </div>
        {spec.range && (
          <div
            className={`timeline-range${spec.arrowToNow ? ' to-now' : ''}`}
            style={{ left: pos(spec.range[0]), width: `calc(${pos(spec.arrowToNow ? NOW : spec.range[1])} - ${pos(spec.range[0])})` }}
          >
            {spec.rangeLabel && <span className="timeline-range-label">{spec.rangeLabel}</span>}
          </div>
        )}
        {spec.point !== undefined && (
          <div className="timeline-point" style={{ left: pos(spec.point) }}>
            <span className="timeline-dot" />
            {spec.pointLabel && (
              <span className={`timeline-point-label${spec.rangeLabel ? ' above-axis' : ''}`}>
                {spec.pointLabel}
              </span>
            )}
          </div>
        )}
        <span className="timeline-edge past">過去</span>
        {hasFuture && <span className="timeline-edge future">未来</span>}
      </div>
      {spec.caption && <p className="timeline-caption">{spec.caption}</p>}
    </figure>
  )
}

function timelineAlt(spec: TimelineSpec): string {
  const parts: string[] = []
  if (spec.title) parts.push(spec.title)
  if (spec.rangeLabel) parts.push(`期間: ${spec.rangeLabel}`)
  if (spec.pointLabel) parts.push(`時点: ${spec.pointLabel}`)
  if (spec.caption) parts.push(spec.caption)
  return `タイムライン図: ${parts.join('、') || '時間軸'}`
}
