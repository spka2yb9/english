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
  Sun,
  Tree,
} from './primitives'

export const B1_SCENES = {
  'u11-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={2} />
      <path d="M47 227h546" className="ill-muted-stroke ill-floor" />
      <g transform="translate(80 80) rotate(-5)">
        <rect width="160" height="118" rx="8" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <rect x="14" y="14" width="132" height="73" rx="4" className="ill-violet ill-pale" />
        <path d="M22 81l38-43 35 32 21-20 25 31" className="ill-blue ill-pale ill-landscape" />
        <PlainText x={80} y={107} text="PAST" width={70} size={12} tone="muted" />
      </g>
      <g transform="translate(260 68)">
        <path d="M0 155C4 33 113 10 213 155" className="ill-teal ill-stroke ill-bridge" />
        <path d="M20 143h174M46 100h119M78 62h58" className="ill-teal ill-stroke ill-fine" />
        <circle cx="1" cy="157" r="9" className="ill-coral ill-solid" />
        <circle cx="213" cy="157" r="9" className="ill-green ill-solid" />
      </g>
      <Character x={506} y={237} scale={0.79} shirt="green" hair="bob" pose="wave" />
      <Label x={157} y={255} width={185} text={l[0]} tone="coral" />
      <Label x={493} y={267} width={174} text={l[1]} tone="green" />
      <Arrow d="M249 54c82-36 156-30 208 6" tone="teal" />
    </>
  ),

  'u11-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={1} />
      <g transform="translate(58 48) rotate(-3 260 100)">
        <rect width="524" height="202" rx="16" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M262 0v202" className="ill-muted-stroke ill-fine" />
        <path d="M30 31h197M30 50h149M30 72h173" className="ill-muted-stroke ill-fine" />
        <circle cx="107" cy="127" r="39" className="ill-blue ill-pale ill-panel" />
        <path d="M81 127h52M107 101v52" className="ill-blue ill-stroke ill-fine" />
        <path d="M295 31h196M295 50h142" className="ill-muted-stroke ill-fine" />
        {[327, 392, 457].map((x, i) => <g key={x}><circle cx={x} cy="124" r="26" className={`ill-${i === 0 ? 'coral' : i === 1 ? 'gold' : 'teal'} ill-pale ill-panel`} /><Check x={x} y={124} scale={0.47} tone={i === 0 ? 'coral' : i === 1 ? 'gold' : 'teal'} /><NumberBadge x={x} y={168} number={String(i + 1)} tone={i === 0 ? 'coral' : i === 1 ? 'gold' : 'teal'} /></g>)}
      </g>
      <Label x={164} y={273} width={158} text={l[0]} tone="coral" />
      <Label x={319} y={273} width={158} text={l[1]} tone="gold" />
      <Label x={476} y={273} width={158} text={l[2]} tone="teal" />
      <PlainText x={320} y={28} text="EXPERIENCE PASSPORT" width={230} size={14} tone="coral" />
    </>
  ),

  'u11-l3': (l) => (
    <>
      <Backdrop tone="green" variant={0} />
      <path d="M57 237h531" className="ill-gold ill-stroke ill-floor" />
      <g transform="translate(113 218)">
        <path d="M-38-36h76l-9 36h-58z" className="ill-coral ill-pale ill-panel" />
        <path d="M0-35v-40M0-65l-23-19M0-55l24-23" className="ill-green ill-stroke ill-wide" />
        <circle cx="-27" cy="-88" r="15" className="ill-green ill-pale" />
        <circle cx="28" cy="-84" r="17" className="ill-green ill-pale" />
      </g>
      <g transform="translate(318 218)">
        <path d="M-48-42h96l-11 42h-74z" className="ill-coral ill-pale ill-panel" />
        <path d="M0-41v-83M0-98l-38-30M0-83l41-35M0-63l-44-17" className="ill-green ill-stroke ill-symbol" />
        <circle cx="-45" cy="-137" r="26" className="ill-green ill-pale" /><circle cx="45" cy="-126" r="29" className="ill-green ill-pale" /><circle cx="-49" cy="-84" r="24" className="ill-green ill-pale" />
      </g>
      <Tree x={524} y={238} scale={0.85} />
      <Arrow d="M157 188c58-53 100-58 130-38" tone="green" />
      <Arrow d="M372 148c45-27 81-24 106 4" tone="green" />
      <Label x={111} y={267} width={178} text={l[0]} tone="coral" />
      <Label x={521} y={267} width={165} text={l[1]} tone="green" />
      <PlainText x={320} y={38} text="2019  ·  ·  ·  ·  ·  NOW" width={310} size={16} tone="green" />
    </>
  ),

  'u11-l4': (l) => (
    <>
      <Backdrop tone="blue" variant={5} />
      <g transform="translate(53 72)">
        <rect width="244" height="151" rx="22" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M44 46h156v72H44z" className="ill-paper ill-panel" />
        <path d="M44 46l78 51 78-51" className="ill-green ill-stroke ill-wide" />
        <path d="M66 24h112" className="ill-green ill-stroke ill-wide" markerEnd="url(#ill-arrow)" />
        <Check x={201} y={26} scale={0.55} />
        <Label x={122} y={176} width={204} text={l[0]} tone="green" />
      </g>
      <g transform="translate(344 72)">
        <rect width="244" height="151" rx="22" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M44 46h156v72H44z" className="ill-paper ill-panel" />
        <path d="M44 46l78 51 78-51" className="ill-coral ill-stroke ill-wide" />
        <Clock x={201} y={29} r={22} time="three" tone="coral" />
        <path d="M97 22h50" className="ill-coral ill-stroke ill-wide ill-dashed" />
        <Label x={122} y={176} width={204} text={l[1]} tone="coral" />
      </g>
      <PlainText x={320} y={47} text="STATUS NOW" width={140} size={13} tone="blue" />
    </>
  ),

  'u11-l5': (l) => (
    <>
      <Backdrop tone="gold" variant={2} />
      <Divider label="vs" />
      <g transform="translate(45 64)">
        <rect width="230" height="170" rx="20" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M48 75q38-52 76 0t76 0" className="ill-gold ill-stroke ill-wide ill-dashed" />
        <g transform="translate(108 91) rotate(-22)"><circle cx="-18" r="17" className="ill-gold ill-pale ill-panel" /><path d="M0 0h69M42 0v19M57 0v13" className="ill-gold ill-stroke ill-symbol" /></g>
        <path d="M44 125h143" className="ill-muted-stroke ill-fine" />
        <Label x={115} y={195} width={226} text={l[0]} tone="gold" />
      </g>
      <g transform="translate(365 64)">
        <rect width="230" height="170" rx="20" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={77} y={163} scale={0.54} shirt="blue" hair="short" mood="sad" />
        <path d="M139 42h59v121h-59z" className="ill-paper ill-panel" />
        <circle cx="151" cy="103" r="4" className="ill-ink-fill" />
        <path d="M124 133h74" className="ill-coral ill-stroke ill-wide" />
        <Cross x={168} y={73} scale={0.52} />
        <Label x={115} y={195} width={226} text={l[1]} tone="coral" />
      </g>
      <PlainText x={154} y={44} text="finished past" width={100} size={12} tone="muted" />
      <PlainText x={486} y={44} text="result now" width={100} size={12} tone="coral" />
    </>
  ),

  'u11-l6': (l) => (
    <>
      <Backdrop tone="violet" variant={3} />
      <g transform="translate(43 62)">
        <path d="M0 169h554" className="ill-muted-stroke ill-floor" />
        <g transform="translate(18)">
          <path d="M0 108h148v61H0z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
          <path d="M25 82h98v26H25z" className="ill-paper ill-panel" />
          <path d="M49 43h50v39H49z" className="ill-blue ill-pale ill-panel" />
          <Check x={74} y={62} scale={0.42} />
          <Label x={74} y={139} width={120} text={l[0]} tone="coral" />
        </g>
        <g transform="translate(203)">
          <path d="M0 74h148v95H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
          <path d="M74 74v-44M74 57l-30-21M74 47l29-25" className="ill-green ill-stroke ill-wide" />
          <circle cx="37" cy="27" r="18" className="ill-green ill-pale" /><circle cx="109" cy="15" r="19" className="ill-green ill-pale" />
          <Label x={74} y={120} width={120} text={l[1]} tone="green" />
        </g>
        <g transform="translate(388)">
          <path d="M0 40h148v129H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
          <path d="M30 68h88v55H30z" className="ill-paper ill-panel" />
          <path d="M30 68l44 37 44-37" className="ill-blue ill-stroke ill-fine" />
          <Check x={120} y={52} scale={0.45} />
          <Label x={74} y={145} width={120} text={l[2]} tone="blue" />
        </g>
      </g>
      <Arrow d="M153 78h73" tone="violet" />
      <Arrow d="M339 78h72" tone="violet" />
      <PlainText x={320} y={33} text="PRESENT PERFECT GALLERY" width={280} size={14} tone="violet" />
    </>
  ),

  'u12-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={0} />
      <Calendar x={184} y={133} width={195} height={166} day="3:00" tone="coral" />
      <Character x={427} y={243} scale={0.78} shirt="teal" hair="short" pose="wave" />
      <Character x={545} y={243} scale={0.78} facing={-1} shirt="gold" hair="bob" pose="wave" />
      <g transform="translate(487 185)"><circle r="29" className="ill-paper ill-panel" /><path d="M-15 2q15-18 30 0M-11 10q11 13 22 0" className="ill-coral ill-stroke ill-fine" /></g>
      <Label x={417} y={63} width={284} text={l[0]} tone="teal" />
      <Label x={184} y={252} width={232} text={l[1]} tone="coral" />
      <Arrow d="M295 142c38-41 79-47 112-26" tone="coral" dashed />
      <Check x={344} y={96} scale={0.58} />
    </>
  ),

  'u12-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={1} />
      <g transform="translate(35 70)">
        <Panel x={0} y={0} width={176} height={158} tone="gold">
          <path d="M88 27l10 24 26 2-20 17 7 25-23-13-23 13 7-25-20-17 26-2z" className="ill-gold ill-solid" />
          <path d="M61 113h54" className="ill-muted-stroke ill-fine" />
          <Label x={88} y={178} width={158} text={l[0]} tone="gold" />
        </Panel>
        <Panel x={199} y={0} width={176} height={158} tone="blue">
          <path d="M231 33h111v78H231z" className="ill-paper ill-panel" />
          <path d="M249 52h75M249 70h61M249 88h48" className="ill-muted-stroke ill-fine" />
          <Check x={326} y={103} scale={0.42} />
          <Label x={287} y={178} width={172} text={l[1]} tone="blue" />
        </Panel>
        <Panel x={398} y={0} width={176} height={158} tone="teal">
          <path d="M431 33h110v79H431z" className="ill-paper ill-panel" />
          <path d="M431 58h110M456 28v25M516 28v25" className="ill-teal ill-stroke ill-wide" />
          <circle cx="486" cy="84" r="14" className="ill-coral ill-solid" />
          <Label x={486} y={178} width={172} text={l[2]} tone="teal" />
        </Panel>
      </g>
      <PlainText x={320} y={43} text="decision  →  plan  →  arrangement" width={330} size={14} tone="muted" />
    </>
  ),

  'u12-l3': (l) => (
    <>
      <Backdrop tone="green" variant={4} />
      <g transform="translate(53 164)">
        <path d="M0 39h262l-19-48-53-28H78L38-6z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M84-31L58-5h161l-37-26z" className="ill-blue ill-pale ill-panel" />
        <circle cx="72" cy="41" r="23" className="ill-ink-fill" /><circle cx="72" cy="41" r="10" className="ill-paper" />
        <circle cx="213" cy="41" r="23" className="ill-ink-fill" /><circle cx="213" cy="41" r="10" className="ill-paper" />
        <path d="M286-66v109M266-66h40" className="ill-ink-stroke ill-wide" />
        <circle cx="286" cy="-78" r="15" className="ill-green ill-solid" />
      </g>
      <Character x={497} y={250} scale={0.8} facing={-1} shirt="coral" hair="bob" pose="point" />
      <g transform="translate(421 145) rotate(-9)">
        <rect x="-23" y="-38" width="46" height="76" rx="7" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M-13-24h26M-10 19h20" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={189} y={72} width={245} text={l[0]} tone="green" />
      <Arrow d="M328 81c41-21 80-15 106 15" tone="green" />
      <Label x={489} y={66} width={226} text={l[1]} tone="coral" />
      <PlainText x={320} y={268} text="WHEN: present  /  MAIN: will" width={270} size={14} tone="muted" />
    </>
  ),

  'u13-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={3} />
      <g transform="translate(42 57)">
        <rect width="225" height="176" rx="19" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <Character x={72} y={167} scale={0.58} shirt="coral" hair="bob" pose="carry" />
        <path d="M132 92h67v75h-67z" className="ill-blue ill-pale ill-panel" />
        <path d="M145 68h41v24h-41z" className="ill-gold ill-pale ill-panel" />
        <path d="M126 136h79" className="ill-green ill-stroke ill-fine" />
        <Label x={112} y={201} width={212} text={l[0]} tone="paper" />
      </g>
      <Arrow d="M282 145h70" tone="teal" width={5} />
      <Label x={317} y={100} width={135} text={l[1]} tone="teal" height={33} />
      <g transform="translate(373 57)">
        <rect width="225" height="176" rx="19" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M68 84h90v83H68z" className="ill-paper ill-panel" />
        <path d="M86 55h55v29H86z" className="ill-gold ill-pale ill-panel" />
        <Sparkles x={164} y={69} tone="gold" />
        <path d="M55 143h116" className="ill-green ill-stroke ill-fine" />
        <path d="M112 15l-52 122h104z" className="ill-gold ill-wash" />
        <Label x={112} y={201} width={212} text={l[2]} tone="teal" />
      </g>
    </>
  ),

  'u13-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={2} />
      <g transform="translate(71 67)">
        <rect width="498" height="165" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M39 123h420" className="ill-muted-stroke ill-floor" />
        <path d="M79 52h96v71H79z" className="ill-blue ill-pale ill-panel" />
        <Sparkles x={176} y={47} tone="gold" />
        <g opacity=".3"><Character x={371} y={121} scale={0.53} shirt="violet" hair="short" pose="carry" /></g>
        <path d="M331 19h92v104h-92z" className="ill-muted-stroke ill-dashed" />
        <Cross x={419} y={38} scale={0.48} />
        <Arrow d="M292 82h-76" tone="blue" />
        <Label x={249} y={191} width={445} text={l[0]} tone="paper" />
      </g>
      <path d="M320 32v40" className="ill-coral ill-stroke ill-wide" markerEnd="url(#ill-arrow)" />
      <Label x={320} y={267} width={292} text={l[1]} tone="blue" />
    </>
  ),

  'u13-l3': (l) => (
    <>
      <Backdrop tone="violet" variant={5} />
      <g transform="translate(45 70)">
        <Panel x={0} y={0} width={244} height={159} tone="coral">
          <Clock x={58} y={76} r={35} time="three" tone="coral" />
          <path d="M113 45h101v62H113z" className="ill-paper ill-panel" />
          <path d="M135 62h57M135 79h45" className="ill-muted-stroke ill-fine" />
          <Arrow d="M97 76h17" tone="coral" width={3} />
          <Label x={122} y={181} width={218} text={l[0]} tone="coral" />
        </Panel>
        <Panel x={306} y={0} width={244} height={159} tone="teal">
          <path d="M337 40h104v72H337z" className="ill-paper ill-panel" />
          <Check x={424} y={59} scale={0.46} />
          <path d="M455 40h65v72h-65z" className="ill-green ill-pale ill-panel" />
          <Sparkles x={488} y={76} tone="gold" />
          <path d="M349 91h72" className="ill-muted-stroke ill-fine" />
          <Label x={428} y={181} width={218} text={l[1]} tone="teal" />
        </Panel>
      </g>
      <PlainText x={320} y={43} text="PASSIVE ASSEMBLY LINE" width={250} size={14} tone="violet" />
      <Arrow d="M298 151h38" tone="violet" />
    </>
  ),

  'u13-l4': (l) => (
    <>
      <Backdrop tone="gold" variant={0} />
      <g transform="translate(46 55)">
        <path d="M0 0h219v183H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <Character x={109} y={170} scale={0.67} shirt="coral" hair="short" pose="point" />
        <path d="M109 3L42 149h134z" className="ill-coral ill-wash" />
        <Label x={109} y={208} width={208} text={l[0]} tone="coral" />
      </g>
      <Arrow d="M278 145h78" tone="gold" width={5} />
      <Label x={317} y={99} width={145} text={l[1]} tone="gold" />
      <g transform="translate(375 55)">
        <path d="M0 0h219v183H0z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M57 92h106v77H57z" className="ill-paper ill-panel" />
        <path d="M110 3L43 149h134z" className="ill-gold ill-wash" />
        <Sparkles x={157} y={74} tone="gold" />
        <Label x={109} y={208} width={208} text={l[2]} tone="teal" />
      </g>
    </>
  ),

  'u14-l1': (l) => (
    <>
      <Backdrop tone="green" variant={1} />
      <g transform="translate(66 64)">
        <path d="M0 169h234V0H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M30 29h174v116H30zM117 29v116M30 87h174" className="ill-blue ill-pale ill-panel" />
        <Character x={154} y={142} scale={0.48} shirt="coral" hair="short" pose="wave" />
        <Label x={117} y={194} width={202} text={l[0]} tone="paper" />
      </g>
      <g transform="translate(357 70)">
        <path d="M0 0h219v157H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <House x={110} y={145} scale={0.57} tone="green" />
        <Tree x={45} y={147} scale={0.38} />
        <Label x={109} y={187} width={240} text={l[1]} tone="green" />
      </g>
      <Arrow d="M301 147c24-28 38-29 52 0" tone="green" />
      <PlainText x={327} y={114} text="who" width={55} size={20} tone="coral" />
    </>
  ),

  'u14-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={4} />
      <Book x={128} y={146} scale={1.14} color="coral" />
      <g transform="translate(234 67)">
        <path d="M0 0h338v92H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M24 28h289M24 53h201" className="ill-muted-stroke ill-fine" />
        <rect x="137" y="14" width="112" height="52" rx="9" className="ill-coral ill-pale ill-panel ill-dashed" />
        <Cross x={273} y={-2} scale={0.53} />
        <Label x={169} y={114} width={325} text={l[0]} tone="paper" />
      </g>
      <Arrow d="M405 179v39" tone="coral" />
      <g transform="translate(234 224)">
        <rect x="0" y="0" width="338" height="43" rx="15" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Label x={169} y={21} width={315} text={l[1]} tone="teal" height={34} />
      </g>
    </>
  ),

  'u14-l3': (l) => (
    <>
      <Backdrop tone="blue" variant={3} />
      <g transform="translate(40 49)">
        <path d="M0 0h359v203H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M20 27l88 37 83-36 145 47v103l-145-45-83 37-88-38z" className="ill-green ill-pale ill-panel" />
        <path d="M108 64v106M191 28v105M39 129c83-81 156 29 269-43" className="ill-blue ill-stroke ill-road ill-dashed" />
        <House x={282} y={125} scale={0.37} tone="coral" />
        <circle cx="67" cy="107" r="8" className="ill-coral ill-solid" />
        <path d="M67 114l-8 15h16z" className="ill-coral ill-solid" />
        <Label x={179} y={225} width={220} text={l[0]} tone="paper" />
      </g>
      <g transform="translate(446 78)">
        <path d="M0 0h151v151H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M29 28h93v76H29z" className="ill-paper ill-panel" />
        <path d="M51 42h49M51 59h38M51 76h55" className="ill-muted-stroke ill-fine" />
        <path d="M75 105v24" className="ill-blue ill-stroke ill-wide" />
        <Label x={75} y={176} width={191} text={l[1]} tone="blue" />
      </g>
      <Arrow d="M404 137h35" tone="blue" />
    </>
  ),

  'u14-l4': (l) => (
    <>
      <Backdrop tone="violet" variant={0} />
      <g transform="translate(51 54)">
        <rect width="538" height="184" rx="24" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        {[82, 177, 272, 367, 462].map((x, i) => <g key={x}><Character x={x} y={155} scale={0.54} shirt={i === 1 || i === 3 ? 'teal' : i % 2 ? 'gold' : 'violet'} hair={i % 3 === 0 ? 'bob' : i % 3 === 1 ? 'short' : 'curl'} /><circle cx={x} cy="105" r="46" className={i === 1 || i === 3 ? 'ill-teal ill-stroke ill-spotlight' : 'ill-muted-stroke ill-dashed'} /></g>)}
        <path d="M148 20v145M337 20v145" className="ill-muted-stroke ill-fine ill-dashed" />
      </g>
      <Label x={175} y={267} width={193} text={l[0]} tone="violet" />
      <Label x={459} y={267} width={193} text={l[1]} tone="teal" />
      <PlainText x={320} y={40} text=",  extra information  ," width={240} size={14} tone="violet" />
    </>
  ),

  'u14-l5': (l) => (
    <>
      <Backdrop tone="gold" variant={5} />
      <g transform="translate(73 57)">
        <rect width="494" height="184" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M247 0v184" className="ill-muted-stroke ill-fine" />
        <g transform="translate(35 27)">
          <circle cx="74" cy="59" r="49" className="ill-blue ill-pale ill-panel" />
          <path d="M74 22v74M38 59h72" className="ill-blue ill-stroke ill-fine" />
          <path d="M148 34h47v51h-47z" className="ill-coral ill-pale ill-panel" />
          <Arrow d="M117 59h27" tone="gold" width={3} />
        </g>
        <g transform="translate(286 27)">
          <House x={59} y={105} scale={0.45} tone="green" />
          <path d="M130 21h55v64h-55z" className="ill-gold ill-pale ill-panel" />
          <path d="M145 37h25M145 52h25" className="ill-muted-stroke ill-fine" />
          <Arrow d="M105 62h21" tone="gold" width={3} />
        </g>
      </g>
      <Label x={194} y={264} width={210} text={l[0]} tone="blue" />
      <Label x={445} y={264} width={210} text={l[1]} tone="green" />
      <PlainText x={320} y={36} text="RELATIVE WORD TOOLBOX" width={260} size={14} tone="gold" />
    </>
  ),

  'u15-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={4} />
      <Cloud x={106} y={74} scale={0.68} raining />
      <circle cx="189" cy="163" r="9" className="ill-blue ill-solid" />
      <Road d="M196 159C285 107 365 109 471 79" tone="blue" dashed={false} />
      <Road d="M196 168C288 214 370 222 495 229" tone="green" dashed={false} />
      <House x={516} y={251} scale={0.63} tone="green" />
      <Sun x={514} y={71} r={29} />
      <Character x={93} y={245} scale={0.68} shirt="coral" hair="bob" pose="think" />
      <Label x={175} y={50} width={185} text={l[0]} tone="blue" />
      <Label x={458} y={121} width={171} text={l[2]} tone="gold" />
      <Label x={407} y={258} width={171} text={l[1]} tone="green" />
      <Arrow d="M221 146c79-39 148-47 224-60" tone="gold" />
      <Arrow d="M221 181c61 36 115 48 174 49" tone="green" />
    </>
  ),

  'u15-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={2} />
      <Character x={137} y={250} scale={0.84} shirt="blue" hair="short" pose="think" />
      <Clock x={94} y={71} r={36} time="ten" tone="coral" />
      <Cross x={157} y={67} scale={0.58} />
      <Label x={122} y={130} width={164} text={l[0]} tone="coral" />
      <path d="M204 140c10-18 29-26 43-17 5-33 44-36 58-10 16-20 52-11 51 17 33-8 55 18 42 43 30 16 18 57-13 57H248c-33 0-43-39-17-56-20-5-34-19-27-34z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <g transform="translate(309 177)">
        <path d="M-67 34L0-32l67 66" className="ill-coral ill-stroke ill-wide" />
        <path d="M-52 34v35h104V34" className="ill-green ill-pale ill-panel" />
        <circle cx="0" cy="-48" r="20" className="ill-sun" />
        <Tree x={45} y={67} scale={0.3} />
      </g>
      <Label x={434} y={82} width={278} text={l[1]} tone="violet" />
      <circle cx="204" cy="187" r="7" className="ill-paper ill-panel" /><circle cx="184" cy="210" r="4" className="ill-paper ill-panel" />
    </>
  ),

  'u15-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={1} />
      <g transform="translate(43 62)">
        <Panel x={0} y={0} width={247} height={175} tone="coral">
          <Cloud x={61} y={55} scale={0.5} raining />
          <Character x={168} y={166} scale={0.56} shirt="teal" hair="bob" pose="walk" />
          <path d="M105 73q35-57 70 0z" className="ill-gold ill-pale ill-panel" />
          <path d="M140 73v64" className="ill-ink-stroke ill-wide" />
          <Label x={124} y={198} width={200} text={l[0]} tone="coral" />
        </Panel>
        <Panel x={307} y={0} width={247} height={175} tone="blue">
          <path d="M342 42h176v95H342z" className="ill-paper ill-panel" />
          <path d="M364 65h45v48h-45zM421 65h73v16h-73zM421 91h58v16h-58z" className="ill-blue ill-pale ill-panel" />
          <path d="M357 28h47" className="ill-coral ill-stroke ill-wide" />
          <path d="M381 19v18" className="ill-coral ill-stroke ill-wide" />
          <Check x={493} y={126} scale={0.44} />
          <Label x={430} y={198} width={200} text={l[1]} tone="blue" />
        </Panel>
      </g>
      <PlainText x={320} y={39} text="remove condition  /  prepare beforehand" width={350} size={14} tone="muted" />
    </>
  ),

  'u15-l4': (l) => (
    <>
      <Backdrop tone="green" variant={3} />
      <Character x={82} y={248} scale={0.76} shirt="gold" hair="curl" pose="think" />
      <circle cx="171" cy="193" r="9" className="ill-gold ill-solid" />
      <Road d="M177 189C265 159 351 119 536 94" tone="green" dashed={false} />
      <Road d="M177 201C291 226 391 239 561 228" tone="violet" dashed={false} />
      <g transform="translate(512 87)"><Sun x={0} y={0} r={28} /><Check x={0} y={0} scale={0.45} /></g>
      <g transform="translate(520 206)"><path d="M-55 8L0-47 55 8v44h-110z" className="ill-violet ill-pale ill-panel" /><path d="M-17-19h34v30h-34z" className="ill-blue ill-pale ill-panel" /><Sparkles x={40} y={-40} tone="gold" /></g>
      <Label x={187} y={58} width={184} text={l[0]} tone="gold" />
      <Label x={413} y={51} width={218} text={l[1]} tone="green" />
      <Label x={419} y={270} width={230} text={l[2]} tone="violet" />
      <PlainText x={306} y={133} text="REAL" width={55} size={12} tone="green" />
      <PlainText x={317} y={228} text="IMAGINED" width={80} size={12} tone="violet" />
    </>
  ),

  'u16-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={0} />
      <g transform="translate(56 72)">
        <rect width="177" height="157" rx="20" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Cloud x={89} y={59} scale={0.67} raining />
        <path d="M33 125h112" className="ill-blue ill-stroke ill-floor" />
        <Label x={89} y={183} width={167} text={l[0]} tone="blue" />
      </g>
      {[262, 300, 338].map((x, i) => <rect key={x} x={x} y={119 + i * 15} width="24" height="70" rx="5" className={`ill-${i === 1 ? 'gold' : 'coral'} ill-pale ill-panel`} transform={`rotate(${18 + i * 12} ${x + 12} ${154 + i * 15})`} />)}
      <Label x={312} y={75} width={86} text={l[1]} tone="gold" />
      <Arrow d="M242 153h88" tone="gold" />
      <g transform="translate(388 72)">
        <rect width="196" height="157" rx="20" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <House x={98} y={144} scale={0.55} tone="green" />
        <Character x={52} y={144} scale={0.45} shirt="coral" hair="bob" />
        <Label x={98} y={183} width={188} text={l[2]} tone="green" />
      </g>
    </>
  ),

  'u16-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={4} />
      <g transform="translate(59 67)">
        <path d="M0 152h521M30 29h153v123H30zM339 29h153v123H339z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M47 55h119M47 79h119" className="ill-muted-stroke ill-fine" />
        <Character x={106} y={144} scale={0.52} shirt="coral" hair="bob" pose="think" />
        <path d="M361 49h111v76H361z" className="ill-blue ill-pale ill-panel" />
        <path d="M385 65h63M385 83h48" className="ill-muted-stroke ill-fine" />
        <Character x={417} y={144} scale={0.45} shirt="teal" hair="short" pose="wave" />
        <path d="M183 105h156" className="ill-violet ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <Clock x={261} y={55} r={29} time="three" tone="violet" />
      </g>
      <Label x={166} y={258} width={178} text={l[0]} tone="coral" />
      <Label x={468} y={258} width={188} text={l[1]} tone="teal" />
      <PlainText x={320} y={42} text="WAITING WINDOW" width={180} size={14} tone="violet" />
    </>
  ),

  'u16-l3': (l) => (
    <>
      <Backdrop tone="gold" variant={2} />
      <g transform="translate(54 61)">
        <Panel x={0} y={0} width={248} height={177} tone="green">
          <path d="M49 116h150M124 33v105" className="ill-green ill-stroke ill-symbol" />
          <circle cx="78" cy="76" r="27" className="ill-blue ill-pale ill-panel" />
          <circle cx="171" cy="76" r="27" className="ill-coral ill-pale ill-panel" />
          <path d="M93 76h63" className="ill-gold ill-stroke ill-wide" />
          <Check x={124} y={76} scale={0.45} />
          <Label x={124} y={201} width={220} text={l[0]} tone="green" />
        </Panel>
        <Panel x={303} y={0} width={248} height={177} tone="coral">
          <path d="M340 111h174M427 35v103" className="ill-coral ill-stroke ill-symbol" />
          <circle cx="382" cy="76" r="27" className="ill-blue ill-pale ill-panel" />
          <circle cx="474" cy="76" r="27" className="ill-coral ill-pale ill-panel" />
          <path d="M405 54l43 44M448 54l-43 44" className="ill-coral ill-stroke ill-wide" />
          <Label x={427} y={201} width={220} text={l[1]} tone="coral" />
        </Panel>
      </g>
      <PlainText x={320} y={39} text="PAIR LOGIC" width={120} size={14} tone="gold" />
    </>
  ),
} satisfies IllustrationSceneMap
