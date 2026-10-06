import { useEffect, useRef, useState } from 'react'
import type { GrammarLesson } from '../content/types'
import { createSectionChat, type SectionChat } from '../services/sectionChat'
import type { QaQuote } from '../services/sectionChat'
import { STUDY_RECORDED_EVENT, type StudyRecord } from '../services/studyDays'
import { AudioButton } from './AudioButton'
import { Ingbird } from './Ingbird'
import './IngbirdChat.css'

type Message = {
  id: number
  role: 'user' | 'bird'
  text: string
  quotes?: QaQuote[]
  followups?: string[]
}

/** 「考え中…」を見せる時間。長すぎるとSN感が出るので短く。 */
const THINK_MS = 450

/**
 * 英文法のセクション専用の質問チャット(SP・PC共通)。
 * 右下のボタンから開き、いま開いているセクションについてイングバードに聞ける。
 * 回答はセクションのQAコーパス(sectionChat)から引く。通信はしない。
 */
export function IngbirdChat({
  lesson,
  thinkingMs = THINK_MS,
  rng,
}: {
  lesson: GrammarLesson
  thinkingMs?: number
  /** あいさつなどの言い回しの抽選。テストでは固定値を渡す。 */
  rng?: () => number
}) {
  const chatRef = useRef<SectionChat | null>(null)
  const greeting = `このセクション「${lesson.title}」は、最初から最後までぜんぶ読んであるよ。意味・例文・なぜ・違い・文型・まとめ…なんでも聞いてね!`
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [thinking, setThinking] = useState(false)
  const nextId = useRef(0)
  const logRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const fabRef = useRef<HTMLButtonElement>(null)
  const timerRef = useRef<number | undefined>(undefined)

  const append = (message: Omit<Message, 'id'>) => setMessages((list) => [...list, { ...message, id: nextId.current++ }])

  // 索引の構築は重いので、チャットを開いて初めて答えるときまで遅らせる(読むだけの利用者にコストを払わせない)
  const getChat = () => {
    if (!chatRef.current) chatRef.current = createSectionChat(lesson, rng)
    return chatRef.current
  }

  const send = (raw: string) => {
    const question = raw.trim()
    if (!question || thinking) return
    append({ role: 'user', text: question })
    setInput('')
    setThinking(true)
    window.clearTimeout(timerRef.current)
    timerRef.current = window.setTimeout(() => {
      const reply = getChat().reply(question)
      if (reply.kind === 'answer') {
        append({ role: 'bird', text: reply.lead, quotes: reply.quotes, followups: reply.followups })
      } else {
        append({ role: 'bird', text: reply.message, followups: reply.suggestions })
      }
      setThinking(false)
    }, thinkingMs)
  }

  const openChat = () => {
    setOpen(true)
    if (messages.length === 0) {
      append({ role: 'bird', text: greeting, followups: getChat().suggestions() })
    }
    requestAnimationFrame(() => inputRef.current?.focus())
  }

  const closeChat = () => {
    setOpen(false)
    fabRef.current?.focus()
  }

  // 開いている間は Escape で閉じる。SPでは背後のスクロールも止める(ドロワーと同じ方針)。
  useEffect(() => {
    if (!open) return
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closeChat()
    }
    const lockScroll = window.matchMedia?.('(max-width: 879px)').matches ?? false
    const previousOverflow = document.body.style.overflow
    if (lockScroll) document.body.style.overflow = 'hidden'
    window.addEventListener('keydown', onKey)
    return () => {
      if (lockScroll) document.body.style.overflow = previousOverflow
      window.removeEventListener('keydown', onKey)
    }
  }, [open])

  // チャットを開いている間に学習日が記録されたら、トーストの代わりにここでほめる
  useEffect(() => {
    if (!open) return
    const onStudy = (event: Event) => {
      const detail = (event as CustomEvent<StudyRecord>).detail
      if (!detail) return
      append({ role: 'bird', text: `${detail.praise.title} ${detail.praise.message}` })
    }
    window.addEventListener(STUDY_RECORDED_EVENT, onStudy)
    return () => window.removeEventListener(STUDY_RECORDED_EVENT, onStudy)
  }, [open])

  useEffect(() => () => window.clearTimeout(timerRef.current), [])

  // 新しいメッセージに合わせて一番下へ
  useEffect(() => {
    const log = logRef.current
    if (log) log.scrollTop = log.scrollHeight
  }, [messages, thinking, open])

  const lastFollowups = [...messages].reverse().find((message) => message.role === 'bird')?.followups ?? []

  return (
    <>
      <button
        ref={fabRef}
        type="button"
        className="ingbird-chat-fab"
        aria-haspopup="dialog"
        aria-expanded={open}
        aria-label="イングバードにこのセクションを質問する"
        onClick={open ? closeChat : openChat}
      >
        <Ingbird mood={open ? (thinking ? 'think' : 'happy') : 'idle'} size={44} decorative />
        <span className="ingbird-chat-badge" aria-hidden="true">
          ?
        </span>
      </button>

      {open && (
        <>
          <div className="ingbird-chat-backdrop" onClick={closeChat} aria-hidden="true" />
          <section
            className="ingbird-chat-panel"
            role="dialog"
            aria-modal="true"
            aria-label={`イングバードに「${lesson.title}」を質問する`}
          >
            <header className="ingbird-chat-head">
              <Ingbird mood={thinking ? 'think' : 'happy'} size={40} decorative />
              <div className="ingbird-chat-head-text">
                <p className="ingbird-chat-title">イングバードにきく</p>
                <p className="ingbird-chat-sub">{lesson.title}</p>
              </div>
              <button type="button" className="ingbird-chat-close" onClick={closeChat} aria-label="チャットを閉じる">
                ×
              </button>
            </header>

            <div className="ingbird-chat-log" ref={logRef} role="log" aria-live="polite">
              {messages.map((message) => (
                <div key={message.id} className={`ingbird-chat-row ${message.role}`}>
                  <div className="ingbird-chat-bubble">
                    <p className="ingbird-chat-text">{message.text}</p>
                    {message.quotes?.map((quote, index) => (
                      <Quote key={index} quote={quote} />
                    ))}
                  </div>
                </div>
              ))}
              {thinking && (
                <p className="ingbird-chat-thinking" role="status">
                  <span aria-hidden="true">
                    <i />
                    <i />
                    <i />
                  </span>
                  考え中…
                </p>
              )}
            </div>

            {lastFollowups.length > 0 && !thinking && (
              <div className="ingbird-chat-chips" aria-label="続けて聞けること">
                {lastFollowups.map((followup) => (
                  <button key={followup} type="button" onClick={() => send(followup)}>
                    {followup}
                  </button>
                ))}
              </div>
            )}

            <form
              className="ingbird-chat-form"
              onSubmit={(event) => {
                event.preventDefault()
                send(input)
              }}
            >
              <input
                ref={inputRef}
                value={input}
                onChange={(event) => setInput(event.target.value)}
                placeholder="このセクションについて質問"
                aria-label="質問を入力"
                autoComplete="off"
                enterKeyHint="send"
              />
              <button type="submit" className="ingbird-chat-send" disabled={input.trim().length === 0 || thinking}>
                送る
              </button>
            </form>
          </section>
        </>
      )}
    </>
  )
}

function Quote({ quote }: { quote: QaQuote }) {
  return (
    <figure className="ingbird-chat-quote">
      <figcaption>{quote.label}</figcaption>
      {quote.en && (
        <p className="ingbird-chat-en" lang="en">
          {quote.en} <AudioButton text={quote.en} />
        </p>
      )}
      {quote.ja && <p className="ingbird-chat-ja">{quote.ja}</p>}
      {quote.note && <p className="ingbird-chat-note">{quote.note}</p>}
      {quote.text?.split('\n').map((line, index) => (
        <p key={index} className="ingbird-chat-quote-text">
          {line}
        </p>
      ))}
    </figure>
  )
}
