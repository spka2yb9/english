import { Link } from 'react-router-dom'
import { Ingbird } from '../components/Ingbird'
import { Hiyoko } from '../components/threeMinute/Hiyoko'
import { useIngbirdAppearance } from '../components/threeMinute/useIngbirdAppearance'
import { LEVEL_ORDER, allLessons, grammarUnits } from '../content/grammar'
import { THREE_MINUTE_PATTERN_INTRO_ID, THREE_MINUTE_PATTERN_INTRO_TITLE } from '../content/threeMinute/ids'
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
 * 冒頭に5文型の導入を置き、そのあとに英文法と同じ33ユニット・116セクションを並べる。
 */
export function ThreeMinuteIndex() {
  const appearance = useIngbirdAppearance()
  const completed = getThreeMinuteCompleted()
  const introDone = completed.has(THREE_MINUTE_PATTERN_INTRO_ID)
  const totalStories = allLessons.length + 1
  const completedCount = allLessons.filter((lesson) => completed.has(lesson.id)).length + (introDone ? 1 : 0)
  const next = introDone
    ? allLessons.find((lesson) => !completed.has(lesson.id))
    : { id: THREE_MINUTE_PATTERN_INTRO_ID, title: THREE_MINUTE_PATTERN_INTRO_TITLE }

  return (
    <div className="page tm-page">
      <section className="tm-hero" aria-labelledby="tm-title">
        <div className="tm-hero-copy">
          <p className="eyebrow">3 Minute English</p>
          <h1 id="tm-title">3分間English</h1>
          <p className="tm-hero-lead">
            イングバード先生とヒヨコ君の、やさしい英文法教室。
            まずは5文型の地図から、英文法の全範囲を1話ずつ学べます。
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
            <span>{totalStories}話</span>
            <span>{grammarUnits.length}ユニット</span>
            <span>{LEVEL_ORDER.length}レベル</span>
            <span>
              完了 {completedCount} / {totalStories}
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

      <Link
        to={`/three-minute/${THREE_MINUTE_PATTERN_INTRO_ID}`}
        className={`tm-start-card${introDone ? ' done' : ''}`}
        aria-labelledby="tm-start-title"
      >
        <span className="tm-start-kicker">まずはここから・約9分</span>
        <h2 id="tm-start-title">{THREE_MINUTE_PATTERN_INTRO_TITLE}</h2>
        <span className="tm-start-lead">
          S / V / O / C / M の役割から、5文型すべての見分け方まで。
          アニメーションと例文で、英文の骨組みをひととおり理解できます。
        </span>
        <span className="tm-start-topics">S / V / O / C / M ・ 5文型 ・ O = C の見分け方</span>
        <span className="tm-start-cta">
          {introDone ? '✓ 完了 — もう一度読む' : '5文型をはじめから学ぶ'} <span aria-hidden="true">→</span>
        </span>
      </Link>

      <p className="tm-note">
        「3分間」は1話の目安です。最初の「5文型の地図」は、5文型をひととおり理解するための少し長めの導入(約9分)です。
        図や音声もあわせて、ゆっくり進めてね。各話の最後に、4択の理解度チェックがあります(通常4問、5文型の導入は8問)。
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
