"""Plot the GMAT two-factor cell means as an interaction plot."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "13-gmat-interaction.png"

courses = ["三小時複習", "一天課程", "十週課程"]
backgrounds = {
    "Business": np.array([540, 500, 580]),
    "Engineering": np.array([500, 590, 590]),
    "Arts and Sciences": np.array([440, 450, 445]),
}
markers = ["o", "s", "^"]
linestyles = ["-", "--", ":"]
x = np.arange(len(courses))

fig, ax = plt.subplots(figsize=(10.6, 5.2))
for (label, means), color, marker, linestyle in zip(
    backgrounds.items(), CATEGORICAL, markers, linestyles
):
    ax.plot(
        x,
        means,
        label=label,
        color=color,
        marker=marker,
        linestyle=linestyle,
        linewidth=2.6,
        markersize=8,
        markeredgecolor=INK_PRIMARY,
    )
    for xi, mean in zip(x, means):
        ax.text(xi, mean + 6, f"{mean}", ha="center", color=color, fontsize=9, weight="bold")

ax.set_xticks(x, courses)
ax.set_xlabel("GMAT 準備課程(因子 A)")
ax.set_ylabel("GMAT 平均分數(分)")
ax.set_ylim(410, 625)
ax.set_title("GMAT 組合平均：先看線條是否平行", fontsize=15, weight="bold")
ax.legend(title="大學背景(因子 B)", loc="center left", bbox_to_anchor=(1.01, 0.5))
ax.grid(axis="x", visible=False)
fig.text(
    0.01,
    0.01,
    "觀察資料的組合平均；線條不完全平行只是視覺線索，本例交互作用檢定 p=0.350。",
    color=INK_MUTED,
    fontsize=9,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)
