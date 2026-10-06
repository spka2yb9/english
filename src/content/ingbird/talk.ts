// イングバードのつぶやきコーパス。フレーズ集とコツを、抽選しやすい形にそろえる。

import { PHRASE_SCENES } from './phrases'
import { TIPS } from './tips'
import {
  ENCOURAGE_BODIES,
  ENCOURAGE_CLOSINGS,
  ENCOURAGE_LINES,
  TIME_GREETINGS,
} from './encouragement'

export type PhraseLine = {
  id: string
  /** 場面ラベル。 */
  scene: string
  en: string
  ja: string
  note: string
}

/** 場面順にならべたフレーズ。IDは場面と連番から決定的に作る。 */
export const PHRASES: readonly PhraseLine[] = PHRASE_SCENES.flatMap((scene, sceneIndex) =>
  scene.phrases.map(([en, ja, note], index) => ({
    id: `p${String(sceneIndex + 1).padStart(2, '0')}-${String(index + 1).padStart(2, '0')}`,
    scene: scene.label,
    en,
    ja,
    note,
  })),
)

export const TIP_LINES: readonly { id: string; text: string }[] = TIPS.map((text, index) => ({
  id: `t${String(index + 1).padStart(3, '0')}`,
  text,
}))

/** コーパスの規模。テストとドキュメントの基準にする。 */
export const TALK_COUNTS = {
  scenes: PHRASE_SCENES.length,
  phrases: PHRASES.length,
  tips: TIP_LINES.length,
  encourageLines: ENCOURAGE_LINES.length,
  bodies: Object.values(ENCOURAGE_BODIES).reduce((sum, list) => sum + list.length, 0),
  closings: ENCOURAGE_CLOSINGS.length,
  greetings: Object.values(TIME_GREETINGS).reduce((sum, list) => sum + list.length, 0),
} as const
