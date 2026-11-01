import { Link } from 'react-router-dom'
import { PATTERN_LABELS } from '../content/grammar/patterns/types'
import { patternShowcases, roleGuides } from '../content/grammar/structures'
import { RoleGuide } from './RoleGuide'

/**
 * 英文法ページの冒頭に置く5文型の見取り図。
 * 詳細なアニメーション・確認問題は「英文の作られ方から学ぶ」ページに置き、
 * ここではS/V/O/C/Mの役割と、5つの骨格を一覧できるようにする。
 */
export function GrammarPatternOverview() {
  return (
    <section className="grammar-pattern-overview" aria-labelledby="grammar-pattern-heading">
      <p className="eyebrow">英文の骨組み</p>
      <h2 id="grammar-pattern-heading">5文型は、動詞のあとに何が続くかで決まる</h2>
      <p className="pattern-intro-lead">
        英文は「主語(S) + 動詞(V)」を軸に、目的語(O)・補語(C)・修飾語(M)が加わります。
        5文型は暗記の分類ではなく、長い文から骨格を取り出すための見取り図です。
        とくに第3文型(SVO)と第5文型(SVOC)は、<strong>O = C</strong> の関係が成り立つかで見分けます。
      </p>

      <RoleGuide guides={roleGuides} />

      <h3 className="grammar-pattern-subheading">5文型の見取り図</h3>
      <div
        className="grammar-pattern-table-wrap"
        role="region"
        aria-label="5文型の一覧（横にスクロールできます）"
        tabIndex={0}
      >
        <table className="grammar-pattern-table">
          <thead>
            <tr>
              <th scope="col">文型</th>
              <th scope="col">骨組み</th>
              <th scope="col">例</th>
              <th scope="col">見分け方</th>
            </tr>
          </thead>
          <tbody>
            {patternShowcases.map((showcase) => (
              <tr key={showcase.pattern}>
                <th scope="row">{PATTERN_LABELS[showcase.pattern]}</th>
                <td>
                  <span className="grammar-pattern-skeleton">{showcase.skeleton}</span>
                </td>
                <td>
                  <span className="grammar-pattern-example" lang="en">
                    {showcase.example.en}
                  </span>
                  <span className="grammar-pattern-ja">{showcase.example.ja}</span>
                </td>
                <td>
                  {showcase.relation && <span className="grammar-pattern-relation">{showcase.relation}</span>}
                  <span>{showcase.example.note}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <p className="grammar-pattern-note">
        第4文型(SVOO)は「人 → もの」の順です。もののほうを先にしたいときは、第3文型(SVO)+ to / for に言い換えます。
        例: My father gave a camera to me.
      </p>

      <p className="grammar-pattern-more">
        <Link to="/grammar/roadmap">図とアニメーションで、5文型と英文の作られ方を詳しく見る →</Link>
      </p>
    </section>
  )
}
