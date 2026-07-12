# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 11, Section 4 worked example: three-group dot plot with means.

Data (minutes):
  A: 4, 5, 6   (n=3, mean=5)
  B: 6, 7, 8   (n=3, mean=7)
  C: 8, 9, 10  (n=3, mean=9)
Grand mean = 7. SS_B = 24, SS_W = 6, F = 12 (matches the chapter's exact
worked example in Section 4, "一個小型計算例").

Each group's raw observations are plotted as dots; a larger diamond marks
each group mean. A solid horizontal reference line marks the grand mean, so
readers can see "how far each group mean sits from the grand mean" (signal,
SS_B) against "how spread out each group's own points are" (noise, SS_W).
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, INK_MUTED, INK_SECONDARY

apply_style()

groups = ["A", "B", "C"]
data = {
    "A": np.array([4, 5, 6]),
    "B": np.array([6, 7, 8]),
    "C": np.array([8, 9, 10]),
}
means = {g: data[g].mean() for g in groups}
grand_mean = np.concatenate(list(data.values())).mean()  # 7

fig, ax = plt.subplots(figsize=(7, 4.6))

x_positions = {"A": 1, "B": 2, "C": 3}
colors = {"A": CATEGORICAL[0], "B": CATEGORICAL[1], "C": CATEGORICAL[2]}

for g in groups:
    x = x_positions[g]
    y = data[g]
    ax.scatter(
        np.full_like(y, x, dtype=float),
        y,
        color=colors[g],
        s=90,
        zorder=3,
        label=f"{g} 組觀測值（$\\bar{{x}}_{{{g}}}={means[g]:.0f}$）",
    )
    ax.scatter(
        [x],
        [means[g]],
        marker="D",
        s=110,
        facecolor="none",
        edgecolor=colors[g],
        linewidth=2.0,
        zorder=4,
    )

ax.axhline(grand_mean, color=INK_MUTED, linewidth=1.4, zorder=2)
ax.text(
    3.35,
    grand_mean,
    f"總平均 $\\bar{{x}}_{{..}}={grand_mean:.0f}$",
    ha="left",
    va="center",
    color=INK_SECONDARY,
    fontsize=10,
)

ax.set_xlim(0.5, 4.3)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["A 組", "B 組", "C 組"])
ax.set_ylim(2.5, 11.5)
ax.set_yticks(range(3, 12))
ax.set_xlabel("組別")
ax.set_ylabel("觀測值（分鐘）")
ax.set_title("三組觀測值與組平均：組間分離（$SS_B=24$）vs. 組內分散（$SS_W=6$）")
ax.legend(loc="upper left", fontsize=9)

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; grand mean = {grand_mean}")
