import type { LessonAnimation } from '../../content/grammar/animations'

const positions = [112, 320, 528]

function Label({ x, y, text }: { x: number; y: number; text: string }) {
  return <text x={x} y={y} className="ga-label">{text}</text>
}

// Keep recurring words mounted between frames so changes of order are visible.
function wordKey(word: string) { return word.toLowerCase().replace(/[.,?!“”]/g, '') }
function textWidth(word: string) {
  return Array.from(word).reduce((sum, char) => sum + (char.codePointAt(0)! > 127 ? 20 : 10), 0)
}
function Sentence({ animation, step }: { animation: LessonAnimation; step: number }) {
  const words = animation.steps[step].sentence.split('|')
  const naturalWidths = words.map((word) => Math.max(70, textWidth(word) + 30))
  const split = naturalWidths.reduce((sum, width) => sum + width + 12, 0) > 560 ? Math.ceil(words.length / 2) : words.length
  const layout = words.map((_, index) => {
    const start = index < split ? 0 : split
    const end = index < split ? split : words.length
    const rowWidths = naturalWidths.slice(start, end)
    const scale = Math.min(1, (572 - (rowWidths.length - 1) * 12) / rowWidths.reduce((sum, width) => sum + width, 0))
    const widths = rowWidths.map((width) => width * scale)
    const fullWidth = widths.reduce((sum, width) => sum + width, 0) + (widths.length - 1) * 12
    return {
      x: (640 - fullWidth) / 2 + widths.slice(0, index - start).reduce((sum, width) => sum + width + 12, 0),
      y: split === words.length ? 82 : index < split ? 26 : 142,
      width: widths[index - start],
    }
  })
  const allWords = [...new Set(animation.steps.flatMap((frame) => frame.sentence.split('|').map(wordKey)))]
  return (
    <g>
      <path d={split === words.length ? 'M40 120H600' : 'M40 64H600M40 180H600'} className="ga-track" />
      {allWords.map((key) => {
        const index = words.findIndex((word) => wordKey(word) === key)
        const present = index !== -1
        const { x, y, width } = present ? layout[index] : { x: 270, y: -40, width: 100 }
        const text = present ? words[index] : key
        return (
          <g key={key} className="ga-word" style={{ transform: `translate(${x}px, ${y}px)`, opacity: present ? 1 : 0 }} aria-hidden={!present}>
            <rect width={width} height="76" rx="14" className={`ga-token ga-tone-${allWords.indexOf(key) % 3}`} />
            <text x={width / 2} y="44" className="ga-word-text" style={{ fontSize: Math.min(23, (width - 16) / Math.max(textWidth(text), 1) * 20) }}>{text}</text>
            <text x={width / 2} y="98" className="ga-order">{present ? String(index + 1).padStart(2, '0') : ''}</text>
          </g>
        )
      })}
    </g>
  )
}

function Timeline({ animation, step, sceneId }: { animation: LessonAnimation; step: number; sceneId: string }) {
  const flashbacks: Record<string, { axis: string[]; cursors: number[] }> = {
    'u18-l2': { axis: ['朝食', '出発', '今'], cursors: [0, 1, 0] },
    'u18-l3': { axis: ['傘をなくす', '雨の中で帰宅', '今'], cursors: [1, 1, 0] },
    'u31-l1': { axis: ['さらに前', '過去', '今'], cursors: [1, 2, 0] },
  }
  const cursor = flashbacks[sceneId]?.cursors[step] ?? step
  const axis = flashbacks[sceneId]?.axis ?? animation.axis
  return <g>
    <path d="M76 130H564" className="ga-track" />
    <path d="m552 122 12 8-12 8" className="ga-track" />
    <path d={`M112 130H${positions[cursor]}`} className="ga-trail" />
    {positions.map((x, i) => <g key={i}>
      <path d={`M${x} 118v24`} className="ga-tick" />
      <circle cx={x} cy="130" r="6" className={i <= cursor ? 'ga-dot-active' : 'ga-dot'} />
      <Label x={x} y={192} text={axis?.[i] ?? ''} />
    </g>)}
    <g className="ga-moving" style={{ transform: `translate(${positions[cursor]}px, 130px)` }}>
      <circle r="24" className="ga-halo" /><circle r="12" className="ga-dot-active" />
      <path d="M0-35v-22" className="ga-tick" />
      <rect x="-42" y="-86" width="84" height="30" rx="15" className="ga-dark" />
      <text x="0" y="-65" className="ga-white-text">注目</text>
    </g>
  </g>
}

function Selection({ step, sceneId }: { step: number; sceneId: string }) {
  const pair = sceneId === 'u16-l3'
  const count = pair ? 2 : 5
  const all = (sceneId === 'u14-l4' || sceneId === 'u33-l1') && step === 2
  const reference = sceneId === 'u04-l3'
  const selected = (i: number) => pair ? step === 0 || (step === 1 && i === 0) : all || (reference ? i === (step === 0 ? 0 : 2) : step > 0 && i === 2)
  return <g>
    <rect x="54" y="45" width="532" height="157" rx="24" className="ga-panel" />
    {Array.from({ length: count }, (_, i) => {
      const x = pair ? 232 + i * 176 : 112 + i * 104
      const active = selected(i)
      return <g key={i} className="ga-moving" style={{ transform: `translate(${x}px, ${active ? 114 : 127}px)` }}>
        <circle r="39" className={`ga-choice ${active ? 'ga-choice-active' : ''}`} />
        <circle r="15" className={reference && i === 2 ? 'ga-reference-object' : 'ga-object-dot'} />
        {pair && <text x="0" y="66" className="ga-label">{i === 0 ? 'A' : 'B'}</text>}
        <circle cy="-46" r="12" className="ga-dot-active" style={{ opacity: active ? 1 : 0 }} />
        <path d="m-5-46 3 4 7-8" className="ga-check" style={{ opacity: active ? 1 : 0 }} />
      </g>
    })}
    <Label x={320} y={235} text={pair ? ['両方を選ぶ', 'どちらかを選ぶ', 'どちらも選ばない'][step] : reference ? ['最初に指したもの', '同じ種類の別のもの', 'まさにそのもの'][step] : all ? 'グループ全体' : step === 0 ? 'まだ対象を特定していない' : '話題の対象を選ぶ'} />
  </g>
}

function Quantity({ step, sceneId }: { step: number; sceneId: string }) {
  const few = sceneId === 'u33-l2'
  return <g>
    <rect x="54" y="38" width="250" height="167" rx="20" className="ga-panel" />
    <rect x="336" y="38" width="250" height="167" rx="20" className="ga-panel" />
    {[0, 1, 2].map((i) => <g key={i} className="ga-moving" style={{ transform: `translate(${104 + i * 74}px, ${few || step > 0 || i === 0 ? 120 : 88}px)`, opacity: few || step > 0 || i === 0 ? 1 : 0.12 }}>
      {sceneId === 'u03-l1' ? <><circle r="25" className="ga-apple" /><path d="M0-23q-4-17 12-18" className="ga-object" /></> : <rect x="-23" y="-30" width="46" height="60" rx="5" className="ga-tone-1" />}
      <text x="0" y="9" className="ga-word-text">{i + 1}</text>
    </g>)}
    <path d="M411 70l8 109h84l8-109" className="ga-glass" />
    <path d="M423 169h76l4-62q-20-10-40 0t-44 0Z" className="ga-water ga-moving" style={{ opacity: step === 2 ? 1 : 0.15, transform: `translateY(${step === 2 ? 0 : 10}px)` }} />
    <Label x={179} y={235} text={few ? step === 0 ? 'ほとんどない' : '少しある' : '1つずつ数える'} /><Label x={461} y={235} text="量で捉える" />
  </g>
}

function Comparison({ animation, step, sceneId }: { animation: LessonAnimation; step: number; sceneId: string }) {
  const podium = sceneId === 'u07-l2'
  const equal = sceneId === 'u07-l3'
  const correlated = sceneId === 'u32-l4'
  const xs = podium ? positions : [216, 424]
  const heights = podium ? [65, 106, 147] : equal ? [110, 110] : correlated ? [55 + step * 38, 55 + step * 38] : [72, 138]
  return <g>
    <path d="M80 190H560" className="ga-track" />
    <path d={`M120 ${190 - Math.max(...heights)}H548`} className="ga-guide" />
    {xs.map((x, i) => <g key={i}>
      <rect x={x - 44} y={190 - heights[i]} width="88" height={heights[i]} rx="12" className={`ga-bar ga-tone-${i}`}
        style={{ opacity: step >= i || correlated ? 1 : 0.2 }} />
      <Label x={x} y={227} text={animation.axis?.[i] ?? ''} />
    </g>)}
    {equal && <text x="320" y="127" className="ga-equals" style={{ opacity: step === 2 ? 1 : 0 }}>＝</text>}
    {podium && <text x="528" y="32" className="ga-star" style={{ opacity: step === 2 ? 1 : 0 }}>★</text>}
  </g>
}

function Space({ animation, step, sceneId }: { animation: LessonAnimation; step: number; sceneId: string }) {
  const distance = sceneId === 'u04-l2'
  const travel = sceneId === 'u08-l3'
  const x = distance ? step === 0 ? 130 : 500 : positions[step]
  const y = distance || travel ? 113 : step === 0 ? 138 : step === 1 ? 107 : 135
  return <g>
    {distance ? <>
      <path d="M130 148H550" className="ga-guide" />
      <circle cx="65" cy="87" r="15" className="ga-object-dot" />
      <path d="M42 149v-25q23-28 46 0v25M90 116l24-8" className="ga-object" />
    </> : travel ? <>
      <path d="M84 148H557" className="ga-track" />
      <path d="M76 147v-46l26-22 26 22v46M90 147v-28h23v28" className="ga-object" />
      <rect x="274" y="65" width="92" height="96" rx="20" className="ga-zone" />
      <path d="M510 147V80h42v24h-42" className="ga-object" />
    </> : <>
      <circle cx="112" cy="138" r="32" className="ga-guide-circle" />
      <path d="M265 122h110M277 122v53m86-53v53" className="ga-object" />
      <rect x="476" y="84" width="104" height="98" rx="12" className="ga-zone" />
    </>}
    <g className="ga-moving" style={{ transform: `translate(${x}px, ${y}px)` }}>
      <circle r="24" className="ga-halo" /><circle r="13" className="ga-dot-active" />
      {distance && <circle cx="38" r="13" className="ga-dot-active" style={{ opacity: step === 2 ? 1 : 0 }} />}
    </g>
    {distance ? <><Label x={130} y={220} text="近い" /><Label x={500} y={220} text={step === 2 ? '遠い・複数' : '遠い'} /></> : positions.map((position, i) => <Label key={i} x={position} y={220} text={animation.axis?.[i] ?? ''} />)}
  </g>
}

function Scale({ animation, step }: { animation: LessonAnimation; step: number }) {
  return <g>
    {[0, 1, 2].map((i) => <g key={i}>
      <rect x={68 + i * 168} y="112" width="168" height="30" rx="4" className={`ga-token ga-tone-${i}`} />
      <Label x={152 + i * 168} y={204} text={animation.axis?.[i] ?? ''} />
    </g>)}
    <g className="ga-moving" style={{ transform: `translate(${152 + step * 168}px, 80px)` }}>
      <path d="m-12-8 12 17L12-8Z" className="ga-dark" />
      <circle cy="47" r="12" className="ga-dark" />
    </g>
  </g>
}

function Branch({ animation, step }: { animation: LessonAnimation; step: number }) {
  return <g>
    <path d="M120 125H244Q270 125 294 60H400M244 125Q270 125 294 185H400" className="ga-track" />
    <path d={step === 0 ? 'M120 125H244' : step === 1 ? 'M120 125H244Q270 125 294 60H400' : 'M120 125H244Q270 125 294 185H400'} className="ga-branch-path" />
    <circle cx="120" cy="125" r="29" className={step === 0 ? 'ga-dot-active' : 'ga-dot'} />
    <circle r="9" className="ga-dot-active ga-moving" style={{ transform: `translate(${step === 0 ? 120 : 340}px, ${step === 0 ? 125 : step === 1 ? 60 : 185}px)` }} />
    {[60, 185].map((y, i) => <g key={i}>
      <rect x="380" y={y - 28} width="218" height="56" rx="16" className={`ga-choice ${step === i + 1 ? 'ga-choice-active' : ''}`} />
      <Label x={489} y={y + 7} text={animation.axis?.[i + 1] ?? ''} />
    </g>)}
    <Label x={120} y={188} text={animation.axis?.[0] ?? ''} />
  </g>
}

export function GrammarAnimationScene({ animation, step, sceneId }: { animation: LessonAnimation; step: number; sceneId: string }) {
  switch (animation.mode) {
    case 'sentence': return <Sentence animation={animation} step={step} />
    case 'timeline': return <Timeline animation={animation} step={step} sceneId={sceneId} />
    case 'select': return <Selection step={step} sceneId={sceneId} />
    case 'quantity': return <Quantity step={step} sceneId={sceneId} />
    case 'compare': return <Comparison animation={animation} step={step} sceneId={sceneId} />
    case 'space': return <Space animation={animation} step={step} sceneId={sceneId} />
    case 'scale': return <Scale animation={animation} step={step} />
    case 'branch': return <Branch animation={animation} step={step} />
  }
}
