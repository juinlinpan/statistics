"""Create representative time-series pattern panels for Chapter 17."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import ACCENT, CATEGORICAL, INK_MUTED, apply_style  # noqa: E402


apply_style()
rng = np.random.default_rng(1701)
t = np.arange(1, 25)
noise = rng.normal(0, 0.55, size=t.size)

series = [
    ("水平型", 20 + noise, "固定水準附近隨機起伏"),
    ("趨勢型", 12 + 0.55 * t + noise, "長期水準逐步上升"),
    ("季節型", 20 + 2.6 * np.sin(2 * np.pi * (t - 1) / 4) + 0.45 * noise,
     "每四期重複一次"),
    ("趨勢＋季節", 12 + 0.42 * t + 2.2 * np.sin(2 * np.pi * (t - 1) / 4)
     + 0.45 * noise, "上升基準上仍有固定節奏"),
]

fig, axes = plt.subplots(2, 2, figsize=(10.4, 6.5), sharex=True)
for ax, (title, y, subtitle), color in zip(axes.flat, series, CATEGORICAL[:4]):
    ax.plot(t, y, marker="o", markersize=3.6, color=color)
    ax.set_title(title, loc="left", fontweight="bold")
    ax.text(0.01, 0.94, subtitle, transform=ax.transAxes, color=INK_MUTED,
            ha="left", va="top", fontsize=9)
    ax.set_ylabel("觀察值")
    ax.set_xticks([1, 4, 8, 12, 16, 20, 24])
    ax.axhline(np.mean(y), color=ACCENT, linewidth=1, linestyle="--", alpha=0.45)

for ax in axes[-1]:
    ax.set_xlabel("時間期數")

fig.suptitle("先看資料長相，再選預測方法", fontsize=16, fontweight="bold")
fig.tight_layout()
out = Path(__file__).resolve().parents[1] / "generated" / "ch17_time_series_patterns.png"
fig.savefig(out)
plt.close(fig)
print(out)
