import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { Timeline } from './Timeline'

describe('Timeline', () => {
  it('期間と時点のラベルを時間軸の上下に分ける', () => {
    render(
      <Timeline
        spec={{
          range: [30, 50],
          rangeLabel: '長い動作',
          point: 42,
          pointLabel: '短い出来事',
        }}
      />,
    )

    expect(screen.getByText('短い出来事')).toHaveClass('above-axis')
  })

  it('時点だけのタイムラインではラベルを従来どおり軸の下に置く', () => {
    render(<Timeline spec={{ point: 42, pointLabel: '短い出来事' }} />)

    expect(screen.getByText('短い出来事')).not.toHaveClass('above-axis')
  })
})
