"""Compare the mean-response confidence band with the individual prediction band."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import CATEGORICAL, INK_PRIMARY, INK_SECONDARY, SURFACE, apply_style


apply_style()

x = np.array([2, 6, 8, 8, 12, 16, 20, 20, 22, 26], dtype=float)
y = np.array([58, 105, 88, 118, 117, 137, 157, 169, 149, 202], dtype=float)
n = 10
x_bar = 14
sxx = 568
s = 13.829
t_critical = 2.306

x_grid = np.linspace(2, 26, 400)
y_grid = 60 + 5 * x_grid
mean_se = s * np.sqrt(1 / n + (x_grid - x_bar) ** 2 / sxx)
prediction_se = s * np.sqrt(1 + 1 / n + (x_grid - x_bar) ** 2 / sxx)

mean_low = y_grid - t_critical * mean_se
mean_high = y_grid + t_critical * mean_se
prediction_low = y_grid - t_critical * prediction_se
prediction_high = y_grid + t_critical * prediction_se

assert np.isclose(60 + 5 * 10, 110)
assert round(s * np.sqrt(1 / n + (10 - x_bar) ** 2 / sxx), 2) == 4.95
assert round(s * np.sqrt(1 + 1 / n + (10 - x_bar) ** 2 / sxx), 2) == 14.69

fig, ax = plt.subplots(figsize=(8.4, 5.4))

ax.fill_between(
    x_grid,
    prediction_low,
    prediction_high,
    color=CATEGORICAL[0],
    alpha=0.13,
    hatch="//",
    edgecolor=CATEGORICAL[0],
    linewidth=0,
    label="95% 個別預測區間（外層）",
)
ax.plot(x_grid, prediction_low, color=CATEGORICAL[0], linestyle="--", linewidth=1.3)
ax.plot(x_grid, prediction_high, color=CATEGORICAL[0], linestyle="--", linewidth=1.3)
ax.fill_between(
    x_grid,
    mean_low,
    mean_high,
    color=CATEGORICAL[1],
    alpha=0.28,
    label="95% 平均反應信賴區間（內層）",
)
ax.plot(x_grid, mean_low, color=CATEGORICAL[1], linestyle=":", linewidth=1.5)
ax.plot(x_grid, mean_high, color=CATEGORICAL[1], linestyle=":", linewidth=1.5)
ax.plot(x_grid, y_grid, color=INK_PRIMARY, label="估計線  ŷ = 60 + 5x")
ax.scatter(
    x,
    y,
    s=42,
    facecolor=SURFACE,
    edgecolor=INK_SECONDARY,
    linewidth=1.3,
    zorder=4,
    label="觀察值",
)

ax.axvline(10, color=INK_SECONDARY, linestyle="-.", linewidth=1.2)
ax.scatter([10], [110], marker="D", s=56, color=CATEGORICAL[5], zorder=5)
ax.text(
    10.5,
    66,
    "x* = 10，中心 ŷ* = 110\n平均反應 CI：98.585–121.415\n個別預測 PI：76.125–143.875",
    ha="left",
    va="bottom",
    bbox={"facecolor": SURFACE, "edgecolor": "none", "alpha": 0.92},
)

ax.set_title("同一個中心，個別預測區間比平均反應信賴區間寬")
ax.set_xlabel("校園學生人口 x（千人）")
ax.set_ylabel("季度銷售額 y（千美元）")
ax.set_xlim(1, 27)
ax.set_ylim(35, 225)
ax.legend(loc="upper left", ncol=2)

output = Path(__file__).resolve().parents[1] / "generated" / "14-confidence-vs-prediction.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)

