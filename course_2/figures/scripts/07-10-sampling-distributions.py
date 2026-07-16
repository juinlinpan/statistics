"""Compare the SAT sample-mean distributions for n=30 and n=100."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_PRIMARY, INK_SECONDARY, apply_style


apply_style()

OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "07-10-sampling-distributions.png"
MU = 1697
LOWER = 1687
UPPER = 1707


def normal_pdf(x: np.ndarray, mean: float, sd: float) -> np.ndarray:
    """Return a normal density without adding another statistical dependency."""
    return np.exp(-0.5 * ((x - mean) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))


fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.4), sharex=True, sharey=True)
cases = [
    (30, 15.96, "15.96", 0.4714, "忽略有限母體修正"),
    (100, 8.2, "8.2", 0.7776, "包含有限母體修正"),
]
x = np.linspace(1640, 1754, 900)

for ax, (n, se, se_label, probability, note) in zip(axes, cases):
    density = normal_pdf(x, MU, se)
    inside = (x >= LOWER) & (x <= UPPER)
    ax.plot(x, density, color=CATEGORICAL[0], label="樣本平均數的抽樣分配")
    ax.fill_between(
        x[inside],
        density[inside],
        color=CATEGORICAL[1],
        alpha=0.28,
        hatch="///",
        edgecolor=CATEGORICAL[1],
        label="1687 到 1707 分",
    )
    ax.axvline(MU, color=INK_PRIMARY, linestyle="--", linewidth=1.5)
    ax.axvline(LOWER, color=ACCENT, linestyle=":", linewidth=1.5)
    ax.axvline(UPPER, color=ACCENT, linestyle=":", linewidth=1.5)
    ax.set_title(f"n = {n}：SE = {se_label} 分")
    ax.set_xlabel("樣本平均 SAT 分數")
    ax.text(
        0.03,
        0.94,
        f"區間機率 = {probability:.2%}\n{note}",
        transform=ax.transAxes,
        va="top",
        color=INK_SECONDARY,
    )

axes[0].set_ylabel("機率密度")
axes[0].legend(loc="upper left", bbox_to_anchor=(0, 0.80))
fig.suptitle("樣本變大，平均數的抽樣分配變窄", fontsize=15, fontweight="bold")
fig.text(0.5, 0.01, "示意分配；中心皆為母體平均數 1697 分", ha="center", color=INK_SECONDARY)
fig.tight_layout(rect=(0, 0.05, 1, 0.92))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT)
plt.close(fig)
