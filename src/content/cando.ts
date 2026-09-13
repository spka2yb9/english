// CEFR の can-do 記述子(Companion Volume の尺度を日本語で要約したもの)と、
// 各コンテンツがどの記述子に対応するかのマッピング。
// 「400時間」という量の主張を、カバレッジという質の主張で裏付けるために使う。
// 対象は読む・聞く・文法・語彙。産出技能(書く・話す)はこのアプリの範囲外とする。

export type CanDoSkill = 'reading' | 'listening' | 'grammar' | 'vocabulary'

export type CanDo = {
  id: string
  level: 'A2' | 'B1' | 'B2'
  skill: CanDoSkill
  text: string
}

export const canDoDescriptors: CanDo[] = [
  { id: 'R-A2-1', level: 'A2', skill: 'reading', text: '身近な話題の短く簡単な文章から、必要な具体情報を探し出せる。' },
  { id: 'R-A2-2', level: 'A2', skill: 'reading', text: '案内・手紙・掲示など日常的な文書の要点を理解できる。' },
  { id: 'R-B1-1', level: 'B1', skill: 'reading', text: '日常や仕事でよく使われる平易な文章の主旨と要点を読み取れる。' },
  { id: 'R-B1-2', level: 'B1', skill: 'reading', text: '出来事や個人的な経験の記述を、時間の流れに沿って追える。' },
  { id: 'R-B2-1', level: 'B2', skill: 'reading', text: '現代的な問題を扱う記事や報告の論点と結論を把握できる。' },
  { id: 'R-B2-2', level: 'B2', skill: 'reading', text: '筆者の立場・態度・含意を読み取り、事実と意見を区別できる。' },
  { id: 'L-A2-1', level: 'A2', skill: 'listening', text: 'ゆっくり明瞭に話されれば、身近な話題の短い発話を理解できる。' },
  { id: 'L-B1-1', level: 'B1', skill: 'listening', text: '標準的な速さの発話で、身近な話題の要点を理解できる。' },
  { id: 'L-B2-1', level: 'B2', skill: 'listening', text: '具体的・抽象的な話題の議論の筋を追い、話者の意図を把握できる。' },
  { id: 'G-A2-1', level: 'A2', skill: 'grammar', text: '基本時制と語順で、日常の事実・習慣・状態を述べられる。' },
  { id: 'G-A2-2', level: 'A2', skill: 'grammar', text: '疑問文・否定文を正しく作り、比較や修飾の基本形を使える。' },
  { id: 'G-B1-1', level: 'B1', skill: 'grammar', text: '完了形・進行形の対比によって時間関係を表せる。' },
  { id: 'G-B1-2', level: 'B1', skill: 'grammar', text: '関係詞・条件文・接続詞で複数の情報を1文にまとめられる。' },
  { id: 'G-B2-1', level: 'B2', skill: 'grammar', text: '仮定法・分詞構文・倒置など複雑な構造を意図に応じて運用できる。' },
  { id: 'G-B2-2', level: 'B2', skill: 'grammar', text: '談話標識を用いて段落間の論理関係を明示できる。' },
  { id: 'V-A2-1', level: 'A2', skill: 'vocabulary', text: '日常生活の基本語彙を、発音と用例とともに運用できる。' },
  { id: 'V-B1-1', level: 'B1', skill: 'vocabulary', text: '身近な話題を扱うのに十分な語彙を持ち、言い換えができる。' },
  { id: 'V-B2-1', level: 'B2', skill: 'vocabulary', text: '多義語・コロケーション・語形成を含む4,500語規模の語彙を運用できる。' },
]

/** 文法ユニット → can-do 記述子 */
export const unitCanDo: Record<string, string[]> = {
  u01: ['G-A2-1'],
  u02: ['G-A2-1'],
  u03: ['G-A2-1'],
  u04: ['G-A2-1'],
  u05: ['G-A2-2'],
  u06: ['G-A2-2'],
  u07: ['G-A2-2'],
  u08: ['G-A2-1', 'G-A2-2'],
  u09: ['G-A2-2'],
  u10: ['G-B1-2'],
  u11: ['G-B1-1'],
  u12: ['G-B1-1'],
  u13: ['G-B1-2'],
  u14: ['G-B1-2'],
  u15: ['G-B1-2'],
  u16: ['G-B1-2', 'G-B2-2'],
  u17: ['G-B1-1'],
  u18: ['G-B1-1'],
  u19: ['G-B1-2'],
  u20: ['G-B1-2'],
  u21: ['G-B1-2'],
  u22: ['G-B2-1'],
  u23: ['G-B2-1'],
  u24: ['G-B2-1'],
  u25: ['G-B2-1'],
  u26: ['G-B2-1'],
  u27: ['G-B2-1'],
  u28: ['G-B2-1'],
  u29: ['G-B2-2'],
  u30: ['G-B2-1'],
  u31: ['G-B2-1'],
  u32: ['G-B2-1'],
  u33: ['G-B2-1', 'G-B2-2'],
}

/** 語彙・発音は水準ごとにまとめて対応づける。 */
export const vocabularyCanDo: Record<'A2' | 'B1' | 'B2', string[]> = {
  A2: ['V-A2-1'],
  B1: ['V-B1-1'],
  B2: ['V-B2-1'],
}

const descriptorMap = new Map(canDoDescriptors.map((d) => [d.id, d]))

export function findCanDo(id: string): CanDo | undefined {
  return descriptorMap.get(id)
}
