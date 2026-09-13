type IconKind =
  | 'home'
  | 'pronunciation'
  | 'grammar'
  | 'vocabulary'
  | 'practice'
  | 'reading'
  | 'settings'

export function LearningIcon({ kind, size = 22 }: { kind: IconKind; size?: number }) {
  return (
    <svg
      aria-hidden="true"
      className={`learning-icon learning-icon-${kind}`}
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
    >
      {kind === 'home' && (
        <>
          <path d="M3.5 10.7 12 3.8l8.5 6.9" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
          <path d="M5.7 9.6v10.1h12.6V9.6M9.5 19.7v-6h5v6" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" />
        </>
      )}
      {kind === 'pronunciation' && (
        <>
          <rect x="8.2" y="3.2" width="7.6" height="11.5" rx="3.8" stroke="currentColor" strokeWidth="1.8" />
          <path d="M5.8 11.6a6.2 6.2 0 0 0 12.4 0M12 17.8v3M8.8 20.8h6.4" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
        </>
      )}
      {kind === 'grammar' && (
        <path d="M4.3 4.2h5.4A2.3 2.3 0 0 1 12 6.5v13a2.3 2.3 0 0 0-2.3-2.3H4.3zM19.7 4.2h-5.4A2.3 2.3 0 0 0 12 6.5v13a2.3 2.3 0 0 1 2.3-2.3h5.4z" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round" />
      )}
      {kind === 'vocabulary' && (
        <>
          <rect x="4" y="5" width="16" height="14" rx="2" stroke="currentColor" strokeWidth="1.8" />
          <path d="m8 15 2.7-6h.6l2.7 6M9 13h4M16.5 9.5v5M15.2 12.8l1.3 1.7 1.3-1.7" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
        </>
      )}
      {kind === 'practice' && (
        <>
          <path d="M4.5 12.5 9 17l10.5-10.5" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
          <path d="M4.5 6.5 7 9" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
        </>
      )}
      {kind === 'reading' && (
        <>
          <path d="M3.5 5.5h6a2.5 2.5 0 0 1 2.5 2.5v10a2 2 0 0 0-2-2h-6.5zM20.5 5.5h-6A2.5 2.5 0 0 0 12 8v10a2 2 0 0 1 2-2h6.5z" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
        </>
      )}
      {kind === 'settings' && (
        <>
          <circle cx="12" cy="12" r="3.1" stroke="currentColor" strokeWidth="1.8" />
          <path d="M12 2.9v2.4M12 18.7v2.4M21.1 12h-2.4M5.3 12H2.9M18.4 5.6l-1.7 1.7M7.3 16.7l-1.7 1.7M18.4 18.4l-1.7-1.7M7.3 7.3 5.6 5.6" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
        </>
      )}
    </svg>
  )
}
