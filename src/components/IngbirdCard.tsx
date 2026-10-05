import { Link } from 'react-router-dom'
import { Ingbird } from './Ingbird'
import './Ingbird.css'
import { MILESTONES, getStudyStatus, praiseFor } from '../services/studyDays'

/**
 * ホームのマスコットカード。数えるのは連続日数ではなく、学習した日の合計(トータル)。
 * 久しぶりの日も、まだ学習していない日も、責めずに「来たこと」からほめる。
 */
export function IngbirdCard() {
  const status = getStudyStatus()
  const praise = praiseFor(status)
  const { next } = status
  // 直前の節目から次の節目までを1本のバーにする(0日目は0→1日目の区間)
  const previous = MILESTONES.filter((milestone) => milestone <= status.totalDays).at(-1) ?? 0
  const ratio = next ? (status.totalDays - previous) / (next.at - previous) : 1

  return (
    <section className="ingbird-card" aria-label="イングバードからのメッセージ">
      <div className="ingbird-card-bird">
        <Ingbird mood={praise.mood} size={128} decorative />
        <span className="ingbird-name">イングバード</span>
      </div>
      <div className="ingbird-card-body">
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
