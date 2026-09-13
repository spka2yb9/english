import type { IllustrationSceneMap } from './types'
import {
  Arrow,
  Backdrop,
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
  Sparkles,
  Sun,
  TinyStar,
  Tree,
} from './primitives'

export const B1_PLUS_SCENES = {
  'u17-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={0} />
      <g transform="translate(87 80)">
        <rect width="452" height="139" rx="18" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M29 27h394v85H29z" className="ill-teal ill-pale ill-panel" />
        <path d="M29 27h94v85H29zM123 27h119v85H123zM242 27h181v85H242z" className="ill-coral ill-solid" opacity=".18" />
        <path d="M123 27v85M242 27v85" className="ill-coral ill-stroke ill-fine ill-dashed" />
        <Character x={345} y={129} scale={0.5} shirt="gold" hair="bob" pose="point" />
        <path d="M316 68h69" className="ill-coral ill-stroke ill-wide" />
        <path d="M389 47l25-20M390 47l24 20" className="ill-coral ill-stroke ill-fine" />
      </g>
      <Clock x={90} y={66} r={30} time="three" tone="coral" />
      <Label x={164} y={248} width={214} text={l[0]} tone="coral" />
      <Label x={476} y={248} width={190} text={l[1]} tone="teal" />
      <Arrow d="M218 253h149" tone="teal" />
      <PlainText x={320} y={48} text="PAINTING · · · · · NOW" width={260} size={15} tone="coral" />
    </>
  ),

  'u17-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={2} />
      <Divider label="vs" />
      <g transform="translate(48 60)">
        <rect width="233" height="173" rx="20" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M35 32h163v112H35z" className="ill-teal ill-solid" opacity=".28" />
        <path d="M35 32h163v112" className="ill-green ill-stroke ill-wide" />
        <Sparkles x={178} y={53} tone="gold" />
        <Check x={116} y={89} scale={0.7} />
        <Label x={116} y={198} width={220} text={l[0]} tone="green" />
      </g>
      <g transform="translate(359 60)">
        <rect width="233" height="173" rx="20" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M35 32h163v112H35z" className="ill-paper ill-panel" />
        <path d="M35 32h88v112H35z" className="ill-teal ill-solid" opacity=".28" />
        <Character x={152} y={165} scale={0.49} facing={-1} shirt="gold" hair="bob" pose="point" />
        <path d="M113 104h42" className="ill-coral ill-stroke ill-wide" />
        <path d="M155 87l26-18" className="ill-coral ill-stroke ill-fine" />
        <Clock x={50} y={52} r={22} time="six" tone="coral" />
        <Label x={116} y={198} width={224} text={l[1]} tone="coral" />
      </g>
      <PlainText x={160} y={41} text="RESULT" width={80} size={13} tone="green" />
      <PlainText x={479} y={41} text="PROCESS" width={80} size={13} tone="coral" />
    </>
  ),

  'u18-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={1} />
      <path d="M53 208h534" className="ill-muted-stroke ill-floor" />
      <g transform="translate(87 145)">
        <path d="M0 37h181V-29H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M22-10h31v28H22zM66-10h31v28H66zM110-10h31v28h-31z" className="ill-paper ill-panel" />
        <path d="M181 37l38-20-38-46" className="ill-blue ill-pale ill-panel" />
        <circle cx="41" cy="41" r="17" className="ill-ink-fill" /><circle cx="141" cy="41" r="17" className="ill-ink-fill" />
      </g>
      <g transform="translate(465 84)">
        <path d="M0 124V0M-26 0h52M-38 124h76" className="ill-gold ill-stroke ill-symbol" />
        <Clock x={0} y={36} r={23} time="three" tone="gold" />
        <Character x={71} y={124} scale={0.51} facing={-1} shirt="coral" hair="bob" pose="walk" />
      </g>
      <Arrow d="M409 89H227" tone="violet" width={5} />
      <Label x={170} y={256} width={203} text={l[0]} tone="blue" />
      <Label x={486} y={256} width={197} text={l[1]} tone="coral" />
      <NumberBadge x={198} y={78} number="1" tone="blue" />
      <NumberBadge x={459} y={53} number="2" tone="coral" />
      <PlainText x={320} y={44} text="earlier in the past" width={170} size={13} tone="violet" />
    </>
  ),

  'u18-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={5} />
      <g transform="translate(47 63)">
        <Panel x={0} y={0} width={245} height={171} tone="blue">
          {[38, 105, 172].map((x, i) => <g key={x}><circle cx={x} cy="75" r="24" className={`ill-${i === 0 ? 'blue' : i === 1 ? 'gold' : 'coral'} ill-pale ill-panel`} /><NumberBadge x={x} y={35} number={String(i + 1)} tone={i === 0 ? 'blue' : i === 1 ? 'gold' : 'coral'} /></g>)}
          <Arrow d="M66 75h11M133 75h11" tone="blue" width={3} />
          <Label x={122} y={195} width={228} text={l[0]} tone="blue" />
        </Panel>
        <Panel x={304} y={0} width={245} height={171} tone="violet">
          <circle cx="343" cy="75" r="24" className="ill-coral ill-pale ill-panel" />
          <circle cx="430" cy="75" r="24" className="ill-blue ill-pale ill-panel" />
          <circle cx="506" cy="75" r="24" className="ill-gold ill-pale ill-panel" />
          <NumberBadge x={430} y={35} number="1" tone="blue" />
          <NumberBadge x={343} y={35} number="0" tone="violet" />
          <NumberBadge x={506} y={35} number="2" tone="gold" />
          <Arrow d="M401 75h-29" tone="violet" width={3} />
          <Arrow d="M459 75h19" tone="gold" width={3} />
          <Label x={426} y={195} width={232} text={l[1]} tone="violet" />
        </Panel>
      </g>
      <PlainText x={320} y={39} text="STORY ORDER  /  TIME ORDER" width={290} size={14} tone="gold" />
    </>
  ),

  'u18-l3': (l) => (
    <>
      <Backdrop tone="blue" variant={0} />
      <g transform="translate(47 62)">
        <path d="M0 0h546v177H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <g transform="translate(18 18)">
          <path d="M0 0h154v141H0z" className="ill-blue ill-pale ill-panel" />
          <Cloud x={78} y={47} scale={0.52} />
          <House x={78} y={139} scale={0.42} tone="blue" />
          <Label x={77} y={159} width={137} text={l[0]} tone="blue" height={32} />
        </g>
        <g transform="translate(196 18)">
          <path d="M0 0h154v141H0z" className="ill-coral ill-pale ill-panel" />
          <Character x={77} y={132} scale={0.55} shirt="coral" hair="bob" pose="walk" />
          <path d="M31 126h92" className="ill-muted-stroke ill-floor" />
          <TinyStar x={115} y={35} tone="coral" scale={1.4} />
          <Label x={77} y={159} width={137} text={l[1]} tone="coral" height={32} />
        </g>
        <g transform="translate(374 18)">
          <path d="M0 0h154v141H0z" className="ill-violet ill-pale ill-panel" />
          <g transform="translate(76 72) rotate(-5)"><rect x="-54" y="-42" width="108" height="84" rx="6" className="ill-paper ill-panel" /><path d="M-41 22l28-35 22 25 18-17 20 27" className="ill-blue ill-pale ill-landscape" /></g>
          <path d="M26 25h102" className="ill-violet ill-stroke ill-wide ill-dashed" />
          <Label x={77} y={159} width={137} text={l[2]} tone="violet" height={32} />
        </g>
      </g>
      <path d="M215 43l15-11 15 11M393 43l15-11 15 11" className="ill-gold ill-stroke ill-wide" />
      <PlainText x={320} y={278} text="background → event → flashback" width={310} size={14} tone="muted" />
    </>
  ),

  'u19-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={2} />
      <Character x={100} y={247} scale={0.77} shirt="coral" hair="bob" pose="point" />
      <g transform="translate(184 80)">
        <path d="M0 0h165v72H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 72l-19 21 41-21" className="ill-paper ill-bubble-tail" />
        <Label x={82} y={35} width={143} text={l[0]} tone="paper" height={38} />
      </g>
      <g transform="translate(337 172) rotate(-15)">
        <rect x="-13" y="-43" width="26" height="61" rx="13" className="ill-gold ill-pale ill-panel" />
        <path d="M0 18v31M-21 49h42" className="ill-gold ill-stroke ill-wide" />
      </g>
      <Label x={337} y={242} width={111} text={l[1]} tone="gold" />
      <Arrow d="M272 167c27 8 34 12 43 21" tone="gold" />
      <Arrow d="M362 187c27-24 51-30 78-22" tone="teal" />
      <g transform="translate(421 63)">
        <path d="M0 0h170v90H0z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M137 90l24 19-6-23" className="ill-teal ill-pale ill-bubble-tail" />
        <Label x={85} y={45} width={151} text={l[2]} tone="teal" height={44} />
      </g>
      <Character x={526} y={249} scale={0.7} facing={-1} shirt="blue" hair="short" />
    </>
  ),

  'u19-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={4} />
      <g transform="translate(45 61)">
        <rect width="230" height="174" rx="21" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <PlainText x={115} y={53} text="?" width={50} size={45} tone="blue" />
        <Label x={115} y={103} width={198} text={l[0]} tone="blue" />
        <Character x={115} y={166} scale={0.43} shirt="coral" hair="bob" pose="point" />
      </g>
      <g transform="translate(303 80)">
        <path d="M0 0h95v140H0z" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M24 27h47M24 48h47M24 69h31" className="ill-muted-stroke ill-fine" />
        <path d="M18 102h59" className="ill-gold ill-stroke ill-wide" />
        <Label x={47} y={165} width={118} text={l[1]} tone="gold" />
      </g>
      <Arrow d="M280 147h21" tone="gold" />
      <Arrow d="M400 147h28" tone="teal" />
      <g transform="translate(431 61)">
        <rect width="166" height="174" rx="21" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 45h116v80H25z" className="ill-paper ill-panel" />
        <path d="M25 45l58 45 58-45" className="ill-teal ill-stroke ill-fine" />
        <Check x={133} y={124} scale={0.42} />
        <Label x={83} y={199} width={190} text={l[2]} tone="teal" />
      </g>
    </>
  ),

  'u19-l3': (l) => (
    <>
      <Backdrop tone="gold" variant={3} />
      <Character x={101} y={247} scale={0.78} shirt="gold" hair="short" pose="point" />
      <g transform="translate(171 56)">
        <path d="M0 0h187v76H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M22 76l-15 20 37-20" className="ill-paper ill-bubble-tail" />
        <Label x={93} y={38} width={161} text={l[0]} tone="paper" />
      </g>
      <g transform="translate(323 188)">
        <path d="M0 43V-34M0-34l72 18L0 2" className="ill-coral ill-stroke ill-wide" />
        <path d="M11-27l16 16 27-31" className="ill-paper-stroke ill-wide" />
      </g>
      <Label x={360} y={247} width={126} text={l[1]} tone="coral" />
      <Arrow d="M287 144c27 12 38 24 42 39" tone="coral" />
      <Arrow d="M400 171c25-18 44-18 66-2" tone="blue" />
      <Character x={531} y={250} scale={0.75} facing={-1} shirt="blue" hair="bob" pose="stand" />
      <Label x={504} y={70} width={238} text={l[2]} tone="blue" />
      <path d="M493 102l27 34" className="ill-blue ill-stroke ill-fine" />
    </>
  ),

  'u19-l4': (l) => (
    <>
      <Backdrop tone="violet" variant={5} />
      <g transform="translate(64 55)">
        <path d="M0 0h512v184H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M29 72h184v67H29z" className="ill-blue ill-pale ill-panel" />
        <PlainText x={121} y={112} text="Do you know" width={145} size={18} tone="blue" />
        <path d="M242 46h235v110H242z" className="ill-violet ill-pale ill-panel ill-dashed" />
        <path d="M272 74h175M272 99h128M272 124h156" className="ill-muted-stroke ill-fine" />
        <path d="M214 105h26" className="ill-violet ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <Label x={360} y={101} width={205} text={l[0]} tone="violet" />
      </g>
      <Label x={200} y={265} width={220} text={l[1]} tone="blue" />
      <g transform="translate(493 42)"><path d="M-25 0h50v26h-50z" className="ill-gold ill-pale ill-panel" /><path d="M-14 11h28" className="ill-muted-stroke ill-fine" /></g>
      <PlainText x={320} y={35} text="QUESTION INSIDE A SENTENCE" width={270} size={14} tone="violet" />
    </>
  ),

  'u20-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={1} />
      <Character x={82} y={244} scale={0.77} shirt="teal" hair="cap" pose="think" />
      <g transform="translate(127 112)">
        <circle r="34" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <circle r="18" className="ill-blue ill-pale ill-panel" />
        <path d="M25 25l31 31" className="ill-ink-stroke ill-check" />
      </g>
      <path d="M208 224L540 224 540 83 208 188z" className="ill-teal ill-wash" />
      <path d="M208 224h356" className="ill-ink-stroke ill-wide" markerEnd="url(#ill-arrow)" />
      {[251, 385, 520].map((x, i) => <g key={x}><path d={`M${x} 215v18`} className="ill-ink-stroke ill-fine" /><circle cx={x} cy={184 - i * 34} r={18 + i * 8} className={`ill-${i === 0 ? 'coral' : i === 1 ? 'gold' : 'green'} ill-pale ill-panel`} />{i === 2 && <Check x={x} y={116} scale={0.45} />}</g>)}
      <Label x={251} y={259} width={124} text={l[0]} tone="coral" />
      <Label x={385} y={259} width={124} text={l[1]} tone="gold" />
      <Label x={520} y={259} width={124} text={l[2]} tone="green" />
      <PlainText x={386} y={54} text="EVIDENCE" width={110} size={14} tone="teal" />
    </>
  ),

  'u20-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={0} />
      <g transform="translate(55 58)">
        <path d="M0 0h531v174H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M35 136C132 52 235 147 337 65c57-46 104-44 159-14" className="ill-muted-stroke ill-road ill-dashed" />
        {[93, 153, 224, 309, 399, 468].map((x, i) => <g key={x} transform={`translate(${x} ${118 - i * 12}) rotate(${i * 9 - 12})`}><ellipse cx="-8" cy="0" rx="8" ry="15" className="ill-violet ill-pale ill-panel" /><ellipse cx="10" cy="-10" rx="7" ry="13" className="ill-violet ill-pale ill-panel" /></g>)}
        <Clock x={466} y={68} r={28} time="eight" tone="violet" />
        <path d="M58 37h83M58 54h56" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={148} y={258} width={173} text={l[0]} tone="coral" />
      <Label x={320} y={258} width={173} text={l[1]} tone="gold" />
      <Label x={493} y={258} width={173} text={l[2]} tone="green" />
      <path d="M148 218v-49M320 218v-89M493 218v-127" className="ill-muted-stroke ill-fine ill-dashed" />
      <PlainText x={320} y={38} text="RECONSTRUCTING THE PAST" width={280} size={14} tone="violet" />
    </>
  ),

  'u20-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={4} />
      <Character x={128} y={251} scale={0.85} shirt="blue" hair="short" pose="think" mood="sad" />
      <g transform="translate(203 172) rotate(-8)">
        <rect x="-24" y="-39" width="48" height="78" rx="8" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M-13-25h26M-10 20h20" className="ill-muted-stroke ill-fine" />
        <circle cx="19" cy="-32" r="8" className="ill-coral ill-solid" />
      </g>
      <path d="M213 137c10-26 27-39 50-35 6-41 53-48 75-19 24-26 69-13 69 24 39-7 62 28 42 57 28 26 4 69-33 65H290c-40 2-58-40-30-65-32-5-51-34-47-27z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <g transform="translate(338 159)">
        <rect x="-55" y="-42" width="110" height="84" rx="9" className="ill-green ill-pale ill-panel" />
        <path d="M-28-11h56M-28 8h42" className="ill-muted-stroke ill-fine" />
        <Check x={37} y={22} scale={0.38} />
      </g>
      <Label x={132} y={61} width={152} text={l[0]} tone="coral" />
      <Label x={424} y={75} width={256} text={l[1]} tone="blue" />
      <PlainText x={363} y={265} text="missed chance" width={120} size={13} tone="muted" />
    </>
  ),

  'u20-l4': (l) => (
    <>
      <Backdrop tone="blue" variant={3} />
      <g transform="translate(76 49) rotate(-4 175 101)">
        <rect width="350" height="202" rx="9" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <rect x="17" y="17" width="316" height="139" rx="4" className="ill-blue ill-pale" />
        <path d="M17 107q157-36 316 0v49H17z" className="ill-blue ill-solid ill-water" />
        <Character x={175} y={144} scale={0.57} shirt="coral" hair="short" pose="celebrate" />
        <path d="M50 126q25-19 50 0M251 130q25-19 50 0" className="ill-paper-stroke ill-wide" />
        <PlainText x={175} y={184} text="THEN" width={70} size={14} tone="muted" />
      </g>
      <path d="M439 146c31-79 120-75 135-6 15 71-70 112-119 62" className="ill-coral ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      <Calendar x={516} y={105} width={93} height={78} day="OLD" tone="coral" />
      <Label x={332} y={263} width={285} text={l[0]} tone="blue" />
      <Label x={518} y={248} width={181} text={l[1]} tone="coral" />
    </>
  ),

  'u21-l1': (l) => (
    <>
      <Backdrop tone="green" variant={2} />
      <Divider label="vs" />
      <g transform="translate(44 65)">
        <rect width="239" height="169" rx="21" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Tree x={59} y={158} scale={0.48} />
        <Character x={144} y={159} scale={0.53} shirt="blue" hair="cap" pose="sit" />
        <path d="M106 159h94" className="ill-gold ill-stroke ill-wide" />
        <path d="M189 90h26v39h-26z" className="ill-blue ill-pale ill-panel" />
        <Label x={119} y={194} width={226} text={l[0]} tone="gold" />
      </g>
      <g transform="translate(357 65)">
        <rect width="239" height="169" rx="21" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Cloud x={120} y={58} scale={0.63} />
        <path d="M78 117l-7 15M119 117l-7 15M160 117l-7 15" className="ill-blue ill-stroke ill-wide" />
        <path d="M77 143h85" className="ill-coral ill-stroke ill-check" />
        <Label x={119} y={194} width={226} text={l[1]} tone="blue" />
      </g>
      <PlainText x={160} y={43} text="stop + TO = purpose" width={170} size={13} tone="gold" />
      <PlainText x={479} y={43} text="stop + ING = end" width={170} size={13} tone="blue" />
    </>
  ),

  'u21-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={5} />
      <Character x={85} y={247} scale={0.78} shirt="coral" hair="bob" pose="point" />
      <Label x={84} y={55} width={92} text={l[0]} tone="coral" />
      <Arrow d="M144 144c37-31 70-35 99-15" tone="coral" />
      <g transform="translate(307 147)">
        <rect x="-77" y="-48" width="154" height="96" rx="18" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M-47-13h94M-32 11h64" className="ill-muted-stroke ill-fine" />
        <path d="M-7-48l7-17 7 17" className="ill-gold ill-stroke ill-wide" />
      </g>
      <Label x={307} y={228} width={224} text={l[1]} tone="gold" />
      <Arrow d="M387 129c37-19 67-9 89 24" tone="blue" />
      <Character x={533} y={247} scale={0.78} facing={-1} shirt="blue" hair="short" pose="carry" />
      <Label x={534} y={55} width={94} text={l[2]} tone="blue" />
      <g transform="translate(463 192)"><path d="M-41 16h82L34-9 15-23h-35L-36-8z" className="ill-blue ill-pale ill-panel" /><circle cx="-25" cy="17" r="10" className="ill-ink-fill" /><circle cx="25" cy="17" r="10" className="ill-ink-fill" /></g>
    </>
  ),

  'u21-l3': (l) => (
    <>
      <Backdrop tone="teal" variant={1} />
      <g transform="translate(58 56)">
        <rect width="524" height="184" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <g transform="translate(41 34)">
          <rect width="132" height="112" rx="17" className="ill-blue ill-pale ill-panel" />
          <rect x="42" y="15" width="48" height="82" rx="8" className="ill-paper ill-panel" />
          <path d="M52 32h28M52 47h28M52 62h18" className="ill-muted-stroke ill-fine" />
          <Check x={81} y={87} scale={0.34} />
        </g>
        <path d="M205 73h91v44h-91z" className="ill-teal ill-pale ill-panel ill-dashed" />
        <path d="M175 95h29" className="ill-teal ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <Label x={250} y={95} width={177} text={l[0]} tone="teal" />
        <g transform="translate(336 34)">
          <path d="M0 0h147v112H0z" className="ill-gold ill-pale ill-panel" />
          <PlainText x={73} y={50} text="It is easy" width={120} size={18} tone="gold" />
          <path d="M29 72h89" className="ill-muted-stroke ill-fine" />
          <Check x={122} y={89} scale={0.38} />
        </g>
      </g>
      <Label x={452} y={262} width={216} text={l[1]} tone="gold" />
      <PlainText x={190} y={265} text="action fits the adjective" width={210} size={14} tone="muted" />
    </>
  ),

  'u22-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={4} />
      <g transform="translate(48 85)">
        <path d="M0 112h544" className="ill-muted-stroke ill-floor" />
        <g transform="translate(57 57)"><path d="M0 27h182v-70H0z" className="ill-blue ill-pale ill-panel" /><path d="M23-25h30v31H23zM67-25h30v31H67zM111-25h30v31h-30z" className="ill-paper ill-panel" /><path d="M182 27l34-17-34-53" className="ill-blue ill-pale ill-panel" /><circle cx="38" cy="30" r="15" className="ill-ink-fill" /><circle cx="145" cy="30" r="15" className="ill-ink-fill" /></g>
        <Character x={362} y={109} scale={0.62} shirt="coral" hair="short" pose="walk" mood="sad" />
        <Clock x={440} y={24} r={31} time="eight" tone="coral" />
        <path d="M292 60c31-59 92-75 130-44" className="ill-coral ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      </g>
      <path d="M438 75c10-29 31-39 54-28 7-34 47-34 60-7 30-6 49 22 34 45 22 19 3 49-26 46H482c-31 0-42-32-22-51-17-1-29-10-22-5z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <Label x={167} y={252} width={180} text={l[0]} tone="coral" />
      <Label x={486} y={159} width={267} text={l[1]} tone="violet" />
      <PlainText x={320} y={36} text="PAST → REWIND" width={160} size={14} tone="violet" />
    </>
  ),

  'u22-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={2} />
      <Character x={144} y={252} scale={0.86} shirt="teal" hair="bob" pose="think" mood="sad" />
      <Clock x={97} y={72} r={38} time="six" tone="coral" />
      <Cross x={159} y={70} scale={0.56} />
      <Label x={125} y={134} width={170} text={l[0]} tone="coral" />
      <g transform="translate(247 59)">
        <path d="M0 0h330v179H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M22 21h286v137H22z" className="ill-paper ill-panel" />
        <Sun x={250} y={58} r={24} />
        <Tree x={82} y={151} scale={0.42} />
        <path d="M25 139l74-65 57 50 43-38 105 53" className="ill-green ill-pale ill-landscape" />
        <Character x={166} y={151} scale={0.45} shirt="coral" hair="short" pose="celebrate" />
      </g>
      <path d="M205 153c13-29 24-42 43-46" className="ill-blue ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      <Label x={412} y={263} width={305} text={l[1]} tone="blue" />
      <Sparkles x={570} y={51} tone="gold" />
    </>
  ),

  'u22-l3': (l) => (
    <>
      <Backdrop tone="gold" variant={0} />
      <g transform="translate(49 59)">
        <path d="M0 174h542" className="ill-muted-stroke ill-floor" />
        <g transform="translate(9 91)">
          <path d="M0 0h161v83H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
          <Sun x={42} y={32} r={19} />
          <House x={112} y={77} scale={0.35} tone="green" />
          <Label x={80} y={104} width={150} text={l[0]} tone="green" />
        </g>
        <g transform="translate(190 52)">
          <path d="M0 0h161v122H0z" className="ill-violet ill-pale ill-panel" filter="url(#ill-shadow)" />
          <Character x={80} y={116} scale={0.49} shirt="violet" hair="bob" pose="think" />
          <path d="M108 28c5-18 17-23 31-17 4-17 25-17 31-3 15-3 24 11 16 23" className="ill-paper ill-panel" />
          <Label x={80} y={143} width={150} text={l[1]} tone="violet" />
        </g>
        <g transform="translate(371 10)">
          <path d="M0 0h161v164H0z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
          <g transform="translate(80 65) rotate(-5)"><rect x="-50" y="-39" width="100" height="78" rx="5" className="ill-paper ill-panel" /><path d="M-38 19l28-33 21 22 14-14 20 25" className="ill-blue ill-pale ill-landscape" /></g>
          <path d="M32 119h96" className="ill-coral ill-stroke ill-wide ill-dashed" />
          <Label x={80} y={185} width={150} text={l[2]} tone="coral" />
        </g>
      </g>
      <Arrow d="M180 126h50" tone="gold" />
      <Arrow d="M362 89h49" tone="gold" />
      <PlainText x={320} y={38} text="REALITY  →  NOW  →  PAST" width={270} size={14} tone="gold" />
    </>
  ),
} satisfies IllustrationSceneMap
