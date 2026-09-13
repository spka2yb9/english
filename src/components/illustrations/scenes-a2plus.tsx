import type { IllustrationSceneMap } from './types'
import {
  Arrow,
  Backdrop,
  Book,
  Character,
  Check,
  Clock,
  Cloud,
  Cross,
  House,
  Label,
  Panel,
  PlainText,
  Road,
  Sparkles,
  Tree,
} from './primitives'

export const A2_PLUS_SCENES = {
  'u07-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={0} />
      <path d="M37 241h566" className="ill-muted-stroke ill-floor" />
      <Character x={142} y={242} scale={0.72} shirt="coral" hair="bob" />
      <Character x={496} y={242} scale={0.94} facing={-1} shirt="teal" hair="short" />
      <path d="M199 116h247M199 116v126M446 116v126" className="ill-blue ill-stroke ill-wide ill-dashed" />
      <path d="M213 105h219" className="ill-coral ill-stroke ill-check" markerEnd="url(#ill-arrow)" markerStart="url(#ill-arrow)" />
      <Label x={142} y={267} width={112} text={l[0]} tone="coral" height={34} />
      <Label x={496} y={267} width={112} text={l[2]} tone="teal" height={34} />
      <Label x={322} y={72} width={190} text={l[1]} tone="blue" />
      <path d="M552 79v128M541 93h22M541 124h22M541 155h22M541 186h22" className="ill-muted-stroke ill-fine" />
    </>
  ),

  'u07-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={4} />
      <g transform="translate(70 91)">
        <path d="M0 155h500" className="ill-muted-stroke ill-floor" />
        <rect x="180" y="26" width="140" height="129" rx="7" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <rect x="28" y="75" width="140" height="80" rx="7" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <rect x="332" y="101" width="140" height="54" rx="7" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <PlainText x={250} y={111} text="1" width={50} size={43} tone="gold" />
        <PlainText x={98} y={130} text="2" width={50} size={34} tone="blue" />
        <PlainText x={402} y={140} text="3" width={50} size={28} tone="coral" />
        <Label x={250} y={4} width={118} text={l[0]} tone="gold" />
        <Label x={98} y={53} width={118} text={l[1]} tone="blue" />
        <Label x={402} y={79} width={118} text={l[2]} tone="coral" />
      </g>
      <path d="M320 29l9 18 20 3-15 14 4 20-18-10-18 10 4-20-15-14 20-3z" className="ill-gold ill-solid" />
      <path d="M240 45l-19-17M401 45l19-17M250 69l-24 5M390 69l24 5" className="ill-coral ill-stroke ill-fine" />
    </>
  ),

  'u07-l3': (l) => (
    <>
      <Backdrop tone="teal" variant={2} />
      <g transform="translate(320 72)">
        <path d="M0 0v145M-37 145h74" className="ill-ink-stroke ill-symbol" />
        <path d="M-215 49h430M-215 49l-47 91h94zM215 49l-47 91h94z" className="ill-teal ill-stroke ill-wide" />
        <circle r="15" className="ill-gold ill-solid" />
      </g>
      <Character x={106} y={213} scale={0.56} shirt="blue" hair="short" />
      <Character x={534} y={213} scale={0.56} facing={-1} shirt="coral" hair="bob" />
      <Label x={105} y={247} width={115} text={l[0]} tone="blue" />
      <Label x={535} y={247} width={115} text={l[2]} tone="coral" />
      <Label x={320} y={252} width={220} text={l[1]} tone="teal" />
      <path d="M275 160h90M275 178h90" className="ill-teal ill-stroke ill-symbol" />
      <Check x={320} y={117} scale={0.65} />
    </>
  ),

  'u07-l4': (l) => (
    <>
      <Backdrop tone="coral" variant={5} />
      <g transform="translate(50 65)">
        <path d="M0 145h540" className="ill-muted-stroke ill-floor" />
        <path d="M35 23h104l-14 114H49z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M49 99h76l-5 38H54z" className="ill-blue ill-solid ill-water" />
        <path d="M218 23h104l-14 114h-76z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M225 63h90l-9 74h-72z" className="ill-green ill-solid ill-water" />
        <path d="M401 23h104l-14 114h-76z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M403 35h100l-13 102h-74z" className="ill-coral ill-solid ill-water" />
        <path d="M18 84h504" className="ill-gold ill-stroke ill-wide ill-dashed" />
        <PlainText x={-3} y={89} text="ENOUGH" width={80} size={12} tone="gold" anchor="start" />
        <Label x={87} y={171} width={154} text={l[0]} tone="blue" />
        <Label x={270} y={171} width={135} text={l[1]} tone="green" />
        <Label x={453} y={171} width={154} text={l[2]} tone="coral" />
      </g>
      <Cross x={503} y={52} scale={0.58} />
      <Check x={320} y={51} scale={0.58} />
    </>
  ),

  'u08-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={1} />
      <g transform="translate(41 59)">
        <Panel x={0} y={0} width={170} height={177} tone="teal">
          <Clock x={85} y={72} r={44} time="eight" tone="teal" />
          <Label x={85} y={148} width={145} text={l[0]} tone="paper" />
        </Panel>
        <Panel x={194} y={0} width={170} height={177} tone="gold">
          <rect x="229" y="31" width="100" height="76" rx="10" className="ill-paper ill-panel" />
          <path d="M229 55h100M253 25v23M305 25v23" className="ill-gold ill-stroke ill-wide" />
          <circle cx="278" cy="81" r="13" className="ill-coral ill-solid" />
          <Label x={279} y={148} width={145} text={l[1]} tone="paper" />
        </Panel>
        <Panel x={388} y={0} width={170} height={177} tone="blue">
          <path d="M419 33h108v75H419z" className="ill-paper ill-panel" />
          <path d="M437 48h72M437 64h72M437 80h48" className="ill-muted-stroke ill-fine" />
          <path d="M414 108h118" className="ill-blue ill-stroke ill-wide" />
          <Label x={473} y={148} width={145} text={l[2]} tone="paper" />
        </Panel>
      </g>
      <PlainText x={126} y={43} text="POINT" width={80} size={12} tone="teal" />
      <PlainText x={320} y={43} text="SURFACE" width={80} size={12} tone="gold" />
      <PlainText x={514} y={43} text="CONTAINER" width={100} size={12} tone="blue" />
    </>
  ),

  'u08-l2': (l) => (
    <>
      <Backdrop tone="green" variant={3} />
      <g transform="translate(39 64)">
        <path d="M0 161h562" className="ill-muted-stroke ill-floor" />
        <path d="M14 9h118v152H14z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <circle cx="112" cy="85" r="5" className="ill-ink-fill" />
        <circle cx="73" cy="161" r="10" className="ill-coral ill-solid" />
        <Label x={73} y={188} width={171} text={l[0]} tone="coral" />
        <path d="M183 91h171v18H183zM205 109v52M332 109v52" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <rect x="244" y="51" width="51" height="40" rx="6" className="ill-blue ill-pale ill-panel" />
        <Label x={269} y={188} width={172} text={l[1]} tone="gold" />
        <path d="M411 62h121v99H411z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M411 62l60 37 61-37M471 99v62" className="ill-green ill-stroke ill-fine" />
        <circle cx="471" cy="126" r="17" className="ill-violet ill-pale ill-panel" />
        <Label x={471} y={188} width={166} text={l[2]} tone="green" />
      </g>
      <path d="M112 48v-19M103 36l9-8 9 8M308 45v-20M299 33l9-8 9 8M510 46v-20M501 34l9-8 9 8" className="ill-teal ill-stroke ill-fine" />
    </>
  ),

  'u08-l3': (l) => (
    <>
      <Backdrop tone="green" variant={0} />
      <House x={91} y={225} scale={0.66} tone="coral" />
      <Tree x={262} y={239} scale={0.62} />
      <Tree x={340} y={239} scale={0.5} tone="teal" />
      <g transform="translate(520 205)">
        <rect x="-60" y="-85" width="120" height="85" rx="5" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M-49-63h98M-35-43h25v25h-25zM10-43h25v25H10z" className="ill-blue ill-stroke ill-fine" />
        <path d="M-70-85h140M-43-97h86" className="ill-coral ill-stroke ill-wide" />
      </g>
      <Road d="M151 219C207 157 384 166 457 214" tone="green" />
      <Character x={309} y={225} scale={0.58} shirt="gold" hair="cap" pose="walk" />
      <Arrow d="M153 186c73-77 230-72 300-6" tone="coral" width={5} />
      <Label x={92} y={265} width={115} text={l[0]} tone="coral" />
      <Label x={307} y={85} width={216} text={l[1]} tone="green" />
      <Label x={520} y={265} width={115} text={l[2]} tone="blue" />
    </>
  ),

  'u08-l4': (l) => (
    <>
      <Backdrop tone="violet" variant={4} />
      <g transform="translate(83 88)">
        <path d="M0 46q0-46 46-46t46 46" className="ill-violet ill-stroke ill-symbol" />
        <rect x="-10" y="39" width="27" height="63" rx="12" className="ill-violet ill-pale ill-panel" />
        <rect x="75" y="39" width="27" height="63" rx="12" className="ill-violet ill-pale ill-panel" />
        <path d="M17 85q29 27 58 0" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={136} y={230} width={176} text={l[0]} tone="violet" />
      <g transform="translate(313 148)">
        <ellipse cx="-24" cy="0" rx="39" ry="27" className="ill-coral ill-pale ill-panel" transform="rotate(-26)" />
        <ellipse cx="24" cy="0" rx="39" ry="27" className="ill-blue ill-pale ill-panel" transform="rotate(-26)" />
        <path d="M-20 15l40-30" className="ill-ink-stroke ill-wide" />
      </g>
      <Arrow d="M207 151h54" tone="coral" />
      <Arrow d="M364 151h48" tone="blue" />
      <g transform="translate(488 76)">
        <circle cx="0" cy="77" r="77" className="ill-teal ill-wash" />
        <path d="M-39 24v92M-39 35q28-20 52 0v81M13 50q29-20 52 0v66" className="ill-teal ill-stroke ill-wide" />
        <path d="M-39 51h52M13 66h52" className="ill-coral ill-stroke ill-fine" />
        <circle cx="-13" cy="83" r="7" className="ill-gold ill-solid" />
        <circle cx="39" cy="95" r="7" className="ill-gold ill-solid" />
      </g>
      <Label x={502} y={230} width={185} text={l[1]} tone="teal" />
    </>
  ),

  'u09-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={2} />
      <g transform="translate(38 59)">
        <rect width="265" height="181" rx="23" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M20 114q112-28 225 0v47H20z" className="ill-blue ill-solid ill-water" />
        <Character x={126} y={128} scale={0.55} shirt="coral" hair="short" pose="celebrate" />
        <path d="M49 138q20-18 40 0M166 145q20-18 40 0" className="ill-paper-stroke ill-wide" />
        <Check x={223} y={37} scale={0.6} />
        <Label x={132} y={205} width={224} text={l[0]} tone="blue" />
      </g>
      <g transform="translate(337 59)">
        <rect width="265" height="181" rx="23" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M29 133h207l-14-46-35-24H84L52 88z" className="ill-paper ill-panel" />
        <circle cx="77" cy="134" r="21" className="ill-ink-fill" /><circle cx="77" cy="134" r="9" className="ill-paper" />
        <circle cx="193" cy="134" r="21" className="ill-ink-fill" /><circle cx="193" cy="134" r="9" className="ill-paper" />
        <Cross x={225} y={37} scale={0.6} />
        <Label x={132} y={205} width={224} text={l[1]} tone="coral" />
      </g>
    </>
  ),

  'u09-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={3} />
      <g transform="translate(55 70)">
        <path d="M0 148h219V0H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M69 148V35h81v113" className="ill-paper ill-panel" />
        <path d="M84 81l18 19 36-42" className="ill-green ill-stroke ill-check" />
        <path d="M185 51q30 17 0 34M185 85l12-4-2 13" className="ill-green ill-stroke ill-fine" />
        <Label x={109} y={176} width={210} text={l[0]} tone="green" />
      </g>
      <g transform="translate(366 70)">
        <path d="M0 148h219V0H0z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M69 148V35h81v113" className="ill-paper ill-panel" />
        <circle cx="110" cy="84" r="33" className="ill-coral ill-stroke ill-symbol" />
        <path d="M86 108l48-48" className="ill-coral ill-stroke ill-symbol" />
        <Label x={109} y={176} width={210} text={l[1]} tone="coral" />
      </g>
      <PlainText x={320} y={45} text="FREE  ≠  FORBIDDEN" width={270} size={15} tone="muted" />
    </>
  ),

  'u09-l3': (l) => (
    <>
      <Backdrop tone="gold" variant={1} />
      <path d="M45 240C158 239 201 184 286 169s178-67 309-113" className="ill-green ill-stroke ill-road" />
      <Character x={95} y={243} scale={0.6} shirt="blue" hair="cap" pose="walk" />
      <g transform="translate(188 183)">
        <path d="M0 44V-32M0-32l70 19-70 19" className="ill-blue ill-stroke ill-wide" />
        <Label x={35} y={-51} width={105} text={l[0]} tone="blue" height={32} />
      </g>
      <g transform="translate(349 125)">
        <path d="M0 62V-17M0-17l88 20-88 20" className="ill-gold ill-stroke ill-wide" />
        <Label x={44} y={-38} width={146} text={l[1]} tone="gold" height={32} />
      </g>
      <g transform="translate(532 57)">
        <path d="M0 73V0M0 0l78 19-78 20" className="ill-coral ill-stroke ill-wide" />
        <Label x={36} y={-21} width={105} text={l[2]} tone="coral" height={32} />
      </g>
      <path d="M538 124l22-40 22 40z" className="ill-coral ill-pale ill-panel" />
      <PlainText x={560} y={112} text="!" width={20} size={24} tone="coral" />
    </>
  ),

  'u09-l4': (l) => (
    <>
      <Backdrop tone="blue" variant={5} />
      <g transform="translate(66 68)">
        <Cloud x={62} y={56} scale={0.62} />
        <circle cx="62" cy="56" r="54" className="ill-muted-stroke ill-dashed" />
        <path d="M28 117h68l-13 74H41z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M42 166h42l-4 25H46z" className="ill-violet ill-solid ill-water" />
        <Label x={62} y={215} width={130} text={l[0]} tone="violet" />
      </g>
      <g transform="translate(258 68)">
        <Cloud x={62} y={56} scale={0.66} raining />
        <circle cx="62" cy="56" r="54" className="ill-gold ill-stroke ill-dashed" />
        <path d="M28 117h68l-13 74H41z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M37 143h50l-8 48H47z" className="ill-gold ill-solid ill-water" />
        <Label x={62} y={215} width={130} text={l[1]} tone="gold" />
      </g>
      <g transform="translate(450 68)">
        <Cloud x={62} y={56} scale={0.7} raining />
        <circle cx="62" cy="56" r="54" className="ill-coral ill-stroke" />
        <path d="M28 117h68l-13 74H41z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M31 121h62l-10 70H41z" className="ill-coral ill-solid ill-water" />
        <Label x={62} y={215} width={130} text={l[2]} tone="coral" />
      </g>
      <PlainText x={320} y={35} text="certainty" width={120} size={13} tone="muted" />
      <Arrow d="M192 42h256" tone="coral" />
    </>
  ),

  'u10-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={0} />
      <g transform="translate(51 75)">
        <rect width="170" height="145" rx="18" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M31 42h108M31 68h72M31 94h91" className="ill-muted-stroke ill-fine" />
        <circle cx="137" cy="104" r="18" className="ill-coral ill-pale ill-panel" />
        <path d="M129 104l6 7 12-15" className="ill-green ill-stroke ill-fine" />
        <Label x={85} y={164} width={174} text={l[0]} tone="paper" />
      </g>
      <Arrow d="M242 151c70-68 134-78 208-40" tone="coral" dashed width={5} />
      <g transform="translate(479 112) rotate(-8)">
        <path d="M-75 26L72-22M-7-29l17-44 25-8-5 47M-21 36l-42 42-27 5 35-59" className="ill-blue ill-stroke ill-symbol" />
        <path d="M-7 15l-58-8-18 14 55 17" className="ill-blue ill-pale ill-panel" />
      </g>
      <path d="M530 196q36 18 68-2" className="ill-blue ill-stroke ill-fine" />
      <Label x={487} y={241} width={215} text={l[1]} tone="blue" />
      <PlainText x={323} y={74} text="to" width={45} size={27} tone="coral" />
    </>
  ),

  'u10-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={3} />
      <g transform="translate(305 162)">
        <path d="M-168 42q27-80 88-56l79 29 83-29q60-22 86 56v41h-336z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M-155 43h310M-88-8v91M89-8v91" className="ill-muted-stroke ill-fine" />
        <Character x={0} y={46} scale={0.69} shirt="teal" hair="bob" pose="sit" />
        <Book x={55} y={-41} scale={0.57} color="gold" open />
      </g>
      <g transform="translate(511 167)">
        <path d="M-24-34h48v56q0 23-24 23t-24-23z" className="ill-gold ill-pale ill-panel" />
        <path d="M24-22q31 0 25 29-4 20-26 17" className="ill-ink-stroke ill-fine" />
        <path d="M-8-50c-8-14 10-17 3-31M12-50c-8-14 10-17 3-31" className="ill-coral ill-stroke ill-fine" />
      </g>
      <Arrow d="M112 90c-28 112 48 171 124 118" tone="coral" />
      <Label x={116} y={67} width={134} text={l[0]} tone="coral" />
      <Label x={421} y={57} width={165} text={l[1]} tone="teal" />
      <path d="M434 76q35 24 1 49-31 22-68 3" className="ill-teal ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      <PlainText x={319} y={272} text="an activity you enjoy" width={250} size={14} tone="muted" />
    </>
  ),

  'u10-l3': (l) => (
    <>
      <Backdrop tone="violet" variant={2} />
      <Character x={88} y={247} scale={0.78} shirt="gold" hair="short" pose="walk" />
      <circle cx="172" cy="204" r="11" className="ill-gold ill-solid" />
      <Road d="M177 201C268 190 304 114 419 77" tone="coral" dashed={false} />
      <Road d="M177 207C280 230 383 245 564 176c52-19 24-93-26-89-48 4-70 72-23 103" tone="teal" dashed={false} />
      <Arrow d="M198 188c69-22 112-75 192-100" tone="coral" />
      <path d="M505 187c47 14 83-11 80-51-4-42-59-47-80-13-19 32 7 68 43 67" className="ill-teal ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      <g transform="translate(446 39)"><path d="M0 48V0M0 0l82 19-82 20" className="ill-coral ill-stroke ill-wide" /></g>
      <Label x={417} y={94} width={202} text={l[0]} tone="coral" />
      <Label x={454} y={248} width={210} text={l[1]} tone="teal" />
      <PlainText x={291} y={49} text="future target" width={100} size={12} tone="coral" />
      <PlainText x={303} y={271} text="activity loop" width={100} size={12} tone="teal" />
    </>
  ),

  'u10-l4': (l) => (
    <>
      <Backdrop tone="green" variant={4} />
      <g transform="translate(64 47)">
        <rect width="185" height="193" rx="22" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={94} y={184} scale={0.68} shirt="coral" hair="bun" pose="carry" />
        <path d="M45 117h98l-11 46H56z" className="ill-gold ill-pale ill-panel" />
        <path d="M69 116c-9-14 11-20 3-35M99 116c-9-14 11-20 3-35" className="ill-blue ill-stroke ill-fine" />
      </g>
      <g transform="translate(316 144)">
        <ellipse cx="-31" cy="0" rx="50" ry="31" className="ill-gold ill-pale ill-panel" transform="rotate(-20)" />
        <ellipse cx="31" cy="0" rx="50" ry="31" className="ill-blue ill-pale ill-panel" transform="rotate(-20)" />
        <path d="M-25 18l50-36" className="ill-ink-stroke ill-wide" />
        <PlainText x={0} y={6} text="at" width={45} size={19} tone="violet" />
      </g>
      <Arrow d="M253 143h25" tone="coral" />
      <Arrow d="M356 143h27" tone="blue" />
      <g transform="translate(422 53)">
        <rect width="150" height="188" rx="18" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M39 20h72l-11 127H50z" className="ill-coral ill-pale ill-panel" />
        <path d="M64 57h22M75 46v22" className="ill-paper-stroke ill-wide" />
        <path d="M31 155h88" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={157} y={263} width={172} text={l[0]} tone="green" />
      <Label x={496} y={263} width={174} text={l[1]} tone="coral" />
      <Sparkles x={581} y={72} tone="gold" />
    </>
  ),
} satisfies IllustrationSceneMap
