import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { chapterFiles, examChapterFiles } from "./handout_manifest.mjs";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(scriptDir, "../../..");
const courseDir = path.join(repoDir, "course_2");
const chaptersDir = path.join(courseDir, "chapters");
const slidesOutput = path.join(courseDir, "course2-slides-handout.md");
const solutionsOutput = path.join(courseDir, "course2-exam-solutions.md");
const mergedBasenames = new Set(chapterFiles);

function stripFrontmatter(markdown, filename) {
  if (!markdown.startsWith("---\n")) return markdown.trim();
  const end = markdown.indexOf("\n---\n", 4);
  if (end === -1) throw new Error(`Unclosed frontmatter in ${filename}`);
  return markdown.slice(end + 5).trim();
}

function toPosix(value) {
  return value.split(path.sep).join("/");
}

function rewriteDestination(rawDestination, mode) {
  const destination = rawDestination.trim();
  if (/^(?:https?:|mailto:|data:)/.test(destination)) return destination;
  const wrapped = destination.startsWith("<") && destination.endsWith(">");
  const unwrapped = wrapped ? destination.slice(1, -1) : destination;
  const hashAt = unwrapped.indexOf("#");
  const pathname = hashAt === -1 ? unwrapped : unwrapped.slice(0, hashAt);
  const fragment = hashAt === -1 ? "" : unwrapped.slice(hashAt);

  if (!pathname && fragment) {
    return mode === "solutions" ? `./course2-slides-handout.html${fragment}` : fragment;
  }

  if (pathname && mergedBasenames.has(path.basename(pathname)) && fragment) {
    return mode === "solutions" ? `./course2-slides-handout.html${fragment}` : fragment;
  }

  if (!pathname) return destination;
  const absoluteTarget = path.resolve(chaptersDir, pathname);
  let rebased = toPosix(path.relative(courseDir, absoluteTarget));
  if (!rebased.startsWith(".")) rebased = `./${rebased}`;
  const result = `${rebased}${fragment}`;
  return wrapped ? `<${result}>` : result;
}

function rewriteLocalLinks(markdown, mode) {
  return markdown.replace(/(!?\[[^\]]*\]\()([^)]+)(\))/g, (_whole, open, destination, close) => {
    return `${open}${rewriteDestination(destination, mode)}${close}`;
  });
}

function teachingPart(body, filename) {
  const marker = "\n## 考古題與詳解";
  const examAt = body.indexOf(marker);
  const result = examAt === -1 ? body : body.slice(0, examAt).trim();
  if (!/^# .+$/m.test(result)) throw new Error(`Missing teaching H1 in ${filename}`);
  return rewriteLocalLinks(result, "slides");
}

function linkLabel(value) {
  return value.replaceAll("[", "\\[").replaceAll("]", "\\]");
}

function coreMethodLinks(solutionLines) {
  const method = solutionLines.find((line) => /\*\*選方法：\*\*/.test(line)) ?? "";
  const calculation = solutionLines.find((line) => /\*\*(?:代入)?計算／推理：\*\*/.test(line)) ?? "";
  const methodCore = method.split("；", 1)[0];
  const source = /\]\([^)]*#[^)]+\)/.test(methodCore)
    ? methodCore
    : /\]\([^)]*#[^)]+\)/.test(calculation)
      ? calculation
      : solutionLines.join("\n");
  const links = [];
  const seen = new Set();
  for (const match of source.matchAll(/\[([^\]]+)\]\(([^)]*#[^)]+)\)/g)) {
    const key = `${match[1]}|${match[2]}`;
    if (seen.has(key)) continue;
    seen.add(key);
    links.push(`[${linkLabel(match[1])}](${match[2]})`);
  }
  return links;
}

function solutionsPart(body, filename) {
  const marker = "\n## 考古題與詳解";
  const examAt = body.indexOf(marker);
  if (examAt === -1) throw new Error(`Missing exam section in ${filename}`);
  const title = body.match(/^# (.+)$/m)?.[1];
  const chapter = body.match(/^# 第 (\d+) 章/m)?.[1];
  if (!title || !chapter) throw new Error(`Cannot determine chapter title in ${filename}`);

  const lines = body.slice(examAt + 1).split("\n");
  const questions = [];
  for (let index = 0; index < lines.length; index += 1) {
    const match = /^#### (選擇題|計算題) (\d+)(?:：.*)?$/.exec(lines[index]);
    if (match) questions.push({ index, type: match[1], number: Number(match[2]) });
  }
  if (!questions.length) throw new Error(`No exam questions found in ${filename}`);

  const output = [
    `# ${title}｜考古題詳解`,
    "",
    "## 考古題詳解",
    "",
    `本章收錄 ${questions.length} 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。`,
    "",
  ];

  let index = 0;
  while (index < lines.length) {
    if (/^### (?:選擇題|計算題)｜/.test(lines[index])) {
      output.push(lines[index], "");
      index += 1;
      continue;
    }

    if (/^#### 題組 /.test(lines[index])) {
      let end = index + 1;
      while (end < lines.length && !/^#{3,4} /.test(lines[end])) end += 1;
      const groupLines = lines.slice(index, end);
      while (groupLines.length && !groupLines[groupLines.length - 1].trim()) groupLines.pop();
      output.push(...groupLines, "");
      index = end;
      continue;
    }

    const match = /^#### (選擇題|計算題) (\d+)(?:：.*)?$/.exec(lines[index]);
    if (!match) {
      index += 1;
      continue;
    }

    let end = index + 1;
    while (end < lines.length && !/^#{3,4} /.test(lines[end])) end += 1;
    const questionLines = lines.slice(index + 1, end);
    const titleAt = questionLines.findIndex((line) => line === "##### 題目");
    const detailAt = questionLines.findIndex((line) => line === "##### 詳解");
    if (titleAt === -1 || detailAt === -1 || titleAt >= detailAt) {
      throw new Error(`Missing ordered 題目／詳解 for ${match[1]} ${match[2]} in ${filename}`);
    }
    while (questionLines.length && !questionLines[questionLines.length - 1].trim()) questionLines.pop();
    const solutionLines = questionLines.slice(detailAt + 1);
    const methodLinks = coreMethodLinks(solutionLines);
    const kind = match[1] === "選擇題" ? "mc" : "problem";
    output.push(
      `#### ${match[1]} ${match[2]} <a id="exam-ch${chapter}-${kind}-${match[2]}"></a>`,
      ...questionLines.slice(0, detailAt + 1),
      "",
    );
    if (methodLinks.length) output.push(`> **回看投影片講義：** ${methodLinks.join("、")}`, "");
    output.push(...solutionLines, "");
    index = end;
  }

  return rewriteLocalLinks(output.join("\n").trim(), "solutions");
}

function readChapter(filename) {
  const sourcePath = path.join(chaptersDir, filename);
  if (!fs.existsSync(sourcePath)) throw new Error(`Missing chapter: ${filename}`);
  return stripFrontmatter(fs.readFileSync(sourcePath, "utf8"), filename);
}

const separator = '<div class="page-break" style="page-break-after: always;"></div>';
const slides = chapterFiles.map((filename) => teachingPart(readChapter(filename), filename));
const examBodies = examChapterFiles.map((filename) => ({ filename, body: readChapter(filename) }));
const solutions = examBodies.map(({ filename, body }) => solutionsPart(body, filename));

const expectedExamStats = examBodies.reduce((totals, { filename, body }) => {
  const questions = (body.match(/^#### (?:選擇題|計算題) \d+(?:：.*?)?$/gm) ?? []).length;
  const titles = (body.match(/^##### 題目$/gm) ?? []).length;
  const details = (body.match(/^##### 詳解$/gm) ?? []).length;
  const groups = (body.match(/^#### 題組 /gm) ?? []).length;
  if (!questions || questions !== titles || questions !== details) {
    throw new Error(`${filename} has ${questions} questions, ${titles} 題目, and ${details} 詳解`);
  }
  return {
    questions: totals.questions + questions,
    groups: totals.groups + groups,
  };
}, { questions: 0, groups: 0 });

fs.writeFileSync(slidesOutput, `${slides.join(`\n\n${separator}\n\n`)}\n`);
fs.writeFileSync(solutionsOutput, `${solutions.join(`\n\n${separator}\n\n`)}\n`);

const solutionText = fs.readFileSync(solutionsOutput, "utf8");
const solutionQuestions = (solutionText.match(/^#### (?:選擇題|計算題) \d+ /gm) ?? []).length;
const solutionTitles = (solutionText.match(/^##### 題目$/gm) ?? []).length;
const solutionDetails = (solutionText.match(/^##### 詳解$/gm) ?? []).length;
const solutionGroups = (solutionText.match(/^#### 題組 /gm) ?? []).length;
if (solutionQuestions !== expectedExamStats.questions || solutionTitles !== solutionQuestions || solutionDetails !== solutionQuestions) {
  throw new Error(`Expected ${expectedExamStats.questions} ordered 題目／詳解 pairs; found ${solutionQuestions} questions, ${solutionTitles} 題目, ${solutionDetails} 詳解`);
}
if (solutionGroups !== expectedExamStats.groups) {
  throw new Error(`Expected ${expectedExamStats.groups} shared question groups, found ${solutionGroups}`);
}

console.log(`Built ${path.relative(repoDir, slidesOutput)} from ${chapterFiles.length} original chapter Markdown files`);
console.log(`Built ${path.relative(repoDir, solutionsOutput)} with ${solutionQuestions} single-copy 題目／詳解 pairs and ${solutionGroups} shared question groups`);
