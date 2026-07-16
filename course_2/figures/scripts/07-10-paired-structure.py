"""Show why the Express Deliveries observations must stay paired."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_MUTED, INK_PRIMARY, INK_SECONDARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "07-10-paired-structure.png"
OFFICES = [
    "Seattle", "Los Angeles", "Boston", "Cleveland", "New York",
    "Houston", "Atlanta", "St. Louis", "Milwaukee", "Denver",
]
UPX = np.array([32, 30, 19, 16, 15, 18, 14, 10, 7, 16])
INTEX = np.array([25, 24, 15, 15, 13, 15, 15, 8, 9, 11])
DIFF = UPX - INTEX

fig, axes = plt.subplots(1, 2, figsize=(12, 5.4), gridspec_kw={"width_ratios": [0.9, 1.4]})

# Left: each office connects its two measurements.
ax = axes[0]
for upx, intex in zip(UPX, INTEX):
    ax.plot([0, 1], [upx, intex], color=INK_MUTED, alpha=0.70, linewidth=1.5)
ax.scatter(np.zeros_like(UPX), UPX, color=CATEGORICAL[0], marker="o", s=42, label="UPX")
ax.scatter(np.ones_like(INTEX), INTEX, facecolor="none", edgecolor=CATEGORICAL[1], marker="s", s=48, linewidth=1.8, label="INTEX")
ax.set_xticks([0, 1], ["UPX", "INTEX"])
ax.set_xlim(-0.35, 1.35)
ax.set_ylabel("配送時間 (小時)")
ax.set_title("同一辦公室的兩筆資料要連在一起")
ax.legend(loc="lower left")

# Right: after pairing, the analysis uses one difference per office.
ax = axes[1]
y = np.arange(len(OFFICES))
colors = [ACCENT if value < 0 else CATEGORICAL[0] for value in DIFF]
ax.hlines(y, 0, DIFF, color=colors, linewidth=2)
ax.scatter(DIFF, y, color=colors, marker="D", s=42)
ax.axvline(0, color=INK_PRIMARY, linestyle="--", linewidth=1.4)
ax.axvline(DIFF.mean(), color=CATEGORICAL[1], linestyle="-.", linewidth=2.1)
ax.set_yticks(y, OFFICES)
ax.invert_yaxis()
ax.set_ylim(9.85, -0.45)
ax.set_xlabel("差值 d = UPX − INTEX (小時)")
ax.set_title("先算每一對的差，再分析 10 個差值")
ax.text(
    0,
    9.55,
    "d = 0：沒有差異",
    ha="center",
    va="center",
    color=INK_SECONDARY,
)
ax.text(
    DIFF.mean(),
    9.55,
    "平均差 = 2.7",
    ha="center",
    va="center",
    color=INK_SECONDARY,
)

fig.suptitle("配對設計保留辦公室之間的一一對應", fontsize=15, fontweight="bold")
fig.text(0.5, 0.01, "Express Deliveries 觀察資料；n 是 10 對，不是 20 筆獨立資料", ha="center", color=INK_SECONDARY)
fig.tight_layout(rect=(0, 0.05, 1, 0.92))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)
