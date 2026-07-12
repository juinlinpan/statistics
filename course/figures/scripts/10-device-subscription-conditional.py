# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 10, Section 10.1 opening example: marginal vs. conditional
distributions.

Two-way table (matches chapter text exactly):
            續訂  未續訂  列合計
  手機       84    36     120
  電腦       40    40      80
  欄合計    124    76     200

Marginal subscription rate (ignores device): 124/200 = 0.62.
Conditional subscription rates (fix device, divide by row total):
  手機: 84/120 = 0.70
  電腦: 40/80  = 0.50

The figure bars show the two conditional proportions; a dashed reference
line marks the marginal proportion, illustrating that neither device-specific
rate matches the overall rate, and that comparing raw counts (or the overall
rate alone) would hide this difference.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, INK_SECONDARY, SURFACE

apply_style()

devices = ["手機\n(84/120)", "電腦\n(40/80)"]
conditional = [84 / 120, 40 / 80]
marginal = 124 / 200
colors = [CATEGORICAL[0], CATEGORICAL[1]]

fig, ax = plt.subplots(figsize=(6.5, 4.6))

bars = ax.bar(devices, conditional, width=0.5, color=colors, edgecolor=SURFACE, linewidth=1.2)

for b, v in zip(bars, conditional):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v * 100:.0f}%",
            ha="center", va="bottom", fontsize=11, fontweight="bold")

ax.axhline(marginal, color=INK_SECONDARY, linestyle="--", linewidth=1.6, zorder=5)
ax.text(1.02, marginal, f"整體邊際續訂比例 = {marginal * 100:.0f}%（124/200）",
        color=INK_SECONDARY, fontsize=9.5, va="center", ha="left",
        transform=ax.get_yaxis_transform())

ax.set_ylabel("續訂比例")
ax.set_ylim(0, 0.85)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8])
ax.set_yticklabels(["0%", "20%", "40%", "60%", "80%"])
ax.set_title("條件分布 vs. 邊際分布：手機與電腦用戶的續訂比例")

fig.subplots_adjust(right=0.72)

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "10-device-subscription-conditional.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
