import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { fileURLToPath } from "node:url";

export default defineConfig({
  root: "desktop",
  base: "./",
  publicDir: "../public",
  plugins: [react()],
  css: {
    postcss: fileURLToPath(new URL(".", import.meta.url)),
  },
  server: {
    port: 1420,
    strictPort: true,
  },
  build: {
    outDir: "../desktop-dist",
    emptyOutDir: true,
  },
});
