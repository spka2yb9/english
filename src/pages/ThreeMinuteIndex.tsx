import { Link } from 'react-router-dom'
import { Ingbird } from '../components/Ingbird'
import { Hiyoko } from '../components/threeMinute/Hiyoko'
import { useIngbirdAppearance } from '../components/threeMinute/useIngbirdAppearance'
import { LEVEL_ORDER, allLessons, grammarUnits } from '../content/grammar'
import { getThreeMinuteCompleted } from '../services/progress'
import './ThreeMinute.css'

const LEVEL_LABEL: Record<string, string> = {
  A2: 'A2 — 基礎の確認',
  'A2+': 'A2+ — 基礎から一歩先へ',
  B1: 'B1 — 中級の核心',
  'B1+': 'B1+ — 中級の完成',
  B2: 'B2 — 上級への到達',
}

/**
 * 3分間English の一覧。
 * 英文法と同じ33ユニット・116セクションを、会話形式の短いお話として並べる。
 */
export function ThreeMinuteIndex() {
  const appearance = useIngbirdAppearance()
  const completed = getThreeMinuteCompleted()
  const completedCount = allLessons.filter((lesson) => completed.has(lesson.id)).length
  const next = allLessons.find((lesson) => !completed.has(lesson.id))

  return (
    <div className="page tm-page">
      <section className="tm-hero" aria-labelledby="tm-title">
        <div className="tm-hero-copy">
          <p className="eyebrow">3 Minute English</p>
          <h1 id="tm-title">3分間English</h1>
          <p className="tm-hero-lead">
            イングバード先生とヒヨコ君の、やさしい英文法教室。
            英文法の全範囲を、1話3分ほどの会話でひとつずつ学べます。
          </p>
          <div className="tm-hero-actions">
            {next ? (
              <Link className="btn-primary" to={`/three-minute/${next.id}`}>
                次のお話を読む
              </Link>
            ) : (
              <Link className="btn-primary" to="/three-minute">
                お話の一覧へ
              </Link>
            )}
            {/* 英文法ページは一時的に非公開。再開するときはこのリンクを戻す。
            <Link className="btn-secondary" to="/grammar">
              英文法でじっくり学ぶ
            </Link>
            */}
          </div>
          <div className="tm-hero-stats" aria-label="収録内容">
            <span>{allLessons.length}話</span>
            <span>{grammarUnits.length}ユニット</span>
            <span>{LEVEL_ORDER.length}レベル</span>
            <span>
              完了 {completedCount} / {allLessons.length}
            </span>
          </div>
        </div>

        <div className="tm-hero-mascots" aria-hidden="true">
          <span className="tm-hero-bubble">いっしょに学ぼう♪</span>
          <div className="tm-hero-bird">
            <Ingbird
              mood="cheer"
              evolution={appearance.evolution}
              outfit={appearance.outfit}
              size={132}
              decorative
            />
            <span>イングバード先生</span>
          </div>
          <div className="tm-hero-chick">
            <Hiyoko mood="happy" size={108} decorative />
            <span>ヒヨコ君</span>
          </div>
        </div>
      </section>

      <p className="tm-note">
        「3分間」は1話の目安です。図や音声もあわせて、ゆっくり進めてね。
        各話の最後に、4択の理解度チェックが4問あります。
      </p>

      <section className="tm-level-section" aria-labelledby="tm-level-list">
        <h2 id="tm-level-list">レベル別のお話</h2>
        {LEVEL_ORDER.map((level) => {
          const units = grammarUnits.filter((unit) => unit.level === level)
          if (units.length === 0) return null
          return (
            <div className="tm-level" key={level}>
              <h3>{LEVEL_LABEL[level]}</h3>
              {units.map((unit) => {
                const doneInUnit = unit.lessons.filter((lesson) => completed.has(lesson.id)).length
                return (
                  <div className="tm-unit" key={unit.id}>
                    <h4>
                      {unit.title}
                      <span className="tm-unit-progress">
                        {doneInUnit} / {unit.lessons.length}
                      </span>
                    </h4>
                    <ul className="tm-lesson-list">
                      {unit.lessons.map((lesson) => {
                        const done = completed.has(lesson.id)
                        return (
                          <li key={lesson.id}>
                            <Link to={`/three-minute/${lesson.id}`} className={done ? 'done' : undefined}>
                              <span className="tm-check" aria-hidden="true">
                                {done ? '✓' : '○'}
                              </span>
                              <span className="tm-lesson-title">{lesson.title}</span>
                              <span className="tm-lesson-badge">3分</span>
                            </Link>
                          </li>
                        )
                      })}
                    </ul>
                  </div>
                )
              })}
            </div>
          )
        })}
      </section>
    </div>
  )
}
