import { useEffect, useState } from "react";
import { ArrowLeft, ArrowRight, BarChart3, BookOpen, Clock3, Image as ImageIcon, ListChecks, MoveRight, Sparkles } from "lucide-react";
import { MarkdownLesson } from "../components/MarkdownLesson";
import { PracticePanel } from "../components/PracticePanel";
import { ProgressTools } from "../components/ProgressTools";
import { StatLab } from "../components/StatLab";
import { chapters, getChapter } from "../lib/course-data";

const storageKey = "stats-course:desktop-current-chapter";

export function DesktopApp() {
  const [slug, setSlug] = useState<string>();

  useEffect(() => {
    const saved = sessionStorage.getItem(storageKey);
    if (saved && getChapter(saved)) setSlug(saved);
  }, []);

  const openChapter = (nextSlug: string) => {
    setSlug(nextSlug);
    sessionStorage.setItem(storageKey, nextSlug);
    history.replaceState(null, "", location.pathname);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const goHome = () => {
    setSlug(undefined);
    sessionStorage.removeItem(storageKey);
    history.replaceState(null, "", location.pathname);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const chapter = slug ? getChapter(slug) : undefined;

  return (
    <>
      <header className="site-header desktop-app-header">
        <div className="header-inner">
          <button className="brand desktop-brand-button" onClick={goHome} aria-label="回到救救我的統計 R 首頁">
            <span className="brand-mark"><BookOpen size={19} strokeWidth={2} /></span>
            <span className="brand-title">救救我的統計 R</span>
          </button>
          <button className="desktop-all-chapters" onClick={goHome}>12 章課程</button>
        </div>
      </header>
      {chapter ? <DesktopChapter slug={chapter.slug} openChapter={openChapter} goHome={goHome} /> : <DesktopHome openChapter={openChapter} />}
    </>
  );
}

function DesktopHome({ openChapter }: { openChapter: (slug: string) => void }) {
  return (
    <main>
      <section className="home-hero desktop-home-hero">
        <div className="hero-copy">
          <span className="hero-kicker"><Sparkles size={15} />統計新手求生講義 · 桌面版</span>
          <h1>救救我的<br /><span>統計 R</span></h1>
          <p>公式看不懂、檢定一直選錯、p 值到底在說什麼？從第 1 章開始，一次救一個觀念。所有講義、圖片與互動都已包在程式裡，不需要網路。</p>
          <button className="hero-primary desktop-primary" onClick={() => openChapter(chapters[0].slug)}>從第 1 章開始<ArrowRight size={18} /></button>
        </div>
        <div className="hero-visual" aria-label="從原始資料走到清楚判斷的學習示意">
          <div className="data-card"><small>一組通勤時間</small><div className="data-numbers"><span>8</span><span>10</span><span>12</span><span>12</span><span>15</span><span>18</span><span>20</span><span>22</span><span>25</span><span className="outlier">58</span></div></div>
          <div className="visual-arrow"><MoveRight /></div>
          <div className="insight-card"><BarChart3 /><div><small>先看分布，再選摘要</small><strong>右偏，有一個極端值</strong><p>中位數比平均數更能代表典型通勤時間。</p></div></div>
        </div>
      </section>
      <section className="trust-strip"><span><strong>12</strong> 完整章節</span><span><strong>22</strong> 教學圖表</span><span><strong>96</strong> 診斷練習</span><span><strong>0</strong> 需要連線</span></section>
      <section className="chapters-section" id="chapters">
        <div className="section-intro"><span className="section-kicker">12 CHAPTERS</span><h2>要救哪一章，直接點</h2></div>
        <div className="chapter-grid">
          {chapters.map((chapter) => (
            <button key={chapter.slug} onClick={() => openChapter(chapter.slug)} className="chapter-card desktop-chapter-card" style={{ "--chapter-accent": chapter.accent } as React.CSSProperties}>
              <div className="card-number">{String(chapter.number).padStart(2, "0")}</div>
              <span>{chapter.eyebrow}</span><h3>{chapter.title}</h3><p>{chapter.description}</p>
              <div className="card-footer"><small>{chapter.questions.length} 題練習 · {chapter.figureCount} 張圖</small><ArrowRight size={18} /></div>
            </button>
          ))}
        </div>
      </section>
      <section className="progress-home desktop-progress"><div><span className="section-kicker">YOUR PROGRESS</span><h2>進度只留在這台電腦</h2><p>不需要登入，也不會上傳作答紀錄。</p></div><ProgressTools /></section>
    </main>
  );
}

function DesktopChapter({ slug, openChapter, goHome }: { slug: string; openChapter: (slug: string) => void; goHome: () => void }) {
  const chapter = getChapter(slug)!;
  const previous = chapters[chapter.number - 2];
  const next = chapters[chapter.number];

  return (
    <main style={{ "--chapter-accent": chapter.accent } as React.CSSProperties}>
      <section className="chapter-hero">
        <div className="chapter-rail" aria-hidden="true"><span>{String(chapter.number).padStart(2, "0")}</span></div>
        <div className="chapter-hero-inner">
          <button onClick={goHome} className="back-link desktop-link-button"><ArrowLeft size={16} />回到 12 章課程</button>
          <span className="chapter-label">CHAPTER {String(chapter.number).padStart(2, "0")}</span>
          <h1>{chapter.title}</h1><p>{chapter.eyebrow}</p>
          <div className="chapter-facts"><span><Clock3 size={17} />約 45–70 分鐘</span><span><ListChecks size={17} />{chapter.questions.length} 個互動練習</span><span><ImageIcon size={17} />{chapter.figureCount} 張教學圖</span></div>
        </div>
      </section>
      <div className="chapter-layout">
        <aside className="chapter-sidebar"><p>本章段落</p><a href="#lesson">01　完整講義</a><a href="#interactive-lab">02　互動實驗</a><a href="#interactive-practice">03　診斷練習</a><ProgressTools compact /></aside>
        <div className="chapter-main">
          <section id="lesson"><MarkdownLesson content={chapter.content} /></section>
          <div id="interactive-lab"><StatLab chapterNumber={chapter.number} accent={chapter.accent} /></div>
          <PracticePanel questions={chapter.questions} chapterSlug={chapter.slug} />
        </div>
      </div>
      <nav className="chapter-next" aria-label="前後章節">
        {previous ? <button onClick={() => openChapter(previous.slug)}><ArrowLeft /><span><small>上一章</small>{previous.title}</span></button> : <span />}
        {next ? <button onClick={() => openChapter(next.slug)}><span><small>下一章</small>{next.title}</span><ArrowRight /></button> : <button onClick={goHome}><span><small>完成課程</small>回到首頁</span><ArrowRight /></button>}
      </nav>
    </main>
  );
}
