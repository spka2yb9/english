import './Ingbird.css'

export type IngbirdMood = 'idle' | 'happy' | 'cheer'

type Props = {
  mood?: IngbirdMood
  /** 表示サイズ(px)。正方形。 */
  size?: number
  /** 周囲のテキストが意味を伝える場合は true にして、読み上げの対象から外す。 */
  decorative?: boolean
  className?: string
}

/**
 * マスコット「イングバード」。英語(イングリッシュ)を覚える鳥。
 * いつも小さく揺れていて、まばたきし、うれしいときは羽をばたつかせて跳ねる。
 * 絵はインラインSVGなので、テーマの色に合わせられて、拡大しても崩れない。
 */
export function Ingbird({ mood = 'idle', size = 120, decorative = false, className }: Props) {
  return (
    <svg
      className={className ? `ingbird ${className}` : 'ingbird'}
      width={size}
      height={size}
      viewBox="0 0 120 120"
      data-mood={mood}
      role={decorative ? undefined : 'img'}
      aria-hidden={decorative || undefined}
      aria-label={decorative ? undefined : 'イングバード'}
      focusable="false"
    >
      <ellipse className="ingbird-shadow" cx="60" cy="110" rx="30" ry="6" />
      <g className="ingbird-inner">
        <path className="ingbird-tail" d="M32 76 12 64l4 24z" />
        <path className="ingbird-wing ingbird-wing-left" d="M31 58q-15 9-10 27 8 2 14-6 6-9 4-21z" />
        <path className="ingbird-wing ingbird-wing-right" d="M89 58q15 9 10 27-8 2-14-6-6-9-4-21z" />
        <ellipse className="ingbird-body" cx="60" cy="64" rx="34" ry="38" />
        <ellipse className="ingbird-belly" cx="61" cy="74" rx="22" ry="25" />
        <g className="ingbird-eye">
          <ellipse className="ingbird-eye-white" cx="49" cy="50" rx="9.5" ry="11" />
          <circle className="ingbird-pupil" cx="50.5" cy="52" r="5" />
          <circle className="ingbird-eye-spark" cx="53" cy="48.5" r="1.8" />
        </g>
        <g className="ingbird-eye">
          <ellipse className="ingbird-eye-white" cx="71" cy="50" rx="9.5" ry="11" />
          <circle className="ingbird-pupil" cx="72.5" cy="52" r="5" />
          <circle className="ingbird-eye-spark" cx="75" cy="48.5" r="1.8" />
        </g>
        <ellipse className="ingbird-cheek" cx="37" cy="64" rx="6" ry="4" />
        <ellipse className="ingbird-cheek" cx="83" cy="64" rx="6" ry="4" />
        <path className="ingbird-beak" d="M60 57 67.5 64 60 71.5 52.5 64z" />
        <path className="ingbird-cap-base" d="M47 28q13 6 26 0v-6q-13 6-26 0z" />
        <path className="ingbird-cap" d="M60 10 88 21 60 32 32 21z" />
        <path className="ingbird-tassel" d="M86 22q7 8 4 17" />
        <circle className="ingbird-tassel-bead" cx="90.5" cy="41.5" r="3.2" />
        <path className="ingbird-foot" d="M50 100v6M46 106h8" />
        <path className="ingbird-foot" d="M70 100v6M66 106h8" />
      </g>
      <g className="ingbird-sparkles">
        <path className="ingbird-sparkle-1" d="m13 13 2.6 6.4L22 22l-6.4 2.6L13 31l-2.6-6.4L4 22l6.4-2.6z" />
        <path className="ingbird-sparkle-2" d="m104 10 2 5 5 2-5 2-2 5-2-5-5-2 5-2z" />
        <path className="ingbird-sparkle-3" d="m108 44 1.7 4.3L114 50l-4.3 1.7L108 56l-1.7-4.3L102 50l4.3-1.7z" />
      </g>
    </svg>
  )
}
