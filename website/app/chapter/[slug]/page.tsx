import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight, Clock3, Image as ImageIcon, ListChecks } from "lucide-react";
import { CourseHeader } from "@/components/CourseHeader";
import { MarkdownLesson } from "@/components/MarkdownLesson";
import { PracticePanel } from "@/components/PracticePanel";
import { ProgressTools } from "@/components/ProgressTools";
import { StatLab } from "@/components/StatLab";
import { chapters, getChapter } from "@/lib/course-data";

export function generateStaticParams() {
  return chapters.map((chapter) => ({ slug: chapter.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const chapter = getChapter(slug);
  return chapter ? { title: `第 ${chapter.number} 章｜${chapter.title}`, description: chapter.description } : {};
}

export default async function ChapterPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const chapter = getChapter(slug);
  if (!chapter) notFound();
  const previous = chapters[chapter.number - 2];
  const next = chapters[chapter.number];

  return (
    <div style={{ "--chapter-accent": chapter.accent } as React.CSSProperties}>
      <CourseHeader activeSlug={chapter.slug} />
      <main>
        <section className="chapter-hero">
          <div className="chapter-rail" aria-hidden="true"><span>{String(chapter.number).padStart(2, "0")}</span></div>
          <div className="chapter-hero-inner">
            <Link href="/#chapters" className="back-link"><ArrowLeft size={16} />回到 12 章課程</Link>
            <span className="chapter-label">CHAPTER {String(chapter.number).padStart(2, "0")}</span>
            <h1>{chapter.title}</h1>
            <p>{chapter.eyebrow}</p>
            <div className="chapter-facts"><span><Clock3 size={17} />約 45–70 分鐘</span><span><ListChecks size={17} />{chapter.questions.length} 個互動練習</span><span><ImageIcon size={17} />{chapter.figureCount} 張教學圖</span></div>
          </div>
        </section>
        <div className="chapter-layout">
          <aside className="chapter-sidebar">
            <p>本章學習路徑</p>
            <a href="#lesson">01　完整講義</a>
            <a href="#interactive-lab">02　互動實驗</a>
            <a href="#interactive-practice">03　診斷練習</a>
            <ProgressTools compact />
          </aside>
          <div className="chapter-main">
            <section id="lesson"><MarkdownLesson content={chapter.content} /></section>
            <div id="interactive-lab"><StatLab chapterNumber={chapter.number} accent={chapter.accent} /></div>
            <PracticePanel questions={chapter.questions} chapterSlug={chapter.slug} />
          </div>
        </div>
        <nav className="chapter-next" aria-label="前後章節">
          {previous ? <Link href={`/chapter/${previous.slug}`}><ArrowLeft /><span><small>上一章</small>{previous.title}</span></Link> : <span />}
          {next ? <Link href={`/chapter/${next.slug}`}><span><small>下一章</small>{next.title}</span><ArrowRight /></Link> : <Link href="/"><span><small>完成課程</small>回到首頁</span><ArrowRight /></Link>}
        </nav>
      </main>
    </div>
  );
}
