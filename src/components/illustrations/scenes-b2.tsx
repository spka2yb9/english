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
  Ear,
  Eye,
  House,
  Label,
  NumberBadge,
  PlainText,
  Sparkles,
  TinyStar,
} from './primitives'

export const B2_SCENES = {
  'u23-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={0} />
      <g transform="translate(45 61)">
        <rect width="550" height="174" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M275 0v174" className="ill-muted-stroke ill-fine ill-dashed" />
        <g transform="translate(28 25)">
          <Calendar x={69} y={62} width={115} height={93} day="PAST" tone="violet" />
          <path d="M146 29h78v86h-78z" className="ill-coral ill-pale ill-panel" />
          <path d="M162 51h46M162 70h32" className="ill-muted-stroke ill-fine" />
          <Cross x={202} y={100} scale={0.38} />
        </g>
        <g transform="translate(303 23)">
          <Character x={104} y={141} scale={0.53} shirt="blue" hair="short" mood="sad" pose="think" />
          <path d="M165 30h63v111h-63z" className="ill-teal ill-pale ill-panel" />
          <path d="M178 53h38M178 72h28M178 91h34" className="ill-muted-stroke ill-fine" />
          <Clock x={35} y={45} r={28} time="six" tone="coral" />
        </g>
      </g>
      <Arrow d="M275 97c30-50 62-50 91 0" tone="violet" />
      <Label x={178} y={259} width={193} text={l[0]} tone="violet" />
      <Label x={464} y={259} width={191} text={l[1]} tone="coral" />
      <PlainText x={320} y={36} text="PAST CAUSE  →  PRESENT RESULT" width={325} size={14} tone="violet" />
    </>
  ),

  'u23-l2': (l) => (
    <>
      <Backdrop tone="green" variant={3} />
      <g transform="translate(56 64)">
        <path d="M0 157h236V0H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M73 157V36h90v121" className="ill-paper ill-panel" />
        <path d="M38 28h160v43H38z" className="ill-green ill-solid" />
        <Check x={118} y={50} scale={0.48} tone="green" />
        <path d="M95 97h46M95 115h34" className="ill-muted-stroke ill-fine" />
        <Label x={118} y={183} width={224} text={l[0]} tone="green" />
      </g>
      <g transform="translate(348 64)">
        <path d="M0 157h236V0H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M73 157V36h90v121" className="ill-paper ill-panel" />
        <path d="M38 28h160v43H38z" className="ill-blue ill-solid" />
        <path d="M95 41h46M95 55h46" className="ill-paper-stroke ill-fine" />
        <path d="M95 97h46M95 115h34" className="ill-muted-stroke ill-fine" />
        <Label x={118} y={183} width={224} text={l[1]} tone="blue" />
      </g>
      <Character x={320} y={260} scale={0.61} shirt="gold" hair="bob" pose="think" />
      <PlainText x={320} y={40} text="ENTRY CONDITIONS" width={180} size={14} tone="green" />
    </>
  ),

  'u23-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={2} />
      <Character x={126} y={251} scale={0.84} shirt="teal" hair="bob" pose="think" />
      <Clock x={87} y={69} r={35} time="eight" tone="coral" />
      <Label x={127} y={130} width={174} text={l[0]} tone="coral" />
      <path d="M207 129c15-27 35-35 56-26 5-37 51-42 68-13 22-24 64-14 65 20 35-7 57 25 40 52 27 20 8 60-25 59H270c-35 0-51-35-29-59-25-3-40-22-34-33z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
      <g transform="translate(326 162)">
        <path d="M-87 35q17-57 65-40l47 18 48-18q47-17 64 40v34h-224z" className="ill-violet ill-pale ill-panel" />
        <path d="M-77 36h204M-31 7v62M79 7v62" className="ill-muted-stroke ill-fine" />
        <Book x={29} y={9} scale={0.35} color="gold" open />
      </g>
      <Label x={445} y={74} width={268} text={l[1]} tone="violet" />
      <path d="M195 178c10-6 18-11 26-12" className="ill-violet ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
    </>
  ),

  'u24-l1': (l) => (
    <>
      <Backdrop tone="coral" variant={1} />
      <g transform="translate(55 55)">
        <rect width="529" height="185" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M22 158h485" className="ill-muted-stroke ill-floor" />
        <Character x={124} y={153} scale={0.58} shirt="blue" hair="short" pose="sit" />
        <path d="M72 153h104M83 153v24M165 153v24" className="ill-gold ill-stroke ill-wide" />
        <g transform="translate(245 73) rotate(-14)">
          <circle cx="-17" cy="-17" r="16" className="ill-coral ill-pale ill-panel" /><circle cx="17" cy="17" r="16" className="ill-coral ill-pale ill-panel" />
          <path d="M-6-6l62 62M6 6l50-50" className="ill-ink-stroke ill-wide" />
        </g>
        <Character x={395} y={153} scale={0.64} facing={-1} shirt="coral" hair="bob" pose="point" />
        <path d="M418 36h65v122h-65z" className="ill-blue ill-pale ill-panel" />
        <path d="M430 57h41M430 76h31" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={111} y={266} width={104} text={l[0]} tone="blue" />
      <Label x={318} y={266} width={205} text={l[1]} tone="coral" />
      <Label x={516} y={266} width={122} text={l[2]} tone="teal" />
      <Arrow d="M168 44c98-35 194-30 286 5" tone="coral" dashed />
    </>
  ),

  'u24-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={4} />
      <g transform="translate(45 63)">
        <path d="M0 168h550" className="ill-muted-stroke ill-floor" />
        <g transform="translate(10)">
          <path d="M79 18v113M31 131h96" className="ill-green ill-stroke ill-symbol" />
          <path d="M79 39l52-27" className="ill-green ill-stroke ill-wide" />
          <circle cx="79" cy="39" r="8" className="ill-gold ill-solid" />
          <path d="M124 12l23-1-12 20" className="ill-green ill-stroke ill-wide" />
          <Label x={79} y={192} width={130} text={l[0]} tone="green" />
        </g>
        <g transform="translate(190)">
          <path d="M85 18v113M37 131h96" className="ill-blue ill-stroke ill-symbol" />
          <path d="M85 39h58" className="ill-blue ill-stroke ill-wide" />
          <circle cx="85" cy="39" r="8" className="ill-gold ill-solid" />
          <path d="M139 27l17 12-17 12" className="ill-blue ill-stroke ill-wide" />
          <Label x={85} y={192} width={160} text={l[1]} tone="blue" />
        </g>
        <g transform="translate(390)">
          <path d="M75 18v113M27 131h96" className="ill-coral ill-stroke ill-symbol" />
          <path d="M75 39l-52-27" className="ill-coral ill-stroke ill-wide" />
          <circle cx="75" cy="39" r="8" className="ill-gold ill-solid" />
          <path d="M30 12L7 11l12 20" className="ill-coral ill-stroke ill-wide" />
          <Label x={75} y={192} width={130} text={l[2]} tone="coral" />
        </g>
      </g>
      <PlainText x={320} y={41} text="freedom  ←  control  →  pressure" width={320} size={14} tone="gold" />
      <Character x={320} y={226} scale={0.45} shirt="gold" hair="short" />
    </>
  ),

  'u24-l3': (l) => (
    <>
      <Backdrop tone="blue" variant={5} />
      <g transform="translate(44 58)">
        <rect width="238" height="177" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Eye x={119} y={68} scale={0.72} />
        <path d="M53 133h132" className="ill-muted-stroke ill-floor" />
        <Character x={119} y={132} scale={0.4} shirt="coral" hair="short" pose="walk" />
        <Arrow d="M65 123h104" tone="blue" width={3} />
        <Label x={119} y={201} width={221} text={l[0]} tone="blue" />
      </g>
      <g transform="translate(359 58)">
        <rect width="238" height="177" rx="22" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Ear x={72} y={76} scale={0.62} />
        <path d="M122 44c23-25 48-25 70 0M122 68c23-25 48-25 70 0M122 92c23-25 48-25 70 0" className="ill-gold ill-stroke ill-fine" />
        <path d="M49 133h143" className="ill-muted-stroke ill-floor" />
        <Character x={170} y={132} scale={0.39} shirt="teal" hair="bob" pose="walk" />
        <Label x={119} y={201} width={221} text={l[1]} tone="gold" />
      </g>
      <PlainText x={320} y={40} text="whole action  /  action in progress" width={310} size={14} tone="blue" />
    </>
  ),

  'u25-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={3} />
      <g transform="translate(47 56)">
        <rect width="359" height="183" rx="21" className="ill-ink-fill" filter="url(#ill-shadow)" />
        <rect x="18" y="18" width="323" height="130" rx="8" className="ill-violet ill-pale" />
        <path d="M37 125l74-73 55 52 47-40 105 61" className="ill-muted-stroke ill-landscape" />
        <circle cx="278" cy="53" r="25" className="ill-gold ill-pale" />
        <path d="M29 161h301" className="ill-paper-stroke ill-wide" />
      </g>
      <Label x={220} y={258} width={215} text={l[0]} tone="violet" />
      <Arrow d="M408 147h54" tone="coral" />
      <Character x={532} y={246} scale={0.83} facing={-1} shirt="coral" hair="short" mood="sad" pose="sit" />
      <path d="M482 244h100" className="ill-gold ill-stroke ill-wide" />
      <Label x={528} y={68} width={177} text={l[1]} tone="coral" />
      <PlainText x={441} y={114} text="CAUSE → FEELING" width={150} size={12} tone="muted" />
    </>
  ),

  'u25-l2': (l) => (
    <>
      <Backdrop tone="teal" variant={0} />
      <g transform="translate(48 67)">
        <path d="M0 158h544" className="ill-muted-stroke ill-floor" />
        <path d="M42 19h142v139H42z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={113} y={152} scale={0.57} shirt="coral" hair="short" />
        <Label x={113} y={184} width={170} text={l[0]} tone="blue" />
        <path d="M210 52h305v89H210z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M232 76h261M232 100h214" className="ill-muted-stroke ill-fine" />
        <path d="M317 58h176v59H317z" className="ill-gold ill-pale ill-panel ill-dashed" />
        <Label x={405} y={81} width={159} text={l[1]} tone="gold" />
        <Arrow d="M193 96h18" tone="teal" width={3} />
      </g>
      <PlainText x={365} y={46} text="NOUN + DETAIL AFTER IT" width={250} size={14} tone="teal" />
    </>
  ),

  'u25-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={4} />
      <g transform="translate(43 57)">
        <path d="M0 0h554v180H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <g transform="translate(27 31)">
          <Character x={70} y={126} scale={0.53} shirt="blue" hair="bob" mood="sad" pose="walk" />
          <Clock x={148} y={50} r={27} time="six" tone="coral" />
          <path d="M195 19h115v106H195z" className="ill-coral ill-pale ill-panel" />
          <path d="M222 39h62M222 58h47" className="ill-muted-stroke ill-fine" />
          <Arrow d="M172 89h20" tone="coral" width={3} />
        </g>
        <Arrow d="M348 90h46" tone="teal" />
        <g transform="translate(407 32)">
          <path d="M0 0h119v123H0z" className="ill-teal ill-pale ill-panel" />
          <Character x={59} y={115} scale={0.48} shirt="blue" hair="bob" mood="sad" pose="walk" />
          <path d="M28 21h63" className="ill-teal ill-stroke ill-wide" />
        </g>
      </g>
      <Label x={211} y={261} width={333} text={l[0]} tone="coral" />
      <Label x={476} y={261} width={232} text={l[1]} tone="teal" />
      <PlainText x={320} y={38} text="COMPRESS THE REASON" width={220} size={14} tone="coral" />
    </>
  ),

  'u26-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={1} />
      <g transform="translate(55 60)">
        <rect width="530" height="176" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        {[63, 126, 189].map((x, i) => <g key={x}><Character x={x} y={164} scale={0.45} shirt={i === 0 ? 'coral' : i === 1 ? 'gold' : 'teal'} hair={i === 0 ? 'bob' : i === 1 ? 'short' : 'curl'} /><path d={`M${x - 25} 62h50v37h-50z`} className="ill-paper ill-panel" /><PlainText x={x} y={87} text="…" width={25} size={17} tone="blue" /></g>)}
        <path d="M239 37h61v127h-61z" className="ill-gold ill-pale ill-panel" />
        <path d="M254 58h31M254 77h31M254 96h31" className="ill-muted-stroke ill-fine" />
        <Arrow d="M213 91h24" tone="blue" width={3} />
        <path d="M328 28h167v113H328z" className="ill-paper ill-panel" />
        <Character x={411} y={135} scale={0.47} shirt="violet" hair="short" pose="think" />
        <TinyStar x={459} y={48} tone="gold" scale={1.1} />
        <Label x={411} y={157} width={188} text={l[0]} tone="paper" height={33} />
      </g>
      <Label x={247} y={263} width={230} text={l[1]} tone="blue" />
      <PlainText x={320} y={37} text="PUBLIC REPORT → PERSON" width={240} size={14} tone="blue" />
    </>
  ),

  'u26-l2': (l) => (
    <>
      <Backdrop tone="teal" variant={5} />
      <Divider label="vs" />
      <g transform="translate(52 64)">
        <rect width="232" height="169" rx="22" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M45 43h142v83H45z" className="ill-paper ill-panel" />
        <path d="M45 43l71 48 71-48M116 91v35" className="ill-gold ill-stroke ill-fine" />
        <path d="M83 22h66" className="ill-coral ill-stroke ill-wide" markerEnd="url(#ill-arrow)" />
        <Label x={116} y={194} width={210} text={l[0]} tone="gold" />
      </g>
      <g transform="translate(356 64)">
        <rect width="232" height="169" rx="22" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M45 43h142v83H45z" className="ill-paper ill-panel" />
        <path d="M45 43l71 48 71-48M116 91v35" className="ill-teal ill-stroke ill-fine" />
        <path d="M78 21c25-20 53-20 78 0" className="ill-teal ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
        <Label x={116} y={194} width={210} text={l[1]} tone="teal" />
      </g>
      <PlainText x={320} y={40} text="PASSIVE DESTINATION  /  PROCESS" width={330} size={14} tone="teal" />
    </>
  ),

  'u26-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={2} />
      <g transform="translate(50 60)">
        <rect width="236" height="174" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M77 35h82l-9 104H86z" className="ill-paper ill-panel" />
        <path d="M118 35l-8 30 15 21-13 22 6 31" className="ill-coral ill-stroke ill-wide" />
        <path d="M39 142h158" className="ill-muted-stroke ill-floor" />
        <Label x={118} y={199} width={222} text={l[0]} tone="blue" />
      </g>
      <g transform="translate(354 60)">
        <rect width="236" height="174" rx="22" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M77 35h82l-9 104H86z" className="ill-paper ill-panel" />
        <path d="M118 35l-8 30 15 21-13 22 6 31" className="ill-coral ill-stroke ill-wide" />
        <path d="M38 142h159" className="ill-muted-stroke ill-floor" />
        <path d="M192 21L157 63" className="ill-coral ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <TinyStar x={198} y={17} tone="coral" scale={1.2} />
        <Label x={118} y={199} width={222} text={l[1]} tone="coral" />
      </g>
      <PlainText x={166} y={41} text="STATE" width={70} size={13} tone="blue" />
      <PlainText x={472} y={41} text="EVENT" width={70} size={13} tone="coral" />
    </>
  ),

  'u27-l1': (l) => (
    <>
      <Backdrop tone="green" variant={0} />
      <House x={150} y={232} scale={0.84} tone="green" />
      <Label x={151} y={267} width={177} text={l[0]} tone="green" />
      <g transform="translate(292 79)">
        <path d="M0 0h292v139H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M29 29h234v80H29z" className="ill-paper ill-panel" />
        <path d="M50 50h192M50 71h144M50 92h171" className="ill-muted-stroke ill-fine" />
        <path d="M75 20v99" className="ill-coral ill-stroke ill-wide ill-dashed" />
        <Label x={146} y={162} width={261} text={l[1]} tone="blue" />
      </g>
      <path d="M215 160c29-44 48-49 74-37" className="ill-green ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
      <g transform="translate(265 119)"><ellipse cx="-22" cy="0" rx="32" ry="20" className="ill-gold ill-pale ill-panel" transform="rotate(-20)" /><ellipse cx="22" cy="0" rx="32" ry="20" className="ill-blue ill-pale ill-panel" transform="rotate(-20)" /></g>
      <PlainText x={320} y={42} text="PREPOSITION + WHICH" width={240} size={14} tone="green" />
    </>
  ),

  'u27-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={4} />
      <g transform="translate(55 57)">
        <rect width="530" height="182" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <Character x={74} y={167} scale={0.55} shirt="coral" hair="bob" pose="point" />
        <path d="M98 33h178v72H98z" className="ill-violet ill-pale ill-panel" />
        <path d="M120 105l-15 20 37-20" className="ill-violet ill-pale ill-bubble-tail" />
        <Label x={187} y={68} width={158} text={l[0]} tone="violet" />
        <path d="M300 37h80v105h-80z" className="ill-gold ill-pale ill-panel ill-dashed" />
        <path d="M320 60h40M320 82h40M320 104h28" className="ill-muted-stroke ill-fine" />
        <Arrow d="M278 89h19" tone="gold" width={3} />
        <path d="M406 48h97v94h-97z" className="ill-teal ill-pale ill-panel" />
        <Check x={454} y={87} scale={0.58} />
      </g>
      <Label x={456} y={263} width={212} text={l[1]} tone="teal" />
      <PlainText x={320} y={38} text="THE THING ITSELF" width={190} size={14} tone="violet" />
    </>
  ),

  'u27-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={1} />
      <g transform="translate(52 69)">
        <rect width="357" height="153" rx="20" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M27 33h303M27 58h260M27 83h284M27 108h217" className="ill-muted-stroke ill-fine" />
        <path d="M17 16h323v110H17z" className="ill-coral ill-stroke ill-spotlight" />
        <Label x={178} y={178} width={203} text={l[0]} tone="coral" />
      </g>
      <PlainText x={430} y={127} text="," width={30} size={38} tone="coral" />
      <Arrow d="M432 153c27 28 48 28 70 0" tone="coral" />
      <g transform="translate(493 76)">
        <path d="M0 0h102v124H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={51} y={117} scale={0.45} shirt="gold" hair="short" mood="surprised" />
        <Sparkles x={83} y={27} tone="gold" />
      </g>
      <Label x={502} y={246} width={236} text={l[1]} tone="blue" />
      <PlainText x={320} y={41} text="COMMENT ON THE WHOLE SENTENCE" width={310} size={14} tone="coral" />
    </>
  ),

  'u28-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={3} />
      <g transform="translate(45 58)">
        <rect width="205" height="177" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Cloud x={102} y={63} scale={0.72} raining />
        <path d="M34 140h137" className="ill-blue ill-stroke ill-floor" />
        <Label x={102} y={202} width={190} text={l[0]} tone="blue" />
      </g>
      <Arrow d="M264 146h81" tone="coral" width={5} />
      <Label x={304} y={99} width={132} text={l[1]} tone="coral" />
      <g transform="translate(364 58)">
        <rect width="231" height="177" rx="22" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={72} y={164} scale={0.54} shirt="coral" hair="bob" pose="walk" />
        <Character x={157} y={164} scale={0.54} facing={-1} shirt="gold" hair="short" pose="walk" />
        <path d="M43 101q72-82 144 0z" className="ill-coral ill-pale ill-panel" />
        <path d="M115 101v50" className="ill-ink-stroke ill-wide" />
        <Label x={115} y={202} width={213} text={l[2]} tone="green" />
      </g>
      <PlainText x={320} y={41} text="CONTRAST WINS" width={160} size={14} tone="coral" />
    </>
  ),

  'u28-l2': (l) => (
    <>
      <Backdrop tone="coral" variant={5} />
      <g transform="translate(50 58)">
        <rect width="208" height="178" rx="22" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M30 41l46 35 41-19 58 63" className="ill-coral ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <path d="M29 138h150M47 138v-21M87 138V99M127 138V83M167 138v-8" className="ill-muted-stroke ill-fine" />
        <Label x={104} y={203} width={193} text={l[0]} tone="coral" />
      </g>
      <g transform="translate(282 102)">
        <rect x="-17" y="-55" width="34" height="110" rx="6" className="ill-gold ill-pale ill-panel" transform="rotate(18)" />
        <path d="M-21-44l40 85" className="ill-gold ill-stroke ill-wide" />
      </g>
      <Arrow d="M267 151h74" tone="gold" />
      <Label x={304} y={88} width={138} text={l[1]} tone="gold" />
      <g transform="translate(361 58)">
        <rect width="229" height="178" rx="22" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M43 46h143v93H43z" className="ill-paper ill-panel" />
        <path d="M65 70h99M65 91h74" className="ill-muted-stroke ill-fine" />
        <path d="M114 112l16-34 16 34" className="ill-green ill-stroke ill-wide" />
        <path d="M45 139h139" className="ill-coral ill-stroke ill-wide" />
        <Label x={114} y={203} width={212} text={l[2]} tone="green" />
      </g>
    </>
  ),

  'u28-l3': (l) => (
    <>
      <Backdrop tone="gold" variant={0} />
      <g transform="translate(45 65)">
        <path d="M0 164h550" className="ill-muted-stroke ill-floor" />
        <g transform="translate(8 87)">
          <path d="M0 0h158v77H0z" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
          <NumberBadge x={28} y={24} number="1" tone="blue" />
          <path d="M61 23h72M61 43h54" className="ill-muted-stroke ill-fine" />
          <Label x={79} y={99} width={145} text={l[0]} tone="blue" />
        </g>
        <g transform="translate(196 47)">
          <path d="M0 0h158v117H0z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
          <NumberBadge x={28} y={24} number="2" tone="teal" />
          <path d="M61 23h72M61 43h54M26 70h106M26 90h83" className="ill-muted-stroke ill-fine" />
          <Label x={79} y={139} width={145} text={l[1]} tone="teal" />
        </g>
        <g transform="translate(384 7)">
          <path d="M0 0h158v157H0z" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
          <path d="M27 27h104v91H27z" className="ill-paper ill-panel" />
          <path d="M46 49h66M46 69h66M46 89h48" className="ill-muted-stroke ill-fine" />
          <Check x={119} y={112} scale={0.4} />
          <Label x={79} y={179} width={145} text={l[2]} tone="coral" />
        </g>
      </g>
      <Arrow d="M198 150h36" tone="gold" />
      <Arrow d="M386 109h36" tone="gold" />
      <PlainText x={320} y={39} text="BUILD A CLEAR ARGUMENT" width={250} size={14} tone="gold" />
    </>
  ),

  'u29-l1': (l) => (
    <>
      <Backdrop tone="violet" variant={2} />
      <Character x={102} y={249} scale={0.79} shirt="coral" hair="bob" pose="think" />
      <g transform="translate(160 67)">
        <path d="M0 0h412v157H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 51h122v68H25z" className="ill-violet ill-pale ill-panel" />
        <PlainText x={86} y={91} text="I think" width={90} size={19} tone="violet" />
        <path d="M177 35h206v101H177z" className="ill-gold ill-pale ill-panel ill-dashed" />
        <path d="M204 57h152M204 80h121M204 103h142" className="ill-muted-stroke ill-fine" />
        <Arrow d="M149 85h25" tone="violet" width={3} />
        <Label x={280} y={85} width={184} text={l[0]} tone="gold" />
      </g>
      <Label x={282} y={254} width={219} text={l[1]} tone="violet" />
      <PlainText x={360} y={42} text="THOUGHT + CONTENT" width={210} size={14} tone="violet" />
    </>
  ),

  'u29-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={4} />
      <Character x={86} y={248} scale={0.78} shirt="gold" hair="short" pose="think" />
      <Label x={151} y={65} width={197} text={l[0]} tone="gold" />
      <g transform="translate(249 143)">
        <circle r="51" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M0-35v70M-35 0h70" className="ill-blue ill-stroke ill-wide" />
        <PlainText x={0} y={10} text="?" width={30} size={29} tone="blue" />
      </g>
      <Arrow d="M301 126c56-45 103-45 154-5" tone="green" />
      <Arrow d="M301 160c61 49 108 50 158 9" tone="coral" />
      <g transform="translate(503 84)"><circle r="34" className="ill-green ill-pale ill-panel" /><Check x={0} y={0} scale={0.55} /></g>
      <g transform="translate(506 206)"><circle r="34" className="ill-coral ill-pale ill-panel" /><Cross x={0} y={0} scale={0.55} /></g>
      <Label x={422} y={263} width={174} text={l[1]} tone="blue" />
      <PlainText x={320} y={42} text="OPEN QUESTION → YES / NO" width={270} size={14} tone="blue" />
    </>
  ),

  'u29-l3': (l) => (
    <>
      <Backdrop tone="teal" variant={1} />
      <g transform="translate(58 56)">
        <path d="M0 0h524v185H0z" className="ill-teal ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M28 27h468v131H28z" className="ill-paper ill-panel" />
        <path d="M55 53h128v79H55z" className="ill-blue ill-pale ill-panel" />
        <PlainText x={119} y={99} text="It is true" width={102} size={18} tone="blue" />
        <path d="M217 45h251v96H217z" className="ill-gold ill-pale ill-panel ill-dashed" />
        <path d="M244 66h198M244 88h157M244 110h180" className="ill-muted-stroke ill-fine" />
        <Label x={342} y={94} width={205} text={l[0]} tone="gold" />
        <Arrow d="M186 92h28" tone="teal" width={3} />
      </g>
      <Label x={320} y={264} width={248} text={l[1]} tone="teal" />
      <PlainText x={320} y={37} text="PLACEHOLDER IT + REAL CONTENT" width={300} size={14} tone="teal" />
    </>
  ),

  'u30-l1': (l) => (
    <>
      <Backdrop tone="gold" variant={3} />
      <g transform="translate(51 60)">
        <rect width="539" height="176" rx="22" className="ill-ink-fill" opacity=".94" filter="url(#ill-shadow)" />
        <path d="M131 11L42 159h178z" className="ill-coral ill-wash" />
        <path d="M409 10L317 159h184z" className="ill-gold ill-wash" />
        <Character x={131} y={165} scale={0.62} shirt="blue" hair="short" pose="point" />
        <path d="M231 87h75v76h-75z" className="ill-paper ill-panel" />
        <path d="M268 87l-9 25 13 19-11 19 7 13" className="ill-coral ill-stroke ill-wide" />
        <Character x={409} y={165} scale={0.67} shirt="coral" hair="short" pose="point" />
      </g>
      <Label x={144} y={260} width={185} text={l[0]} tone="blue" />
      <Label x={320} y={87} width={162} text={l[1]} tone="gold" />
      <Arrow d="M249 254h90" tone="gold" />
      <Label x={479} y={260} width={230} text={l[2]} tone="coral" />
      <PlainText x={320} y={37} text="MOVE THE SPOTLIGHT" width={210} size={14} tone="gold" />
    </>
  ),

  'u30-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={5} />
      <g transform="translate(75 51)">
        <path d="M0 0h490v202H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <g transform="translate(29 27)">
          <rect width="432" height="57" rx="14" className="ill-blue ill-pale ill-panel" />
          <path d="M25 28h381" className="ill-muted-stroke ill-fine" />
          <Label x={216} y={28} width={389} text={l[0]} tone="blue" height={40} />
        </g>
        <path d="M76 108c-50 0-50 54 0 54h338c50 0 50-54 0-54" className="ill-violet ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
        <g transform="translate(29 120)">
          <rect width="432" height="57" rx="14" className="ill-violet ill-pale ill-panel" />
          <Label x={216} y={28} width={389} text={l[1]} tone="violet" height={40} />
        </g>
      </g>
      <PlainText x={320} y={40} text="FRONT THE NEGATIVE → INVERT" width={290} size={14} tone="violet" />
      <g transform="translate(45 154)"><path d="M0-17l17 17L0 17" className="ill-coral ill-stroke ill-wide" /></g>
    </>
  ),

  'u30-l3': (l) => (
    <>
      <Backdrop tone="blue" variant={2} />
      <g transform="translate(58 55)">
        <rect width="524" height="186" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M25 25h474v63H25z" className="ill-blue ill-pale ill-panel" />
        <Cloud x={83} y={56} scale={0.38} raining />
        <path d="M137 45h329M137 67h268" className="ill-muted-stroke ill-fine" />
        <Label x={262} y={106} width={475} text={l[0]} tone="blue" height={34} />
        <Arrow d="M262 121v24" tone="coral" width={3} />
        <path d="M105 143h314v34H105z" className="ill-coral ill-pale ill-panel" />
        <Cloud x={150} y={160} scale={0.25} raining />
        <Label x={291} y={160} width={223} text={l[1]} tone="coral" height={29} />
        <path d="M432 143h67v34h-67z" className="ill-gold ill-pale ill-panel ill-dashed" />
        <PlainText x={465} y={165} text="same idea" width={56} size={10} tone="gold" />
      </g>
      <PlainText x={320} y={36} text="SAY IT ONCE" width={130} size={14} tone="blue" />
    </>
  ),

  'u31-l1': (l) => (
    <>
      <Backdrop tone="teal" variant={4} />
      <Character x={77} y={245} scale={0.73} shirt="teal" hair="cap" pose="think" />
      <g transform="translate(118 93)"><circle r="29" className="ill-paper ill-panel" /><circle r="15" className="ill-blue ill-pale ill-panel" /><path d="M21 21l29 29" className="ill-ink-stroke ill-wide" /></g>
      <path d="M189 202h398" className="ill-ink-stroke ill-wide" markerEnd="url(#ill-arrow)" />
      {[247, 385, 526].map((x, i) => <g key={x}><path d={`M${x} 185v34`} className="ill-ink-stroke ill-fine" /><g transform={`translate(${x} ${107 - i * 18})`}><rect x="-55" y="-39" width="110" height="78" rx="12" className={`ill-${i === 0 ? 'coral' : i === 1 ? 'green' : 'violet'} ill-pale ill-panel`} filter="url(#ill-shadow)" />{i === 0 ? <Calendar x={0} y={0} width={72} height={59} day="PAST" tone="coral" /> : i === 1 ? <Check x={0} y={0} scale={0.52} /> : <Clock x={0} y={0} r={25} time="eight" tone="violet" />}</g></g>)}
      <Label x={247} y={251} width={137} text={l[0]} tone="coral" />
      <Label x={385} y={251} width={147} text={l[1]} tone="green" />
      <Label x={526} y={251} width={147} text={l[2]} tone="violet" />
      <PlainText x={377} y={38} text="CHOOSE BY TIME RELATION" width={280} size={14} tone="teal" />
    </>
  ),

  'u31-l2': (l) => (
    <>
      <Backdrop tone="gold" variant={1} />
      <Divider label="vs" />
      <g transform="translate(46 62)">
        <rect width="239" height="173" rx="22" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M73 31h93l-13 33q-8 22-33 25 25 3 33 25l13 33H73l13-33q8-22 33-25-25-3-33-25z" className="ill-paper ill-panel" />
        <path d="M88 133h63M92 52h55" className="ill-gold ill-stroke ill-wide" />
        <Clock x={188} y={51} r={22} time="three" tone="coral" />
        <Label x={119} y={198} width={222} text={l[0]} tone="coral" />
      </g>
      <g transform="translate(356 62)">
        <rect width="239" height="173" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={66} y={163} scale={0.52} shirt="teal" hair="bob" pose="think" />
        <path d="M115 39h89v124h-89z" className="ill-paper ill-panel" />
        <Clock x={159} y={80} r={28} time="six" tone="blue" />
        <path d="M128 125h62" className="ill-blue ill-stroke ill-wide ill-dashed" />
        <Label x={119} y={198} width={222} text={l[1]} tone="blue" />
      </g>
      <PlainText x={160} y={41} text="deadline point" width={120} size={13} tone="coral" />
      <PlainText x={479} y={41} text="continuing span" width={120} size={13} tone="blue" />
    </>
  ),

  'u31-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={0} />
      <g transform="translate(48 61)">
        <rect width="239" height="175" rx="22" className="ill-coral ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M78 24h82v113H78z" className="ill-paper ill-panel" />
        <path d="M119 113V50M105 65l14-16 14 16" className="ill-coral ill-stroke ill-symbol" />
        <circle cx="119" cy="113" r="19" className="ill-coral ill-solid" />
        <path d="M37 147h164" className="ill-muted-stroke ill-fine" />
        <Label x={119} y={201} width={222} text={l[0]} tone="coral" />
      </g>
      <g transform="translate(353 61)">
        <rect width="239" height="175" rx="22" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M43 50h152v93H43z" className="ill-paper ill-panel" />
        <path d="M43 50l76 47 76-47M119 97v46" className="ill-gold ill-stroke ill-fine" />
        <path d="M68 27h102" className="ill-muted-stroke ill-fine" />
        <Label x={119} y={201} width={222} text={l[1]} tone="gold" />
      </g>
      <PlainText x={320} y={39} text="ADJECTIVE  /  NOUN PHRASE" width={300} size={14} tone="coral" />
    </>
  ),

  'u32-l1': (l) => (
    <>
      <Backdrop tone="blue" variant={3} />
      <path d="M48 222h545" className="ill-muted-stroke ill-floor" />
      <g transform="translate(86 187)">
        <path d="M0 35V-82M-21-82h42" className="ill-coral ill-stroke ill-symbol" />
        <Clock x={0} y={-40} r={27} time="three" tone="coral" />
      </g>
      <Label x={86} y={254} width={109} text={l[0]} tone="coral" />
      <Arrow d="M132 182h104" tone="blue" dashed width={5} />
      <g transform="translate(258 82)">
        <path d="M0 133h133V0H0z" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M24 27h86M24 49h86M24 71h56" className="ill-muted-stroke ill-fine" />
        <Character x={67} y={126} scale={0.43} shirt="blue" hair="short" pose="point" />
        <path d="M102 84h25" className="ill-blue ill-stroke ill-wide" />
      </g>
      <Arrow d="M405 182h81" tone="green" dashed width={5} />
      <g transform="translate(505 83)">
        <path d="M0 132h90V0H0z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Check x={45} y={61} scale={0.72} />
        <Sparkles x={72} y={23} tone="gold" />
      </g>
      <Label x={513} y={254} width={203} text={l[1]} tone="green" />
      <PlainText x={320} y={41} text="IN PROGRESS  →  COMPLETE BY THEN" width={340} size={14} tone="blue" />
    </>
  ),

  'u32-l2': (l) => (
    <>
      <Backdrop tone="violet" variant={2} />
      <g transform="translate(79 74)">
        <path d="M0 143h482" className="ill-muted-stroke ill-floor" />
        <path d="M42 143V24M21 24h42" className="ill-violet ill-stroke ill-symbol" />
        <Calendar x={42} y={72} width={72} height={62} day="THEN" tone="violet" />
        <Character x={103} y={140} scale={0.53} shirt="coral" hair="bob" pose="point" />
        <Arrow d="M126 80c103-76 207-71 309-9" tone="violet" dashed width={5} />
        <g transform="translate(397 70) rotate(-8)">
          <path d="M-59 24L58-17M-5-23l13-35 19-6-4 38M-17 31l-33 34-22 5 28-48" className="ill-blue ill-stroke ill-symbol" />
          <path d="M-5 14l-47-6-14 11 44 14" className="ill-blue ill-pale ill-panel" />
        </g>
      </g>
      <Label x={151} y={254} width={220} text={l[0]} tone="violet" />
      <Label x={466} y={254} width={216} text={l[1]} tone="blue" />
      <PlainText x={320} y={42} text="FUTURE SEEN FROM THE PAST" width={300} size={14} tone="violet" />
    </>
  ),

  'u32-l3': (l) => (
    <>
      <Backdrop tone="coral" variant={5} />
      <g transform="translate(71 52)">
        <path d="M0 0h498v203H0z" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <g transform="translate(34 27)">
          <rect width="430" height="58" rx="14" className="ill-blue ill-pale ill-panel" />
          <Label x={215} y={29} width={395} text={l[0]} tone="blue" height={40} />
        </g>
        <path d="M72 104c-49 0-49 55 0 55h354c49 0 49-55 0-55" className="ill-coral ill-stroke ill-arrow" markerEnd="url(#ill-arrow)" />
        <g transform="translate(34 127)">
          <rect width="430" height="58" rx="14" className="ill-coral ill-pale ill-panel" />
          <Label x={215} y={29} width={395} text={l[1]} tone="coral" height={40} />
        </g>
      </g>
      <g transform="translate(43 154)"><path d="M0-18l18 18L0 18" className="ill-gold ill-stroke ill-wide" /></g>
      <PlainText x={320} y={39} text="DROP IF · MOVE HAD" width={210} size={14} tone="coral" />
    </>
  ),

  'u32-l4': (l) => (
    <>
      <Backdrop tone="green" variant={0} />
      <g transform="translate(53 57)">
        <path d="M0 183h534" className="ill-muted-stroke ill-floor" />
        <path d="M18 143h130v40H18zM148 100h151v83H148zM299 52h216v131H299z" className="ill-green ill-pale ill-panel" filter="url(#ill-shadow)" />
        <Character x={83} y={138} scale={0.5} shirt="blue" hair="short" pose="walk" />
        <Character x={222} y={95} scale={0.53} shirt="gold" hair="short" pose="walk" />
        <Character x={406} y={47} scale={0.56} shirt="coral" hair="short" pose="celebrate" />
        <Arrow d="M108 118c27-26 50-33 75-28" tone="green" />
        <Arrow d="M262 72c31-26 60-35 92-29" tone="green" />
      </g>
      <Label x={133} y={263} width={191} text={l[0]} tone="blue" />
      <Label x={337} y={263} width={172} text={l[1]} tone="green" />
      <Label x={518} y={263} width={145} text={l[2]} tone="coral" />
      <PlainText x={320} y={35} text="MORE INPUT  ↗  MORE RESULT" width={290} size={14} tone="green" />
      <Sparkles x={520} y={52} tone="gold" />
    </>
  ),

  'u33-l1': (l) => (
    <>
      <Backdrop tone="gold" variant={4} />
      <g transform="translate(49 57)">
        <rect width="542" height="180" rx="22" className="ill-ink-fill" opacity=".93" filter="url(#ill-shadow)" />
        <g transform="translate(32 25)">
          <path d="M0 0h211v130H0z" className="ill-paper ill-panel" />
          {[48, 105, 162].map((x, i) => <circle key={x} cx={x} cy="58" r="24" className={`ill-${i === 0 ? 'blue' : i === 1 ? 'coral' : 'gold'} ill-pale ill-panel`} />)}
          <circle cx="105" cy="58" r="37" className="ill-gold ill-stroke ill-spotlight" />
          <PlainText x={105} y={111} text="FIRST VIEW" width={100} size={12} tone="muted" />
        </g>
        <g transform="translate(299 25)">
          <path d="M0 0h211v130H0z" className="ill-teal ill-pale ill-panel" />
          <circle cx="105" cy="58" r="30" className="ill-coral ill-pale ill-panel" />
          <path d="M105 12L55 109h100z" className="ill-gold ill-wash" />
          <Check x={153} y={35} scale={0.42} />
          <PlainText x={105} y={111} text="KNOWN NOW" width={100} size={12} tone="teal" />
        </g>
      </g>
      <Label x={154} y={262} width={230} text={l[0]} tone="gold" />
      <Arrow d="M273 257h87" tone="gold" />
      <Label x={483} y={262} width={214} text={l[1]} tone="teal" />
      <PlainText x={320} y={38} text="INTRODUCE  →  IDENTIFY" width={240} size={14} tone="gold" />
    </>
  ),

  'u33-l2': (l) => (
    <>
      <Backdrop tone="blue" variant={1} />
      <g transform="translate(47 64)">
        <rect width="245" height="171" rx="22" className="ill-gold ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M31 137h183M50 137L73 38h101l21 99" className="ill-gold ill-stroke ill-wide" />
        {[88, 126, 164].map((x, i) => <Book key={x} x={x} y={94 - i * 7} scale={0.36} color={i % 2 ? 'coral' : 'blue'} />)}
        <Label x={122} y={195} width={222} text={l[0]} tone="gold" />
      </g>
      <g transform="translate(349 64)">
        <rect width="245" height="171" rx="22" className="ill-blue ill-pale ill-panel" filter="url(#ill-shadow)" />
        <path d="M74 34h97l-14 103H88z" className="ill-paper ill-panel" />
        <path d="M88 100h69l-5 37H93z" className="ill-blue ill-solid ill-water" />
        <path d="M106 73c-12-18 14-23 3-40M137 73c-12-18 14-23 3-40" className="ill-blue ill-stroke ill-fine" />
        <Label x={122} y={195} width={222} text={l[1]} tone="blue" />
      </g>
      <PlainText x={320} y={39} text="COUNTABLE  /  UNCOUNTABLE" width={290} size={14} tone="blue" />
      <PlainText x={171} y={105} text="+" width={25} size={28} tone="green" />
      <PlainText x={474} y={105} text="+" width={25} size={28} tone="green" />
    </>
  ),

  'u33-l3': (l) => (
    <>
      <Backdrop tone="teal" variant={5} />
      <g transform="translate(54 60)">
        <rect width="532" height="176" rx="22" className="ill-paper ill-panel" filter="url(#ill-shadow)" />
        <path d="M55 119h181" className="ill-teal ill-stroke ill-symbol" />
        <path d="M78 119V48M129 119V48M181 119V48" className="ill-muted-stroke ill-fine" />
        <circle cx="129" cy="68" r="15" className="ill-coral ill-solid" />
        <path d="M129 54V22" className="ill-coral ill-stroke ill-wide" />
        <path d="M246 88h40" className="ill-gold ill-stroke ill-symbol" markerEnd="url(#ill-arrow)" />
        <g transform="translate(323 42)">
          <path d="M0 0h165v94H0z" className="ill-gold ill-pale ill-panel" />
          <path d="M45 22h75v50H45z" className="ill-paper ill-panel" />
          <path d="M82 22v50M45 47h75" className="ill-gold ill-stroke ill-fine" />
          <path d="M129 47h28" className="ill-coral ill-stroke ill-wide" />
        </g>
        <path d="M374 150h92" className="ill-muted-stroke ill-fine" />
      </g>
      <Label x={151} y={263} width={181} text={l[0]} tone="teal" />
      <Label x={463} y={263} width={181} text={l[1]} tone="gold" />
      <PlainText x={320} y={39} text="VERB · PRONOUN · PARTICLE" width={280} size={14} tone="teal" />
      <Sparkles x={548} y={80} tone="gold" />
    </>
  ),
} satisfies IllustrationSceneMap
