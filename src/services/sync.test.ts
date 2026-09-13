import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { pull, push, signOut } from './sync'

const FILE = 'english-progress.json'

function gistResponse(snapshot: unknown) {
  return { ok: true, json: async () => ({ files: { [FILE]: { content: JSON.stringify(snapshot) } } }) }
}

function signedInFixture() {
  localStorage.setItem('eng.sync.token', 'ghp_test')
  localStorage.setItem('eng.sync.gist', 'gist123')
}

beforeEach(() => {
  localStorage.clear()
  sessionStorage.clear()
})

afterEach(() => {
  vi.unstubAllGlobals()
})

describe('端末間同期', () => {
  it('リモートが新しければ取り込み、同期設定キーは触らない', async () => {
    signedInFixture()
    localStorage.setItem('eng.grammar.completed', '["old"]')
    vi.stubGlobal('fetch', vi.fn(async () => gistResponse({ savedAt: 100, data: { 'eng.grammar.completed': '["new"]' } })))

    await pull()

    expect(localStorage.getItem('eng.grammar.completed')).toBe('["new"]')
    expect(localStorage.getItem('eng.sync.token')).toBe('ghp_test')
    expect(localStorage.getItem('eng.sync.savedAt')).toBe('100')
  })

  it('リモートが古ければローカルを残す', async () => {
    signedInFixture()
    localStorage.setItem('eng.sync.savedAt', '200')
    localStorage.setItem('eng.grammar.completed', '["local"]')
    vi.stubGlobal('fetch', vi.fn(async () => gistResponse({ savedAt: 100, data: { 'eng.grammar.completed': '["remote"]' } })))

    await pull()

    expect(localStorage.getItem('eng.grammar.completed')).toBe('["local"]')
  })

  it('pull に成功するまで push しない(古い端末が新しい進捗を消さない)', async () => {
    signedInFixture()
    const fetchMock = vi.fn(async () => ({ ok: false, status: 500, json: async () => ({}) }))
    vi.stubGlobal('fetch', fetchMock)

    await expect(pull()).rejects.toThrow()
    await push()

    expect(fetchMock).toHaveBeenCalledTimes(1) // push は送っていない
  })

  it('pull 後の push は進捗キーだけを送る', async () => {
    signedInFixture()
    localStorage.setItem('eng.sync.savedAt', '999') // リモートは古い = 取り込みなし
    localStorage.setItem('eng.vocab.stats', '{"a":1}')
    localStorage.setItem('eng.practice.stats.dictation', '{"b":2}')
    let sentBody = ''
    vi.stubGlobal(
      'fetch',
      vi.fn(async (_url: string, init?: RequestInit) => {
        if (init?.method === 'PATCH') sentBody = String(init.body)
        return gistResponse({ savedAt: 1, data: {} })
      }),
    )

    await pull()
    await push()

    const sent = JSON.parse(JSON.parse(sentBody).files[FILE].content).data
    expect(Object.keys(sent).sort()).toEqual(['eng.practice.stats.dictation', 'eng.vocab.stats'])
  })

  it('サインアウトすると同期は止まる', async () => {
    signedInFixture()
    signOut()
    const fetchMock = vi.fn()
    vi.stubGlobal('fetch', fetchMock)

    await pull()
    await push()

    expect(fetchMock).not.toHaveBeenCalled()
  })
})
