# 語彙データセットの増補（8,000語 → 8,800語）

## なぜ増やすか

8,000語到達後もなお、**A1相当の基礎語**と**選定から漏れた日常語**に穴が残っている。
B2の抽象語・学術語は厚い一方で、`door` `window` `school` `day` `apple` `hot` `drink` `want` `know` のような
高頻度語が1語も収録されていない。出題がB1/B2に偏る体感の主因はここにある
（`src/services/vocabSelection.ts` はレベルを見ないため、出題率は収録率に一致する）。

## 何を足すか

語リストは `scripts/vocab-8800/words.tsv`（`word<TAB>level<TAB>batch`）。全800語。内訳:

| 由来 | 語数 | 内容 |
| --- | ---: | --- |
| A1相当の基礎語 | 607 | `src/content/basicWords.ts`（多読の未習語率検査で「既習」として扱っている1,130語）のうち未収録分。機能語・代名詞を含む |
| 多読の語注 | 79 | `src/content/reading/` の glossary にあり未収録だった語 |
| 選定漏れの具体語 | 108 | 衣食住・道具・素材・園芸・育児・医療・職業・教科・動植物・天気・感情などのトピック候補から、未収録のものだけを抽出 |
| 生成元リストの取りこぼし | 6 | `scripts/wordlist.txt` に載っているのに未収録: `online` `opposite` `partner` `topic` `traffic` `uncertain` |

集め方は `/tmp/miss.py` 方式と同じで、既存8,000語の見出し語集合に候補を突き合わせ、
**id ではなく見出し語**で未収録を判定した。英米つづり違い（`neighbourhood` と `neighborhood`）は重複として除外している。

## レベルの扱い

`VocabularyEntry['level']` は `'A2' | 'B1' | 'B2'` のままとし、**A1相当の語も `A2` として登録する**。
`docs/vocabulary-methodology.md` の「level の値は『B2到達までに扱う範囲』を示すもので、
Oxford のタグをそのまま転記したものではない」（C1帯を B2 と表示する扱い）と同じ考え方。
内訳は A2 735語 / B1 65語。

## バッチ

`plus40.ts` 〜 `plus47.ts` の8ファイル、各100語。

| バッチ | 語数 | 範囲 |
| --- | ---: | --- |
| plus40 | 100 | a – c |
| plus41 | 100 | c – f |
| plus42 | 100 | f – k |
| plus43 | 100 | k – m |
| plus44 | 100 | m – p |
| plus45 | 100 | p – s |
| plus46 | 100 | s – t |
| plus47 | 100 | t – z |

## 1語に必要なもの

`docs/vocabulary-expansion.md` と同じ。

- `mnemonic`（覚えるヒント）と `collocations` は全語必須。コロケーションは最低1件が見出し語の語幹を含むこと
- `exampleSentence` も同じ語幹を含むこと（語幹 = 先頭語の先頭 `max(3, 長さ-3)` 文字）
- 語源（`etymology`）は持たない。由来を書く場合も `mnemonic` の中で断定しない

## 1バッチの手順

1. `scripts/vocab-8800/words.tsv` から担当バッチの語を取り、`src/content/vocabulary/plusNN.ts` に書く。
   様式は既存の `plus39.ts` と同じ（`import type { VocabularyEntry } from '../types'` → 配列を export）。
2. 統合前に単体検査する:
   `node --experimental-strip-types --no-warnings scripts/check-vocab-file.mjs src/content/vocabulary/plusNN.ts` を `bad 0` にする。
3. `src/content/vocabulary/index.ts` に import と spread を足す。
4. 件数を2か所直す。`src/content/content.test.ts` の `toHaveLength` と `src/content/summary.ts` の `vocabularyCount`
   （`npm run summary` で再生成できる）。
5. `npm run validate:content` と `npx tsc --noEmit` を通す。
6. 挿絵を `docs/vocabulary-illustrations.md` の手順で追加する（語を入れ終えてから）。

## 進捗

**完了**。語彙800語と挿絵800枚が揃い、総計8,800語になった。

| バッチ | 語 | 挿絵の回 | 状態 |
| --- | --- | --- | --- |
| plus40 | 100 | 第192回(`batch192.py`) | 済 |
| plus41 | 100 | 第193回(`batch193.py`) | 済 |
| plus42 | 100 | 第194回(`batch194.py`) | 済 |
| plus43 | 100 | 第195回(`batch195.py`) | 済 |
| plus44 | 100 | 第196回(`batch196.py`) | 済 |
| plus45 | 100 | 第197回(`batch197.py`) | 済 |
| plus46 | 100 | 第198回(`batch198.py`) | 済 |
| plus47 | 100 | 第199回(`batch199.py`) | 済 |

- 語彙: `plus40.ts` ～ `plus47.ts`（各100語）を `index.ts` へ配線し、`content.test.ts` の `toHaveLength(8800)` と `summary.ts` を更新。
  内訳は A2 1,750 / B1 1,781 / B2 5,269。
- 挿絵: `illustrations.ts` は 8,800件、`public/images/vocabulary/` は 8,800枚。全エントリの `src` が実ファイルを指すことを確認済み。
- 挿絵のファイル名は既存の回（`batch40.py` など）と衝突するため、本増補は**第192回から**の通し番号で置く。
  追記は `node scripts/vocab-illustrations/append-ts.mjs /tmp/batchNN.json ...`。
- 挿絵の目視確認（各回の一覧HTML `/tmp/batchNN.html`）は今回スキップした。読み取れない絵があれば `batchNNb.py` に描き直しを分けて出す。
- 出題は `src/services/vocabSelection.ts` の `LEVEL_WEIGHTS`（A2 3 : B1 2 : B2 1）でレベルの低い語を優先する。
  新規状態での出題は A2 20% → 37%、1語もA2が出ないセッションは 33% → 10% になった（2,000セッションの試行）。
