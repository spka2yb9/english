// イングバードの着せかえパーツ。SVGの形だけを持ち、色と動きは CSS で付ける。
// どのパーツも aria-hidden。学習の意味はカード側のテキストが伝える。

import './IngbirdOutfit.css'
import type { AccessoryId, EffectId, GlassesId, HatId, ShoeId } from '../content/ingbird/outfits'

export function HatParts({ id }: { id: HatId }) {
  switch (id) {
    case 'none':
      return null
    case 'grad':
      return (
        <>
          <path className="ingbird-cap-base" d="M47 28q13 6 26 0v-6q-13 6-26 0z" />
          <path className="ingbird-cap" d="M60 10 88 21 60 32 32 21z" />
          <g className="ingbird-tassel-group">
            <path className="ingbird-tassel" d="M86 22q7 8 4 17" />
            <circle className="ingbird-tassel-bead" cx="90.5" cy="41.5" r="3.2" />
          </g>
        </>
      )
    case 'beanie':
      return (
        <g className="ingbird-hat ingbird-hat-beanie" aria-hidden="true">
          <path className="ingbird-beanie" d="M41 27q0-17 19-17t19 17z" />
          <path className="ingbird-beanie-brim" d="M38 25h44v8H38z" />
          <circle className="ingbird-beanie-pom" cx="60" cy="7" r="4.6" />
        </g>
      )
    case 'cap':
      return (
        <g className="ingbird-hat ingbird-hat-cap" aria-hidden="true">
          <path className="ingbird-fabric-teal" d="M42 27q0-16 18-16t18 16z" />
          <path className="ingbird-fabric-navy" d="M73 23h16q4 0 4 3t-4 3H72z" />
        </g>
      )
    case 'beret':
      return (
        <g className="ingbird-hat ingbird-hat-beret" aria-hidden="true">
          <ellipse className="ingbird-fabric-red" cx="59" cy="22" rx="22" ry="10" transform="rotate(-7 59 22)" />
          <circle className="ingbird-fabric-red" cx="65" cy="9" r="2.6" />
        </g>
      )
    case 'headband':
      return (
        <g className="ingbird-hat ingbird-hat-headband" aria-hidden="true">
          <path className="ingbird-fabric-teal" d="M38 26q22-10 44 0v6q-22-9-44 0z" />
          <path className="ingbird-fabric-gold" d="M38 27l-8-8 2 9z" />
        </g>
      )
    case 'flower':
      return (
        <g className="ingbird-hat ingbird-hat-flower" aria-hidden="true">
          <path className="ingbird-fabric-green" d="M39 27q21-9 42 0v5q-21-8-42 0z" />
          <circle className="ingbird-fabric-pink" cx="44" cy="23" r="3.4" />
          <circle className="ingbird-fabric-cream" cx="52" cy="20" r="3" />
          <circle className="ingbird-fabric-pink" cx="60" cy="19" r="3.4" />
          <circle className="ingbird-fabric-cream" cx="68" cy="20" r="3" />
          <circle className="ingbird-fabric-pink" cx="76" cy="23" r="3.4" />
        </g>
      )
    case 'party':
      return (
        <g className="ingbird-hat ingbird-hat-party" aria-hidden="true">
          <path className="ingbird-fabric-pink" d="M60 4 46 27h28z" />
          <path className="ingbird-fabric-cream" d="M52 15h16l5 8H47z" />
          <circle className="ingbird-fabric-gold" cx="60" cy="4" r="3.4" />
        </g>
      )
    case 'crown':
      return (
        <g className="ingbird-hat ingbird-hat-crown" aria-hidden="true">
          <path className="ingbird-crown" d="M42 28V13l9 7 9-12 9 12 9-7v15z" />
          <circle className="ingbird-crown-jewel" cx="60" cy="22" r="2.6" />
        </g>
      )
    case 'wizard':
      return (
        <g className="ingbird-hat ingbird-hat-wizard" aria-hidden="true">
          <ellipse className="ingbird-wizard-brim" cx="60" cy="27" rx="25" ry="6" />
          <path className="ingbird-wizard-cone" d="M60 2 46 27h28z" />
          <path className="ingbird-wizard-star" d="m60 13 1.8 4.4 4.4 1.8-4.4 1.8L60 25l-1.8-4.4-4.4-1.8 4.4-1.8z" />
        </g>
      )
    case 'santa':
      return (
        <g className="ingbird-hat ingbird-hat-santa" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M45 24q0-16 15-16t15 16z" />
          <path className="ingbird-fabric-cream" d="M39 23q21-8 42 0v7q-21-8-42 0z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="6" r="3.6" />
        </g>
      )
    case 'chef':
      return (
        <g className="ingbird-hat ingbird-hat-chef" aria-hidden="true">
          <path className="ingbird-fabric-cream" d="M44 26q-9-1-9-9 0-8 10-8 3-6 11-6t10 7q9-1 9 7 0 7-9 9z" />
          <path className="ingbird-fabric-silver" d="M44 26h32v6H44z" />
        </g>
      )
    case 'pirate':
      return (
        <g className="ingbird-hat ingbird-hat-pirate" aria-hidden="true">
          <path className="ingbird-fabric-dark" d="M35 27q25-20 50 0-12 6-25 6t-25-6z" />
          <path className="ingbird-line-cream" d="M60 16v8M56 19h8" />
        </g>
      )
    case 'cowboy':
      return (
        <g className="ingbird-hat ingbird-hat-cowboy" aria-hidden="true">
          <ellipse className="ingbird-fabric-brown" cx="60" cy="26" rx="30" ry="7" />
          <path className="ingbird-fabric-brown" d="M46 26q0-12 14-12t14 12z" />
          <path className="ingbird-fabric-gold" d="M46 25h28v3H46z" />
        </g>
      )
    case 'mushroom':
      return (
        <g className="ingbird-hat ingbird-hat-mushroom" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M36 26q0-17 24-17t24 17z" />
          <circle className="ingbird-fabric-cream" cx="49" cy="17" r="3" />
          <circle className="ingbird-fabric-cream" cx="63" cy="13" r="2.6" />
          <circle className="ingbird-fabric-cream" cx="73" cy="20" r="2.4" />
        </g>
      )
    case 'top':
      return (
        <g className="ingbird-hat ingbird-hat-top" aria-hidden="true">
          <path className="ingbird-fabric-dark" d="M46 4h28v22H46z" />
          <ellipse className="ingbird-fabric-dark" cx="60" cy="26" rx="24" ry="4.2" />
          <path className="ingbird-fabric-red" d="M46 18h28v5H46z" />
        </g>
      )
    case 'crown_gold':
      return (
        <g className="ingbird-hat ingbird-hat-crown_gold" aria-hidden="true">
          <path className="ingbird-fabric-gold-strong" d="M40 29V11l10 8 10-13 10 13 10-8v18z" />
          <circle className="ingbird-fabric-pink" cx="60" cy="22" r="2.8" />
          <circle className="ingbird-fabric-pink" cx="49" cy="24" r="2" />
          <circle className="ingbird-fabric-pink" cx="71" cy="24" r="2" />
        </g>
      )
    case 'halo':
      return (
        <g className="ingbird-hat ingbird-hat-halo" aria-hidden="true">
          <ellipse className="ingbird-line-gold" cx="60" cy="8" rx="18" ry="4.5" />
        </g>
      )
    case 'straw':
      return (
        <g className="ingbird-hat ingbird-hat-straw" aria-hidden="true">
          <ellipse className="ingbird-fabric-straw" cx="60" cy="26" rx="31" ry="7" />
          <path className="ingbird-fabric-straw" d="M44 26q0-12 16-12t16 12z" />
          <path className="ingbird-fabric-red" d="M44 23h32v4H44z" />
        </g>
      )
    case 'propeller':
      return (
        <g className="ingbird-hat ingbird-hat-propeller" aria-hidden="true">
          <path className="ingbird-fabric-teal" d="M42 27q0-15 18-15t18 15z" />
          <path className="ingbird-hat-stem" d="M60 12V5" />
          <path className="ingbird-fabric-red" d="M46 3h28v4H46z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="5" r="2.2" />
        </g>
      )
    case 'cat_ears':
      return (
        <g className="ingbird-hat ingbird-hat-cat_ears" aria-hidden="true">
          <path className="ingbird-fabric-dark" d="M42 25 38 8l15 10z" />
          <path className="ingbird-fabric-dark" d="M78 25 82 8 67 18z" />
          <path className="ingbird-fabric-pink" d="M44 21 42 12l8 6z" />
          <path className="ingbird-fabric-pink" d="M76 21 78 12l-8 6z" />
        </g>
      )
    case 'bunny_ears':
      return (
        <g className="ingbird-hat ingbird-hat-bunny_ears" aria-hidden="true">
          <ellipse className="ingbird-fabric-cream" cx="49" cy="10" rx="5" ry="13" transform="rotate(-10 49 10)" />
          <ellipse className="ingbird-fabric-cream" cx="71" cy="10" rx="5" ry="13" transform="rotate(10 71 10)" />
          <ellipse className="ingbird-fabric-pink" cx="49" cy="11" rx="2.4" ry="8" transform="rotate(-10 49 11)" />
          <ellipse className="ingbird-fabric-pink" cx="71" cy="11" rx="2.4" ry="8" transform="rotate(10 71 11)" />
        </g>
      )
    case 'turban':
      return (
        <g className="ingbird-hat ingbird-hat-turban" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M41 27q0-17 19-17t19 17z" />
          <path className="ingbird-fabric-red" d="M41 22q19-7 38 0v6q-19-6-38 0z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="16" r="3.4" />
        </g>
      )
    case 'sombrero':
      return (
        <g className="ingbird-hat ingbird-hat-sombrero" aria-hidden="true">
          <ellipse className="ingbird-fabric-straw" cx="60" cy="27" rx="34" ry="6" />
          <path className="ingbird-fabric-straw" d="M48 27q0-14 12-14t12 14z" />
          <path className="ingbird-fabric-red" d="M48 24h24v4H48z" />
        </g>
      )
    case 'viking':
      return (
        <g className="ingbird-hat ingbird-hat-viking" aria-hidden="true">
          <path className="ingbird-fabric-silver" d="M41 26q0-16 19-16t19 16z" />
          <path className="ingbird-fabric-cream" d="M48 13 39 2l11 4z" />
          <path className="ingbird-fabric-cream" d="M72 13 81 2 70 6z" />
          <path className="ingbird-fabric-silver" d="M57 26h6v6h-6z" />
        </g>
      )
    case 'knight':
      return (
        <g className="ingbird-hat ingbird-hat-knight" aria-hidden="true">
          <path className="ingbird-fabric-silver" d="M41 28V18q0-10 19-10t19 10v10z" />
          <path className="ingbird-fabric-dark" d="M50 17h20v3H50zM50 23h20v3H50z" />
          <path className="ingbird-fabric-red" d="M60 7v6" />
        </g>
      )
    case 'jester':
      return (
        <g className="ingbird-hat ingbird-hat-jester" aria-hidden="true">
          <path className="ingbird-fabric-plum" d="M43 26 30 10l14 5z" />
          <path className="ingbird-fabric-red" d="M60 26V6l10 12z" />
          <path className="ingbird-fabric-gold" d="M77 26 90 10l-14 5z" />
          <circle className="ingbird-fabric-cream" cx="30" cy="9" r="2.6" />
          <circle className="ingbird-fabric-cream" cx="60" cy="5" r="2.6" />
          <circle className="ingbird-fabric-cream" cx="90" cy="9" r="2.6" />
        </g>
      )
    case 'helmet':
      return (
        <g className="ingbird-hat ingbird-hat-helmet" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M40 27q0-17 20-17t20 17z" />
          <path className="ingbird-fabric-dark" d="M39 26h42v4H39z" />
          <path className="ingbird-fabric-cream" d="M53 17h14v3H53z" />
        </g>
      )
    case 'tiara':
      return (
        <g className="ingbird-hat ingbird-hat-tiara" aria-hidden="true">
          <path className="ingbird-fabric-gold-strong" d="M42 26V18l6 4 6-8 6 8 6-8 6 8 6-4v8z" />
          <circle className="ingbird-fabric-pink" cx="60" cy="16" r="2.4" />
        </g>
      )
    case 'antenna':
      return (
        <g className="ingbird-hat ingbird-hat-antenna" aria-hidden="true">
          <path className="ingbird-antenna-stem" d="M52 18 46 6M68 18l6-12" />
          <circle className="ingbird-fabric-pink" cx="46" cy="5" r="3" />
          <circle className="ingbird-fabric-teal" cx="74" cy="5" r="3" />
          <path className="ingbird-fabric-navy" d="M44 24q16-8 32 0v5q-16-7-32 0z" />
        </g>
      )
    case 'demon_horns':
      return (
        <g className="ingbird-hat ingbird-hat-demon_horns" aria-hidden="true">
          <path className="ingbird-dark-horn" d="M45 22Q37 8 47 1q2 10 8 14z" />
          <path className="ingbird-dark-horn" d="M75 22Q83 8 73 1q-2 10-8 14z" />
        </g>
      )
    case 'cursed_crown':
      return (
        <g className="ingbird-hat ingbird-hat-cursed_crown" aria-hidden="true">
          <path className="ingbird-dark-metal" d="M42 28V13l9 7 9-12 9 12 9-7v15z" />
          <circle className="ingbird-dark-gem" cx="60" cy="22" r="2.6" />
        </g>
      )
    case 'skull_helm':
      return (
        <g className="ingbird-hat ingbird-hat-skull_helm" aria-hidden="true">
          <path className="ingbird-dark-bone" d="M42 26q0-16 18-16t18 16v6H42z" />
          <circle className="ingbird-dark-hollow" cx="52" cy="19" r="3" />
          <circle className="ingbird-dark-hollow" cx="68" cy="19" r="3" />
          <path className="ingbird-dark-hollow" d="M57 26h6l-3 4z" />
        </g>
      )
    case 'dark_hood':
      return (
        <g className="ingbird-hat ingbird-hat-dark_hood" aria-hidden="true">
          <path className="ingbird-dark-cloth" d="M36 30q0-24 24-24t24 24l-8 4q-16-8-32 0z" />
          <path className="ingbird-dark-shadow" d="M44 30q16-8 32 0v4q-16-6-32 0z" />
        </g>
      )
    case 'dragon_horns':
      return (
        <g className="ingbird-hat ingbird-hat-dragon_horns" aria-hidden="true">
          <path className="ingbird-dark-horn" d="M48 20 38 4l12 8 2-10 6 14z" />
          <path className="ingbird-dark-horn" d="M72 20 82 4 70 12 68 2l-6 14z" />
        </g>
      )
    case 'abyss_crown':
      return (
        <g className="ingbird-hat ingbird-hat-abyss_crown" aria-hidden="true">
          <path className="ingbird-dark-metal" d="M40 29V11l10 8 10-13 10 13 10-8v18z" />
          <circle className="ingbird-dark-gem" cx="60" cy="22" r="3" />
          <path className="ingbird-dark-gem" d="m48 14 2 4 4 2-4 2-2 4-2-4-4-2 4-2z" />
        </g>
      )
    case 'sun_hat':
      return (
        <g className="ingbird-hat ingbird-hat-sun_hat" aria-hidden="true">
          <ellipse className="ingbird-fabric-straw" cx="60" cy="27" rx="30" ry="6" />
          <path className="ingbird-fabric-straw" d="M45 27q0-13 15-13t15 13z" />
          <path className="ingbird-fabric-teal" d="M45 24h30v4H45z" />
        </g>
      )
    case 'sailor':
      return (
        <g className="ingbird-hat ingbird-hat-sailor" aria-hidden="true">
          <path className="ingbird-fabric-white" d="M44 27q0-14 16-14t16 14z" />
          <path className="ingbird-fabric-navy" d="M44 24h32v4H44z" />
          <circle className="ingbird-fabric-gold" cx="60" cy="13" r="2.4" />
        </g>
      )
    case 'beanie_stripe':
      return (
        <g className="ingbird-hat ingbird-hat-beanie_stripe" aria-hidden="true">
          <path className="ingbird-fabric-teal" d="M41 27q0-17 19-17t19 17z" />
          <path className="ingbird-fabric-cream" d="M42 20q18-8 36 0v4q-18-8-36 0z" />
          <path className="ingbird-fabric-teal" d="M38 25h44v8H38z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="7" r="4" />
        </g>
      )
    case 'graduation_gold':
      return (
        <g className="ingbird-hat ingbird-hat-graduation_gold" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M47 28q13 6 26 0v-6q-13 6-26 0z" />
          <path className="ingbird-fabric-gold-strong" d="M60 10 88 21 60 32 32 21z" />
          <path className="ingbird-gold-tassel" d="M86 22q7 8 4 17" />
          <circle className="ingbird-fabric-gold" cx="90.5" cy="41.5" r="3" />
        </g>
      )
    case 'witch_black':
      return (
        <g className="ingbird-hat ingbird-hat-witch_black" aria-hidden="true">
          <ellipse className="ingbird-hat-black" cx="60" cy="28" rx="26" ry="6" />
          <path className="ingbird-hat-black" d="M60 2 46 28h28z" />
          <path className="ingbird-dark-trim" d="M47 25h26v4H47z" />
          <path className="ingbird-shoe-star" d="m64 16 1.4 3.4 3.4 1.4-3.4 1.4-1.4 3.4-1.4-3.4-3.4-1.4 3.4-1.4z" />
        </g>
      )
    case 'flower_crown':
      return (
        <g className="ingbird-hat ingbird-hat-flower_crown" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M39 27q21-9 42 0v5q-21-8-42 0z" />
          <circle className="ingbird-fabric-pink" cx="44" cy="23" r="3" />
          <circle className="ingbird-fabric-cream" cx="52" cy="20" r="2.6" />
          <circle className="ingbird-fabric-pink" cx="60" cy="19" r="3" />
          <circle className="ingbird-fabric-cream" cx="68" cy="20" r="2.6" />
          <circle className="ingbird-fabric-pink" cx="76" cy="23" r="3" />
          <circle className="ingbird-fabric-teal" cx="52" cy="25" r="1.4" />
          <circle className="ingbird-fabric-teal" cx="68" cy="25" r="1.4" />
        </g>
      )
    case 'samurai':
      return (
        <g className="ingbird-hat ingbird-hat-samurai" aria-hidden="true">
          <path className="ingbird-dark-metal" d="M40 27q0-17 20-17t20 17z" />
          <path className="ingbird-fabric-gold" d="M52 12 44 2l10 4 6-6 6 6 10-4-8 10z" />
          <path className="ingbird-dark-trim" d="M40 25h40v4H40z" />
        </g>
      )
    case 'phoenix':
      return (
        <g className="ingbird-hat ingbird-hat-phoenix" aria-hidden="true">
          <path className="ingbird-phoenix-1" d="M60 28q-12-10-8-24 6 6 8 8 0-8 0-12 4 6 8 12 4 6-8 16z" />
          <path className="ingbird-phoenix-2" d="M52 20q-8-4-10-10 6 0 10 4zM68 20q8-4 10-10-6 0-10 4z" />
        </g>
      )
    default:
      return null
  }
}

export function GlassesParts({ id }: { id: GlassesId }) {
  switch (id) {
    case 'none':
      return null
    case 'round':
      return (
        <g className="ingbird-glasses ingbird-glasses-round" aria-hidden="true">
          <circle cx="49" cy="50" r="9.5" />
          <circle cx="71" cy="50" r="9.5" />
          <path d="M58.5 50h3" />
          <path d="M39.5 48 33 45M80.5 48 87 45" />
        </g>
      )
    case 'square':
      return (
        <g className="ingbird-glasses ingbird-glasses-square" aria-hidden="true">
          <rect className="ingbird-lens" x="38" y="41" width="20" height="17" rx="2" />
          <rect className="ingbird-lens" x="62" y="41" width="20" height="17" rx="2" />
          <path className="ingbird-frame" d="M58 48h4M38 45 32 43M82 45 88 43" />
        </g>
      )
    case 'sunglasses':
      return (
        <g className="ingbird-glasses ingbird-glasses-sunglasses" aria-hidden="true">
          <rect x="38" y="41" width="20" height="16" rx="4" />
          <rect x="62" y="41" width="20" height="16" rx="4" />
          <path className="ingbird-glasses-bridge" d="M58 46h4" />
          <path className="ingbird-glasses-arm" d="M38 44 32 42M82 44 88 42" />
        </g>
      )
    case 'star':
      return (
        <g className="ingbird-glasses ingbird-glasses-star" aria-hidden="true">
          <path d="m49 38 2.9 7.1L59 48l-7.1 2.9L49 58l-2.9-7.1L39 48l7.1-2.9z" />
          <path d="m71 38 2.9 7.1L81 48l-7.1 2.9L71 58l-2.9-7.1L61 48l7.1-2.9z" />
        </g>
      )
    case 'heart':
      return (
        <g className="ingbird-glasses ingbird-glasses-heart" aria-hidden="true">
          <path className="ingbird-lens-heart" d="M49 60c-7-4.5-11-7.5-11-11.5a5.5 5.5 0 0 1 11-1.5 5.5 5.5 0 0 1 11 1.5c0 4-4 7-11 11.5z" />
          <path className="ingbird-lens-heart" d="M71 60c-7-4.5-11-7.5-11-11.5a5.5 5.5 0 0 1 11-1.5 5.5 5.5 0 0 1 11 1.5c0 4-4 7-11 11.5z" />
        </g>
      )
    case 'monocle':
      return (
        <g className="ingbird-glasses ingbird-glasses-monocle" aria-hidden="true">
          <circle className="ingbird-lens" cx="71" cy="50" r="11" />
          <path className="ingbird-frame" d="M82 54q6 7 3 14" />
        </g>
      )
    case 'oval':
      return (
        <g className="ingbird-glasses ingbird-glasses-oval" aria-hidden="true">
          <ellipse className="ingbird-lens" cx="49" cy="50" rx="10.5" ry="8" />
          <ellipse className="ingbird-lens" cx="71" cy="50" rx="10.5" ry="8" />
          <path className="ingbird-frame" d="M59.5 50h1M38.5 48 33 46M81.5 48 87 46" />
        </g>
      )
    case 'pixel':
      return (
        <g className="ingbird-glasses ingbird-glasses-pixel" aria-hidden="true">
          <rect className="ingbird-lens" x="37" y="42" width="21" height="16" />
          <rect className="ingbird-lens" x="62" y="42" width="21" height="16" />
          <path className="ingbird-frame" d="M58 47h4v5h-4zM37 44 31 42M83 44 89 42" />
        </g>
      )
    case 'sport':
      return (
        <g className="ingbird-glasses ingbird-glasses-sport" aria-hidden="true">
          <path className="ingbird-shield" d="M35 43q25-5 50 0 2 8-5 12-10 5-20 5t-20-5q-7-4-5-12z" />
          <path className="ingbird-shield-glint" d="M43 47q8-2 16 0" />
          <path className="ingbird-frame" d="M35 45 29 42M85 45 91 42" />
        </g>
      )
    case 'reading':
      return (
        <g className="ingbird-glasses ingbird-glasses-reading" aria-hidden="true">
          <path className="ingbird-lens" d="M39 47h16v2a8 8 0 0 1-16 0z" />
          <path className="ingbird-lens" d="M65 47h16v2a8 8 0 0 1-16 0z" />
          <path className="ingbird-frame" d="M59 48h2M39 47l-6-2M81 47l6-2" />
        </g>
      )
    case 'rainbow':
      return (
        <g className="ingbird-glasses ingbird-glasses-rainbow" aria-hidden="true">
          <circle className="ingbird-rb-1" cx="49" cy="50" r="11" />
          <circle className="ingbird-rb-2" cx="49" cy="50" r="8.5" />
          <circle className="ingbird-rb-3" cx="49" cy="50" r="6" />
          <circle className="ingbird-rb-1" cx="71" cy="50" r="11" />
          <circle className="ingbird-rb-2" cx="71" cy="50" r="8.5" />
          <circle className="ingbird-rb-3" cx="71" cy="50" r="6" />
        </g>
      )
    case 'visor':
      return (
        <g className="ingbird-glasses ingbird-glasses-visor" aria-hidden="true">
          <path className="ingbird-visor" d="M33 45q27-9 54 0v7q-27 8-54 0z" />
          <path className="ingbird-frame" d="M33 47 27 44M87 47 93 44" />
        </g>
      )
    case 'goggles':
      return (
        <g className="ingbird-glasses ingbird-glasses-goggles" aria-hidden="true">
          <circle className="ingbird-goggle" cx="49" cy="50" r="10" />
          <circle className="ingbird-goggle" cx="71" cy="50" r="10" />
          <path className="ingbird-goggle-strap" d="M39 48H30M81 48h9M59 50h2" />
        </g>
      )
    case 'cat_eye':
      return (
        <g className="ingbird-glasses ingbird-glasses-cat_eye" aria-hidden="true">
          <path className="ingbird-lens" d="M38 51q1-10 11-10 9 0 10 6-3 8-11 8t-10-4z" />
          <path className="ingbird-lens" d="M82 51q-1-10-11-10-9 0-10 6 3 8 11 8t10-4z" />
          <path className="ingbird-frame" d="M59 49h2M38 44 32 41M82 44 88 41" />
        </g>
      )
    case 'aviator':
      return (
        <g className="ingbird-glasses ingbird-glasses-aviator" aria-hidden="true">
          <path className="ingbird-lens-gold" d="M38 43h20q2 10-4 13-9 4-14-2-3-4-2-11z" />
          <path className="ingbird-lens-gold" d="M82 43H62q-2 10 4 13 9 4 14-2 3-4 2-11z" />
          <path className="ingbird-frame-gold" d="M58 46h4M38 44 32 41M82 44 88 41" />
        </g>
      )
    case 'rimless':
      return (
        <g className="ingbird-glasses ingbird-glasses-rimless" aria-hidden="true">
          <ellipse className="ingbird-lens-rimless" cx="49" cy="50" rx="10" ry="8" />
          <ellipse className="ingbird-lens-rimless" cx="71" cy="50" rx="10" ry="8" />
          <path className="ingbird-frame-rimless" d="M59 50h2M39 49l-6-1M81 49l6-1" />
        </g>
      )
    case 'diamond':
      return (
        <g className="ingbird-glasses ingbird-glasses-diamond" aria-hidden="true">
          <path className="ingbird-lens-diamond" d="m49 40 8 10-8 10-8-10z" />
          <path className="ingbird-lens-diamond" d="m71 40 8 10-8 10-8-10z" />
          <path className="ingbird-frame" d="M57 50h6M33 46l8-4M87 46l-8-4" />
        </g>
      )
    case 'spiral':
      return (
        <g className="ingbird-glasses ingbird-glasses-spiral" aria-hidden="true">
          <path className="ingbird-spiral" d="M49 50a4 4 0 1 1 4 4 8 8 0 1 1-8-8 12 12 0 1 1 12 12" />
          <path className="ingbird-spiral" d="M71 50a4 4 0 1 1 4 4 8 8 0 1 1-8-8 12 12 0 1 1 12 12" />
        </g>
      )
    case '3d':
      return (
        <g className="ingbird-glasses ingbird-glasses-3d" aria-hidden="true">
          <rect className="ingbird-lens-3d-red" x="38" y="42" width="20" height="16" rx="2" />
          <rect className="ingbird-lens-3d-blue" x="62" y="42" width="20" height="16" rx="2" />
          <path className="ingbird-frame" d="M58 48h4M38 45 32 43M82 45 88 43" />
        </g>
      )
    case 'ski':
      return (
        <g className="ingbird-glasses ingbird-glasses-ski" aria-hidden="true">
          <rect className="ingbird-goggle-ski" x="33" y="41" width="54" height="18" rx="9" />
          <path className="ingbird-shield-glint" d="M43 48q8-3 16 0" />
          <path className="ingbird-goggle-strap" d="M33 48H26M87 48h7" />
        </g>
      )
    case 'flower':
      return (
        <g className="ingbird-glasses ingbird-glasses-flower" aria-hidden="true">
          <circle className="ingbird-lens" cx="49" cy="50" r="9" />
          <circle className="ingbird-lens" cx="71" cy="50" r="9" />
          <circle className="ingbird-petal" cx="39" cy="43" r="2.4" />
          <circle className="ingbird-petal" cx="36" cy="50" r="2.4" />
          <circle className="ingbird-petal" cx="39" cy="57" r="2.4" />
          <circle className="ingbird-petal" cx="81" cy="43" r="2.4" />
          <circle className="ingbird-petal" cx="84" cy="50" r="2.4" />
          <circle className="ingbird-petal" cx="81" cy="57" r="2.4" />
          <path className="ingbird-frame" d="M58 50h4" />
        </g>
      )
    case 'cyber':
      return (
        <g className="ingbird-glasses ingbird-glasses-cyber" aria-hidden="true">
          <rect className="ingbird-cyber-frame" x="34" y="42" width="52" height="16" rx="4" />
          <path className="ingbird-cyber-line" d="M40 47h16M64 47h16M48 53h24" />
          <path className="ingbird-cyber-frame" d="M34 47 28 45M86 47l6-2" />
        </g>
      )
    case 'star_legend':
      return (
        <g className="ingbird-glasses ingbird-glasses-star_legend" aria-hidden="true">
          <path className="ingbird-star-legend" d="m49 36 3.4 8.6L61 49l-8.6 3.4L49 61l-3.4-8.6L37 49l8.6-4.4z" />
          <path className="ingbird-star-legend" d="m71 36 3.4 8.6L83 49l-8.6 3.4L71 61l-3.4-8.6L59 49l8.6-4.4z" />
        </g>
      )
    case 'crimson_gaze':
      return (
        <g className="ingbird-glasses ingbird-glasses-crimson_gaze" aria-hidden="true">
          <circle className="ingbird-dark-eye" cx="49" cy="50" r="7" />
          <circle className="ingbird-dark-eye" cx="71" cy="50" r="7" />
        </g>
      )
    case 'cursed_lens':
      return (
        <g className="ingbird-glasses ingbird-glasses-cursed_lens" aria-hidden="true">
          <circle className="ingbird-dark-lens" cx="49" cy="50" r="10" />
          <circle className="ingbird-dark-lens" cx="71" cy="50" r="10" />
          <path className="ingbird-dark-frame" d="M59 50h2M39 48 33 45M81 48 87 45" />
        </g>
      )
    case 'skull_goggles':
      return (
        <g className="ingbird-glasses ingbird-glasses-skull_goggles" aria-hidden="true">
          <rect className="ingbird-dark-metal" x="36" y="42" width="21" height="15" rx="4" />
          <rect className="ingbird-dark-metal" x="63" y="42" width="21" height="15" rx="4" />
          <path className="ingbird-dark-frame" d="M57 47h6M36 46 30 44M84 46l6-2" />
        </g>
      )
    case 'abyss_mask':
      return (
        <g className="ingbird-glasses ingbird-glasses-abyss_mask" aria-hidden="true">
          <path className="ingbird-dark-mask" d="M34 42q26-8 52 0v18q-26 8-52 0z" />
          <path className="ingbird-dark-slit" d="M42 49h14M64 49h14" />
        </g>
      )
    case 'demon_eyes':
      return (
        <g className="ingbird-glasses ingbird-glasses-demon_eyes" aria-hidden="true">
          <ellipse className="ingbird-dark-eye" cx="49" cy="50" rx="6" ry="7" />
          <ellipse className="ingbird-dark-eye" cx="71" cy="50" rx="6" ry="7" />
          <path className="ingbird-dark-pupil" d="M49 44v12M71 44v12" />
        </g>
      )
    case 'tinted':
      return (
        <g className="ingbird-glasses ingbird-glasses-tinted" aria-hidden="true">
          <circle className="ingbird-lens-tinted" cx="49" cy="50" r="9.5" />
          <circle className="ingbird-lens-tinted" cx="71" cy="50" r="9.5" />
          <path className="ingbird-frame" d="M58.5 50h3M39.5 48 33 45M80.5 48 87 45" />
        </g>
      )
    case 'butterfly':
      return (
        <g className="ingbird-glasses ingbird-glasses-butterfly" aria-hidden="true">
          <ellipse className="ingbird-lens-butterfly" cx="44" cy="45" rx="7.5" ry="4.4" transform="rotate(-22 44 45)" />
          <ellipse className="ingbird-lens-butterfly" cx="54" cy="55" rx="7.5" ry="4.4" transform="rotate(22 54 55)" />
          <ellipse className="ingbird-lens-butterfly" cx="66" cy="55" rx="7.5" ry="4.4" transform="rotate(-22 66 55)" />
          <ellipse className="ingbird-lens-butterfly" cx="76" cy="45" rx="7.5" ry="4.4" transform="rotate(22 76 45)" />
          <path className="ingbird-frame" d="M58 50h4" />
        </g>
      )
    case 'tulip':
      return (
        <g className="ingbird-glasses ingbird-glasses-tulip" aria-hidden="true">
          <path className="ingbird-lens-tulip" d="M49 40q8 2 8 10t-8 9q-8-2-8-9t8-10z" />
          <path className="ingbird-lens-tulip" d="M71 40q8 2 8 10t-8 9q-8-2-8-9t8-10z" />
          <path className="ingbird-frame" d="M59 50h2" />
        </g>
      )
    case 'halo':
      return (
        <g className="ingbird-glasses ingbird-glasses-halo" aria-hidden="true">
          <circle className="ingbird-lens-halo" cx="49" cy="50" r="10" />
          <circle className="ingbird-lens-halo" cx="71" cy="50" r="10" />
          <path className="ingbird-frame-gold" d="M59 50h2M39 48 33 45M81 48 87 45" />
        </g>
      )
    case 'swirl':
      return (
        <g className="ingbird-glasses ingbird-glasses-swirl" aria-hidden="true">
          <path className="ingbird-swirl-lens" d="M49 40a10 10 0 1 0 0 20 7 7 0 1 0 0-14 4 4 0 1 0 0 8" />
          <path className="ingbird-swirl-lens" d="M71 40a10 10 0 1 0 0 20 7 7 0 1 0 0-14 4 4 0 1 0 0 8" />
        </g>
      )
    case 'neon':
      return (
        <g className="ingbird-glasses ingbird-glasses-neon" aria-hidden="true">
          <rect className="ingbird-neon-frame" x="37" y="42" width="21" height="16" rx="3" />
          <rect className="ingbird-neon-frame" x="62" y="42" width="21" height="16" rx="3" />
          <path className="ingbird-neon-line" d="M58 47h4M37 44 31 42M83 44 89 42" />
        </g>
      )
    case 'mirror':
      return (
        <g className="ingbird-glasses ingbird-glasses-mirror" aria-hidden="true">
          <path className="ingbird-mirror-lens" d="M35 43q25-5 50 0 2 8-5 12-10 5-20 5t-20-5q-7-4-5-12z" />
          <path className="ingbird-shield-glint" d="M43 47q10-2 18 0" />
          <path className="ingbird-frame" d="M35 45 29 42M85 45 91 42" />
        </g>
      )
    default:
      return null
  }
}

/** 体の後ろに描く小物(マント・羽)。 */
export function BackAccessoryParts({ id }: { id: AccessoryId }) {
  switch (id) {
    case 'cape':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-cape" aria-hidden="true">
          <path className="ingbird-fabric-plum" d="M30 52q30-14 60 0l-8 48q-22 8-44 0z" />
          <path className="ingbird-fabric-gold" d="M42 56q18-6 36 0v5q-18-6-36 0z" />
        </g>
      )
    case 'wings':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-wings" aria-hidden="true">
          <path className="ingbird-fabric-cream" d="M48 64q-26-16-36 2 12 14 38 6z" />
          <path className="ingbird-fabric-cream" d="M72 64q26-16 36 2-12 14-38 6z" />
        </g>
      )
    case 'backpack':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-backpack" aria-hidden="true">
          <rect className="ingbird-fabric-red" x="28" y="62" width="18" height="27" rx="6" />
          <rect className="ingbird-fabric-red" x="74" y="62" width="18" height="27" rx="6" />
          <path className="ingbird-fabric-cream" d="M28 70h18M74 70h18" />
        </g>
      )
    case 'wings_angel':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-wings_angel" aria-hidden="true">
          <path className="ingbird-fabric-white" d="M48 62q-30-18-40 0 10 16 40 10z" />
          <path className="ingbird-fabric-white" d="M72 62q30-18 40 0-10 16-40 10z" />
          <path className="ingbird-wing-lines" d="M20 64q12 2 20 6M100 64q-12 2-20 6" />
        </g>
      )
    case 'dark_cape':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-dark_cape" aria-hidden="true">
          <path className="ingbird-dark-cloth" d="M30 52q30-14 60 0l-8 48q-22 8-44 0z" />
          <path className="ingbird-dark-trim" d="M42 56q18-6 36 0v5q-18-6-36 0z" />
        </g>
      )
    case 'demon_wings':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-demon_wings" aria-hidden="true">
          <path className="ingbird-dark-wing" d="M48 62q-26-18-36-2 4 8 14 10-8 4-2 10 12 2 24-8z" />
          <path className="ingbird-dark-wing" d="M72 62q26-18 36-2-4 8-14 10 8 4 2 10-12 2-24-8z" />
        </g>
      )
    case 'backpack_gold':
      return (
        <g className="ingbird-accessory ingbird-accessory-back ingbird-accessory-backpack_gold" aria-hidden="true">
          <rect className="ingbird-fabric-gold" x="28" y="62" width="18" height="27" rx="6" />
          <rect className="ingbird-fabric-gold" x="74" y="62" width="18" height="27" rx="6" />
          <path className="ingbird-fabric-cream" d="M28 70h18M74 70h18" />
        </g>
      )
    default:
      return null
  }
}

/** 体の前に描く小物。 */
export function FrontAccessoryParts({ id }: { id: AccessoryId }) {
  switch (id) {
    case 'scarf':
      return (
        <g className="ingbird-accessory ingbird-accessory-scarf ingbird-scarf-group" aria-hidden="true">
          <path className="ingbird-scarf" d="M39 77q21 9 42 0v10q-21 8-42 0z" />
          <path className="ingbird-scarf-tail" d="M77 86l3 14 7-2-3-13z" />
        </g>
      )
    case 'bowtie':
      return (
        <g className="ingbird-accessory ingbird-accessory-bowtie ingbird-bowtie-group" aria-hidden="true">
          <path className="ingbird-bowtie" d="M60 80 47 73v14z" />
          <path className="ingbird-bowtie" d="M60 80 73 73v14z" />
          <circle className="ingbird-bowtie-knot" cx="60" cy="80" r="3.4" />
        </g>
      )
    case 'necktie':
      return (
        <g className="ingbird-accessory ingbird-accessory-necktie" aria-hidden="true">
          <path className="ingbird-fabric-navy" d="M57 75h6v5h-6z" />
          <path className="ingbird-fabric-navy" d="M57 80h6l2 4-5 10-5-10z" />
        </g>
      )
    case 'bell':
      return (
        <g className="ingbird-accessory ingbird-accessory-bell" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M43 78q17 7 34 0v6q-17 6-34 0z" />
          <circle className="ingbird-fabric-gold" cx="60" cy="87" r="4.4" />
        </g>
      )
    case 'medal':
      return (
        <g className="ingbird-accessory ingbird-accessory-medal" aria-hidden="true">
          <path className="ingbird-ribbon" d="M54 76l6 7 6-7" />
          <circle className="ingbird-fabric-gold" cx="60" cy="89" r="6" />
          <circle className="ingbird-fabric-cream" cx="60" cy="89" r="2.6" />
        </g>
      )
    case 'pendant':
      return (
        <g className="ingbird-accessory ingbird-accessory-pendant" aria-hidden="true">
          <path className="ingbird-chain" d="M46 76q14 10 28 0" />
          <path className="ingbird-fabric-pink" d="M60 84l4 6-4 5-4-5z" />
        </g>
      )
    case 'bandana':
      return (
        <g className="ingbird-accessory ingbird-accessory-bandana" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M40 77h40L60 93z" />
          <circle className="ingbird-fabric-red" cx="38" cy="80" r="3" />
        </g>
      )
    case 'headphones':
      return (
        <g className="ingbird-accessory ingbird-accessory-headphones" aria-hidden="true">
          <path className="ingbird-headphone-band" d="M32 56q0-34 28-34t28 34" />
          <rect className="ingbird-fabric-navy" x="24" y="50" width="9" height="15" rx="4.5" />
          <rect className="ingbird-fabric-navy" x="87" y="50" width="9" height="15" rx="4.5" />
        </g>
      )
    case 'sash':
      return (
        <g className="ingbird-accessory ingbird-accessory-sash" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M40 67 84 87 81 94 37 74z" />
        </g>
      )
    case 'scarf_red':
      return (
        <g className="ingbird-accessory ingbird-accessory-scarf_red ingbird-scarf-group" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M39 77q21 9 42 0v10q-21 8-42 0z" />
          <path className="ingbird-fabric-red" d="M77 86l3 14 7-2-3-13z" />
        </g>
      )
    case 'bell_gold':
      return (
        <g className="ingbird-accessory ingbird-accessory-bell_gold" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M43 78q17 7 34 0v6q-17 6-34 0z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="87" r="4.4" />
        </g>
      )
    case 'medal_legend':
      return (
        <g className="ingbird-accessory ingbird-accessory-medal_legend" aria-hidden="true">
          <path className="ingbird-ribbon" d="M54 76l6 7 6-7" />
          <circle className="ingbird-fabric-gold-strong" cx="60" cy="89" r="6.5" />
          <path className="ingbird-star" d="m60 85 1.4 3.4 3.4 1.4-3.4 1.4L60 95l-1.4-3.8-3.4-1.4 3.4-1.4z" />
        </g>
      )
    case 'mustache':
      return (
        <g className="ingbird-accessory ingbird-accessory-mustache" aria-hidden="true">
          <ellipse className="ingbird-fabric-dark" cx="51" cy="77" rx="8" ry="3" transform="rotate(-12 51 77)" />
          <ellipse className="ingbird-fabric-dark" cx="69" cy="77" rx="8" ry="3" transform="rotate(12 69 77)" />
        </g>
      )
    case 'whistle':
      return (
        <g className="ingbird-accessory ingbird-accessory-whistle" aria-hidden="true">
          <path className="ingbird-whistle-cord" d="M44 76q16 8 32 0" />
          <rect className="ingbird-fabric-silver" x="56" y="80" width="12" height="7" rx="2" />
          <circle className="ingbird-fabric-dark" cx="64" cy="83" r="1.6" />
        </g>
      )
    case 'camera':
      return (
        <g className="ingbird-accessory ingbird-accessory-camera" aria-hidden="true">
          <path className="ingbird-camera-strap" d="M44 76q16 8 32 0" />
          <rect className="ingbird-fabric-dark" x="50" y="80" width="20" height="12" rx="3" />
          <circle className="ingbird-fabric-silver" cx="60" cy="86" r="3.6" />
        </g>
      )
    case 'badge':
      return (
        <g className="ingbird-accessory ingbird-accessory-badge" aria-hidden="true">
          <circle className="ingbird-fabric-teal" cx="60" cy="82" r="5" />
          <path className="ingbird-fabric-cream" d="m60 79 1 2.2 2.2 1-2.2 1-1 2.2-1-2.2-2.2-1 2.2-1z" />
        </g>
      )
    case 'flower_pin':
      return (
        <g className="ingbird-accessory ingbird-accessory-flower_pin" aria-hidden="true">
          <circle className="ingbird-fabric-pink" cx="60" cy="82" r="3.4" />
          <circle className="ingbird-fabric-cream" cx="56" cy="79" r="2.4" />
          <circle className="ingbird-fabric-cream" cx="64" cy="79" r="2.4" />
          <circle className="ingbird-fabric-cream" cx="56" cy="85" r="2.4" />
          <circle className="ingbird-fabric-cream" cx="64" cy="85" r="2.4" />
        </g>
      )
    case 'bell_blue':
      return (
        <g className="ingbird-accessory ingbird-accessory-bell_blue" aria-hidden="true">
          <path className="ingbird-fabric-navy" d="M43 78q17 7 34 0v6q-17 6-34 0z" />
          <circle className="ingbird-fabric-silver" cx="60" cy="87" r="4.4" />
        </g>
      )
    case 'scarf_green':
      return (
        <g className="ingbird-accessory ingbird-accessory-scarf_green ingbird-scarf-group" aria-hidden="true">
          <path className="ingbird-fabric-green" d="M39 77q21 9 42 0v10q-21 8-42 0z" />
          <path className="ingbird-fabric-green" d="M77 86l3 14 7-2-3-13z" />
        </g>
      )
    case 'bowtie_gold':
      return (
        <g className="ingbird-accessory ingbird-accessory-bowtie_gold ingbird-bowtie-group" aria-hidden="true">
          <path className="ingbird-fabric-gold-strong" d="M60 80 47 73v14z" />
          <path className="ingbird-fabric-gold-strong" d="M60 80 73 73v14z" />
          <circle className="ingbird-fabric-cream" cx="60" cy="80" r="3.4" />
        </g>
      )
    case 'bone_pendant':
      return (
        <g className="ingbird-accessory ingbird-accessory-bone_pendant" aria-hidden="true">
          <path className="ingbird-dark-chain" d="M46 76q14 10 28 0" />
          <path className="ingbird-dark-bone" d="M54 84h12v3H54zM56 87h8v6h-8z" />
        </g>
      )
    case 'cursed_bell':
      return (
        <g className="ingbird-accessory ingbird-accessory-cursed_bell" aria-hidden="true">
          <path className="ingbird-dark-cloth" d="M43 78q17 7 34 0v6q-17 6-34 0z" />
          <circle className="ingbird-dark-gem" cx="60" cy="87" r="4.4" />
        </g>
      )
    case 'chain_collar':
      return (
        <g className="ingbird-accessory ingbird-accessory-chain_collar" aria-hidden="true">
          <path className="ingbird-dark-chain" d="M42 79q18 8 36 0" />
          <circle className="ingbird-dark-chain" cx="46" cy="80" r="2" />
          <circle className="ingbird-dark-chain" cx="53" cy="82" r="2" />
          <circle className="ingbird-dark-chain" cx="60" cy="83" r="2" />
          <circle className="ingbird-dark-chain" cx="67" cy="82" r="2" />
          <circle className="ingbird-dark-chain" cx="74" cy="80" r="2" />
        </g>
      )
    case 'dark_orb':
      return (
        <g className="ingbird-accessory ingbird-accessory-dark_orb" aria-hidden="true">
          <circle className="ingbird-dark-orb" cx="60" cy="84" r="5" />
          <circle className="ingbird-dark-orb-glint" cx="58" cy="82" r="1.4" />
        </g>
      )
    case 'spiked_collar':
      return (
        <g className="ingbird-accessory ingbird-accessory-spiked_collar" aria-hidden="true">
          <path className="ingbird-dark-metal" d="M43 78q17 7 34 0v5q-17 6-34 0z" />
          <path className="ingbird-dark-spike" d="m46 78-2-6 5 5zM54 80l-1-7 4 6zM62 80l1-7 3 7zM70 80l3-6 2 6z" />
        </g>
      )
    case 'ribbon':
      return (
        <g className="ingbird-accessory ingbird-accessory-ribbon" aria-hidden="true">
          <path className="ingbird-fabric-red" d="M60 78 50 72v12z" />
          <path className="ingbird-fabric-red" d="M60 78 70 72v12z" />
          <circle className="ingbird-fabric-red" cx="60" cy="78" r="2.6" />
        </g>
      )
    case 'cravat':
      return (
        <g className="ingbird-accessory ingbird-accessory-cravat" aria-hidden="true">
          <path className="ingbird-fabric-cream" d="M56 76h8l3 5-7 12-7-12z" />
          <circle className="ingbird-fabric-gold" cx="60" cy="78" r="2" />
        </g>
      )
    case 'lanyard':
      return (
        <g className="ingbird-accessory ingbird-accessory-lanyard" aria-hidden="true">
          <path className="ingbird-lanyard" d="M46 75q14 8 28 0" />
          <rect className="ingbird-fabric-white" x="54" y="82" width="12" height="9" rx="1.5" />
          <path className="ingbird-shoe-line" d="M57 85h6M57 88h4" />
        </g>
      )
    case 'compass':
      return (
        <g className="ingbird-accessory ingbird-accessory-compass" aria-hidden="true">
          <path className="ingbird-chain" d="M46 76q14 10 28 0" />
          <circle className="ingbird-fabric-gold" cx="60" cy="86" r="5" />
          <path className="ingbird-shoe-line" d="M60 83v6M57 86h6" />
        </g>
      )
    case 'lei':
      return (
        <g className="ingbird-accessory ingbird-accessory-lei" aria-hidden="true">
          <path className="ingbird-fabric-green" d="M40 77q20 12 40 0" />
          <circle className="ingbird-fabric-pink" cx="46" cy="80" r="3.4" />
          <circle className="ingbird-fabric-cream" cx="53" cy="84" r="3.4" />
          <circle className="ingbird-fabric-pink" cx="60" cy="86" r="3.4" />
          <circle className="ingbird-fabric-cream" cx="67" cy="84" r="3.4" />
          <circle className="ingbird-fabric-pink" cx="74" cy="80" r="3.4" />
        </g>
      )
    case 'scarf_blue':
      return (
        <g className="ingbird-accessory ingbird-accessory-scarf_blue ingbird-scarf-group" aria-hidden="true">
          <path className="ingbird-fabric-navy" d="M39 77q21 9 42 0v10q-21 8-42 0z" />
          <path className="ingbird-fabric-navy" d="M77 86l3 14 7-2-3-13z" />
        </g>
      )
    case 'medal_silver':
      return (
        <g className="ingbird-accessory ingbird-accessory-medal_silver" aria-hidden="true">
          <path className="ingbird-ribbon" d="M54 76l6 7 6-7" />
          <circle className="ingbird-fabric-silver" cx="60" cy="89" r="6" />
          <circle className="ingbird-fabric-cream" cx="60" cy="89" r="2.6" />
        </g>
      )
    default:
      return null
  }
}

export function EffectParts({ id }: { id: EffectId }) {
  switch (id) {
    case 'none':
      return null
    case 'sparkle':
      return (
        <g className="ingbird-effect ingbird-fx-sparkle" aria-hidden="true">
          <path d="m14 18 2.2 5.4L21.6 26l-5.4 2.2L14 33.6l-2.2-5.4L6.4 26l5.4-2.6z" />
          <path d="m104 14 1.8 4.4 4.4 1.8-4.4 1.8-1.8 4.4-1.8-4.4-4.4-1.8 4.4-1.8z" />
          <path d="m100 84 1.6 4 4 1.6-4 1.6-1.6 4-1.6-4-4-1.6 4-1.6z" />
          <path d="m16 88 1.4 3.4 3.4 1.4-3.4 1.4L16 98l-1.4-3.4L11.2 93l3.4-1.4z" />
        </g>
      )
    case 'bubble':
      return (
        <g className="ingbird-effect ingbird-fx-bubble" aria-hidden="true">
          <circle cx="16" cy="78" r="3.2" />
          <circle cx="104" cy="66" r="2.4" />
          <circle cx="96" cy="26" r="3.8" />
          <circle cx="22" cy="34" r="2.8" />
        </g>
      )
    case 'sakura':
      return (
        <g className="ingbird-effect ingbird-fx-sakura" aria-hidden="true">
          <ellipse cx="18" cy="30" rx="3.4" ry="1.8" transform="rotate(-25 18 30)" />
          <ellipse cx="102" cy="24" rx="3" ry="1.6" transform="rotate(35 102 24)" />
          <ellipse cx="98" cy="84" rx="3.4" ry="1.8" transform="rotate(-15 98 84)" />
          <ellipse cx="22" cy="86" rx="3" ry="1.6" transform="rotate(20 22 86)" />
        </g>
      )
    case 'snow':
      return (
        <g className="ingbird-effect ingbird-fx-snow" aria-hidden="true">
          <path d="M16 22v7M12.5 25.5h7M13.5 23l5 5M18.5 23l-5 5" />
          <path d="M103 18v6M100 21h6M101 19l4 4M105 19l-4 4" />
          <path d="M100 78v7M96.5 81.5h7M97.5 79l5 5M102.5 79l-5 5" />
          <path d="M22 84v6M19 87h6M20 85l4 4M24 85l-4 4" />
        </g>
      )
    case 'leaves':
      return (
        <g className="ingbird-effect ingbird-fx-leaves" aria-hidden="true">
          <ellipse className="ingbird-leaf-green" cx="18" cy="30" rx="4.2" ry="1.9" transform="rotate(-30 18 30)" />
          <ellipse className="ingbird-leaf-orange" cx="102" cy="24" rx="3.8" ry="1.7" transform="rotate(35 102 24)" />
          <ellipse className="ingbird-leaf-orange" cx="98" cy="86" rx="4.2" ry="1.9" transform="rotate(-20 98 86)" />
          <ellipse className="ingbird-leaf-green" cx="20" cy="82" rx="3.8" ry="1.7" transform="rotate(25 20 82)" />
        </g>
      )
    case 'notes':
      return (
        <g className="ingbird-effect ingbird-fx-notes" aria-hidden="true">
          <path className="ingbird-note-stem" d="M18 36V24l8-2v10" />
          <ellipse className="ingbird-fabric-navy" cx="16" cy="37" rx="3.4" ry="2.6" />
          <ellipse className="ingbird-fabric-navy" cx="24" cy="35" rx="3.4" ry="2.6" />
          <path className="ingbird-note-stem" d="M100 84V72l8-2v10" />
          <ellipse className="ingbird-fabric-navy" cx="98" cy="85" rx="3.4" ry="2.6" />
          <ellipse className="ingbird-fabric-navy" cx="106" cy="83" rx="3.4" ry="2.6" />
        </g>
      )
    case 'hearts':
      return (
        <g className="ingbird-effect ingbird-fx-hearts" aria-hidden="true">
          <path className="ingbird-heart" d="M16 40c-2.4-3.6-8-2.8-8 1.6 0 3.2 3.6 5.8 8 8.8 4.4-3 8-5.6 8-8.8 0-4.4-5.6-5.2-8-1.6z" />
          <path className="ingbird-heart" d="M104 28c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
          <path className="ingbird-heart" d="M100 88c-2-3-6.6-2.4-6.6 1.4 0 2.6 3 4.8 6.6 7.2 3.6-2.4 6.6-4.6 6.6-7.2 0-3.8-4.6-4.4-6.6-1.4z" />
          <path className="ingbird-heart" d="M20 84c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
        </g>
      )
    case 'stars':
      return (
        <g className="ingbird-effect ingbird-fx-stars" aria-hidden="true">
          <path className="ingbird-star-dot" d="m18 24 1.4 3.6 3.6 1.4-3.6 1.4L18 34l-1.4-3.6L13 29l3.6-1.4z" />
          <path className="ingbird-star-dot" d="m104 20 1.2 3 3 1.2-3 1.2-1.2 3-1.2-3-3-1.2 3-1.2z" />
          <path className="ingbird-star-dot" d="m100 84 1.4 3.4 3.4 1.4-3.4 1.4-1.4 3.4-1.4-3.4-3.4-1.4 3.4-1.4z" />
          <path className="ingbird-star-dot" d="m20 78 1.2 3 3 1.2-3 1.2-1.2 3-1.2-3-3-1.2 3-1.2z" />
        </g>
      )
    case 'confetti':
      return (
        <g className="ingbird-effect ingbird-fx-confetti" aria-hidden="true">
          <rect className="ingbird-confetti-piece piece-1" x="14" y="26" width="7" height="3" rx="1" transform="rotate(-25 14 26)" />
          <rect className="ingbird-confetti-piece piece-2" x="104" y="22" width="7" height="3" rx="1" transform="rotate(30 104 22)" />
          <rect className="ingbird-confetti-piece piece-3" x="12" y="82" width="6" height="3" rx="1" transform="rotate(15 12 82)" />
          <rect className="ingbird-confetti-piece piece-4" x="102" y="86" width="7" height="3" rx="1" transform="rotate(-20 102 86)" />
          <rect className="ingbird-confetti-piece piece-5" x="24" y="40" width="5" height="2.6" rx="1" transform="rotate(40 24 40)" />
          <rect className="ingbird-confetti-piece piece-6" x="94" y="44" width="5" height="2.6" rx="1" transform="rotate(-35 94 44)" />
        </g>
      )
    case 'rain':
      return (
        <g className="ingbird-effect ingbird-fx-rain" aria-hidden="true">
          <path className="ingbird-rain" d="M16 22v7M26 30v7M100 24v7M92 34v7M18 80v7M100 82v7" />
        </g>
      )
    case 'fireflies':
      return (
        <g className="ingbird-effect ingbird-fx-fireflies" aria-hidden="true">
          <circle className="ingbird-firefly" cx="16" cy="34" r="2.2" />
          <circle className="ingbird-firefly" cx="26" cy="66" r="1.7" />
          <circle className="ingbird-firefly" cx="100" cy="26" r="2" />
          <circle className="ingbird-firefly" cx="104" cy="78" r="2.4" />
          <circle className="ingbird-firefly" cx="90" cy="96" r="1.7" />
        </g>
      )
    case 'lightning':
      return (
        <g className="ingbird-effect ingbird-fx-lightning" aria-hidden="true">
          <path className="ingbird-bolt" d="m18 24-6 12h5l-3 9 11-14h-5l4-7z" />
          <path className="ingbird-bolt" d="m102 30-5 10h4l-2 8 9-12h-4l3-6z" />
          <path className="ingbird-bolt" d="m100 84-4 9h3l-2 7 8-11h-4l3-5z" />
        </g>
      )
    case 'rainbow':
      return (
        <g className="ingbird-effect ingbird-fx-rainbow" aria-hidden="true">
          <path className="ingbird-rainbow-1" d="M2 34q14-20 28 0" />
          <path className="ingbird-rainbow-2" d="M2 38q14-20 28 0" />
          <path className="ingbird-rainbow-3" d="M2 42q14-20 28 0" />
          <path className="ingbird-rainbow-1" d="M90 34q14-20 28 0" />
          <path className="ingbird-rainbow-2" d="M90 38q14-20 28 0" />
          <path className="ingbird-rainbow-3" d="M90 42q14-20 28 0" />
        </g>
      )
    case 'bigbubbles':
      return (
        <g className="ingbird-effect ingbird-fx-bigbubbles" aria-hidden="true">
          <circle cx="16" cy="36" r="6" />
          <circle cx="102" cy="70" r="7" />
          <circle cx="96" cy="20" r="5" />
        </g>
      )
    case 'goldsparkle':
      return (
        <g className="ingbird-effect ingbird-fx-goldsparkle" aria-hidden="true">
          <path d="m16 22 2.6 6.4L25 31l-6.4 2.6L16 40l-2.6-6.4L7 31l6.4-2.6z" />
          <path d="m104 18 2.2 5.4 5.4 2.2-5.4 2.2-2.2 5.4-2.2-5.4-5.4-2.2 5.4-2.2z" />
          <path d="m100 82 2 5 5 2-5 2-2 5-2-5-5-2 5-2z" />
          <path d="m20 80 2 4.6 4.6 2-4.6 2-2 4.6-2-4.6L13 86.6l4.6-2z" />
        </g>
      )
    case 'meteor':
      return (
        <g className="ingbird-effect ingbird-fx-meteor" aria-hidden="true">
          <path className="ingbird-meteor-trail" d="M4 16 22 30" />
          <circle className="ingbird-meteor-head" cx="23" cy="31" r="2.6" />
          <path className="ingbird-meteor-trail" d="M96 8 108 18" />
          <circle className="ingbird-meteor-head" cx="109" cy="19" r="2.2" />
        </g>
      )
    case 'aurora':
      return (
        <g className="ingbird-effect ingbird-fx-aurora" aria-hidden="true">
          <path className="ingbird-aurora-1" d="M2 4q22 6 24 26" />
          <path className="ingbird-aurora-2" d="M8 2q20 8 22 28" />
          <path className="ingbird-aurora-3" d="M118 4q-22 6-24 26" />
          <path className="ingbird-aurora-1" d="M112 2q-20 8-22 28" />
        </g>
      )
    case 'galaxy':
      return (
        <g className="ingbird-effect ingbird-fx-galaxy" aria-hidden="true">
          <circle className="ingbird-galaxy-dot" cx="12" cy="18" r="1.4" />
          <circle className="ingbird-galaxy-dot" cx="22" cy="10" r="1" />
          <circle className="ingbird-galaxy-dot" cx="106" cy="16" r="1.5" />
          <circle className="ingbird-galaxy-dot" cx="96" cy="8" r="1" />
          <circle className="ingbird-galaxy-dot" cx="14" cy="70" r="1.2" />
          <circle className="ingbird-galaxy-dot" cx="8" cy="92" r="1.6" />
          <circle className="ingbird-galaxy-dot" cx="104" cy="88" r="1.2" />
          <circle className="ingbird-galaxy-dot" cx="94" cy="104" r="1.4" />
          <path className="ingbird-galaxy-star" d="m104 22 1.8 4.4 4.4 1.8-4.4 1.8-1.8 4.4-1.8-4.4-4.4-1.8 4.4-1.8z" />
          <path className="ingbird-galaxy-star" d="m18 88 1.6 4 4 1.6-4 1.6-1.6 4-1.6-4-4-1.6 4-1.6z" />
        </g>
      )
    case 'butterfly':
      return (
        <g className="ingbird-effect ingbird-fx-butterfly" aria-hidden="true">
          <ellipse className="ingbird-butterfly-wing" cx="16" cy="36" rx="5" ry="3.4" transform="rotate(-30 16 36)" />
          <ellipse className="ingbird-butterfly-wing" cx="22" cy="34" rx="5" ry="3.4" transform="rotate(30 22 34)" />
          <ellipse className="ingbird-butterfly-wing" cx="100" cy="80" rx="4.4" ry="3" transform="rotate(-30 100 80)" />
          <ellipse className="ingbird-butterfly-wing" cx="106" cy="78" rx="4.4" ry="3" transform="rotate(30 106 78)" />
        </g>
      )
    case 'balloons':
      return (
        <g className="ingbird-effect ingbird-fx-balloons" aria-hidden="true">
          <ellipse className="ingbird-balloon-1" cx="16" cy="30" rx="6" ry="7.5" />
          <path className="ingbird-balloon-string" d="M16 38v12" />
          <ellipse className="ingbird-balloon-2" cx="102" cy="64" rx="5.5" ry="7" />
          <path className="ingbird-balloon-string" d="M102 71v12" />
          <ellipse className="ingbird-balloon-3" cx="94" cy="18" rx="4.6" ry="6" />
          <path className="ingbird-balloon-string" d="M94 24v10" />
        </g>
      )
    case 'bubblestars':
      return (
        <g className="ingbird-effect ingbird-fx-bubblestars" aria-hidden="true">
          <circle className="ingbird-bubblestar" cx="18" cy="32" r="4.5" />
          <circle className="ingbird-bubblestar" cx="102" cy="28" r="5" />
          <circle className="ingbird-bubblestar" cx="96" cy="80" r="4" />
          <circle className="ingbird-bubblestar" cx="22" cy="82" r="5.5" />
        </g>
      )
    case 'fireworks':
      return (
        <g className="ingbird-effect ingbird-fx-fireworks" aria-hidden="true">
          <path className="ingbird-firework-1" d="M18 26v-8M18 26v8M10 26h8M26 26h-8M13 21l5 5M23 21l-5 5" />
          <path className="ingbird-firework-2" d="M102 84v-8M102 84v8M94 84h8M110 84h-8M97 79l5 5M107 79l-5 5" />
        </g>
      )
    case 'heart_rain':
      return (
        <g className="ingbird-effect ingbird-fx-heart_rain" aria-hidden="true">
          <path className="ingbird-heart" d="M16 30c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
          <path className="ingbird-heart" d="M104 34c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
          <path className="ingbird-heart" d="M100 78c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
          <path className="ingbird-heart" d="M20 82c-1.8-2.8-6-2.2-6 1.2 0 2.4 2.8 4.4 6 6.8 3.2-2.4 6-4.4 6-6.8 0-3.4-4.2-4-6-1.2z" />
        </g>
      )
    case 'gold_leaves':
      return (
        <g className="ingbird-effect ingbird-fx-gold_leaves" aria-hidden="true">
          <ellipse className="ingbird-leaf-gold" cx="18" cy="30" rx="4.2" ry="1.9" transform="rotate(-30 18 30)" />
          <ellipse className="ingbird-leaf-gold" cx="102" cy="24" rx="3.8" ry="1.7" transform="rotate(35 102 24)" />
          <ellipse className="ingbird-leaf-gold" cx="98" cy="86" rx="4.2" ry="1.9" transform="rotate(-20 98 86)" />
          <ellipse className="ingbird-leaf-gold" cx="20" cy="82" rx="3.8" ry="1.7" transform="rotate(25 20 82)" />
        </g>
      )
    case 'stardust':
      return (
        <g className="ingbird-effect ingbird-fx-stardust" aria-hidden="true">
          <circle className="ingbird-stardust-dot" cx="14" cy="20" r="1.4" />
          <circle className="ingbird-stardust-dot" cx="26" cy="14" r="1" />
          <circle className="ingbird-stardust-dot" cx="104" cy="22" r="1.5" />
          <circle className="ingbird-stardust-dot" cx="94" cy="14" r="1" />
          <circle className="ingbird-stardust-dot" cx="12" cy="64" r="1.2" />
          <circle className="ingbird-stardust-dot" cx="106" cy="70" r="1.4" />
          <circle className="ingbird-stardust-dot" cx="98" cy="94" r="1.2" />
          <circle className="ingbird-stardust-dot" cx="18" cy="92" r="1.5" />
        </g>
      )
    case 'comet':
      return (
        <g className="ingbird-effect ingbird-fx-comet" aria-hidden="true">
          <path className="ingbird-comet-tail" d="M4 10 26 34" />
          <circle className="ingbird-comet-head" cx="27" cy="35" r="3.4" />
          <path className="ingbird-comet-tail" d="M100 6 112 20" />
          <circle className="ingbird-comet-head" cx="113" cy="21" r="2.6" />
        </g>
      )
    case 'sunlight':
      return (
        <g className="ingbird-effect ingbird-fx-sunlight" aria-hidden="true">
          <circle className="ingbird-sun" cx="18" cy="18" r="5" />
          <path className="ingbird-sun-ray" d="M18 10V6M18 26v4M10 18H6M26 18h4" />
          <circle className="ingbird-sun" cx="102" cy="86" r="3.4" />
          <path className="ingbird-sun-ray" d="M102 80v-3M102 92v3M96 86h-3M108 86h3" />
        </g>
      )
    case 'thunderstorm':
      return (
        <g className="ingbird-effect ingbird-fx-thunderstorm" aria-hidden="true">
          <path className="ingbird-rain" d="M14 20v7M24 28v7M100 22v7M92 32v7M16 78v7M100 80v7" />
          <path className="ingbird-thunder-bolt" d="m100 44-5 10h4l-2 8 9-12h-4l3-6z" />
        </g>
      )
    case 'aurora_borealis':
      return (
        <g className="ingbird-effect ingbird-fx-aurora_borealis" aria-hidden="true">
          <path className="ingbird-aurora-1" d="M2 6q20 8 22 30" />
          <path className="ingbird-aurora-2" d="M10 2q18 10 20 32" />
          <path className="ingbird-aurora-3" d="M118 6q-20 8-22 30" />
          <path className="ingbird-aurora-1" d="M110 2q-18 10-20 32" />
          <path className="ingbird-aurora-2" d="M2 110q20-8 22-30" />
          <path className="ingbird-aurora-3" d="M118 110q-20-8-22-30" />
        </g>
      )
    case 'stardust_legend':
      return (
        <g className="ingbird-effect ingbird-fx-stardust_legend" aria-hidden="true">
          <circle className="ingbird-stardust-legend" cx="12" cy="16" r="1.8" />
          <circle className="ingbird-stardust-legend" cx="24" cy="10" r="1.2" />
          <circle className="ingbird-stardust-legend" cx="106" cy="14" r="1.8" />
          <circle className="ingbird-stardust-legend" cx="96" cy="8" r="1.2" />
          <circle className="ingbird-stardust-legend" cx="10" cy="68" r="1.4" />
          <circle className="ingbird-stardust-legend" cx="106" cy="76" r="1.8" />
          <circle className="ingbird-stardust-legend" cx="94" cy="102" r="1.4" />
          <circle className="ingbird-stardust-legend" cx="18" cy="96" r="1.8" />
          <path className="ingbird-star-dot" d="m104 26 2 5 5 2-5 2-2 5-2-5-5-2 5-2z" />
          <path className="ingbird-star-dot" d="m18 84 1.8 4.4 4.4 1.8-4.4 1.8-1.8 4.4-1.8-4.4-4.4-1.8 4.4-1.8z" />
        </g>
      )
    case 'dark_mist':
      return (
        <g className="ingbird-effect ingbird-fx-dark_mist" aria-hidden="true">
          <path className="ingbird-dark-mist" d="M6 84q10-8 20 0t20 0M74 92q10-8 20 0t20 0M10 34q8-6 16 0t16 0" />
        </g>
      )
    case 'bats':
      return (
        <g className="ingbird-effect ingbird-fx-bats" aria-hidden="true">
          <path className="ingbird-dark-bat" d="M14 24q4-6 8 0 4-6 8 0-4 1-8 5-4-4-8-5z" />
          <path className="ingbird-dark-bat" d="M96 20q3-5 6 0 3-5 6 0-3 1-6 4-3-3-6-4z" />
          <path className="ingbird-dark-bat" d="M98 80q4-6 8 0 4-6 8 0-4 1-8 5-4-4-8-5z" />
        </g>
      )
    case 'purple_flame':
      return (
        <g className="ingbird-effect ingbird-fx-purple_flame" aria-hidden="true">
          <path className="ingbird-dark-flame" d="M18 96q-6-8 0-16 6 8 0 16z" />
          <path className="ingbird-dark-flame" d="M100 90q-6-8 0-16 6 8 0 16z" />
          <path className="ingbird-dark-flame" d="M24 40q-4-6 0-12 4 6 0 12z" />
        </g>
      )
    case 'cursed_glow':
      return (
        <g className="ingbird-effect ingbird-fx-cursed_glow" aria-hidden="true">
          <circle className="ingbird-dark-glow" cx="16" cy="30" r="4" />
          <circle className="ingbird-dark-glow" cx="102" cy="24" r="3" />
          <circle className="ingbird-dark-glow" cx="98" cy="82" r="4.5" />
          <circle className="ingbird-dark-glow" cx="20" cy="84" r="3" />
        </g>
      )
    case 'blood_moon':
      return (
        <g className="ingbird-effect ingbird-fx-blood_moon" aria-hidden="true">
          <circle className="ingbird-blood-moon-ring" cx="100" cy="26" r="16" />
          <circle className="ingbird-blood-moon" cx="100" cy="26" r="12" />
          <circle className="ingbird-dark-glow" cx="16" cy="84" r="3.4" />
        </g>
      )
    case 'ghosts':
      return (
        <g className="ingbird-effect ingbird-fx-ghosts" aria-hidden="true">
          <path className="ingbird-ghost" d="M16 40q0-10 8-10t8 10v8l-4-3-4 3-4-3-4 3z" />
          <path className="ingbird-ghost" d="M92 88q0-8 7-8t7 8v7l-3.5-3-3.5 3-3.5-3-3.5 3z" />
        </g>
      )
    case 'abyss':
      return (
        <g className="ingbird-effect ingbird-fx-abyss" aria-hidden="true">
          <path className="ingbird-abyss-swirl" d="M8 20q16 4 14 20M112 100q-16-4-14-20" />
          <circle className="ingbird-abyss-dot" cx="20" cy="90" r="1.6" />
          <circle className="ingbird-abyss-dot" cx="100" cy="18" r="1.8" />
          <circle className="ingbird-abyss-dot" cx="92" cy="96" r="1.4" />
        </g>
      )
    case 'void_rift':
      return (
        <g className="ingbird-effect ingbird-fx-void_rift" aria-hidden="true">
          <path className="ingbird-void-rift" d="M14 8q4 14-2 24t2 22M106 90q-4-14 2-24t-2-22" />
          <path className="ingbird-void-glow" d="M14 8q4 14-2 24t2 22M106 90q-4-14 2-24t-2-22" />
        </g>
      )
    case 'drizzle':
      return (
        <g className="ingbird-effect ingbird-fx-drizzle" aria-hidden="true">
          <path className="ingbird-rain-light" d="M14 22v6M24 30v6M98 24v6M90 34v6M18 78v6M100 82v6" />
        </g>
      )
    case 'sunshower':
      return (
        <g className="ingbird-effect ingbird-fx-sunshower" aria-hidden="true">
          <circle className="ingbird-sun" cx="18" cy="22" r="4.5" />
          <path className="ingbird-sun-ray" d="M18 14v-3M18 33v3M10 22H7M29 22h3" />
          <path className="ingbird-rain-light" d="M96 26v6M88 38v6M100 78v6M22 80v6" />
        </g>
      )
    case 'raindrops':
      return (
        <g className="ingbird-effect ingbird-fx-raindrops" aria-hidden="true">
          <path className="ingbird-drop" d="M16 26q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop" d="M102 22q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop" d="M100 82q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop" d="M20 78q4 5 0 8-4-3 0-8z" />
        </g>
      )
    case 'rainbow_rain':
      return (
        <g className="ingbird-effect ingbird-fx-rainbow_rain" aria-hidden="true">
          <path className="ingbird-drop ingbird-drop-red" d="M16 26q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop ingbird-drop-yellow" d="M102 22q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop ingbird-drop-blue" d="M100 82q4 5 0 8-4-3 0-8z" />
          <path className="ingbird-drop ingbird-drop-green" d="M20 78q4 5 0 8-4-3 0-8z" />
        </g>
      )
    case 'sleet':
      return (
        <g className="ingbird-effect ingbird-fx-sleet" aria-hidden="true">
          <path className="ingbird-rain-light" d="M14 22v6M24 30v6M98 24v6M90 34v6" />
          <path className="ingbird-snow-light" d="M18 78v6M15 81h6M100 80v6M97 83h6M92 60v5M89.5 62.5h5" />
        </g>
      )
    case 'storm':
      return (
        <g className="ingbird-effect ingbird-fx-storm" aria-hidden="true">
          <path className="ingbird-rain-light" d="M12 18v8M22 28v8M32 20v8M96 22v8M88 32v8M100 72v8M92 84v8" />
          <path className="ingbird-thunder-bolt" d="m100 44-5 10h4l-2 8 9-12h-4l3-6z" />
          <path className="ingbird-storm-wind" d="M6 60q10-4 18 0M100 62q-8-4-14 0" />
        </g>
      )
    case 'bubble_rain':
      return (
        <g className="ingbird-effect ingbird-fx-bubble_rain" aria-hidden="true">
          <path className="ingbird-rain-light" d="M14 22v6M24 30v6M98 24v6M90 34v6" />
          <circle className="ingbird-bubblestar" cx="18" cy="80" r="4.5" />
          <circle className="ingbird-bubblestar" cx="100" cy="78" r="5" />
        </g>
      )
    case 'star_rain':
      return (
        <g className="ingbird-effect ingbird-fx-star_rain" aria-hidden="true">
          <path className="ingbird-star-rain" d="m16 24 1.4 3.6 3.6 1.4-3.6 1.4L16 34l-1.4-3.6L11 29l3.6-1.4z" />
          <path className="ingbird-star-rain" d="m102 20 1.2 3 3 1.2-3 1.2-1.2 3-1.2-3-3-1.2 3-1.2z" />
          <path className="ingbird-star-rain" d="m98 82 1.4 3.4 3.4 1.4-3.4 1.4-1.4 3.4-1.4-3.4-3.4-1.4 3.4-1.4z" />
          <path className="ingbird-star-rain" d="m20 78 1.2 3 3 1.2-3 1.2-1.2 3-1.2-3-3-1.2 3-1.2z" />
        </g>
      )
    case 'gold_rain':
      return (
        <g className="ingbird-effect ingbird-fx-gold_rain" aria-hidden="true">
          <path className="ingbird-gold-drop" d="M16 26v7M26 34v7M98 24v7M90 36v7M20 78v7M100 82v7" />
        </g>
      )
    case 'reverse_rain':
      return (
        <g className="ingbird-effect ingbird-fx-reverse_rain" aria-hidden="true">
          <path className="ingbird-rain-reverse" d="M14 30v-7M24 38v-7M98 32v-7M90 42v-7M18 88v-7M100 90v-7M92 76v-7" />
        </g>
      )
    default:
      return null
  }
}

export function ShoeParts({ id }: { id: ShoeId }) {
  switch (id) {
    case 'none':
      return null
    case 'sneakers':
      return (
        <g className="ingbird-shoes ingbird-shoes-sneakers" aria-hidden="true">
          <path className="ingbird-shoe-white" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-white" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M44 106h13M63 106h13M46 103h8M66 103h8" />
        </g>
      )
    case 'boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-boots" aria-hidden="true">
          <rect className="ingbird-shoe-brown" x="47" y="91" width="8" height="10" rx="2" />
          <rect className="ingbird-shoe-brown" x="65" y="91" width="8" height="10" rx="2" />
          <path className="ingbird-shoe-brown" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-brown" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M47 95h8M65 95h8" />
        </g>
      )
    case 'sandals':
      return (
        <g className="ingbird-shoes ingbird-shoes-sandals" aria-hidden="true">
          <path className="ingbird-shoe-sole" d="M42 105h17v3H42zM61 105h17v3H61z" />
          <path className="ingbird-shoe-strap" d="M46 105v-4M55 105v-4M65 105v-4M74 105v-4" />
        </g>
      )
    case 'rain_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-rain_boots" aria-hidden="true">
          <rect className="ingbird-shoe-yellow" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-shoe-yellow" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-shoe-yellow" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-yellow" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M47 97h8M65 97h8" />
        </g>
      )
    case 'slippers':
      return (
        <g className="ingbird-shoes ingbird-shoes-slippers" aria-hidden="true">
          <path className="ingbird-shoe-pink" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-pink" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <circle className="ingbird-shoe-cream" cx="47" cy="101" r="2.2" />
          <circle className="ingbird-shoe-cream" cx="73" cy="101" r="2.2" />
        </g>
      )
    case 'dress_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-dress_shoes" aria-hidden="true">
          <path className="ingbird-shoe-black" d="M58 104q0-3-4-3H47q-5 2-5 5 0 2 3 2h10q3-1 3-4z" />
          <path className="ingbird-shoe-black" d="M62 104q0-3 4-3h7q5 2 5 5 0 2-3 2H65q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M44 107h14M62 107h14" />
        </g>
      )
    case 'roller_skates':
      return (
        <g className="ingbird-shoes ingbird-shoes-roller_skates" aria-hidden="true">
          <path className="ingbird-shoe-white" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-white" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <circle className="ingbird-shoe-wheel" cx="47" cy="109" r="2.4" />
          <circle className="ingbird-shoe-wheel" cx="55" cy="109" r="2.4" />
          <circle className="ingbird-shoe-wheel" cx="65" cy="109" r="2.4" />
          <circle className="ingbird-shoe-wheel" cx="73" cy="109" r="2.4" />
        </g>
      )
    case 'ice_skates':
      return (
        <g className="ingbird-shoes ingbird-shoes-ice_skates" aria-hidden="true">
          <path className="ingbird-shoe-white" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-white" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-blade" d="M43 109h14M63 109h14" />
        </g>
      )
    case 'sports':
      return (
        <g className="ingbird-shoes ingbird-shoes-sports" aria-hidden="true">
          <path className="ingbird-shoe-teal" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-teal" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M46 102l6 4M66 102l-6 4" />
        </g>
      )
    case 'geta':
      return (
        <g className="ingbird-shoes ingbird-shoes-geta" aria-hidden="true">
          <path className="ingbird-shoe-wood" d="M41 102h17v4H41zM62 102h17v4H62z" />
          <path className="ingbird-shoe-wood" d="M45 106h3v4h-3zM52 106h3v4h-3zM66 106h3v4h-3zM73 106h3v4h-3z" />
          <path className="ingbird-shoe-strap" d="M46 102v-4M55 102v-4M66 102v-4M75 102v-4" />
        </g>
      )
    case 'star_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-star_boots" aria-hidden="true">
          <rect className="ingbird-shoe-gold" x="47" y="91" width="8" height="10" rx="2" />
          <rect className="ingbird-shoe-gold" x="65" y="91" width="8" height="10" rx="2" />
          <path className="ingbird-shoe-gold" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-gold" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-star" d="m50 96 1.2 2.8 2.8 1.2-2.8 1.2L50 104l-1.2-2.8L46 100l2.8-1.2z" />
          <path className="ingbird-shoe-star" d="m70 96 1.2 2.8 2.8 1.2-2.8 1.2L70 104l-1.2-2.8L66 100l2.8-1.2z" />
        </g>
      )
    case 'rocket_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-rocket_boots" aria-hidden="true">
          <rect className="ingbird-shoe-silver" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-shoe-silver" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-shoe-silver" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-silver" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-flame" d="M50 108q-3 4 0 7 3-3 0-7z" />
          <path className="ingbird-shoe-flame" d="M70 108q-3 4 0 7 3-3 0-7z" />
        </g>
      )
    case 'glass_slippers':
      return (
        <g className="ingbird-shoes ingbird-shoes-glass_slippers" aria-hidden="true">
          <path className="ingbird-shoe-glass" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-glass" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-sparkle" d="m45 98 1 2.2 2.2 1-2.2 1-1 2.2-1-2.2-2.2-1 2.2-1z" />
          <path className="ingbird-shoe-sparkle" d="m75 98 1 2.2 2.2 1-2.2 1-1 2.2-1-2.2-2.2-1 2.2-1z" />
        </g>
      )
    case 'cloud_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-cloud_shoes" aria-hidden="true">
          <circle className="ingbird-shoe-cloud" cx="46" cy="103" r="4" />
          <circle className="ingbird-shoe-cloud" cx="52" cy="101" r="5" />
          <circle className="ingbird-shoe-cloud" cx="57" cy="104" r="3.6" />
          <circle className="ingbird-shoe-cloud" cx="64" cy="104" r="3.6" />
          <circle className="ingbird-shoe-cloud" cx="70" cy="101" r="5" />
          <circle className="ingbird-shoe-cloud" cx="76" cy="103" r="4" />
        </g>
      )
    case 'cursed_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-cursed_boots" aria-hidden="true">
          <rect className="ingbird-dark-cloth" x="47" y="91" width="8" height="10" rx="2" />
          <rect className="ingbird-dark-cloth" x="65" y="91" width="8" height="10" rx="2" />
          <path className="ingbird-dark-cloth" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-dark-cloth" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-dark-slit" d="M47 96h8M65 96h8" />
        </g>
      )
    case 'shadow_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-shadow_shoes" aria-hidden="true">
          <path className="ingbird-dark-shadow" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-dark-shadow" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-dark-mist" d="M44 108q6-3 12 0M64 108q6-3 12 0" />
        </g>
      )
    case 'dragon_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-dragon_boots" aria-hidden="true">
          <rect className="ingbird-dark-scale" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-dark-scale" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-dark-scale" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-dark-scale" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-dark-spike" d="m48 90 2-5 2 5zM66 90l2-5 2 5z" />
        </g>
      )
    case 'underworld_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-underworld_boots" aria-hidden="true">
          <rect className="ingbird-dark-metal" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-dark-metal" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-dark-metal" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-dark-metal" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-dark-flame" d="M50 108q-3 4 0 7 3-3 0-7z" />
          <path className="ingbird-dark-flame" d="M70 108q-3 4 0 7 3-3 0-7z" />
        </g>
      )
    case 'loafers':
      return (
        <g className="ingbird-shoes ingbird-shoes-loafers" aria-hidden="true">
          <path className="ingbird-shoe-brown" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-brown" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-line" d="M48 102h6M66 102h6" />
        </g>
      )
    case 'boat_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-boat_shoes" aria-hidden="true">
          <path className="ingbird-shoe-cream" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-shoe-cream" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-strap" d="M47 103l3 4M53 103l-3 4M67 103l3 4M73 103l-3 4" />
        </g>
      )
    case 'jelly_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-jelly_shoes" aria-hidden="true">
          <path className="ingbird-jelly" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-jelly" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
        </g>
      )
    case 'rain_shoes':
      return (
        <g className="ingbird-shoes ingbird-shoes-rain_shoes" aria-hidden="true">
          <path className="ingbird-fabric-navy" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-fabric-navy" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-rain-light" d="M46 108v3M54 108v3M66 108v3M74 108v3" />
        </g>
      )
    case 'moon_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-moon_boots" aria-hidden="true">
          <rect className="ingbird-fabric-silver" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-fabric-silver" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-fabric-silver" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-fabric-silver" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-star" d="m50 94 1 2.4 2.4 1-2.4 1-1 2.4-1-2.4-2.4-1 2.4-1z" />
        </g>
      )
    case 'sun_sneakers':
      return (
        <g className="ingbird-shoes ingbird-shoes-sun_sneakers" aria-hidden="true">
          <path className="ingbird-fabric-gold" d="M57 104q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-fabric-gold" d="M63 104q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <circle className="ingbird-fabric-cream" cx="49" cy="100" r="2" />
          <circle className="ingbird-fabric-cream" cx="71" cy="100" r="2" />
        </g>
      )
    case 'fire_boots':
      return (
        <g className="ingbird-shoes ingbird-shoes-fire_boots" aria-hidden="true">
          <rect className="ingbird-fabric-red" x="47" y="90" width="8" height="11" rx="2" />
          <rect className="ingbird-fabric-red" x="65" y="90" width="8" height="11" rx="2" />
          <path className="ingbird-fabric-red" d="M57 103q0-3-3-3H46q-4 1-4 4t4 3h10q3-1 3-4z" />
          <path className="ingbird-fabric-red" d="M63 103q0-3 3-3h8q4 1 4 4t-4 3H66q-3-1-3-4z" />
          <path className="ingbird-shoe-flame" d="M50 108q-3 4 0 7 3-3 0-7z" />
          <path className="ingbird-shoe-flame" d="M70 108q-3 4 0 7 3-3 0-7z" />
        </g>
      )
    default:
      return null
  }
}
