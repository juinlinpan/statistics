import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const html = await readFile(new URL("desktop-dist/index.html", root), "utf8");
const figures = (await readdir(new URL("desktop-dist/figures/", root))).filter((name) => name.endsWith(".png"));

assert.match(html, /<title>救救我的統計 R<\/title>/);
assert.match(html, /\.\/assets\/index-[^"']+\.js/);
assert.match(html, /\.\/assets\/index-[^"']+\.css/);
assert.equal(figures.length, 23, "desktop bundle must contain all 23 course figures");
await access(new URL("desktop-dist/figures/01-commute-histogram.png", root));
await access(new URL("desktop-dist/figures/12-fwer-curve.png", root));
console.log("desktop static bundle contains the course shell and all figures");
