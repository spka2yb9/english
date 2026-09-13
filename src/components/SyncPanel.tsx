import { useState } from 'react'
import { push, signedIn, signIn, signOut } from '../services/sync'

const TOKEN_URL = 'https://github.com/settings/tokens/new?scopes=gist&description=English%20A2-B2'

/** 端末間で進捗を同期するための1人用サインイン。保存先は自分の private Gist。 */
export function SyncPanel() {
  const [token, setToken] = useState('')
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [done, setDone] = useState('')

  async function run(action: () => Promise<void>, reload: boolean, message = '') {
    setBusy(true)
    setError('')
    setDone('')
    try {
      await action()
      // ponytail: 画面全体が localStorage を読み直す一番短い手段。状態を配り回すなら useSyncExternalStore へ
      if (reload) location.reload()
      else setDone(message)
    } catch (e) {
      setError(e instanceof Error ? e.message : '同期に失敗しました')
    } finally {
      setBusy(false)
    }
  }

  return (
    <section className="sync-panel" aria-labelledby="sync-heading">
      <h2 id="sync-heading">端末間の同期</h2>
      {signedIn() ? (
        <>
          <p>この端末の進捗は、あなたの private Gist に自動保存されています。</p>
          <div className="sync-actions">
            <button type="button" className="btn-primary" disabled={busy} onClick={() => void run(push, false, '同期しました')}>
              今すぐ同期
            </button>
            <button type="button" className="btn-secondary" disabled={busy} onClick={() => void run(async () => signOut(), true)}>
              サインアウト
            </button>
          </div>
        </>
      ) : (
        <form
          onSubmit={(e) => {
            e.preventDefault()
            void run(() => signIn(token), true)
          }}
        >
          <p>
            GitHub の <code>gist</code> スコープだけのトークンを貼ると、複数の端末で進捗を共有できます。
            <a href={TOKEN_URL} target="_blank" rel="noreferrer">
              トークンを作る
            </a>
          </p>
          <label className="practice-input-label">
            Personal Access Token
            <input
              className="practice-input"
              type="password"
              autoComplete="off"
              value={token}
              onChange={(e) => setToken(e.target.value)}
              placeholder="ghp_..."
            />
          </label>
          <p className="sync-warning">
            保存済みの進捗がある場合、この端末の進捗はそちらで上書きされます。
          </p>
          <button type="submit" className="btn-primary" disabled={busy}>
            {busy ? '接続中…' : '同期を有効にする'}
          </button>
        </form>
      )}
      {error !== '' && <p className="sync-error" role="alert">{error}</p>}
      {done !== '' && <p role="status">{done}</p>}
    </section>
  )
}
