/// <reference types="vitest/config" />
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// GitHub Actions では GITHUB_REPOSITORY に `owner/repo` が入る。
// プロジェクトページは https://owner.github.io/repo/ 配下に出るため base をそこに合わせる。
// ユーザーページ(owner.github.io リポジトリ)とローカル開発はルート配信なので '/'。
const repo = process.env.GITHUB_REPOSITORY?.split('/')[1]
const base = repo !== undefined && !repo.endsWith('.github.io') ? `/${repo}/` : '/'

// https://vite.dev/config/
export default defineConfig({
  base,
  plugins: [react()],
  build: {
    // 文法・語彙は実行コードではなく教材データ主体の遅延チャンク。
    // 3,000語を含む語彙チャンクは約992 kB（gzip約318 kB）で、初期表示とは分離済み。
    chunkSizeWarningLimit: 1050,
  },
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
  },
})
