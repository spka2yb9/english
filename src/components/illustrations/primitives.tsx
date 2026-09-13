import type { ReactNode } from 'react'

export type SceneTone = 'teal' | 'coral' | 'gold' | 'blue' | 'violet' | 'green'

const TONE_CLASS: Record<SceneTone, string> = {
  teal: 'ill-teal',
  coral: 'ill-coral',
  gold: 'ill-gold',
  blue: 'ill-blue',
  violet: 'ill-violet',
  green: 'ill-green',
}

/** Shared SVG definitions. The illustration component is rendered once per lesson page. */
export function SceneDefs() {
  return (
    <defs>
      <filter id="ill-shadow" x="-30%" y="-30%" width="160%" height="170%">
        <feDropShadow dx="0" dy="5" stdDeviation="5" floodColor="#17324d" floodOpacity=".13" />
      </filter>
      <marker id="ill-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M1 1l8 4-8 4z" className="ill-arrow-head" />
      </marker>
      <pattern id="ill-dots" width="18" height="18" patternUnits="userSpaceOnUse">
        <circle cx="3" cy="3" r="1.5" className="ill-pattern-dot" />
      </pattern>
    </defs>
  )
}

export function Backdrop({ tone = 'teal', variant = 0 }: { tone?: SceneTone; variant?: number }) {
  const toneClass = TONE_CLASS[tone]
  const decorations = [
    <g key="a" aria-hidden="true">
      <circle cx="555" cy="42" r="78" className={`${toneClass} ill-wash`} />
      <path d="M0 236C126 198 198 284 334 250s198-16 306 20v30H0z" className="ill-ground" />
      <circle cx="47" cy="45" r="18" className="ill-sun" />
    </g>,
    <g key="b" aria-hidden="true">
      <path d="M0 0h190c-18 43-64 75-190 82z" className={`${toneClass} ill-wash`} />
      <circle cx="564" cy="238" r="96" className="ill-ground" />
      <path d="M510 25h104M532 43h74" className={`${toneClass} ill-decor-line`} />
    </g>,
    <g key="c" aria-hidden="true">
      <rect x="18" y="18" width="604" height="264" rx="28" className="ill-inner-frame" />
      <path d="M25 246c108-75 194 49 302-10s196 19 288-41" className={`${toneClass} ill-decor-line`} />
      <circle cx="581" cy="52" r="24" className="ill-sun" />
    </g>,
    <g key="d" aria-hidden="true">
      <circle cx="72" cy="250" r="116" className={`${toneClass} ill-wash`} />
      <rect x="472" y="0" width="168" height="300" className="ill-dot-field" />
      <path d="M506 63c25-30 54-30 80 0" className={`${toneClass} ill-decor-line`} />
    </g>,
    <g key="e" aria-hidden="true">
      <path d="M0 30c105 48 174-38 290 4s226 14 350-20V0H0z" className={`${toneClass} ill-wash`} />
      <path d="M0 266c140-51 244 37 380-8s184-18 260 6v36H0z" className="ill-ground" />
      <circle cx="590" cy="72" r="9" className="ill-coral ill-solid" />
      <circle cx="566" cy="46" r="5" className="ill-gold ill-solid" />
    </g>,
    <g key="f" aria-hidden="true">
      <path d="M26 26h160v7H26zM454 267h160v7H454z" className={`${toneClass} ill-solid`} />
      <circle cx="553" cy="75" r="68" className="ill-ground" />
      <circle cx="78" cy="230" r="52" className={`${toneClass} ill-wash`} />
    </g>,
  ]

  return (
    <>
      <rect width="640" height="300" rx="26" className="ill-canvas" />
      {decorations[variant % decorations.length]}
    </>
  )
}

function estimatedTextWidth(text: string, size: number) {
  let units = 0
  for (const char of text) units += /[\u3000-\u9fff\uff00-\uffef]/.test(char) ? 1 : /[MW@%]/.test(char) ? 0.85 : /[ilI.,' ]/.test(char) ? 0.32 : 0.57
  return units * size
}

function fittedFontSize(text: string, maxWidth: number, preferred: number, minimum = 12) {
  const estimate = estimatedTextWidth(text, preferred)
  return Math.max(minimum, Math.min(preferred, preferred * (maxWidth / Math.max(estimate, 1))))
}

export function Label({
  x,
  y,
  width,
  text,
  tone = 'paper',
  height = 38,
  fontSize = 22,
  rotate,
  icon,
}: {
  x: number
  y: number
  width: number
  text: string
  tone?: SceneTone | 'paper' | 'ink'
  height?: number
  fontSize?: number
  rotate?: number
  icon?: ReactNode
}) {
  const fillClass = tone === 'paper' ? 'ill-paper' : tone === 'ink' ? 'ill-ink-fill' : `${TONE_CLASS[tone]} ill-pale`
  const actualSize = fittedFontSize(text, width - (icon ? 48 : 22), fontSize)
  return (
    <g transform={rotate ? `rotate(${rotate} ${x} ${y})` : undefined} className="ill-label" filter="url(#ill-shadow)">
      <rect x={x - width / 2} y={y - height / 2} width={width} height={height} rx={height / 2} className={fillClass} />
      {icon && <g transform={`translate(${x - width / 2 + 12} ${y - 11})`}>{icon}</g>}
      <text
        x={x + (icon ? 12 : 0)}
        y={y + actualSize * 0.34}
        style={{ fontSize: actualSize }}
        className={tone === 'ink' ? 'ill-light-text' : undefined}
      >
        {text}
      </text>
    </g>
  )
}

export function PlainText({
  x,
  y,
  text,
  width = 180,
  size = 16,
  tone = 'ink',
  anchor = 'middle',
  className = '',
}: {
  x: number
  y: number
  text: string
  width?: number
  size?: number
  tone?: SceneTone | 'ink' | 'muted' | 'light'
  anchor?: 'start' | 'middle' | 'end'
  className?: string
}) {
  const actualSize = fittedFontSize(text, width, size)
  const colorClass = tone === 'ink' ? '' : tone === 'muted' ? 'ill-muted-text' : tone === 'light' ? 'ill-light-text' : `ill-${tone}-text`
  return (
    <text x={x} y={y} textAnchor={anchor} style={{ fontSize: actualSize }} className={`${colorClass} ${className}`.trim()}>
      {text}
    </text>
  )
}

export function Arrow({
  d,
  tone = 'teal',
  dashed = false,
  width = 4,
}: {
  d: string
  tone?: SceneTone | 'ink' | 'muted'
  dashed?: boolean
  width?: number
}) {
  const toneClass = tone === 'ink' ? 'ill-ink-stroke' : tone === 'muted' ? 'ill-muted-stroke' : `${TONE_CLASS[tone]} ill-stroke`
  return <path d={d} className={`${toneClass} ill-arrow ${dashed ? 'ill-dashed' : ''}`} style={{ strokeWidth: width }} markerEnd="url(#ill-arrow)" />
}

export function Panel({
  x,
  y,
  width,
  height,
  tone = 'paper',
  children,
  dashed = false,
  radius = 20,
}: {
  x: number
  y: number
  width: number
  height: number
  tone?: SceneTone | 'paper'
  children?: ReactNode
  dashed?: boolean
  radius?: number
}) {
  const fillClass = tone === 'paper' ? 'ill-paper' : `${TONE_CLASS[tone]} ill-pale`
  return (
    <g>
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        rx={radius}
        className={`${fillClass} ill-panel ${dashed ? 'ill-dashed' : ''}`}
        filter="url(#ill-shadow)"
      />
      {children}
    </g>
  )
}

export function Divider({ x = 320, label }: { x?: number; label?: string }) {
  return (
    <g aria-hidden="true">
      <path d={`M${x} 42v216`} className="ill-muted-stroke ill-dashed" />
      {label && <Label x={x} y={150} width={48} height={30} text={label} tone="ink" fontSize={12} />}
    </g>
  )
}

export function SpeechBubble({
  x,
  y,
  width,
  height = 58,
  text,
  tone = 'paper',
  tail = 'left',
}: {
  x: number
  y: number
  width: number
  height?: number
  text: string
  tone?: SceneTone | 'paper'
  tail?: 'left' | 'right' | 'bottom'
}) {
  const fillClass = tone === 'paper' ? 'ill-paper' : `${TONE_CLASS[tone]} ill-pale`
  const tailPath =
    tail === 'left'
      ? `M${x - width / 2 + 32} ${y + height / 2 - 2}l-22 22 34-17`
      : tail === 'right'
        ? `M${x + width / 2 - 32} ${y + height / 2 - 2}l22 22-34-17`
        : `M${x - 7} ${y + height / 2 - 2}l7 22 10-22`
  return (
    <g filter="url(#ill-shadow)">
      <rect x={x - width / 2} y={y - height / 2} width={width} height={height} rx="20" className={`${fillClass} ill-panel`} />
      <path d={tailPath} className={`${fillClass} ill-bubble-tail`} />
      <PlainText x={x} y={y + 5} text={text} width={width - 28} size={16} />
    </g>
  )
}

type CharacterPose = 'stand' | 'wave' | 'point' | 'carry' | 'think' | 'walk' | 'sit' | 'celebrate'
type CharacterHair = 'short' | 'bob' | 'bun' | 'curl' | 'cap'

export function Character({
  x,
  y = 246,
  scale = 1,
  facing = 1,
  shirt = 'teal',
  trousers = 'blue',
  pose = 'stand',
  hair = 'short',
  mood = 'smile',
}: {
  x: number
  y?: number
  scale?: number
  facing?: 1 | -1
  shirt?: SceneTone
  trousers?: SceneTone
  pose?: CharacterPose
  hair?: CharacterHair
  mood?: 'smile' | 'neutral' | 'surprised' | 'sad'
}) {
  const shirtClass = `${TONE_CLASS[shirt]} ill-solid`
  const trouserClass = `${TONE_CLASS[trousers]} ill-dark`
  const arms: Record<CharacterPose, ReactNode> = {
    stand: <path d="M-22-70l-16 45M22-70l16 45" className="ill-skin ill-body-line" />,
    wave: <><path d="M-22-70l-16 45" className="ill-skin ill-body-line" /><path d="M22-70l22-25 4-25" className="ill-skin ill-body-line" /><path d="M40-120l-8-7M46-121v-10M51-118l8-7" className="ill-ink-stroke ill-fine" /></>,
    point: <><path d="M-22-70l-14 44" className="ill-skin ill-body-line" /><path d="M22-70l44 5" className="ill-skin ill-body-line" /><circle cx="69" cy="-65" r="5" className="ill-skin" /></>,
    carry: <><path d="M-22-70l12 34" className="ill-skin ill-body-line" /><path d="M22-70L10-36" className="ill-skin ill-body-line" /></>,
    think: <><path d="M-22-70l-17 41" className="ill-skin ill-body-line" /><path d="M22-70L8-94" className="ill-skin ill-body-line" /><circle cx="6" cy="-101" r="5" className="ill-skin" /></>,
    walk: <><path d="M-22-70l-28 29" className="ill-skin ill-body-line" /><path d="M22-70l31 24" className="ill-skin ill-body-line" /></>,
    sit: <><path d="M-22-70l-9 41" className="ill-skin ill-body-line" /><path d="M22-70l17 37" className="ill-skin ill-body-line" /></>,
    celebrate: <><path d="M-22-70l-26-35-5-17" className="ill-skin ill-body-line" /><path d="M22-70l26-35 5-17" className="ill-skin ill-body-line" /><path d="M-57-128l-9-7M-53-132l1-12M57-128l9-7M53-132l-1-12" className="ill-ink-stroke ill-fine" /></>,
  }
  const legs =
    pose === 'walk' ? (
      <><path d="M-12-8l-26 33" className={`${trouserClass} ill-leg`} /><path d="M12-8l28 28" className={`${trouserClass} ill-leg`} /></>
    ) : pose === 'sit' ? (
      <><path d="M-13-8l30 11 20 19" className={`${trouserClass} ill-leg`} /><path d="M10-8l35 4 19 8" className={`${trouserClass} ill-leg`} /></>
    ) : (
      <><path d="M-12-8l-7 35" className={`${trouserClass} ill-leg`} /><path d="M12-8l7 35" className={`${trouserClass} ill-leg`} /></>
    )
  const hairShape: Record<CharacterHair, ReactNode> = {
    short: <path d="M-24-109q3-28 25-28 24 0 28 25-13-10-27-4-12-11-26 7z" className="ill-hair" />,
    bob: <path d="M-29-108q1-31 29-31t30 31v23l-11-9v-18q-20 9-40 0v20l-8 8z" className="ill-hair" />,
    bun: <><circle cx="15" cy="-140" r="12" className="ill-hair" /><path d="M-26-111q3-28 27-28 22 0 27 27-15-13-28-3-12-9-26 4z" className="ill-hair" /></>,
    curl: <path d="M-27-108q-2-27 23-33 27-5 34 24-8-5-12 3-7-12-15-2-9-11-14 1-7-8-16 7z" className="ill-hair" />,
    cap: <><path d="M-25-116q8-25 29-21 19 2 23 23z" className="ill-blue ill-solid" /><path d="M20-117h21" className="ill-ink-stroke ill-fine" /></>,
  }
  const mouth = mood === 'smile' ? 'M-8-94q8 8 16 0' : mood === 'sad' ? 'M-8-90q8-8 16 0' : mood === 'surprised' ? undefined : 'M-7-92h14'

  return (
    <g transform={`translate(${x} ${y}) scale(${scale * facing} ${scale})`} className="ill-character">
      {legs}
      <path d="M-25-78q25-13 50 0l-8 72h-34z" className={shirtClass} />
      {arms[pose]}
      {pose === 'carry' && <rect x="-31" y="-50" width="62" height="38" rx="5" className="ill-gold ill-pale ill-panel" />}
      <circle cx="0" cy="-108" r="24" className="ill-skin" />
      {hairShape[hair]}
      <circle cx="-8" cy="-104" r="2.2" className="ill-ink-fill" />
      <circle cx="8" cy="-104" r="2.2" className="ill-ink-fill" />
      {mood === 'surprised' ? <circle cx="0" cy="-91" r="4" className="ill-ink-stroke" /> : <path d={mouth} className="ill-ink-stroke ill-face" />}
    </g>
  )
}

export function Book({ x, y, scale = 1, color = 'coral', open = false }: { x: number; y: number; scale?: number; color?: SceneTone; open?: boolean }) {
  const colorClass = `${TONE_CLASS[color]} ill-pale`
  return open ? (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M0 0q-29-15-60-5v48q31-10 60 6zM0 0q29-15 60-5v48Q29 33 0 49z" className={`${colorClass} ill-panel`} />
      <path d="M0 2v45M-46 10h31M-46 20h35M15 10h31M11 20h35" className="ill-muted-stroke ill-fine" />
    </g>
  ) : (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <rect x="-34" y="-45" width="68" height="90" rx="6" className={`${colorClass} ill-panel`} />
      <path d="M-22-45v90M-12-25h31M-12-14h24" className="ill-muted-stroke ill-fine" />
    </g>
  )
}

export function Clock({ x, y, r = 40, time = 'ten', tone = 'teal' }: { x: number; y: number; r?: number; time?: 'ten' | 'three' | 'six' | 'eight'; tone?: SceneTone }) {
  const hands: Record<string, string> = {
    ten: `M${x} ${y}v-${r * 0.55}M${x} ${y}l-${r * 0.42}-${r * 0.22}`,
    three: `M${x} ${y}v-${r * 0.55}M${x} ${y}h${r * 0.48}`,
    six: `M${x} ${y}v-${r * 0.54}M${x} ${y}v${r * 0.48}`,
    eight: `M${x} ${y}v-${r * 0.52}M${x} ${y}l-${r * 0.4} ${r * 0.28}`,
  }
  return (
    <g>
      <circle cx={x} cy={y} r={r} className={`${TONE_CLASS[tone]} ill-pale ill-panel`} filter="url(#ill-shadow)" />
      <circle cx={x} cy={y} r="4" className="ill-ink-fill" />
      <path d={hands[time]} className="ill-ink-stroke ill-clock-hand" />
      <path d={`M${x} ${y - r + 8}v6M${x + r - 8} ${y}h-6M${x} ${y + r - 8}v-6M${x - r + 8} ${y}h6`} className="ill-muted-stroke ill-fine" />
    </g>
  )
}

export function Calendar({ x, y, width = 112, height = 100, day = '18', tone = 'coral' }: { x: number; y: number; width?: number; height?: number; day?: string; tone?: SceneTone }) {
  return (
    <g filter="url(#ill-shadow)">
      <rect x={x - width / 2} y={y - height / 2} width={width} height={height} rx="12" className="ill-paper ill-panel" />
      <path d={`M${x - width / 2} ${y - height / 2 + 27}h${width}`} className={`${TONE_CLASS[tone]} ill-stroke ill-wide`} />
      <path d={`M${x - width * .27} ${y - height / 2 - 7}v20M${x + width * .27} ${y - height / 2 - 7}v20`} className="ill-ink-stroke ill-wide" />
      <PlainText x={x} y={y + 22} text={day} width={width - 16} size={31} tone={tone} />
    </g>
  )
}

export function House({ x, y, scale = 1, tone = 'teal' }: { x: number; y: number; scale?: number; tone?: SceneTone }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M-62-50L0-105l62 55v76H-62z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <path d="M-72-43L0-108l72 65" className={`${TONE_CLASS[tone]} ill-stroke ill-wide`} />
      <rect x="-14" y="-25" width="28" height="51" rx="3" className={`${TONE_CLASS[tone]} ill-pale ill-panel`} />
      <rect x="-47" y="-36" width="23" height="24" rx="3" className="ill-blue ill-pale ill-panel" />
      <circle cx="6" cy="0" r="2" className="ill-ink-fill" />
    </g>
  )
}

export function Tree({ x, y, scale = 1, tone = 'green' }: { x: number; y: number; scale?: number; tone?: SceneTone }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M-7 4v-58h14V4" className="ill-gold ill-dark" />
      <circle cx="-22" cy="-69" r="27" className={`${TONE_CLASS[tone]} ill-pale`} />
      <circle cx="16" cy="-77" r="31" className={`${TONE_CLASS[tone]} ill-pale`} />
      <circle cx="2" cy="-105" r="25" className={`${TONE_CLASS[tone]} ill-pale`} />
    </g>
  )
}

export function Check({ x, y, scale = 1, tone = 'green' }: { x: number; y: number; scale?: number; tone?: SceneTone }) {
  return <path d={`M${x - 17 * scale} ${y}l${12 * scale} ${13 * scale} ${25 * scale}-${28 * scale}`} className={`${TONE_CLASS[tone]} ill-stroke ill-check`} />
}

export function Cross({ x, y, scale = 1, tone = 'coral' }: { x: number; y: number; scale?: number; tone?: SceneTone }) {
  return <path d={`M${x - 16 * scale} ${y - 16 * scale}l${32 * scale} ${32 * scale}M${x + 16 * scale} ${y - 16 * scale}l-${32 * scale} ${32 * scale}`} className={`${TONE_CLASS[tone]} ill-stroke ill-check`} />
}

export function Sparkles({ x, y, tone = 'gold' }: { x: number; y: number; tone?: SceneTone }) {
  return (
    <g className={`${TONE_CLASS[tone]} ill-stroke ill-fine`} aria-hidden="true">
      <path d={`M${x} ${y - 13}v26M${x - 13} ${y}h26`} />
      <path d={`M${x + 25} ${y - 3}v15M${x + 18} ${y + 5}h15`} />
      <path d={`M${x - 25} ${y - 4}v12M${x - 31} ${y + 2}h12`} />
    </g>
  )
}

export function NumberBadge({ x, y, number, tone = 'coral' }: { x: number; y: number; number: string; tone?: SceneTone }) {
  return (
    <g filter="url(#ill-shadow)">
      <circle cx={x} cy={y} r="19" className={`${TONE_CLASS[tone]} ill-solid`} />
      <PlainText x={x} y={y + 6} text={number} width={26} size={16} tone="light" />
    </g>
  )
}

export function Sun({ x, y, r = 28 }: { x: number; y: number; r?: number }) {
  return (
    <g className="ill-gold ill-stroke">
      <circle cx={x} cy={y} r={r} className="ill-gold ill-pale" />
      {[0, 45, 90, 135].map((deg) => (
        <path key={deg} d={`M${x} ${y - r - 9}v-12M${x} ${y + r + 9}v12`} transform={`rotate(${deg} ${x} ${y})`} />
      ))}
    </g>
  )
}

export function Cloud({ x, y, scale = 1, raining = false }: { x: number; y: number; scale?: number; raining?: boolean }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M-52 16q-5-25 19-31 8-31 39-20 17 2 22 20 28-3 30 22 1 22-24 24h-66q-17-1-20-15z" className="ill-blue ill-pale ill-panel" />
      {raining && <path d="M-31 44l-7 14M0 44l-7 14M31 44l-7 14" className="ill-blue ill-stroke ill-wide" />}
    </g>
  )
}

export function Road({ d, tone = 'blue', dashed = true }: { d: string; tone?: SceneTone; dashed?: boolean }) {
  return <path d={d} className={`${TONE_CLASS[tone]} ill-stroke ill-road ${dashed ? 'ill-dashed' : ''}`} />
}

export function Eye({ x, y, scale = 1 }: { x: number; y: number; scale?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M-47 0q47-45 94 0-47 45-94 0z" className="ill-paper ill-panel" />
      <circle cx="0" cy="0" r="18" className="ill-blue ill-pale ill-panel" />
      <circle cx="0" cy="0" r="7" className="ill-ink-fill" />
    </g>
  )
}

export function Ear({ x, y, scale = 1 }: { x: number; y: number; scale?: number }) {
  return (
    <g transform={`translate(${x} ${y}) scale(${scale})`}>
      <path d="M6 43c-28-5-30-30-29-57 1-29 19-45 43-39 20 5 29 29 17 47-7 11-20 13-22 28-2 12-3 19-9 21z" className="ill-skin ill-panel" />
      <path d="M-4 10c-8-26 21-39 25-16 2 13-12 14-13 26" className="ill-muted-stroke ill-fine" />
    </g>
  )
}

export function TinyStar({ x, y, tone = 'gold', scale = 1 }: { x: number; y: number; tone?: SceneTone; scale?: number }) {
  return <path d={`M${x} ${y - 14 * scale}l${4 * scale} ${9 * scale} ${10 * scale} ${1 * scale}-${8 * scale} ${7 * scale} ${3 * scale} ${10 * scale}-${9 * scale}-${5 * scale}-${9 * scale} ${5 * scale} ${3 * scale}-${10 * scale}-${8 * scale}-${7 * scale} ${10 * scale}-${1 * scale}z`} className={`${TONE_CLASS[tone]} ill-solid`} />
}
