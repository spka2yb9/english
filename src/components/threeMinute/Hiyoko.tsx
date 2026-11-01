import './hiyoko.css'

export type HiyokoMood = 'happy' | 'cheer' | 'think' | 'curious' | 'wow' | 'shy' | 'proud'

type Props = {
  mood?: HiyokoMood
  /** 表示サイズ(px)。正方形。 */
  size?: number
  /** 周囲のテキストが名前を伝える場合は true。 */
  decorative?: boolean
  className?: string
}

/**
 * 3分間English の学習者役「ヒヨコ君」。
 *
 * まばたき・小さな上下動・羽の動きはCSSだけで動く。
 * mood で、首かしげ・びっくり・てれ・お祝いの仕草を切り替える。
 */
export function Hiyoko({ mood = 'happy', size = 64, decorative = false, className }: Props) {
  return (
    <svg
      className={className ? `hiyoko ${className}` : 'hiyoko'}
      width={size}
      height={size}
      viewBox="0 0 120 120"
      data-mood={mood}
      role={decorative ? undefined : 'img'}
      aria-hidden={decorative || undefined}
      aria-label={decorative ? undefined : 'ヒヨコ君'}
      focusable="false"
    >
      <ellipse className="hiyoko-shadow" cx="60" cy="111" rx="29" ry="5.5" />

      <g className="hiyoko-inner">
        <path className="hiyoko-wing hiyoko-wing-left" d="M31 67q-14 8-9 27 8 1 13-7 5-8 3-18z" />
        <path className="hiyoko-wing hiyoko-wing-right" d="M89 67q14 8 9 27-8 1-13-7-5-8-3-18z" />

        <ellipse className="hiyoko-body" cx="60" cy="72" rx="33" ry="32" />
        <ellipse className="hiyoko-belly" cx="60" cy="80" rx="21" ry="21" />

        <g className="hiyoko-head">
          <path className="hiyoko-tuft" d="M54 43 48 27l10 7 2-12 2 12 10-7-6 16z" />

          <g className="hiyoko-eye hiyoko-eye-left">
            <ellipse className="hiyoko-eye-white" cx="48" cy="60" rx="7.3" ry="8.2" />
            <circle className="hiyoko-pupil" cx="49" cy="62" r="3.6" />
            <circle className="hiyoko-spark" cx="50.6" cy="59.6" r="1.35" />
            <path className="hiyoko-eye-lid" d="M41 60h14" />
          </g>
          <g className="hiyoko-eye hiyoko-eye-right">
            <ellipse className="hiyoko-eye-white" cx="72" cy="60" rx="7.3" ry="8.2" />
            <circle className="hiyoko-pupil" cx="73" cy="62" r="3.6" />
            <circle className="hiyoko-spark" cx="74.6" cy="59.6" r="1.35" />
            <path className="hiyoko-eye-lid" d="M65 60h14" />
          </g>

          <ellipse className="hiyoko-cheek" cx="37" cy="70" rx="5.4" ry="3.3" />
          <ellipse className="hiyoko-cheek" cx="83" cy="70" rx="5.4" ry="3.3" />
          <path className="hiyoko-beak" d="M60 66 68 72 60 78 52 72z" />
          <path className="hiyoko-beak-lower" d="M53 72.5 60 79 67 72.5 60 74z" />
        </g>

        <path className="hiyoko-foot" d="M51 102v5M47 107h8" />
        <path className="hiyoko-foot" d="M69 102v5M65 107h8" />
      </g>

      <g className="hiyoko-sparkles" aria-hidden="true">
        <path className="hiyoko-sparkle hiyoko-sparkle-1" d="m17 34 2.4 5.8 5.8 2.4-5.8 2.4L17 50.4l-2.4-5.8L8.8 42.2l5.8-2.4z" />
        <path className="hiyoko-sparkle hiyoko-sparkle-2" d="m103 26 1.8 4.5 4.5 1.8-4.5 1.8-1.8 4.5-1.8-4.5-4.5-1.8 4.5-1.8z" />
        <path className="hiyoko-sparkle hiyoko-sparkle-3" d="m105 72 1.6 4 4 1.6-4 1.6-1.6 4-1.6-4-4-1.6 4-1.6z" />
      </g>

      <g className="hiyoko-question" aria-hidden="true">
        <path d="M98 35c0-4.6 6.4-5.2 6.4-1.2 0 3.6-4.9 3.2-4.9 6.8" />
        <circle cx="99.5" cy="45.5" r="1.8" />
      </g>

      <g className="hiyoko-exclaim" aria-hidden="true">
        <path d="M103 22v13" />
        <circle cx="103" cy="41" r="2" />
      </g>

      <g className="hiyoko-sweat" aria-hidden="true">
        <path d="M30 44c-4 5-5 8-5 10a5 5 0 0 0 10 0c0-2-1-5-5-10z" />
      </g>

      <g className="hiyoko-hearts" aria-hidden="true">
        <path d="M26 25c-2-3.1-6.8-2.4-6.8 1.4 0 2.7 3.1 4.8 6.8 7.3 3.7-2.5 6.8-4.6 6.8-7.3 0-3.8-4.8-4.5-6.8-1.4z" />
      </g>
    </svg>
  )
}
