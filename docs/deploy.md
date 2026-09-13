# GitHub Pages へのデプロイ手順

静的サイトなので GitHub Pages に置くだけで動きます。サーバもDBも不要、月額0円です。
`main` に push すると GitHub Actions がテスト → ビルド → 公開まで自動で行います。

以下では `<owner>` を自分の GitHub アカウント名、`<repo>` をリポジトリ名に読み替えてください。

## 前提

- GitHub アカウント
- ローカルに Node.js 22 以上と git
- **リポジトリは public にすること**。GitHub Free では private リポジトリの Pages が使えず、
  無料で運用するには public が必要です(有料プランなら private でも可)。
  教材データもソースごと公開される点だけ確認してください。

## 1. リポジトリを作って push する

このディレクトリはまだ git 管理されていないので、初期化から始めます。

```bash
git init -b main
git add -A
git commit -m "Initial commit"
gh repo create <repo> --public --source=. --push   # gh CLI がなければ GitHub 上で空のリポジトリを作り、
                                                   # git remote add origin ... && git push -u origin main
```

`dist/` と `node_modules/` は `.gitignore` 済みなので、ビルド成果物をコミットする必要はありません。

## 2. Pages の公開元を Actions に切り替える

リポジトリの **Settings → Pages → Build and deployment → Source** で
**GitHub Actions** を選びます(既定の "Deploy from a branch" のままだとワークフローが失敗します)。

## 3. デプロイを確認する

`main` への push で `.github/workflows/deploy.yml` が動きます。
**Actions** タブでジョブが緑になったら、次のURLで公開されています。

```
https://<owner>.github.io/<repo>/
```

以降は `main` に push するたびに自動で更新されます。手動で流したいときは
Actions タブの "Deploy to GitHub Pages" → **Run workflow**。

## ワークフローがやっていること

| ステップ | 目的 |
| --- | --- |
| `npm ci` | `package-lock.json` どおりに依存を入れる |
| `npm test` | 失敗したらデプロイしない(壊れた状態を公開しないため) |
| `npm run build` | `dist/` を生成 |
| `cp dist/index.html dist/404.html` | Pages にSPAフォールバックが無いため、直リンクとリロードを動かす |
| `upload-pages-artifact` / `deploy-pages` | `dist/` を Pages に公開 |

サブパス配信への対応は設定済みです。`vite.config.ts` が Actions の `GITHUB_REPOSITORY` から
`base` を `/<repo>/` に決め、`src/App.tsx` の `BrowserRouter basename` がそれに追従します。
リポジトリ名を変えても再デプロイするだけで追従し、ローカル開発(`npm run dev`)はルート配信のままです。

## 端末間同期(private Gist)を使う場合

設定手順は [docs/sync.md](sync.md) を参照してください。公開サイトでも、進捗の保存先は
あなた個人の private Gist です。トークンはブラウザの localStorage にのみ入り、
リポジトリにもサイトにも含まれません。デプロイ側で注意する点は1つだけです。

- `<owner>.github.io` 配下の別プロジェクトとは localStorage が共通になる。
  同じアカウントで他のアプリも公開している場合、キー名(`eng.` 接頭辞)の衝突がないか確認する

## うまくいかないとき

| 症状 | 原因と対処 |
| --- | --- |
| Actions が `deploy-pages` で失敗する | 手順2をやっていない。Source を GitHub Actions にして再実行 |
| 画面が真っ白、アセットが404 | `base` の不一致。リポジトリ名を変更した直後なら再デプロイで直る |
| トップは開くが直リンクやリロードで404 | `404.html` のコピー漏れ。ワークフローの `cp` ステップを確認 |
| push しても内容が変わらない | Actions の完了を待つ(数十秒)。その後スーパーリロード(Ctrl+Shift+R) |
| Actions がテストで落ちる | 意図した動作。ローカルで `npm test` を通してから push する |
