// batchNN.py が /tmp に出した JSON を illustrations.ts へ追記する。
// 同じキーが複数回出たら、あとの回（描き直し）の alt / caption を採用する。
import fs from 'node:fs'
import path from 'node:path'

const TS = 'src/content/vocabulary/illustrations.ts'
const files = process.argv.slice(2)
if (files.length === 0) {
  console.error('usage: node append-ts.mjs /tmp/batch168.json ...')
  process.exit(1)
}

const entries = new Map()
for (const f of files) {
  for (const e of JSON.parse(fs.readFileSync(f, 'utf8'))) entries.set(e.key, e)
}

const src = fs.readFileSync(TS, 'utf8')
const existing = new Set([...src.matchAll(/^ {2}'?([^':\n]+?)'?: \{$/gm)].map((m) => m[1]))
const quote = (k) => (/^[A-Za-z_$][\w$]*$/.test(k) ? k : `'${k.replace(/'/g, "\\'")}'`)

const added = []
for (const [key, e] of entries) {
  if (existing.has(key)) continue
  added.push(
    `  ${quote(key)}: {\n` +
    `    src: 'images/vocabulary/${e.slug}.svg',\n` +
    `    alt: '${e.alt.replace(/'/g, "\\'")}',\n` +
    `    caption: '${e.caption.replace(/'/g, "\\'")}',\n` +
    `  },\n`,
  )
  if (!fs.existsSync(path.join('public/images/vocabulary', `${e.slug}.svg`))) {
    console.error(`missing svg: ${e.slug}.svg`)
    process.exit(1)
  }
}

const close = src.lastIndexOf('}\n')
fs.writeFileSync(TS, src.slice(0, close) + added.join('') + src.slice(close))
console.log(`added ${added.length} entries (${entries.size} in manifests)`)
