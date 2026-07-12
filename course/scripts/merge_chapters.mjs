import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const courseDir = path.resolve(scriptDir, "..");
const chaptersDir = path.join(courseDir, "chapters");
const outputPath = path.join(courseDir, "merged_chapters.md");

const chapterFiles = fs
  .readdirSync(chaptersDir)
  .filter((name) => /^\d{2}-.*\.md$/.test(name))
  .sort();

if (chapterFiles.length !== 12) {
  throw new Error(`Expected 12 chapter files, found ${chapterFiles.length}`);
}

function stripFrontmatter(markdown, filename) {
  if (!markdown.startsWith("---\n")) return markdown.trim();
  const end = markdown.indexOf("\n---\n", 4);
  if (end === -1) throw new Error(`Unclosed frontmatter in ${filename}`);
  return markdown.slice(end + 5).trim();
}

const chapters = chapterFiles.map((filename, index) => {
  const source = fs.readFileSync(path.join(chaptersDir, filename), "utf8");
  const body = stripFrontmatter(source, filename);
  const expectedTitle = new RegExp(`^# 第 ${index + 1} 章[：:]`, "m");
  if (!expectedTitle.test(body)) {
    throw new Error(`Unexpected or missing chapter title in ${filename}`);
  }
  return `${body}\n\n<div style="page-break-after: always;"></div>`;
});

fs.writeFileSync(outputPath, `${chapters.join("\n\n")}\n`);
console.log(`Merged ${chapterFiles.length} chapters into ${path.relative(path.resolve(courseDir, ".."), outputPath)}`);
