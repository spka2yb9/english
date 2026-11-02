import type { GrammarExample, LessonBlock, QuizQuestion, SentencePattern, SentenceRole } from '../types'
import type { LessonAnimation } from '../grammar/animations'
import { PATTERN_LABELS } from '../grammar/patterns/types.ts'
import {
  patternAnimations,
  patternBlocks,
  patternExamples,
  patternShowcases,
  roleBlocks,
  roleGuides,
  wordOrderAnimation,
} from '../grammar/structures/index.ts'
import { THREE_MINUTE_PATTERN_INTRO_ID, THREE_MINUTE_PATTERN_INTRO_TITLE } from './ids.ts'
import type {
  ThreeMinuteLine,
  ThreeMinuteMood,
  ThreeMinutePart,
  ThreeMinuteSection,
  ThreeMinuteSpeaker,
} from './types'

const INGBIRD: ThreeMinuteSpeaker = 'ingbird'
const HIYOKO: ThreeMinuteSpeaker = 'hiyoko'

const ROLE_NAMES: Record<SentenceRole, { name: string; meaning: string }> = {
  S: { name: '主語', meaning: '「だれが・何が」' },
  V: { name: '動詞', meaning: '文の中心。「する・だ・なる」' },
  O: { name: '目的語', meaning: '動作の対象。「何を・だれに」' },
  C: { name: '補語', meaning: '主語や目的語を説明する。「どんな状態か」' },
  M: { name: '修飾語', meaning: 'いつ・どこで・どんなふうに。骨格には入らない' },
}

const SV_WITH_M: GrammarExample = {
  en: 'My father works at a bank.',
  ja: '父は銀行で働いています。',
  highlight: 'works',
  pattern: 'SV',
  patternNote: 'at a bank は場所を表す修飾語(M)。外しても My father works. で SV。',
}

const SVO_WITH_TO: GrammarExample = {
  en: 'He gave a book to me.',
  ja: '彼は私に本をくれました。',
  highlight: 'gave a book',
  pattern: 'SVO',
  patternNote: '目的語は a book ひとつ。to me は修飾語(M)。',
}

function examplesOf(pattern: SentencePattern): GrammarExample[] {
  return patternExamples.filter((example) => example.pattern === pattern)
}

function examplesBlock(title: string, items: GrammarExample[]): LessonBlock {
  return { type: 'examples', title, items }
}

/** 英文の作られ方ページと同じブロックを、見出しで参照する。 */
function patternBlock(title: string): LessonBlock {
  const block = patternBlocks.find((item) => 'title' in item && item.title === title)
  if (!block) throw new Error(`5文型の導入: ブロック「${title}」が見つかりません。`)
  return block
}

const roleTable: LessonBlock = {
  type: 'table',
  title: 'S / V / O / C / M の役割',
  headers: ['記号', '名前', '何を表すか', '例'],
  rows: roleGuides.map((guide) => [
    guide.role,
    ROLE_NAMES[guide.role].name,
    ROLE_NAMES[guide.role].meaning,
    guide.example,
  ]),
}

const decisionTable: LessonBlock = {
  type: 'table',
  title: 'Vのあとを見ると、文型が決まる',
  headers: ['Vのあとに続くもの', '見分け方', '文型'],
  rows: [
    ['OもCも続かない', 'Mが続いても骨格は S + V', '第1文型 SV'],
    ['名詞・形容詞が1つ', 'S = その語（主語の説明）', '第2文型 SVC'],
    ['名詞が1つ', '動作の対象（S ≠ その語）', '第3文型 SVO'],
    ['名詞が2つ', '人 → もの（O同士はイコールでない）', '第4文型 SVOO'],
    ['名詞 + 説明する語', 'O = C', '第5文型 SVOC'],
  ],
}

const relationTable: LessonBlock = {
  type: 'table',
  title: 'O = C かどうかで見分ける',
  headers: ['文', 'O と C', '関係', '文型'],
  rows: [
    ['My father gave me a camera.', 'me / a camera', 'me ≠ a camera', 'SVOO'],
    ['They named the baby Emma.', 'the baby / Emma', 'the baby = Emma', 'SVOC'],
  ],
}

const svcWithPlace: LessonBlock = {
  type: 'breakdown',
  title: 'be動詞のあとが、いつもCとは限らない',
  sentence: 'She is in the kitchen.',
  ja: '彼女は台所にいます。',
  pattern: 'SV',
  parts: [
    { text: 'She', role: 'S' },
    { text: 'is', role: 'V' },
    { text: 'in the kitchen.', role: 'M', note: '場所を表す修飾語' },
  ],
  skeleton: 'She is.',
  skeletonPattern: 'SV',
  caption:
    'in the kitchen は「どこにいるか」を足す修飾語(M)です。She = in the kitchen ではないので補語(C)ではありません。骨格は She is. の SV です。',
}

const summaryTable: LessonBlock = {
  type: 'table',
  title: '5文型 早見表',
  headers: ['文型', '骨組み', '例', '見分け方'],
  rows: patternShowcases.map((showcase) => [
    PATTERN_LABELS[showcase.pattern],
    showcase.skeleton,
    `${showcase.example.en}（${showcase.example.ja}）`,
    `${showcase.relation ? `${showcase.relation}。` : ''}${showcase.example.note}`,
  ]),
}

const parts: ThreeMinutePart[] = []

const say = (
  speaker: ThreeMinuteSpeaker,
  text: string,
  mood: ThreeMinuteMood = 'happy',
  extra?: Pick<ThreeMinuteLine, 'en' | 'ja' | 'highlight'>,
) => {
  parts.push({ kind: 'line', line: { speaker, text, mood, ...extra } })
}

const show = (block: LessonBlock, label: string) => {
  parts.push({ kind: 'block', block, label })
}

const animate = (animation: LessonAnimation) => {
  parts.push({ kind: 'animation', animation })
}

say(INGBIRD, 'やっほー、ヒヨコ君! 今日は特別に、英語の文の「骨組み」をぜんぶ見てしまおう。', 'cheer')
say(HIYOKO, 'ぜんぶ? 5文型ってやつ? 名前は聞いたことがあるけど、呪文みたいで苦手なんだ…', 'think')
say(
  INGBIRD,
  '大丈夫。5文型は暗記する呪文じゃないよ。英文を組み立てるときの「型」で、**動詞(V)のあとに何が続くか** だけで決まるんだ。',
  'happy',
)
say(
  INGBIRD,
  '今日のゴールは、どんな文でも **S・V・O・C・M** に分けて、5つの型のどれかを言えるようになること。',
  'proud',
)
say(HIYOKO, 'ちゅん! 今日で5文型を卒業しちゃうよ!', 'cheer')

say(
  INGBIRD,
  'まずは、どうして語順が大事なのかから。日本語なら「ケンがマリを愛している」と、助詞の「が」「を」が役割を教えてくれるよね。',
  'happy',
)
say(INGBIRD, 'でも英語には、その助詞がない。だから **語順そのもの** が「だれが・何を」を決めるんだ。', 'think')
say(INGBIRD, 'たとえば、この文。', 'happy', {
  en: 'Ken loves Mari.',
  ja: 'ケンがマリを愛しています。',
  highlight: 'Ken loves Mari',
})
say(INGBIRD, 'そして、語の順番を入れ替えると…', 'think', {
  en: 'Mari loves Ken.',
  ja: 'マリがケンを愛しています。',
  highlight: 'Mari loves Ken',
})
say(HIYOKO, 'えっ、同じ3語なのに意味が反対!? 順番、こわい〜。', 'wow')
say(INGBIRD, 'でしょ? だから英文を読むときは、まず「だれが・する・何を」の順番を取り出す。これが5文型の第一歩。', 'happy')
animate(wordOrderAnimation)
say(HIYOKO, '動詞の前に主語、動詞のあとに目的語。まずはこの並びなんだね!', 'curious')

say(INGBIRD, '次に、文の中の役割に名前をつけよう。S・V・O・C・M の5つ。', 'happy')
show(roleTable, 'S / V / O / C / M の役割')
say(HIYOKO, 'Sは主語、Vは動詞、Oは目的語、Cは補語、Mは修飾語…アルファベットがいっぱいで、ちょっとこんがらがるよ。', 'think')
say(HIYOKO, 'Mって、マンゴーのM? 文型にフルーツが出てくるの?', 'curious')
say(INGBIRD, 'マンゴーじゃない! Mは修飾語。飾りだから、なくても文は成り立つ。', 'proud')
say(
  INGBIRD,
  '覚え方は簡単。**S と V はどの文にもいる**。O と C は動詞が「必要とするか」で決まる。M はいてもいなくてもいい飾り。',
  'proud',
)
show(roleBlocks[0], '1つの文で役割を確かめる')
say(INGBIRD, 'My sister gave me a book yesterday. なら、yesterday は「いつ」を足す M。外しても骨格は壊れない。', 'happy')
say(INGBIRD, 'Mを外すと **My sister gave me a book.** が残る。これがこの文の骨格だよ。', 'happy')
say(HIYOKO, '飾りをはがすと、文の骨が見えるんだ! おもしろい!', 'wow')

say(INGBIRD, '5文型の見分け方は、たった3ステップ。', 'happy')
say(INGBIRD, '- ① 動詞(V)を探す\n- ② Vの前に主語(S)を探す\n- ③ Vのあとに何が続くかを見る', 'think')
show(decisionTable, 'Vのあとを見ると、文型が決まる')
say(HIYOKO, 'ふむふむ…でも「名詞が2つ」って、SVOOとSVOCのどっちか迷わない?', 'curious')
say(INGBIRD, 'いい質問! そこが最大の分かれ道。**2つの語がイコールかどうか** で決めるんだ。', 'proud')
show(relationTable, 'O = C かどうかで見分ける')
say(INGBIRD, 'My father gave me a camera. の me と a camera は、イコールじゃない。別のものだから **SVOO**。', 'happy')
say(
  INGBIRD,
  'They named the baby Emma. は the baby = Emma。同じ人を指しているから **SVOC**。この「=」が見えたら勝ち。',
  'cheer',
)
say(HIYOKO, '「イコールかどうか」かぁ! 呪文よりずっとわかりやすい!', 'cheer')

say(INGBIRD, 'じゃあ、5つを順番に見ていこう。まず第1文型 **SV**。', 'cheer')
animate(patternAnimations.SV)
say(HIYOKO, '鳥が飛ぶ! 目的語も補語もないね。', 'curious')
say(
  INGBIRD,
  'そう。動詞のあとに何もいらない文。sleep, walk, arrive, happen のように、目的語を取らない動詞で作るよ。',
  'happy',
)
show(examplesBlock('第1文型 SV の例', [...examplesOf('SV'), SV_WITH_M]), '第1文型 SV の例')
say(
  INGBIRD,
  'in the sky や at a bank は場所を表す M。外しても **Birds fly.** / **My father works.** で文になる。これが SV の合図。',
  'proud',
)
say(HIYOKO, '修飾語がついても、骨格は S + V のままなんだね!', 'happy')

say(INGBIRD, '次は第2文型 **SVC**。Vのあとの語が **主語を説明する** 型だよ。', 'happy')
animate(patternAnimations.SVC)
say(INGBIRD, 'My sister = a nurse。だから a nurse は補語(C)。be動詞や become, look, seem のあとによく出るよ。', 'happy')
show(examplesBlock('第2文型 SVC の例', examplesOf('SVC')), '第2文型 SVC の例')
say(INGBIRD, 'ここで注意。be動詞のあとだからといって、いつも SVC とは限らない。', 'think')
show(svcWithPlace, 'be動詞のあとが、いつもCとは限らない')
say(HIYOKO, 'えっ、be動詞なのに SV? 場所は C じゃないんだ!', 'wow')
say(INGBIRD, 'そう。C は「S = C」の関係があるときだけ。場所や時間は M と覚えておこう。', 'proud')

say(INGBIRD, '第3文型 **SVO** は、動詞のあとに **動作の対象** が1つ。', 'happy')
animate(patternAnimations.SVO)
show(examplesBlock('第3文型 SVO の例', [...examplesOf('SVO'), SVO_WITH_TO]), '第3文型 SVO の例')
say(INGBIRD, 'yesterday は M。to me も M。だから骨格は **I bought a new bike.** と **He gave a book.** の SVO。', 'happy')
say(HIYOKO, '「〜に」があるから SVOO かと思ったけど、to がついたら M なんだね!', 'curious')
say(INGBIRD, 'その通り。**to / for + 人** は修飾語。SVOO は「人 + もの」をそのまま並べたときだけだよ。', 'proud')

say(INGBIRD, '第4文型 **SVOO**。目的語が2つ並ぶ型。', 'happy')
say(HIYOKO, 'SVOが2つなら、SVO2って呼べばいいじゃん!', 'cheer')
say(INGBIRD, '呼び方を勝手に変えるな! SVOOだ。Oが2つ並ぶから第4文型。', 'proud')
animate(patternAnimations.SVOO)
say(INGBIRD, '順番は **人 → もの**。give, send, show, teach などが代表だよ。', 'happy')
show(examplesBlock('第4文型 SVOO の例', examplesOf('SVOO')), '第4文型 SVOO の例')
say(INGBIRD, 'もう一度、O同士の関係を確かめよう。me と a camera はイコールじゃない。だから SVOO。', 'think')
show(patternBlock('第4文型と「to + 人」の言い換え'), 'SVOO と「to + 人」の言い換え')
say(HIYOKO, '同じ出来事でも、人を先にするか、to で後ろに回すかで文型が変わるんだ!', 'wow')
say(INGBIRD, 'そう。どちらも正しいけど、**型は別**。to がついたら SVO と覚えると迷わないよ。', 'proud')

say(INGBIRD, '最後は第5文型 **SVOC**。O と C が **O = C** の関係になる型。', 'cheer')
animate(patternAnimations.SVOC)
say(INGBIRD, 'The news made everyone happy. なら everyone = happy。They named the baby Emma. なら the baby = Emma。', 'happy')
show(examplesBlock('第5文型 SVOC の例', examplesOf('SVOC')), '第5文型 SVOC の例')
say(INGBIRD, 'ここが一番の落とし穴。O のあとに語が続いても、それが O を説明していなければ C じゃない。', 'think')
show(patternBlock('C は目的語を説明する'), 'C は目的語を説明する')
show(patternBlock('似ているが C ではない文'), '似ているが C ではない文')
say(
  INGBIRD,
  'very useful は the book を説明するから C。yesterday は「いつ」を足すだけだから M。同じ found でも、続く語の働きで文型が変わるんだ。',
  'proud',
)
say(HIYOKO, 'the book = very useful は成り立つ。the book = yesterday は成り立たない。だから C か M かがわかるんだね!', 'cheer')
say(INGBIRD, '完璧! その「=」のテストが、SVOCを見抜く魔法の合言葉。', 'proud')

say(INGBIRD, 'さいごに、5つを並べておこう。暗記しなくていい。**Vのあとに何があるか** で思い出してね。', 'happy')
show(summaryTable, '5文型 早見表')
say(INGBIRD, '第4文型と第5文型は、Oが2つに見えても **O = C** なら SVOC、イコールでなければ SVOO。', 'proud')
say(HIYOKO, 'よし! 5つの顔、ちゃんと区別できる気がする!', 'cheer')

say(INGBIRD, 'じゃあ、ヒヨコ君。この文の文型は?', 'cheer', {
  en: 'I found the book very useful.',
  ja: '私はその本がとても役に立つと分かりました。',
})
say(HIYOKO, 'えっと… found のあとに the book があるから **SVO**!', 'think')
say(INGBIRD, 'おしい! でもね、very useful は the book を説明しているよ。the book = very useful だから **SVOC**。', 'happy')
say(HIYOKO, 'あっ! Cを見落としてた! O = C のテストをするんだった!', 'wow')
say(
  INGBIRD,
  'そう。Oのあとに語が続いたら、必ず「この語はOを説明している?」って聞いてみて。説明していれば C、していなければ M。',
  'proud',
)

say(INGBIRD, '今日のポイントを振り返ろう!', 'cheer')
say(INGBIRD, '**S と V はどの文にもある**。まず V を探し、その前に S を見つける。', 'happy')
say(HIYOKO, 'まず動詞! それから主語だね!', 'curious')
say(INGBIRD, '**Vのあとに O や C がいくつ続くか** で5文型が決まる。M は数えない。', 'happy')
say(HIYOKO, '場所や時間は M。骨格の外側だね!', 'happy')
say(INGBIRD, '**O = C が成り立てば SVOC**、O同士がイコールでなければ SVOO。', 'happy')
say(HIYOKO, '「=」のテスト、忘れないよ!', 'cheer')
say(INGBIRD, 'これで5文型の地図は完成。次からは、この地図を使って1つずつ文法を見ていこう!', 'proud')
say(HIYOKO, 'ちゅん! 5文型、卒業できた気がする! ありがとう、イングバード先生!', 'cheer')

export const patternIntroQuiz: QuizQuestion[] = [
  {
    id: 'tm-pattern-q1',
    prompt: '次の文の文型を選んでください。',
    sentence: 'Birds fly.',
    sentenceJa: '鳥は飛びます。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOO(第4文型)'],
    correctIndex: 0,
    explanation: 'fly は目的語も補語も必要としない動詞です。Birds + fly だけで文が完成するので SV(第1文型)です。',
    choiceNotes: [
      null,
      'SVC なら、動詞のあとに主語を説明する補語(C)が必要です。fly のあとには補語がありません。',
      'SVO なら、動詞のあとに動作の対象(目的語)が必要です。この文には目的語がありません。',
      'SVOO は目的語を2つ取る型です。この文には目的語がありません。',
    ],
    audioEn: 'Birds fly.',
  },
  {
    id: 'tm-pattern-q2',
    prompt: '次の文の文型を選んでください。',
    sentence: 'My sister is a nurse.',
    sentenceJa: '姉は看護師です。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOC(第5文型)'],
    correctIndex: 1,
    explanation:
      'is のうしろの a nurse は主語 My sister を説明する補語(C)です。My sister = a nurse の関係なので SVC(第2文型)です。ただし、be動詞のうしろがいつもCとは限りません。She is in the kitchen. の in the kitchen は場所を表す修飾語(M)なので SV です。',
    choiceNotes: [
      'SV は目的語も補語も取らない型です。is のうしろの a nurse は主語を説明する補語(C)です。',
      null,
      'SVO の O は動作の対象です。a nurse は対象ではなく、主語 My sister の説明です。',
      'SVOC には目的語(O)が必要です。この文に目的語はなく、a nurse は主語を説明する補語(C)です。',
    ],
    audioEn: 'My sister is a nurse.',
  },
  {
    id: 'tm-pattern-q3',
    prompt: '次の文の文型を選んでください。',
    sentence: 'I bought a new bike yesterday.',
    sentenceJa: '私は昨日新しい自転車を買いました。',
    choices: ['SV(第1文型)', 'SVC(第2文型)', 'SVO(第3文型)', 'SVOC(第5文型)'],
    correctIndex: 2,
    explanation:
      'a new bike が動作の対象で目的語(O)です。yesterday は時を表す修飾語(M)なので要素に数えず、骨格は I bought a new bike. の SVO(第3文型)です。',
    choiceNotes: [
      'SV には目的語がありません。この文には a new bike という目的語があります。',
      'SVC のうしろは主語の説明です。a new bike は動作の対象なので目的語(O)です。',
      null,
      'SVOC には目的語を説明する補語(C)が必要です。yesterday は bought を修飾するだけで、bike を説明していません。',
    ],
    audioEn: 'I bought a new bike yesterday.',
  },
  {
    id: 'tm-pattern-q4',
    prompt: '次の文の文型を選んでください。',
    sentence: 'My father gave me a camera.',
    sentenceJa: '父は私にカメラをくれました。',
    choices: ['SVC(第2文型)', 'SVO(第3文型)', 'SVOO(第4文型)', 'SVOC(第5文型)'],
    correctIndex: 2,
    explanation:
      'me と a camera の2つが目的語(O)です。「人 → もの」の順で、me ≠ a camera なので SVOO(第4文型)です。',
    choiceNotes: [
      'SVC のうしろは主語の説明です。me と a camera はどちらも動作の対象で、補語ではありません。',
      'SVO の目的語は1つです。この文には me と a camera の2つがあります。',
      null,
      'SVOC なら me = a camera の関係が必要です。me と a camera は別のものなので SVOC ではありません。',
    ],
    audioEn: 'My father gave me a camera.',
  },
  {
    id: 'tm-pattern-q5',
    prompt: '次の文の文型を選んでください。',
    sentence: 'The news made everyone happy.',
    sentenceJa: 'その知らせはみんなを幸せにしました。',
    choices: ['SVO(第3文型)', 'SVOO(第4文型)', 'SVOC(第5文型)', 'SVC(第2文型)'],
    correctIndex: 2,
    explanation:
      'everyone が目的語(O)、happy がその目的語を説明する補語(C)です。everyone = happy の関係があるので SVOC(第5文型)です。',
    choiceNotes: [
      'SVO なら happy は続きません。happy が everyone を説明しているので、目的語のあとに補語がある SVOC です。',
      'SVOO の2つ目は「もの」にあたる目的語です。happy は形容詞で、everyone を説明する補語(C)です。',
      null,
      'SVC の補語は主語を説明します。happy が説明しているのは主語 the news ではなく、目的語 everyone です。',
    ],
    audioEn: 'The news made everyone happy.',
  },
  {
    id: 'tm-pattern-q6',
    prompt: '次の文の文型を選んでください。',
    sentence: 'I found the book very useful.',
    sentenceJa: '私はその本がとても役に立つと分かりました。',
    choices: ['SVO(第3文型)', 'SVOO(第4文型)', 'SVOC(第5文型)', 'SV(第1文型)'],
    correctIndex: 2,
    explanation:
      'the book が目的語(O)、very useful がその目的語を説明する補語(C)です。the book = very useful の関係があるので SVOC(第5文型)です。',
    choiceNotes: [
      'SVO なら the book のあとに説明の語は続きません。very useful が続いているので SVO ではありません。',
      'SVOO の2つ目は「もの」にあたる目的語です。very useful は the book を説明する補語(C)です。',
      null,
      'SV は目的語も補語も取らない型です。この文には the book という目的語があります。',
    ],
    audioEn: 'I found the book very useful.',
  },
  {
    id: 'tm-pattern-q7',
    prompt: '次の文の文型を選んでください。',
    sentence: 'He gave a book to me.',
    sentenceJa: '彼は私に本をくれました。',
    choices: ['SVOO(第4文型)', 'SVO(第3文型)', 'SVOC(第5文型)', 'SVC(第2文型)'],
    correctIndex: 1,
    explanation:
      '目的語は a book ひとつだけです。to me は「だれに」を足す修飾語(M)なので、骨格は He gave a book. の SVO(第3文型)です。',
    choiceNotes: [
      'SVOO は「人 + もの」をそのまま並べます。to me がついているので、目的語は a book ひとつです。',
      null,
      'SVOC には目的語を説明する補語(C)が必要です。to me は修飾語(M)です。',
      'SVC のうしろは主語の説明です。a book は動作の対象で目的語(O)です。',
    ],
    audioEn: 'He gave a book to me.',
  },
  {
    id: 'tm-pattern-q8',
    prompt: 'They named the baby Emma. で成り立つ関係を選んでください。',
    sentenceJa: '第5文型の目的語と補語の関係を確かめます。',
    choices: ['the baby = Emma', 'the baby → Emma', 'They = Emma', 'the baby = They'],
    correctIndex: 0,
    explanation:
      '第5文型(SVOC)では目的語(O)と補語(C)の間に「O = C」の関係があります。named のあとは the baby = Emma です。',
    choiceNotes: [
      null,
      '矢印ではなくイコールの関係です。Emma は the baby の名前を説明しています。',
      'Emma が説明しているのは They ではなく、目的語の the baby です。',
      'They は主語(S)、the baby は目的語(O)です。イコールの関係にはなりません。',
    ],
    audioEn: 'They named the baby Emma.',
  },
]

export const patternIntroSection: ThreeMinuteSection = {
  lessonId: THREE_MINUTE_PATTERN_INTRO_ID,
  title: THREE_MINUTE_PATTERN_INTRO_TITLE,
  level: 'A2',
  unitId: 'intro',
  unitTitle: 'はじめに',
  objective:
    'S / V / O / C / M の役割と、SV・SVC・SVO・SVOO・SVOC の5つの骨組みを、どんな文でも見分けられるようになります。',
  minutes: 9,
  parts,
  terms: [
    { term: '主語(S)', plain: '文の「だれが・何が」にあたる部分。英語では動詞の前に置きます。' },
    { term: '動詞(V)', plain: '動作や状態を表す語。文の中心になります。' },
    { term: '目的語(O)', plain: '動詞の動作の対象。「〜を・〜に」にあたる語です。' },
    { term: '補語(C)', plain: '主語や目的語を説明する語。「S = C」「O = C」の関係になるときの C です。' },
    { term: '修飾語(M)', plain: '文の骨格に情報を足す飾り。場所・時・様子などを表し、外しても文は成り立ちます。' },
    { term: '5文型', plain: 'SV・SVC・SVO・SVOO・SVOC の5つの骨組み。動詞のあとに何が続くかで決まります。' },
  ],
  quiz: patternIntroQuiz,
}
