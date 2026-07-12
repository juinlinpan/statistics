import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const packageJson = JSON.parse(await readFile(new URL("package.json", root), "utf8"));
const tauriConfig = JSON.parse(await readFile(new URL("src-tauri/tauri.conf.json", root), "utf8"));
const cargo = await readFile(new URL("src-tauri/Cargo.toml", root), "utf8");
const cargoVersion = cargo.match(/^version = "([^"]+)"$/m)?.[1];

assert.match(packageJson.version, /^\d+\.\d+\.\d+$/, "package.json must use a semantic version");
assert.equal(tauriConfig.version, packageJson.version, "tauri.conf.json version differs from package.json");
assert.equal(cargoVersion, packageJson.version, "Cargo.toml version differs from package.json");
console.log(`desktop version ${packageJson.version} is synchronized`);
