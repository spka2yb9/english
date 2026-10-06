import './Ingbird.css'
import type { IngbirdMood } from '../services/studyDays'

export type { IngbirdMood }

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
 *
 * いつも小さく揺れていて、まばたきし、ときどき羽を伸ばす。
 * mood で表情と動きが変わる(うれしい・はりきる・お祝い・得意・手ふり・きになる・
 * びっくり・ねむい・てれる・考え中・ごきげん)。絵はインラインSVGなので、
 * テーマの色に合わせられて、拡大しても崩れない。動きはすべてCSSで、
 * prefers-reduced-motion のときは止まる。
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
      <ellipse className="ingbird-shadow" cx="60" cy="111" rx="30" ry="6" />
      <g className="ingbird-inner">
        <path className="ingbird-tail" d="M32 76 12 64l4 24z" />
        <path className="ingbird-wing ingbird-wing-left" d="M31 58q-15 9-10 27 8 2 14-6 6-9 4-21z" />
        <path className="ingbird-wing ingbird-wing-right" d="M89 58q15 9 10 27-8 2-14-6-6-9-4-21z" />
        <ellipse className="ingbird-body" cx="60" cy="64" rx="34" ry="38" />
        <ellipse className="ingbird-belly" cx="61" cy="74" rx="22" ry="25" />
        <g className="ingbird-head">
          <g className="ingbird-eye">
            <g className="ingbird-eye-shape">
              <ellipse className="ingbird-eye-white" cx="49" cy="50" rx="9.5" ry="11" />
              <circle className="ingbird-pupil" cx="50.5" cy="52" r="5" />
              <circle className="ingbird-eye-spark" cx="53" cy="48.5" r="1.8" />
              <path className="ingbird-eye-lid" d="M40 50h18" />
              <path className="ingbird-eye-arc" d="M41.5 52.5q7.5-7 15 0" />
            </g>
          </g>
          <g className="ingbird-eye">
            <g className="ingbird-eye-shape">
              <ellipse className="ingbird-eye-white" cx="71" cy="50" rx="9.5" ry="11" />
              <circle className="ingbird-pupil" cx="72.5" cy="52" r="5" />
              <circle className="ingbird-eye-spark" cx="75" cy="48.5" r="1.8" />
              <path className="ingbird-eye-lid" d="M62 50h18" />
              <path className="ingbird-eye-arc" d="M63.5 52.5q7.5-7 15 0" />
            </g>
          </g>
          <path className="ingbird-brow ingbird-brow-left" d="M40.5 40.5q8.5-4.5 17 0" />
          <path className="ingbird-brow ingbird-brow-right" d="M62.5 40.5q8.5-4.5 17 0" />
          <ellipse className="ingbird-cheek" cx="37" cy="64" rx="6" ry="4" />
          <ellipse className="ingbird-cheek" cx="83" cy="64" rx="6" ry="4" />
          <path className="ingbird-beak" d="M60 57 67.5 64 60 71.5 52.5 64z" />
          <path className="ingbird-beak-lower" d="M53.5 65.5 60 73 66.5 65.5 60 66.4z" />
          <path className="ingbird-cap-base" d="M47 28q13 6 26 0v-6q-13 6-26 0z" />
          <path className="ingbird-cap" d="M60 10 88 21 60 32 32 21z" />
          <g className="ingbird-tassel-group">
            <path className="ingbird-tassel" d="M86 22q7 8 4 17" />
            <circle className="ingbird-tassel-bead" cx="90.5" cy="41.5" r="3.2" />
          </g>
        </g>
        <path className="ingbird-foot" d="M50 100v6M46 106h8" />
        <path className="ingbird-foot" d="M70 100v6M66 106h8" />
      </g>

      {/* 気分で見え方が変わる飾り。すべて装飾なので読み上げない。 */}
      <g className="ingbird-sparkles" aria-hidden="true">
        <path className="ingbird-sparkle-1" d="m13 13 2.6 6.4L22 22l-6.4 2.6L13 31l-2.6-6.4L4 22l6.4-2.6z" />
        <path className="ingbird-sparkle-2" d="m104 10 2 5 5 2-5 2-2 5-2-5-5-2 5-2z" />
        <path className="ingbird-sparkle-3" d="m108 44 1.7 4.3L114 50l-4.3 1.7L108 56l-1.7-4.3L102 50l4.3-1.7z" />
      </g>
      <g className="ingbird-hearts" aria-hidden="true">
        <path className="ingbird-heart-1" d="M18 46c-2.2-3.4-7.4-2.6-7.4 1.5 0 3 3.4 5.3 7.4 8 4-2.7 7.4-5 7.4-8 0-4.1-5.2-4.9-7.4-1.5z" />
        <path className="ingbird-heart-2" d="M32 30c-1.4-2.2-4.8-1.7-4.8 1 0 1.9 2.2 3.4 4.8 5.1 2.6-1.7 4.8-3.2 4.8-5.1 0-2.7-3.4-3.2-4.8-1z" />
      </g>
      <g className="ingbird-notes" aria-hidden="true">
        <g className="ingbird-note-1">
          <path d="M99 22v12" />
          <ellipse cx="95.8" cy="34.5" rx="3.6" ry="2.9" />
        </g>
        <g className="ingbird-note-2">
          <path d="M109 13v11" />
          <ellipse cx="105.8" cy="24.5" rx="3.4" ry="2.7" />
        </g>
      </g>
      <g className="ingbird-zzz" aria-hidden="true">
        <path className="ingbird-z-1" d="M94 31h8l-8 9h8" />
        <path className="ingbird-z-2" d="M104 15h6l-6 7h6" />
      </g>
      <g className="ingbird-question" aria-hidden="true">
        <path d="M99 17c0-3.6 5-4 5-.9 0 2.8-3.8 2.5-3.8 5.3" />
        <circle cx="100.2" cy="26" r="1.6" />
      </g>
      <g className="ingbird-bang" aria-hidden="true">
        <path d="M102 12v11" />
        <circle cx="102" cy="29" r="2.2" />
      </g>
      <g className="ingbird-thought" aria-hidden="true">
        <circle cx="92" cy="42" r="2.2" />
        <circle cx="100" cy="33" r="3.2" />
        <circle cx="109" cy="22" r="4.4" />
      </g>
    </svg>
  )
}
