import { A2_SCENES } from './scenes-a2'
import { A2_PLUS_SCENES } from './scenes-a2plus'
import { B1_SCENES } from './scenes-b1'
import { B1_PLUS_SCENES } from './scenes-b1plus'
import { B2_SCENES } from './scenes-b2'
import type { IllustrationSceneMap } from './types'

export const LESSON_SCENES: IllustrationSceneMap = {
  ...A2_SCENES,
  ...A2_PLUS_SCENES,
  ...B1_SCENES,
  ...B1_PLUS_SCENES,
  ...B2_SCENES,
}
