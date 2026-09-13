// 1人用の端末間同期。保存先は自分の private Gist なのでサーバもDBも要らず、月額0円。
// 「ログイン」= gist スコープの Personal Access Token を1回貼るだけ。

const API = 'https://api.github.com/gists'
const FILE = 'english-progress.json'
const DATA_PREFIX = 'eng.' // 進捗キーの接頭辞。KEYS を列挙しないので音声練習の動的キーも自動で乗る
const SYNC_PREFIX = 'eng.sync.' // 同期の設定自体は同期しない
const TOKEN_KEY = 'eng.sync.token'
const GIST_KEY = 'eng.sync.gist'
const STAMP_KEY = 'eng.sync.savedAt'
const PULLED_KEY = 'eng.sync.pulled' // sessionStorage: このタブで pull 済みか
const PUSH_DELAY_MS = 3000

type Snapshot = { savedAt: number; data: Record<string, string> }

const token = () => localStorage.getItem(TOKEN_KEY) ?? ''
const gistId = () => localStorage.getItem(GIST_KEY) ?? ''
const stamp = () => Number(localStorage.getItem(STAMP_KEY) ?? 0)

export function signedIn(): boolean {
  return token() !== '' && gistId() !== ''
}

function headers(pat: string = token()): Record<string, string> {
  return {
    Authorization: `Bearer ${pat}`,
    Accept: 'application/vnd.github+json',
    'Content-Type': 'application/json',
  }
}

/**
 * 進捗データのキー一覧。`KEYS` を列挙せず接頭辞で拾うので、音声練習の動的キー
 * (`eng.practice.stats.<mode>`)も自動で入る。同期の設定自体(`eng.sync.*`)は除く。
 */
export function progressKeys(): string[] {
  const keys: string[] = []
  for (let i = 0; i < localStorage.length; i += 1) {
    const key = localStorage.key(i)
    if (key === null || !key.startsWith(DATA_PREFIX) || key.startsWith(SYNC_PREFIX)) continue
    keys.push(key)
  }
  return keys
}

function snapshot(): Snapshot {
  const data: Record<string, string> = {}
  for (const key of progressKeys()) data[key] = localStorage.getItem(key) ?? ''
  return { savedAt: Date.now(), data }
}

function apply(remote: Snapshot): void {
  for (const key of progressKeys()) localStorage.removeItem(key)
  for (const [key, value] of Object.entries(remote.data)) localStorage.setItem(key, value)
  localStorage.setItem(STAMP_KEY, String(remote.savedAt))
}

/** 起動時に1回。取得に成功するまで push しない — 古い端末が新しい進捗を消さないため。 */
export async function pull(): Promise<void> {
  if (!signedIn()) return
  const res = await fetch(`${API}/${gistId()}`, { headers: headers(), signal: AbortSignal.timeout(10_000) })
  if (!res.ok) throw new Error(`進捗の取得に失敗しました (${res.status})`)
  // ponytail: 1MB超のファイルは content が切り詰められ JSON.parse が失敗する(push はしないので消えはしない)。
  // 進捗がその規模になったら truncated/raw_url を見て取り直す
  const body = (await res.json()) as { files?: Record<string, { content?: string }> }
  const content = body.files?.[FILE]?.content
  const remote = content ? (JSON.parse(content) as Partial<Snapshot>) : undefined
  if (remote?.savedAt !== undefined && remote.data !== undefined && remote.savedAt > stamp()) {
    apply({ savedAt: remote.savedAt, data: remote.data })
  }
  sessionStorage.setItem(PULLED_KEY, '1')
}

export async function push(): Promise<void> {
  if (!signedIn() || sessionStorage.getItem(PULLED_KEY) !== '1') return
  const current = snapshot()
  const res = await fetch(`${API}/${gistId()}`, {
    method: 'PATCH',
    headers: headers(),
    body: JSON.stringify({ files: { [FILE]: { content: JSON.stringify(current) } } }),
  })
  if (!res.ok) throw new Error(`進捗の保存に失敗しました (${res.status})`)
  localStorage.setItem(STAMP_KEY, String(current.savedAt))
}

let timer: ReturnType<typeof setTimeout> | undefined

/** saveJson から呼ばれる。連続保存はまとめて1回だけ送る。 */
export function schedulePush(): void {
  if (!signedIn()) return
  clearTimeout(timer)
  timer = setTimeout(() => {
    timer = undefined
    void push().catch(() => {})
  }, PUSH_DELAY_MS)
}

// タブを離れる時に未送信分を取りこぼさない
if (typeof document !== 'undefined') {
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState !== 'hidden' || timer === undefined) return
    clearTimeout(timer)
    timer = undefined
    void push().catch(() => {})
  })
}

/** サインイン。既存の保存先 Gist があれば再利用し、無ければ private Gist を作る。 */
export async function signIn(pat: string): Promise<void> {
  const trimmed = pat.trim()
  if (trimmed === '') throw new Error('トークンを入力してください')
  // ponytail: 直近100件から探す。Gistが100件を超えたらページングか説明文での絞り込みを足す
  const list = await fetch(`${API}?per_page=100`, { headers: headers(trimmed) })
  if (!list.ok) {
    throw new Error(list.status === 401 ? 'トークンが無効です' : `GitHubに接続できません (${list.status})`)
  }
  const gists = (await list.json()) as { id: string; files?: Record<string, unknown> }[]
  let id = gists.find((gist) => gist.files?.[FILE] !== undefined)?.id
  if (id === undefined) {
    const created = await fetch(API, {
      method: 'POST',
      headers: headers(trimmed),
      body: JSON.stringify({
        description: 'English A2→B2 の学習進捗',
        public: false,
        files: { [FILE]: { content: '{}' } },
      }),
    })
    if (!created.ok) throw new Error(`保存先の作成に失敗しました (${created.status})`)
    id = ((await created.json()) as { id: string }).id
  }
  localStorage.setItem(TOKEN_KEY, trimmed)
  localStorage.setItem(GIST_KEY, id)
  await pull()
}

export function signOut(): void {
  for (const key of [TOKEN_KEY, GIST_KEY, STAMP_KEY]) localStorage.removeItem(key)
  sessionStorage.removeItem(PULLED_KEY)
}
