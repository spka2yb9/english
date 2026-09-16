import { useEffect, useRef, useState } from 'react'
import { allVocabulary, findWord } from '../content/vocabulary'
import type { VocabularyEntry } from '../content/types'
import { AudioButton } from '../components/AudioButton'
import { VocabularyMemoryImage } from '../components/VocabularyMemoryImage'
import { vocabularyIllustrations } from '../content/vocabulary/illustrations'
import { answer, currentWordId, startSession, type VocabSessionState } from '../services/vocabSession'
import { selectSessionWords, recordAnswer, masteryOf, SESSION_SIZE } from '../services/vocabSelection'
import type { Mastery, WordStats } from '../services/vocabSelection'
import {
  fillDays,
  getVocabHistory,
  getVocabStats,
  recordVocabAnswer,
  saveVocabStats,
  type VocabDay,
} from '../services/progress'

type Phase = 'start' | 'question' | 'revealed' | 'finished'

export function Vocabulary() {
  const [session, setSession] = useState<VocabSessionState | null>(null)
  const [phase, setPhase] = useState<Phase>('start')
  const [lastKnown, setLastKnown] = useState(false)
  const [roundBanner, setRoundBanner] = useState<string | null>(null)
  const knowRef = useRef<HTMLButtonElement>(null)
  const dontKnowRef = useRef<HTMLButtonElement>(null)
  const nextRef = useRef<HTMLButtonElement>(null)

  // A/D で選択、F で決定(解説中は次へ)。スペースは既定のスクロールのまま残す。
  // どのボタンが出ているかは ref の有無で分かるので、phase に依存しない。
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.repeat || e.metaKey || e.ctrlKey || e.altKey) return
      const focused = document.activeElement
      switch (e.key.toLowerCase()) {
        case 'a':
          knowRef.current?.focus()
          break
        case 'd':
          dontKnowRef.current?.focus()
          break
        case 'f':
          if (nextRef.current) nextRef.current.click()
          else if (focused === knowRef.current || focused === dontKnowRef.current)
            (focused as HTMLButtonElement).click()
          break
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const start = () => {
    // レベルの低い語(A2 → B1 → B2)を優先して出題する。findWord は Map 参照なので、
    // 語ごとの参照コストは他の候補判定と変わらない。
    const ids = selectSessionWords(
      allVocabulary.map((e) => e.id),
      getVocabStats(),
      Date.now(),
      SESSION_SIZE,
      Math.random,
      (id) => findWord(id)?.level,
    )
    setSession(startSession(ids))
    setPhase('question')
    setRoundBanner(null)
  }

  if (allVocabulary.length === 0) {
    return (
      <div className="page">
        <h1>英単語</h1>
        <p>語彙データを準備中です。</p>
      </div>
    )
  }

  if (phase === 'start' || !session) {
    return (
      <div className="page vocab-page">
        <h1>英単語</h1>
        <p className="page-lead">
          {SESSION_SIZE}語を出題します。レベルの低い語(A2 → B1 → B2)を優先し、復習の時期が来た語は先に戻します。
          単語を見て意味を思い出せるか自分で判定してください。わからなかった語は、わかるまで繰り返し出題されます。
        </p>
        <MasteryChart stats={getVocabStats()} history={getVocabHistory()} />
        <button type="button" className="btn-primary btn-large" onClick={start}>
          {SESSION_SIZE}語クイズを始める
        </button>
      </div>
    )
  }

  if (phase === 'finished') {
    return (
      <div className="page vocab-page">
        <h1>英単語</h1>
        <div className="vocab-complete" role="status">
          <p className="vocab-complete-title"><span aria-hidden="true">✓ </span>{SESSION_SIZE}語すべて確認できました!</p>
          <p>
            {session.round > 1
              ? `わからなかった語も、${session.round}周目ですべて「わかる」になりました。`
              : '1周目ですべての語がわかりました。素晴らしい!'}
          </p>
          <button type="button" className="btn-primary btn-large" onClick={start}>
            もう一度{SESSION_SIZE}語に挑戦する
          </button>
        </div>
      </div>
    )
  }

  const wordId = currentWordId(session)
  const entry = wordId ? findWord(wordId) : undefined
  if (!entry) return null

  const onAnswer = (known: boolean) => {
    setLastKnown(known)
    const stats = recordAnswer(getVocabStats(), entry.id, known)
    saveVocabStats(stats)
    recordVocabAnswer(stats)
    setPhase('revealed')
  }

  const onNext = () => {
    const next = answer(session, lastKnown)
    setSession(next)
    if (next.finished) {
      setPhase('finished')
      return
    }
    if (next.round > session.round) {
      setRoundBanner(
        `${session.round}周目完了 — わからなかった${next.queue.length}語をもう一度確認します`,
      )
    } else if (next.round > 1) {
      setRoundBanner(next.queue.length - next.index === 1 ? '残り1語です' : null)
    } else {
      setRoundBanner(null)
    }
    setPhase('question')
  }

  return (
    <div className="page vocab-page">
      <h1>英単語</h1>
      <p className="vocab-session-progress">
        {session.round > 1 && <span className="vocab-round-tag">{session.round}周目 </span>}
        {session.index + 1} / {session.queue.length}語
      </p>
      {roundBanner && (
        <p className="vocab-round-banner" role="status">
          {roundBanner}
        </p>
      )}

      <div className="vocab-card">
        <p className="vocab-word" lang="en">
          {entry.word}
          <AudioButton text={entry.word} />
        </p>

        {phase === 'question' ? (
          <>
            <p className="vocab-instruction">この単語の意味を思い出してから、ボタンを押してください。</p>
            <div className="vocab-answer-row">
              <button type="button" className="btn-know" ref={knowRef} onClick={() => onAnswer(true)}>
                わかる
              </button>
              <button type="button" className="btn-dontknow" ref={dontKnowRef} onClick={() => onAnswer(false)}>
                わからない
              </button>
            </div>
          </>
        ) : (
          <div className="vocab-reveal">
            <p className={`vocab-self-verdict ${lastKnown ? 'known' : 'unknown'}`}>
              {lastKnown ? '「わかる」と答えました' : '「わからない」と答えました — 後でもう一度出題されます'}
            </p>
            <p className="vocab-pron">
              <span className="vocab-ipa" lang="en">{entry.pronunciation}</span>
              <span className="vocab-pos">{entry.partOfSpeech}</span>
              <span className="vocab-level">{entry.level}</span>
            </p>
            <p className="vocab-meaning">{entry.meaningsJa.join('、')}</p>

            <div className="vocab-example">
              <p className="example-en" lang="en">
                {entry.exampleSentence}
                <span className="example-audio">
                  <AudioButton text={entry.exampleSentence} />
                  <AudioButton text={entry.exampleSentence} slow />
                </span>
              </p>
              <p className="example-ja">{entry.exampleTranslationJa}</p>
              {entry.exampleSource && (
                <p className="vocab-example-source">
                  例文出典:{' '}
                  <a href={entry.exampleSource.url} target="_blank" rel="noreferrer">
                    {entry.exampleSource.name}
                  </a>{' '}
                  ({entry.exampleSource.license})
                  {entry.exampleSource.attribution && ` — ${entry.exampleSource.attribution}`}
                </p>
              )}
            </div>

            {entry.collocations && entry.collocations.length > 0 && (
              <p className="vocab-collocations">
                <strong>よく使う組み合わせ:</strong>{' '}
                {entry.collocations.map((c, i) => (
                  <span key={i} className="collocation" lang="en">
                    {c}
                    {i < entry.collocations!.length - 1 ? ' / ' : ''}
                  </span>
                ))}
              </p>
            )}

            {hasHints(entry) && (
              <details className="vocab-hints" open>
                <summary>覚えるヒント</summary>
                {vocabularyIllustrations[entry.id] && (
                  <VocabularyMemoryImage key={entry.id} illustration={vocabularyIllustrations[entry.id]} />
                )}
                {entry.wordFormation && (
                  <p>
                    <strong>語のつくり:</strong> {entry.wordFormation}
                  </p>
                )}
                {entry.mnemonic && (
                  <p>
                    <strong>記憶のコツ:</strong> {entry.mnemonic}
                  </p>
                )}
                {entry.relatedWords && entry.relatedWords.length > 0 && (
                  <p>
                    <strong>関連語:</strong> <span lang="en">{entry.relatedWords.join(', ')}</span>
                  </p>
                )}
              </details>
            )}

          </div>
        )}
      </div>

      <div className="vocab-keybar">
        <p className="vocab-keybar-hint">
          {phase === 'question'
            ? 'A わかる / D わからない / F 決定（スペースでスクロール）'
            : 'F 次へ（スペースでスクロール）'}
        </p>
        {phase === 'revealed' && (
          <button type="button" className="btn-primary vocab-next" ref={nextRef} onClick={onNext}>
            次へ
          </button>
        )}
      </div>
    </div>
  )
}

const BANDS: { key: Mastery; label: string }[] = [
  { key: 'mastered', label: '定着' },
  { key: 'learning', label: '学習中' },
  { key: 'weak', label: '苦手' },
]

/** グラフに出す日数。localStorage には120日分あるが、横軸が潰れない範囲で切る。 */
const CHART_DAYS = 30

type Tally = Record<Mastery, number> & { unseen: number; total: number }

function tally(entries: readonly VocabularyEntry[], stats: WordStats): Tally {
  const t: Tally = { mastered: 0, learning: 0, weak: 0, unseen: 0, total: entries.length }
  for (const entry of entries) {
    const stat = stats[entry.id]
    if (stat) t[masteryOf(stat)] += 1
    else t.unseen += 1
  }
  return t
}

const monthDay = (date: string) => `${+date.slice(5, 7)}/${+date.slice(8, 10)}`

/** 覚えている量。現在の内訳(積み上げ棒)+ 定着語数の推移(折れ線)+ 日別の練習量(棒)。 */
function MasteryChart({ stats, history }: { stats: WordStats; history: VocabDay[] }) {
  const t = tally(allVocabulary, stats)
  const series = fillDays(history, CHART_DAYS)
  const studied = t.total - t.unseen
  const percent = Math.round((t.mastered / t.total) * 100)

  return (
    <section className="mastery" aria-labelledby="mastery-title">
      <h2 id="mastery-title" className="mastery-title">覚えている量</h2>
      <p className="mastery-hero">
        <strong>{t.mastered.toLocaleString()}</strong>語 定着
        <span className="mastery-hero-sub">
          収録 {t.total.toLocaleString()}語の{percent}% ・ 学習済み {studied.toLocaleString()}語
        </span>
      </p>

      <div className="mastery-bar" role="img" aria-label={barAlt(t)}>
        {BANDS.filter((band) => t[band.key] > 0).map((band) => (
          <span
            key={band.key}
            className={`mastery-seg ${band.key}`}
            style={{ width: `${(t[band.key] / t.total) * 100}%` }}
            title={`${band.label} ${t[band.key]}語`}
          />
        ))}
      </div>
      <ul className="mastery-legend">
        {BANDS.map((band) => (
          <li key={band.key}>
            <span className={`mastery-swatch ${band.key}`} aria-hidden="true" />
            {band.label} {t[band.key].toLocaleString()}語
          </li>
        ))}
        <li>
          <span className="mastery-swatch unseen" aria-hidden="true" />
          未学習 {t.unseen.toLocaleString()}語
        </li>
      </ul>

      {series.length > 1 ? (
        <div className="mastery-charts">
          <TrendChart series={series} />
          <DailyChart series={series} />
        </div>
      ) : (
        <p className="mastery-note">
          {series.length === 0
            ? 'クイズを始めると、定着した語の推移と日別の練習量をここにグラフで表示します。'
            : '推移のグラフは、2日目の学習から表示されます。'}
        </p>
      )}

      <p className="mastery-note">
        「わかる」が別の日に3回続いた語を定着、直近で「わからない」と答えた語を苦手としています。
      </p>
    </section>
  )
}

/** 定着語数の推移。スパークライン(面+折れ線)。目盛りは最大値と両端の日付だけ。 */
function TrendChart({ series }: { series: VocabDay[] }) {
  const W = 320
  const H = 84
  const PAD = 6
  const max = Math.max(...series.map((d) => d.mastered), 1)
  const x = (i: number) => PAD + (i / (series.length - 1)) * (W - PAD * 2)
  const y = (v: number) => H - PAD - (v / max) * (H - PAD * 2)
  const points = series.map((d, i) => `${x(i).toFixed(1)},${y(d.mastered).toFixed(1)}`).join(' ')
  const last = series[series.length - 1]
  const gained = last.mastered - series[0].mastered

  return (
    <figure className="chart">
      <figcaption className="chart-title">
        定着語数の推移
        <span className="chart-sub">{series.length}日間で{gained >= 0 ? '+' : ''}{gained}語</span>
      </figcaption>
      <svg className="chart-svg" viewBox={`0 0 ${W} ${H}`} role="img" aria-label={trendAlt(series)}>
        <polygon className="trend-area" points={`${PAD},${H - PAD} ${points} ${W - PAD},${H - PAD}`} />
        <polyline className="trend-line" points={points} />
        {series.map((d, i) => (
          <circle
            key={d.date}
            className={`trend-dot${i === series.length - 1 ? ' last' : ''}`}
            cx={x(i)}
            cy={y(d.mastered)}
            r={4}
          >
            <title>{`${monthDay(d.date)} 定着 ${d.mastered}語`}</title>
          </circle>
        ))}
      </svg>
      <p className="chart-axis">
        <span>{monthDay(series[0].date)}</span>
        <span className="chart-axis-max">最大 {max.toLocaleString()}語</span>
        <span>{monthDay(last.date)}</span>
      </p>
    </figure>
  )
}

/** 日別の練習語数。棒は CSS の高さだけで足りるので SVG を使わない。 */
function DailyChart({ series }: { series: VocabDay[] }) {
  const max = Math.max(...series.map((d) => d.count), 1)
  const total = series.reduce((sum, d) => sum + d.count, 0)

  return (
    <figure className="chart">
      <figcaption className="chart-title">
        日別の練習語数
        <span className="chart-sub">{series.length}日間で{total.toLocaleString()}語</span>
      </figcaption>
      <div className="daily-bars" role="img" aria-label={dailyAlt(series)}>
        {series.map((d) => (
          <span key={d.date} className="daily-slot" title={`${monthDay(d.date)} ${d.count}語`}>
            <span className="daily-bar" style={{ height: `${(d.count / max) * 100}%` }} />
          </span>
        ))}
      </div>
      <p className="chart-axis">
        <span>{monthDay(series[0].date)}</span>
        <span className="chart-axis-max">最大 {max}語/日</span>
        <span>{monthDay(series[series.length - 1].date)}</span>
      </p>
    </figure>
  )
}

function barAlt(t: Tally): string {
  return `収録${t.total}語の内訳: ${BANDS.map((b) => `${b.label}${t[b.key]}語`).join('、')}、未学習${t.unseen}語`
}

function trendAlt(series: VocabDay[]): string {
  const shown = series.filter((d, i) => i === 0 || i === series.length - 1 || d.count > 0)
  return `定着語数の推移: ${shown.map((d) => `${monthDay(d.date)} ${d.mastered}語`).join('、')}`
}

function dailyAlt(series: VocabDay[]): string {
  const active = series.filter((d) => d.count > 0)
  return `日別の練習語数: ${active.map((d) => `${monthDay(d.date)} ${d.count}語`).join('、') || '記録なし'}`
}

function hasHints(entry: VocabularyEntry): boolean {
  return Boolean(vocabularyIllustrations[entry.id] || entry.wordFormation || entry.mnemonic || (entry.relatedWords && entry.relatedWords.length > 0))
}
