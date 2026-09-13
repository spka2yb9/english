import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { LessonBlocks } from '../components/LessonBlocks'
import { Quiz } from '../components/Quiz'
import { WordOrder } from '../components/WordOrder'
import { findLesson, findUnit, nextLesson } from '../content/grammar'
import type { GrammarLesson } from '../content/types'
import { downloadLessonMarkdown, downloadLessonPdf } from '../services/export'
import { getCompletedLessons, markLessonCompleted, recordGrammarItemAnswer } from '../services/progress'

export function GrammarLessonPage() {
  const { lessonId } = useParams<{ lessonId: string }>()
  const lesson = lessonId ? findLesson(lessonId) : undefined

  if (!lesson) {
    return (
      <div className="page empty-state">
        <h1>レッスンが見つかりません</h1>
        <p>URLが変更されたか、存在しないセクションです。</p>
        <Link className="btn-primary" to="/grammar">
          英文法の一覧へ戻る
        </Link>
      </div>
    )
  }

  // 同じルート内で次のレッスンへ遷移したときも、クイズ状態を確実に初期化する。
  return <GrammarLessonContent key={lesson.id} lesson={lesson} />
}

function GrammarLessonContent({ lesson }: { lesson: GrammarLesson }) {
  const [completed, setCompleted] = useState(() => getCompletedLessons().has(lesson.id))
  const [pdfBusy, setPdfBusy] = useState(false)
  const [exportError, setExportError] = useState<string | null>(null)
  const unit = findUnit(lesson.unitId)
  const next = nextLesson(lesson.id)
  const prereqLessons = (lesson.prereqs ?? []).map((id) => findLesson(id)).filter((item) => item !== undefined)

  const toggleCompleted = () => {
    markLessonCompleted(lesson.id, !completed)
    setCompleted(!completed)
  }

  const exportPdf = async () => {
    setPdfBusy(true)
    setExportError(null)
    try {
      await downloadLessonPdf(lesson)
    } catch {
      setExportError('PDFを生成できませんでした。時間をおいてもう一度お試しください。')
    } finally {
      setPdfBusy(false)
    }
  }

  return (
    <div className="page lesson-page">
      <nav className="lesson-breadcrumb" aria-label="パンくず">
        <Link to="/grammar">英文法</Link> <span aria-hidden="true">›</span> {unit?.title}
      </nav>
      <header className="lesson-header">
        <span className="lesson-level-badge">{lesson.level}</span>
        <h1>{lesson.title}</h1>
        <p className="lesson-meta">目安: 約{lesson.minutes}分</p>
        <div className="lesson-goal">
          <h2>このセクションの目標</h2>
          <p>{lesson.objective}</p>
        </div>
        {prereqLessons.length > 0 && (
          <p className="lesson-prereqs">
            前提:{' '}
            {prereqLessons.map((prereq, index) => (
              <span key={prereq.id}>
                {index > 0 && '、'}
                <Link to={`/grammar/${prereq.id}`}>{prereq.title}</Link>
              </span>
            ))}
          </p>
        )}
      </header>

      <LessonBlocks blocks={lesson.blocks} />

      <section className="lesson-quiz">
        <h2>理解度チェック</h2>
        {/* 正誤を残しておくと、設定ページの進捗集計とGist同期にそのまま乗る。 */}
        <Quiz
          questions={lesson.quiz}
          onAnswer={(question, correct) => {
            recordGrammarItemAnswer(question.id, correct)
          }}
        />
      </section>

      <section className="lesson-word-order">
        <h2>並べ替え</h2>
        <WordOrder lesson={lesson} />
      </section>

      <section className="lesson-summary">
        <h2>まとめ</h2>
        <ul>
          {lesson.summary.map((point, index) => (
            <li key={index}>{point}</li>
          ))}
        </ul>
      </section>

      <div className="export-row">
        <button type="button" className="btn-secondary" onClick={() => downloadLessonMarkdown(lesson)}>
          ⬇ このレッスンをMarkdownで保存
        </button>
        <button type="button" className="btn-secondary" onClick={exportPdf} disabled={pdfBusy}>
          {pdfBusy ? 'PDFを生成中…' : '⬇ このレッスンをPDFで保存'}
        </button>
      </div>
      {exportError && (
        <p className="export-error" role="alert">
          {exportError}
        </p>
      )}

      <footer className="lesson-footer">
        <button
          type="button"
          className={`lesson-complete-btn ${completed ? 'btn-secondary' : 'btn-primary'}`}
          onClick={toggleCompleted}
          aria-pressed={completed}
        >
          {completed ? '✓ 完了済み（取り消す）' : 'このセクションを完了にする'}
        </button>
        {completed && (
          <p className="lesson-done-msg" role="status">
            このセクションを完了しました!
          </p>
        )}
        {next ? (
          <Link to={`/grammar/${next.id}`} className="btn-primary lesson-next-link">
            次のセクション: {next.title} →
          </Link>
        ) : (
          <Link to="/grammar" className="btn-primary lesson-next-link">
            一覧へ戻る
          </Link>
        )}
      </footer>
    </div>
  )
}
