import { useMemo, useState } from 'react'
import type { QuizQuestion } from '../content/types'
import { shuffle } from '../services/shuffle'
import { AudioButton } from './AudioButton'
import { renderHighlighted } from './textRendering'

type Props = {
  questions: QuizQuestion[]
  onComplete?: (correctCount: number) => void
  /** 1問ごとの正誤。SRSの記録に使う。 */
  onAnswer?: (question: QuizQuestion, correct: boolean) => void
}

/**
 * 多肢選択クイズ。回答後に即時フィードバック(正誤・理由・誤答解説・正解文音声)を表示。
 *
 * 選択肢は表示時にシャッフルする。データ上の正解位置には偏りがあり(A/Bに8割超)、
 * そのまま並べると内容を理解せず位置で当てられてしまうため。
 * インデックスは元データのものを保持し、correctIndex / choiceNotes はそのまま使える。
 */
export function Quiz({ questions, onComplete, onAnswer }: Props) {
  const displayOrders = useMemo(
    () => questions.map((q) => shuffle(q.choices.map((_, i) => i))),
    [questions],
  )
  const [qIndex, setQIndex] = useState(0)
  const [selected, setSelected] = useState<number | null>(null)
  const [correctCount, setCorrectCount] = useState(0)
  const [done, setDone] = useState(false)

  if (questions.length === 0) return null

  if (done) {
    return (
      <div className="quiz-result" role="status">
        <p className="quiz-result-score">
          {questions.length}問中 {correctCount}問正解
        </p>
        <p>{correctCount === questions.length ? 'すべて正解です。よくできました!' : '間違えた問題の解説をもう一度確認しましょう。'}</p>
      </div>
    )
  }

  const question = questions[qIndex]
  const answered = selected !== null
  const isCorrect = selected === question.correctIndex

  const choose = (i: number) => {
    if (answered) return
    setSelected(i)
    if (i === question.correctIndex) setCorrectCount((c) => c + 1)
    onAnswer?.(question, i === question.correctIndex)
  }

  const next = () => {
    if (qIndex + 1 >= questions.length) {
      setDone(true)
      onComplete?.(correctCount)
    } else {
      setQIndex(qIndex + 1)
      setSelected(null)
    }
  }

  return (
    <div className="quiz">
      <p className="quiz-progress">
        問題 {qIndex + 1} / {questions.length}
      </p>
      <p className="quiz-prompt">
        {question.prompt}
        {question.promptAudio && (
          <>
            {' '}
            <AudioButton text={question.promptAudio} leadingPause />{' '}
            <AudioButton text={question.promptAudio} slow leadingPause />
          </>
        )}
      </p>
      {question.sentence && (
        <p className="quiz-sentence" lang="en">
          {question.sentence}
          {question.sentenceJa && <span className="quiz-sentence-ja">{question.sentenceJa}</span>}
        </p>
      )}
      <div className="quiz-choices" role="group" aria-label="選択肢">
        {displayOrders[qIndex].map((i) => {
          let cls = 'quiz-choice'
          if (answered && i === question.correctIndex) cls += ' correct'
          else if (answered && i === selected) cls += ' incorrect'
          return (
            <button key={i} type="button" className={cls} onClick={() => choose(i)} disabled={answered} lang="en">
              {question.choices[i]}
            </button>
          )
        })}
      </div>

      {answered && (
        <div className={`quiz-feedback ${isCorrect ? 'ok' : 'ng'}`} role="status">
          <p className="quiz-verdict">{isCorrect ? '正解!' : '不正解'}</p>
          {!isCorrect && (
            <p className="quiz-correct-answer" lang="en">
              正解: {renderHighlighted(question.choices[question.correctIndex])}
            </p>
          )}
          <p className="quiz-explanation">{question.explanation}</p>
          {question.choiceNotes && (
            <ul className="quiz-choice-notes">
              {displayOrders[qIndex].map((i) => {
                const note = question.choiceNotes?.[i]
                return note && i !== question.correctIndex ? (
                  <li key={i}>
                    <span lang="en">{question.choices[i]}</span> — {note}
                  </li>
                ) : null
              })}
            </ul>
          )}
          {question.audioEn && (
            <p className="quiz-audio" lang="en">
              {question.audioEn} <AudioButton text={question.audioEn} leadingPause />{' '}
              <AudioButton text={question.audioEn} slow leadingPause />
            </p>
          )}
          <button type="button" className="btn-primary quiz-next" onClick={next}>
            {qIndex + 1 >= questions.length ? '結果を見る' : '次の問題へ'}
          </button>
        </div>
      )}
    </div>
  )
}
