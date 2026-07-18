import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawn, spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(scriptDir, "../../..");
const courseDir = path.join(repoDir, "course_2");
const outputDir = path.join(repoDir, "output", "pdf");

const allEditions = [
  {
    name: "slides",
    html: path.join(courseDir, "course2-slides-handout.html"),
    pdf: path.join(outputDir, "course2-slides-handout.pdf"),
  },
  {
    name: "solutions",
    html: path.join(courseDir, "course2-exam-solutions.html"),
    pdf: path.join(outputDir, "course2-exam-solutions.pdf"),
  },
];
const requestedEdition = process.env.COURSE2_PRINT_EDITION;
if (requestedEdition && !allEditions.some(({ name }) => name === requestedEdition)) {
  throw new Error(`Unknown COURSE2_PRINT_EDITION: ${requestedEdition}`);
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: repoDir,
    encoding: "utf8",
    stdio: options.capture ? "pipe" : "inherit",
    timeout: options.timeout ?? 300_000,
    env: { ...process.env, ...(options.env ?? {}) },
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    throw new Error(`${command} failed with exit ${result.status}\n${result.stderr ?? ""}`);
  }
  return result;
}

const sleep = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));

function signalProcessGroup(child, signal) {
  try {
    if (process.platform !== "win32" && child.pid) process.kill(-child.pid, signal);
    else child.kill(signal);
  } catch (error) {
    if (error.code !== "ESRCH") throw error;
  }
}

async function printPdf(chromePath, edition, profileDir) {
  fs.rmSync(edition.pdf, { force: true });
  const child = spawn(chromePath, [
    "--headless=new",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-background-networking",
    "--disable-component-update",
    "--disable-sync",
    "--metrics-recording-only",
    "--no-first-run",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    `--user-data-dir=${profileDir}`,
    `--print-to-pdf=${edition.pdf}`,
    pathToFileURL(edition.html).href,
  ], {
    cwd: repoDir,
    detached: process.platform !== "win32",
    stdio: ["ignore", "inherit", "inherit"],
  });

  let exited = false;
  let exitCode = null;
  child.once("exit", (code) => {
    exited = true;
    exitCode = code;
  });

  const deadline = Date.now() + 180_000;
  let previousSize = -1;
  let stableChecks = 0;
  let valid = false;
  while (Date.now() < deadline) {
    if (fs.existsSync(edition.pdf)) {
      const stat = fs.statSync(edition.pdf);
      const signature = fs.readFileSync(edition.pdf).subarray(0, 4).toString("ascii");
      if (signature === "%PDF" && stat.size >= 100_000) {
        stableChecks = stat.size === previousSize ? stableChecks + 1 : 0;
        previousSize = stat.size;
        if (stableChecks >= 3) {
          valid = true;
          break;
        }
      }
    }
    if (exited && exitCode !== 0) break;
    await sleep(500);
  }

  if (!exited) {
    signalProcessGroup(child, "SIGTERM");
    for (let attempt = 0; attempt < 10 && !exited; attempt += 1) await sleep(200);
    if (!exited) signalProcessGroup(child, "SIGKILL");
  }

  if (!valid) {
    throw new Error(`Chrome did not create a stable ${edition.name} PDF (exit ${exitCode ?? "pending"})`);
  }
}

if (process.env.COURSE2_SKIP_PRINT_BUILD !== "1") {
  run(process.execPath, [path.join(scriptDir, "split_print_editions.mjs")]);
  for (const edition of allEditions) {
    run(process.execPath, [path.join(scriptDir, "build_handout.mjs")], {
      env: { COURSE2_HANDOUT_EDITION: edition.name },
    });
  }
}

// Chrome occasionally leaves background processes behind after printing. Run
// each edition in its own short-lived Node process so one print cannot prevent
// the other edition from being exported.
if (!requestedEdition) {
  for (const edition of allEditions) {
    run(process.execPath, [fileURLToPath(import.meta.url)], {
      env: {
        COURSE2_PRINT_EDITION: edition.name,
        COURSE2_SKIP_PRINT_BUILD: "1",
      },
      timeout: 900_000,
    });
  }
  process.exit(0);
}

const editions = allEditions.filter(({ name }) => name === requestedEdition);

const chromeCandidates = [
  process.env.CHROME_PATH,
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/Applications/Chromium.app/Contents/MacOS/Chromium",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
].filter(Boolean);
const chromePath = chromeCandidates.find((candidate) => fs.existsSync(candidate));
if (!chromePath) throw new Error("Chrome/Chromium not found. Set CHROME_PATH to a browser executable.");

fs.mkdirSync(outputDir, { recursive: true });
for (const edition of editions) {
  const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), `course2-${edition.name}-chrome-`));
  try {
    await printPdf(chromePath, edition, profileDir);
  } finally {
    fs.rmSync(profileDir, { recursive: true, force: true });
  }

  if (!fs.existsSync(edition.pdf)) throw new Error(`Chrome did not create ${edition.pdf}`);
  const stat = fs.statSync(edition.pdf);
  const signature = fs.readFileSync(edition.pdf).subarray(0, 4).toString("ascii");
  if (signature !== "%PDF" || stat.size < 100_000) {
    throw new Error(`Invalid ${edition.name} PDF: ${stat.size} bytes, signature ${signature}`);
  }
  const info = spawnSync("pdfinfo", [edition.pdf], { encoding: "utf8" });
  const pages = info.status === 0
    ? info.stdout.split(/\r?\n/).find((line) => line.startsWith("Pages:")) ?? ""
    : "";
  console.log(`Exported ${path.relative(repoDir, edition.pdf)} (${(stat.size / 1024 / 1024).toFixed(1)} MiB)${pages ? `; ${pages}` : ""}`);
}
