"""Generate the learner-facing figures for Chapter 18."""

from __future__ import annotations

from math import comb
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import ACCENT, CATEGORICAL, GRIDLINE, INK_MUTED, INK_PRIMARY, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated"


def save(fig: plt.Figure, name: str) -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT / name, dpi=200, bbox_inches="tight")
    plt.close(fig)


def sign_test_information() -> None:
    """Show both the information discarded by signs and the exact tail calculation."""
    apply_style()
    values = np.array([380, 415, 426, 474, 485, 515, 562, 662, 721, 860])
    median0 = 450
    signs = np.where(values > median0, "+", "-")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    y = np.zeros_like(values, dtype=float)
    colors = [CATEGORICAL[0] if sign == "-" else CATEGORICAL[1] for sign in signs]
    markers = ["v" if sign == "-" else "^" for sign in signs]
    for value, marker, color, sign in zip(values, markers, colors, signs):
        ax.scatter(value, 0, marker=marker, s=90, color=color, zorder=3)
        ax.text(value, 0.08, sign, ha="center", va="bottom", color=color, weight="bold")
    ax.axvline(median0, color=ACCENT, linestyle="--", label="假設中位數 = 450")
    ax.set_ylim(-0.2, 0.32)
    ax.set_yticks([])
    ax.set_xlabel("每週銷售額 (美元)")
    ax.set_title("符號檢定只保留方向")
    ax.text(0.5, -0.22, "離 450 多遠會被丟掉；只留下 7 個 +、3 個 -",
            transform=ax.transAxes, ha="center", color=INK_MUTED)
    ax.legend(loc="upper left")

    ax = axes[1]
    x = np.arange(11)
    probs = np.array([comb(10, i) / 2**10 for i in x])
    bars = ax.bar(x, probs, color=GRIDLINE, edgecolor=INK_PRIMARY, linewidth=0.6)
    for i in [7, 8, 9, 10]:
        bars[i].set_color(CATEGORICAL[1])
        bars[10 - i].set_color(CATEGORICAL[0])
    ax.axvline(7, color=CATEGORICAL[1], linestyle="--", linewidth=1.3)
    ax.set_xlabel("正號數 $X$")
    ax.set_ylabel("$P(X=x)$")
    ax.set_title("$H_0:p=0.5$ 下的精確二項分布")
    ax.text(0.5, 0.93, "$p=2P(X\\geq7)=0.3438$", transform=ax.transAxes,
            ha="center", va="top", color=INK_PRIMARY)
    fig.suptitle("符號檢定：用資訊換取較少的分布假設", fontsize=15, weight="bold")
    fig.tight_layout()
    save(fig, "ch18_sign_test_information.png")


def rank_test_structures() -> None:
    """Contrast the data structures of the three rank-based tests."""
    apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.8))

    before = np.array([10.2, 9.6, 9.2, 10.6, 9.9, 10.2, 10.6, 11.2])
    after = np.array([9.5, 9.8, 8.8, 10.1, 10.3, 9.3, 10.5, 10.6])
    ax = axes[0]
    for i, (a, b) in enumerate(zip(before, after)):
        ax.plot([0, 1], [a, b], color=INK_MUTED, alpha=0.6,
                marker="o" if i % 2 == 0 else "s", markersize=5)
    ax.set_xticks([0, 1], ["方法 A", "方法 B"])
    ax.set_ylabel("同一位工人的完成時間 (分鐘)")
    ax.set_title("Wilcoxon signed-rank\n同一單位的成對差")
    ax.text(0.5, -0.2, "先取差，再排 $|d_i|$ 的名次", transform=ax.transAxes,
            ha="center", color=INK_MUTED)

    group1 = np.array([805, 875, 925, 945, 950, 955, 975, 1025, 1055, 1095, 1195, 1200])
    group2 = np.array([750, 800, 850, 865, 885, 915, 935, 950, 1000, 1050])
    ax = axes[1]
    ax.scatter(group1, np.ones_like(group1), marker="o", color=CATEGORICAL[0], label="分行 1")
    ax.scatter(group2, np.zeros_like(group2), marker="x", color=CATEGORICAL[1], s=55, label="分行 2")
    ax.set_yticks([0, 1], ["分行 2", "分行 1"])
    ax.set_xlabel("帳戶餘額")
    ax.set_title("Mann-Whitney-Wilcoxon\n兩個獨立樣本混合排名")
    ax.text(0.5, -0.2, "兩群名次越混合，分布越相似", transform=ax.transAxes,
            ha="center", color=INK_MUTED)

    groups = [[25, 60, 70, 80, 85, 90, 95], [15, 20, 30, 35, 40, 60],
              [50, 60, 70, 70, 75, 80, 90]]
    ax = axes[2]
    for j, group in enumerate(groups):
        jitter = np.linspace(-0.08, 0.08, len(group))
        ax.scatter(np.full(len(group), j) + jitter, group,
                   marker=["o", "s", "^"][j], color=CATEGORICAL[j], s=45)
        ax.hlines(np.median(group), j - 0.25, j + 0.25, color=INK_PRIMARY, linewidth=2)
    ax.set_xticks(range(3), ["A", "B", "C"])
    ax.set_ylabel("績效評分")
    ax.set_title("Kruskal-Wallis\n三個以上獨立樣本")
    ax.text(0.5, -0.2, "比較各群得到高名次的傾向", transform=ax.transAxes,
            ha="center", color=INK_MUTED)

    fig.suptitle("先看資料結構，再決定要排哪一種名次", fontsize=15, weight="bold")
    fig.tight_layout()
    save(fig, "ch18_rank_test_structures.png")


def spearman_monotonic() -> None:
    """Show why Spearman targets monotonic order rather than only straight lines."""
    apply_style()
    rng = np.random.default_rng(1805)
    x = np.linspace(1, 10, 22)
    y = np.exp(x / 3.7) + rng.normal(0, 0.45, len(x))
    pearson = stats.pearsonr(x, y).statistic
    rho = stats.spearmanr(x, y).statistic

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.7))
    ax = axes[0]
    ax.scatter(x, y, marker="o", color=CATEGORICAL[0])
    ax.set_xlabel("投入量 $x$")
    ax.set_ylabel("反應 $y$")
    ax.set_title("原始尺度：明顯單調，但不是直線")
    ax.text(0.04, 0.93, f"Pearson $r={pearson:.2f}$", transform=ax.transAxes,
            va="top", color=INK_PRIMARY)

    ax = axes[1]
    rank_x = stats.rankdata(x)
    rank_y = stats.rankdata(y)
    ax.scatter(rank_x, rank_y, marker="s", color=CATEGORICAL[1])
    ax.plot([1, len(x)], [1, len(x)], linestyle="--", color=INK_MUTED,
            label="兩套名次完全一致")
    ax.set_xlabel("$x$ 的名次")
    ax.set_ylabel("$y$ 的名次")
    ax.set_title("名次尺度：只問排序是否一致")
    ax.text(0.04, 0.93, f"Spearman $r_s={rho:.2f}$", transform=ax.transAxes,
            va="top", color=INK_PRIMARY)
    ax.legend(loc="lower right")
    fig.suptitle("Spearman 相關捕捉單調關係，不要求原始關係是直線", fontsize=15, weight="bold")
    fig.tight_layout()
    save(fig, "ch18_spearman_monotonic.png")


def main() -> None:
    sign_test_information()
    rank_test_structures()
    spearman_monotonic()
    for path in sorted(OUTPUT.glob("ch18_*.png")):
        print(path)


if __name__ == "__main__":
    main()
