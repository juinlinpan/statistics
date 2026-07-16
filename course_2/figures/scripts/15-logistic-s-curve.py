"""Plot the chapter's logistic curve with beta0=-7 and beta1=3."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_SECONDARY, apply_style


apply_style()

x = np.linspace(0, 4.5, 400)
probability = 1 / (1 + np.exp(-(-7 + 3 * x)))
highlight_x = np.array([2.0, 3.0])
highlight_probability = 1 / (1 + np.exp(-(-7 + 3 * highlight_x)))

fig, ax = plt.subplots(figsize=(8.2, 4.8))
ax.plot(x, probability, color=CATEGORICAL[0], linewidth=2.6, label="P(y=1|x) = logistic(-7 + 3x)")
ax.scatter(highlight_x, highlight_probability, color=ACCENT, marker="D", s=75, zorder=3)
for x_value, p_value in zip(highlight_x, highlight_probability):
    ax.vlines(x_value, 0, p_value, color=INK_SECONDARY, linestyle=":", linewidth=1.3)
    ax.hlines(p_value, 0, x_value, color=INK_SECONDARY, linestyle=":", linewidth=1.3)
    ax.annotate(f"x={x_value:.0f}：P≈{p_value:.2f}", (x_value, p_value), xytext=(8, -20), textcoords="offset points")

ax.axhline(0.5, color=INK_SECONDARY, linestyle="--", linewidth=1.2, label="機率 0.5")
ax.set(xlabel="x", ylabel="事件發生機率 P(y=1|x)", title="Logistic 函數把所有預測壓在 0 到 1")
ax.set_xlim(0, 4.5)
ax.set_ylim(0, 1.03)
ax.legend(loc="lower right")
fig.tight_layout()

output = Path(__file__).resolve().parents[1] / "generated" / "15-logistic-s-curve.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)
