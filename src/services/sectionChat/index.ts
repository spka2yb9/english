// セクション内Q&A(イングバードにきく)の入口。
// レッスンから質問応答エンジンを作り、質問に合うQAを1件返す。

export { createSectionChat, type SectionChat } from './matcher'
export { buildSectionQa, intentsOf } from './corpus'
export type { ChatReply, QaAnswer, QaEntry, QaIntent, QaQuote } from './types'
