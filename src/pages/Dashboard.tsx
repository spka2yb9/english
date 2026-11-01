import { Link } from 'react-router-dom'
import { IngbirdCard } from '../components/IngbirdCard'
import { LearningIcon } from '../components/LearningIcon'
import { grammarLessonSummaries, readingPassageCount, vocabularyCount } from '../content/summary'
import { getThreeMinuteCompleted, getTodayVocabCount, getVocabStats } from '../services/progress'
import { SESSION_SIZE } from '../services/vocabSelection'

/**
 * ホーム。次に学習すべきものを明確に示すシンプルなダッシュボード。
 *
 * 件数と次のセクションは生成済みサマリー(数KB)から取る。教材データ本体を import すると
 * カウンタ2つのために文法・語彙の全チャンク(gzip 約700KB)がトップページに乗るため。
 */
export function Dashboard() {
  // 英文法ページは一時的に非公開。再開するときは以下の集計とカードを戻す。
  // const completed = getCompletedLessons()
  // const totalLessons = grammarLessonSummaries.length
  // const completedCount = grammarLessonSummaries.filter((l) => completed.has(l.id)).length
  // const nextGrammar = grammarLessonSummaries.find((l) => !completed.has(l.id))

  // 3分間Englishは英文法の全セクションを1話ずつ扱うため、件数は文法サマリーと同じ。
  const threeMinuteCount = grammarLessonSummaries.length
  const threeMinuteCompleted = getThreeMinuteCompleted()
  const threeMinuteDone = grammarLessonSummaries.filter((lesson) => threeMinuteCompleted.has(lesson.id)).length

  const stats = getVocabStats()
  const statEntries = Object.values(stats)
  const studiedWords = statEntries.length
  const difficultWords = statEntries.filter((s) => s.unknown > s.known).length
  const todayCount = getTodayVocabCount()

  return (
    <div className="page dashboard">
      <h1>ホーム</h1>
      <p className="page-lead">B2まで、短いセクションを積み重ねて学習しましょう。</p>

      <IngbirdCard />

      <div className="dash-grid">
        <Link to="/three-minute" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="three-minute" /></span>3分間English</h2>
          <p className="dash-stat">{threeMinuteDone} / {threeMinuteCount}話 完了</p>
          <div
            className="progress-bar"
            role="progressbar"
            aria-valuenow={threeMinuteDone}
            aria-valuemin={0}
            aria-valuemax={threeMinuteCount}
            aria-label="3分間Englishの進捗"
          >
            <div
              className="progress-fill"
              style={{ width: threeMinuteCount ? `${(threeMinuteDone / threeMinuteCount) * 100}%` : '0%' }}
            />
          </div>
          <p className="dash-next">
            イングバード先生とヒヨコ君の会話で、英文法を1話3分ほどで学び直せます。各話の最後に4択の確認問題つき。
          </p>
        </Link>

        {/* 英文法ページは一時的に非公開。再開するときはこのカードを戻す。
        <Link to="/grammar" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="grammar" /></span>英文法</h2>
          <p className="dash-stat">
            {completedCount} / {totalLessons} セクション完了
          </p>
          <div className="progress-bar" role="progressbar" aria-valuenow={completedCount} aria-valuemin={0} aria-valuemax={totalLessons} aria-label="文法の進捗">
            <div className="progress-fill" style={{ width: totalLessons ? `${(completedCount / totalLessons) * 100}%` : '0%' }} />
          </div>
          {nextGrammar ? (
            <p className="dash-next">
              次のセクション: <strong>{nextGrammar.title}</strong>
              <span className="dash-duration">（{nextGrammar.minutes}分）</span>
            </p>
          ) : (
            <p className="dash-next">すべてのセクションを完了しました!</p>
          )}
        </Link>
        */}

        <Link to="/vocabulary" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="vocabulary" /></span>英単語</h2>
          <p className="dash-stat">今日の練習: {todayCount}語</p>
          <ul className="dash-list">
            <li>学習済み: {studiedWords} / {vocabularyCount}語</li>
            <li>苦手な単語: {difficultWords}語</li>
          </ul>
          <p className="dash-next">{SESSION_SIZE}語のクイズでボキャブラリーを増やしましょう。</p>
        </Link>

        <Link to="/practice" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="practice" /></span>音声練習</h2>
          <p className="dash-next">
            音読・シャドーイングとディクテーション。学んだ英文を、聞く・声に出すで仕上げます。
          </p>
        </Link>

        <Link to="/reading" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="reading" /></span>多読</h2>
          <p className="dash-stat">{readingPassageCount}本</p>
          <p className="dash-next">段落ごとの音声と和訳つき。読んだあとに内容理解を確認します。</p>
        </Link>

        <Link to="/pronunciation" className="dash-card">
          <h2><span className="dash-title-icon"><LearningIcon kind="pronunciation" /></span>発音記号</h2>
          <p className="dash-next">発音記号と日本人が苦手な音のリファレンス。音声付きでいつでも確認できます。</p>
        </Link>
      </div>

      <p className="dash-settings-link">
        端末間の同期と進捗のリセットは<Link to="/settings">設定</Link>から行えます。
      </p>
    </div>
  )
}
