import { lazy, Suspense } from 'react'
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import './App.css'
import { Layout } from './components/Layout'

const Dashboard = lazy(() => import('./pages/Dashboard').then((module) => ({ default: module.Dashboard })))
const Pronunciation = lazy(() => import('./pages/Pronunciation').then((module) => ({ default: module.Pronunciation })))
// 英文法ページは一時的に非公開。再開するときは以下の3つの import を戻す。
// const GrammarIndex = lazy(() => import('./pages/GrammarIndex').then((module) => ({ default: module.GrammarIndex })))
// const GrammarRoadmapPage = lazy(() =>
//   import('./pages/GrammarRoadmapPage').then((module) => ({ default: module.GrammarRoadmapPage })),
// )
// const GrammarLessonPage = lazy(() =>
//   import('./pages/GrammarLesson').then((module) => ({ default: module.GrammarLessonPage })),
// )
const ThreeMinuteIndex = lazy(() =>
  import('./pages/ThreeMinuteIndex').then((module) => ({ default: module.ThreeMinuteIndex })),
)
const ThreeMinuteLessonPage = lazy(() =>
  import('./pages/ThreeMinuteLesson').then((module) => ({ default: module.ThreeMinuteLessonPage })),
)
const Vocabulary = lazy(() => import('./pages/Vocabulary').then((module) => ({ default: module.Vocabulary })))
const Practice = lazy(() => import('./pages/Practice').then((module) => ({ default: module.Practice })))
const ReadingIndex = lazy(() => import('./pages/Reading').then((module) => ({ default: module.ReadingIndex })))
const ReadingPassagePage = lazy(() =>
  import('./pages/Reading').then((module) => ({ default: module.ReadingPassagePage })),
)
const Settings = lazy(() => import('./pages/Settings').then((module) => ({ default: module.Settings })))

function PageLoader() {
  return (
    <div className="page page-loading" role="status">
      <span className="loading-dot" aria-hidden="true" />
      教材を読み込んでいます…
    </div>
  )
}

function NotFound() {
  return (
    <div className="page empty-state">
      <p className="eyebrow">404</p>
      <h1>ページが見つかりません</h1>
      <p>URLを確認するか、ホームから学習を続けてください。</p>
      <Link className="btn-primary" to="/">
        ホームへ戻る
      </Link>
    </div>
  )
}

// basename: サブパス配信(https://owner.github.io/repo/)でもルーティングを合わせる
function App() {
  return (
    <BrowserRouter basename={import.meta.env.BASE_URL}>
      <Suspense fallback={<PageLoader />}>
        <Routes>
          <Route element={<Layout />}>
            <Route index element={<Dashboard />} />
            <Route path="pronunciation" element={<Pronunciation />} />
            {/* 英文法ページは一時的に非公開。再開するときはこの3ルートを戻す。
            <Route path="grammar" element={<GrammarIndex />} />
            <Route path="grammar/roadmap" element={<GrammarRoadmapPage />} />
            <Route path="grammar/:lessonId" element={<GrammarLessonPage />} />
            */}
            <Route path="three-minute" element={<ThreeMinuteIndex />} />
            <Route path="three-minute/:lessonId" element={<ThreeMinuteLessonPage />} />
            <Route path="vocabulary" element={<Vocabulary />} />
            <Route path="practice" element={<Practice />} />
            <Route path="reading" element={<ReadingIndex />} />
            <Route path="reading/:passageId" element={<ReadingPassagePage />} />
            <Route path="settings" element={<Settings />} />
            <Route path="*" element={<NotFound />} />
          </Route>
        </Routes>
      </Suspense>
    </BrowserRouter>
  )
}

export default App
