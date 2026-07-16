"""Show the two-tailed rejection regions for the accident-proportion test."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_PRIMARY, INK_SECONDARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "07-10-two-tailed-test.png"
CRITICAL = 1.96
OBSERVED = 1.28


def standard_normal_pdf(x: np.ndarray) -> np.ndarray:
    return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)


fig, ax = plt.subplots(figsize=(9.6, 4.8))
x = np.linspace(-4, 4, 1000)
density = standard_normal_pdf(x)
left = x <= -CRITICAL
right = x >= CRITICAL

ax.plot(x, density, color=CATEGORICAL[0], label="$H_0$ 下的標準常態分配")
ax.fill_between(
    x[left], density[left], color=ACCENT, alpha=0.38,
    hatch="xx", edgecolor=ACCENT, label="拒絕域：每尾 2.5%",
)
ax.fill_between(x[right], density[right], color=ACCENT, alpha=0.38, hatch="xx", edgecolor=ACCENT)
for critical in (-CRITICAL, CRITICAL):
    ax.axvline(critical, color=ACCENT, linestyle="--", linewidth=1.6)
ax.axvline(OBSERVED, color=INK_PRIMARY, linestyle="-.", linewidth=2.2, label="觀察值 z = 1.28")
ax.scatter([OBSERVED], [standard_normal_pdf(np.array([OBSERVED]))[0]], color=INK_PRIMARY, marker="D", zorder=4)

ax.annotate(
    "z = 1.28 仍在不拒絕區\n雙尾 p 值 = 0.2006",
    xy=(OBSERVED, standard_normal_pdf(np.array([OBSERVED]))[0]),
    xytext=(2.25, 0.28),
    arrowprops={"arrowstyle": "->", "color": INK_SECONDARY},
    ha="center",
    color=INK_SECONDARY,
)
ax.text(-CRITICAL, 0.015, "−1.96", ha="right", color=ACCENT)
ax.text(CRITICAL, 0.015, "1.96", ha="left", color=ACCENT)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.44)
ax.set_xlabel("z 檢定統計量")
ax.set_ylabel("機率密度")
ax.set_title("雙尾檢定：兩端都是反對 $H_0$ 的極端結果", fontsize=15, fontweight="bold")
ax.legend(loc="upper left")
fig.text(0.5, 0.01, "National Safety Council 例題：α = 0.05，臨界值為 ±1.96", ha="center", color=INK_SECONDARY)
fig.tight_layout(rect=(0, 0.05, 1, 1))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)

