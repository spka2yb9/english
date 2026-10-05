// 「イングバードにきく」の精度評価セット。
//
// 合格条件は「意図が一致し、引用に期待の文字列が含まれる」こと。失敗一覧を出し、
// リソース(テンプレート・語彙)を足して精度が伸びなくなったらプラトーとみなす。
// 実行すると ACCURACY 行に正解率が出る。

import { describe, expect, it } from 'vitest'
import { findLesson } from '../../content/grammar'
import { createSectionChat } from './matcher'
import type { ChatReply, QaIntent } from './types'

type Step = {
  q: string
  intent?: QaIntent
  contains?: string
  leadContains?: string
  fallback?: boolean
}

type Case = { id: string; steps: Step[] }

const CASES: Case[] = [
  // ===== u01-l1: be動詞の現在形 =====
  { id: 'u01-l1', steps: [{ q: 'このセクションで何を学ぶの?', intent: 'overview', contains: 'am / is / are' }] },
  { id: 'u01-l1', steps: [{ q: 'まとめを教えて', intent: 'summary', contains: 'do / does' }] },
  { id: 'u01-l1', steps: [{ q: '"I am a nurse." の意味は?', intent: 'meaning', contains: '看護師' }] },
  { id: 'u01-l1', steps: [{ q: '彼女は今日疲れています。', intent: 'meaning', contains: 'tired' }] },
  { id: 'u01-l1', steps: [{ q: '「彼女は今日疲れています。」を英語にすると?', intent: 'meaning', contains: 'tired' }] },
  { id: 'u01-l1', steps: [{ q: '"I am a nurse." は何文型?', intent: 'pattern', contains: 'SVC' }] },
  { id: 'u01-l1', steps: [{ q: '主語はどれ?', intent: 'structure', contains: 'She' }] },
  { id: 'u01-l1', steps: [{ q: 'be動詞とは?', intent: 'concept', contains: 'be動詞' }] },
  { id: 'u01-l1', steps: [{ q: 'be動詞', contains: 'be動詞' }] },
  { id: 'u01-l1', steps: [{ q: 'amとisの違いは?', contains: 'am' }] },
  { id: 'u01-l1', steps: [{ q: 'be動詞と一般動詞の違いは?', intent: 'difference', contains: '一般動詞' }] },
  { id: 'u01-l1', steps: [{ q: 'youのときのbe動詞は?', contains: 'are' }] },
  { id: 'u01-l1', steps: [{ q: 'Iの短縮形は?', intent: 'concept', contains: "I'm" }] },
  { id: 'u01-l1', steps: [{ q: 'クイズのヒントをちょうだい', intent: 'quiz', contains: '考え方' }] },
  { id: 'u01-l1', steps: [{ q: '答えを教えて', intent: 'quiz', leadContains: '言わない' }] },
  { id: 'u01-l1', steps: [{ q: '他の選択肢はなぜダメ?', intent: 'note', contains: 'am' }] },
  { id: 'u01-l1', steps: [{ q: 'クイズは何問?', intent: 'quiz', contains: '4問' }] },
  { id: 'u01-l1', steps: [{ q: '例文を教えて', intent: 'example', contains: 'nurse' }] },
  { id: 'u01-l1', steps: [{ q: '"I am a nurse." はどう発音する?', intent: 'pronunciation', contains: 'nurse' }] },
  { id: 'u01-l1', steps: [{ q: 'I am a nurse.', intent: 'meaning', contains: 'nurse' }] },
  { id: 'u01-l1', steps: [{ q: '発音を聞きたい', intent: 'pronunciation' }] },
  { id: 'u01-l1', steps: [{ q: '注意することは?', intent: 'note', contains: 'not' }] },
  { id: 'u01-l1', steps: [{ q: 'こんにちは', intent: 'greeting' }] },
  { id: 'u01-l1', steps: [{ q: '何ができるの?', intent: 'capability' }] },
  { id: 'u01-l1', steps: [{ q: 'このセクションのタイトルは?', intent: 'overview', contains: 'be動詞の現在形' }] },
  { id: 'u01-l1', steps: [{ q: 'どのくらいで終わる?', intent: 'overview', contains: '8分' }] },
  { id: 'u01-l1', steps: [{ q: '表を見せて', intent: 'table', contains: 'am' }] },
  { id: 'u01-l1', steps: [{ q: '表の読み方は?', intent: 'table' }] },
  { id: 'u01-l1', steps: [{ q: '今日の天気は?', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'ソクラテスとは?', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'おすすめの映画は?', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'もっと詳しく', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'もう一度言って', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'not', contains: 'not' }] },
  { id: 'u01-l1', steps: [{ q: 'is', contains: 'is' }] },
  { id: 'u01-l1', steps: [{ q: 'どうしてbe動詞は主語で変わるの?', intent: 'concept' }] },

  // 返答の返答
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse." の意味は?', intent: 'meaning' },
      { q: 'この文の文型は?', intent: 'pattern', contains: 'SVC' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse." の意味は?', intent: 'meaning' },
      { q: 'なぜ?', intent: 'concept' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: 'まとめを教えて', intent: 'summary' },
      { q: 'もう一度', leadContains: 'もう一度', contains: 'do / does' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse." の意味は?' },
      { q: '他には?' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: 'be動詞とは?', intent: 'concept' },
      { q: 'もっと詳しく' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: 'クイズのヒントをちょうだい', intent: 'quiz' },
      { q: '他の選択肢は?', contains: 'am' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse." の意味は?' },
      { q: 'それってどういう意味?' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse." は何文型?' },
      { q: 'この文の意味は?', intent: 'meaning', contains: '看護師' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '例文を教えて' },
      { q: 'もっと詳しく' },
    ],
  },

  // ===== u01-l2: 三単現 =====
  { id: 'u01-l2', steps: [{ q: '三単現とは?', intent: 'concept', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: '三単現', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: '例文', intent: 'example', contains: 'works' }] },
  { id: 'u01-l2', steps: [{ q: '文型', intent: 'pattern' }] },
  { id: 'u01-l2', steps: [{ q: '違いは?', intent: 'difference' }] },
  { id: 'u01-l2', steps: [{ q: '「-s が付く」と「-s が付かない」の違いは?', intent: 'difference', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: '"She likes music." の意味は?', intent: 'meaning', contains: '音楽' }] },
  { id: 'u01-l2', steps: [{ q: '彼女は音楽が好きです。', intent: 'meaning', contains: 'likes' }] },
  { id: 'u01-l2', steps: [{ q: 'なぜ三人称単数で-sを付けるの?', intent: 'concept', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: '三単現の例文は?', intent: 'example', contains: 'watches' }] },
  { id: 'u01-l2', steps: [{ q: 'studyの三単現は?', intent: 'concept', contains: 'studies' }] },
  { id: 'u01-l2', steps: [{ q: '三単現って結局何?', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: 'example sentences please', intent: 'example' }] },
  { id: 'u01-l2', steps: [{ q: 'why does she work become works?', intent: 'concept', contains: 'works' }] },

  // ===== u01-l3: 否定文と疑問文 =====
  { id: 'u01-l3', steps: [{ q: 'doとdoesの違いは?' }] },
  { id: 'u01-l3', steps: [{ q: 'なぜdoesを使うと動詞が原形に戻るの?', intent: 'concept', contains: '原形' }] },
  { id: 'u01-l3', steps: [{ q: '疑問文の作り方は?', intent: 'concept' }] },

  // ===== u02-l1: 現在進行形(構造図) =====
  { id: 'u02-l1', steps: [{ q: 'この文の主語は?', intent: 'structure', contains: '主語(S)' }] },
  { id: 'u02-l1', steps: [{ q: '"I am playing tennis." の骨格は?', intent: 'structure', contains: 'I play tennis' }] },
  { id: 'u02-l1', steps: [{ q: '"I am playing tennis." は何文型?', intent: 'pattern', contains: 'SVO' }] },
  { id: 'u02-l1', steps: [{ q: '文を分解して', intent: 'structure', contains: 'am playing' }] },
  { id: 'u02-l1', steps: [{ q: '現在進行形とは?', intent: 'concept', contains: 'ing' }] },
  { id: 'u02-l1', steps: [{ q: 'ingはどこに付けるの?' }] },
  { id: 'u02-l1', steps: [{ q: '例文', intent: 'example' }] },
  { id: 'u02-l1', steps: [{ q: '現在形との違いは?' }] },
  { id: 'u02-l1', steps: [{ q: 'where is the subject?', intent: 'structure' }] },

  // ===== u11-l1: 現在完了 =====
  { id: 'u11-l1', steps: [{ q: '現在完了とは?', intent: 'concept', contains: '完了' }] },
  { id: 'u11-l1', steps: [{ q: '現在完了' }] },
  { id: 'u11-l1', steps: [{ q: 'まとめは?', intent: 'summary' }] },
  { id: 'u11-l1', steps: [{ q: '例文は?', intent: 'example' }] },
  { id: 'u11-l1', steps: [{ q: '現在完了の例文は?', intent: 'example' }] },

  // ===== u13-l1: 受動態 =====
  { id: 'u13-l1', steps: [{ q: '受動態とは?', intent: 'concept', contains: 'be' }] },
  { id: 'u13-l1', steps: [{ q: '受け身とは?', intent: 'concept' }] },
  { id: 'u13-l1', steps: [{ q: 'byはどこに置く?' }] },
  { id: 'u13-l1', steps: [{ q: '能動態と受動態の違いは?', contains: '受動態' }] },

  // ===== 英語の質問 =====
  { id: 'u01-l1', steps: [{ q: 'what does "I am a nurse." mean?', intent: 'meaning', contains: '看護師' }] },
  { id: 'u01-l1', steps: [{ q: 'give me a hint', intent: 'quiz' }] },
  { id: 'u01-l1', steps: [{ q: 'What will I learn here?', intent: 'overview' }] },
  { id: 'u01-l1', steps: [{ q: 'difference between am and is', contains: 'am' }] },
  { id: 'u01-l1', steps: [{ q: 'how do you say "私は看護師です。" in English?', intent: 'meaning', contains: 'nurse' }] },

  // ===== その他・境界 =====
  { id: 'u01-l1', steps: [{ q: '「彼は疲れています」は英語で?' }] },
  { id: 'u01-l1', steps: [{ q: '意味と文型を教えて' }] },
  { id: 'u02-l1', steps: [{ q: 'cookingはどこで使われてる?' }] },
  { id: 'u01-l1', steps: [{ q: 'おすすめの教材は?', fallback: true }] },

  // ===== 追加の対抗ケース(別レベル・かな・英語・多段) =====
  { id: 'u23-l1', steps: [{ q: 'まとめを教えて', intent: 'summary' }] },
  { id: 'u23-l1', steps: [{ q: '例文を教えて', intent: 'example' }] },
  { id: 'u23-l1', steps: [{ q: 'このセクションで何を学ぶの?', intent: 'overview' }] },
  { id: 'u30-l1', steps: [{ q: '文型は?', intent: 'pattern' }] },
  { id: 'u30-l1', steps: [{ q: 'ヒントをちょうだい', intent: 'quiz' }] },
  { id: 'u33-l1', steps: [{ q: 'クイズは何問?', intent: 'quiz' }] },
  { id: 'u33-l1', steps: [{ q: '例文', intent: 'example' }] },
  { id: 'u13-l1', steps: [{ q: 'うけみとは?', intent: 'concept', contains: '受動態' }] },
  { id: 'u01-l2', steps: [{ q: 'さんたんげんとは?', intent: 'concept', contains: '3人称' }] },
  { id: 'u01-l2', steps: [{ q: '三単現のルールが知りたい', contains: '-s' }] },
  { id: 'u01-l1', steps: [{ q: 'このセクションのポイントを教えて', intent: 'summary' }] },
  { id: 'u01-l1', steps: [{ q: 'わからない', intent: 'quiz' }] },
  { id: 'u01-l1', steps: [{ q: 'ちょっとヒント', intent: 'quiz' }] },
  { id: 'u01-l3', steps: [{ q: 'doとdoesの使い分け', contains: 'does' }] },
  { id: 'u01-l1', steps: [{ q: 'ＡＭとＩＳの違いは？', contains: 'am' }] },
  { id: 'u01-l1', steps: [{ q: '"I am a nurse."の"am"の意味は?', contains: '看護師' }] },
  { id: 'u01-l1', steps: [{ q: '意味と例文を教えて' }] },
  { id: 'u01-l1', steps: [{ q: 'who is the president of the united states?', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: 'translate this to French', fallback: true }] },
  { id: 'u01-l3', steps: [{ q: 'what is the difference between do and does?', contains: 'does' }] },
  { id: 'u13-l1', steps: [{ q: 'explain the passive voice', intent: 'concept' }] },
  { id: 'u11-l1', steps: [{ q: 'what is the present perfect?', intent: 'concept' }] },
  { id: 'u01-l2', steps: [{ q: 'when do we use the third person singular?', intent: 'concept', contains: '3人称' }] },
  { id: 'u01-l1', steps: [{ q: 'show me an example', intent: 'example' }] },
  {
    id: 'u01-l2',
    steps: [
      { q: 'studyの三単現は?', contains: 'studies' },
      { q: 'なぜそうなるの?', intent: 'concept' },
    ],
  },
  {
    id: 'u02-l1',
    steps: [
      { q: '"I am playing tennis." は何文型?', intent: 'pattern' },
      { q: 'それの意味は?', intent: 'meaning', contains: 'テニス' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '例文を教えて' },
      { q: 'もっと簡単に言って', leadContains: 'もう一度' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: 'クイズのヒントをちょうだい' },
      { q: 'もっと詳しく' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: 'be動詞とは?' },
      { q: '他の例は?' },
    ],
  },

  // ===== 追加ラウンド: 表・活用・タイムライン・構造・多段 =====
  // u03-l1: 可算・不可算
  { id: 'u03-l1', steps: [{ q: '可算名詞とは?', intent: 'concept', contains: '数え' }] },
  { id: 'u03-l1', steps: [{ q: '不可算名詞とは?', intent: 'concept', contains: '数え' }] },
  { id: 'u03-l1', steps: [{ q: '可算名詞と不可算名詞の違いは?', intent: 'difference', contains: 'a / an' }] },
  { id: 'u03-l1', steps: [{ q: 'coffeeの数え方は?', contains: 'cups of coffee' }] },
  { id: 'u03-l1', steps: [{ q: 'adviceの数える言い方は?', contains: 'a piece of advice' }] },
  { id: 'u03-l1', steps: [{ q: 'informationの意味は?', contains: '情報' }] },
  { id: 'u03-l1', steps: [{ q: 'まとめを教えて', intent: 'summary', contains: '不可算' }] },
  { id: 'u03-l1', steps: [{ q: '不可算名詞の例文は?', intent: 'example' }] },
  { id: 'u03-l1', steps: [{ q: '数えられない名詞は?', contains: '不可算' }] },
  { id: 'u03-l1', steps: [{ q: '不可算', intent: 'concept', contains: '数え' }] },
  { id: 'u03-l1', steps: [{ q: '表を見せて', intent: 'table', contains: 'water' }] },
  // u07-l1: 比較級
  { id: 'u07-l1', steps: [{ q: 'bigの比較級は?', contains: 'bigger' }] },
  { id: 'u07-l1', steps: [{ q: 'goodの比較級は?', contains: 'better' }] },
  { id: 'u07-l1', steps: [{ q: '比較級の作り方は?', intent: 'table', contains: 'taller' }] },
  { id: 'u07-l1', steps: [{ q: 'thanはどこに置く?', contains: 'than' }] },
  { id: 'u07-l1', steps: [{ q: 'This bag is lighter than that one.の意味は?', intent: 'meaning', contains: 'カバン' }] },
  { id: 'u07-l1', steps: [{ q: '「電車はバスより料金が高いです。」は英語で?', intent: 'meaning', contains: 'expensive' }] },
  { id: 'u07-l1', steps: [{ q: '"The train is more expensive than the bus."は何文型?', intent: 'pattern', contains: 'SVC' }] },
  { id: 'u07-l1', steps: [{ q: 'goodはどう変化する?', contains: 'better' }] },
  { id: 'u07-l1', steps: [{ q: '比較級の例文を教えて', intent: 'example' }] },
  { id: 'u07-l1', steps: [{ q: 'what is the comparative form?', intent: 'concept', contains: '比較級' }] },
  { id: 'u07-l1', steps: [{ q: '比較級', intent: 'concept', contains: '比較級' }] },
  {
    id: 'u07-l1',
    steps: [
      { q: '"This bag is lighter than that one."は何文型?', intent: 'pattern' },
      { q: 'この文の意味は?', intent: 'meaning', contains: 'カバン' },
    ],
  },
  {
    id: 'u07-l1',
    steps: [
      { q: '"My brother is two years older than me."の意味は?', intent: 'meaning' },
      { q: 'それの文型は?', intent: 'pattern' },
    ],
  },
  // u12-l1: 予定の現在進行形
  { id: 'u12-l1', steps: [{ q: '現在進行形で予定を表せるの?', intent: 'concept', contains: '予定' }] },
  { id: 'u12-l1', steps: [{ q: '"I am meeting Emi for lunch tomorrow."の意味は?', intent: 'meaning', contains: 'ランチ' }] },
  { id: 'u12-l1', steps: [{ q: '「来週の金曜日、飛行機で沖縄に行きます。」は英語で?', intent: 'meaning', contains: 'Okinawa' }] },
  { id: 'u12-l1', steps: [{ q: '確定的な予定って何?', contains: '手配' }] },
  { id: 'u12-l1', steps: [{ q: '時間のイメージは?', intent: 'timeline', contains: '今の動作' }] },
  { id: 'u12-l1', steps: [{ q: '"We are flying to Okinawa next Friday."は何文型?', intent: 'pattern', contains: 'SV' }] },
  { id: 'u12-l1', steps: [{ q: '例文を教えて', intent: 'example', contains: 'Emi' }] },
  {
    id: 'u12-l1',
    steps: [
      { q: '"I am meeting Emi for lunch tomorrow."の意味は?' },
      { q: 'もっと詳しく' },
    ],
  },
  // u17-l1: 現在完了進行形
  { id: 'u17-l1', steps: [{ q: '現在完了進行形とは?', intent: 'concept', contains: 'been' }] },
  { id: 'u17-l1', steps: [{ q: '「バスを20分間待ち続けています。」は英語で?', intent: 'meaning', contains: 'waiting' }] },
  { id: 'u17-l1', steps: [{ q: '"She has been studying English since April."は何文型?', intent: 'pattern', contains: 'SVO' }] },
  { id: 'u17-l1', steps: [{ q: 'forとsinceの違いは?', contains: 'since' }] },
  { id: 'u17-l1', steps: [{ q: 'have been doingの構造は?', contains: 'studying' }] },
  { id: 'u17-l1', steps: [{ q: 'まとめを教えて', intent: 'summary', contains: 'for' }] },
  {
    id: 'u17-l1',
    steps: [
      { q: '現在完了進行形とは?' },
      { q: '例文を教えて', intent: 'example' },
    ],
  },
  // 未知語・範囲外
  { id: 'u01-l1', steps: [{ q: 'translate this to German', fallback: true }] },
  { id: 'u03-l1', steps: [{ q: 'フランス語では何て言う?', fallback: true }] },
  {
    id: 'u01-l1',
    steps: [
      { q: 'be動詞とは?' },
      { q: 'もっと詳しく' },
      { q: 'もう一度' },
    ],
  },

  // ===== 第3ラウンド: 他レベル・かな・英語・さらに多段 =====
  { id: 'u01-l3', steps: [{ q: 'doとdoesはどう使い分けるの?', intent: 'difference', contains: 'does' }] },
  { id: 'u01-l3', steps: [{ q: '"He plays tennis."の意味は?', contains: 'He plays tennis' }] },
  { id: 'u01-l3', steps: [{ q: '肯定文の例は?', intent: 'example' }] },
  { id: 'u01-l3', steps: [{ q: 'ヒントが欲しい', intent: 'quiz' }] },
  { id: 'u02-l2', steps: [{ q: 'まとめを教えて', intent: 'summary', contains: 'いつも' }] },
  { id: 'u02-l2', steps: [{ q: '例文を教えて', intent: 'example' }] },
  { id: 'u04-l2', steps: [{ q: 'thisとthatの違いは?', intent: 'difference', contains: '距離' }] },
  { id: 'u05-l2', steps: [{ q: '副詞とは?', intent: 'concept', contains: '副詞' }] },
  { id: 'u07-l2', steps: [{ q: '最上級とは?', intent: 'concept', contains: '一番' }] },
  { id: 'u07-l2', steps: [{ q: '最上級の例文は?', intent: 'example' }] },
  { id: 'u09-l2', steps: [{ q: 'mustとhave toの違いは?', intent: 'difference', contains: 'must' }] },
  { id: 'u10-l1', steps: [{ q: 'to不定詞とは?', intent: 'concept', contains: 'to' }] },
  { id: 'u11-l1', steps: [{ q: '現在完了のまとめを教えて', intent: 'summary' }] },
  { id: 'u13-l1', steps: [{ q: '受動態の例文は?', intent: 'example' }] },
  { id: 'u17-l1', steps: [{ q: '"I have been waiting for the bus for twenty minutes."は何文型?', intent: 'pattern', contains: 'SV' }] },
  { id: 'u23-l1', steps: [{ q: 'まとめを教えて', intent: 'summary' }] },
  { id: 'u30-l1', steps: [{ q: 'まとめを教えて', intent: 'summary' }] },
  { id: 'u33-l1', steps: [{ q: 'このセクションで何を学ぶの?', intent: 'overview' }] },
  // かな・一語・英語
  { id: 'u13-l1', steps: [{ q: 'うけみ', intent: 'concept', contains: '受動態' }] },
  { id: 'u11-l1', steps: [{ q: 'げんざいかんりょう', intent: 'concept', contains: '現在完了' }] },
  { id: 'u13-l1', steps: [{ q: 'passive', intent: 'concept', contains: '受動態' }] },
  { id: 'u11-l1', steps: [{ q: 'present perfect', intent: 'concept', contains: '現在完了' }] },
  { id: 'u07-l1', steps: [{ q: 'what is the comparative?', intent: 'concept', contains: '比較級' }] },
  { id: 'u07-l1', steps: [{ q: 'show me examples of the comparative', intent: 'example' }] },
  { id: 'u07-l1', steps: [{ q: 'more expensiveの意味は?', intent: 'meaning', contains: '高い' }] },
  { id: 'u01-l1', steps: [{ q: '読めない', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: '量子力学とは?', fallback: true }] },
  { id: 'u01-l1', steps: [{ q: '今の説明をもう一度', fallback: true }] },
  {
    id: 'u13-l1',
    steps: [
      { q: '受動態とは?', intent: 'concept' },
      { q: '例文を教えて', intent: 'example' },
    ],
  },
  {
    id: 'u01-l1',
    steps: [
      { q: '"I am a nurse."の意味は?' },
      { q: '"I am a nurse."はどう発音する?', intent: 'pronunciation', contains: 'nurse' },
    ],
  },
  {
    id: 'u17-l1',
    steps: [
      { q: '現在完了進行形とは?' },
      { q: 'もっと詳しく' },
      { q: '他の例は?' },
    ],
  },

  // ===== 第4ラウンド: 言い換え・崩した入力・長い多段 =====
  { id: 'u01-l1', steps: [{ q: 'be動詞って何?', intent: 'concept', contains: 'be動詞' }] },
  { id: 'u01-l1', steps: [{ q: 'be動詞の使い方を教えて', intent: 'concept', contains: 'be動詞' }] },
  { id: 'u01-l1', steps: [{ q: '今日は何を学ぶの?', intent: 'overview' }] },
  { id: 'u01-l1', steps: [{ q: '総復習したい', intent: 'summary' }] },
  { id: 'u01-l1', steps: [{ q: 'クイズの答えが知りたい', intent: 'quiz', leadContains: '言わない' }] },
  { id: 'u01-l1', steps: [{ q: 'am はどういうときに使う?', contains: 'am' }] },
  { id: 'u01-l2', steps: [{ q: '三人称単数現在って?', contains: '人称' }] },
  { id: 'u01-l2', steps: [{ q: '動詞に-sが付くのはどんなとき?', contains: '3人称' }] },
  { id: 'u01-l3', steps: [{ q: '否定文の例文は?', intent: 'example', contains: "doesn'" }] },
  { id: 'u01-l3', steps: [{ q: 'なぜdoesを使うの?', intent: 'concept' }] },
  { id: 'u03-l1', steps: [{ q: '名詞は数えられるものと数えられないものがある?', contains: '不可算' }] },
  { id: 'u07-l1', steps: [{ q: '比較級でthanはいつ使う?', contains: 'than' }] },
  { id: 'u13-l1', steps: [{ q: '受け身形の作り方は?', intent: 'concept', contains: 'be' }] },

  { id: 'u12-l1', steps: [{ q: '「今週末は何か予定ある?」は英語で?', intent: 'meaning', contains: 'weekend' }] },
  { id: 'u17-l1', steps: [{ q: 'どのくらい続いているか聞きたい', contains: 'How long' }] },
  { id: 'u01-l1', steps: [{ q: '  まとめ  ', intent: 'summary' }] },
  {
    id: 'u13-l1',
    steps: [
      { q: '受動態とは?' },
      { q: '他の例は?' },
      { q: 'もっと簡単に言って' },
    ],
  },
  {
    id: 'u01-l2',
    steps: [
      { q: '三単現の-sはなぜ必要?' },
      { q: 'もっと詳しく' },
      { q: 'もっと詳しく' },
    ],
  },
]

function textOf(reply: ChatReply): string {
  if (reply.kind === 'fallback') return reply.message
  return [
    reply.lead,
    ...reply.quotes.flatMap((quote) => [quote.label, quote.en ?? '', quote.ja ?? '', quote.note ?? '', quote.text ?? '']),
  ].join('\n')
}

function check(reply: ChatReply, step: Step): boolean {
  if (step.fallback) return reply.kind === 'fallback'
  if (reply.kind !== 'answer') return false
  if (step.intent && reply.intent !== step.intent) return false
  if (step.leadContains && !reply.lead.includes(step.leadContains)) return false
  if (step.contains && !textOf(reply).includes(step.contains)) return false
  return true
}

describe('判定精度の評価セット', () => {
  it(
    '正解率を計測し、しきい値を満たす',
    () => {
    let passed = 0
    let total = 0
    const failures: string[] = []
    for (const item of CASES) {
      const lesson = findLesson(item.id)
      if (!lesson) throw new Error(`レッスンが見つかりません: ${item.id}`)
      const chat = createSectionChat(lesson, () => 0)
      item.steps.forEach((step, index) => {
        total += 1
        const reply = chat.reply(step.q)
        if (!check(reply, step)) {
          const actual = reply.kind === 'answer' ? `${reply.intent}/${textOf(reply).replace(/\n/g, ' ').slice(0, 60)}` : 'fallback'
          failures.push(`${item.id} step${index + 1} "${step.q}" -> ${actual}`)
        } else {
          passed += 1
        }
      })
    }
    const accuracy = passed / total
    console.log(`ACCURACY ${passed}/${total} = ${(accuracy * 100).toFixed(1)}%`)
    if (failures.length > 0) console.log(`FAILURES(${failures.length}):\n${failures.join('\n')}`)
    expect(accuracy).toBeGreaterThanOrEqual(0.9)
    },
    30_000,
  )
})
