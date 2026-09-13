import type { IllustrationSceneMap } from './types'
import {
  Arrow,
  Backdrop,
  Book,
  Calendar,
  Character,
  Check,
  Clock,
  Cloud,
  Cross,
  Divider,
  House,
  Label,
  NumberBadge,
  Panel,
  PlainText,
  Road,
  Sparkles,
  SpeechBubble,
  Sun,
  Tree,
} from './primitives'

/** A2: every lesson has its own storyboard; only the visual vocabulary is shared. */
export const A2_SCENES = {
  'u01-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={0} />
      <path d="M39 214h562" className="ill-muted-stroke ill-floor" />
      <g transform="translate(34 58)">
        <rect width="168" height="116" rx="17" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M84 18v44M62 40h44" className="ill-coral ill-stroke ill-check" />
        <path d="M24 92h120" className="ill-muted-stroke ill-fine" />
      </g>
      <Character x={150} y={253} scale={0.82} shirt="blue" hair="bob" pose="wave" />
      <Label x={143} y={52} width={96} text={l[0]} tone="paper" />
      <g transform="translate(282 135)">
        <path d="M-42-17h84M-42 17h84" className="ill-teal ill-stroke ill-symbol" />
        <Label x={0} y={-54} width={72} text={l[1]} tone="teal" />
      </g>
      <path d="M337 213q51-82 102 0" className="ill-blue ill-stroke ill-wide" />
      <Character x={471} y={251} scale={0.83} shirt="coral" hair="bun" pose="stand" />
      <g transform="translate(472 139)" filter="url(#ill-shadow)">
        <rect x="-61" y="-21" width="122" height="42" rx="8" className="ill-paper ill-panel" />
        <path d="M-45-8h22M-45 3h34" className="ill-muted-stroke ill-fine" />
        <circle cx="39" cy="0" r="12" className="ill-coral ill-pale" />
      </g>
      <Label x={520} y={56} width={156} text={l[2]} tone="coral" />
    </>
  ),

  'u01-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={4} />
      <Sun x={88} y={76} r={26} />
      <g transform="translate(504 215)">
        <rect x="-62" y="-91" width="124" height="91" rx="6" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M-49-67h98M-40-48h22v22h-22zM-6-48h22v22H-6zM28-48h22v22H28z" className="ill-blue ill-stroke ill-fine" />
        <path d="M-73-91h146M-48-104h96" className="ill-ink-stroke ill-wide" />
      </g>
      <Road d="M73 234C173 183 338 261 455 211" tone="gold" />
      <Character x={271} y={236} scale={0.73} shirt="teal" hair="short" pose="walk" />
      <g transform="translate(219 181) rotate(-11)">
        <rect x="-19" y="-24" width="38" height="48" rx="4" className="ill-coral ill-pale ill-panel" />
        <path d="M-9-13h18M-9-3h18" className="ill-muted-stroke ill-fine" />
      </g>
      <Arrow d="M115 190c69-65 221-76 320-9" tone="teal" width={5} />
      <Label x={284} y={60} width={252} text={l[0]} tone="paper" />
      <Label x={103} y={257} width={150} text={l[1]} tone="gold" />
      <path d="M57 164c-26-49 28-80 62-45 27 28-4 64-33 53" className="ill-coral ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
    </>
  ),

  'u01-l3': (l) => (
    <>
      <Backdrop tone="blue" variant={1} />
      <Panel x={46} y={72} width={174} height={154} tone="blue">
        <path d="M79 72v-19h108v19" className="ill-ink-stroke ill-wide" />
        <path d="M46 123h174M133 73v153" className="ill-muted-stroke ill-fine" />
        <circle cx="133" cy="123" r="11" className="ill-gold ill-solid" />
      </Panel>
      <Label x={131} y={103} width={119} text={l[0]} tone="ink" />
      <path d="M253 178q31-35 61 0l-9 54h-43z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
      <path d="M271 173q12-24 24 0" className="ill-ink-stroke ill-wide" />
      <circle cx="284" cy="202" r="16" className="ill-gold ill-pale ill-panel" />
      <path d="M284 187v30M269 202h30" className="ill-muted-stroke ill-fine" />
      <Label x={284} y={130} width={116} text={l[1]} tone="teal" />
      <Arrow d="M231 150c44-29 79-29 112-2" tone="blue" />
      <g transform="translate(468 151) rotate(5)">
        <Label x={0} y={0} width={155} text={l[2]} tone="paper" />
        <Cross x={71} y={-29} scale={0.72} />
      </g>
      <Character x={542} y={258} scale={0.68} facing={-1} shirt="coral" hair="cap" pose="point" />
      <PlainText x={445} y={238} text="動詞は原形へ" width={160} size={14} tone="muted" />
    </>
  ),

  'u01-l4': (l) => (
    <>
      <Backdrop tone="coral" variant={2} />
      <path d="M32 236h576" className="ill-muted-stroke ill-floor" />
      <g transform="translate(82 185)">
        <circle cx="0" cy="46" r="17" className="ill-ink-fill" />
        <circle cx="0" cy="46" r="8" className="ill-paper" />
        <path d="M-47-23h75l27 30v39H-47z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M14-22v29h40" className="ill-muted-stroke ill-fine" />
        <path d="M-30-9h26M-30 4h30" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={83} y={123} width={82} text={l[0]} tone="coral" />
      <g transform="translate(288 190)">
        <rect x="-75" y="-38" width="150" height="84" rx="14" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Book x={0} y={2} scale={0.55} color="teal" open />
        <circle cx="-48" cy="50" r="15" className="ill-ink-fill" />
        <circle cx="48" cy="50" r="15" className="ill-ink-fill" />
      </g>
      <Label x={287} y={102} width={104} text={l[1]} tone="teal" />
      <g transform="translate(505 188)">
        <rect x="-78" y="-40" width="156" height="88" rx="14" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Book x={0} y={4} scale={0.62} color="blue" />
        <circle cx="-50" cy="52" r="15" className="ill-ink-fill" />
        <circle cx="50" cy="52" r="15" className="ill-ink-fill" />
      </g>
      <Label x={505} y={102} width={142} text={l[2]} tone="blue" />
      <Arrow d="M147 196h54" tone="coral" />
      <Arrow d="M368 196h54" tone="coral" />
      <PlainText x={320} y={52} text="S  →  V  →  O" width={250} size={22} tone="coral" />
    </>
  ),

  'u02-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={3} />
      <g transform="translate(403 205)">
        <path d="M-92 5h184v22H-92z" className="ill-gold ill-dark" />
        <path d="M-65 27v31M66 27v31" className="ill-ink-stroke ill-wide" />
        <path d="M-37-17h76l-8 22h-60z" className="ill-coral ill-pale ill-panel" />
        <path d="M-25-17q25-28 50 0" className="ill-muted-stroke ill-fine" />
        <path d="M-13-38c-14-19 15-26 2-45M16-38c-14-19 15-26 2-45" className="ill-blue ill-stroke ill-fine" />
      </g>
      <Character x={281} y={258} scale={0.8} shirt="gold" hair="bun" pose="carry" />
      <Clock x={96} y={102} r={49} time="ten" tone="teal" />
      <path d="M95 173v57" className="ill-muted-stroke ill-fine" />
      <Label x={160} y={53} width={246} text={l[0]} tone="coral" />
      <Label x={127} y={250} width={181} text={l[1]} tone="teal" />
      <g className="ill-coral ill-stroke ill-fine">
        <path d="M499 70q18-18 36 0M515 100q18-18 36 0" />
        <path d="M526 53v42M542 83h28" />
      </g>
      <Sparkles x={565} y={155} tone="gold" />
    </>
  ),

  'u02-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={5} />
      <Divider label="vs" />
      <g transform="translate(55 68)">
        <path d="M0 155C50 102 123 180 203 115" className="ill-muted-stroke ill-road ill-dashed" />
        <Sun x={32} y={27} r={20} />
        <path d="M176 86h55v69h-55zM169 86l34-31 35 31" className="ill-teal ill-pale ill-panel" />
        <Character x={112} y={164} scale={0.58} shirt="teal" hair="short" pose="walk" />
      </g>
      <Label x={163} y={251} width={252} text={l[0]} tone="paper" />
      <g transform="translate(345 58)">
        <path d="M15 170c55-61 140-63 245-11" className="ill-blue ill-stroke ill-road" />
        <Character x={126} y={181} scale={0.72} shirt="coral" hair="bob" pose="walk" />
        <path d="M191 109l25 22-25 22M217 109l25 22-25 22" className="ill-coral ill-stroke ill-wide" />
        <Clock x={229} y={42} r={28} time="three" tone="coral" />
      </g>
      <Label x={476} y={251} width={268} text={l[1]} tone="coral" />
    </>
  ),

  'u02-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={1} />
      <g transform="translate(70 38) rotate(-4 165 105)" filter="url(#ill-shadow)">
        <rect width="330" height="210" rx="10" className="ill-paper ill-panel" />
        <rect x="18" y="18" width="294" height="140" rx="5" className="ill-blue ill-pale" />
        <circle cx="260" cy="50" r="25" className="ill-sun" />
        <path d="M29 147L97 73l54 60 43-40 103 54" className="ill-green ill-pale ill-landscape" />
        <path d="M118 151v-60M92 105h52M100 105v-13h36v13M105 91V80h26v12" className="ill-coral ill-stroke ill-wide" />
        <Label x={165} y={181} width={250} text={l[0]} tone="paper" height={34} />
      </g>
      <g transform="translate(459 69) rotate(6 70 82)">
        <Calendar x={70} y={82} width={140} height={145} day="AUG" tone="coral" />
        <Label x={70} y={178} width={168} text={l[1]} tone="coral" />
      </g>
      <path d="M461 224q36 25 79 3" className="ill-coral ill-stroke ill-fine" />
      <circle cx="552" cy="232" r="19" className="ill-blue ill-pale ill-panel" />
      <circle cx="552" cy="232" r="8" className="ill-ink-stroke" />
    </>
  ),

  'u02-l4': (l) => (
    <>
      <Backdrop tone="violet" variant={2} />
      <g transform="translate(46 43)">
        <rect width="548" height="200" rx="22" className="ill-violet ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M274 0v200" className="ill-paper-stroke ill-wide" />
        <circle cx="57" cy="48" r="26" className="ill-gold ill-pale" />
        <path d="M57 17v62M26 48h62" className="ill-violet ill-stroke ill-fine" />
        <Character x={180} y={190} scale={0.73} shirt="coral" hair="bob" pose="carry" />
        <path d="M116 174h128v18H116zM134 140h81l-8 34h-66z" className="ill-gold ill-pale ill-panel" />
        <path d="M156 139c-14-18 15-25 2-42M186 139c-14-18 15-25 2-42" className="ill-blue ill-stroke ill-fine" />
        <Clock x={405} y={92} r={53} time="eight" tone="violet" />
        <path d="M334 162h143" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={183} y={65} width={231} text={l[0]} tone="paper" />
      <Label x={446} y={241} width={220} text={l[1]} tone="violet" />
    </>
  ),

  'u02-l5': (l) => (
    <>
      <Backdrop tone="blue" variant={4} />
      <Cloud x={102} y={63} scale={0.78} raining />
      <path d="M30 241h580" className="ill-blue ill-stroke ill-floor" />
      <Character x={201} y={250} scale={0.84} shirt="coral" hair="bob" mood="sad" />
      <Character x={422} y={250} scale={0.84} facing={-1} shirt="teal" hair="short" pose="point" />
      <path d="M287 161q49-79 99 0z" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
      <path d="M337 161v65q0 15-13 15-12 0-12-13" className="ill-ink-stroke ill-wide" />
      <SpeechBubble x={445} y={74} width={239} text={l[1]} tone="paper" tail="right" />
      <g transform="translate(248 76)">
        <circle r="42" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M-18 1l13 13 26-31" className="ill-green ill-stroke ill-check" />
      </g>
      <Label x={248} y={134} width={145} text={l[0]} tone="gold" />
      <Sparkles x={364} y={105} tone="coral" />
    </>
  ),

  'u02-l6': (l) => (
    <>
      <Backdrop tone="green" variant={0} />
      <House x={522} y={229} scale={0.82} tone="green" />
      <g transform="translate(256 215)">
        <rect x="-82" y="-57" width="74" height="57" className="ill-gold ill-pale ill-panel" />
        <rect x="4" y="-76" width="90" height="76" className="ill-coral ill-pale ill-panel" />
        <path d="M-45-57v57M49-76v76M4-38h90" className="ill-muted-stroke ill-fine" />
        <path d="M-70-40h35M18-57h44" className="ill-muted-stroke ill-fine" />
      </g>
      <Character x={119} y={251} scale={0.78} shirt="blue" hair="bun" pose="carry" />
      <Calendar x={326} y={82} width={108} height={89} day="SAT" tone="green" />
      <Check x={390} y={95} scale={0.7} />
      <Arrow d="M332 170c48-44 91-50 132-27" tone="green" dashed />
      <Label x={181} y={56} width={288} text={l[0]} tone="paper" />
      <Label x={451} y={266} width={205} text={l[1]} tone="green" />
    </>
  ),

  'u03-l1': (l) => (
    <>
      <Backdrop tone="green" variant={5} />
      <Tree x={93} y={225} scale={0.78} />
      <g transform="translate(185 170)">
        {[-42, 0, 42].map((x, i) => <g key={x}><circle cx={x} cy={0} r="22" className="ill-coral ill-pale ill-panel" /><path d={`M${x} -21q3-13 13-15`} className="ill-green ill-stroke ill-fine" /><NumberBadge x={x} y={50} number={String(i + 1)} tone="coral" /></g>)}
      </g>
      <Label x={185} y={253} width={213} text={l[0]} tone="coral" />
      <Divider x={325} />
      <g transform="translate(475 150)">
        <path d="M-65-54h130l-16 105h-98z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M-52 5q52-22 104 0l-7 46h-90z" className="ill-blue ill-solid ill-water" />
        <path d="M-34-80c-17-22 18-30 2-54M4-80c-17-22 18-30 2-54M40-80c-17-22 18-30 2-54" className="ill-blue ill-stroke ill-fine" />
      </g>
      <Label x={474} y={253} width={203} text={l[1]} tone="blue" />
    </>
  ),

  'u03-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={3} />
      <g transform="translate(46 76)">
        <rect width="250" height="144" rx="20" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        {[48, 103, 158, 213].map((x, i) => <circle key={x} cx={x} cy="69" r="22" className={`ill-${i === 1 ? 'coral' : 'gold'} ill-pale ill-panel`} />)}
        <path d="M103 25v17M96 35l7 8 7-8" className="ill-coral ill-stroke ill-wide" />
        <Label x={125} y={122} width={218} text={l[0]} tone="gold" height={34} />
      </g>
      <g transform="translate(349 46)">
        <path d="M0 0h231v190H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M15 15h201v105H15z" className="ill-paper ill-panel" />
        <circle cx="116" cy="66" r="31" className="ill-coral ill-pale ill-panel" />
        <path d="M116 29v-15M105 17l11-5 11 5" className="ill-green ill-stroke ill-fine" />
        <path d="M61 141h110M81 158h70" className="ill-muted-stroke ill-fine" />
        <Label x={116} y={210} width={204} text={l[1]} tone="coral" />
      </g>
      <Sparkles x={320} y={148} tone="gold" />
    </>
  ),

  'u03-l3': (l) => (
    <>
      <Backdrop tone="violet" variant={1} />
      <g transform="translate(47 46)">
        <rect width="391" height="199" rx="12" className="ill-gold ill-dark ill-panel" filter="url(#ill-shadow)" />
        <path d="M18 67h355M18 132h355" className="ill-paper-stroke ill-wide" />
        {[35, 76, 117, 158, 216, 257, 298, 339].map((x, i) => <rect key={x} x={x} y={i % 2 ? 24 : 18} width={25} height={i % 3 ? 43 : 49} rx="3" className={`ill-${i === 5 ? 'coral' : i % 2 ? 'blue' : 'teal'} ill-pale ill-panel`} />)}
        {[44, 92, 143, 205, 254, 307, 347].map((x, i) => <rect key={x} x={x} y={82 + (i % 2) * 7} width={28} height={43 - (i % 2) * 7} rx="3" className={`ill-${i % 2 ? 'gold' : 'violet'} ill-pale ill-panel`} />)}
        <circle cx="269" cy="43" r="37" className="ill-coral ill-stroke ill-spotlight" />
        <path d="M319-3L286 12" className="ill-coral ill-stroke ill-wide" />
      </g>
      <Character x={526} y={250} scale={0.78} facing={-1} shirt="violet" hair="curl" pose="point" />
      <Label x={140} y={266} width={155} text={l[0]} tone="paper" />
      <Label x={374} y={266} width={176} text={l[1]} tone="coral" />
    </>
  ),

  'u03-l4': (l) => (
    <>
      <Backdrop tone="blue" variant={0} />
      <g transform="translate(45 79)">
        <path d="M0 131h250M30 131L57 18h132l31 113" className="ill-gold ill-stroke ill-wide" />
        {[74, 105, 136, 167].map((x, i) => <Book key={x} x={x} y={83 - (i % 2) * 8} scale={0.42} color={i % 2 ? 'coral' : 'teal'} />)}
        <Label x={125} y={155} width={205} text={l[0]} tone="gold" />
      </g>
      <g transform="translate(359 64)">
        <path d="M75 11c45 0 83 37 83 83s-38 83-83 83S-8 140-8 94 30 11 75 11z" className="ill-blue ill-wash" />
        <path d="M25 36h99l-15 101H40z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M38 82q37-17 74 0l-8 55H46z" className="ill-blue ill-solid ill-water" />
        <path d="M129 61q37 5 27 46-8 27-38 19" className="ill-blue ill-stroke ill-wide" />
        <Label x={75} y={201} width={183} text={l[1]} tone="blue" />
      </g>
      <PlainText x={320} y={55} text="COUNT  /  MASS" width={230} size={14} tone="muted" />
    </>
  ),

  'u04-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={2} />
      <Character x={111} y={247} scale={0.86} shirt="coral" hair="bun" pose="point" />
      <Character x={521} y={247} scale={0.86} facing={-1} shirt="blue" hair="short" pose="wave" />
      <Label x={108} y={61} width={82} text={l[0]} tone="coral" />
      <Label x={525} y={61} width={89} text={l[2]} tone="blue" />
      <g transform="translate(317 145)">
        <path d="M-96-40h192v80H-96z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M-73-11h146M-58 11h116" className="ill-muted-stroke ill-fine" />
        <Label x={0} y={56} width={118} text={l[1]} tone="teal" />
      </g>
      <Arrow d="M165 157c41-41 76-48 104-30" tone="coral" />
      <Arrow d="M366 127c39-18 69-9 99 28" tone="blue" />
      <PlainText x={318} y={269} text="主語 → 動詞 → 目的語" width={280} size={15} tone="muted" />
    </>
  ),

  'u04-l2': (l) => (
    <>
      <Backdrop tone="green" variant={4} />
      <Character x={74} y={250} scale={0.85} shirt="gold" hair="short" pose="point" />
      <g transform="translate(184 179)">
        <circle cx="0" cy="-25" r="42" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M0-58v99M-33-30l33 20 32-22" className="ill-green ill-stroke ill-wide" />
        <rect x="-28" y="17" width="56" height="35" rx="6" className="ill-coral ill-pale ill-panel" />
      </g>
      <Tree x={482} y={231} scale={0.46} />
      <House x={552} y={235} scale={0.45} tone="blue" />
      <path d="M118 238h470" className="ill-muted-stroke ill-floor" />
      <path d="M235 231c95-28 168-29 262-2" className="ill-blue ill-stroke ill-road ill-dashed" />
      <Label x={189} y={72} width={190} text={l[0]} tone="green" />
      <Label x={493} y={82} width={184} text={l[1]} tone="blue" />
      <path d="M279 202l14 13-14 13M321 197l19 18-19 18M373 190l26 25-26 25" className="ill-muted-stroke ill-fine" />
    </>
  ),

  'u04-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={5} />
      <g transform="translate(49 52)">
        <rect width="347" height="169" rx="19" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 118h297" className="ill-gold ill-stroke ill-wide" />
        {[61, 128, 195, 262].map((x, i) => <g key={x} transform={`translate(${x} 84)`}><path d="M-24-25h48v50h-48z" className={`ill-${i === 2 ? 'coral' : i === 0 ? 'blue' : 'gold'} ill-pale ill-panel`} /><path d="M24-14h13v23H24" className="ill-ink-stroke ill-fine" /></g>)}
        <circle cx="195" cy="84" r="41" className="ill-coral ill-stroke ill-spotlight" />
        <Label x={174} y={145} width={203} text={l[0]} tone="coral" height={34} />
      </g>
      <Character x={515} y={253} scale={0.83} facing={-1} shirt="teal" hair="bob" pose="carry" />
      <g transform="translate(497 153)">
        <path d="M-28-22h56v44h-56z" className="ill-coral ill-pale ill-panel" />
        <path d="M28-13h16v26H28" className="ill-ink-stroke ill-fine" />
      </g>
      <Arrow d="M395 136c33-22 57-17 79 2" tone="teal" />
      <Label x={513} y={67} width={98} text={l[1]} tone="teal" />
      <Check x={572} y={109} scale={0.62} />
    </>
  ),

  'u05-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={1} />
      <g transform="translate(54 99)">
        <path d="M12 96h254l-18-54-45-25H76L43 48z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M84 24L63 55h161l-28-31z" className="ill-blue ill-pale ill-panel" />
        <circle cx="72" cy="96" r="25" className="ill-ink-fill" /><circle cx="72" cy="96" r="11" className="ill-paper" />
        <circle cx="218" cy="96" r="25" className="ill-ink-fill" /><circle cx="218" cy="96" r="11" className="ill-paper" />
        <Label x={143} y={132} width={126} text={l[0]} tone="paper" />
      </g>
      <g transform="translate(388 99)">
        <path d="M12 96h199l-15-54-38-25H65L37 48z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M72 24L54 55h124l-25-31z" className="ill-blue ill-pale ill-panel" />
        <circle cx="64" cy="96" r="25" className="ill-ink-fill" /><circle cx="64" cy="96" r="11" className="ill-paper" />
        <circle cx="169" cy="96" r="25" className="ill-ink-fill" /><circle cx="169" cy="96" r="11" className="ill-paper" />
        <Label x={112} y={132} width={186} text={l[1]} tone="coral" />
      </g>
      <Arrow d="M328 159h43" tone="coral" />
      <g transform="translate(351 79)"><path d="M-12 25v-34h24v34" className="ill-coral ill-stroke ill-wide" /><path d="M-22-9h44" className="ill-coral ill-stroke ill-wide" /></g>
    </>
  ),

  'u05-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={0} />
      <Road d="M26 236C146 95 262 279 417 152c61-50 126-49 197-13" tone="gold" />
      <g transform="translate(311 191) rotate(-8)">
        <path d="M-70 25h140L58-14 31-34h-70l-25 22z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <circle cx="-42" cy="28" r="17" className="ill-ink-fill" /><circle cx="-42" cy="28" r="7" className="ill-paper" />
        <circle cx="43" cy="28" r="17" className="ill-ink-fill" /><circle cx="43" cy="28" r="7" className="ill-paper" />
      </g>
      {[110, 466, 555].map((x, i) => <g key={x} transform={`translate(${x} ${205 - i * 20})`}><path d="M-16 25L0-26l16 51z" className="ill-coral ill-pale ill-panel" /><path d="M-10 7h20" className="ill-paper-stroke ill-wide" /></g>)}
      <Label x={153} y={65} width={150} text={l[0]} tone="paper" />
      <Arrow d="M221 79c70-39 159-38 230 8" tone="blue" dashed />
      <Label x={476} y={79} width={232} text={l[1]} tone="teal" />
      <Check x={574} y={113} scale={0.65} />
    </>
  ),

  'u05-l3': (l) => (
    <>
      <Backdrop tone="violet" variant={3} />
      <circle cx="320" cy="146" r="91" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <circle cx="320" cy="146" r="55" className="ill-violet ill-pale" />
      <path d="M320 146V91M320 146l42 25" className="ill-ink-stroke ill-clock-hand" />
      <g transform="translate(105 167)">
        <path d="M-34 45h68M-24 45v-63h48v63" className="ill-muted-stroke ill-wide" />
        <Cross x={0} y={-41} scale={0.55} />
      </g>
      <Label x={104} y={244} width={145} text={l[0]} tone="coral" />
      <g transform="translate(320 248)"><path d="M-26-10q26-36 52 0" className="ill-gold ill-stroke ill-wide" /><NumberBadge x={0} y={-27} number="3" tone="gold" /></g>
      <Label x={320} y={277} width={161} text={l[1]} tone="gold" height={33} />
      <g transform="translate(537 155)"><Sun x={0} y={0} r={31} /><Check x={0} y={1} scale={0.55} /></g>
      <Label x={536} y={244} width={145} text={l[2]} tone="green" />
      <Arrow d="M158 141c46-66 95-78 131-76" tone="violet" />
      <Arrow d="M351 66c59 2 103 32 131 75" tone="violet" />
    </>
  ),

  'u06-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={2} />
      <g transform="translate(54 55)">
        <path d="M0 0h302v187H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 27l73 33 68-31 107 38v91l-107-37-68 31-73-33z" className="ill-green ill-pale ill-panel" />
        <path d="M98 60v92M166 29v92M43 117c49-73 103 20 158-37 27-29 52-18 72-13" className="ill-blue ill-stroke ill-road ill-dashed" />
        <circle cx="222" cy="67" r="12" className="ill-coral ill-solid" />
        <path d="M222 78l-11 19h22z" className="ill-coral ill-solid" />
      </g>
      <Character x={483} y={255} scale={0.8} facing={-1} shirt="teal" hair="curl" pose="think" />
      <SpeechBubble x={482} y={78} width={230} text={l[0]} tone="paper" tail="right" />
      <g transform="translate(382 157)">
        <circle r="42" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <circle r="21" className="ill-paper ill-panel" />
        <path d="M31 31l29 29" className="ill-ink-stroke ill-check" />
      </g>
      <Label x={390} y={230} width={135} text={l[1]} tone="teal" />
    </>
  ),

  'u06-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={5} />
      <g transform="translate(85 82)">
        <path d="M0 92q65-92 130 0M130 92q65-92 130 0" className="ill-blue ill-stroke ill-symbol" />
        <path d="M0 92h260M0 79v26M260 79v26" className="ill-ink-stroke ill-wide" />
        {[26, 52, 78, 104, 130, 156, 182, 208, 234].map((x, i) => <path key={x} d={`M${x} 86v${i % 2 ? 6 : 12}`} className="ill-muted-stroke ill-fine" />)}
        <path d="M14 118h232" className="ill-gold ill-stroke ill-wide" markerEnd="url(#ill-arrow)" markerStart="url(#ill-arrow)" />
      </g>
      <Character x={510} y={254} scale={0.83} facing={-1} shirt="coral" hair="bob" pose="point" />
      <SpeechBubble x={495} y={74} width={206} text={l[0]} tone="paper" tail="right" />
      <Label x={310} y={245} width={191} text={l[1]} tone="gold" />
      <PlainText x={216} y={65} text="?" width={60} size={47} tone="coral" />
    </>
  ),

  'u06-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={4} />
      <g transform="translate(273 202)">
        <path d="M-37-93h74v65q0 28-37 28t-37-28z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M0-93l-10 23 16 15-17 19 11 36" className="ill-coral ill-stroke ill-wide" />
        <path d="M-38-51h-21q-22 0-19 25 3 20 40 17M38-51h21q22 0 19 25-3 20-40 17" className="ill-ink-stroke ill-wide" />
      </g>
      <g transform="translate(77 56)">
        <path d="M82 0c46 0 82 35 82 78s-36 78-82 78S0 121 0 78 36 0 82 0z" className="ill-ink-fill" opacity=".08" />
        <path d="M54 133q0-54 28-54t28 54M82 35a22 22 0 1 1 0 44 22 22 0 0 1 0-44z" className="ill-violet ill-pale ill-panel" />
        <PlainText x={82} y={105} text="?" width={40} size={37} tone="violet" />
      </g>
      <Label x={159} y={243} width={122} text={l[0]} tone="violet" />
      <Arrow d="M227 137c44-37 79-36 112 0" tone="coral" />
      <Label x={366} y={95} width={153} text={l[1]} tone="coral" />
      <g transform="translate(494 151) rotate(5)">
        <Label x={0} y={0} width={146} text={l[2]} tone="paper" />
        <Cross x={70} y={-30} scale={0.62} />
      </g>
      <PlainText x={499} y={222} text="do / did は不要" width={180} size={14} tone="muted" />
    </>
  ),
} satisfies IllustrationSceneMap
