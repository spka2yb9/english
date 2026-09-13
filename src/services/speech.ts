// 音声合成の抽象層。UIとコンテンツからTTS実装を分離する。
// 現在の実装は Web Speech API。将来クラウドTTSや事前生成音声に差し替え可能。

export type SpeechOptions = {
  locale?: string
  rate?: number
  volume?: number
  /** 同じ発話内に短い開始キューを置き、教材英文の先頭が欠けるのを防ぐ。 */
  leadingPause?: boolean
}

export interface SpeechService {
  isSupported(): boolean
  /** 再生開始。既存の再生は停止する。終了(またはキャンセル)時に resolve。 */
  speak(text: string, options?: SpeechOptions): Promise<void>
  stop(): void
}

export const DEFAULT_LOCALE = 'en-US'
export const NORMAL_RATE = 1.0
export const SLOW_RATE = 0.5
// SpeechSynthesisUtterance の音量範囲は 0.0〜1.0。常に上限で再生する。
export const DEFAULT_VOLUME = 1.0

const LEADING_CUE_TEXT = 'Ready. '

class WebSpeechService implements SpeechService {
  private current: { utterance: SpeechSynthesisUtterance; finish: () => void } | null = null

  isSupported(): boolean {
    return (
      typeof window !== 'undefined' &&
      'speechSynthesis' in window &&
      typeof SpeechSynthesisUtterance !== 'undefined'
    )
  }

  private pickVoice(locale: string): SpeechSynthesisVoice | null {
    const voices = window.speechSynthesis.getVoices()
    return (
      voices.find((v) => v.lang === locale && v.localService) ??
      voices.find((v) => v.lang === locale) ??
      voices.find((v) => v.lang.replace('_', '-').startsWith(locale.split('-')[0])) ??
      null
    )
  }

  speak(text: string, options: SpeechOptions = {}): Promise<void> {
    if (!this.isSupported()) return Promise.resolve()
    const {
      locale = DEFAULT_LOCALE,
      rate = NORMAL_RATE,
      volume = DEFAULT_VOLUME,
      leadingPause = true,
    } = options
    // ページ間で残ったキューや一時停止状態を毎回リセットする。
    // 直後の冒頭が欠けても開始キュー側だけになるため、教材本文は保護される。
    this.stop()
    return new Promise((resolve) => {
      // 開始キューと教材本文を一つの発話にする。発話間で出力経路が
      // 閉じる環境でも、欠ける可能性があるのは開始キュー側だけになる。
      const utterance = new SpeechSynthesisUtterance(leadingPause ? `${LEADING_CUE_TEXT}${text}` : text)
      utterance.lang = locale
      utterance.rate = rate
      utterance.volume = Math.min(1, Math.max(0, volume))
      const voice = this.pickVoice(locale)
      if (voice) utterance.voice = voice

      let settled = false
      const finish = () => {
        if (settled) return
        settled = true
        if (this.current?.utterance === utterance) this.current = null
        resolve()
      }
      utterance.onend = finish
      utterance.onerror = finish
      this.current = { utterance, finish }
      window.speechSynthesis.resume()
      window.speechSynthesis.speak(utterance)
    })
  }

  stop(): void {
    const current = this.current
    this.current = null
    if (this.isSupported()) window.speechSynthesis.cancel()
    // ブラウザによって cancel() 後に end/error が発火しないため、
    // 待機中の UI を必ず idle に戻す。
    current?.finish()
  }
}

export const speechService: SpeechService = new WebSpeechService()
