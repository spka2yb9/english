// 発音記号の穴埋め演習。ipaEntries の全記号を10語ずつカバーする。
// ipa の [] が出題される空所。囲みの外に答えと同じ記号を置かないこと(答えが見えてしまう)。
// 誤答は SIMILAR_SYMBOLS(混同しやすい記号)から作る。検証は quiz.test.ts。

import type { QuizQuestion } from '../types'
import { sample } from '../../services/shuffle'
import { ipaEntries } from './data'

export type IpaQuizWord = { word: string; ipa: string }

export const ipaQuizWords: IpaQuizWord[] = [
  // ─── 母音 ───
  // iː
  { word: 'see', ipa: 's[iː]' },
  { word: 'tea', ipa: 't[iː]' },
  { word: 'green', ipa: 'gr[iː]n' },
  { word: 'eat', ipa: '[iː]t' },
  { word: 'meet', ipa: 'm[iː]t' },
  { word: 'key', ipa: 'k[iː]' },
  { word: 'read', ipa: 'r[iː]d' },
  { word: 'sleep', ipa: 'sl[iː]p' },
  { word: 'cheese', ipa: 'tʃ[iː]z' },
  { word: 'week', ipa: 'w[iː]k' },

  // ɪ
  { word: 'sit', ipa: 's[ɪ]t' },
  { word: 'big', ipa: 'b[ɪ]g' },
  { word: 'fish', ipa: 'f[ɪ]ʃ' },
  { word: 'six', ipa: 's[ɪ]ks' },
  { word: 'kitchen', ipa: 'ˈk[ɪ]tʃən' },
  { word: 'live', ipa: 'l[ɪ]v' },
  { word: 'this', ipa: 'ð[ɪ]s' },
  { word: 'milk', ipa: 'm[ɪ]lk' },
  { word: 'city', ipa: 'ˈs[ɪ]ti' },
  { word: 'window', ipa: 'ˈw[ɪ]ndoʊ' },

  // e
  { word: 'bed', ipa: 'b[e]d' },
  { word: 'red', ipa: 'r[e]d' },
  { word: 'pen', ipa: 'p[e]n' },
  { word: 'egg', ipa: '[e]g' },
  { word: 'ten', ipa: 't[e]n' },
  { word: 'head', ipa: 'h[e]d' },
  { word: 'friend', ipa: 'fr[e]nd' },
  { word: 'help', ipa: 'h[e]lp' },
  { word: 'best', ipa: 'b[e]st' },
  { word: 'yes', ipa: 'j[e]s' },

  // æ
  { word: 'cat', ipa: 'k[æ]t' },
  { word: 'apple', ipa: 'ˈ[æ]pəl' },
  { word: 'hand', ipa: 'h[æ]nd' },
  { word: 'bag', ipa: 'b[æ]g' },
  { word: 'map', ipa: 'm[æ]p' },
  { word: 'black', ipa: 'bl[æ]k' },
  { word: 'man', ipa: 'm[æ]n' },
  { word: 'thank', ipa: 'θ[æ]ŋk' },
  { word: 'happy', ipa: 'ˈh[æ]pi' },
  { word: 'fast', ipa: 'f[æ]st' },

  // ʌ
  { word: 'cup', ipa: 'k[ʌ]p' },
  { word: 'sun', ipa: 's[ʌ]n' },
  { word: 'love', ipa: 'l[ʌ]v' },
  { word: 'bus', ipa: 'b[ʌ]s' },
  { word: 'lunch', ipa: 'l[ʌ]ntʃ' },
  { word: 'money', ipa: 'ˈm[ʌ]ni' },
  { word: 'but', ipa: 'b[ʌ]t' },
  { word: 'young', ipa: 'j[ʌ]ŋ' },
  { word: 'jump', ipa: 'dʒ[ʌ]mp' },
  { word: 'brother', ipa: 'ˈbr[ʌ]ðər' },

  // ɑː
  { word: 'father', ipa: 'ˈf[ɑː]ðər' },
  { word: 'hot', ipa: 'h[ɑː]t' },
  { word: 'box', ipa: 'b[ɑː]ks' },
  { word: 'stop', ipa: 'st[ɑː]p' },
  { word: 'car', ipa: 'k[ɑː]r' },
  { word: 'job', ipa: 'dʒ[ɑː]b' },
  { word: 'watch', ipa: 'w[ɑː]tʃ' },
  { word: 'shop', ipa: 'ʃ[ɑː]p' },
  { word: 'park', ipa: 'p[ɑː]rk' },
  { word: 'doctor', ipa: 'ˈd[ɑː]ktər' },

  // ɔː
  { word: 'talk', ipa: 't[ɔː]k' },
  { word: 'call', ipa: 'k[ɔː]l' },
  { word: 'saw', ipa: 's[ɔː]' },
  { word: 'four', ipa: 'f[ɔː]r' },
  { word: 'door', ipa: 'd[ɔː]r' },
  { word: 'small', ipa: 'sm[ɔː]l' },
  { word: 'walk', ipa: 'w[ɔː]k' },
  { word: 'ball', ipa: 'b[ɔː]l' },
  { word: 'morning', ipa: 'ˈm[ɔː]rnɪŋ' },
  { word: 'law', ipa: 'l[ɔː]' },

  // ʊ
  { word: 'book', ipa: 'b[ʊ]k' },
  { word: 'good', ipa: 'g[ʊ]d' },
  { word: 'put', ipa: 'p[ʊ]t' },
  { word: 'look', ipa: 'l[ʊ]k' },
  { word: 'foot', ipa: 'f[ʊ]t' },
  { word: 'cook', ipa: 'k[ʊ]k' },
  { word: 'woman', ipa: 'ˈw[ʊ]mən' },
  { word: 'could', ipa: 'k[ʊ]d' },
  { word: 'full', ipa: 'f[ʊ]l' },
  { word: 'sugar', ipa: 'ˈʃ[ʊ]gər' },

  // uː
  { word: 'food', ipa: 'f[uː]d' },
  { word: 'blue', ipa: 'bl[uː]' },
  { word: 'moon', ipa: 'm[uː]n' },
  { word: 'school', ipa: 'sk[uː]l' },
  { word: 'two', ipa: 't[uː]' },
  { word: 'soon', ipa: 's[uː]n' },
  { word: 'juice', ipa: 'dʒ[uː]s' },
  { word: 'room', ipa: 'r[uː]m' },
  { word: 'shoes', ipa: 'ʃ[uː]z' },
  { word: 'you', ipa: 'j[uː]' },

  // ɜːr
  { word: 'bird', ipa: 'b[ɜːr]d' },
  { word: 'girl', ipa: 'g[ɜːr]l' },
  { word: 'work', ipa: 'w[ɜːr]k' },
  { word: 'word', ipa: 'w[ɜːr]d' },
  { word: 'first', ipa: 'f[ɜːr]st' },
  { word: 'turn', ipa: 't[ɜːr]n' },
  { word: 'learn', ipa: 'l[ɜːr]n' },
  { word: 'nurse', ipa: 'n[ɜːr]s' },
  { word: 'hurt', ipa: 'h[ɜːr]t' },
  { word: 'shirt', ipa: 'ʃ[ɜːr]t' },

  // ə
  { word: 'about', ipa: '[ə]ˈbaʊt' },
  { word: 'lemon', ipa: 'ˈlem[ə]n' },
  { word: 'again', ipa: '[ə]ˈgen' },
  { word: 'problem', ipa: 'ˈprɑːbl[ə]m' },
  { word: 'seven', ipa: 'ˈsev[ə]n' },
  { word: 'open', ipa: 'ˈoʊp[ə]n' },
  { word: 'police', ipa: 'p[ə]ˈliːs' },
  { word: 'listen', ipa: 'ˈlɪs[ə]n' },
  { word: 'garden', ipa: 'ˈgɑːrd[ə]n' },
  { word: 'pencil', ipa: 'ˈpens[ə]l' },

  // ─── 二重母音 ───
  // eɪ
  { word: 'day', ipa: 'd[eɪ]' },
  { word: 'rain', ipa: 'r[eɪ]n' },
  { word: 'cake', ipa: 'k[eɪ]k' },
  { word: 'name', ipa: 'n[eɪ]m' },
  { word: 'eight', ipa: '[eɪ]t' },
  { word: 'train', ipa: 'tr[eɪ]n' },
  { word: 'make', ipa: 'm[eɪ]k' },
  { word: 'wait', ipa: 'w[eɪ]t' },
  { word: 'table', ipa: 'ˈt[eɪ]bəl' },
  { word: 'they', ipa: 'ð[eɪ]' },

  // aɪ
  { word: 'my', ipa: 'm[aɪ]' },
  { word: 'time', ipa: 't[aɪ]m' },
  { word: 'five', ipa: 'f[aɪ]v' },
  { word: 'night', ipa: 'n[aɪ]t' },
  { word: 'buy', ipa: 'b[aɪ]' },
  { word: 'ice', ipa: '[aɪ]s' },
  { word: 'white', ipa: 'w[aɪ]t' },
  { word: 'right', ipa: 'r[aɪ]t' },
  { word: 'like', ipa: 'l[aɪ]k' },
  { word: 'fly', ipa: 'fl[aɪ]' },

  // ɔɪ
  { word: 'boy', ipa: 'b[ɔɪ]' },
  { word: 'coin', ipa: 'k[ɔɪ]n' },
  { word: 'enjoy', ipa: 'ɪnˈdʒ[ɔɪ]' },
  { word: 'noise', ipa: 'n[ɔɪ]z' },
  { word: 'toy', ipa: 't[ɔɪ]' },
  { word: 'voice', ipa: 'v[ɔɪ]s' },
  { word: 'join', ipa: 'dʒ[ɔɪ]n' },
  { word: 'point', ipa: 'p[ɔɪ]nt' },
  { word: 'oil', ipa: '[ɔɪ]l' },
  { word: 'choice', ipa: 'tʃ[ɔɪ]s' },

  // aʊ
  { word: 'now', ipa: 'n[aʊ]' },
  { word: 'house', ipa: 'h[aʊ]s' },
  { word: 'down', ipa: 'd[aʊ]n' },
  { word: 'brown', ipa: 'br[aʊ]n' },
  { word: 'out', ipa: '[aʊ]t' },
  { word: 'sound', ipa: 's[aʊ]nd' },
  { word: 'mouth', ipa: 'm[aʊ]θ' },
  { word: 'count', ipa: 'k[aʊ]nt' },
  { word: 'cloud', ipa: 'kl[aʊ]d' },
  { word: 'about', ipa: 'əˈb[aʊ]t' },

  // oʊ
  { word: 'go', ipa: 'g[oʊ]' },
  { word: 'home', ipa: 'h[oʊ]m' },
  { word: 'boat', ipa: 'b[oʊ]t' },
  { word: 'snow', ipa: 'sn[oʊ]' },
  { word: 'phone', ipa: 'f[oʊ]n' },
  { word: 'cold', ipa: 'k[oʊ]ld' },
  { word: 'no', ipa: 'n[oʊ]' },
  { word: 'road', ipa: 'r[oʊ]d' },
  { word: 'window', ipa: 'ˈwɪnd[oʊ]' },
  { word: 'yellow', ipa: 'ˈjel[oʊ]' },

  // ─── 子音 ───
  // p
  { word: 'pen', ipa: '[p]en' },
  { word: 'apple', ipa: 'ˈæ[p]əl' },
  { word: 'stop', ipa: 'stɑː[p]' },
  { word: 'park', ipa: '[p]ɑːrk' },
  { word: 'help', ipa: 'hel[p]' },
  { word: 'happy', ipa: 'ˈhæ[p]i' },
  { word: 'top', ipa: 'tɑː[p]' },
  { word: 'pick', ipa: '[p]ɪk' },
  { word: 'open', ipa: 'ˈoʊ[p]ən' },
  { word: 'sleep', ipa: 'sliː[p]' },

  // b
  { word: 'big', ipa: '[b]ɪg' },
  { word: 'blue', ipa: '[b]luː' },
  { word: 'job', ipa: 'dʒɑː[b]' },
  { word: 'book', ipa: '[b]ʊk' },
  { word: 'table', ipa: 'ˈteɪ[b]əl' },
  { word: 'club', ipa: 'klʌ[b]' },
  { word: 'best', ipa: '[b]est' },
  { word: 'about', ipa: 'əˈ[b]aʊt' },
  { word: 'number', ipa: 'ˈnʌm[b]ər' },
  { word: 'boat', ipa: '[b]oʊt' },

  // t
  { word: 'ten', ipa: '[t]en' },
  { word: 'time', ipa: '[t]aɪm' },
  { word: 'cat', ipa: 'kæ[t]' },
  { word: 'table', ipa: 'ˈ[t]eɪbəl' },
  { word: 'tea', ipa: '[t]iː' },
  { word: 'night', ipa: 'naɪ[t]' },
  { word: 'top', ipa: '[t]ɑːp' },
  { word: 'eat', ipa: 'iː[t]' },
  { word: 'hot', ipa: 'hɑː[t]' },
  { word: 'turn', ipa: '[t]ɜːrn' },

  // d
  { word: 'dog', ipa: '[d]ɔːg' },
  { word: 'ready', ipa: 'ˈre[d]i' },
  { word: 'bed', ipa: 'be[d]' },
  { word: 'door', ipa: '[d]ɔːr' },
  { word: 'red', ipa: 're[d]' },
  { word: 'day', ipa: '[d]eɪ' },
  { word: 'down', ipa: '[d]aʊn' },
  { word: 'food', ipa: 'fuː[d]' },
  { word: 'garden', ipa: 'ˈgɑːr[d]ən' },
  { word: 'hand', ipa: 'hæn[d]' },

  // k
  { word: 'key', ipa: '[k]iː' },
  { word: 'school', ipa: 's[k]uːl' },
  { word: 'back', ipa: 'bæ[k]' },
  { word: 'cat', ipa: '[k]æt' },
  { word: 'milk', ipa: 'mɪl[k]' },
  { word: 'book', ipa: 'bʊ[k]' },
  { word: 'ask', ipa: 'æs[k]' },
  { word: 'walk', ipa: 'wɔː[k]' },
  { word: 'week', ipa: 'wiː[k]' },
  { word: 'thank', ipa: 'θæŋ[k]' },

  // g
  { word: 'go', ipa: '[g]oʊ' },
  { word: 'girl', ipa: '[g]ɜːrl' },
  { word: 'bag', ipa: 'bæ[g]' },
  { word: 'big', ipa: 'bɪ[g]' },
  { word: 'green', ipa: '[g]riːn' },
  { word: 'egg', ipa: 'e[g]' },
  { word: 'again', ipa: 'əˈ[g]en' },
  { word: 'glass', ipa: '[g]læs' },
  { word: 'dog', ipa: 'dɔː[g]' },
  { word: 'garden', ipa: 'ˈ[g]ɑːrdən' },

  // f
  { word: 'fish', ipa: '[f]ɪʃ' },
  { word: 'coffee', ipa: 'ˈkɔː[f]i' },
  { word: 'life', ipa: 'laɪ[f]' },
  { word: 'four', ipa: '[f]ɔːr' },
  { word: 'phone', ipa: '[f]oʊn' },
  { word: 'laugh', ipa: 'læ[f]' },
  { word: 'food', ipa: '[f]uːd' },
  { word: 'friend', ipa: '[f]rend' },
  { word: 'half', ipa: 'hæ[f]' },
  { word: 'first', ipa: '[f]ɜːrst' },

  // v
  { word: 'very', ipa: 'ˈ[v]eri' },
  { word: 'seven', ipa: 'ˈse[v]ən' },
  { word: 'love', ipa: 'lʌ[v]' },
  { word: 'five', ipa: 'faɪ[v]' },
  { word: 'voice', ipa: '[v]ɔɪs' },
  { word: 'river', ipa: 'ˈrɪ[v]ər' },
  { word: 'give', ipa: 'gɪ[v]' },
  { word: 'visit', ipa: 'ˈ[v]ɪzɪt' },
  { word: 'never', ipa: 'ˈne[v]ər' },
  { word: 'live', ipa: 'lɪ[v]' },

  // θ
  { word: 'think', ipa: '[θ]ɪŋk' },
  { word: 'three', ipa: '[θ]riː' },
  { word: 'bath', ipa: 'bæ[θ]' },
  { word: 'thank', ipa: '[θ]æŋk' },
  { word: 'month', ipa: 'mʌn[θ]' },
  { word: 'mouth', ipa: 'maʊ[θ]' },
  { word: 'thing', ipa: '[θ]ɪŋ' },
  { word: 'north', ipa: 'nɔːr[θ]' },
  { word: 'health', ipa: 'hel[θ]' },
  { word: 'birthday', ipa: 'ˈbɜːr[θ]deɪ' },

  // ð
  { word: 'this', ipa: '[ð]ɪs' },
  { word: 'mother', ipa: 'ˈmʌ[ð]ər' },
  { word: 'they', ipa: '[ð]eɪ' },
  { word: 'that', ipa: '[ð]æt' },
  { word: 'brother', ipa: 'ˈbrʌ[ð]ər' },
  { word: 'weather', ipa: 'ˈwe[ð]ər' },
  { word: 'other', ipa: 'ˈʌ[ð]ər' },
  { word: 'father', ipa: 'ˈfɑː[ð]ər' },
  { word: 'together', ipa: 'təˈge[ð]ər' },
  { word: 'than', ipa: '[ð]æn' },

  // s
  { word: 'sun', ipa: '[s]ʌn' },
  { word: 'city', ipa: 'ˈ[s]ɪti' },
  { word: 'bus', ipa: 'bʌ[s]' },
  { word: 'see', ipa: '[s]iː' },
  { word: 'ice', ipa: 'aɪ[s]' },
  { word: 'small', ipa: '[s]mɔːl' },
  { word: 'school', ipa: '[s]kuːl' },
  { word: 'stop', ipa: '[s]tɑːp' },
  { word: 'yes', ipa: 'je[s]' },
  { word: 'house', ipa: 'haʊ[s]' },

  // z
  { word: 'zoo', ipa: '[z]uː' },
  { word: 'music', ipa: 'ˈmjuː[z]ɪk' },
  { word: 'size', ipa: 'saɪ[z]' },
  { word: 'noise', ipa: 'nɔɪ[z]' },
  { word: 'busy', ipa: 'ˈbɪ[z]i' },
  { word: 'easy', ipa: 'ˈiː[z]i' },
  { word: 'please', ipa: 'pliː[z]' },
  { word: 'nose', ipa: 'noʊ[z]' },
  { word: 'zero', ipa: 'ˈ[z]ɪroʊ' },
  { word: 'is', ipa: 'ɪ[z]' },

  // ʃ
  { word: 'she', ipa: '[ʃ]iː' },
  { word: 'shop', ipa: '[ʃ]ɑːp' },
  { word: 'fish', ipa: 'fɪ[ʃ]' },
  { word: 'station', ipa: 'ˈsteɪ[ʃ]ən' },
  { word: 'wash', ipa: 'wɑː[ʃ]' },
  { word: 'shoes', ipa: '[ʃ]uːz' },
  { word: 'sugar', ipa: 'ˈ[ʃ]ʊgər' },
  { word: 'machine', ipa: 'məˈ[ʃ]iːn' },
  { word: 'short', ipa: '[ʃ]ɔːrt' },
  { word: 'English', ipa: 'ˈɪŋglɪ[ʃ]' },

  // ʒ
  { word: 'television', ipa: 'ˈtelɪvɪ[ʒ]ən' },
  { word: 'usual', ipa: 'ˈjuː[ʒ]uəl' },
  { word: 'measure', ipa: 'ˈme[ʒ]ər' },
  { word: 'vision', ipa: 'ˈvɪ[ʒ]ən' },
  { word: 'garage', ipa: 'gəˈrɑː[ʒ]' },
  { word: 'decision', ipa: 'dɪˈsɪ[ʒ]ən' },
  { word: 'pleasure', ipa: 'ˈple[ʒ]ər' },
  { word: 'casual', ipa: 'ˈkæ[ʒ]uəl' },
  { word: 'treasure', ipa: 'ˈtre[ʒ]ər' },
  { word: 'occasion', ipa: 'əˈkeɪ[ʒ]ən' },

  // h
  { word: 'hat', ipa: '[h]æt' },
  { word: 'hello', ipa: '[h]əˈloʊ' },
  { word: 'behind', ipa: 'bɪˈ[h]aɪnd' },
  { word: 'house', ipa: '[h]aʊs' },
  { word: 'help', ipa: '[h]elp' },
  { word: 'happy', ipa: 'ˈ[h]æpi' },
  { word: 'hand', ipa: '[h]ænd' },
  { word: 'hot', ipa: '[h]ɑːt' },
  { word: 'who', ipa: '[h]uː' },
  { word: 'ahead', ipa: 'əˈ[h]ed' },

  // tʃ
  { word: 'chair', ipa: '[tʃ]er' },
  { word: 'teacher', ipa: 'ˈtiː[tʃ]ər' },
  { word: 'watch', ipa: 'wɑː[tʃ]' },
  { word: 'lunch', ipa: 'lʌn[tʃ]' },
  { word: 'kitchen', ipa: 'ˈkɪ[tʃ]ən' },
  { word: 'cheese', ipa: '[tʃ]iːz' },
  { word: 'children', ipa: 'ˈ[tʃ]ɪldrən' },
  { word: 'catch', ipa: 'kæ[tʃ]' },
  { word: 'much', ipa: 'mʌ[tʃ]' },
  { word: 'question', ipa: 'ˈkwes[tʃ]ən' },

  // dʒ
  { word: 'job', ipa: '[dʒ]ɑːb' },
  { word: 'juice', ipa: '[dʒ]uːs' },
  { word: 'bridge', ipa: 'brɪ[dʒ]' },
  { word: 'orange', ipa: 'ˈɔːrɪn[dʒ]' },
  { word: 'enjoy', ipa: 'ɪnˈ[dʒ]ɔɪ' },
  { word: 'age', ipa: 'eɪ[dʒ]' },
  { word: 'jump', ipa: '[dʒ]ʌmp' },
  { word: 'change', ipa: 'tʃeɪn[dʒ]' },
  { word: 'village', ipa: 'ˈvɪlɪ[dʒ]' },
  { word: 'large', ipa: 'lɑːr[dʒ]' },

  // m
  { word: 'man', ipa: '[m]æn' },
  { word: 'summer', ipa: 'ˈsʌ[m]ər' },
  { word: 'time', ipa: 'taɪ[m]' },
  { word: 'moon', ipa: '[m]uːn' },
  { word: 'name', ipa: 'neɪ[m]' },
  { word: 'home', ipa: 'hoʊ[m]' },
  { word: 'make', ipa: '[m]eɪk' },
  { word: 'come', ipa: 'kʌ[m]' },
  { word: 'morning', ipa: 'ˈ[m]ɔːrnɪŋ' },
  { word: 'room', ipa: 'ruː[m]' },

  // n
  { word: 'no', ipa: '[n]oʊ' },
  { word: 'dinner', ipa: 'ˈdɪ[n]ər' },
  { word: 'sun', ipa: 'sʌ[n]' },
  { word: 'name', ipa: '[n]eɪm' },
  { word: 'night', ipa: '[n]aɪt' },
  { word: 'green', ipa: 'griː[n]' },
  { word: 'want', ipa: 'wɑː[n]t' },
  { word: 'money', ipa: 'ˈmʌ[n]i' },
  { word: 'know', ipa: '[n]oʊ' },
  { word: 'down', ipa: 'daʊ[n]' },

  // ŋ
  { word: 'sing', ipa: 'sɪ[ŋ]' },
  { word: 'long', ipa: 'lɔː[ŋ]' },
  { word: 'morning', ipa: 'ˈmɔːrnɪ[ŋ]' },
  { word: 'think', ipa: 'θɪ[ŋ]k' },
  { word: 'thank', ipa: 'θæ[ŋ]k' },
  { word: 'young', ipa: 'jʌ[ŋ]' },
  { word: 'English', ipa: 'ˈɪ[ŋ]glɪʃ' },
  { word: 'bring', ipa: 'brɪ[ŋ]' },
  { word: 'strong', ipa: 'strɔː[ŋ]' },
  { word: 'hungry', ipa: 'ˈhʌ[ŋ]gri' },

  // l
  { word: 'light', ipa: '[l]aɪt' },
  { word: 'yellow', ipa: 'ˈje[l]oʊ' },
  { word: 'ball', ipa: 'bɔː[l]' },
  { word: 'love', ipa: '[l]ʌv' },
  { word: 'school', ipa: 'skuː[l]' },
  { word: 'milk', ipa: 'mɪ[l]k' },
  { word: 'like', ipa: '[l]aɪk' },
  { word: 'help', ipa: 'he[l]p' },
  { word: 'hello', ipa: 'həˈ[l]oʊ' },
  { word: 'follow', ipa: 'ˈfɑː[l]oʊ' },

  // r
  { word: 'right', ipa: '[r]aɪt' },
  { word: 'sorry', ipa: 'ˈsɑː[r]i' },
  { word: 'car', ipa: 'kɑː[r]' },
  { word: 'red', ipa: '[r]ed' },
  { word: 'tree', ipa: 't[r]iː' },
  { word: 'rain', ipa: '[r]eɪn' },
  { word: 'read', ipa: '[r]iːd' },
  { word: 'friend', ipa: 'f[r]end' },
  { word: 'morning', ipa: 'ˈmɔː[r]nɪŋ' },
  { word: 'very', ipa: 'ˈve[r]i' },

  // w
  { word: 'we', ipa: '[w]iː' },
  { word: 'week', ipa: '[w]iːk' },
  { word: 'always', ipa: 'ˈɔːl[w]eɪz' },
  { word: 'window', ipa: 'ˈ[w]ɪndoʊ' },
  { word: 'one', ipa: '[w]ʌn' },
  { word: 'walk', ipa: '[w]ɔːk' },
  { word: 'want', ipa: '[w]ɑːnt' },
  { word: 'wait', ipa: '[w]eɪt' },
  { word: 'away', ipa: 'əˈ[w]eɪ' },
  { word: 'quick', ipa: 'k[w]ɪk' },

  // j
  { word: 'yes', ipa: '[j]es' },
  { word: 'year', ipa: '[j]ɪr' },
  { word: 'music', ipa: 'ˈm[j]uːzɪk' },
  { word: 'young', ipa: '[j]ʌŋ' },
  { word: 'yellow', ipa: '[j]eloʊ' },
  { word: 'you', ipa: '[j]uː' },
  { word: 'use', ipa: '[j]uːz' },
  { word: 'yesterday', ipa: 'ˈ[j]estərdeɪ' },
  { word: 'beautiful', ipa: 'ˈb[j]uːtɪfəl' },
  { word: 'computer', ipa: 'kəmˈp[j]uːtər' },
]

/**
 * 誤答に使う「混同しやすい記号」。同じ type から機械的に選ぶと無関係な記号が並んで
 * 消去法で解けてしまうため、記号ごとに手で列挙する。各4件から3件を出題時に抽選する。
 */
const SIMILAR_SYMBOLS: Record<string, string[]> = {
  // 母音
  iː: ['ɪ', 'e', 'eɪ', 'ə'],
  ɪ: ['iː', 'e', 'ə', 'æ'],
  e: ['æ', 'ɪ', 'eɪ', 'ʌ'],
  æ: ['e', 'ʌ', 'ɑː', 'ə'],
  ʌ: ['ɑː', 'æ', 'ə', 'ɔː'],
  ɑː: ['ʌ', 'ɔː', 'æ', 'oʊ'],
  ɔː: ['ɑː', 'oʊ', 'ʌ', 'ʊ'],
  ʊ: ['uː', 'ʌ', 'oʊ', 'ə'],
  uː: ['ʊ', 'oʊ', 'ɔː', 'ə'],
  ɜːr: ['ə', 'ʌ', 'ɑː', 'ɔː'],
  ə: ['ʌ', 'ɜːr', 'ɪ', 'e'],
  // 二重母音
  eɪ: ['e', 'aɪ', 'iː', 'ɪ'],
  aɪ: ['eɪ', 'aʊ', 'ɔɪ', 'ɑː'],
  ɔɪ: ['ɔː', 'aɪ', 'oʊ', 'aʊ'],
  aʊ: ['oʊ', 'aɪ', 'ɔː', 'uː'],
  oʊ: ['ɔː', 'aʊ', 'uː', 'ʊ'],
  // 子音
  p: ['b', 'f', 't', 'k'],
  b: ['p', 'v', 'd', 'm'],
  t: ['d', 'tʃ', 'θ', 'k'],
  d: ['t', 'ð', 'dʒ', 'b'],
  k: ['g', 't', 'p', 'h'],
  g: ['k', 'd', 'b', 'ŋ'],
  f: ['v', 'θ', 'h', 'p'],
  v: ['f', 'b', 'ð', 'w'],
  θ: ['s', 'f', 'ð', 't'],
  ð: ['z', 'θ', 'd', 'v'],
  s: ['θ', 'ʃ', 'z', 'f'],
  z: ['s', 'ʒ', 'ð', 'dʒ'],
  ʃ: ['s', 'tʃ', 'ʒ', 'θ'],
  ʒ: ['ʃ', 'dʒ', 'z', 'j'],
  h: ['f', 'θ', 'k', 'w'],
  tʃ: ['ʃ', 'dʒ', 't', 's'],
  dʒ: ['ʒ', 'tʃ', 'd', 'z'],
  m: ['n', 'ŋ', 'b', 'w'],
  n: ['m', 'ŋ', 'l', 'd'],
  ŋ: ['n', 'm', 'g', 'k'],
  l: ['r', 'n', 'w', 'j'],
  r: ['l', 'w', 'j', 'n'],
  w: ['v', 'r', 'j', 'l'],
  j: ['w', 'l', 'dʒ', 'ʒ'],
}

const BLANK = '___'
const bySymbol = new Map(ipaEntries.map((entry) => [entry.symbol, entry]))

/** 空所の記号を取り出す。データ検証と出題で共用する。 */
export function blankSymbol(ipa: string): string {
  return ipa.slice(ipa.indexOf('[') + 1, ipa.indexOf(']'))
}

/** 記号ごとの誤答候補(混同しやすい記号)。 */
export function similarSymbols(symbol: string): string[] {
  return SIMILAR_SYMBOLS[symbol] ?? []
}

function toQuestion(item: IpaQuizWord, rng: () => number): QuizQuestion {
  const symbol = blankSymbol(item.ipa)
  const entry = bySymbol.get(symbol)
  if (!entry) throw new Error(`未知の発音記号: ${symbol} (${item.word})`)
  return {
    id: `ipa-${item.word}-${symbol}`,
    prompt: `「${item.word}」の発音記号です。${BLANK} に入る記号を選んでください。`,
    promptAudio: item.word,
    sentence: `/${item.ipa.replace(/\[[^\]]*\]/, BLANK)}/`,
    choices: [symbol, ...sample(similarSymbols(symbol), 3, rng)],
    correctIndex: 0,
    explanation: `${item.word} は /${item.ipa.replace(/[[\]]/g, '')}/ と発音します。${entry.ja}`,
    audioEn: item.word,
  }
}

/** 語彙全体から count 問をランダムに出題する。 */
export function buildIpaQuestions(count: number, rng: () => number = Math.random): QuizQuestion[] {
  return sample(ipaQuizWords, count, rng).map((item) => toQuestion(item, rng))
}
