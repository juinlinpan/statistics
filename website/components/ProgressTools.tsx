"use client";

import { Download, RotateCcw } from "lucide-react";
import { useEffect, useState } from "react";

const prefix = "stats-course:";

export function ProgressTools({ compact = false }: { compact?: boolean }) {
  const [count, setCount] = useState(0);

  const refresh = () => {
    const keys = Object.keys(localStorage).filter((key) => key.startsWith(prefix) && localStorage.getItem(key) === "done");
    setCount(keys.length);
  };

  useEffect(refresh, []);

  const reset = () => {
    if (!confirm("確定要清除這台裝置上的全部作答進度嗎？")) return;
    Object.keys(localStorage).filter((key) => key.startsWith(prefix)).forEach((key) => localStorage.removeItem(key));
    refresh();
    window.dispatchEvent(new Event("stats-progress"));
  };

  const exportProgress = () => {
    const data = Object.fromEntries(Object.keys(localStorage).filter((key) => key.startsWith(prefix)).map((key) => [key, localStorage.getItem(key)]));
    const blob = new Blob([JSON.stringify({ exportedAt: new Date().toISOString(), progress: data }, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "statistics-learning-progress.json";
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className={compact ? "progress-tools compact" : "progress-tools"}>
      {!compact && <p><strong>{count}</strong> 個練習已完成</p>}
      <button onClick={exportProgress}><Download size={16} />匯出進度</button>
      <button onClick={reset}><RotateCcw size={16} />重設</button>
    </div>
  );
}
