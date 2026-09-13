import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { AudioButton } from '../components/AudioButton'
import { Quiz } from '../components/Quiz'
import { findPassage, readingPassages } from '../content/reading'
import type { ReadingPassage } from '../content/types'
import { KEYS, loadJson, saveJson } from '../services/storage'

const LEVELS: ReadingPassage['level'][] = ['A2', 'B1', 'B2']

function getDone(): Set<string> {
  return new Set(loadJson<string[]>(KEYS.readingDone, []))
}

/** 読了の記録。`done=false` で取り消す。文法の `markLessonCompleted` と同じ扱い。 */
function markPassageDone(passageId: string, done = true): void {
  const ids = getDone()
  if (done) ids.add(passageId)
  else ids.delete(passageId)
  saveJson(KEYS.readingDone, [...ids])
}

export function ReadingIndex() {
  const done = getDone()
  // null = 未保存。その場合だけ「最初の未読了レベルを開く」既定にする。
  const [openLevels, setOpenLevels] = useState<string[] | null>(() =>
    loadJson<string[] | null>(KEYS.readingOpen, null),
  )
  const groups = LEVELS.map((level) => ({
    level,
    items: readingPassages.filter((p) => p.level === level),
  })).filter((group) => group.items.length > 0)
  const doneCount = readingPassages.filter((p) => done.has(p.id)).length
  // 本文が多いので既定は折りたたみ、最初の未読了レベルだけ開く。全部読了なら最後のレベル。
  const defaultOpen =
    groups.find((group) => group.items.some((p) => !done.has(p.id)))?.level ?? groups.at(-1)?.level
  const isOpen = (level: string) => (openLevels ? openLevels.includes(level) : level === defaultOpen)
  const toggle = (level: string, open: boolean) => {
    const current = groups.map((g) => g.level).filter(isOpen)
    const next = open ? [...current, level] : current.filter((l) => l !== level)
    setOpenLevels(next)
    saveJson(KEYS.readingOpen, next)
  }

  return (
    <div className="page">
      <h1>多読</h1>
      <p className="page-lead">
        まとまった英文を読み、内容を確認します。段落ごとに音声と和訳があるので、読んだあとに聞き直せます。
      </p>
      <p className="grammar-progress-line">
        多読 {doneCount} / {readingPassages.length} 本 読了
      </p>
      {groups.map(({ level, items }) => {
        const levelDone = items.filter((p) => done.has(p.id)).length
        return (
          <details
            key={level}
            className="level-section reading-level"
            open={isOpen(level)}
            onToggle={(e) => toggle(level, e.currentTarget.open)}
          >
            <summary>
              {level}
              <span className="unit-progress">
                {levelDone} / {items.length} 本
              </span>
            </summary>
            <ul className="lesson-list reading-list">
              {items.map((passage) => (
                <li key={passage.id}>
                  <Link to={`/reading/${passage.id}`} className="lesson-link">
                    <span className="lesson-link-title">
                      {done.has(passage.id) && <span aria-label="読了" className="done-mark">✓ </span>}
                      {passage.title}
                    </span>
                    <span className="lesson-link-meta">
                      {passage.titleJa} ・ 約{passage.minutes}分
                    </span>
                  </Link>
                </li>
              ))}
            </ul>
          </details>
        )
      })}
    </div>
  )
}

export function ReadingPassagePage() {
  const { passageId } = useParams<{ passageId: string }>()
  const passage = passageId ? findPassage(passageId) : undefined
  const [showJa, setShowJa] = useState(false)
  const [completed, setCompleted] = useState(() => (passageId ? getDone().has(passageId) : false))

  if (!passage) {
    return (
      <div className="page empty-state">
        <h1>本文が見つかりません</h1>
        <Link className="btn-primary" to="/reading">
          多読の一覧へ
        </Link>
      </div>
    )
  }

  const toggleCompleted = () => {
    markPassageDone(passage.id, !completed)
    setCompleted(!completed)
  }

  return (
    <div className="page lesson-page">
      <nav className="lesson-breadcrumb" aria-label="パンくず">
        <Link to="/reading">多読</Link> <span aria-hidden="true">›</span> {passage.level}
      </nav>
      <header className="lesson-header">
        <span className="lesson-level-badge">{passage.level}</span>
        <h1 lang="en">{passage.title}</h1>
        <p className="lesson-meta">
          {passage.titleJa} ・ 目安: 約{passage.minutes}分
        </p>
      </header>

      <div className="reading-controls">
        <button type="button" className="btn-secondary" onClick={() => setShowJa(!showJa)} aria-pressed={showJa}>
          {showJa ? '和訳を隠す' : '和訳を表示'}
        </button>
      </div>

      <article className="reading-body">
        {passage.paragraphs.map((paragraph, i) => (
          <div key={i} className="reading-para">
            <p lang="en">
              {paragraph}
              <span className="example-audio">
                <AudioButton text={paragraph} leadingPause />
                <AudioButton text={paragraph} slow leadingPause />
              </span>
            </p>
            {showJa && <p className="reading-ja">{passage.paragraphsJa[i]}</p>}
          </div>
        ))}
      </article>

      <section className="reading-glossary">
        <h2>語注</h2>
        <ul>
          {passage.glossary.map((item) => (
            <li key={item.word}>
              <span lang="en">{item.word}</span> — {item.ja}
            </li>
          ))}
        </ul>
      </section>

      <section className="lesson-quiz">
        <h2>内容理解</h2>
        <Quiz questions={passage.questions} />
      </section>

      <footer className="lesson-footer">
        <button
          type="button"
          className={`lesson-complete-btn ${completed ? 'btn-secondary' : 'btn-primary'}`}
          onClick={toggleCompleted}
          aria-pressed={completed}
        >
          {completed ? '✓ 読了済み（取り消す）' : 'この本文を読了にする'}
        </button>
        {completed && (
          <p className="lesson-done-msg" role="status">
            この本文を読了しました!
          </p>
        )}
        <Link to="/reading" className="btn-primary lesson-next-link">
          多読の一覧へ戻る
        </Link>
      </footer>
    </div>
  )
}
