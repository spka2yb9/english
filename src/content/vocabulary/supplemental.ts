import type { VocabularyEntry } from '../types'

/** Oxford差分外でもB1学習者に特に有用な句動詞。 */
export const supplementalVocabulary: VocabularyEntry[] = [
  {
    id: 'come across',
    word: 'come across',
    level: 'B1',
    partOfSpeech: '句動詞',
    meaningsJa: ['偶然見つける、偶然出会う'],
    pronunciation: '/ˌkʌm əˈkrɔs/',
    exampleSentence: 'I often come across useful expressions while reading the news.',
    exampleTranslationJa: 'ニュースを読んでいると、役立つ表現をよく偶然見つける。',
    collocations: ['come across an article', 'come across as confident'],
    relatedWords: ['find', 'encounter', 'run into'],
  },
  {
    id: 'break down',
    word: 'break down',
    level: 'B1',
    partOfSpeech: '句動詞',
    meaningsJa: ['故障する', '細かく分けて説明する'],
    pronunciation: '/ˌbreɪk ˈdaʊn/',
    exampleSentence: 'Good teachers break down complex ideas into manageable steps.',
    exampleTranslationJa: 'よい教師は複雑な考えを取り組みやすい段階に分けて説明する。',
    collocations: ['a car breaks down', 'break down a problem', 'break down barriers'],
    relatedWords: ['failure', 'analyze', 'divide'],
  },
]
