import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawn, spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(scriptDir, "../../..");
const courseDir = path.join(repoDir, "course_2");
const htmlPath = path.join(courseDir, "merged_chapters.html");
const outputDir = path.join(repoDir, "output", "pdf");
const pdfPath = path.join(outputDir, "course2-business-statistics-handout.pdf");

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: repoDir,
    encoding: "utf8",
    stdio: options.capture ? "pipe" : "inherit",
    timeout: options.timeout ?? 300_000,
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

async function printPdf(chromePath, profileDir) {
  fs.rmSync(pdfPath, { force: true });
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
    `--print-to-pdf=${pdfPath}`,
    pathToFileURL(htmlPath).href,
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

  const deadline = Date.now() + 300_000;
  let previousSize = -1;
  let stableChecks = 0;
  let valid = false;
  while (Date.now() < deadline) {
    if (fs.existsSync(pdfPath)) {
      const stat = fs.statSync(pdfPath);
      const signature = fs.readFileSync(pdfPath).subarray(0, 4).toString("ascii");
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
  if (!valid) throw new Error(`Chrome did not create a stable PDF (exit ${exitCode ?? "pending"})`);
}

run(process.execPath, [path.join(scriptDir, "merge_chapters.mjs")]);
run(process.execPath, [path.join(scriptDir, "build_handout.mjs")]);

const chromeCandidates = [
  process.env.CHROME_PATH,
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/Applications/Chromium.app/Contents/MacOS/Chromium",
  "/usr/bin/google-chrome",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
].filter(Boolean);
const chromePath = chromeCandidates.find((candidate) => fs.existsSync(candidate));
if (!chromePath) {
  throw new Error("Chrome/Chromium not found. Set CHROME_PATH to a browser executable.");
}

fs.mkdirSync(outputDir, { recursive: true });
const profileDir = fs.mkdtempSync(path.join(os.tmpdir(), "course2-handout-chrome-"));
try {
  await printPdf(chromePath, profileDir);
} finally {
  fs.rmSync(profileDir, { recursive: true, force: true });
}

if (!fs.existsSync(pdfPath)) throw new Error(`Chrome did not create ${pdfPath}`);
const stat = fs.statSync(pdfPath);
const signature = fs.readFileSync(pdfPath).subarray(0, 4).toString("ascii");
if (signature !== "%PDF" || stat.size < 100_000) {
  throw new Error(`Invalid or unexpectedly small PDF: ${stat.size} bytes, signature ${signature}`);
}

let pageSummary = "";
const pdfInfo = spawnSync("pdfinfo", [pdfPath], { encoding: "utf8" });
if (pdfInfo.status === 0) {
  pageSummary = pdfInfo.stdout.split(/\r?\n/).find((line) => line.startsWith("Pages:")) ?? "";
}

console.log(`Exported ${path.relative(repoDir, pdfPath)} (${(stat.size / 1024 / 1024).toFixed(1)} MiB)${pageSummary ? `; ${pageSummary}` : ""}`);
