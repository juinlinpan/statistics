"""Visualize between-treatment signal and within-treatment noise for Chemitech."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "13-chemitech-between-within.png"

groups = {
    "方法 A": np.array([58, 64, 55, 66, 67]),
    "方法 B": np.array([58, 69, 71, 64, 68]),
    "方法 C": np.array([48, 57, 59, 47, 49]),
}
group_means = np.array([values.mean() for values in groups.values()])
grand_mean = np.concatenate(list(groups.values())).mean()
mstr = 260.0
mse = 28.33

fig, (ax_data, ax_ratio) = plt.subplots(
    1,
    2,
    figsize=(11.2, 4.8),
    gridspec_kw={"width_ratios": [1.65, 1]},
)

offsets = np.linspace(-0.15, 0.15, 5)
for index, ((label, values), mean, color) in enumerate(
    zip(groups.items(), group_means, CATEGORICAL)
):
    x = np.full(values.size, index, dtype=float) + offsets
    ax_data.scatter(
        x,
        values,
        s=58,
        color=color,
        edgecolor=INK_PRIMARY,
        linewidth=0.7,
        zorder=3,
        label=f"{label}觀測值",
    )
    ax_data.hlines(mean, index - 0.28, index + 0.28, color=color, linewidth=4, zorder=4)
    ax_data.text(index, mean + 1.1, f"平均 {mean:.0f}", ha="center", color=color, weight="bold")

ax_data.axhline(grand_mean, color=INK_PRIMARY, linestyle="--", linewidth=1.6)
ax_data.text(2.34, grand_mean, "整體平均 60", va="center", ha="right", color=INK_PRIMARY)
ax_data.set_xticks(range(3), groups.keys())
ax_data.set_ylabel("每週組裝台數(台)")
ax_data.set_title("原始資料：組內散布與組平均差距")
ax_data.set_ylim(44, 74)
ax_data.grid(axis="x", visible=False)

bars = ax_ratio.bar(
    [0, 1],
    [mstr, mse],
    color=[ACCENT, CATEGORICAL[0]],
    edgecolor=INK_PRIMARY,
    linewidth=0.8,
    hatch=["//", ".."],
    width=0.62,
)
ax_ratio.set_xticks([0, 1], ["組間 MSTR", "組內 MSE"])
ax_ratio.set_ylabel("變異估計(台²)")
ax_ratio.set_title("F 是兩種變異估計的比值")
for bar, value in zip(bars, [mstr, mse]):
    ax_ratio.text(
        bar.get_x() + bar.get_width() / 2,
        value + 8,
        f"{value:.2f}" if value < 100 else f"{value:.0f}",
        ha="center",
        weight="bold",
    )
ax_ratio.annotate(
    "F = 260 / 28.33 = 9.18",
    xy=(0.5, 0.72),
    xycoords="axes fraction",
    ha="center",
    color=INK_PRIMARY,
    weight="bold",
    bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": INK_MUTED},
)
ax_ratio.set_ylim(0, 310)
ax_ratio.grid(axis="x", visible=False)

fig.suptitle("Chemitech：組間訊號遠大於組內雜訊", fontsize=15, weight="bold")
fig.text(0.01, 0.01, "觀察資料；每點是一位工人一週的產量。", color=INK_MUTED, fontsize=9)
fig.tight_layout(rect=(0, 0.04, 1, 0.94))
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)

