import { useState } from 'react'
import { ipaEntries, minimalPairs, pronunciationTopics } from '../content/pronunciation/data'
import { buildIpaQuestions, ipaQuizWords } from '../content/pronunciation/quiz'
import type { PronunciationEntry } from '../content/types'
import { AudioButton } from '../components/AudioButton'
import { EnglishExample } from '../components/EnglishExample'
import { Quiz } from '../components/Quiz'
import { RichText } from '../components/RichText'

const QUESTIONS_PER_ROUND = 10

const TYPE_LABEL: Record<PronunciationEntry['type'], string> = {
  vowel: '母音',
  diphthong: '二重母音',
  consonant: '子音',
}

export function Pronunciation() {
  const types: PronunciationEntry['type'][] = ['vowel', 'diphthong', 'consonant']
  // n は Quiz の key。ラウンドを進めるたびに出題し直し、Quiz の進行状態もリセットする。
  const [round, setRound] = useState(() => ({ n: 0, questions: buildIpaQuestions(QUESTIONS_PER_ROUND) }))

  return (
    <div className="page">
      <h1>発音記号</h1>
      <p className="page-lead">
        アメリカ英語の発音記号のリファレンスです。例語のスピーカーボタンを押すと音声を聞けます。
        日本人が特に苦手な音は「聞き分けチャレンジ」で練習しましょう。
      </p>

      {types.map((type) => (
        <section key={type} className="ipa-section">
          <h2>{TYPE_LABEL[type]}</h2>
          <p className="scroll-hint">表は横にスクロールできます。</p>
          <div
            className="table-scroll"
            role="region"
            aria-label={`${TYPE_LABEL[type]}の発音記号表（横にスクロールできます）`}
            tabIndex={0}
          >
            <table className="ipa-table">
              <thead>
                <tr>
                  <th>記号</th>
                  <th>例語</th>
                  <th>音の説明</th>
                  <th>出し方のコツ</th>
                </tr>
              </thead>
              <tbody>
                {ipaEntries
                  .filter((e) => e.type === type)
                  .map((entry) => (
                    <tr key={entry.symbol}>
                      <td className="ipa-symbol" lang="en">
                        {entry.symbol}
                      </td>
                      <td className="ipa-examples">
                        {entry.examples.map((word) => (
                          <span key={word} className="ipa-example" lang="en">
                            {word} <AudioButton text={word} />
                          </span>
                        ))}
                      </td>
                      <td>{entry.ja}</td>
                      <td>{entry.tip}</td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </section>
      ))}

      <section className="pairs-section">
        <h2>聞き分けチャレンジ(日本人が苦手な音)</h2>
        <p>2つの単語を交互に聞いて、違いを耳に覚えさせましょう。何度でも再生できます。</p>
        <div className="pairs-grid">
          {minimalPairs.map((pair, i) => (
            <div key={i} className="pair-card">
              <h3>{pair.focus}</h3>
              <div className="pair-words">
                <span className="pair-word" lang="en">
                  {pair.a.word} <span className="pair-ipa">{pair.a.ipa}</span>{' '}
                  <AudioButton text={pair.a.word} />
                </span>
                <span className="pair-vs" aria-hidden="true">
                  vs
                </span>
                <span className="pair-word" lang="en">
                  {pair.b.word} <span className="pair-ipa">{pair.b.ipa}</span>{' '}
                  <AudioButton text={pair.b.word} />
                </span>
              </div>
              <p className="pair-tip">{pair.tip}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="ipa-quiz-section">
        <h2>演習問題(発音記号の穴埋め)</h2>
        <p>
          単語の発音記号のうち1つが空所になっています。スピーカーボタンで単語の音声を聞きながら、
          入る記号を4択で選びましょう。選択肢には似た音の記号が並びます。
          全{ipaQuizWords.length}問から毎回{QUESTIONS_PER_ROUND}問をランダムに出題します。
        </p>
        <Quiz key={round.n} questions={round.questions} />
        <button
          type="button"
          className="btn-secondary"
          onClick={() => setRound((r) => ({ n: r.n + 1, questions: buildIpaQuestions(QUESTIONS_PER_ROUND) }))}
        >
          別の{QUESTIONS_PER_ROUND}問に挑戦
        </button>
      </section>

      <section className="topics-section">
        <h2>英語の音の仕組み</h2>
        {pronunciationTopics.map((topic) => (
          <details key={topic.id} className="topic-card">
            <summary>{topic.title}</summary>
            <RichText text={topic.body} />
            {topic.examples.map((ex, i) => (
              <EnglishExample
                key={i}
                text={ex.en}
                translation={ex.ja}
                highlight={ex.highlight}
                note={ex.note}
              />
            ))}
          </details>
        ))}
      </section>
    </div>
  )
}
