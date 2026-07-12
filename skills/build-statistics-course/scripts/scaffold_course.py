#!/usr/bin/env python3
"""Idempotently scaffold the statistics course workspace."""

from __future__ import annotations

import argparse
from pathlib import Path


CHAPTERS = [
    (1, "descriptive-statistics", "描述統計與資料探索"),
    (2, "sampling-and-experiments", "抽樣與實驗設計"),
    (3, "probability", "機率"),
    (4, "normal-and-binomial", "常態近似與二項分配"),
    (5, "sampling-distributions-clt", "抽樣分配與中央極限定理"),
    (6, "regression", "迴歸"),
    (7, "confidence-intervals", "信賴區間"),
    (8, "significance-tests", "顯著性檢定"),
    (9, "resampling", "重抽樣"),
    (10, "categorical-data", "類別資料分析"),
    (11, "one-way-anova", "單因子變異數分析"),
    (12, "multiple-comparisons", "多重比較"),
]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def chapter_template(number: int, slug: str, title: str) -> str:
    return f"""---
chapter: {number}
slug: {slug}
title: {title}
phase1: 未開始
phase2: 未開始
phase3: 未開始
phase4: 未開始
---

# 第 {number} 章：{title}

> 本檔為章節骨架；內容通過品質檢查前不得標記完成。

## 為什麼要學這一章

<!-- Phase 1 content -->

## 必備觀念與公式

<!-- Phase 1 content -->

## 練習與逐步詳解

<!-- Phase 2 content: append practice to this same chapter note; do not create a second note. -->

## 跨章比較與選法

<!-- Phase 3 content: append cross-chapter guidance to this same chapter note; do not create a second note. -->

## 圖表補充

<!-- Phase 4 content: insert figures next to the explanations/examples they support; do not batch into a separate gallery. -->
"""


def scaffold(root: Path) -> list[Path]:
    created: list[Path] = []
    course = root / "course"
    for directory in (
        course / "chapters",
        course / "questions",
        course / "figures" / "scripts",
        course / "figures" / "generated",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    for number, slug, title in CHAPTERS:
        path = course / "chapters" / f"{number:02d}-{slug}.md"
        if write_if_missing(path, chapter_template(number, slug, title)):
            created.append(path)

    rows = "\n".join(
        f"| {n:02d} | {title} | 未開始 | 未開始 | 未開始 | 未開始 |"
        for n, _, title in CHAPTERS
    )
    progress = f"""# 統計講義工程進度

## 章節進度

| 章節 | 名稱 | Phase 1 講義 | Phase 2 類題與詳解 | Phase 3 跨章串聯 | Phase 4 圖表補充 |
|---:|---|---|---|---|---|
{rows}

## Phase 5 互動網站

- 狀態：鎖定
- 解鎖條件：上表 12 章的 Phase 1、Phase 2、Phase 3、Phase 4 共 48 格全部為「完成」。
- 執行原則：解鎖後才可開始，並以全課程為單位統一開發。

## 驗收證據

<!-- 每次完成驗收後新增日期、章節、Phase、檢查內容、檔案與已知限制。 -->
"""
    for relative, content in (
        ("進度.md", progress),
        ("concept-map.md", "# 統計觀念地圖\n\n<!-- Phase 3 -->\n"),
        ("method-selector.md", "# 統計方法選擇器\n\n<!-- Phase 3 -->\n"),
        ("references.md", "# 參考資料\n"),
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
