import { lazy, Suspense } from 'react'
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom'
import './App.css'
import { Layout } from './components/Layout'

const Dashboard = lazy(() => import('./pages/Dashboard').then((module) => ({ default: module.Dashboard })))
const Pronunciation = lazy(() => import('./pages/Pronunciation').then((module) => ({ default: module.Pronunciation })))
const GrammarIndex = lazy(() => import('./pages/GrammarIndex').then((module) => ({ default: module.GrammarIndex })))
const GrammarLessonPage = lazy(() =>
  import('./pages/GrammarLesson').then((module) => ({ default: module.GrammarLessonPage })),
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
            <Route path="grammar" element={<GrammarIndex />} />
            <Route path="grammar/:lessonId" element={<GrammarLessonPage />} />
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
