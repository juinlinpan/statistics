import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import React from "../../../website/node_modules/react/index.js";
import { renderToStaticMarkup } from "../../../website/node_modules/react-dom/server.node.js";
import ReactMarkdown from "../../../website/node_modules/react-markdown/index.js";
import remarkGfm from "../../../website/node_modules/remark-gfm/index.js";
import remarkMath from "../../../website/node_modules/remark-math/index.js";
import rehypeRaw from "../../../website/node_modules/rehype-raw/index.js";
import rehypeKatex from "../../../website/node_modules/rehype-katex/index.js";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(scriptDir, "../../..");
const courseDir = path.join(repoDir, "course_2");
const inputPath = path.join(courseDir, "merged_chapters.md");
const outputPath = path.join(courseDir, "merged_chapters.html");

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function escapeCssString(value) {
  return value
    .replaceAll("\\", "\\\\")
    .replaceAll('"', '\\"')
    .replaceAll("\n", " ");
}

function textContent(node) {
  if (typeof node === "string" || typeof node === "number") return String(node);
  if (Array.isArray(node)) return node.map(textContent).join("");
  if (React.isValidElement(node)) return textContent(node.props.children);
  return "";
}

class Slugger {
  constructor() {
    this.seen = new Map();
  }

  slug(value) {
    const base = value
      .trim()
      .toLowerCase()
      .replace(/[\s]+/g, "-")
      .replace(/[!"#$%&'()*+,./:;<=>?@[\\\]^`{|}~，。！？：；、（）【】〈〉《》「」『』]/g, "")
      .replace(/^-+|-+$/g, "") || "section";
    const count = this.seen.get(base) ?? 0;
    this.seen.set(base, count + 1);
    return count === 0 ? base : `${base}-${count}`;
  }
}

function collectHeadings(markdown) {
  const slugger = new Slugger();
  const headings = [];
  for (const line of markdown.split(/\r?\n/)) {
    const match = /^(#{1,6})\s+(.+?)\s*#*$/.exec(line);
    if (!match) continue;
    const level = match[1].length;
    const label = match[2]
      .replace(/\[(.*?)\]\([^)]*\)/g, "$1")
      .replace(/[*_`$]/g, "")
      .trim();
    headings.push({ level, label, id: slugger.slug(label) });
  }
  return headings;
}

function embedKatexFonts(css) {
  const katexDir = path.join(repoDir, "website/node_modules/katex/dist");
  return css.replace(/url\(([^)]+)\)/g, (whole, rawUrl) => {
    const cleanUrl = rawUrl.replace(/["']/g, "");
    const fontPath = path.resolve(katexDir, cleanUrl);
    if (!fontPath.startsWith(katexDir) || !fs.existsSync(fontPath)) return whole;
    const extension = path.extname(fontPath).slice(1);
    const mime = extension === "woff2" ? "font/woff2" : extension === "woff" ? "font/woff" : "application/octet-stream";
    return `url(data:${mime};base64,${fs.readFileSync(fontPath).toString("base64")})`;
  });
}

function normalizeInlineCurrencyMath(source) {
  // remark-math treats the escaped dollar inside `$\$1{,}000$` as a closing
  // delimiter. Currency does not need math layout, so render that narrow
  // pattern as ordinary escaped text while leaving formulas untouched.
  return source.replace(/\$\\\$([^$\n]+)\$/g, (_whole, amount) => {
    return `\\$${amount.replaceAll("{,}", ",")}`;
  });
}

if (!fs.existsSync(inputPath)) {
  throw new Error(`Missing ${path.relative(repoDir, inputPath)}; run merge_chapters.mjs first`);
}

const markdown = fs.readFileSync(inputPath, "utf8");
const renderMarkdown = normalizeInlineCurrencyMath(markdown);
const headings = collectHeadings(markdown);
const chapterHeadings = headings.filter(({ level }) => level === 1);
if (chapterHeadings.length !== 6) {
  throw new Error(`Expected 6 completed chapters in merged Markdown, found ${chapterHeadings.length}`);
}

const questionCount = (markdown.match(/^#### (?:選擇題|計算題) \d+(?:：.*?)?(?:\s+<a id="exam-ch\d+-(?:mc|problem)-\d+"><\/a>)?$/gm) ?? []).length;
const figureCount = (markdown.match(/^!\[[^\]]*\]\([^)]+\)$/gm) ?? []).length;
const slugger = new Slugger();

function headingComponent(tagName) {
  return function Heading({ children, node: _node, ...props }) {
    const label = textContent(children);
    const classes = [];
    if (tagName === "h1") classes.push("chapter-title");
    if (tagName === "h4" && /^(?:選擇題|計算題|題組)\s/.test(label)) classes.push("question-heading");
    if (tagName === "h5" && label === "題目") classes.push("prompt-heading");
    if (tagName === "h5" && label === "詳解") classes.push("solution-heading");
    return React.createElement(tagName, {
      ...props,
      id: slugger.slug(label),
      className: classes.length ? classes.join(" ") : undefined,
    }, children);
  };
}

const components = {
  h1: headingComponent("h1"),
  h2: headingComponent("h2"),
  h3: headingComponent("h3"),
  h4: headingComponent("h4"),
  h5: headingComponent("h5"),
  h6: headingComponent("h6"),
  a({ children, href, node: _node, ...props }) {
    return React.createElement("a", { ...props, href }, children);
  },
  blockquote({ children, node: _node, ...props }) {
    const label = textContent(children).trim();
    const classes = ["callout"];
    if (label.startsWith("對應考古題：")) classes.push("exam-crossref", "exam-crossref-questions");
    if (label.startsWith("回看講義：")) classes.push("exam-crossref", "exam-crossref-theory");
    return React.createElement("blockquote", {
      ...props,
      className: classes.join(" "),
    }, children);
  },
  img({ src, alt, node: _node, ...props }) {
    return React.createElement("img", { ...props, src, alt: alt ?? "" });
  },
};

const renderedArticleHtml = renderToStaticMarkup(
  React.createElement(
    ReactMarkdown,
    {
      remarkPlugins: [remarkGfm, remarkMath],
      rehypePlugins: [rehypeRaw, [rehypeKatex, { strict: "ignore", throwOnError: false }]],
      components,
    },
    renderMarkdown,
  ),
);

function wrapChapterSections(html, expectedHeadings) {
  const starts = [...html.matchAll(/<h1 id="([^"]+)" class="chapter-title">/g)];
  if (starts.length !== expectedHeadings.length) {
    throw new Error(`Expected ${expectedHeadings.length} rendered chapter starts, found ${starts.length}`);
  }

  return starts.map((match, index) => {
    const expected = expectedHeadings[index];
    if (match[1] !== expected.id) {
      throw new Error(`Rendered chapter order mismatch: expected ${expected.id}, found ${match[1]}`);
    }
    const end = starts[index + 1]?.index ?? html.length;
    const chapterHtml = html
      .slice(match.index, end)
      .replace(/\s*<div class="page-break" style="page-break-after:always"><\/div>\s*$/, "")
      .trim();
    return `<section class="chapter chapter-${index + 1}">${chapterHtml}</section>`;
  }).join("\n");
}

const articleHtml = wrapChapterSections(renderedArticleHtml, chapterHeadings);

const tocHtml = chapterHeadings
  .map(({ label, id }, index) => {
    const shortLabel = label.replace(/^第\s*(?:7[–-]10|\d+)\s*章[：:]?\s*/, "");
    return `<li><a href="#${escapeHtml(id)}"><span>${String(index + 1).padStart(2, "0")}</span>${escapeHtml(shortLabel)}</a></li>`;
  })
  .join("\n");

const katexCss = embedKatexFonts(
  fs.readFileSync(path.join(repoDir, "website/node_modules/katex/dist/katex.min.css"), "utf8"),
);

const chapterPageCss = chapterHeadings.map(({ label }, index) => String.raw`
.chapter-${index + 1} { page: chapter-${index + 1}; }
@page chapter-${index + 1} {
  @top-right { content: "${escapeCssString(label)}"; color: #65737e; font-size: 8.5pt; }
}`).join("\n");

const handoutCss = String.raw`
:root {
  --ink: #24303a;
  --muted: #61707d;
  --accent: #315f74;
  --accent-dark: #173f50;
  --accent-soft: #eaf2f5;
  --paper: #fffefb;
  --rule: #c9d4da;
  --solution: #3f6b4b;
  --solution-soft: #edf5ef;
}

@page {
  size: A4;
  margin: 17mm 16mm 19mm;
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-right { content: counter(page); color: #65737e; font-size: 8.5pt; }
}

@page cover {
  margin: 0;
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-right { content: none; }
}

@page contents {
  @top-right { content: "目錄"; color: #65737e; font-size: 8.5pt; }
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: #e7ebee;
  font-family: "Noto Serif TC", "Songti TC", "PMingLiU", serif;
  font-size: 10.8pt;
  line-height: 1.72;
  text-rendering: optimizeLegibility;
}

.book {
  width: 210mm;
  margin: 10mm auto;
  padding: 17mm;
  background: var(--paper);
  box-shadow: 0 8px 32px rgba(31, 41, 51, .16);
}

.cover {
  page: cover;
  min-height: 245mm;
  padding: 30mm 20mm 20mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f7fafc;
  background: linear-gradient(145deg, #173f50 0%, #315f74 57%, #91aeb7 100%);
  break-after: page;
}
.cover-kicker { margin: 0; font: 600 10pt/1.4 system-ui, sans-serif; letter-spacing: .2em; }
.cover h1 { max-width: 140mm; margin: 0; font-size: 34pt; line-height: 1.23; letter-spacing: .055em; }
.cover-subtitle { max-width: 130mm; margin: 7mm 0 0; font-size: 14.5pt; line-height: 1.65; color: #dcecef; }
.cover-meta { padding-top: 7mm; border-top: 1px solid rgba(255,255,255,.42); font: 10pt/1.65 system-ui, sans-serif; color: #edf5f6; }

.toc { page: contents; break-after: page; padding: 8mm 3mm 0; }
.toc h2 { margin: 0 0 8mm; border: 0; font-size: 24pt; color: var(--accent); }
.toc ol { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 10mm; margin: 0; padding: 0; list-style: none; }
.toc li { margin: 0; }
.toc a { display: flex; gap: 3mm; align-items: baseline; padding: 2.5mm 0; border-bottom: 1px solid var(--rule); color: var(--ink); text-decoration: none; }
.toc a span { min-width: 8mm; color: var(--accent); font: 700 9pt/1 system-ui, sans-serif; letter-spacing: .08em; }

article { counter-reset: figure table; }
.page-break { break-after: page; height: 0; }
.chapter { break-before: page; }
.chapter-title {
  margin: 0 0 12mm;
  padding: 23mm 0 8mm;
  border-bottom: 1.2mm solid var(--accent);
  color: var(--accent-dark);
  font-size: 25pt;
  line-height: 1.3;
  letter-spacing: .035em;
  break-inside: avoid-page;
  break-after: avoid-page;
}
h2, h3, h4, h5, h6 {
  color: var(--accent-dark);
  line-height: 1.42;
  break-inside: avoid-page;
  break-after: avoid-page;
}
h2 { margin: 11mm 0 4mm; padding-bottom: 2mm; border-bottom: .35mm solid #9fb7c1; font-size: 17.5pt; }
h3 { margin: 8mm 0 3mm; font-size: 14pt; }
h4 { margin: 6mm 0 2.5mm; font-size: 12.2pt; }
h5, h6 { margin: 5mm 0 2mm; font-size: 11.2pt; }
.question-heading { padding-top: 2mm; border-top: .3mm solid #d6dfe3; }
.prompt-heading { color: var(--accent); }
.solution-heading { padding: 2mm 3mm; border-left: 1mm solid #73947b; background: var(--solution-soft); color: var(--solution); }
p { margin: 0 0 4mm; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 4.5mm; padding-left: 7mm; }
li { margin: 1.2mm 0; }
li > p { margin-bottom: 1.5mm; }
strong { color: #102f3b; }
a { color: #1e667f; text-decoration-thickness: .2mm; text-underline-offset: .5mm; }
hr { margin: 9mm 0; border: 0; border-top: .3mm solid var(--rule); }

blockquote {
  margin: 4mm 0 5mm;
  padding: 3.5mm 5mm;
  border-left: 1.1mm solid var(--accent);
  background: var(--accent-soft);
  color: #314852;
}
blockquote > :last-child { margin-bottom: 0; }
.exam-crossref {
  margin: 2.2mm 0 4mm;
  padding: 2mm 3mm;
  border-left-width: .75mm;
  font-size: 8.8pt;
  line-height: 1.55;
  break-inside: avoid-page;
}
.exam-crossref p { margin: 0; }
.exam-crossref-questions { background: #f3f7f8; }
.exam-crossref-theory {
  border-left-color: #73947b;
  background: #f2f7f3;
}
code {
  padding: .2mm 1mm;
  border-radius: 1mm;
  background: #eef1f3;
  font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
  font-size: .88em;
}
pre {
  margin: 5mm 0;
  padding: 4mm;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
  border: .25mm solid var(--rule);
  border-radius: 2mm;
  background: #f6f7f8;
  break-inside: avoid;
}
pre code { padding: 0; background: none; }

table {
  width: 100%;
  margin: 5mm 0 7mm;
  border-collapse: collapse;
  font-size: 9.15pt;
  line-height: 1.5;
}
thead { display: table-header-group; }
tr { break-inside: avoid; }
th, td { padding: 2mm 2.3mm; border: .25mm solid #aebbc3; vertical-align: top; overflow-wrap: anywhere; }
th { background: #e6eef1; color: var(--accent-dark); font-weight: 700; text-align: left; }
tbody tr:nth-child(even) { background: #f8faf9; }

img {
  display: block;
  max-width: 100%;
  max-height: 165mm;
  width: auto;
  height: auto;
  margin: 6mm auto;
  object-fit: contain;
  break-inside: avoid;
}
.katex { font-size: .98em; }
.katex-display { margin: 5mm 0; overflow: hidden; break-inside: avoid; }
.katex-display > .katex { max-width: 100%; }

@media print {
  body { background: white; font-size: 10.5pt; }
  .book { width: auto; margin: 0; padding: 0; box-shadow: none; }
  .cover { width: 210mm; height: 297mm; min-height: 297mm; margin: 0; padding: 50mm 37mm 30mm; }
  a { color: inherit; text-decoration: none; }
}

@media screen and (max-width: 850px) {
  .book { width: 100%; margin: 0; padding: 7vw; }
  .cover { min-height: 86vh; margin: -7vw -7vw 8vw; padding: 15vw 10vw 10vw; }
  .toc ol { grid-template-columns: 1fr; }
}
`;

const output = `<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>商業統計講義｜估計、檢定與迴歸</title>
  <style>${katexCss}\n${handoutCss}\n${chapterPageCss}</style>
</head>
<body>
  <main class="book">
    <section class="cover">
      <p class="cover-kicker">BUSINESS STATISTICS · COURSE HANDOUT</p>
      <div>
        <h1>商業統計講義</h1>
        <p class="cover-subtitle">從估計與檢定，到卡方、ANOVA 與迴歸模型：用直覺、公式、圖解與完整考古題詳解串起統計推理。</p>
      </div>
      <p class="cover-meta">已完成章節版 · 第 7–16 章 · ${chapterHeadings.length} 份講義<br>${questionCount} 題考古題 · ${figureCount} 張統計圖解 · 詳解完整展開</p>
    </section>
    <nav class="toc" aria-label="目錄">
      <h2>目錄</h2>
      <ol>${tocHtml}</ol>
    </nav>
    <article>${articleHtml}</article>
  </main>
</body>
</html>
`;

fs.writeFileSync(outputPath, output);
console.log(`Built ${path.relative(repoDir, outputPath)} from ${path.relative(repoDir, inputPath)}`);
console.log(`${chapterHeadings.length} chapters; ${questionCount} exam questions; ${figureCount} figures`);
