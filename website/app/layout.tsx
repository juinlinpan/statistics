import type { Metadata } from "next";
import { headers } from "next/headers";
import "katex/dist/katex.min.css";
import "./globals.css";

export async function generateMetadata(): Promise<Metadata> {
  const requestHeaders = await headers();
  const host = requestHeaders.get("host") ?? "localhost:3000";
  const origin = `${host.startsWith("localhost") ? "http" : "https"}://${host}`;
  const title = "救救我的統計 R";
  const description = "統計新手的 12 章求生講義：完整講義、圖表、診斷練習與互動實驗。";
  return {
    title: { default: title, template: `%s｜${title}` },
    description,
    icons: { icon: "/favicon.svg", shortcut: "/favicon.svg" },
    openGraph: { title, description, type: "website", locale: "zh_TW", images: [{ url: `${origin}/og-v2.png`, width: 1728, height: 896, alt: `${title}｜12 章統計求生講義` }] },
    twitter: { card: "summary_large_image", title, description, images: [`${origin}/og-v2.png`] },
  };
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="zh-Hant"><body>{children}</body></html>;
}
