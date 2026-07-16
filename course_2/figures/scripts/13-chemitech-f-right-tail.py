"""Plot the Chemitech F distribution and its right-tail rejection region."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f

from _style import ACCENT, CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "13-chemitech-f-right-tail.png"

df1, df2 = 2, 12
alpha = 0.05
critical = f.ppf(1 - alpha, df1, df2)
observed = 9.18
p_value = f.sf(observed, df1, df2)

x = np.linspace(0.001, 12, 1600)
y = f.pdf(x, df1, df2)

fig, ax = plt.subplots(figsize=(9.6, 4.8))
ax.plot(x, y, color=CATEGORICAL[0], label=r"$F(2,12)$ 密度")
tail = x >= critical
ax.fill_between(
    x[tail],
    y[tail],
    color=ACCENT,
    alpha=0.28,
    hatch="///",
    edgecolor=ACCENT,
    label=r"拒絕域：上尾 $\alpha=0.05$",
)
ax.axvline(critical, color=ACCENT, linestyle="--", linewidth=2)
ax.axvline(observed, color=INK_PRIMARY, linestyle="-.", linewidth=2.2)
ax.annotate(
    f"臨界值 {critical:.2f}",
    xy=(critical, f.pdf(critical, df1, df2)),
    xytext=(critical + 0.6, 0.16),
    arrowprops={"arrowstyle": "->", "color": ACCENT},
    color=ACCENT,
    weight="bold",
)
ax.annotate(
    f"觀察值 F = {observed:.2f}\np ≈ {p_value:.3f}",
    xy=(observed, f.pdf(observed, df1, df2)),
    xytext=(7.1, 0.32),
    arrowprops={"arrowstyle": "->", "color": INK_PRIMARY},
    color=INK_PRIMARY,
    weight="bold",
)
ax.set_xlim(0, 12)
ax.set_ylim(bottom=0)
ax.set_xlabel("F 統計量")
ax.set_ylabel("機率密度")
ax.set_title("Chemitech 的 F 檢定只有右尾拒絕域", fontsize=15, weight="bold")
ax.legend(loc="upper center", bbox_to_anchor=(0.56, 0.98))
fig.text(
    0.01,
    0.01,
    "理論分配；df₁=2、df₂=12。F 越大，代表組間變異相對組內變異越突出。",
    color=INK_MUTED,
    fontsize=9,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)
