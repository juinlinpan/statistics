# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Histogram of the chapter's running commute-time example (n=10).

Data: 8, 10, 12, 12, 15, 18, 20, 22, 25, 58 minutes.
Illustrates the right-skewed shape caused by the 58-minute outlier, with
mean (20) and median (16.5) marked to show mean > median under right skew.
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
mean = commute.mean()
median = np.median(commute)

bins = [0, 10, 20, 30, 40, 50, 60]

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.hist(
    commute,
    bins=bins,
    color=CATEGORICAL[0],
    edgecolor="white",
    linewidth=1.2,
)

ax.axvline(mean, color=ACCENT, linewidth=2.0, linestyle="-", zorder=5)
ax.axvline(median, color=INK_SECONDARY, linewidth=2.0, linestyle="--", zorder=5)

ax.text(mean + 1, ax.get_ylim()[1] * 0.92, f"平均數 = {mean:.0f}", color=ACCENT, fontsize=10, va="top")
ax.text(median - 1, ax.get_ylim()[1] * 0.78, f"中位數 = {median:.1f}", color=INK_SECONDARY, fontsize=10, va="top", ha="right")

ax.set_xlabel("單程通勤時間（分鐘）")
ax.set_ylabel("學生人數（個）")
ax.set_title("10 位學生通勤時間直方圖：右側長尾拉高平均數")
ax.set_xticks(bins)

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "01-commute-histogram.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
