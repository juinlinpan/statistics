"""Show within-controller comparisons in the randomized block example."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "13-air-traffic-blocks.png"

systems = ["系統 A", "系統 B", "系統 C"]
scores = np.array(
    [
        [15, 15, 18],
        [14, 14, 14],
        [10, 11, 15],
        [13, 12, 17],
        [16, 13, 16],
        [13, 13, 13],
    ]
)
means = scores.mean(axis=0)
x = np.arange(3)

fig, ax = plt.subplots(figsize=(9.4, 5.2))
for row in scores:
    ax.plot(
        x,
        row,
        color=INK_MUTED,
        alpha=0.65,
        linewidth=1.4,
        marker="o",
        markersize=5,
    )

ax.plot(
    x,
    means,
    color=CATEGORICAL[0],
    linewidth=3.3,
    linestyle="--",
    marker="s",
    markersize=9,
    markeredgecolor=INK_PRIMARY,
    label="處理平均",
    zorder=5,
)
label_positions = [(0.06, "left"), (1.0, "center"), (1.94, "right")]
for (xi, horizontal_alignment), mean in zip(label_positions, means):
    ax.text(xi, mean - 0.55, f"平均 {mean:.1f}", ha=horizontal_alignment, color=CATEGORICAL[0], weight="bold")

ax.annotate(
    "每條灰線＝同一位管制員",
    xy=(1.0, scores[2, 1]),
    xytext=(0.25, 9.2),
    arrowprops={"arrowstyle": "->", "color": ACCENT},
    color=ACCENT,
    weight="bold",
)
ax.set_xticks(x, systems)
ax.set_ylabel("壓力分數(分)")
ax.set_ylim(8.5, 19)
ax.set_title("隨機集區：先在同一位管制員內比較", fontsize=15, weight="bold")
ax.legend(loc="upper left")
ax.grid(axis="x", visible=False)
fig.text(
    0.01,
    0.01,
    "觀察資料；六條灰線各代表一位管制員，連線保留同一集區的配對關係。",
    color=INK_MUTED,
    fontsize=9,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)
