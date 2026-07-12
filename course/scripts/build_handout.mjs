import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import React from "../../website/node_modules/react/index.js";
import { renderToStaticMarkup } from "../../website/node_modules/react-dom/server.node.js";
import ReactMarkdown from "../../website/node_modules/react-markdown/index.js";
import remarkGfm from "../../website/node_modules/remark-gfm/index.js";
import remarkMath from "../../website/node_modules/remark-math/index.js";
import rehypeRaw from "../../website/node_modules/rehype-raw/index.js";
import rehypeKatex from "../../website/node_modules/rehype-katex/index.js";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const courseDir = path.resolve(scriptDir, "..");
const repoDir = path.resolve(courseDir, "..");
const inputPath = path.join(courseDir, "merged_chapters.md");
const outputPath = path.join(courseDir, "merged_chapters.html");

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
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
      .replace(/[*_`]/g, "")
      .trim();
    const id = slugger.slug(label);
    if (level <= 2) headings.push({ level, label, id });
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

function normalizeHref(href = "") {
  if (/^(?:https?:|mailto:|#)/.test(href)) return href;
  const markdownLink = /^(?:\.\.\/)?(?:chapters\/)?[^/#]+\.md(#[^#]+)?$/.exec(href);
  if (markdownLink?.[1]) return markdownLink[1];
  return href;
}

function normalizeImageSrc(src = "") {
  return src.startsWith("../figures/") ? src.slice(3) : src;
}

const markdown = fs.readFileSync(inputPath, "utf8");
const headings = collectHeadings(markdown);
const chapterHeadings = headings.filter(({ level }) => level === 1);
const slugger = new Slugger();

const components = {
  h1({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h1", { ...props, id: slugger.slug(label), className: "chapter-title" }, children);
  },
  h2({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h2", { ...props, id: slugger.slug(label) }, children);
  },
  h3({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h3", { ...props, id: slugger.slug(label) }, children);
  },
  h4({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h4", { ...props, id: slugger.slug(label) }, children);
  },
  h5({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h5", { ...props, id: slugger.slug(label) }, children);
  },
  h6({ children, node: _node, ...props }) {
    const label = textContent(children);
    return React.createElement("h6", { ...props, id: slugger.slug(label) }, children);
  },
  details({ children, node: _node, ...props }) {
    return React.createElement("details", { ...props, open: true }, children);
  },
  a({ children, href, node: _node, ...props }) {
    return React.createElement("a", { ...props, href: normalizeHref(href) }, children);
  },
  img({ src, alt, node: _node, ...props }) {
    return React.createElement("img", { ...props, src: normalizeImageSrc(src), alt: alt ?? "" });
  },
};

const renderedArticleHtml = renderToStaticMarkup(
  React.createElement(
    ReactMarkdown,
    {
      remarkPlugins: [remarkGfm, remarkMath],
      rehypePlugins: [rehypeRaw, rehypeKatex],
      components,
    },
    markdown,
  ),
);

// CommonMark treats Markdown inside raw <details> blocks conservatively.
// The source intentionally uses bold lead-ins there, so restore that small,
// well-defined subset after React has safely escaped the surrounding text.
const articleHtml = renderedArticleHtml.replace(/\*\*([^*<>\n]+?)\*\*/g, "<strong>$1</strong>");

const tocHtml = chapterHeadings
  .map(({ label, id }, index) => `<li><a href="#${escapeHtml(id)}"><span>${String(index + 1).padStart(2, "0")}</span>${escapeHtml(label.replace(/^第\s*\d+\s*章[：:]?\s*/, ""))}</a></li>`)
  .join("\n");

const katexCss = embedKatexFonts(
  fs.readFileSync(path.join(repoDir, "website/node_modules/katex/dist/katex.min.css"), "utf8"),
);

const handoutCss = String.raw`
:root {
  --ink: #1f2933;
  --muted: #52606d;
  --accent: #245c73;
  --accent-soft: #e9f2f5;
  --paper: #fffefb;
  --rule: #cbd5dc;
  --answer: #f2f7f3;
  --answer-rule: #6f9277;
}

@page {
  size: A4;
  margin: 17mm 17mm 19mm;
  @top-left { content: "統計學互動講義"; color: #65737e; font-size: 8.5pt; }
  @top-right { content: string(chapter); color: #65737e; font-size: 8.5pt; }
  @bottom-center { content: counter(page); color: #65737e; font-size: 8.5pt; }
}

@page :first {
  margin: 0;
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-center { content: none; }
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: #e7ebee;
  font-family: "Noto Serif TC", "Songti TC", "PMingLiU", serif;
  font-size: 11.2pt;
  line-height: 1.75;
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
  min-height: 245mm;
  padding: 33mm 20mm 20mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f7fafc;
  background: linear-gradient(145deg, #163b4a 0%, #245c73 58%, #8caeae 100%);
  break-after: page;
}
.cover-kicker { margin: 0; font: 600 10pt/1.4 system-ui, sans-serif; letter-spacing: .22em; }
.cover h1 { max-width: 135mm; margin: 0; font-size: 34pt; line-height: 1.25; letter-spacing: .06em; }
.cover-subtitle { max-width: 125mm; margin: 7mm 0 0; font-size: 15pt; line-height: 1.65; color: #dcecef; }
.cover-meta { padding-top: 7mm; border-top: 1px solid rgba(255,255,255,.42); font: 10pt/1.6 system-ui, sans-serif; color: #edf5f6; }

.toc { break-after: page; padding: 8mm 3mm 0; }
.toc h2 { margin: 0 0 8mm; border: 0; font-size: 24pt; color: var(--accent); }
.toc ol { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 10mm; margin: 0; padding: 0; list-style: none; }
.toc li { margin: 0; }
.toc a { display: flex; gap: 3mm; align-items: baseline; padding: 2.5mm 0; border-bottom: 1px solid var(--rule); color: var(--ink); text-decoration: none; }
.toc a span { min-width: 8mm; color: var(--accent); font: 700 9pt/1 system-ui, sans-serif; letter-spacing: .08em; }

article { counter-reset: figure table; }
.chapter-title {
  string-set: chapter content(text);
  break-before: page;
  margin: 0 0 12mm;
  padding: 23mm 0 8mm;
  border-bottom: 1.2mm solid var(--accent);
  color: #173f50;
  font-size: 25pt;
  line-height: 1.3;
  letter-spacing: .035em;
}
article > .chapter-title:first-child { break-before: auto; }
h2, h3, h4, h5, h6 { color: #173f50; line-height: 1.42; break-after: avoid; }
h2 { margin: 11mm 0 4mm; padding-bottom: 2mm; border-bottom: .35mm solid #9fb7c1; font-size: 17.5pt; }
h3 { margin: 8mm 0 3mm; font-size: 14pt; }
h4 { margin: 6mm 0 2.5mm; font-size: 12.2pt; }
h5, h6 { margin: 5mm 0 2mm; font-size: 11.2pt; }
p { margin: 0 0 4mm; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 4.5mm; padding-left: 7mm; }
li { margin: 1.2mm 0; }
li > p { margin-bottom: 1.5mm; }
strong { color: #102f3b; }
a { color: #1e667f; text-decoration-thickness: .2mm; text-underline-offset: .5mm; }
hr { margin: 9mm 0; border: 0; border-top: .3mm solid var(--rule); }

blockquote {
  margin: 5mm 0;
  padding: 3.5mm 5mm;
  border-left: 1.2mm solid var(--accent);
  background: var(--accent-soft);
  color: #314852;
  break-inside: avoid;
}
blockquote > :last-child { margin-bottom: 0; }
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
  font-size: 9.6pt;
  line-height: 1.55;
}
thead { display: table-header-group; }
tr { break-inside: avoid; }
th, td { padding: 2.2mm 2.5mm; border: .25mm solid #aebbc3; vertical-align: top; }
th { background: #e6eef1; color: #173f50; font-weight: 700; text-align: left; }
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
.katex { font-size: 1.02em; }
.katex-display { margin: 5mm 0; overflow: hidden; break-inside: avoid; }
.katex-display > .katex { max-width: 100%; white-space: normal; }

details {
  margin: 5mm 0 7mm;
  padding: 0 4.5mm 4mm;
  border: .3mm solid #b6c9bb;
  border-left: 1.2mm solid var(--answer-rule);
  border-radius: 1.5mm;
  background: var(--answer);
  break-inside: auto;
}
summary {
  margin: 0 -4.5mm 3.5mm;
  padding: 2.8mm 4.5mm;
  border-bottom: .25mm solid #c9d8cc;
  color: #365b3e;
  font-family: system-ui, sans-serif;
  font-size: 10pt;
  font-weight: 700;
  letter-spacing: .04em;
  list-style: none;
  break-after: avoid;
}
summary::-webkit-details-marker { display: none; }
summary::before { content: "詳解｜"; color: #6d8f74; }
details > :last-child { margin-bottom: 0; }

@media print {
  body { background: white; font-size: 10.8pt; }
  .book { width: auto; margin: 0; padding: 0; box-shadow: none; }
  .cover { width: 210mm; height: 297mm; min-height: 297mm; margin: 0; padding: 50mm 37mm 30mm; }
  a { color: inherit; text-decoration: none; }
  details { display: block; }
  details > * { display: block; }
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
  <title>統計學互動講義</title>
  <style>${katexCss}\n${handoutCss}</style>
</head>
<body>
  <main class="book">
    <section class="cover">
      <p class="cover-kicker">STATISTICS · COURSE HANDOUT</p>
      <div>
        <h1>統計學互動講義</h1>
        <p class="cover-subtitle">從描述資料到多重比較：以例題、圖解、檢核與逐步詳解建立統計推理。</p>
      </div>
      <p class="cover-meta">全 12 章 · 講義列印版<br>所有練習答案與詳解均已展開</p>
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
console.log(`${chapterHeadings.length} chapters; ${[...output.matchAll(/<details\b/g)].length} expanded detail blocks`);
