"""Show how correcting the chapter's erroneous outlier changes the fitted line."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import CATEGORICAL, INK_PRIMARY, INK_SECONDARY, SURFACE, apply_style


apply_style()

x = np.array([1, 1, 2, 3, 3, 3, 4, 4, 5, 6], dtype=float)
y_with_error = np.array([45, 55, 50, 75, 40, 45, 30, 35, 25, 15], dtype=float)
y_corrected = y_with_error.copy()
y_corrected[3] = 30


def fit_summary(y_values: np.ndarray) -> tuple[float, float, float]:
    slope, intercept = np.polyfit(x, y_values, 1)
    fitted = intercept + slope * x
    sse = np.sum((y_values - fitted) ** 2)
    sst = np.sum((y_values - y_values.mean()) ** 2)
    return intercept, slope, 1 - sse / sst


bad_intercept, bad_slope, bad_r2 = fit_summary(y_with_error)
good_intercept, good_slope, good_r2 = fit_summary(y_corrected)
assert round(bad_intercept, 2) == 64.96
assert round(bad_slope, 2) == -7.33
assert round(100 * bad_r2, 2) == 49.68
assert round(good_intercept, 2) == 59.24
assert round(good_slope, 2) == -6.95
assert round(100 * good_r2, 2) == 83.80

fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.8), sharex=True, sharey=True)
x_line = np.linspace(0.7, 6.3, 200)

for ax, y_values, intercept, slope, title, equation, r_squared, text_position, text_alignment in [
    (
        axes[0],
        y_with_error,
        bad_intercept,
        bad_slope,
        "更正前：第 4 筆誤植為 75",
        "ŷ = 64.96 − 7.33x",
        "R² = 49.68%",
        (0.05, 0.06),
        ("left", "bottom"),
    ),
    (
        axes[1],
        y_corrected,
        good_intercept,
        good_slope,
        "更正後：第 4 筆為 30",
        "ŷ = 59.24 − 6.95x",
        "R² = 83.80%",
        (0.95, 0.93),
        ("right", "top"),
    ),
]:
    ax.scatter(
        x,
        y_values,
        s=52,
        marker="o",
        facecolor=SURFACE,
        edgecolor=CATEGORICAL[0],
        linewidth=1.7,
        zorder=3,
    )
    ax.plot(x_line, intercept + slope * x_line, color=INK_PRIMARY)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.text(
        text_position[0],
        text_position[1],
        f"{equation}\n{r_squared}",
        transform=ax.transAxes,
        ha=text_alignment[0],
        va=text_alignment[1],
        bbox={"facecolor": SURFACE, "edgecolor": "none", "alpha": 0.9},
    )

bad_fitted_at_three = bad_intercept + bad_slope * 3
axes[0].plot([3, 3], [bad_fitted_at_three, 75], color=CATEGORICAL[5], linestyle="--", linewidth=1.5)
axes[0].scatter([3], [75], marker="X", s=105, color=CATEGORICAL[5], zorder=4)
axes[0].annotate(
    "錯誤離群值\n標準化殘差 2.6816",
    xy=(3, 75),
    xytext=(3.65, 75),
    arrowprops={"arrowstyle": "->", "color": CATEGORICAL[5]},
    color=INK_SECONDARY,
)
axes[1].scatter([3], [30], marker="D", s=75, color=CATEGORICAL[1], zorder=4)
axes[1].annotate(
    "查證後更正為 30",
    xy=(3, 30),
    xytext=(3.55, 20),
    arrowprops={"arrowstyle": "->", "color": CATEGORICAL[1]},
    color=INK_SECONDARY,
)

axes[0].set_ylabel("y")
axes[0].set_xlim(0.5, 6.5)
axes[0].set_ylim(5, 82)
fig.suptitle("一筆資料錯誤會改變配適線、殘差與 R²", y=1.02)

output = Path(__file__).resolve().parents[1] / "generated" / "14-outlier-correction.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)
