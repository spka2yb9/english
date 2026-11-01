import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { Ingbird } from '../components/Ingbird'
import { Quiz } from '../components/Quiz'
import { Hiyoko } from '../components/threeMinute/Hiyoko'
import { ThreeMinuteDialogue } from '../components/threeMinute/Dialogue'
import { useIngbirdAppearance } from '../components/threeMinute/useIngbirdAppearance'
import { getThreeMinuteSection, nextThreeMinuteSection, type ThreeMinuteSection } from '../content/threeMinute'
import { THREE_MINUTE_PATTERN_INTRO_ID } from '../content/threeMinute/ids'
import {
  getThreeMinuteCompleted,
  markThreeMinuteCompleted,
  recordGrammarItemAnswer,
} from '../services/progress'
import './ThreeMinute.css'

export function ThreeMinuteLessonPage() {
  const { lessonId } = useParams<{ lessonId: string }>()
  const section = lessonId ? getThreeMinuteSection(lessonId) : undefined

  if (!section) {
    return (
      <div className="page empty-state">
        <h1>お話が見つかりません</h1>
        <p>URLが変更されたか、存在しないセクションです。</p>
        <Link className="btn-primary" to="/three-minute">
          3分間Englishの一覧へ戻る
        </Link>
      </div>
    )
  }

  return <ThreeMinuteLessonContent key={section.lessonId} section={section} />
}

function ThreeMinuteLessonContent({ section }: { section: ThreeMinuteSection }) {
  const appearance = useIngbirdAppearance()
  const [completed, setCompleted] = useState(() => getThreeMinuteCompleted().has(section.lessonId))
  const [quizDone, setQuizDone] = useState(false)
  const [correctCount, setCorrectCount] = useState(0)
  const next = nextThreeMinuteSection(section.lessonId)
  const isIntro = section.lessonId === THREE_MINUTE_PATTERN_INTRO_ID
  const allCorrect = quizDone && correctCount === section.quiz.length

  const toggleCompleted = () => {
    markThreeMinuteCompleted(section.lessonId, !completed)
    setCompleted(!completed)
  }

  return (
    <div className="page tm-page tm-lesson-page">
      <nav className="lesson-breadcrumb" aria-label="パンくず">
        <Link to="/three-minute">3分間English</Link> <span aria-hidden="true">›</span> {section.unitTitle}
      </nav>

      <header className="tm-lesson-header">
        <div className="tm-lesson-kicker">
          <span className="lesson-level-badge">{isIntro ? 'はじめに' : section.level}</span>
          <span className="tm-lesson-time">読了目安 約{section.minutes}分</span>
        </div>
        <h1>{section.title}</h1>
        <p className="tm-lesson-lead">
          {isIntro
            ? 'イングバード先生とヒヨコ君の会話で、英文の骨組みをひととおり学びます。'
            : `イングバード先生とヒヨコ君の会話で、${section.title}のポイントを学びます。`}
        </p>
        <div className="lesson-goal tm-goal">
          <h2>このお話のゴール</h2>
          <p>{section.objective}</p>
        </div>
      </header>

      <div className="tm-cast" aria-label="登場人物">
        <span>
          <Ingbird
            mood="happy"
            evolution={appearance.evolution}
            outfit={appearance.outfit}
            size={38}
            decorative
          />
          イングバード先生
        </span>
        <span>
          <Hiyoko mood="happy" size={38} decorative />
          ヒヨコ君
        </span>
      </div>

      <ThreeMinuteDialogue section={section} appearance={appearance} />

      <section className="lesson-quiz tm-quiz" aria-labelledby="tm-quiz-title">
        <h2 id="tm-quiz-title">理解度チェック</h2>
        <p className="section-lead">{section.quiz.length}問の4択です。答えるとすぐに解説が出ます。</p>
        <Quiz
          questions={section.quiz}
          onAnswer={(question, correct) => {
            recordGrammarItemAnswer(question.id, correct)
          }}
          onComplete={(count) => {
            setQuizDone(true)
            setCorrectCount(count)
          }}
        />
      </section>

      {quizDone && (
        <div className="tm-clear" role="status">
          <Ingbird
            mood={allCorrect ? 'party' : 'happy'}
            evolution={appearance.evolution}
            outfit={appearance.outfit}
            size={74}
            decorative
          />
          <div>
            <p className="tm-clear-title">
              {allCorrect ? `${section.quiz.length}問ぜんぶ正解!` : `${section.quiz.length}問中 ${correctCount}問正解!`}
            </p>
            <p>
              {allCorrect
                ? 'ヒヨコ君、すごいね! この調子で次のお話へ進もう♪'
                : 'おしい問題もあったね。解説を読み返せば、次はできるよ。'}
            </p>
          </div>
          <Hiyoko mood={allCorrect ? 'cheer' : 'happy'} size={66} decorative />
        </div>
      )}

      <footer className="tm-lesson-footer">
        <button
          type="button"
          className={`lesson-complete-btn ${completed ? 'btn-secondary' : 'btn-primary'}`}
          onClick={toggleCompleted}
          aria-pressed={completed}
        >
          {completed ? '✓ 完了済み（取り消す）' : 'このお話を完了にする'}
        </button>
        {completed && (
          <p className="lesson-done-msg" role="status">
            このお話を完了しました!
          </p>
        )}
        {next ? (
          <Link to={`/three-minute/${next.id}`} className="btn-primary lesson-next-link">
            次のお話: {next.title} →
          </Link>
        ) : (
          <Link to="/three-minute" className="btn-primary lesson-next-link">
            一覧へ戻る
          </Link>
        )}
        {/* 英文法ページは一時的に非公開。再開するときはこのリンクを戻す。
        <p className="tm-back-grammar">
          <Link to={`/grammar/${section.lessonId}`}>このテーマを英文法でじっくり学ぶ →</Link>
        </p>
        */}
      </footer>
    </div>
  )
}
