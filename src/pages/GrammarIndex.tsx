import { useState } from 'react'
import { Link } from 'react-router-dom'
import { grammarRoadmap } from '../content/grammar/roadmap'
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
        英文法は B2まで {grammarUnits.length} ユニット・{allLessons.length} セクション。
        文法事項を個別に覚えるのではなく、<strong>英文がどう組み上がっているか</strong>を追いながら進めるのがおすすめです。
        迷ったら、先に「英文の作られ方」で学習の順番を確かめてください。
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

      <Link className="roadmap-cta" to="/grammar/roadmap" aria-labelledby="roadmap-cta-heading">
        <span className="roadmap-cta-body">
          <span className="eyebrow">学習の流れ</span>
          <h2 id="roadmap-cta-heading">英文の作られ方から学ぶ</h2>
          <span className="roadmap-cta-text">
            <strong>骨格 → 動詞 → 修飾 → 句 → 節 → つなぐ → 長文</strong> の{grammarRoadmap.length}ステップで、英文を読み解く順番を示します。
            5文型は暗記の対象ではなく、英文の中心(S / V / O / C)を見つける道具として使います。
          </span>
        </span>
        <span className="roadmap-cta-arrow" aria-hidden="true">
          →
        </span>
      </Link>

      <section className="level-section" aria-labelledby="level-list-heading">
        <h2 id="level-list-heading" className="level-list-heading">
          レベル別のセクション一覧
        </h2>
        {LEVEL_ORDER.map((level) => {
          const units = unitsByLevel(level)
          if (units.length === 0) return null
          return (
            <div key={level}>
              <h3 className="level-heading">{LEVEL_LABEL[level]}</h3>
              {units.map((unit) => {
                const unitDone = unit.lessons.filter((l) => completed.has(l.id)).length
                return (
                  <div key={unit.id} className="unit-card">
                    <h4>
                      {unit.title}
                      <span className="unit-progress">
                        {unitDone} / {unit.lessons.length}
                      </span>
                    </h4>
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
            </div>
          )
        })}
      </section>
    </div>
  )
}
