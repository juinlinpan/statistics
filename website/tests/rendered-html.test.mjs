import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import test from "node:test";

async function render(pathname = "/") {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}-${pathname}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request(`http://localhost${pathname}`, { headers: { accept: "text/html" } }),
    { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
    { waitUntil() {}, passThroughOnException() {} },
  );
}

test("server-renders the finished course home", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type") ?? "", /^text\/html\b/i);
  const html = await response.text();

  assert.match(html, /<html lang="zh-Hant">/i);
  assert.match(html, /<title>救救我的統計 R<\/title>/i);
  assert.match(html, /統計新手的 12 章求生講義/);
  assert.match(html, /href="\/chapter\/descriptive-statistics"/);
  assert.match(html, /href="\/chapter\/multiple-comparisons"/);
  assert.match(html, /property="og:image"/);
  assert.doesNotMatch(html, /怎麼學|課程地圖|HOW IT WORKS|COURSE MAP/);
  assert.doesNotMatch(html, /codex-preview|Your site is taking shape|react-loading-skeleton/i);
});

test("server-renders the canonical lesson, formula anchors, and interactions", async () => {
  const response = await render("/chapter/descriptive-statistics");
  assert.equal(response.status, 200);
  const html = await response.text();

  assert.match(html, /第 1 章：描述統計與資料探索/);
  assert.match(html, /id="formula-ch01-sample-mean"/);
  assert.match(html, /src="\/figures\/01-commute-histogram.png"/);
  assert.match(html, /id="interactive-lab"/);
  assert.match(html, /id="interactive-practice"/);
  assert.match(html, /選項背後的迷思/);
  assert.match(html, /互動實驗/);
  assert.match(html, /診斷練習/);
  assert.doesNotMatch(html, /把理解變成判斷/);
  assert.match(html, /拿掉 58 分鐘後，哪個摘要量的變化會比較大/);
  assert.doesNotMatch(html, /type="range"/);
});

test("removes all starter-preview infrastructure", async () => {
  const [page, layout, packageJson] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/layout.tsx", import.meta.url), "utf8"),
    readFile(new URL("../package.json", import.meta.url), "utf8"),
  ]);

  assert.doesNotMatch(page, /SkeletonPreview|codex-preview/);
  assert.doesNotMatch(layout, /Starter Project|codex-preview/);
  assert.doesNotMatch(packageJson, /react-loading-skeleton/);
  await assert.rejects(access(new URL("../app/_sites-preview", import.meta.url)));
});
