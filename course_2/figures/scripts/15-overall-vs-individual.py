"""Contrast the overall F test and individual t tests under multicollinearity."""

from pathlib import Path

import matplotlib.pyplot as plt

from _style import ACCENT, CATEGORICAL, INK_SECONDARY, apply_style


apply_style()

labels = ["整體 F\n(F = 8.41)", "里程 t", "油耗 t"]
p_values = [0.014, 0.075, 0.350]
colors = [ACCENT, CATEGORICAL[0], CATEGORICAL[0]]
markers = ["D", "o", "o"]

fig, ax = plt.subplots(figsize=(8.2, 4.8))
for index, (label, p_value, color, marker) in enumerate(zip(labels, p_values, colors, markers)):
    ax.vlines(index, 0, p_value, color=color, linewidth=3, alpha=0.7)
    ax.scatter(index, p_value, color=color, marker=marker, s=95, zorder=3)
    ax.text(index, p_value + 0.015, f"p = {p_value:.3f}", ha="center", color=INK_SECONDARY)

ax.axhline(0.05, color=INK_SECONDARY, linestyle="--", linewidth=1.7, label="顯著水準 α = 0.05")
ax.text(0.02, 0.058, "低於線：顯著", color=INK_SECONDARY, transform=ax.get_yaxis_transform())
ax.set_xticks(range(len(labels)), labels)
ax.set(ylabel="p-value", title="共線性下：整體模型顯著，個別變數可能不顯著")
ax.set_ylim(0, 0.41)
ax.legend(loc="upper left")
fig.tight_layout()

output = Path(__file__).resolve().parents[1] / "generated" / "15-overall-vs-individual.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)
