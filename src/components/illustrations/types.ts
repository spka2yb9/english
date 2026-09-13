import type { ReactNode } from 'react'

export type IllustrationScene = (labels: string[]) => ReactNode
export type IllustrationSceneMap = Record<string, IllustrationScene>
