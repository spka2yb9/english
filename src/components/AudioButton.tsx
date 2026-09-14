import { useEffect, useRef, useState } from 'react'
import { speechService, NORMAL_RATE, SLOW_RATE } from '../services/speech'

type Props = {
  /** TTSに渡すクリーンな英文 */
  text: string
  /** スロー再生ボタンとして表示 */
  slow?: boolean
  className?: string
}

const supported = speechService.isSupported()

/** 英文の音声再生ボタン。既存の再生は自動的に停止・置き換えられる。 */
export function AudioButton({ text, slow = false, className }: Props) {
  const [playing, setPlaying] = useState(false)
  const mounted = useRef(true)
  const active = useRef(false)

  useEffect(() => {
    mounted.current = true
    return () => {
      mounted.current = false
      if (active.current) speechService.stop()
    }
  }, [])

  const play = async () => {
    if (playing) {
      speechService.stop()
      active.current = false
      setPlaying(false)
      return
    }
    setPlaying(true)
    active.current = true
    try {
      await speechService.speak(text, { rate: slow ? SLOW_RATE : NORMAL_RATE })
    } catch {
      // 音声エンジンが実行時に失敗しても教材の閲覧を妨げない。
    } finally {
      active.current = false
      if (mounted.current) setPlaying(false)
    }
  }

  const label = slow ? `ゆっくり再生: ${text}` : `音声を再生: ${text}`

  return (
    <button
      type="button"
      className={`audio-btn${playing ? ' playing' : ''}${slow ? ' slow' : ''}${className ? ` ${className}` : ''}`}
      onClick={play}
      disabled={!supported}
      aria-label={supported ? label : '音声再生はこのブラウザでは利用できません'}
      title={supported ? (slow ? 'ゆっくり再生' : '音声を再生') : '音声再生非対応'}
    >
      {slow ? <TurtleIcon /> : <SpeakerIcon playing={playing} />}
    </button>
  )
}

function SpeakerIcon({ playing }: { playing: boolean }) {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path
        d="M4 9v6h4l5 4V5L8 9H4z"
        fill="currentColor"
      />
      {playing ? (
        <>
          <path d="M16 8.5a5 5 0 0 1 0 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
          <path d="M18.5 6a8.5 8.5 0 0 1 0 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
        </>
      ) : (
        <path d="M16 8.5a5 5 0 0 1 0 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
      )}
    </svg>
  )
}

function TurtleIcon() {
  return (
    <span aria-hidden="true" className="turtle-icon">
      0.5×
    </span>
  )
}
