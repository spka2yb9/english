# 文法コンテンツ執筆ガイド(コンテンツ生成エージェント用)

必読ファイル:
1. `src/content/types.ts` — データモデル(これに厳密に従う)
2. `src/content/grammar/a2/u01.ts` — ゴールドスタンダード。品質・構造・トーンの基準
3. `docs/grammar-curriculum.md` — 担当ユニットのレッスンID・タイトル・目標・分数

## ファイル規約

- ユニットごとに1ファイル: `src/content/grammar/<dir>/uNN.ts`
  - dir: A2→`a2`、A2+→`a2plus`、B1→`b1`、B1+→`b1plus`、B2→`b2`
- エクスポート: `export const uNN: GrammarUnit = { ... }`
- インポート: `import type { GrammarUnit } from '../../types'`
- レッスンID・タイトル・分数・目標はカリキュラム文書の指定に従う(目標は自然な日本語に肉付けしてよい)

## レッスン構造(必須)

各レッスン:
- `objective`: 「〜できるようになります」形式の日本語1〜2文
- `blocks`: 4〜7ブロック。順序は「解説 →(図解)→ 例文 →(対比)」を基本とする
  - `explanation` は最低2つ。用語から入らず直感的な説明から。段落は `\n\n` 区切り、`**強調**`、`- ` 箇条書き可
  - `examples` は最低1つ、例文7〜9個(自然な和訳付き、学習対象を `highlight`)
  - **時制・アスペクトのレッスンは必ず `timeline` ブロックを使う**(0=過去、100=今、130=未来。`range`+`arrowToNow` で継続、`point` で一点の出来事)
  - 使い分け・対比がテーマのレッスンは必ず `contrast` ブロックを使う
  - 活用表・使い分け一覧は `table`、語順は `structure`
  - 図解は装飾ではなく理解を助ける場合のみ
- `quiz`: 4問。id は `<lessonId>-q1` 〜。全問に:
  - `prompt`(日本語の設問)、選択肢4つ、`correctIndex`
  - `explanation`(正解の理由)
  - `choiceNotes`(choices と同じ長さの配列。誤答がなぜ誤りか。正解位置は null)
  - `audioEn`(完全な正解英文)
  - 問題形式は混ぜる: 空所補充(`sentence` に `___`)/正しい文の選択/誤り探し/意味の判別。表面的な手がかりで解けない設計に
- `summary`: 2〜5点
- `prereqs`: ユニット内は直前レッスン。カリキュラム文書のレベル間依存も反映

## 品質ルール

- 日本語はです・ます調。明快・会話的・教育的に正確。専門用語の羅列をしない
- 英語は自然なアメリカ英語。「文法のためだけの不自然な文」を作らない
- `en` / `audioEn` は TTS にそのまま渡せるクリーンな英文のみ(括弧・記号・注記・スラッシュを含めない)
- `highlight` は `en` の正確な部分文字列であること
- 嘘の言語学的説明を書かない。不確かなことは書かない
- 水増しコンテンツ禁止。すべての例文・問題に教育的価値を持たせる

## 挿絵レイヤー

- `src/content/grammar/illustrations.ts` に、全レッスンの挿絵(図の種類 + ラベル + 説明文)を1件ずつ置く
- 図の種類は `src/content/illustrations.ts` の `ILLUSTRATIONS` から選ぶ(絵柄は `src/components/Illustration.tsx`)。新しい絵柄が必要なときだけ追加する
- ラベルは図に描き込むので短く保つ(目安: 英語15字・日本語8字まで)。長い説明は `caption` に書く
- `applyLessonIllustrations` が最初の解説ブロックの直後へ挿絵を差し込む。`blocks` に自分で挿絵を書く必要はない
- レッスンを追加した場合は同じIDの挿絵も必須。`npm run validate:content` がIDの過不足とラベル本数を検査する

## 全レッスン共通の補強レイヤー

- `src/content/grammar/expansions/` に、全110レッスンそれぞれの補強解説と追加例文3つを置く
- 補強解説は2段落以上とし、既存解説の言い換えではなく、判断手順・意味の違い・よくある誤りのいずれかを深掘りする
- `applyLessonExpansions` が主例文ブロックの直前へ補強解説を置き、主例文へ3文を追加する。UI・Markdown・PDFは合成後の同じデータを使う
- レッスンを追加した場合は同じIDの補強データも必須。`npm run validate:content` がIDの過不足、解説量、追加例文数を検査する

## TypeScript 規約

- 文字列は基本シングルクォート。アポストロフィを含む英文は `"He doesn't know."` のようにダブルクォートを使う
- 執筆後に `npx tsc --noEmit 2>&1 | grep <自分のファイル名>` で自分のファイルのエラーが無いことを確認し、あれば修正する
