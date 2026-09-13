import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { DEFAULT_LOCALE, DEFAULT_VOLUME, NORMAL_RATE, SLOW_RATE, speechService } from './speech'

// Web Speech API のモック
class FakeUtterance {
  text: string
  lang = ''
  rate = 1
  volume = 1
  voice: unknown = null
  onend: (() => void) | null = null
  onerror: (() => void) | null = null
  constructor(text: string) {
    this.text = text
  }
}

const speakMock = vi.fn()
const cancelMock = vi.fn()
const resumeMock = vi.fn()

beforeEach(() => {
  speakMock.mockReset()
  cancelMock.mockReset()
  resumeMock.mockReset()
  vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance)
  Object.defineProperty(window, 'speechSynthesis', {
    configurable: true,
    value: {
      speak: speakMock,
      cancel: cancelMock,
      resume: resumeMock,
      getVoices: () => [],
    },
  })
})

afterEach(() => {
  vi.unstubAllGlobals()
  // @ts-expect-error テスト用に注入したモックを除去
  delete window.speechSynthesis
})

describe('speechService', () => {
  it('開始キューと英文を一つの発話として TTS に渡す', async () => {
    const promise = speechService.speak('I have lived here for five years.')
    const utterance = speakMock.mock.calls[0][0] as FakeUtterance
    expect(speakMock).toHaveBeenCalledTimes(1)
    expect(utterance.text).toBe('Ready. I have lived here for five years.')
    expect(utterance.lang).toBe(DEFAULT_LOCALE)
    expect(utterance.rate).toBe(NORMAL_RATE)
    expect(utterance.volume).toBe(DEFAULT_VOLUME)
    expect(cancelMock).toHaveBeenCalledTimes(1)
    expect(resumeMock).toHaveBeenCalledTimes(1)
    utterance.onend?.()
    await promise
  })

  it('スロー再生は SLOW_RATE を使う', async () => {
    const promise = speechService.speak('Hello.', { rate: SLOW_RATE })
    const utterance = speakMock.mock.calls[0][0] as FakeUtterance
    expect(utterance.rate).toBe(SLOW_RATE)
    utterance.onend?.()
    await promise
  })

  it('先頭保護を指定すると開始キューと教材英文を同じ発話にする', async () => {
    const promise = speechService.speak('I am a student.', { leadingPause: true })
    const utterance = speakMock.mock.calls[0][0] as FakeUtterance
    expect(speakMock).toHaveBeenCalledTimes(1)
    expect(utterance.text).toBe('Ready. I am a student.')
    utterance.onend?.()
    await promise
  })

  it('音量は Web Speech API の有効範囲に収める', async () => {
    const promise = speechService.speak('Louder.', { volume: 1.3 })
    const utterance = speakMock.mock.calls[0][0] as FakeUtterance
    expect(utterance.volume).toBe(1)
    utterance.onend?.()
    await promise
  })

  it('新しい再生を開始すると既存の再生をキャンセルする', async () => {
    const first = speechService.speak('First sentence.')
    const firstUtterance = speakMock.mock.calls[0][0] as FakeUtterance
    const second = speechService.speak('Second sentence.')
    expect(cancelMock).toHaveBeenCalled()
    firstUtterance.onend?.()
    const secondUtterance = speakMock.mock.calls[1][0] as FakeUtterance
    secondUtterance.onend?.()
    await Promise.all([first, second])
  })

  it('stop で再生中の音声をキャンセルする', async () => {
    const playback = speechService.speak('Please stop this sentence.')
    speechService.stop()
    expect(cancelMock).toHaveBeenCalled()
    await playback
  })

  it('stop でブラウザの end イベントがなくても再生 Promise を完了する', async () => {
    const playback = speechService.speak('Please stop this sentence.')
    speechService.stop()
    await expect(playback).resolves.toBeUndefined()
  })

  it('TTS 非対応環境では何もせず resolve する(壊れない)', async () => {
    // @ts-expect-error 非対応環境を再現
    delete window.speechSynthesis
    await expect(speechService.speak('Hello.')).resolves.toBeUndefined()
    expect(speakMock).not.toHaveBeenCalled()
  })
})
