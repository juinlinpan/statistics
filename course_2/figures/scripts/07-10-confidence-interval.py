"""Visualize the Apartment Rents 95% t confidence interval."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

from _style import ACCENT, CATEGORICAL, INK_PRIMARY, INK_SECONDARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "07-10-confidence-interval.png"
DF = 15
T_CRITICAL = 2.131
XBAR = 750.0
MARGIN = 29.30
LOWER = 720.70
UPPER = 779.30

fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.3), gridspec_kw={"width_ratios": [1.2, 1]})

# Left: where the t multiplier comes from.
ax = axes[0]
x = np.linspace(-4.2, 4.2, 900)
density = t.pdf(x, DF)
middle = (x >= -T_CRITICAL) & (x <= T_CRITICAL)
tails = ~middle
ax.plot(x, density, color=CATEGORICAL[0])
ax.fill_between(
    x[middle], density[middle], color=CATEGORICAL[1], alpha=0.25,
    hatch="///", edgecolor=CATEGORICAL[1], label="中央 95%",
)
ax.fill_between(
    x[tails & (x < 0)], density[tails & (x < 0)], color=ACCENT, alpha=0.35,
    hatch="xx", edgecolor=ACCENT,
)
ax.fill_between(
    x[tails & (x > 0)], density[tails & (x > 0)], color=ACCENT, alpha=0.35,
    hatch="xx", edgecolor=ACCENT, label="每尾 2.5%",
)
for critical in (-T_CRITICAL, T_CRITICAL):
    ax.axvline(critical, color=INK_PRIMARY, linestyle="--", linewidth=1.4)
ax.text(-T_CRITICAL, 0.02, "−2.131", ha="right", color=INK_SECONDARY)
ax.text(T_CRITICAL, 0.02, "2.131", ha="left", color=INK_SECONDARY)
ax.set_title("df = 15 的 t 臨界值")
ax.set_xlabel("t 值")
ax.set_ylabel("機率密度")
ax.legend(loc="upper left")

# Right: transform the multiplier into the rent interval.
ax = axes[1]
ax.errorbar(
    XBAR,
    0,
    xerr=MARGIN,
    fmt="o",
    color=INK_PRIMARY,
    ecolor=CATEGORICAL[0],
    elinewidth=4,
    capsize=10,
    markersize=8,
    label="樣本平均與 95% 區間",
)
ax.axvline(XBAR, color=INK_PRIMARY, linestyle="--", linewidth=1.2)
ax.text(LOWER, 0.10, "$720.70", ha="center", color=CATEGORICAL[0])
ax.text(XBAR, -0.15, "$750.00", ha="center", color=INK_PRIMARY)
ax.text(UPPER, 0.10, "$779.30", ha="center", color=CATEGORICAL[0])
ax.text(XBAR, 0.30, "誤差範圍 ±$29.30", ha="center", color=INK_SECONDARY)
ax.set_xlim(705, 795)
ax.set_ylim(-0.42, 0.55)
ax.set_yticks([])
ax.set_xlabel("平均月租 (美元)")
ax.set_title("750 ± 29.30 美元")
ax.legend(loc="lower center")

fig.suptitle("95% 信賴區間：臨界值 × 標準誤", fontsize=15, fontweight="bold")
fig.text(0.5, 0.01, "Apartment Rents 例題；區間估計的是母體平均月租", ha="center", color=INK_SECONDARY)
fig.tight_layout(rect=(0, 0.05, 1, 0.92))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)

