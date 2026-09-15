import { render, screen, within } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'

vi.mock('../services/speech', () => ({
  NORMAL_RATE: 1,
  SLOW_RATE: 0.5,
  speechService: { isSupported: () => false, speak: vi.fn(), stop: vi.fn() },
}))

import { SentenceBreakdown } from './SentenceBreakdown'
import { SentenceExpansion } from './SentenceExpansion'

describe('SentenceBreakdown', () => {
  it('英文を役割ごとの区画に分けて表示し、意味の関係と骨格を示す', () => {
    render(
      <SentenceBreakdown
        sentence="I found the book very useful."
        ja="私はその本がとても役に立つと分かりました。"
        pattern="SVOC"
        parts={[
          { text: 'I', role: 'S' },
          { text: 'found', role: 'V' },
          { text: 'the book', role: 'O', note: '動作の対象' },
          { text: 'very useful.', role: 'C', note: 'the book を説明する' },
        ]}
        relation="the book = very useful"
        skeleton="I found the book."
        skeletonPattern="SVO"
        caption="O = C の関係があるので第5文型です。"
      />,
    )

    // 役割バッジは型名だけでなく、日本語の意味を持つ読み上げラベルを付ける。
    expect(screen.getByLabelText(/補語 C/)).toBeInTheDocument()
    // この文に修飾語(M)は無い。
    expect(screen.queryByLabelText(/修飾語 M/)).toBeNull()
    expect(screen.getByText('very useful.')).toBeInTheDocument()
    expect(screen.getByText('the book = very useful')).toBeInTheDocument()
    expect(screen.getByText('I found the book.')).toBeInTheDocument()
    expect(screen.getByText('O = C の関係があるので第5文型です。')).toBeInTheDocument()
  })

  it('修飾語(M)を骨格の要素と区別して表示する', () => {
    render(
      <SentenceBreakdown
        sentence="I found the book yesterday."
        parts={[
          { text: 'I', role: 'S' },
          { text: 'found', role: 'V' },
          { text: 'the book', role: 'O' },
          { text: 'yesterday.', role: 'M', note: 'found を修飾する副詞' },
        ]}
      />,
    )

    const parts = document.querySelectorAll('.breakdown-part')
    expect(parts).toHaveLength(4)
    expect(parts[3]?.className).toContain('role-M')
    expect(within(parts[3] as HTMLElement).getByText('M')).toBeInTheDocument()
    // 骨格が無い文では「骨格」の行を出さない。
    expect(document.querySelector('.breakdown-skeleton')).toBeNull()
  })
})

describe('SentenceExpansion', () => {
  it('段階ごとの英文と、その段階で加わった部分を表示する', () => {
    render(
      <SentenceExpansion
        steps={[
          { en: 'I saw a dog.', ja: '私は犬を見かけました。', note: '骨格は S + V + O。' },
          { en: 'I saw a big dog.', ja: '私は大きな犬を見かけました。', focus: 'big', note: '形容詞が加わりました。' },
        ]}
        caption="足した部分はすべて修飾語です。"
      />,
    )

    const steps = document.querySelectorAll('.expansion-step')
    expect(steps).toHaveLength(2)
    // focus で指定した語句は、元の英文の中で強調表示する。
    expect(within(steps[1] as HTMLElement).getByText('big').tagName).toBe('MARK')
    expect(screen.getByText('形容詞が加わりました。')).toBeInTheDocument()
    expect(screen.getByText('足した部分はすべて修飾語です。')).toBeInTheDocument()
  })

  it('focus が英文に無い場合は強調せず、そのまま表示する', () => {
    render(<SentenceExpansion steps={[{ en: 'She sings.', focus: 'sang' }, { en: 'She sings well.' }]} />)
    expect(document.querySelector('.expansion-steps mark')).toBeNull()
    expect(screen.getByText('She sings.')).toBeInTheDocument()
  })
})
