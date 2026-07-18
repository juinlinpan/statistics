import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { chapterFiles } from "./handout_manifest.mjs";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(scriptDir, "../../..");
const courseDir = path.join(repoDir, "course_2");
const chaptersDir = path.join(courseDir, "chapters");
const outputPath = path.join(courseDir, "merged_chapters.md");

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

function rewriteDestination(rawDestination, filename) {
  const destination = rawDestination.trim();
  if (/^(?:https?:|mailto:|data:|#)/.test(destination)) return destination;

  // This course does not use Markdown link titles. Fail visibly if one appears,
  // rather than silently rewriting an ambiguous target.
  if (/\s+["'].*["']$/.test(destination)) {
    throw new Error(`Link titles are not supported by the merger: ${filename}: ${destination}`);
  }

  const wrapped = destination.startsWith("<") && destination.endsWith(">");
  const unwrapped = wrapped ? destination.slice(1, -1) : destination;
  const hashAt = unwrapped.indexOf("#");
  const pathname = hashAt === -1 ? unwrapped : unwrapped.slice(0, hashAt);
  const fragment = hashAt === -1 ? "" : unwrapped.slice(hashAt);

  if (!pathname) return fragment || destination;

  // Links between merged chapters become in-document links.
  if (mergedBasenames.has(path.basename(pathname)) && fragment) return fragment;

  const absoluteTarget = path.resolve(chaptersDir, pathname);
  let rebased = toPosix(path.relative(courseDir, absoluteTarget));
  if (!rebased.startsWith(".")) rebased = `./${rebased}`;
  const result = `${rebased}${fragment}`;
  return wrapped ? `<${result}>` : result;
}

function rewriteLocalLinks(markdown, filename) {
  return markdown.replace(/(!?\[[^\]]*\]\()([^)]+)(\))/g, (_whole, open, destination, close) => {
    return `${open}${rewriteDestination(destination, filename)}${close}`;
  });
}

function examQuestionId(chapter, type, number) {
  const kind = type === "選擇題" ? "mc" : "problem";
  return `exam-ch${chapter}-${kind}-${number}`;
}

function markdownLinkLabel(value) {
  return value.replaceAll("[", "\\[").replaceAll("]", "\\]");
}

function formatQuestionLinks(questions) {
  const groups = new Map();
  for (const question of questions) {
    const key = `${question.chapter}:${question.type}`;
    const group = groups.get(key) ?? [];
    group.push(question);
    groups.set(key, group);
  }

  return [...groups.values()]
    .sort((a, b) => Number(a[0].chapter) - Number(b[0].chapter)
      || ["選擇題", "計算題"].indexOf(a[0].type) - ["選擇題", "計算題"].indexOf(b[0].type))
    .map((group) => {
      const [{ chapter, type }] = group;
      const links = group
        .sort((a, b) => a.number - b.number)
        .map(({ number }) => `[${number}](#${examQuestionId(chapter, type, number)})`);
      return `Ch${chapter} ${type} ${links.join("、")}`;
    })
    .join("；");
}

function anchorIdsFromText(text) {
  const ids = [];
  for (const match of text.matchAll(/\]\(([^)]+)\)/g)) {
    const destination = match[1];
    const hashAt = destination.lastIndexOf("#");
    if (hashAt !== -1 && hashAt < destination.length - 1) {
      ids.push(destination.slice(hashAt + 1));
    }
  }
  return ids;
}

function analyzeChapter(filename, body) {
  const lines = body.split("\n");
  const examLine = lines.findIndex((line) => line === "## 考古題與詳解");
  const chapterMatch = body.match(/^# 第 (\d+) 章/m);
  const chapter = chapterMatch?.[1] ?? null;
  const anchors = [];
  let previousHeading = null;
  const teachingEnd = examLine === -1 ? lines.length : examLine;

  for (let index = 0; index < teachingEnd; index += 1) {
    const heading = /^(#{2,4})\s+(.+)$/.exec(lines[index]);
    if (heading) previousHeading = { index, label: heading[2] };

    const anchor = /<a id="([^"]+)"><\/a>/.exec(lines[index]);
    if (!anchor) continue;
    let next = index + 1;
    while (next < teachingEnd && !lines[next].trim()) next += 1;
    const followingHeading = /^(#{2,4})\s+(.+)$/.exec(lines[next] ?? "");
    const target = followingHeading
      ? { index: next, label: followingHeading[2] }
      : previousHeading;
    if (target) anchors.push({ id: anchor[1], filename, ...target });
  }

  const questions = [];
  if (examLine !== -1) {
    if (!chapter) throw new Error(`Cannot determine exam chapter number in ${filename}`);
    for (let index = examLine + 1; index < lines.length; index += 1) {
      const match = /^#### (選擇題|計算題) (\d+)(?:：.*)?$/.exec(lines[index]);
      if (match) {
        questions.push({
          filename,
          chapter,
          index,
          type: match[1],
          number: Number(match[2]),
        });
      }
    }
  }

  return { filename, body, lines, examLine, chapter, anchors, questions };
}

function chooseQuestionAnchors(record, question, questionIndex, globalAnchorTargets) {
  const end = record.questions[questionIndex + 1]?.index ?? record.lines.length;
  const blockLines = record.lines.slice(question.index, end);
  const methodLines = blockLines.filter((line) => /\*\*選方法：\*\*/.test(line));
  const calculationLines = blockLines.filter((line) => /\*\*(?:代入)?計算／推理：\*\*/.test(line));

  // In a method sentence, the first semicolon-delimited clause is the primary
  // technique. Later clauses usually contain diagnostics or caveats.
  const methodCore = methodLines.map((line) => line.split("；", 1)[0]).join("\n");
  const priorityIds = anchorIdsFromText(methodCore).length
    ? anchorIdsFromText(methodCore)
    : anchorIdsFromText(calculationLines.join("\n"));
  const allIds = anchorIdsFromText(blockLines.join("\n"));

  function validUnique(ids) {
    return [...new Set(ids)].filter((id) => globalAnchorTargets.has(id));
  }

  const priority = validUnique(priorityIds);
  const all = validUnique(allIds);
  const prioritySpecific = priority.filter((id) => !id.startsWith("compare-"));
  const allSpecific = all.filter((id) => !id.startsWith("compare-"));
  const fallback = `compare-ch${question.chapter}-method-selection`;
  const chosen = prioritySpecific.length
    ? prioritySpecific
    : allSpecific.length
      ? allSpecific
      : priority.length
        ? priority
        : all.length
          ? all
          : [fallback];

  if (!globalAnchorTargets.has(fallback)) {
    throw new Error(`Missing fallback method-selection anchor ${fallback} in ${record.filename}`);
  }
  return { ids: chosen, end };
}

function addExamCrossReferences(records) {
  const globalAnchorTargets = new Map();
  for (const record of records) {
    for (const target of record.anchors) globalAnchorTargets.set(target.id, target);
  }

  const reverseReferences = new Map();
  const insertions = new Map(records.map((record) => [record.filename, {
    headingAnchors: new Map(),
    after: new Map(),
  }]));
  let questionCount = 0;

  for (const record of records) {
    record.questions.forEach((question, questionIndex) => {
      const { ids, end } = chooseQuestionAnchors(record, question, questionIndex, globalAnchorTargets);
      const targets = [];
      const seenTargets = new Set();
      for (const id of ids) {
        const target = globalAnchorTargets.get(id);
        const targetKey = `${target.filename}:${target.index}`;
        if (seenTargets.has(targetKey)) continue;
        seenTargets.add(targetKey);
        targets.push({ anchor: id, ...target });
        const references = reverseReferences.get(targetKey) ?? [];
        references.push(question);
        reverseReferences.set(targetKey, references);
      }

      const insertion = insertions.get(record.filename);
      insertion.headingAnchors.set(
        question.index,
        `<a id="${examQuestionId(question.chapter, question.type, question.number)}"></a>`,
      );
      const solutionOffset = record.lines
        .slice(question.index, end)
        .findIndex((line) => line === "##### 詳解");
      if (solutionOffset === -1) {
        throw new Error(`Missing 詳解 heading for ${question.type} ${question.number} in ${record.filename}`);
      }
      const solutionLine = question.index + solutionOffset;
      const theoryLinks = targets.map(({ anchor, label }) => {
        return `[${markdownLinkLabel(label)}](#${anchor})`;
      });
      insertion.after.set(solutionLine, [
        "",
        "<!-- exam-theory-links:start -->",
        `> **回看講義：** ${theoryLinks.join("、")}`,
        "<!-- exam-theory-links:end -->",
      ]);
      questionCount += 1;
    });
  }

  for (const [targetKey, references] of reverseReferences) {
    const separatorAt = targetKey.lastIndexOf(":");
    const filename = targetKey.slice(0, separatorAt);
    const headingIndex = Number(targetKey.slice(separatorAt + 1));
    const unique = [...new Map(references.map((question) => [
      `${question.chapter}:${question.type}:${question.number}`,
      question,
    ])).values()];
    const insertion = insertions.get(filename);
    insertion.after.set(headingIndex, [
      "",
      "<!-- exam-question-links:start -->",
      `> **對應考古題：** ${formatQuestionLinks(unique)}`,
      "<!-- exam-question-links:end -->",
      ...(insertion.after.get(headingIndex) ?? []),
    ]);
  }

  const bodies = new Map();
  for (const record of records) {
    const { headingAnchors, after } = insertions.get(record.filename);
    const augmented = [];
    record.lines.forEach((line, index) => {
      augmented.push(headingAnchors.has(index) ? `${line} ${headingAnchors.get(index)}` : line);
      if (after.has(index)) augmented.push(...after.get(index));
    });
    bodies.set(record.filename, augmented.join("\n"));
  }

  return { bodies, questionCount, reverseReferenceCount: reverseReferences.size };
}

function validateChapter(body, filename) {
  const h1 = body.match(/^# .+$/gm) ?? [];
  if (h1.length !== 1) throw new Error(`Expected exactly one H1 in ${filename}, found ${h1.length}`);
  if (!/^# 第 (?:7[–-]10|\d+) 章/m.test(body)) {
    throw new Error(`Unexpected chapter title in ${filename}: ${h1[0] ?? "missing"}`);
  }
  if (/本檔為講義骨架|老師尚未公布|<!--\s*Phase\s+[1-8]/.test(body)) {
    throw new Error(`Scaffold or unfinished phase marker found in ${filename}`);
  }
}

const seenAnchors = new Map();
const records = chapterFiles.map((filename) => {
  const sourcePath = path.join(chaptersDir, filename);
  if (!fs.existsSync(sourcePath)) throw new Error(`Missing chapter: ${filename}`);
  const source = fs.readFileSync(sourcePath, "utf8");
  const body = stripFrontmatter(source, filename);
  validateChapter(body, filename);

  for (const match of body.matchAll(/<a id="([^"]+)"/g)) {
    const id = match[1];
    if (seenAnchors.has(id)) {
      throw new Error(`Duplicate anchor ${id}: ${seenAnchors.get(id)} and ${filename}`);
    }
    seenAnchors.set(id, filename);
  }

  return analyzeChapter(filename, body);
});

const crossReferenced = addExamCrossReferences(records);
const chapters = records.map(({ filename }) => {
  return rewriteLocalLinks(crossReferenced.bodies.get(filename), filename);
});

const separator = '<div class="page-break" style="page-break-after: always;"></div>';
fs.writeFileSync(outputPath, `${chapters.join(`\n\n${separator}\n\n`)}\n`);

console.log(`Merged ${chapterFiles.length} completed chapter files into ${path.relative(repoDir, outputPath)}`);
console.log(`${seenAnchors.size} explicit anchors preserved; local links rebased for the merged Markdown`);
console.log(`${crossReferenced.questionCount} exam-question anchors generated; every question linked back to its primary teaching method`);
console.log(`${crossReferenced.reverseReferenceCount} teaching sections list their corresponding exam questions, including cross-chapter links`);
