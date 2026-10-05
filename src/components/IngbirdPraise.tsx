import { useEffect, useRef, useState } from 'react'
import { Ingbird } from './Ingbird'
import './Ingbird.css'
import { STUDY_RECORDED_EVENT, type StudyRecord } from '../services/studyDays'

/** 表示しておく時間。閉じるボタンでも消せる。 */
const SHOW_MS = 9_000

/** 紙吹雪の位置・色・大きさ。ランダムにすると毎回ちらつくので固定の並びにする。 */
const CONFETTI = [
  { left: '5%', delay: '0s', color: '#177c78', width: 7, height: 11 },
  { left: '14%', delay: '0.35s', color: '#d9a441', width: 8, height: 8 },
  { left: '23%', delay: '0.12s', color: '#e08a76', width: 6, height: 12 },
  { left: '32%', delay: '0.5s', color: '#216b8f', width: 8, height: 8 },
  { left: '41%', delay: '0.22s', color: '#2f8f83', width: 7, height: 11 },
  { left: '50%', delay: '0.62s', color: '#d9a441', width: 6, height: 10 },
  { left: '59%', delay: '0.08s', color: '#177c78', width: 8, height: 8 },
  { left: '68%', delay: '0.45s', color: '#e08a76', width: 7, height: 12 },
  { left: '77%', delay: '0.28s', color: '#216b8f', width: 6, height: 10 },
  { left: '86%', delay: '0.56s', color: '#2f8f83', width: 8, height: 8 },
  { left: '94%', delay: '0.18s', color: '#d9a441', width: 7, height: 11 },
]

/**
 * 学習日が新しく記録された瞬間に、どのページでもイングバードがほめに来る。
 * 記録イベントの購読はレイアウトに1つだけ置き、同じ日に何度も出さない。
 */
export function IngbirdPraise() {
  const [record, setRecord] = useState<StudyRecord | null>(null)
  const [shownCount, setShownCount] = useState(0)
  const shownDate = useRef<string | null>(null)

  useEffect(() => {
    const onStudy = (event: Event) => {
      const detail = (event as CustomEvent<StudyRecord>).detail
      if (!detail || shownDate.current === detail.date) return // 保存できない環境でも1日1回に抑える
      shownDate.current = detail.date
      setRecord(detail)
      setShownCount((count) => count + 1)
    }
    window.addEventListener(STUDY_RECORDED_EVENT, onStudy)
    return () => window.removeEventListener(STUDY_RECORDED_EVENT, onStudy)
  }, [])

  useEffect(() => {
    if (!record) return
    const timer = window.setTimeout(() => setRecord(null), SHOW_MS)
    return () => window.clearTimeout(timer)
  }, [record])

  if (!record) return null
  const { praise, status } = record

  return (
    <div className="ingbird-toast" key={shownCount} role="status">
      {praise.confetti && (
        <div className="ingbird-confetti" aria-hidden="true">
          {CONFETTI.map((piece, index) => (
            <span
              key={index}
              style={{
                left: piece.left,
                width: piece.width,
                height: piece.height,
                background: piece.color,
                animationDelay: piece.delay,
              }}
            />
          ))}
        </div>
      )}
      <Ingbird mood={praise.mood} size={86} decorative className="ingbird-toast-bird" />
      <div className="ingbird-toast-body">
        <p className="ingbird-toast-title">{praise.title}</p>
        <p className="ingbird-toast-message">{praise.message}</p>
        <p className="ingbird-toast-total">
          学習日 <strong>{status.totalDays}</strong>日（トータル）
        </p>
      </div>
      <button
        type="button"
        className="ingbird-toast-close"
        aria-label="メッセージを閉じる"
        onClick={() => setRecord(null)}
      >
        ×
      </button>
    </div>
  )
}
