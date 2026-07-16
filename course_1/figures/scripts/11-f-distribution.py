# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "scipy"]
# ///
"""Chapter 11, Section 4-5 worked example: F distribution and the right-tail p-value.

Reuses the exact same three-group worked example as
11-group-dotplot.py (A: 4,5,6; B: 6,7,8; C: 8,9,10; grand mean 7):
  SS_B=24, SS_W=6, df_B=2, df_W=6, MS_B=12, MS_W=1, F_obs = MS_B/MS_W = 12.

F ~ F_{2,6} under H0. p = P(F_{2,6} >= 12), computed here with scipy.stats.f
(right-tailed, per Section 5's "F 分配與 p 值").
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f as f_dist

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

df_b, df_w = 2, 6
f_obs = 12.0
p_value = f_dist.sf(f_obs, df_b, df_w)

x_max = 14.5
x = np.linspace(0.001, x_max, 900)
y = f_dist.pdf(x, df_b, df_w)

fig, ax = plt.subplots(figsize=(7.5, 4.5))

ax.plot(x, y, color=CATEGORICAL[0], linewidth=2.2, label=f"$F$ 分配（$df=(2,6)$）")

x_tail = np.linspace(f_obs, x_max, 200)
y_tail = f_dist.pdf(x_tail, df_b, df_w)
ax.fill_between(
    x_tail, y_tail, color=ACCENT, alpha=0.35, linewidth=0,
    label=f"右尾 $P(F_{{2,6}}\\geq12)\\approx{p_value:.4f}$",
)

ax.axvline(f_obs, color=ACCENT, linestyle="-", linewidth=1.6)
ax.text(f_obs, ax.get_ylim()[1] * 0.35, "$F_{obs}=12$", ha="right", va="center",
        color=ACCENT, fontsize=10, rotation=90)

ax.set_xlim(0, x_max)
ax.set_xlabel("$F$ 統計量（分子自由度 2，分母自由度 6）")
ax.set_ylabel("機率密度")
ax.set_title("F 分配的右尾 p 值：三組小型範例（$F_{2,6}=12$）")
ax.legend(loc="upper center")

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; F = {f_obs}, df=({df_b},{df_w}), p = {p_value:.6f}")
