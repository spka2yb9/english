# SOURCES

教材の範囲・レベル・学習設計を判断する際に参照した主要資料。文法教材や商用教材の説明文・問題・紙面構成は
コピーしていない。外部のオープンデータを使用する語彙例文には、アプリ内で個別に出典を表示する。アクセス確認日: 2026-08-21。

## CEFR / 文法カリキュラム

- [Council of Europe — CEFR Companion Volume (2020)](https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions)
  — CEFRのレベル、言語活動、更新された記述尺度の基準。
- [Council of Europe — The framework](https://www.coe.int/en/web/common-european-framework-reference-languages/introduction-and-context)
  — A1–C2とA2+／B1+などのplus level、教材・カリキュラム設計での位置づけ。
- [English Profile — Introducing the CEFR / English Vocabulary Profile / English Grammar Profile](https://www.englishprofile.org/images/pdf/theenglishprofilebooklet.pdf)
  — 学習者コーパスに基づき語義・文法形式をCEFR段階で捉える方法。
- [English Vocabulary Profile user guide](https://www.englishprofile.org/images/pdf/evp%20user%20guide.pdf)
  — EVPが記述的資料であり、単語全体ではなく語義ごとのレベルも扱うという方法論。

## 語彙

- [Oxford University Press — The Oxford 3000 and Oxford 5000](https://learningenglishwithoxford.oup.com/2021/02/17/how-to-online-learner-dictionaries/)
  — 頻度、CEFRレベル、学習上の有用性を組み合わせた見出し語選定の主参照。
- [CEFR-J Wordlist 作成資料（東京外国語大学 投野研究室）](https://www.tufs.ac.jp/ts/personal/corpuskun/pdf/2018/CEFR-J_Wordlist_Making2.pdf)
  — 日本語母語話者向けCEFR語彙尺度との照合。
- [EJDict-hand](https://github.com/kujirahand/EJDict)
  — CC0の英和辞書データ。追加見出し語の日本語語義候補として利用し、例文の和訳と照合して対象語義を選択。
- [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict)
  — BSDライセンスの米語発音辞書。追加見出し語のIPA生成に利用。
- [Tatoeba Downloads](https://tatoeba.org/en/downloads)
  — CC BY 2.0 FRの対訳コーパス。拡張語彙のうち770例で使用し、各カードに文ID、投稿者、ライセンス、リンクを表示。

語彙リスト自体に唯一の「完全なB2集合」はないため、このアプリは上記を照合して4,500語を選び、完全性は
主張しない。うち1,500語は Oxford 5000 の C1帯・高頻度句動詞・定型表現からなる増補分で、
B2到達に必要な受容語彙としてアプリ内では B2 として提示する。
既存の詳細語彙、拡張分1,180例、増補分1,500例の英文・和訳は本プロジェクト用に作成した。

## 発音

- [International Phonetic Association — IPA chart](https://www.internationalphoneticassociation.org/content/ipa-chart)
  — 発音記号体系の確認。
- [ユーザー指定 Pronunciation Handbook](https://d27rnpuamwvieu.cloudfront.net/pdf/0c99MPMh1v9steJXNVbZMlwXX.pdf?openExternalBrowser=1)
  — 収録候補（母音、二重母音、有声／無声子音、L/R、鼻音、R母音）の範囲確認のみ。文言・図版・レイアウトは転載していない。
- 日本語と英語の音韻差に関する一般的な英語音声学の知見 — R/L、TH、V/B、F/H、S/SH、語末子音、
  schwa、強勢、弱形、連結を日本人学習者向け重点項目として採用。

## 学習科学

- [Roediger & Karpicke (2006), “Test-Enhanced Learning”](https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01693.x/)
  — 再読だけでなく想起テストを行うことによる遅延保持の改善。
- [Cepeda et al. (2006), “Distributed practice in verbal recall tasks”](https://pubmed.ncbi.nlm.nih.gov/16719566/)
  — 分散学習と保持間隔に関するメタ分析。
- [Dunlosky et al. (2013), “Improving Students’ Learning With Effective Learning Techniques”](https://doi.org/10.1177/1529100612453266)
  — practice testing と distributed practice を含む学習技法レビュー。
- Paivio — dual coding theory。図は装飾ではなく、時間・構造・対比の関係を言語説明と併記する方針に反映。
- Sweller — cognitive load theory / worked examples。3–15分の分割、短い説明から例題・問題へ進む設計に反映。
- Bjork — desirable difficulties。意味を先に見せない語彙想起と、類似形式を区別する問題に限定して反映。

これらを「脳科学的な近道」として宣伝せず、想起、間隔、フィードバック、短い単位、意味のある図解という
具体的な操作にだけ結びつけている。

## 実装・フォント

- [MDN — Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
  — ブラウザ音声合成の互換性とAPI形状。
- [IPA Font License v1.0](https://moji.or.jp/ipafont/license/)
  — PDF用IPAexゴシック。ライセンス本文は `public/fonts/IPA_Font_License_Agreement_v1.0.txt` に同梱。
