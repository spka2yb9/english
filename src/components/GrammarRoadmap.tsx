import { Link } from 'react-router-dom'
import { findLesson } from '../content/grammar'
import { grammarRoadmap } from '../content/grammar/roadmap'
import { LessonBlocks } from './LessonBlocks'

/**
 * 英文の作られ方(STEP 1〜7)の一覧。
 * 見出しと導入文はページ側が持ち、ここはステップの並びだけを描画する。
 * 各ステップは既存のセクション(/grammar/:lessonId)へのリンクを持つ。
 */
export function GrammarRoadmap() {
  return (
    <ol className="roadmap-steps">
      {grammarRoadmap.map((step) => {
        const lessons = step.lessonIds.map((id) => findLesson(id)).filter((lesson) => lesson !== undefined)
        return (
          <li key={step.id} className="roadmap-step">
            <div className="roadmap-step-head">
              <span className="roadmap-number">STEP {step.number}</span>
              <h2>{step.title}</h2>
            </div>
            <p className="roadmap-lead">{step.lead}</p>
            <ul className="roadmap-points">
              {step.points.map((point, index) => (
                <li key={index}>{point}</li>
              ))}
            </ul>
            {step.blocks && (
              <div className="roadmap-figure">
                <LessonBlocks blocks={step.blocks} />
              </div>
            )}
            <p className="roadmap-links">
              <span className="roadmap-links-label">この段階のセクション</span>
              {lessons.map((lesson) => (
                <Link key={lesson.id} to={`/grammar/${lesson.id}`} className="roadmap-link">
                  {lesson.title}
                </Link>
              ))}
            </p>
          </li>
        )
      })}
    </ol>
  )
}
