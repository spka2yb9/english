import { readFileSync, writeFileSync } from 'node:fs'

const preparedPath = process.argv[2] ?? '/tmp/vocabulary-expansion.json'
const examplesPath = process.argv[3] ?? 'scripts/vocabulary-expansion-examples.tsv'
const outputPath = process.argv[4] ?? 'src/content/vocabulary/expanded.ts'

const prepared = JSON.parse(readFileSync(preparedPath, 'utf8'))
const manualExamples = readManualExamples()
const candidateWords = new Set(prepared.map((entry) => entry.word))

function main() {
const unknownManualWords = [...manualExamples.keys()].filter((word) => !candidateWords.has(word))
if (unknownManualWords.length > 0) {
  throw new Error(`候補リストにない手動例文: ${unknownManualWords.join(', ')}`)
}

const rows = prepared.map((entry) => {
  const manual = manualExamples.get(entry.word)
  const example = manual ?? entry.referenceExample
  if (!example) throw new Error(`${entry.word}: 例文がありません`)

  return [
    entry.word,
    entry.level,
    entry.partOfSpeech,
    selectMeanings(entry.word, entry.meaningCandidates, example.japanese),
    entry.pronunciation,
    example.english,
    example.japanese,
    manual ? null : parseTatoebaSource(entry.referenceExample.attribution),
  ]
})

const source = `// このファイルは scripts/generate-vocabulary-expansion.mjs で生成する。\n` +
  `// Oxford A2–B2 差分、CC0英和語義、CMUdict発音、独自例文／Tatoeba対訳を正規化した拡張データ。\n` +
  `import type { VocabularyEntry } from '../types'\n\n` +
  `type ExpandedRow = [\n` +
  `  word: string,\n` +
  `  level: 'A2' | 'B1' | 'B2',\n` +
  `  partOfSpeech: string,\n` +
  `  meaningsJa: string[],\n` +
  `  pronunciation: string,\n` +
  `  exampleSentence: string,\n` +
  `  exampleTranslationJa: string,\n` +
  `  source: VocabularyEntry['exampleSource'] | null,\n` +
  `]\n\n` +
  `const rows: ExpandedRow[] = ${JSON.stringify(rows, null, 2)}\n\n` +
  `export const expandedVocabulary: VocabularyEntry[] = rows.map((row) => ({\n` +
  `  id: row[0],\n` +
  `  word: row[0],\n` +
  `  level: row[1],\n` +
  `  partOfSpeech: row[2],\n` +
  `  meaningsJa: row[3],\n` +
  `  pronunciation: row[4],\n` +
  `  exampleSentence: row[5],\n` +
  `  exampleTranslationJa: row[6],\n` +
  `  ...(row[7] ? { exampleSource: row[7] } : {}),\n` +
  `}))\n`

writeFileSync(outputPath, source)
console.log(
  JSON.stringify({
    generated: rows.length,
    originalExamples: rows.filter((row) => row[7] === null).length,
    attributedCorpusExamples: rows.filter((row) => row[7] !== null).length,
    outputPath,
  }),
)
}

function readManualExamples() {
  const examples = new Map()
  for (const [index, line] of readFileSync(examplesPath, 'utf8').split(/\r?\n/).entries()) {
    if (!line || line.startsWith('#')) continue
    const fields = line.split('\t')
    if (fields.length !== 3) throw new Error(`${examplesPath}:${index + 1}: 3列ではありません`)
    const [word, english, japanese] = fields
    if (examples.has(word)) throw new Error(`${examplesPath}:${index + 1}: ${word} が重複しています`)
    if (!containsTarget(english, word)) {
      throw new Error(`${examplesPath}:${index + 1}: 例文に ${word} が含まれていません`)
    }
    examples.set(word, { english, japanese })
  }
  return examples
}

function selectMeanings(word, candidates, japaneseExample) {
  const contextualMeanings = contextualMeaningOverrides[word]
  if (contextualMeanings) return contextualMeanings
  if (!Array.isArray(candidates) || candidates.length === 0) return ['文脈に応じた意味']
  const scored = candidates.map((meaning, index) => ({
    meaning,
    index,
    score: meaningScore(meaning, japaneseExample),
  }))
  scored.sort((left, right) => right.score - left.score || left.index - right.index)
  const selected = [scored[0].meaning]
  const second = scored.find((item) => item.index !== scored[0].index && item.score > 1)
  if (second && second.meaning !== selected[0]) selected.push(second.meaning)
  return selected
}

function meaningScore(meaning, japaneseExample) {
  const normalizedMeaning = normalizeJapanese(meaning)
  const normalizedExample = normalizeJapanese(japaneseExample)
  if (!normalizedMeaning || !normalizedExample) return 0
  let score = normalizedExample.includes(normalizedMeaning) ? 100 + normalizedMeaning.length ** 2 : 0
  for (let size = Math.min(8, normalizedMeaning.length); size >= 2; size -= 1) {
    for (let index = 0; index <= normalizedMeaning.length - size; index += 1) {
      const part = normalizedMeaning.slice(index, index + size)
      if (normalizedExample.includes(part)) score = Math.max(score, size * size)
    }
  }
  return score
}

function normalizeJapanese(value) {
  return (value.match(/[ぁ-ん一-龯ァ-ヶー]/g) ?? []).join('')
}

function parseTatoebaSource(attribution) {
  const matches = [...attribution.matchAll(/#(\d+) \(([^)]+)\)/g)]
  const englishId = matches[0]?.[1]
  const shortAttribution = matches.map((match) => `#${match[1]} (${match[2]})`).join(' / ')
  return {
    name: 'Tatoeba',
    url: englishId ? `https://tatoeba.org/en/sentences/show/${englishId}` : 'https://tatoeba.org/',
    license: 'CC BY 2.0 FR',
    attribution: shortAttribution || 'Tatoeba contributors',
  }
}

function containsTarget(sentence, word) {
  const escaped = word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  if (new RegExp(`(^|[^a-z])${escaped}([^a-z]|$)`, 'i').test(sentence)) return true
  if (!/^[a-z]+$/.test(word)) return false
  const stem = word.slice(0, Math.max(3, word.length - 3))
  return sentence.toLowerCase().includes(stem)
}

// 例文が扱う語義を優先する。特に多義語では辞書の先頭語義と一致しないため、
// 自動文字列照合だけに任せず、人手で確認した文脈語義を固定する。
const contextualMeaningOverrides = {
  absolutely: ['まったく', '絶対に'],
  accidentally: ['誤って', '偶然に'],
  accomplish: ['達成する', '成し遂げる'],
  activate: ['作動させる', '有効にする'],
  addiction: ['依存', '中毒'],
  administration: ['政権', '行政'],
  adult: ['大人', '成人の'],
  advise: ['助言する', '勧める'],
  against: ['〜に反対して', '〜に対して'],
  aged: ['〜歳の', '高齢の'],
  agreement: ['合意', '一致'],
  all: ['すべての', '全部'],
  allow: ['許す', '〜できるようにする'],
  along: ['〜に沿って'],
  alongside: ['〜に沿って', '〜のそばに'],
  amazed: ['驚いた'],
  analyst: ['アナリスト', '分析者'],
  animation: ['アニメーション', '動画'],
  annoying: ['煩わしい', '迷惑な'],
  anybody: ['誰か', '誰でも'],
  anywhere: ['どこでも'],
  appear: ['現れる', '表示される'],
  apply: ['応募する', '適用する'],
  approval: ['承認', '賛成'],
  appropriately: ['適切に', 'ふさわしく'],
  army: ['軍', '陸軍'],
  asset: ['強み', '資産'],
  assistance: ['手助け', '支援'],
  attachment: ['添付ファイル', '愛着'],
  attraction: ['観光名所', '魅力'],
  awful: ['ひどい', '恐ろしい'],
  beat: ['打ち負かす', 'たたく'],
  bet: ['きっと〜だと思う', '賭ける'],
  bias: ['偏り', '偏見'],
  bin: ['ごみ箱', '容器'],
  birth: ['出産', '誕生'],
  bowl: ['ボウル', '一杯'],
  bug: ['バグ', '不具合', '虫'],
  bush: ['茂み', '低木'],
  by: ['〜までに', '〜によって'],
  calm: ['冷静な', '穏やかな'],
  casual: ['普段着の', '気軽な'],
  central: ['中心的な', '不可欠な'],
  challenging: ['難しい', 'やりがいのある'],
  check: ['確認する', '小切手'],
  cheer: ['歓声', '応援する'],
  cheerful: ['明るい', '陽気な'],
  chief: ['主任の', '主要な', '長'],
  choice: ['選択肢', '選択'],
  circuit: ['周回', '回路'],
  clarify: ['明確にする'],
  classical: ['クラシックの', '古典の'],
  clerk: ['係員', '事務員'],
  clever: ['賢い', '巧妙な'],
  click: ['クリックする', 'カチッという音'],
  code: ['コード', '暗証番号'],
  column: ['列', '円柱'],
  comic: ['滑稽な', '漫画'],
  communication: ['意思疎通', '通信'],
  confusing: ['分かりにくい', '混乱させる'],
  connected: ['つながった', '関連した'],
  consistent: ['一貫した'],
  continuous: ['連続した'],
  convey: ['伝える', '運ぶ'],
  cool: ['冷ます', '涼しい'],
  corporation: ['企業', '法人'],
  crazy: ['無謀な', '正気でない'],
  creation: ['設立', '創造'],
  creativity: ['創造力'],
  critically: ['重篤に', '批判的に'],
  crowded: ['混雑した'],
  cupboard: ['戸棚'],
  curly: ['巻き毛の'],
  data: ['データ', '資料'],
  deal: ['合意', '取引', '扱う'],
  dear: ['〜様', '親愛なる'],
  decent: ['まずまずの', 'きちんとした'],
  defence: ['弁護', '防衛'],
  demonstration: ['実演', 'デモ'],
  depression: ['うつ状態', '不況'],
  disk: ['ディスク', '円盤'],
  drawing: ['図面', '絵'],
  dressed: ['正装した', '服を着た'],
  drunk: ['酔った', 'drinkの過去分詞'],
  electricity: ['電気', '電力'],
  electronics: ['電子機器', '電子工学'],
  emission: ['排出', '排出物'],
  empty: ['空の'],
  engaged: ['取り組んでいる', '婚約した'],
  enhance: ['高める', '良くする'],
  entertaining: ['面白い', '楽しませる'],
  episode: ['番組の回', 'エピソード'],
  estate: ['土地', '不動産'],
  examination: ['検査', '試験'],
  executive: ['役員', '経営幹部'],
  exotic: ['珍しい', '異国風の'],
  exploration: ['探査', '探検'],
  extension: ['延長', '内線'],
  fabulous: ['すばらしい'],
  farm: ['栽培する', '農業を営む'],
  favour: ['お願い', '親切'],
  female: ['女性の', '雌の'],
  file: ['ファイル', '保管する'],
  fire: ['解雇する', '火'],
  fit: ['収まる', '適合する'],
  fitness: ['体力', '健康'],
  fly: ['運航する', '飛ぶ'],
  foreign: ['海外の', '外国の'],
  format: ['形式'],
  forum: ['意見交換の場', 'フォーラム'],
  forward: ['前へ', '楽しみにして'],
  fry: ['炒める', '揚げる'],
  fulfil: ['発揮する', '果たす'],
  fully: ['完全に', 'すべて'],
  furious: ['激怒した'],
  gaming: ['ゲーム', 'ゲームをすること'],
  globe: ['世界', '地球'],
  gorgeous: ['見事な', '豪華な'],
  graphic: ['生々しい', '図表の'],
  graphics: ['画像', 'グラフィックス'],
  guard: ['警備員', '守る'],
  hand: ['手渡す', '手'],
  hate: ['嫌う', '憎む'],
  head: ['率いる', '頭'],
  heal: ['治る', '治す'],
  heat: ['温める', '熱'],
  honour: ['表彰する', '名誉'],
  hopefully: ['うまくいけば'],
  hurt: ['痛む', '傷つける'],
  icon: ['アイコン'],
  implication: ['影響', '含意'],
  indication: ['兆候', '表示'],
  infrastructure: ['基盤', 'インフラ'],
  input: ['意見', '入力'],
  interaction: ['交流', '相互作用'],
  interval: ['休憩', '間隔'],
  invasion: ['侵攻', '侵入'],
  isolate: ['特定して切り離す', '分離する'],
  jam: ['渋滞', 'ジャム'],
  journalist: ['記者', 'ジャーナリスト'],
  kid: ['子ども'],
  kill: ['枯らす', '殺す'],
  last: ['もつ', '続く'],
  leading: ['第一線の', '主要な'],
  line: ['並ぶ', '線'],
  live: ['生放送で', '生きる'],
  luck: ['運', '幸運'],
  lucky: ['運がよい'],
  making: ['意思決定', '作ること'],
  male: ['男性の', '雄の'],
  manager: ['管理者', '責任者'],
  marker: ['標識', '印'],
  marketing: ['マーケティング', '販売促進'],
  martial: ['武術の', '軍事の'],
  mass: ['大量', '塊'],
  mate: ['仲間', '学友'],
  material: ['教材', '材料'],
  mechanic: ['整備士'],
  medical: ['医療の', '医学の'],
  medication: ['薬'],
  medium: ['中くらいの', '媒体'],
  mention: ['触れる', '言及する'],
  mind: ['〜していただけますか', '気にする'],
  minimum: ['最低', '最小'],
  miserable: ['つらい', 'みじめな'],
  mixed: ['間違えた', '混ざった'],
  mixture: ['混合物', '雨と雪の混合'],
  mobile: ['携帯電話', '移動式の'],
  mode: ['ア・ラ・モード', '方式'],
  monitor: ['監視する', '確認する'],
  monthly: ['毎月の'],
  mortgage: ['住宅ローン', '抵当'],
  mosque: ['モスク'],
  mostly: ['ほとんど', '主に'],
  motion: ['動き', 'スローモーション'],
  motivate: ['動機づける'],
  motivation: ['意欲', '動機'],
  mount: ['取り付ける', '設置する'],
  moving: ['感動的な', '動いている'],
  musical: ['音楽の', '音楽的な'],
  mystery: ['謎'],
  nail: ['爪', 'くぎ'],
  national: ['国の', '国立の'],
  native: ['母語話者の', '生まれつきの'],
  nature: ['性質', '自然'],
  nearby: ['近くに', '近くの'],
  nearly: ['もう少しで', 'ほとんど'],
  necessarily: ['必ずしも'],
  nerve: ['勇気', '神経'],
  nervous: ['緊張した', '神経の'],
  network: ['人脈', 'ネットワーク'],
  newly: ['新しく'],
  next: ['隣の', '次の'],
  notice: ['通知', '届け出'],
  notion: ['考え', '概念'],
  offence: ['悪気', '犯罪', '違反'],
  offer: ['提供する', '申し出る'],
  opening: ['開館', '開始'],
  option: ['選択肢'],
  organ: ['臓器', 'オルガン'],
  organized: ['整理された', '組織された'],
  organizer: ['主催者'],
  originally: ['もともと', '本来'],
  outfit: ['服装', '衣装'],
  oven: ['オーブン'],
  owner: ['所有者', '店主'],
  pace: ['ペース', '速度'],
  package: ['小包', '一式'],
  packet: ['小袋', '包み'],
  particular: ['好みがうるさい', '特定の'],
  partly: ['一部は', '部分的に'],
  passionate: ['熱心な', '情熱的な'],
  password: ['パスワード'],
  penalty: ['刑罰', '罰則'],
  'per cent': ['パーセント'],
  perceive: ['受け取る', '認識する'],
  photography: ['写真撮影', '写真術'],
  pick: ['受け取る', '選ぶ'],
  pill: ['錠剤'],
  pin: ['留め針', 'ピンで留める'],
  placement: ['職場実習', '配置'],
  planning: ['計画', '計画立案'],
  plastic: ['プラスチック', 'ラップ'],
  please: ['どうぞ', '〜してください'],
  point: ['観点', '要点'],
  pointed: ['鋭い', '先のとがった'],
  pot: ['ポット', '容器'],
  presentation: ['プレゼンテーション', '発表'],
  press: ['報道陣', '押す'],
  print: ['絶版', '印刷する'],
  prior: ['事前の', '前の'],
  probability: ['可能性', '確率'],
  probable: ['ありそうな'],
  protester: ['抗議者'],
  public: ['公共の', '公有の'],
  publicity: ['宣伝', '売名'],
  purely: ['まったく', '純粋に'],
  pursuit: ['追跡', '追求'],
  quotation: ['見積もり', '引用'],
  race: ['人類', '競争'],
  reasonably: ['適正に', '合理的に'],
  realize: ['気づく', '実現する'],
  reckon: ['〜だと思う', '見積もる'],
  recognition: ['気づくこと', '認識'],
  recruitment: ['採用', '募集'],
  regularly: ['いつも', '定期的に'],
  relaxing: ['リラックスできる', 'くつろいだ'],
  remarkably: ['驚くほど', '著しく'],
  resign: ['辞職する', '辞める'],
  resort: ['最後の手段', '行楽地'],
  rest: ['残り', '休息'],
  revision: ['修正', '改訂'],
  rival: ['太刀打ちする', '競争相手'],
  scenario: ['想定', 'シナリオ'],
  screening: ['検診', '上映'],
  season: ['季節', '時期'],
  seat: ['席', '腰掛け'],
  secondary: ['二次的な', '第2の'],
  seeker: ['求職者', '探し求める人'],
  self: ['自己', '自分'],
  setting: ['設定', '環境'],
  settler: ['入植者'],
  severely: ['重度に', 'ひどく'],
  shooting: ['銃撃', '射撃'],
  shot: ['発射音', '発砲'],
  shout: ['叫ぶ', '大声を出す'],
  sibling: ['きょうだい'],
  since: ['〜して以来', '〜なので'],
  sir: ['お客様', '〜さん'],
  smoking: ['喫煙'],
  soft: ['柔らかい'],
  speaker: ['話者', 'スピーカー'],
  spending: ['支出', '消費'],
  spite: ['〜にもかかわらず', '悪意'],
  spoken: ['話された', '口語の'],
  spokesman: ['報道担当者', '代弁者'],
  sponsorship: ['後援', '資金提供'],
  spring: ['温泉', '春', 'ばね'],
  stall: ['露店', '屋台'],
  sticky: ['付箋の', '粘着する'],
  stream: ['人の流れ', '小川'],
  stroke: ['画', '一打ち'],
  strongly: ['強く思う', '強く'],
  stunning: ['見事な', '驚くほど美しい'],
  subsequently: ['その後', '続いて'],
  super: ['とても', 'すごい'],
  tablet: ['錠剤', 'タブレット端末'],
  tap: ['蛇口', '軽くたたく'],
  taste: ['味がする', '味覚'],
  term: ['学期', '用語'],
  terms: ['〜の観点で', '条件', '用語'],
  territory: ['敵地', '領域'],
  text: ['テキストメッセージ', '文章'],
  thick: ['濃い', '厚い'],
  thinking: ['思考', '考えること'],
  thoroughly: ['すっかり', '徹底的に'],
  throw: ['吐く', '投げる'],
  timing: ['タイミング', '時期'],
  tissue: ['ティッシュ', '組織'],
  tongue: ['母語', '舌'],
  top: ['首位', '頂上'],
  total: ['総額', '合計'],
  totally: ['すっかり', '完全に'],
  trace: ['跡', '痕跡'],
  track: ['突き止める', '跡を追う'],
  trading: ['取引', '貿易'],
  traditional: ['伝統的な'],
  training: ['研修', '訓練'],
  transportation: ['交通手段', '輸送'],
  trial: ['試行', '裁判'],
  trick: ['手品', '仕掛け'],
  trouble: ['困ったこと', '問題'],
  typical: ['いかにも〜らしい', '典型的な'],
  unable: ['〜できない'],
  uncertainty: ['不確実性', '不安'],
  unit: ['設備一式', '単位'],
  united: ['団結した', '一体となった'],
  unity: ['連帯感', '団結'],
  upon: ['〜するとすぐ', '〜の上に'],
  variation: ['ばらつき', '変化'],
  van: ['バン', '小型配送車'],
  vast: ['大多数の', '広大な'],
  view: ['景色', '見方'],
  virtual: ['オンラインの', '仮想の'],
  vision: ['将来像', '視力'],
  volume: ['音量', '容量'],
  volunteer: ['協力者', '志願者'],
  warming: ['温暖化', '暖めること'],
  way: ['はるかに', 'ずっと'],
  weakness: ['欠点', '弱さ'],
  wealth: ['収入源', '富'],
  web: ['ウェブ', '網'],
  weird: ['おかしな', '奇妙な'],
  while: ['しばらく', '〜する間'],
  wisdom: ['知恵', '親知らず'],
  withdraw: ['引き出す', '撤回する'],
  working: ['働くこと', '勤務している'],
  workshop: ['講座', '作業場'],
  worth: ['〜する価値がある'],
  zone: ['領域', '地帯'],
}

main()
