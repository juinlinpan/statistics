"""Plot the Armand's Pizza observations, least-squares line, and residuals."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import CATEGORICAL, INK_PRIMARY, INK_SECONDARY, SURFACE, apply_style


apply_style()

x = np.array([2, 6, 8, 8, 12, 16, 20, 20, 22, 26], dtype=float)
y = np.array([58, 105, 88, 118, 117, 137, 157, 169, 149, 202], dtype=float)
y_hat = 60 + 5 * x

assert np.isclose(x.mean(), 14)
assert np.isclose(y.mean(), 130)
assert np.isclose(np.sum((y - y_hat) ** 2), 1530)

fig, ax = plt.subplots(figsize=(8.2, 5.2))

for index, (x_i, y_i, fitted_i) in enumerate(zip(x, y, y_hat)):
    ax.plot(
        [x_i, x_i],
        [fitted_i, y_i],
        color=INK_SECONDARY,
        linestyle="--",
        linewidth=1.2,
        alpha=0.75,
        label="殘差：實際值到迴歸線的垂直距離" if index == 0 else None,
        zorder=1,
    )

x_line = np.linspace(1, 27, 200)
ax.plot(x_line, 60 + 5 * x_line, color=CATEGORICAL[5], label="估計線  ŷ = 60 + 5x", zorder=2)
ax.scatter(
    x,
    y,
    s=62,
    marker="o",
    facecolor=SURFACE,
    edgecolor=CATEGORICAL[0],
    linewidth=2,
    label="10 家餐廳的觀察值",
    zorder=3,
)

ax.set_title("Armand's Pizza：散佈圖、配適線與殘差")
ax.set_xlabel("校園學生人口 x（千人）")
ax.set_ylabel("季度銷售額 y（千美元）")
ax.set_xlim(0, 28)
ax.set_ylim(45, 215)
ax.legend(loc="upper left")
ax.text(
    0.98,
    0.06,
    "斜率 5：每多 1 千名學生\n預估季度銷售額增加 5 千美元",
    transform=ax.transAxes,
    ha="right",
    va="bottom",
    color=INK_PRIMARY,
    bbox={"facecolor": SURFACE, "edgecolor": "none", "alpha": 0.9},
)

output = Path(__file__).resolve().parents[1] / "generated" / "14-armands-fit.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)

