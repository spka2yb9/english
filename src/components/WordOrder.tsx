import { useMemo, useState } from 'react'
import type { GrammarLesson } from '../content/types'
import { isAnswerCorrect } from '../services/answerCheck'
import { buildWordOrderItem, lessonWordOrderSentences } from '../services/derivedItems'
import { AudioButton } from './AudioButton'

/**
 * セクション末尾の並べ替え演習。そのセクションの例文8文を語順から組み立て直す。
 * 選択肢を選ぶクイズが「見て分かる」段階なら、こちらは「自分で並べられる」段階を確かめる。
 */
export function WordOrder({ lesson }: { lesson: GrammarLesson }) {
  const sentences = useMemo(() => lessonWordOrderSentences(lesson), [lesson])
  const [index, setIndex] = useState(0)
  const [picked, setPicked] = useState<number[]>([])
  const [checked, setChecked] = useState(false)
  const [correctCount, setCorrectCount] = useState(0)

  const sentence = sentences[index]
  // シャッフルに乱数を使うため、render のたびではなく出題中の文に対して一度だけ組み立てる。
  const item = useMemo(() => (sentence ? buildWordOrderItem(sentence) : null), [sentence])

  if (sentences.length === 0) return null

  if (index >= sentences.length) {
    return (
      <div className="quiz-result" role="status">
        <p className="quiz-result-score">
          {sentences.length}問中 {correctCount}問正解
        </p>
        <p>
          {correctCount === sentences.length
            ? 'すべて正解です。語順が身についています!'
            : '間違えた文は、もう一度声に出して読んでみましょう。'}
        </p>
      </div>
    )
  }

  if (!item) return null

  const answerText = picked.map((i) => item.tokens[i]).join(' ')
  const correct = checked && isAnswerCorrect(answerText, item.answer)

  const toggleToken = (i: number) => {
    if (checked) return
    // 直前の値から作る。同じtickで複数回押されても選択が失われないようにする。
    setPicked((prev) => (prev.includes(i) ? prev.filter((p) => p !== i) : [...prev, i]))
  }

  const check = () => {
    if (isAnswerCorrect(answerText, item.answer)) setCorrectCount((c) => c + 1)
    setChecked(true)
  }

  const next = () => {
    setIndex(index + 1)
    setPicked([])
    setChecked(false)
  }

  return (
    <div className="practice">
      <p className="quiz-progress">
        問題 {index + 1} / {sentences.length}
      </p>
      <div className="practice-card">
        <p className="practice-hint">語を順に押して英文を作ってください。もう一度押すと取り消せます。</p>
        <p className="practice-ja practice-prompt">{item.ja}</p>
        <ul className="token-list" lang="en">
          {item.tokens.map((token, i) => {
            const used = picked.includes(i)
            return (
              <li key={i}>
                <button
                  type="button"
                  className={`token${used ? ' used' : ''}`}
                  onClick={() => toggleToken(i)}
                  disabled={checked}
                  aria-pressed={used}
                >
                  {token}
                </button>
              </li>
            )
          })}
        </ul>
        <p className="practice-answer-line" lang="en" aria-live="polite">
          {answerText || <span className="practice-placeholder">語を押すとここに並びます</span>}
        </p>

        {!checked ? (
          <button type="button" className="btn-primary" onClick={check} disabled={picked.length === 0}>
            採点する
          </button>
        ) : (
          <div className={`quiz-feedback ${correct ? 'ok' : 'ng'}`} role="status">
            <p className="quiz-verdict">{correct ? '正解!' : '不正解'}</p>
            <p className="practice-answer" lang="en">
              {item.answer} <AudioButton text={item.answer} leadingPause />{' '}
              <AudioButton text={item.answer} slow leadingPause />
            </p>
            <p className="practice-ja">{item.ja}</p>
            <button type="button" className="btn-primary quiz-next" onClick={next}>
              {index + 1 >= sentences.length ? '結果を見る' : '次の問題へ'}
            </button>
          </div>
        )}
      </div>
    </div>
  )
}
