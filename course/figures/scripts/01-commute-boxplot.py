# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Box plot of the chapter's running commute-time example (n=10).

Data: 8, 10, 12, 12, 15, 18, 20, 22, 25, 58 minutes.
Five-number summary per the chapter's convention: (8, 12, 16.5, 22, 58).
IQR = 22 - 12 = 10; 1.5*IQR fences = (-3, 37), so 58 is flagged as a
potential outlier and drawn as an individual point beyond the upper whisker.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

commute = np.array([8, 10, 12, 12, 15, 18, 20, 22, 25, 58])

fig, ax = plt.subplots(figsize=(7, 3.6))

bp = ax.boxplot(
    commute,
    vert=False,
    widths=0.5,
    patch_artist=True,
    whis=1.5,
    flierprops=dict(
        marker="o",
        markerfacecolor=ACCENT,
        markeredgecolor=ACCENT,
        markersize=7,
        zorder=5,
    ),
    medianprops=dict(color=INK_SECONDARY, linewidth=2.0),
    boxprops=dict(facecolor=CATEGORICAL[0], edgecolor=CATEGORICAL[0], alpha=0.35),
    whiskerprops=dict(color=CATEGORICAL[0]),
    capprops=dict(color=CATEGORICAL[0]),
)

ax.set_yticks([])
ax.set_xlabel("單程通勤時間（分鐘）")
ax.set_title("10 位學生通勤時間盒鬚圖：58 分鐘超出上界，標記為潛在離群值")

ax.annotate(
    "潛在離群值\n58 分鐘",
    xy=(58, 1),
    xytext=(50, 1.32),
    ha="center",
    fontsize=9.5,
    color=ACCENT,
    arrowprops=dict(arrowstyle="-", color=ACCENT, linewidth=1.0),
)

ax.set_xlim(0, 62)
ax.set_xticks(range(0, 62, 10))

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "01-commute-boxplot.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
