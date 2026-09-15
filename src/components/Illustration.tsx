import { LESSON_ANIMATIONS } from '../content/grammar/animations'
import type { IllustrationKind } from '../content/types'
import { GrammarAnimation } from './GrammarAnimation'

/**
 * レッスンの挿絵。画面では animations.ts の3段階の2Dアニメーションを表示する。
 * kind / labels は従来の教材データとの互換性のために受け取るだけ。
 */
export function Illustration({ sceneId }: {
  sceneId: string
  kind: IllustrationKind
  labels: string[]
  alt?: string
}) {
  const animation = LESSON_ANIMATIONS[sceneId]
  if (!animation) throw new Error(`${sceneId}: animation is not implemented`)
  return <GrammarAnimation key={sceneId} sceneId={sceneId} animation={animation} />
}
