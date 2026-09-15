import { ROLE_LABELS, ROLE_MEANINGS, roleAccessibleLabel } from '../content/grammar/structures/roles'
import type { RoleGuide as RoleGuideEntry } from '../content/grammar/structures'

/**
 * S / V / O / C / M がそれぞれ何を表すかを示すカード列。
 * 構造図(SentenceBreakdown)と同じ役割バッジと色を使い、同じ語句が同じ色で見えるようにする。
 */
export function RoleGuide({ guides }: { guides: RoleGuideEntry[] }) {
  return (
    <ul className="role-guide">
      {guides.map((guide) => (
        <li key={guide.role} className={`role-guide-item role-${guide.role}`}>
          <div className="role-guide-head">
            <span className="role-badge" aria-label={roleAccessibleLabel(guide.role)}>
              {guide.role}
            </span>
            <span className="role-guide-name">{ROLE_LABELS[guide.role]}</span>
          </div>
          <p className="role-guide-meaning">{ROLE_MEANINGS[guide.role]}</p>
          <p className="role-guide-example" lang="en">
            {guide.example}
          </p>
          <p className="role-guide-note">{guide.note}</p>
          <p className="role-guide-sentence" lang="en">
            {guide.sentence}
          </p>
        </li>
      ))}
    </ul>
  )
}
