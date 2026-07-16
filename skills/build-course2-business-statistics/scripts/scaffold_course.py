#!/usr/bin/env python3
"""Idempotently scaffold the course_2 (Quan1150 商業數量方法) study-note workspace."""

from __future__ import annotations

import argparse
from pathlib import Path


# (chapter-label, slug, title, source deck in course_2/ppt/ or None if not yet published)
NOTES = [
    ("7-10", "07-10-review-estimation-and-testing", "第 7-10 章複習：估計與檢定", "Quan1150_Week2.pdf"),
    ("12", "12-chi-square-tests", "第 12 章：卡方檢定", "Quan1150(Chi-Square).pdf"),
    ("13", "13-anova", "第 13 章：變異數分析", "Quan1150(ANOVA).pdf"),
    ("14", "14-simple-linear-regression", "第 14 章：簡單線性迴歸", "Quan1150(Simple Regression).pdf"),
    ("15", "15-multiple-regression", "第 15 章：複迴歸", "Quan1150(Multiple Regression).pdf"),
    ("16", "16-regression-model-building", "第 16 章：建立迴歸模型", "Quan1150(Model Construction).pdf"),
    ("17", "17-index-numbers", "第 17 章：指數", None),
    ("18", "18-time-series-and-forecasting", "第 18 章：時間序列分析與預測", None),
]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def note_template(chapter: str, slug: str, title: str, deck: str | None) -> str:
    deck_line = f"source_deck: {deck}" if deck else "source_deck: 尚未公布"
    waiting = (
        ""
        if deck
        else "\n> 老師尚未公布本章投影片；公布後才可開始 Phase 1（見 course_2/進度.md）。\n"
    )
    return f"""---
chapter: "{chapter}"
slug: {slug}
title: {title}
{deck_line}
---

# {title}

> 本檔為講義骨架；內容通過品質檢查前不得標記完成。Phase 進度只記錄在 course_2/進度.md，不寫在本檔（講義之後會合併列印）。
{waiting}
## 先備知識

<!-- Phase 3: course_1 對應章節的白話摘要與連結；無對應則說明本章自給自足。 -->

## 學習目標

<!-- Phase 1 -->

## 本章重點一覽

<!-- Phase 1 -->

## 內容講解

<!-- Phase 1: 依投影片順序分節，不漏掉任何教學內容。Phase 2 修錯；Phase 4 在對應段落旁插圖。 -->

## 跟前面像的東西怎麼分

<!-- Phase 5: 只放與更前面章節易混淆的比較；比較表 + 一句話判斷準則 + 錨點引用。 -->

## 考古題與詳解

<!-- Phase 6: 該章 quiz-set 考古題全收錄，逐步詳解並引用前面教學的錨點。 -->
"""


def scaffold(root: Path) -> list[Path]:
    created: list[Path] = []
    course = root / "course_2"
    for directory in (
        course / "chapters",
        course / "figures" / "scripts",
        course / "figures" / "generated",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    for chapter, slug, title, deck in NOTES:
        path = course / "chapters" / f"{slug}.md"
        if write_if_missing(path, note_template(chapter, slug, title, deck)):
            created.append(path)

    rows = "\n".join(
        "| {t} | {p1} | 未開始 | 未開始 | 未開始 | {p5} | {p6} |".format(
            t=title,
            p1="未開始（可開始）" if deck else "未開始（等投影片）",
            p5="不適用" if chapter == "7-10" else "未開始",
            p6="不適用" if chapter == "7-10" else "未開始",
        )
        for chapter, _, title, deck in NOTES
    )
    progress = f"""# course_2 商業統計講義進度

考試範圍 Ch12–18；第 7–10 章為複習（無考古題，Phase 5/6 不適用）。投影片還沒到手的章節不可開始 Phase 1（見下方素材公布紀錄）。

## 素材公布紀錄

拿到新素材（投影片、考古題）當天在此加一行，並同步更新下表對應格的狀態與 curriculum.md 的對應表。

| 日期 | 新到素材 | 解鎖的工作 |
|---|---|---|
| 2026-07-12 | 考古題 Ch12–18（quiz-set/） | Ch12–18 的 Phase 6、Phase 7 素材已備 |
| 2026-07-15 | 投影片：Ch7–10 複習、Ch12、Ch13、Ch14、Ch15、Ch16（ppt/） | 這六份講義可開始 Phase 1 |
| （待補） | 投影片：Ch17、Ch18 | 公布後其講義才可開始 Phase 1 |

## 講義進度

| 講義 | Phase 1 投影片講義化 | Phase 2 課本查核 | Phase 3 先備補強 | Phase 4 圖表 | Phase 5 跨章分辨 | Phase 6 考古題詳解 |
|---|---|---|---|---|---|---|
{rows}

## Phase 7 題型攻略（course_2/題型攻略.md）

- 狀態：未開始
- 解鎖條件：所有適用章節（Ch12–18）的 Phase 6 皆為「完成」。

## 驗收證據

<!-- 每次驗收後新增：日期、講義、Phase、審閱檔案（投影片頁碼/考古題題號）、執行的檢查、已知限制。 -->
"""
    for relative, content in (
        ("進度.md", progress),
        ("references.md", "# 參考資料\n\n- 老師投影片（course_2/ppt/，Anderson 14e Metric 版）\n- Anderson, Sweeney, Williams. *Statistics for Business and Economics*, 11th ed.（本地 PDF，查核用；節號與 14e 可能有差）\n- 考古題（course_2/quiz-set/）\n"),
    ):
        path = course / relative
        if write_if_missing(path, content):
            created.append(path)
    return created


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    created = scaffold(args.root.resolve())
    print(f"Created {len(created)} files; preserved all existing files.")


if __name__ == "__main__":
    main()
