// タイプ入力の採点。表記ゆれ(大小文字・句読点・短縮形・全角記号)を吸収し、
// 内容が合っていれば正解として扱う。ディクテーション・和文英訳・語彙産出で共用する。

const CONTRACTIONS: [RegExp, string][] = [
  [/\bcan't\b/g, 'cannot'],
  [/\bwon't\b/g, 'will not'],
  [/\bshan't\b/g, 'shall not'],
  [/n't\b/g, ' not'], // isn't → is not(前に \b は置けない。s と n の間に語境界がない)
  [/\b'll\b/g, ' will'],
  [/\b're\b/g, ' are'],
  [/\b've\b/g, ' have'],
  [/\b'd\b/g, ' would'],
  [/\bi'm\b/g, 'i am'],
  [/\bit's\b/g, 'it is'],
  [/\bhe's\b/g, 'he is'],
  [/\bshe's\b/g, 'she is'],
  [/\bthat's\b/g, 'that is'],
  [/\bthere's\b/g, 'there is'],
  [/\bwhat's\b/g, 'what is'],
  [/\bwho's\b/g, 'who is'],
  [/\blet's\b/g, 'let us'],
]

/** 比較用の正規化。大小文字・句読点・短縮形・空白の違いを消す。 */
export function normalizeAnswer(text: string): string {
  let s = text.toLowerCase().replace(/[’‘]/g, "'").replace(/[“”]/g, '"')
  for (const [pattern, replacement] of CONTRACTIONS) s = s.replace(pattern, replacement)
  // 's は所有格(the boy's book)なので残し、それ以外の記号を落とす
  s = s.replace(/[.,!?;:"“”()[\]—–-]/g, ' ')
  return s.replace(/\s+/g, ' ').trim()
}

/** 内容が一致すれば正解。alternates は別解(和文英訳などで複数正解がある場合)。 */
export function isAnswerCorrect(input: string, expected: string, alternates: string[] = []): boolean {
  const normalized = normalizeAnswer(input)
  if (normalized.length === 0) return false
  return [expected, ...alternates].some((candidate) => normalizeAnswer(candidate) === normalized)
}

export type DiffToken = { word: string; status: 'ok' | 'missing' | 'extra' }

/**
 * 語単位の差分。どこを間違えたかを提示するために使う。
 * 抜けがあると以降が全部ずれるため、位置合わせではなく最長共通部分列で対応付ける。
 */
export function diffAnswer(input: string, expected: string): DiffToken[] {
  const got = normalizeAnswer(input).split(' ').filter(Boolean)
  const want = normalizeAnswer(expected).split(' ').filter(Boolean)

  // LCS長のテーブル
  const lcs: number[][] = Array.from({ length: got.length + 1 }, () => new Array(want.length + 1).fill(0))
  for (let i = got.length - 1; i >= 0; i--) {
    for (let j = want.length - 1; j >= 0; j--) {
      lcs[i][j] = got[i] === want[j] ? lcs[i + 1][j + 1] + 1 : Math.max(lcs[i + 1][j], lcs[i][j + 1])
    }
  }

  const tokens: DiffToken[] = []
  let i = 0
  let j = 0
  while (i < got.length && j < want.length) {
    if (got[i] === want[j]) {
      tokens.push({ word: want[j], status: 'ok' })
      i++
      j++
    } else if (lcs[i + 1][j] >= lcs[i][j + 1]) {
      tokens.push({ word: got[i], status: 'extra' })
      i++
    } else {
      tokens.push({ word: want[j], status: 'missing' })
      j++
    }
  }
  while (i < got.length) tokens.push({ word: got[i++], status: 'extra' })
  while (j < want.length) tokens.push({ word: want[j++], status: 'missing' })
  return tokens
}
