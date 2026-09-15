import { useEffect, useRef, useState } from 'react'
import { SyncPanel } from '../components/SyncPanel'
import { getCompletedLessons, getGrammarItemStats, getVocabHistory, getVocabStats } from '../services/progress'
import { KEYS, loadJson, resetProgress } from '../services/storage'
import { push, signedIn } from '../services/sync'

/**
 * リセットの単位は学習エリアごとの4つ。それぞれが localStorage に持つキーをまとめて消す。
 * 件数は localStorage だけから数え、教材データは読み込まない(音声練習も practice.ts 経由では数えない —
 * 文バンクを設定ページのチャンクに持ち込んでしまうため)。
 */
function savedGroups() {
  const recorded = (key: string) => Object.keys(loadJson<Record<string, unknown>>(key, {})).length
  const lessons = getCompletedLessons().size
  const items = Object.keys(getGrammarItemStats()).length
  const words = Object.keys(getVocabStats()).length
  const days = getVocabHistory().length
  const sentences = recorded(`${KEYS.practiceStats}.shadowing`) + recorded(`${KEYS.practiceStats}.dictation`)
  const passages = loadJson<string[]>(KEYS.readingDone, []).length
  return [
    {
      id: 'grammar',
      label: '文法',
      prefixes: [KEYS.grammarProgress, KEYS.grammarItemStats],
      count: lessons + items,
      detail: `完了 ${lessons}セクション・正誤を記録した ${items}問`,
    },
    {
      id: 'vocab',
      label: '単語',
      prefixes: [KEYS.vocabStats, KEYS.vocabDaily],
      count: words + days,
      detail: `学習履歴のある ${words}語・学習ログ ${days}日`,
    },
    {
      id: 'practice',
      label: '音声練習',
      prefixes: [KEYS.practiceStats],
      count: sentences,
      detail: `実施した ${sentences}文`,
    },
    {
      id: 'reading',
      label: '多読',
      prefixes: [KEYS.readingDone],
      count: passages,
      detail: `読了した ${passages}本`,
    },
  ]
}

export function Settings() {
  const dialogRef = useRef<HTMLDialogElement>(null)
  const [open, setOpen] = useState(false)
  const [busy, setBusy] = useState(false)
  const [groups, setGroups] = useState(savedGroups)
  const [selected, setSelected] = useState<string[]>([])

  // showModal() でないと Escape・フォーカストラップ・::backdrop が効かない。
  useEffect(() => {
    const dialog = dialogRef.current
    if (!dialog) return
    if (open && !dialog.open) dialog.showModal()
    if (!open && dialog.open) dialog.close()
  }, [open])

  const total = groups.reduce((sum, group) => sum + group.count, 0)
  const chosen = groups.filter((group) => selected.includes(group.id) && group.count > 0)

  const toggle = (id: string) =>
    setSelected((ids) => (ids.includes(id) ? ids.filter((x) => x !== id) : [...ids, id]))

  const confirmReset = async () => {
    setBusy(true)
    resetProgress(chosen.flatMap((group) => group.prefixes))
    // 同期がオンなら、リロードで保留中の push が消える前に空の状態を送っておく。
    if (signedIn()) await push().catch(() => {})
    // 他のページが持っている進捗の表示も一緒に作り直す。SyncPanel と同じ方針。
    location.reload()
  }

  return (
    <div className="page">
      <h1>設定</h1>
      <p className="page-lead">同期の設定と、この端末に保存された学習進捗の管理を行います。</p>

      <SyncPanel />

      <section className="sync-panel danger-panel" aria-labelledby="reset-heading">
        <h2 id="reset-heading">進捗のリセット</h2>
        <p>
          消したい学習エリアを選んで、この端末に保存された進捗を初期状態に戻します。選ばなかったエリアの進捗と、
          教材そのものは残ります。
        </p>
        <ul className="reset-counts">
          {groups.map((group) => (
            <li key={group.id}>
              <label className="reset-choice">
                <input
                  type="checkbox"
                  checked={selected.includes(group.id)}
                  disabled={group.count === 0}
                  onChange={() => toggle(group.id)}
                />
                <span>{group.label}</span>
              </label>
              <strong>{group.count === 0 ? '記録なし' : group.detail}</strong>
            </li>
          ))}
        </ul>
        {total === 0 ? (
          <p className="sync-warning">まだ保存された進捗はありません。</p>
        ) : (
          <button
            type="button"
            className="btn-danger"
            disabled={chosen.length === 0}
            onClick={() => {
              setGroups(savedGroups())
              setOpen(true)
            }}
          >
            選んだ進捗をリセットする
          </button>
        )}
      </section>

      <dialog
        ref={dialogRef}
        className="confirm-dialog"
        aria-labelledby="reset-dialog-title"
        // Escape や backdrop で閉じたときも React 側の状態を合わせる
        onClose={() => setOpen(false)}
        onCancel={(e) => {
          if (busy) e.preventDefault()
        }}
      >
        <h2 id="reset-dialog-title">選んだ進捗をリセットしますか?</h2>
        <p>
          次の記録がすべて消えます。<strong>この操作は取り消せません。</strong>
        </p>
        <ul className="reset-counts">
          {chosen.map((group) => (
            <li key={group.id}>
              <span>{group.label}</span>
              <strong>{group.detail}</strong>
            </li>
          ))}
        </ul>
        {signedIn() && (
          <p className="sync-warning">
            同期が有効なため、Gist に保存された進捗も同じように消えます。ほかの端末にも反映されます。
          </p>
        )}
        <div className="sync-actions">
          <button type="button" className="btn-secondary" disabled={busy} onClick={() => setOpen(false)}>
            キャンセル
          </button>
          <button type="button" className="btn-danger" disabled={busy} onClick={() => void confirmReset()}>
            {busy ? 'リセット中…' : 'リセットする'}
          </button>
        </div>
      </dialog>
    </div>
  )
}
