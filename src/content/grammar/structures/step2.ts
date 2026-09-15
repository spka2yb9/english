// STEP 2「動詞を中心に文を見る」の構造データ。
//
// 時制・進行形・完了形・助動詞・受動態は、どれも「骨格はそのままで動詞の部分が変わる」
// という視点でまとめる。動詞が変わると文全体の意味がどう変わるかを見せる。

import type { LessonStructureMap } from './types.ts'

export const step2Structures: LessonStructureMap = {
  // 現在進行形: 動詞の部分が2語になっても骨格は変わらない。
  'u02-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '進行形でも骨格は変わらない',
        sentence: 'I am playing tennis.',
        ja: '私はテニスをしています。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'am playing', role: 'V', note: 'be動詞 + -ing で1つの動詞' },
          { text: 'tennis.', role: 'O' },
        ],
        skeleton: 'I play tennis.',
        skeletonPattern: 'SVO',
        caption:
          '動詞の部分が am playing と2語になっても、骨格は I + play + tennis の SVO のままです。変わったのは動詞の形で、意味が「習慣」から「今している最中」に移りました。',
      },
      {
        type: 'breakdown',
        title: '現在形と並べて見る',
        sentence: 'I play tennis every Sunday.',
        ja: '私は毎週日曜日にテニスをします。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'play', role: 'V' },
          { text: 'tennis', role: 'O' },
          { text: 'every Sunday.', role: 'M', note: '習慣を支える「いつ」の情報' },
        ],
        skeleton: 'I play tennis.',
        skeletonPattern: 'SVO',
        caption:
          '2つの文を並べると、違いは動詞の形だけだと分かります。骨格を先に取っておくと、時制の違いは「動詞の部分」だけを見ればよくなります。',
      },
    ],
    quiz: [
      {
        id: 'u02-l1-s1',
        prompt: '文の動詞(V)にあたる部分を選んでください。',
        sentence: 'My sister is reading a book.',
        sentenceJa: '姉は本を読んでいます。',
        choices: ['My sister', 'is reading', 'a book', 'is'],
        correctIndex: 1,
        explanation: 'is reading は「be動詞 + -ing」でひとまとまりの動詞(V)です。1語ずつに分けず、動詞の部分としてまとめて捉えます。',
        choiceNotes: [
          'My sister は主語(S)です。',
          null,
          'a book は動作の対象で目的語(O)です。',
          'is だけでは「読んでいる」という意味になりません。-ing と合わせて1つの動詞です。',
        ],
        audioEn: 'My sister is reading a book.',
      },
      {
        id: 'u02-l1-s2',
        prompt: 'I play tennis. と I am playing tennis. で変わっているのはどの部分ですか。',
        sentenceJa: '骨格と動詞の形を分けて考えます。',
        choices: ['文の骨格(S + V + O)', '動詞の形', '主語', '目的語'],
        correctIndex: 1,
        explanation: '変わるのは動詞の形(play → am playing)だけで、骨格はどちらも SVO のままです。',
        choiceNotes: [
          '骨格はどちらも S + V + O で変わりません。',
          null,
          '主語はどちらも I です。',
          '目的語はどちらも tennis です。',
        ],
        audioEn: 'I am playing tennis.',
      },
    ],
  },

  // 現在完了: have + 過去分詞も「1つの動詞」として骨格を見る。
  'u11-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: 'have + 過去分詞で1つの動詞',
        sentence: 'I have lost my key.',
        ja: '私は鍵をなくしてしまいました。',
        pattern: 'SVO',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'have lost', role: 'V', note: 'have + 過去分詞で1つの動詞' },
          { text: 'my key.', role: 'O' },
        ],
        caption:
          '完了形になっても骨格は SVO のままです。変わるのは動詞の部分で、過去形 I lost my key. が「過去の出来事」を述べるのに対し、現在完了は「今どうなっているか」まで伝えます。',
      },
      {
        type: 'breakdown',
        title: '期間や場所は骨格の外側',
        sentence: 'I have lived in Osaka for five years.',
        ja: '私は5年間大阪に住んでいます。',
        pattern: 'SV',
        parts: [
          { text: 'I', role: 'S' },
          { text: 'have lived', role: 'V' },
          { text: 'in Osaka', role: 'M', note: 'どこに' },
          { text: 'for five years.', role: 'M', note: 'どれだけの期間' },
        ],
        skeleton: 'I have lived in Osaka.',
        skeletonPattern: 'SV',
        caption:
          'live は目的語を取らない動詞なので、骨格は S + V の第1文型です。期間の for five years は「どれだけ」を足す修飾語(M)で、骨格の外側にあります。',
      },
    ],
    quiz: [
      {
        id: 'u11-l1-s1',
        prompt: 'I have lost my key. の have lost は文の中でどの役割ですか。',
        sentenceJa: '動詞の部分をひとまとまりで捉えます。',
        choices: ['主語(S)', '動詞(V)', '目的語(O)', '修飾語(M)'],
        correctIndex: 1,
        explanation: 'have + 過去分詞はひとまとまりで動詞(V)です。完了形でも文の中心は動詞です。',
        choiceNotes: ['主語は I です。', null, '目的語は my key です。', '修飾語ではありません。意味の中心になる動詞の部分です。'],
        audioEn: 'I have lost my key.',
      },
      {
        id: 'u11-l1-s2',
        prompt: '完了形の文で、動詞の部分を正しく捉えているものを選んでください。',
        sentence: 'She has finished her homework.',
        sentenceJa: '彼女は宿題を終えてしまいました。',
        choices: ['has', 'finished', 'has finished', 'her homework'],
        correctIndex: 2,
        explanation: 'has + 過去分詞 finished でひとまとまりの動詞(V)です。have / has だけでは意味が完成しません。',
        choiceNotes: [
          'has だけでは「終えた」という意味になりません。',
          'finished だけでは現在完了の形になりません。',
          null,
          'her homework は目的語(O)です。',
        ],
        audioEn: 'She has finished her homework.',
      },
    ],
  },

  // 受動態: 目的語が主語の席へ移るので、骨格は SV になる。
  'u13-l1': {
    blocks: [
      {
        type: 'breakdown',
        title: '能動態: する側が主語',
        sentence: 'The city built this bridge.',
        ja: '市がこの橋を建てました。',
        pattern: 'SVO',
        parts: [
          { text: 'The city', role: 'S', note: 'する側' },
          { text: 'built', role: 'V' },
          { text: 'this bridge.', role: 'O', note: 'される物' },
        ],
        caption: '能動態では「する側」が主語(S)、「される物」が目的語(O)です。骨格は SVO です。',
      },
      {
        type: 'breakdown',
        title: '受動態: 目的語だった語が主語の席へ',
        sentence: 'This bridge was built by the city.',
        ja: 'この橋は市によって建てられました。',
        pattern: 'SV',
        parts: [
          { text: 'This bridge', role: 'S', note: 'もとは built の目的語だった語' },
          { text: 'was built', role: 'V', note: 'be + 過去分詞で1つの動詞' },
          { text: 'by the city.', role: 'M', note: '誰がしたか。省けることもある' },
        ],
        skeleton: 'This bridge was built.',
        skeletonPattern: 'SV',
        caption:
          '受動態では、もと目的語だった This bridge が主語の席に移ります。動詞のあとに目的語が残らないので、骨格は S + V の第1文型になります。',
      },
    ],
    quiz: [
      {
        id: 'u13-l1-s1',
        prompt: 'This bridge was built by the city. の主語(S)を選んでください。',
        sentenceJa: '受動態ではだれが主語になるかを確かめます。',
        choices: ['This bridge', 'was built', 'the city', 'by the city'],
        correctIndex: 0,
        explanation: '受動態では、もとは目的語だった This bridge が主語の席に来ます。文が「何について述べているか」を示す語が S です。',
        choiceNotes: [
          null,
          'was built は be + 過去分詞でまとめて動詞(V)です。',
          'the city は by といっしょに「誰がしたか」を表す修飾部分の中にあります。',
          'by the city は行為者を表す修飾語(M)です。',
        ],
        audioEn: 'This bridge was built by the city.',
      },
      {
        id: 'u13-l1-s2',
        prompt: '受動態にすると骨格が 第1文型(SV) になるのはなぜですか。',
        sentenceJa: '目的語がどうなるかに注目します。',
        choices: [
          '目的語が主語の席へ移り、動詞のあとに目的語が残らないから',
          'be動詞が入るので目的語が不要になるから',
          'by句が目的語の代わりになるから',
          '主語が省略されるから',
        ],
        correctIndex: 0,
        explanation:
          '受動態では、もと目的語だった語が主語の席に移ります。動詞のあとに目的語が残らないので、骨格は S + V だけになります。',
        choiceNotes: [
          null,
          'be動詞が入っても、目的語を取らないから SV になるという説明にはなりません。',
          'by句は「誰がしたか」を足す修飾語で、目的語の代わりではありません。',
          '受動態でも主語は必要です。省かれることが多いのは行為者のほうです。',
        ],
        audioEn: 'This bridge was built by the city.',
      },
    ],
  },
}
