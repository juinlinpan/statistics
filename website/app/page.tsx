import Link from "next/link";
import { ArrowRight, BarChart3, MoveRight, Sparkles } from "lucide-react";
import { CourseHeader } from "@/components/CourseHeader";
import { ProgressTools } from "@/components/ProgressTools";
import { chapters } from "@/lib/course-data";

export default function Home() {
  return (
    <>
      <CourseHeader />
      <main>
        <section className="home-hero">
          <div className="hero-orbit orbit-one" /><div className="hero-orbit orbit-two" />
          <div className="hero-copy">
            <span className="hero-kicker"><Sparkles size={15} />統計新手求生講義</span>
            <h1>救救我的<br /><span>統計 R</span></h1>
            <p>公式看不懂、檢定一直選錯、p 值到底在說什麼？從第 1 章開始，一次救一個觀念。12 章完整講義、22 張教學圖、96 道診斷練習。</p>
            <div className="hero-actions"><Link className="hero-primary" href={`/chapter/${chapters[0].slug}`}>從第 1 章開始<ArrowRight size={18} /></Link></div>
          </div>
          <div className="hero-visual" aria-label="從原始資料走到清楚判斷的學習示意">
            <div className="data-card"><small>一組通勤時間</small><div className="data-numbers"><span>8</span><span>10</span><span>12</span><span>12</span><span>15</span><span>18</span><span>20</span><span>22</span><span>25</span><span className="outlier">58</span></div></div>
            <div className="visual-arrow"><MoveRight /></div>
            <div className="insight-card"><BarChart3 /><div><small>先看分布，再選摘要</small><strong>右偏，有一個極端值</strong><p>中位數比平均數更能代表典型通勤時間。</p></div></div>
            <div className="floating-note note-one">不是背答案<br /><strong>是學會判斷</strong></div>
            <div className="floating-note note-two">58 把平均數<br />往右拉了！</div>
          </div>
        </section>

        <section className="trust-strip"><span><strong>12</strong> 完整章節</span><span><strong>22</strong> 教學圖表</span><span><strong>96</strong> 診斷練習</span><span><strong>0</strong> 蒐集個資</span></section>

        <section className="chapters-section" id="chapters">
          <div className="section-intro"><span className="section-kicker">YOUR LEARNING PATH</span><h2>12 章，把統計的骨架一節節搭起來</h2><p>前面建立資料與機率直覺，中段理解抽樣與推論，最後處理多組資料與多重檢定。</p></div>
          <div className="chapter-grid">
            {chapters.map((chapter) => (
              <Link key={chapter.slug} href={`/chapter/${chapter.slug}`} className="chapter-card" style={{ "--chapter-accent": chapter.accent } as React.CSSProperties}>
                <div className="card-number">{String(chapter.number).padStart(2, "0")}</div>
                <span>{chapter.eyebrow}</span><h3>{chapter.title}</h3><p>{chapter.description}</p>
                <div className="card-footer"><small>{chapter.questions.length} 題練習 · {chapter.figureCount} 張圖</small><ArrowRight size={18} /></div>
              </Link>
            ))}
          </div>
        </section>

        <section className="progress-home"><div><span className="section-kicker">YOUR PROGRESS</span><h2>進度只留在你的裝置上</h2><p>網站不蒐集姓名或作答紀錄。你可以隨時匯出或清除本機進度。</p></div><ProgressTools /></section>
      </main>
      <footer><p>救救我的統計 R</p><span>一次救一個統計觀念。</span></footer>
    </>
  );
}
