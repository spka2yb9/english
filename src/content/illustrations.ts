// 挿絵の仕様。図の絵柄は src/components/Illustration.tsx、
// レッスンごとの割り当ては src/content/grammar/illustrations.ts。
// labels: 図に描き込むラベルの本数(コンテンツ側と一致させる。content.test.ts が検査する)
// alt: 図の見た目を日本語で説明した文。スクリーンリーダー・Markdown・PDF が使う。

import type { IllustrationKind } from './types'

export const ILLUSTRATIONS: Record<IllustrationKind, { labels: number; alt: string }> = {
  equals: { labels: 3, alt: 'イコールの図: 左の人物と右のカードを等号がつなぐ' },
  action: { labels: 3, alt: '動作の図: 左の人物から右のカードへ矢印が伸びる' },
  'helper-verb': { labels: 3, alt: 'ヘルパー動詞の図: 助動詞のカードと原形のカードが並び、使わない形のカードにバツが付く' },
  'repeat-cycle': { labels: 2, alt: 'くり返しの図: ぐるりと回る矢印と、くり返す内容のカード' },
  'clock-moment': { labels: 2, alt: '時計の図: 時計と、その時点で進行中の内容のカード' },
  'calendar-day': { labels: 2, alt: 'カレンダーの図: 印の付いた日付と、その日の出来事のカード' },
  'now-to-future': { labels: 2, alt: '未来への図: 今を示す縦線から右の未来のカードへ点線の矢印が伸びる' },
  scale: { labels: 3, alt: '度合いの図: 左から右へ太くなる帯に3つの目盛りラベルが付く' },
  'count-vs-mass': { labels: 2, alt: '名詞の図: 左に3つの丸い果物、右にコップの液体' },
  'one-vs-the': { labels: 2, alt: '冠詞の図: 左は同じ形3つのうち1つを点線で囲み、右は特定の1つを矢印で指す' },
  'filter-group': { labels: 2, alt: '絞り込みの図: 左の3人がじょうごを通って右の1人になる' },
  'near-far': { labels: 2, alt: '距離の図: 手前の大きなカードと、奥の小さなカード' },
  'tag-noun': { labels: 2, alt: 'ふせんの図: 左のカードに説明のふせんが付く' },
  'question-mark': { labels: 2, alt: '疑問の図: 人物と大きな疑問符、そして疑問詞のカード' },
  'bars-compare': { labels: 3, alt: '比較の図: 高さの違う2本の棒と、中央に比較の言葉' },
  podium: { labels: 3, alt: '表彰台の図: 中央の1位が一番高く、星が付く' },
  'point-surface-box': { labels: 3, alt: '前置詞の図: 点・面の上・箱の中という3つの絵' },
  'path-move': { labels: 3, alt: '移動の図: 家から旗へ曲線の矢印が伸びる' },
  'linked-pair': { labels: 2, alt: 'セットの図: 2枚のカードが鎖でつながる' },
  'gate-allow': { labels: 2, alt: '可否の図: 左に丸、右にバツ' },
  'arrow-vs-loop': { labels: 2, alt: '形の図: 左は前へ進む矢印、右は輪' },
  'bridge-past-now': { labels: 2, alt: '現在完了の図: 過去の点から今の点へアーチがかかる' },
  steps: { labels: 3, alt: '段の図: 左から右へ高くなる3つのブロック' },
  'spotlight-swap': { labels: 3, alt: 'スポットライトの図: 左のカードから矢印が伸び、右のカードが光に照らされる' },
  'dots-omit': { labels: 2, alt: '省略の図: 上の長いカードと、一部を省いた下の短いカード' },
  'two-roads': { labels: 3, alt: '分かれ道の図: 1つの点から上下2方向へ道が分かれる' },
  'thought-cloud': { labels: 2, alt: '想像の図: 人物と、頭の上に浮かぶ雲の吹き出し' },
  'speech-relay': { labels: 3, alt: '伝達の図: 発言の吹き出しから、伝えた形の吹き出しへ矢印が伸びる' },
  'earlier-later': { labels: 2, alt: '前後関係の図: 過去へ向かう線の上に、先の旗とあとの旗が立つ' },
  'cause-effect': { labels: 3, alt: '因果の図: 原因のカードから結果のカードへ矢印が伸びる' },
  'box-in-slot': { labels: 2, alt: 'はめ込みの図: 上のカードが下の文の点線のわくに入る' },
  'feeling-source': { labels: 2, alt: '感情の図: 原因のカードから、表情のある人物へ矢印が伸びる' },
  handoff: { labels: 3, alt: '依頼の図: 頼む人・依頼内容のカード・する人が矢印で並ぶ' },
  'eye-ear': { labels: 2, alt: '知覚の図: 目と耳の絵と、見聞きした場面のカード' },
  'swap-cards': { labels: 2, alt: '語順の図: 上のカードと下のカードで語順が入れ替わる' },
  'two-cards': { labels: 2, alt: '使い分けの図: 2枚のカードが「vs」を挟んで並ぶ' },
}

/** 図の内容を説明する alt テキスト。UI・Markdown・PDF で共通に使う。 */
export function illustrationAlt(kind: IllustrationKind, labels: string[]): string {
  return `${ILLUSTRATIONS[kind].alt}(${labels.join(' / ')})`
}
