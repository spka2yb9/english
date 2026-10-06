import { useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { Ingbird } from './Ingbird'
import './Ingbird.css'
import { MILESTONES, getStudyStatus, praiseFor, type IngbirdMood } from '../services/studyDays'
import { speechService } from '../services/speech'
import type { TalkLine } from '../content/ingbird/types'

/** つぶやきのコーパスは大きいので、最初のタップまで読み込まない。 */
type TalkModule = typeof import('../services/ingbirdTalk')

/** カードに添える、そのときの気分の短いラベル。 */
const MOOD_LABELS: Record<IngbirdMood, string> = {
  idle: 'のんびり',
  happy: 'にっこり',
  cheer: 'はりきり',
  party: 'お祝い',
  proud: 'どや顔',
  wave: 'おかえり',
  curious: 'きになる',
  wow: 'びっくり',
  sleepy: 'おやすみ',
  shy: 'てれ',
  think: '考え中',
  sing: 'ごきげん',
}

const KIND_LABELS: Record<TalkLine['kind'], string> = {
  encourage: 'イングバードのひとこと',
  tip: '学習のコツ',
  phrase: '英会話フレーズ',
}

/** つぶやきを読み上げる文とロケール。フレーズ以外は日本語で読む。 */
function speechOf(talk: TalkLine): { text: string; locale: string } {
  return talk.speech ?? { text: talk.text, locale: 'ja-JP' }
}

/**
 * ホームのマスコットカード。数えるのは連続日数ではなく、学習した日の合計(トータル)。
 * 久しぶりの日も、まだ学習していない日も、責めずに「来たこと」からほめる。
 *
 * イングバードをタップすると吹き出しが出て、励まし・学習のコツ・英会話フレーズを
 * 1つずつ話す。話した言葉は、日本語の音声があれば読み上げる。
 */
export function IngbirdCard() {
  // カードのほめ言葉は表示中ずっと同じにする(再描画のたびに抽選し直さない)。
  const [status] = useState(() => getStudyStatus())
  const [praise] = useState(() => praiseFor(status))
  const [talk, setTalk] = useState<TalkLine | null>(null)
  const [talkCount, setTalkCount] = useState(0)
  const [thinking, setThinking] = useState(false)
  const talkModule = useRef<TalkModule | null>(null)
  const talkState = useRef<ReturnType<TalkModule['createTalkState']> | null>(null)
  const loading = useRef(false)

  const { next } = status
  // 直前の節目から次の節目までを1本のバーにする(0日目は0→1日目の区間)
  const previous = MILESTONES.filter((milestone) => milestone <= status.totalDays).at(-1) ?? 0
  const ratio = next ? (status.totalDays - previous) / (next.at - previous) : 1
  const mood = talk?.mood ?? (thinking ? 'think' : praise.mood)

  function speak(line: TalkLine) {
    if (!speechService.isSupported()) return
    const { text, locale } = speechOf(line)
    // 日本語の声が入っていない環境で、無理に日本語を読ませない。
    if (!locale.startsWith('en') && !(speechService.hasVoice?.(locale) ?? false)) return
    void speechService.speak(text, { locale })
  }

  async function handleTalk() {
    if (loading.current) return
    loading.current = true
    setThinking(true)
    try {
      if (!talkModule.current) talkModule.current = await import('../services/ingbirdTalk')
      const module = talkModule.current
      if (!talkState.current) talkState.current = module.createTalkState()
      const line = module.nextTalk(talkState.current, status)
      setTalk(line)
      setTalkCount((count) => count + 1)
      speak(line)
    } catch {
      // コーパスを読み込めない環境では何も話さない(ホームの操作は壊さない)
    } finally {
      loading.current = false
      setThinking(false)
    }
  }

  return (
    <section
      className={`ingbird-card${praise.confetti ? ' is-celebrating' : ''}`}
      aria-label="イングバードからのメッセージ"
    >
      <div className={`ingbird-card-bird ingbird-mood-${mood}${talk ? ' is-talking' : ''}`}>
        <button
          type="button"
          className="ingbird-talk-btn"
          onClick={handleTalk}
          aria-expanded={talk !== null}
          aria-controls="ingbird-talk"
          aria-label="イングバードに話しかける"
        >
          <Ingbird mood={mood} size={132} decorative />
        </button>
        <span className="ingbird-name">イングバード</span>
        <span className="ingbird-mood-label">{MOOD_LABELS[mood]}</span>
        <span className="ingbird-talk-hint">{talk ? 'もう一度タップで次のひとこと' : 'タップでひとこと'}</span>
      </div>

      <div className="ingbird-card-body">
        {/* 読み上げ用の領域は常に置き、中身だけを差し替えて通知されるようにする */}
        <div className="ingbird-bubble-area" id="ingbird-talk" aria-live="polite">
          {talk && (
            <div className="ingbird-bubble" key={talkCount} data-kind={talk.kind}>
              <p className="ingbird-bubble-badge">
                {KIND_LABELS[talk.kind]}
                {talk.scene && <span className="ingbird-bubble-scene">{talk.scene}</span>}
              </p>
              {talk.kind === 'phrase' ? (
                <>
                  <p className="ingbird-bubble-en" lang="en">
                    {talk.text}
                  </p>
                  {talk.ja && <p className="ingbird-bubble-ja">{talk.ja}</p>}
                  {talk.note && <p className="ingbird-bubble-note">{talk.note}</p>}
                </>
              ) : (
                <p className="ingbird-bubble-text">{talk.text}</p>
              )}
              <div className="ingbird-bubble-actions">
                {speechService.isSupported() && (talk.kind === 'phrase' || (speechService.hasVoice?.('ja-JP') ?? false)) && (
                  <button type="button" className="ingbird-bubble-btn" onClick={() => speak(talk)}>
                    {talk.kind === 'phrase' ? '🔊 もう一度聞く' : '🔊 よみあげ'}
                  </button>
                )}
                <button type="button" className="ingbird-bubble-btn" onClick={handleTalk}>
                  別のひとこと
                </button>
                <button
                  type="button"
                  className="ingbird-bubble-btn is-quiet"
                  onClick={() => setTalk(null)}
                  aria-label="吹き出しを閉じる"
                >
                  ×
                </button>
              </div>
            </div>
          )}
        </div>

        <p className="ingbird-card-kicker">きみの学習日（トータル）</p>
        <p className="ingbird-card-title">{praise.title}</p>
        <p className="ingbird-card-message">{praise.message}</p>

        <div className="ingbird-card-stats">
          <p className="ingbird-total">
            <strong>{status.totalDays}</strong>
            <span>日</span>
          </p>
          <p className={`ingbird-today${status.studiedToday ? ' done' : ''}`}>
            {status.studiedToday
              ? '今日の学習: ずみ ✓'
              : status.daysSinceLast === null
                ? '今日の学習: まだ'
                : `今日の学習: まだ（前回から${status.daysSinceLast}日）`}
          </p>
        </div>

        {next && (
          <div className="ingbird-meter">
            <p>
              次の節目 {next.at}日目まで あと{next.remaining}日
            </p>
            <div
              className="progress-bar"
              role="progressbar"
              aria-valuenow={status.totalDays}
              aria-valuemin={previous}
              aria-valuemax={next.at}
              aria-label={`次の節目${next.at}日目までの進み具合`}
            >
              <div
                className="progress-fill"
                style={{ width: `${Math.round(Math.min(1, Math.max(0, ratio)) * 100)}%` }}
              />
            </div>
          </div>
        )}

        <p className="ingbird-card-note">
          連続日数ではなく、学習した日の合計です。休んだ日があっても、積み上げた日は1日も減りません。
        </p>

        {!status.studiedToday && (
          <div className="ingbird-card-actions">
            <Link className="btn-primary" to="/vocabulary">
              1セッション始める
            </Link>
            <Link className="btn-secondary" to="/practice">
              音声だけでも
            </Link>
          </div>
        )}
      </div>
    </section>
  )
}
