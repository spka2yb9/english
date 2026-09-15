import { Link } from 'react-router-dom'
import { EnglishExample } from '../components/EnglishExample'
import { GrammarAnimation } from '../components/GrammarAnimation'
import { GrammarRoadmap } from '../components/GrammarRoadmap'
import { LessonBlocks } from '../components/LessonBlocks'
import { Quiz } from '../components/Quiz'
import { RichText } from '../components/RichText'
import { RoleGuide } from '../components/RoleGuide'
import { SentencePatternCard } from '../components/SentencePatternCard'
import { WordOrder } from '../components/WordOrder'
import { grammarRoadmap } from '../content/grammar/roadmap'
import {
  patternAnimations,
  patternBlocks,
  patternExamples,
  patternQuiz,
  patternShowcases,
  roleBlocks,
  roleGuides,
  wordOrderAnimation,
  wordOrderBlocks,
  wordOrderExamples,
  wordOrderQuiz,
} from '../content/grammar/structures'
import { PATTERN_ORDER } from '../content/grammar/patterns/types'
import { SKELETON_GUIDE } from '../content/grammar/structures/roles'
import { wordOrderSentencesFromExamples } from '../services/derivedItems'
import { recordGrammarItemAnswer } from '../services/progress'

/**
 * ページの例文から作る並べ替え。旧 u01-l4 / u01-l5 の産出練習を引き継ぐ。
 * 4語未満の文は除き、掲載順に最大10問。
 */
const guideWordOrderSentences = wordOrderSentencesFromExamples([...wordOrderExamples, ...patternExamples])

/**
 * 「英文の作られ方から学ぶ」ページ。
 * 英文法の一覧からリンクで飛び、ここから各セクション(既存ルート)へ進む。
 * 旧 u01-l4「英語の語順 SVO」と旧 u01-l5「5文型で文の骨組みを見る」を統合し、
 * その内容を STEP 1 の詳しい解説として置いている。
 */
export function GrammarRoadmapPage() {
  const record = (questionId: string, correct: boolean) => {
    recordGrammarItemAnswer(questionId, correct)
  }

  return (
    <div className="page lesson-page">
      <nav className="lesson-breadcrumb" aria-label="パンくず">
        <Link to="/grammar">英文法</Link> <span aria-hidden="true">›</span> 英文の作られ方
      </nav>

      <header className="lesson-header">
        <h1>英文の作られ方から学ぶ</h1>
        <p className="roadmap-header-lead">
          文法事項を1つずつ覚えるのではなく、英文がどのような部品と構造で組み上がっているかを追う順番です。
          上から{grammarRoadmap.length}つのSTEPをたどると、長い英文でも構造を見失わずに読めるようになります。
        </p>
        <div className="lesson-goal">
          <h2>このページの目標</h2>
          <p>
            英文を見たときに、主語・動詞・目的語・補語と、文を飾る修飾語を自分で見分け、文の骨格を取り出せるようになります。
          </p>
        </div>
      </header>

      <div className="roadmap-intro">
        <RichText text={SKELETON_GUIDE} />
      </div>

      <section className="block block-explanation" aria-labelledby="roles-heading">
        <h2 id="roles-heading">S / V / O / C / M とは</h2>
        <div className="pattern-intro-lead">
          英文は「主語 + 動詞 + (目的語・補語)」という骨格に、修飾語を足したものです。まず5つの記号が
          何を表すかを押さえます。S と V はどの文にもあり、O と C は動詞しだいで現れ、M は外しても骨格が壊れません。
        </div>
        <RoleGuide guides={roleGuides} />
      </section>

      <LessonBlocks blocks={roleBlocks} />

      <section className="block block-explanation" aria-labelledby="word-order-heading">
        <h2 id="word-order-heading">英語の語順 — S + V + O を先に作る</h2>
        <div className="pattern-intro-lead">
          英語には「〜が」「〜を」にあたる助詞がないため、語順そのものが役割を示します。動詞を先に見つけ、
          その前に主語、うしろに目的語や補語があるかを確かめます。
        </div>
        <GrammarAnimation sceneId="roadmap-word-order" animation={wordOrderAnimation} />
      </section>

      <LessonBlocks blocks={wordOrderBlocks} />

      <section className="block block-examples">
        <h3>例文</h3>
        {wordOrderExamples.map((example, index) => (
          <EnglishExample
            key={index}
            text={example.en}
            translation={example.ja}
            highlight={example.highlight}
            pattern={example.pattern}
            patternNote={example.patternNote}
            note={example.note}
          />
        ))}
      </section>

      <section className="lesson-quiz">
        <h2>理解度チェック（記号と語順）</h2>
        <Quiz questions={wordOrderQuiz} onAnswer={(question, correct) => record(question.id, correct)} />
      </section>

      <section className="block block-explanation" aria-labelledby="patterns-heading">
        <h2 id="patterns-heading">5文型は骨格の見取り図</h2>
        <div className="pattern-intro-lead">
          5文型は覚えるための分類ではなく、<strong>動詞のあとに何が続くかを確かめる道具</strong>です。
          下のカードは、それぞれの骨格がどう組み上がるかを動きで示します。同じ骨格のまま動詞だけが変わること、
          「O = C」の関係が見えることを確かめてください。
        </div>
      </section>

      <div className="pattern-cards">
        {PATTERN_ORDER.map((pattern) => {
          const showcase = patternShowcases.find((item) => item.pattern === pattern)
          if (!showcase) return null
          return <SentencePatternCard key={pattern} showcase={showcase} animation={patternAnimations[pattern]} />
        })}
      </div>

      <LessonBlocks blocks={patternBlocks} />

      <section className="block block-examples">
        <h3>例文</h3>
        {patternExamples.map((example, index) => (
          <EnglishExample
            key={index}
            text={example.en}
            translation={example.ja}
            highlight={example.highlight}
            pattern={example.pattern}
            patternNote={example.patternNote}
            note={example.note}
          />
        ))}
      </section>

      <section className="lesson-quiz">
        <h2>理解度チェック（5文型）</h2>
        <Quiz questions={patternQuiz} onAnswer={(question, correct) => record(question.id, correct)} />
      </section>

      <section className="lesson-word-order">
        <h2>並べ替え</h2>
        <p className="pattern-intro-lead">
          ここまでに読んだ例文を、語順から組み立て直します。骨格(S + V + O / O / C)を先に置いてから、
          修飾語を足す順で並べてみてください。
        </p>
        <WordOrder sentences={guideWordOrderSentences} />
      </section>

      <section className="roadmap-section" aria-label="ここから先の学習の流れ">
        <p className="pattern-intro-lead">
          ここまでは STEP 1(文の骨格)の内容です。ここからは、この骨格の見方を保ったまま長い英文へ進む順番を示します。
          各STEPの「この段階のセクション」から、対応するレッスンへ進めます。
        </p>
        <GrammarRoadmap />
      </section>

      <footer className="lesson-footer">
        <Link to="/grammar" className="btn-primary lesson-next-link">
          レベル別のセクション一覧へ →
        </Link>
      </footer>
    </div>
  )
}
