"""Plot Butler standardized residuals against fitted values."""

from pathlib import Path

import matplotlib.pyplot as plt

from _style import ACCENT, CATEGORICAL, INK_SECONDARY, apply_style


apply_style()

fitted = [8.93846, 4.95830, 8.93846, 7.09161, 4.03488, 5.86892, 6.48667, 6.79875, 7.40369, 6.48026]
standardized = [0.78344, -0.34962, -0.08334, -1.30929, 0.38167, 0.65431, 1.68917, -1.77372, 0.36703, -0.77639]

fig, ax = plt.subplots(figsize=(8.2, 4.8))
ax.scatter(fitted, standardized, color=CATEGORICAL[0], marker="o", s=65, edgecolor="white", linewidth=0.8, zorder=3)
for observation, (x_value, residual) in enumerate(zip(fitted, standardized), start=1):
    ax.annotate(str(observation), (x_value, residual), xytext=(5, 5), textcoords="offset points", fontsize=9)

ax.axhline(0, color=INK_SECONDARY, linewidth=1.5)
ax.axhline(2, color=ACCENT, linestyle="--", linewidth=1.7)
ax.axhline(-2, color=ACCENT, linestyle="--", linewidth=1.7, label="可能離群值界線 ±2")
ax.fill_between([3.7, 9.3], -2, 2, color=CATEGORICAL[0], alpha=0.05)
ax.set(xlabel="預測行車時間(小時)", ylabel="標準化殘差", title="Butler：殘差圍繞 0，且都在 ±2 內")
ax.set_xlim(3.7, 9.3)
ax.set_ylim(-2.35, 2.35)
ax.legend(loc="upper left")
fig.tight_layout()

output = Path(__file__).resolve().parents[1] / "generated" / "15-standardized-residuals.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)
