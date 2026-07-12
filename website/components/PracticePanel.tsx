"use client";

import { Check, ChevronLeft, ChevronRight, Lightbulb, RotateCcw } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import type { Question } from "@/lib/course-data";

function QuestionCard({ question, chapterSlug, onDone }: { question: Question; chapterSlug: string; onDone: () => void }) {
  const [selected, setSelected] = useState<string>();
  const [submitted, setSubmitted] = useState(false);
  const [step, setStep] = useState(0);
  const storageKey = `stats-course:${chapterSlug}:${question.id}`;
  const isCalculation = question.type === "calculation";
  const selectedOption = question.options?.find((option) => option.id === selected);

  useEffect(() => {
    const done = localStorage.getItem(storageKey) === "done";
    if (done) {
      setSubmitted(true);
      setStep(question.steps?.length ?? 0);
    }
  }, [storageKey, question.steps?.length]);

  const markDone = () => {
    localStorage.setItem(storageKey, "done");
    window.dispatchEvent(new Event("stats-progress"));
    onDone();
  };

  const submit = () => {
    if (!selected) return;
    setSubmitted(true);
    if (selectedOption?.correct) markDone();
  };

  const revealNext = () => {
    const next = Math.min(step + 1, question.steps?.length ?? 0);
    setStep(next);
    if (next === question.steps?.length) markDone();
  };

  const retry = () => {
    setSelected(undefined);
    setSubmitted(false);
  };

  return (
    <div className="question-card">
      <div className="question-meta"><span>{isCalculation ? "計算與推理" : "觀念判斷"}</span><span>{question.difficulty === "foundational" ? "基礎" : "進階"}</span></div>
      <h3>{question.prompt}</h3>
      {!isCalculation && (
        <div className="option-list" role="radiogroup" aria-label="作答選項">
          {question.options?.map((option) => {
            const chosen = selected === option.id;
            const state = submitted && chosen ? (option.correct ? "correct" : "incorrect") : "";
            return (
              <button key={option.id} role="radio" aria-checked={chosen} className={`option ${chosen ? "selected" : ""} ${state}`} onClick={() => !submitted && setSelected(option.id)}>
                <span>{option.id.toUpperCase()}</span>{option.text}{submitted && chosen && option.correct && <Check size={18} />}
              </button>
            );
          })}
        </div>
      )}
      {!isCalculation && !submitted && <button className="primary-button" disabled={!selected} onClick={submit}>送出答案</button>}
      {!isCalculation && submitted && selectedOption && (
        <div className={`feedback ${selectedOption.correct ? "success" : "try-again"}`}>
          <Lightbulb size={20} />
          <div><strong>{selectedOption.correct ? "答對了，你抓到判斷關鍵。" : "再想一下這個判斷點。"}</strong><p>{selectedOption.feedback}</p></div>
          {!selectedOption.correct && <button onClick={retry}><RotateCcw size={15} />再試一次</button>}
        </div>
      )}
      {isCalculation && (
        <div className="step-solution">
          <p className="think-first">先在紙上試算，再一次揭開一個步驟。</p>
          {question.steps?.slice(0, step).map((item, index) => (
            <div className="solution-step" key={`${item.title}-${index}`}>
              <span>{index + 1}</span><div><strong>{item.title}</strong><p>{item.explanation}</p>{item.formula_ref && <a href={`#${item.formula_ref}`}>回到使用的公式</a>}</div>
            </div>
          ))}
          {step < (question.steps?.length ?? 0) ? <button className="primary-button" onClick={revealNext}>{step === 0 ? "開始逐步解題" : "揭開下一步"}</button> : <div className="final-answer"><Check size={18} /><strong>答案：</strong>{question.answer}</div>}
        </div>
      )}
    </div>
  );
}

export function PracticePanel({ questions, chapterSlug }: { questions: Question[]; chapterSlug: string }) {
  const [index, setIndex] = useState(0);
  const [version, setVersion] = useState(0);
  const doneCount = useMemo(() => {
    if (typeof window === "undefined") return 0;
    return questions.filter((question) => localStorage.getItem(`stats-course:${chapterSlug}:${question.id}`) === "done").length;
  }, [questions, chapterSlug, version]);

  return (
    <section className="practice-section" id="interactive-practice">
      <div className="section-heading-row">
        <div><span className="section-kicker">診斷練習</span><h2>診斷練習</h2><p>題目來自原講義題庫。答錯時，回饋會指出那個選項背後的迷思。</p></div>
        <div className="practice-progress" aria-label={`已完成 ${doneCount} / ${questions.length} 題`}><strong>{doneCount}</strong><span>/ {questions.length} 題</span></div>
      </div>
      <QuestionCard key={questions[index].id} question={questions[index]} chapterSlug={chapterSlug} onDone={() => setVersion((value) => value + 1)} />
      <div className="question-pager">
        <button onClick={() => setIndex((value) => Math.max(0, value - 1))} disabled={index === 0}><ChevronLeft size={17} />上一題</button>
        <span>{index + 1} / {questions.length}</span>
        <button onClick={() => setIndex((value) => Math.min(questions.length - 1, value + 1))} disabled={index === questions.length - 1}>下一題<ChevronRight size={17} /></button>
      </div>
    </section>
  );
}
