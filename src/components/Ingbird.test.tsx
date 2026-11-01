import { fireEvent, render, screen, waitFor, within } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { Ingbird } from './Ingbird'
import { IngbirdCard } from './IngbirdCard'
import { IngbirdPraise } from './IngbirdPraise'
import { todayString, shiftDate } from '../services/dates'
import { KEYS, saveJson } from '../services/storage'
import { recordStudyDay, type IngbirdMood } from '../services/studyDays'
import { EVOLUTIONS } from '../services/ingbirdEvolution'
import { DEFAULT_OUTFIT, OUTFIT_ITEMS, OUTFIT_SLOT_ORDER, type IngbirdOutfit } from '../content/ingbird/outfits'
import { getOutfit, saveOutfit } from '../services/ingbirdWardrobe'

const ALL_MOODS: IngbirdMood[] = [
  'idle',
  'happy',
  'cheer',
  'party',
  'proud',
  'wave',
  'curious',
  'wow',
  'sleepy',
  'shy',
  'think',
  'sing',
]

const MOOD_PARTS = [
  '.ingbird-brow',
  '.ingbird-eye-arc',
  '.ingbird-eye-lid',
  '.ingbird-beak-lower',
  '.ingbird-sparkles',
  '.ingbird-hearts',
  '.ingbird-notes',
  '.ingbird-zzz',
  '.ingbird-question',
  '.ingbird-bang',
  '.ingbird-thought',
]

beforeEach(() => {
  localStorage.clear()
  vi.spyOn(Math, 'random').mockReturnValue(0) // 言い回しの抽選を固定する
})

afterEach(() => {
  vi.restoreAllMocks()
})

function renderCard() {
  return render(
    <MemoryRouter>
      <IngbirdCard />
    </MemoryRouter>,
  )
}

describe('Ingbird', () => {
  it('マスコットは気分に応じた見た目を持ち、装飾利用では読み上げから外れる', () => {
    const { container } = render(<Ingbird mood="cheer" decorative />)
    const svg = container.querySelector('svg')
    expect(svg).toHaveAttribute('data-mood', 'cheer')
    expect(svg).toHaveAttribute('aria-hidden', 'true')
    expect(svg?.querySelector('.ingbird-sparkles')).not.toBeNull()
  })

  it('すべての気分を描けて、表情のパーツ(眉・まぶた・くちばし・飾り)を備える', () => {
    for (const mood of ALL_MOODS) {
      const { container, unmount } = render(<Ingbird mood={mood} />)
      expect(container.querySelector('svg')).toHaveAttribute('data-mood', mood)
      for (const part of MOOD_PARTS) expect(container.querySelector(part), `${mood}/${part}`).not.toBeNull()
      unmount()
    }
  })

  it('気分を指定しなくても描ける(いつもの表情)', () => {
    const { container } = render(<Ingbird decorative />)
    expect(container.querySelector('svg')).toHaveAttribute('data-mood', 'idle')
  })
})

describe('Ingbird の進化', () => {
  const THRESHOLDS: Record<string, number> = {
    aura: 1,
    rocks: 2,
    crest: 2,
    embers: 3,
    lightning: 3,
    'evolution-eyes': 4,
    'halo-ring': 5,
  }

  it('0〜5のすべての段階を描けて、段階に応じたパーツが点く', () => {
    for (const info of EVOLUTIONS) {
      const { container, unmount } = render(<Ingbird evolution={info.stage} />)
      expect(container.querySelector('svg')).toHaveAttribute('data-evolution', String(info.stage))
      for (const [part, threshold] of Object.entries(THRESHOLDS)) {
        const node = container.querySelector(`.ingbird-${part}`)
        expect(node, `${info.stage}/${part}`).not.toBeNull()
        expect(node?.classList.contains('is-on'), `${info.stage}/${part} の点灯`).toBe(info.stage >= threshold)
      }
      unmount()
    }
  })

  it('進化を指定しなければ、ふつうの姿', () => {
    const { container } = render(<Ingbird decorative />)
    expect(container.querySelector('svg')).toHaveAttribute('data-evolution', '0')
    expect(container.querySelector('.ingbird-aura')?.classList.contains('is-on')).toBe(false)
  })
})

describe('Ingbird の着せかえ', () => {
  const FULL: IngbirdOutfit = {
    glasses: 'sunglasses',
    hat: 'crown',
    effect: 'sakura',
    accessory: 'scarf',
    shoes: 'sneakers',
  }

  it('メガネ・帽子・小物・エフェクトを描き分ける', () => {
    const { container } = render(<Ingbird outfit={FULL} />)
    const svg = container.querySelector('svg')
    expect(svg).toHaveAttribute('data-glasses', 'sunglasses')
    expect(svg).toHaveAttribute('data-hat', 'crown')
    expect(svg).toHaveAttribute('data-effect', 'sakura')
    expect(svg).toHaveAttribute('data-accessory', 'scarf')
    expect(svg).toHaveAttribute('data-shoes', 'sneakers')
    expect(container.querySelector('.ingbird-glasses-sunglasses')).not.toBeNull()
    expect(container.querySelector('.ingbird-hat-crown')).not.toBeNull()
    expect(container.querySelector('.ingbird-fx-sakura')).not.toBeNull()
    expect(container.querySelector('.ingbird-scarf-group')).not.toBeNull()
    expect(container.querySelector('.ingbird-shoes-sneakers')).not.toBeNull()
    // 王冠をかぶったら学帽は消える
    expect(container.querySelector('.ingbird-cap')).toBeNull()
  })

  it('すべての着せかえアイテムを描ける', () => {
    const prefix = {
      glasses: 'ingbird-glasses',
      hat: 'ingbird-hat',
      effect: 'ingbird-fx',
      accessory: 'ingbird-accessory',
      shoes: 'ingbird-shoes',
    } as const
    for (const slot of OUTFIT_SLOT_ORDER) {
      for (const item of OUTFIT_ITEMS[slot]) {
        if (item.id === 'none' || (slot === 'hat' && item.id === 'grad')) continue
        const outfit = { ...DEFAULT_OUTFIT, [slot]: item.id } as IngbirdOutfit
        const { container, unmount } = render(<Ingbird outfit={outfit} />)
        expect(container.querySelector(`.${prefix[slot]}-${item.id}`), `${slot}/${item.id}`).not.toBeNull()
        unmount()
      }
    }
  })

  it('帽子なしでは学帽も消え、メガネなしでは眼鏡パーツが出ない', () => {
    const { container } = render(
      <Ingbird outfit={{ glasses: 'none', hat: 'none', effect: 'none', accessory: 'none', shoes: 'none' }} />,
    )
    expect(container.querySelector('.ingbird-cap')).toBeNull()
    expect(container.querySelector('.ingbird-hat')).toBeNull()
    expect(container.querySelector('.ingbird-glasses')).toBeNull()
    expect(container.querySelector('.ingbird-effect')).toBeNull()
    expect(container.querySelector('.ingbird-accessory')).toBeNull()
    expect(container.querySelector('.ingbird-shoes')).toBeNull()
  })

  it('既定は学帽をかぶったすがた', () => {
    const { container } = render(<Ingbird decorative />)
    expect(container.querySelector('svg')).toHaveAttribute('data-hat', 'grad')
    expect(container.querySelector('.ingbird-cap')).not.toBeNull()
    expect(container.querySelector('.ingbird-tassel-group')).not.toBeNull()
  })
})

describe('IngbirdCard', () => {
  it('学習日は連続ではなくトータルで表示する', () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -8), shiftDate(today, -5), today])
    const { container } = renderCard()
    expect(container.querySelector('.ingbird-total')?.textContent).toBe('3日')
    expect(screen.getByText(/今日の学習: ずみ/)).toBeInTheDocument()
  })

  it('久しぶりの学習日もほめる', () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -5), today])
    renderCard()
    expect(screen.getByText(/5日ぶり!おかえり!/)).toBeInTheDocument()
    expect(screen.getByText(/減らさない/)).toBeInTheDocument()
  })

  it('まだ学習していない日は、1問から誘う(久しぶりでも責めない)', () => {
    saveJson(KEYS.studyDays, [shiftDate(todayString(), -4)])
    renderCard()
    expect(screen.getByText(/4日ぶりだね、待ってたよ!/)).toBeInTheDocument()
    expect(screen.getByRole('link', { name: '1セッション始める' })).toBeInTheDocument()
    expect(screen.getByText(/連続日数ではなく/)).toBeInTheDocument()
  })

  it('記録がなければ0日として迎える', () => {
    const { container } = renderCard()
    expect(container.querySelector('.ingbird-total')?.textContent).toBe('0日')
    expect(screen.getByText('今日はまだ、これから!')).toBeInTheDocument()
  })

  it('気分に合わせた表情とラベルを出し、お祝いの日はカードも祝う', () => {
    saveJson(KEYS.studyDays, [todayString()])
    const { container } = renderCard()
    expect(screen.getByText('1日目、はじまった!')).toBeInTheDocument()
    // Math.random は 0 固定なので、抽選は各候補の先頭になる
    expect(container.querySelector('.ingbird-mood-party')).not.toBeNull()
    expect(screen.getByText('お祝い')).toBeInTheDocument()
    expect(container.querySelector('.ingbird-card')?.className).toContain('is-celebrating')
  })

  it('ふつうの日は控えめな表情で、お祝いクラスは付かない', () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -1), today])
    const { container } = renderCard()
    expect(container.querySelector('.ingbird-card')?.className).not.toContain('is-celebrating')
    expect(screen.getByText('にっこり')).toBeInTheDocument()
    expect(container.querySelector('.ingbird-mood-happy')).not.toBeNull()
  })

  it('画面を開くと、今日ぶんの進捗に合わせたひとことを自動で出す', async () => {
    const today = todayString()
    saveJson(KEYS.studyDays, [shiftDate(today, -1), today])
    renderCard()
    // Math.random は 0 固定なので、本文の先頭にトータル日数が入る
    const bubble = await screen.findByText(/トータル2日/)
    expect(bubble.closest('.ingbird-bubble')).not.toBeNull()
    expect(screen.getByText('イングバードのひとこと')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'イングバードに話しかける' })).toHaveAttribute('aria-expanded', 'true')
  })

  it('まだ1日も学習していなくても、開いた時点ではじまりのひとことを出す', async () => {
    const { container } = renderCard()
    await screen.findByText(/まだ0日でも大丈夫/)
    // 初期表示の気分はカードのほめ言葉に合わせる(0日目の「きになる」)
    expect(container.querySelector('.ingbird-mood-curious')).not.toBeNull()
  })

  it('まだ進化していない日は「ふつう」', () => {
    const { container } = renderCard()
    expect(screen.getByText('ふつう')).toBeInTheDocument()
    expect(container.querySelector('svg')).toHaveAttribute('data-evolution', '0')
  })

  it('学習日トータルに応じた進化を表示する', () => {
    const today = todayString()
    saveJson(
      KEYS.studyDays,
      Array.from({ length: 30 }, (_, index) => shiftDate(today, -29 + index)),
    )
    const { container } = renderCard()
    expect(screen.getByText('雷光')).toBeInTheDocument()
    expect(container.querySelector('.ingbird-evolution-label.is-stage-3')).not.toBeNull()
    expect(container.querySelector('svg')).toHaveAttribute('data-evolution', '3')
    expect(container.querySelector('.ingbird-lightning')?.classList.contains('is-on')).toBe(true)
  })

  it('学習日が足りないアイテムは、必要日数つきで選べない', async () => {
    const { container } = renderCard()
    await waitFor(() => expect(container.querySelector('.ingbird-bubble')).not.toBeNull())
    fireEvent.click(screen.getByRole('button', { name: 'きせかえ' }))

    expect(screen.getByText(/解放 \d+ \/ \d+/)).toBeInTheDocument()
    const preview = container.querySelector('.ingbird-wardrobe-next')
    expect(preview).not.toBeNull()
    expect(within(preview as HTMLElement).getByText('つぎのごほうび')).toBeInTheDocument()
    expect(within(preview as HTMLElement).getByText('あと1日')).toBeInTheDocument()
    // 1日で解放される2つ(丸メガネ・きらきら)のプレビュー
    expect(within(preview as HTMLElement).getByText('丸メガネ')).toBeInTheDocument()
    expect(within(preview as HTMLElement).getByText('きらきら')).toBeInTheDocument()

    const lockedCrown = screen.getByRole('button', { name: /^王冠/ })
    expect(lockedCrown).toBeDisabled()
    expect(lockedCrown).toHaveTextContent('50日')
    expect(screen.getByRole('button', { name: '学帽' })).toBeEnabled()

    fireEvent.click(lockedCrown)
    expect(container.querySelector('svg')).toHaveAttribute('data-hat', 'grad')
  })

  it('きせかえパネルでメガネや帽子を変えられ、保存される', async () => {
    const today = todayString()
    saveJson(
      KEYS.studyDays,
      Array.from({ length: 60 }, (_, index) => shiftDate(today, -59 + index)),
    )
    const { container } = renderCard()
    await screen.findByText(/トータル60日/)
    const open = screen.getByRole('button', { name: 'きせかえ' })
    expect(open).toHaveAttribute('aria-expanded', 'false')

    fireEvent.click(open)
    expect(open).toHaveAttribute('aria-expanded', 'true')
    const panel = screen.getByRole('group', { name: 'イングバードのきせかえ' })

    fireEvent.click(within(panel).getByRole('button', { name: 'サングラス' }))
    expect(container.querySelector('svg')).toHaveAttribute('data-glasses', 'sunglasses')
    expect(within(panel).getByRole('button', { name: 'サングラス' })).toHaveAttribute('aria-pressed', 'true')

    fireEvent.click(within(panel).getByRole('button', { name: '王冠' }))
    expect(container.querySelector('svg')).toHaveAttribute('data-hat', 'crown')
    expect(container.querySelector('.ingbird-crown')).not.toBeNull()
    expect(getOutfit()).toMatchObject({ glasses: 'sunglasses', hat: 'crown' })

    fireEvent.click(screen.getByRole('button', { name: 'きせかえを閉じる' }))
    expect(screen.queryByRole('group', { name: 'イングバードのきせかえ' })).toBeNull()
  })

  it('保存した着せかえを読み込み、はじめの姿に戻せる', async () => {
    saveOutfit({ glasses: 'round', hat: 'beanie', effect: 'snow', accessory: 'bowtie', shoes: 'boots' })
    const { container } = renderCard()
    await screen.findByText(/まだ0日でも大丈夫/)
    expect(container.querySelector('.ingbird-beanie')).not.toBeNull()

    fireEvent.click(screen.getByRole('button', { name: 'きせかえ' }))
    fireEvent.click(screen.getByRole('button', { name: 'はじめの姿にもどす' }))
    expect(container.querySelector('svg')).toHaveAttribute('data-hat', 'grad')
    expect(container.querySelector('.ingbird-beanie')).toBeNull()
    expect(getOutfit()).toEqual(DEFAULT_OUTFIT)
  })

  it('バードをタップすると次のひとことに変わり、閉じられる', async () => {
    const { container } = renderCard()
    await screen.findByText(/まだ0日でも大丈夫/)
    const bird = screen.getByRole('button', { name: 'イングバードに話しかける' })

    let previous = container.querySelector('.ingbird-bubble')?.textContent ?? ''
    for (let i = 0; i < 6 && !container.querySelector('.ingbird-bubble-en'); i += 1) {
      fireEvent.click(bird)
      await waitFor(() => {
        expect(container.querySelector('.ingbird-bubble')?.textContent ?? '').not.toBe(previous)
      })
      previous = container.querySelector('.ingbird-bubble')?.textContent ?? ''
    }

    const english = container.querySelector('.ingbird-bubble-en')
    expect(english).not.toBeNull()
    expect(english).toHaveAttribute('lang', 'en')
    expect(container.querySelector('.ingbird-bubble-ja')?.textContent?.length).toBeGreaterThan(1)
    expect(container.querySelector('.ingbird-bubble-note')?.textContent?.length).toBeGreaterThan(5)
    expect(screen.getByText('英会話フレーズ')).toBeInTheDocument()

    fireEvent.click(screen.getByRole('button', { name: '吹き出しを閉じる' }))
    expect(container.querySelector('.ingbird-bubble')).toBeNull()
    expect(bird).toHaveAttribute('aria-expanded', 'false')
  })
})

describe('IngbirdPraise', () => {
  it('新しい学習日を記録すると、トータル日数つきでほめ、閉じられる', async () => {
    render(<IngbirdPraise />)
    expect(screen.queryByRole('status')).toBeNull()

    recordStudyDay()
    const toast = await screen.findByRole('status')
    expect(toast).toHaveTextContent('1日目、はじまった!')
    expect(toast).toHaveTextContent('学習日 1日（トータル）')
    // 1日目で解放される着せかえを知らせる
    expect(toast).toHaveClass('has-unlock')
    expect(toast).toHaveTextContent('新しいアイテムを解放!')
    expect(toast).toHaveTextContent('メガネ・丸メガネ')
    expect(toast).toHaveTextContent('エフェクト・きらきら')

    fireEvent.click(screen.getByRole('button', { name: 'メッセージを閉じる' }))
    expect(screen.queryByRole('status')).toBeNull()
  })

  it('新しいアイテムがない日は、解放の知らせを出さない', async () => {
    const today = todayString()
    saveJson(
      KEYS.studyDays,
      Array.from({ length: 18 }, (_, index) => shiftDate(today, -18 + index)),
    )
    render(<IngbirdPraise />)
    recordStudyDay()
    const toast = await screen.findByRole('status')
    expect(toast).toHaveTextContent('学習日 19日（トータル）')
    expect(toast).not.toHaveTextContent('新しいアイテムを解放!')
    expect(screen.queryByText('新しいアイテムを解放!')).toBeNull()
  })

  it('同じ日の2回目以降は出し直さない', async () => {
    render(<IngbirdPraise />)
    recordStudyDay()
    await screen.findByRole('status')
    recordStudyDay()
    expect(screen.getAllByRole('status')).toHaveLength(1)
  })
})
