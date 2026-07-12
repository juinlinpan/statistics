"use client";

import Link from "next/link";
import { BookOpen, Menu, X } from "lucide-react";
import { useState } from "react";
import { chapters } from "@/lib/course-data";

export function CourseHeader({ activeSlug }: { activeSlug?: string }) {
  const [open, setOpen] = useState(false);

  return (
    <header className="site-header">
      <div className="header-inner">
        <Link href="/" className="brand" aria-label="救救我的統計 R 首頁">
          <span className="brand-mark"><BookOpen size={19} strokeWidth={2} /></span>
          <span className="brand-title">救救我的統計 R</span>
        </Link>
        <nav className="desktop-nav" aria-label="主要導覽">
          <Link href="/#chapters">12 章課程</Link>
        </nav>
        <button className="menu-button" onClick={() => setOpen(!open)} aria-label={open ? "關閉章節選單" : "開啟章節選單"} aria-expanded={open}>
          {open ? <X /> : <Menu />}
        </button>
      </div>
      {open && (
        <nav className="mobile-menu" aria-label="章節導覽">
          {chapters.map((chapter) => (
            <Link key={chapter.slug} href={`/chapter/${chapter.slug}`} onClick={() => setOpen(false)} className={activeSlug === chapter.slug ? "active" : ""}>
              <span>{String(chapter.number).padStart(2, "0")}</span>{chapter.title}
            </Link>
          ))}
        </nav>
      )}
    </header>
  );
}
