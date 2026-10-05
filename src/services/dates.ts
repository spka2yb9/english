// YYYY-MM-DD(端末のローカル日付)の計算。語彙の日次ログ・学習日・グラフの横軸が共有する。

export function dateString(d: Date): string {
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`
}

export function todayString(): string {
  return dateString(new Date())
}

/** YYYY-MM-DD を days 日ずらす。月末・うるう年は Date に任せる。 */
export function shiftDate(date: string, days: number): string {
  const d = new Date(`${date}T00:00:00`)
  d.setDate(d.getDate() + days)
  return dateString(d)
}

/**
 * from から to までの日数(to が後なら正)。日付だけを見るので、
 * 夏時間のある地域でも 23/25 時間ずれないよう、UTC の 0 時どうしで引く。
 */
export function daysBetween(from: string, to: string): number {
  const ms = Date.parse(`${to}T00:00:00Z`) - Date.parse(`${from}T00:00:00Z`)
  return Math.round(ms / 86_400_000)
}
