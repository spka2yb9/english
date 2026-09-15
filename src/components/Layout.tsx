import { useEffect, useState } from 'react'
import { Link, NavLink, Outlet, useLocation } from 'react-router-dom'
import { LearningIcon } from './LearningIcon'

const NAV_ITEMS = [
  { to: '/', label: 'ホーム', icon: 'home' },
  { to: '/pronunciation', label: '発音記号', icon: 'pronunciation' },
  { to: '/grammar', label: '英文法', icon: 'grammar' },
  { to: '/vocabulary', label: '英単語', icon: 'vocabulary' },
  { to: '/practice', label: '音声練習', icon: 'practice' },
  { to: '/reading', label: '多読', icon: 'reading' },
  { to: '/settings', label: '設定', icon: 'settings' },
] as const

/** レスポンシブレイアウト。デスクトップ: 固定サイドバー / モバイル: トップバー + ドロワー */
export function Layout() {
  const [drawerOpen, setDrawerOpen] = useState(false)
  const { pathname } = useLocation()

  useEffect(() => {
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' })
  }, [pathname])

  // ドロワー表示中は Escape で閉じる
  useEffect(() => {
    if (!drawerOpen) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setDrawerOpen(false)
    }
    const previousOverflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    window.addEventListener('keydown', onKey)
    return () => {
      document.body.style.overflow = previousOverflow
      window.removeEventListener('keydown', onKey)
    }
  }, [drawerOpen])

  return (
    <div className="layout">
      <a className="skip-link" href="#main-content">
        本文へ移動
      </a>
      <header className="topbar">
        <button
          type="button"
          className="menu-btn"
          onClick={() => setDrawerOpen(!drawerOpen)}
          aria-label={drawerOpen ? 'メニューを閉じる' : 'メニューを開く'}
          aria-expanded={drawerOpen}
        >
          <span aria-hidden="true">☰</span>
        </button>
        <Link className="topbar-title" to="/" onClick={() => setDrawerOpen(false)}>
          English Reach B2
        </Link>
      </header>

      {drawerOpen && <div className="drawer-backdrop" onClick={() => setDrawerOpen(false)} aria-hidden="true" />}

      <nav className={`sidebar${drawerOpen ? ' open' : ''}`} aria-label="メインナビゲーション">
        <Link className="sidebar-brand" to="/" onClick={() => setDrawerOpen(false)}>
          <span className="sidebar-logo" aria-hidden="true">
            <LearningIcon kind="grammar" size={25} />
          </span>
          <span>
            English
            <br />
            <small>Reach B2</small>
          </span>
        </Link>
        <ul>
          {NAV_ITEMS.map((item) => (
            <li key={item.to}>
              <NavLink
                to={item.to}
                end={item.to === '/'}
                className={({ isActive }) => (isActive ? 'active' : '')}
                onClick={() => setDrawerOpen(false)}
              >
                <span aria-hidden="true" className="nav-icon">
                  <LearningIcon kind={item.icon} size={21} />
                </span>
                {item.label}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>

      <main className="main" id="main-content" tabIndex={-1}>
        <Outlet />
      </main>
    </div>
  )
}
