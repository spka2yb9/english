import { useState } from 'react'
import { Link } from 'react-router-dom'
import { LEVEL_ORDER, allLessons, grammarUnits, unitsByLevel } from '../content/grammar'
import { getCompletedLessons } from '../services/progress'
import { downloadAllMarkdown, downloadAllPdf } from '../services/export'

const LEVEL_LABEL: Record<string, string> = {
  A2: 'A2 — 基礎の確認',
  'A2+': 'A2+ — 基礎から一歩先へ',
  B1: 'B1 — 中級の核心',
  'B1+': 'B1+ — 中級の完成',
  B2: 'B2 — 上級への到達',
}

export function GrammarIndex() {
  const completed = getCompletedLessons()
  const completedCount = allLessons.filter((l) => completed.has(l.id)).length
  const [busy, setBusy] = useState(false)
  const [exportError, setExportError] = useState<string | null>(null)

  const exportPdf = async () => {
    setBusy(true)
    setExportError(null)
    try {
      await downloadAllPdf()
    } catch {
      setExportError('PDFを生成できませんでした。時間をおいてもう一度お試しください。')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="page">
      <h1>英文法</h1>
      <p className="page-lead">
        B2まで {grammarUnits.length} ユニット・{allLessons.length} セクション。上から順に進めるのがおすすめです。
      </p>
      <p className="grammar-progress-line">
        英文法 {completedCount} / {allLessons.length} セクション完了
      </p>
      <div className="export-row">
        <button type="button" className="btn-secondary" onClick={downloadAllMarkdown}>
          ⬇ Markdownで全教材をダウンロード
        </button>
        <button type="button" className="btn-secondary" onClick={exportPdf} disabled={busy}>
          {busy ? 'PDFを生成中…' : '⬇ PDFで全教材をダウンロード'}
        </button>
      </div>
      {exportError && (
        <p className="export-error" role="alert">
          {exportError}
        </p>
      )}

      {LEVEL_ORDER.map((level) => {
        const units = unitsByLevel(level)
        if (units.length === 0) return null
        return (
          <section key={level} className="level-section">
            <h2 className="level-heading">{LEVEL_LABEL[level]}</h2>
            {units.map((unit) => {
              const unitDone = unit.lessons.filter((l) => completed.has(l.id)).length
              return (
                <div key={unit.id} className="unit-card">
                  <h3>
                    {unit.title}
                    <span className="unit-progress">
                      {unitDone} / {unit.lessons.length}
                    </span>
                  </h3>
                  <ul className="lesson-list">
                    {unit.lessons.map((lesson) => (
                      <li key={lesson.id}>
                        <Link to={`/grammar/${lesson.id}`} className={completed.has(lesson.id) ? 'done' : ''}>
                          <span className="lesson-check" aria-hidden="true">
                            {completed.has(lesson.id) ? '✓' : '○'}
                          </span>
                          <span className="lesson-title">{lesson.title}</span>
                          <span className="lesson-minutes">{lesson.minutes}分</span>
                        </Link>
                      </li>
                    ))}
                  </ul>
                </div>
              )
            })}
          </section>
        )
      })}
    </div>
  )
}
