import './Ingbird.css'
import { BackAccessoryParts, EffectParts, FrontAccessoryParts, GlassesParts, HatParts, ShoeParts } from './IngbirdOutfit'
import type { IngbirdMood } from '../services/studyDays'
import type { IngbirdEvolution } from '../services/ingbirdEvolution'
import { DEFAULT_OUTFIT, type IngbirdOutfit } from '../content/ingbird/outfits'

export type { IngbirdMood }

type Props = {
  mood?: IngbirdMood
  /** 学習日トータルに応じた進化段階(0〜5)。 */
  evolution?: IngbirdEvolution
  /** 着せかえ(メガネ・帽子・エフェクト・小物)。 */
  outfit?: IngbirdOutfit
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
 * びっくり・ねむい・てれる・考え中・ごきげん)。
 * evolution で、学習日トータルに応じた進化の見た目(金色のオーラ・逆立つ羽・雷・浮遊岩・
 * 光る目・環)が重なる。outfit で、メガネ・帽子・エフェクト・小物を着せられる。
 * 絵はインラインSVGなので、テーマの色に合わせられて、拡大しても崩れない。
 * 動きはすべてCSSで、prefers-reduced-motion のときは止まる。
 */
export function Ingbird({
  mood = 'idle',
  evolution = 0,
  outfit = DEFAULT_OUTFIT,
  size = 120,
  decorative = false,
  className,
}: Props) {
  return (
    <svg
      className={className ? `ingbird ${className}` : 'ingbird'}
      width={size}
      height={size}
      viewBox="0 0 120 120"
      data-mood={mood}
      data-evolution={evolution}
      data-glasses={outfit.glasses}
      data-hat={outfit.hat}
      data-effect={outfit.effect}
      data-accessory={outfit.accessory}
      data-shoes={outfit.shoes}
      role={decorative ? undefined : 'img'}
      aria-hidden={decorative || undefined}
      aria-label={decorative ? undefined : 'イングバード'}
      focusable="false"
    >
      <ellipse className="ingbird-shadow" cx="60" cy="111" rx="30" ry="6" />

      {/* 進化で重なる背景。0のときはすべて透明 */}
      <g className={`ingbird-halo-ring${evolution >= 5 ? ' is-on' : ''}`} aria-hidden="true">
        <ellipse className="ingbird-halo" cx="60" cy="16" rx="38" ry="10" />
        <ellipse className="ingbird-halo ingbird-halo-2" cx="60" cy="16" rx="45" ry="13" />
      </g>
      <g className={`ingbird-aura${evolution >= 1 ? ' is-on' : ''}`} aria-hidden="true">
        <ellipse className="ingbird-aura-ring ingbird-aura-ring-1" cx="60" cy="66" rx="55" ry="57" />
        <ellipse className="ingbird-aura-ring ingbird-aura-ring-2" cx="60" cy="66" rx="47" ry="49" />
      </g>
      <g className={`ingbird-rocks${evolution >= 2 ? ' is-on' : ''}`} aria-hidden="true">
        <path className="ingbird-rock ingbird-rock-1" d="m15 89 6-4 5 4-2 6-7 1z" />
        <path className="ingbird-rock ingbird-rock-2" d="m97 80 7-2 4 5-5 5-6-3z" />
        <path className="ingbird-rock ingbird-rock-3" d="m24 48 4-3 4 4-3 5-5-2z" />
        <path className="ingbird-rock ingbird-rock-4" d="m94 55 5-3 4 4-4 5-5-2z" />
      </g>
      <g className={`ingbird-embers${evolution >= 3 ? ' is-on' : ''}`} aria-hidden="true">
        <circle className="ingbird-ember ingbird-ember-1" cx="22" cy="90" r="2.2" />
        <circle className="ingbird-ember ingbird-ember-2" cx="33" cy="102" r="1.7" />
        <circle className="ingbird-ember ingbird-ember-3" cx="88" cy="96" r="2.4" />
        <circle className="ingbird-ember ingbird-ember-4" cx="99" cy="86" r="1.8" />
        <circle className="ingbird-ember ingbird-ember-5" cx="12" cy="74" r="1.9" />
        <circle className="ingbird-ember ingbird-ember-6" cx="108" cy="70" r="2.1" />
      </g>
      <g className={`ingbird-lightning${evolution >= 3 ? ' is-on' : ''}`} aria-hidden="true">
        <path className="ingbird-bolt ingbird-bolt-1" d="m22 20-8 15h6l-4 12 14-18h-6l5-9z" />
        <path className="ingbird-bolt ingbird-bolt-2" d="m101 33-6 12h5l-3 10 11-14h-5l4-8z" />
        <path className="ingbird-bolt ingbird-bolt-3" d="m97 84-5 10h4l-2 8 9-12h-4l3-6z" />
      </g>

      <g className="ingbird-inner">
        <BackAccessoryParts id={outfit.accessory} />
        <path className="ingbird-tail" d="M32 76 12 64l4 24z" />
        <path className="ingbird-wing ingbird-wing-left" d="M31 58q-15 9-10 27 8 2 14-6 6-9 4-21z" />
        <path className="ingbird-wing ingbird-wing-right" d="M89 58q15 9 10 27-8 2-14-6-6-9-4-21z" />
        <ellipse className="ingbird-body" cx="60" cy="64" rx="34" ry="38" />
        <ellipse className="ingbird-belly" cx="61" cy="74" rx="22" ry="25" />

        <FrontAccessoryParts id={outfit.accessory} />
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
          {/* 進化4で光る目 */}
          <g className={`ingbird-evolution-eyes${evolution >= 4 ? ' is-on' : ''}`} aria-hidden="true">
            <circle cx="50.5" cy="52" r="7" />
            <circle cx="72.5" cy="52" r="7" />
          </g>
          <ellipse className="ingbird-cheek" cx="37" cy="64" rx="6" ry="4" />
          <ellipse className="ingbird-cheek" cx="83" cy="64" rx="6" ry="4" />
          <path className="ingbird-beak" d="M60 57 67.5 64 60 71.5 52.5 64z" />
          <path className="ingbird-beak-lower" d="M53.5 65.5 60 73 66.5 65.5 60 66.4z" />
          {/* 進化2で逆立つ金の羽(キャップの下に重ねる) */}
          <g className={`ingbird-crest${evolution >= 2 ? ' is-on' : ''}`} aria-hidden="true">
            <path className="ingbird-crest-spike" d="M52 11 46 0l8 6 6-6 6 6 8-6-6 11z" />
            <path className="ingbird-crest-spike ingbird-crest-side" d="M44 15 35 5l9 5 3-7 4 9z" />
            <path className="ingbird-crest-spike ingbird-crest-side" d="M76 15 85 5l-9 5-3-7-4 9z" />
          </g>
          <HatParts id={outfit.hat} />
          {/* メガネは最後に描いて、目の上にフレームを重ねる */}
          <GlassesParts id={outfit.glasses} />
        </g>
        <path className="ingbird-foot" d="M50 100v6M46 106h8" />
        <path className="ingbird-foot" d="M70 100v6M66 106h8" />
        <ShoeParts id={outfit.shoes} />
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

      {/* 着せかえのエフェクト */}
      <EffectParts id={outfit.effect} />
    </svg>
  )
}
