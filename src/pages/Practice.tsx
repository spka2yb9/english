import { useState } from 'react'
import { AudioButton } from '../components/AudioButton'
import { diffAnswer, isAnswerCorrect } from '../services/answerCheck'
import {
  drawPracticeSentence,
  getPracticeStats,
  poolFor,
  recordPracticeAnswer,
  type PracticeMode,
} from '../services/practice'
import type { BankSentence } from '../services/sentenceBank'
import { speechService } from '../services/speech'

const MODES: { id: PracticeMode; label: string; description: string }[] = [
  { id: 'shadowing', label: '音読・シャドーイング', description: '英文を聞いて、同じ速さで声に出して繰り返す。テキストは常に表示。' },
  { id: 'dictation', label: 'ディクテーション', description: '音声だけを聞いて英文を書き取る。TTSで安定して読める文のみ出題。' },
]

/**
 * 音声練習。学んだ英文を「聞く」「声に出す」「書き取る」で仕上げる。
 * 出題は実施回数の少ない文から順に全体を1周ずつ回し、問題数も終わりも決めない。
 * モードが2つだけなので一覧画面は挟まず、切り替えは上部のトグルで行う。
 */
export function Practice() {
  const [mode, setMode] = useState<PracticeMode>('shadowing')
  const current = MODES.find((m) => m.id === mode) as (typeof MODES)[number]

  return (
    <div className="page">
      <h1>音声練習</h1>
      <p className="page-lead">
        学んだ英文を、音でも使えるようにします。実施回数の少ない文から順に、全体を1周ずつ回します。
        終わりはないので、やめるときはモードを切り替えるか、ほかのページへ移動してください。
      </p>

      <div className="mode-switch" role="group" aria-label="練習の種類">
        {MODES.map((m) => (
          <button
            key={m.id}
            type="button"
            className={`mode-switch-btn${m.id === mode ? ' selected' : ''}`}
            onClick={() => setMode(m.id)}
            aria-pressed={m.id === mode}
          >
            {m.label}
          </button>
        ))}
      </div>

      <p className="mode-desc">
        {current.description}
        <span className="mode-count">（{poolFor(mode).length.toLocaleString()}文を1周ずつ）</span>
      </p>

      {!speechService.isSupported() && (
        <p className="practice-hint" role="status">
          このブラウザは音声合成に対応していないため、音声は再生できません。英文と和訳は文字で確認できます。
        </p>
      )}

      {/* モードを切り替えたら出題を引き直す(key で作り直す) */}
      <SentenceSession key={mode} mode={mode} />
    </div>
  )
}

function SentenceSession({ mode }: { mode: PracticeMode }) {
  const [sentence, setSentence] = useState<BankSentence | undefined>(() =>
    drawPracticeSentence(mode, getPracticeStats(mode)),
  )
  const [index, setIndex] = useState(0)
  const [input, setInput] = useState('')
  const [checked, setChecked] = useState(false)
  // この練習で採点した文の数と、そのうち正解した数。終わりがないので分母(問題数)は持たない。
  const [graded, setGraded] = useState(0)
  const [correctCount, setCorrectCount] = useState(0)

  if (!sentence) {
    return <p>この練習に使える文がまだありません。</p>
  }

  const correct = checked && isAnswerCorrect(input, sentence.en)

  const check = () => {
    const ok = isAnswerCorrect(input, sentence.en)
    setChecked(true)
    setGraded((n) => n + 1)
    if (ok) setCorrectCount((c) => c + 1)
    recordPracticeAnswer(mode, sentence.id)
  }

  const shadowingDone = () => {
    recordPracticeAnswer(mode, sentence.id)
    next()
  }

  const next = () => {
    // 記録した実施回数を読んで、まだその周で出していない文から引く
    setSentence(drawPracticeSentence(mode, getPracticeStats(mode)))
    setIndex((i) => i + 1)
    setInput('')
    setChecked(false)
  }

  return (
    <div className="practice">
      <p className="quiz-progress">
        {index + 1}問目
        {mode === 'dictation' && graded > 0 && `（正解 ${correctCount} / ${graded}）`}
      </p>

      {mode === 'shadowing' ? (
        <div className="practice-card">
          <p className="practice-en" lang="en">
            {sentence.en}
          </p>
          <p className="practice-ja">{sentence.ja}</p>
          <p className="practice-audio">
            <AudioButton text={sentence.en} />
            <AudioButton text={sentence.en} slow />
          </p>
          <p className="practice-hint">音声を聞き、同じ速さで声に出して繰り返してください（2〜3回）。</p>
          <button type="button" className="btn-primary" onClick={shadowingDone}>
            次の文へ
          </button>
        </div>
      ) : (
        <div className="practice-card">
          <p className="practice-hint">音声を聞いて、英文を書き取ってください。何度でも再生できます。</p>
          <p className="practice-audio">
            <AudioButton text={sentence.en} />
            <AudioButton text={sentence.en} slow />
          </p>

          <label className="practice-input-label">
            <span>解答</span>
            <textarea
              className="practice-input"
              lang="en"
              rows={3}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={checked}
              placeholder="英文を入力"
            />
          </label>

          {!checked ? (
            <button type="button" className="btn-primary" onClick={check} disabled={input.trim().length === 0}>
              採点する
            </button>
          ) : (
            <div className={`quiz-feedback ${correct ? 'ok' : 'ng'}`} role="status">
              <p className="quiz-verdict">{correct ? '正解!' : '不正解'}</p>
              <p className="practice-answer" lang="en">
                {sentence.en} <AudioButton text={sentence.en} />
              </p>
              <p className="practice-ja">{sentence.ja}</p>
              {!correct && (
                <>
                  <p className="practice-diff" lang="en">
                    {diffAnswer(input, sentence.en).map((token, i) => (
                      <span key={i} className={`diff-${token.status}`}>
                        {token.word}{' '}
                      </span>
                    ))}
                  </p>
                  <p className="practice-hint">緑=一致 / 赤=不足 / 取り消し線=余分</p>
                </>
              )}
              <button type="button" className="btn-primary quiz-next" onClick={next}>
                次の問題へ
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
