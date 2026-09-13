import { useState } from 'react'
import type { VocabularyIllustration } from '../content/vocabulary/illustrations'

export function VocabularyMemoryImage({ illustration }: { illustration: VocabularyIllustration }) {
  const [failed, setFailed] = useState(false)
  if (failed) return null

  return (
    <figure className="vocab-memory-image">
      <span className="vocab-memory-image-label">イメージで覚える</span>
      <img src={`${import.meta.env.BASE_URL}${illustration.src}`}
        alt={illustration.alt} width={1536} height={1024}
        loading="lazy" decoding="async" onError={() => setFailed(true)} />
      <figcaption>{illustration.caption}</figcaption>
    </figure>
  )
}
