import { useEffect, useId, useRef, useState } from 'react'
import type { LessonAnimation } from '../content/grammar/animations'
import { GrammarAnimationScene } from './illustrations/GrammarAnimationScene'
import './illustrations/grammar-animation.css'

/**
 * 3段階の2Dアニメーションを再生する共通UI。
 * レッスンの挿絵(Illustration)と、5文型の図解(英文の作られ方ページ)が同じ形式で使う。
 * sceneId はモードごとの固有の演出(タイムラインの軸など)を切り替えるためのキー。
 */
export function GrammarAnimation({ sceneId, animation }: { sceneId: string; animation: LessonAnimation }) {
  const titleId = useId()
  const stageId = useId()
  const root = useRef<HTMLDivElement>(null)
  const [step, setStep] = useState(0)
  const [playing, setPlaying] = useState(false)
  const [visible, setVisible] = useState(false)
  const [pageVisible, setPageVisible] = useState(() => !document.hidden)

  useEffect(() => {
    const media = window.matchMedia?.('(prefers-reduced-motion: reduce)')
    const onMotionChange = () => { if (media?.matches) setPlaying(false) }
    const onVisibilityChange = () => setPageVisible(!document.hidden)
    media?.addEventListener('change', onMotionChange)
    document.addEventListener('visibilitychange', onVisibilityChange)
    const observer = typeof IntersectionObserver === 'undefined' ? null : new IntersectionObserver(
      ([entry]) => setVisible(entry.isIntersecting), { threshold: 0.2 },
    )
    if (observer && root.current) observer.observe(root.current)
    else setVisible(true)
    return () => {
      media?.removeEventListener('change', onMotionChange)
      document.removeEventListener('visibilitychange', onVisibilityChange)
      observer?.disconnect()
    }
  }, [])

  const running = playing && visible && pageVisible
  useEffect(() => {
    if (!running) return
    const timer = window.setTimeout(() => {
      if (step === 2) setPlaying(false)
      else setStep(step + 1)
    }, 4200)
    return () => window.clearTimeout(timer)
  }, [running, step])

  const selectStep = (index: number) => { setPlaying(false); setStep(index) }
  const frame = animation.steps[step]

  return (
    <div ref={root} className="grammar-animation" role="group" aria-labelledby={titleId}
      data-scene={sceneId} data-playing={running}>
      <div className="grammar-animation-heading">
        <span className="grammar-animation-eyebrow"><span aria-hidden="true">◈</span> 動きでわかる英文法</span>
        <span className="grammar-animation-count" aria-label={`全3段階の${step + 1}段階目`}>0{step + 1} / 03</span>
      </div>
      <h3 id={titleId}>{animation.title}</h3>
      <div id={stageId} className="grammar-animation-stage">
        <svg viewBox="0 0 640 250" role="img" focusable="false"
          aria-label={`${animation.title}。${frame.sentence.replaceAll('|', ' ')}。${frame.note}`}>
          <GrammarAnimationScene animation={animation} step={step} sceneId={sceneId} />
        </svg>
        <div className="grammar-animation-explanation" aria-live={playing ? 'off' : 'polite'} aria-atomic="true">
          <p className="grammar-animation-sentence" lang="en">{frame.sentence.replaceAll('|', ' ')}</p>
          <p className="grammar-animation-note">{frame.note}</p>
        </div>
      </div>
      <div className="grammar-animation-controls">
        <button type="button" className="grammar-animation-play" aria-controls={stageId}
          onClick={() => {
            if (!playing && step === 2) setStep(0)
            setPlaying(!playing)
          }}>
          <span aria-hidden="true">{playing ? 'Ⅱ' : '▶'}</span>
          {playing ? '一時停止' : step === 2 ? 'もう一度' : '再生'}
        </button>
        <div className="grammar-animation-steps" aria-label="表示する段階">
          {animation.steps.map((item, index) => (
            <button type="button" key={index} aria-label={`ステップ${index + 1}: ${item.note}`}
              aria-current={step === index ? 'step' : undefined} aria-controls={stageId}
              onClick={() => selectStep(index)}><span>{index + 1}</span></button>
          ))}
        </div>
        <button type="button" className="grammar-animation-next" disabled={step === 2}
          aria-controls={stageId} onClick={() => selectStep(step + 1)}>次へ <span aria-hidden="true">→</span></button>
      </div>
    </div>
  )
}
