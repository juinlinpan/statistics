# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "scipy"]
# ///
"""Chapter 8, Section 5 worked example: one-sample t-test, left-tailed p-value.

New ordering interface wait-time example: n=25 customers, x_bar=5.6 min,
s=1.5 min, H0:mu=6 vs HA:mu<6.

SE = 1.5/sqrt(25) = 0.3 min
t  = (5.6-6)/0.3 = -1.33, df = 24

p-value = P(T_24 <= -1.33), the left tail of the t_24 distribution.
Numbers match the chapter's worked example in Section 5 exactly.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t as t_dist

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

df = 24
t_obs = -1.33
p_value = t_dist.cdf(t_obs, df)

x = np.linspace(-4.2, 4.2, 800)
y = t_dist.pdf(x, df)

fig, ax = plt.subplots(figsize=(7.5, 4.5))

ax.plot(x, y, color=CATEGORICAL[0], linewidth=2.2, label=f"$t$ 分配（$df=24$）")

x_tail = np.linspace(-4.2, t_obs, 200)
y_tail = t_dist.pdf(x_tail, df)
ax.fill_between(x_tail, y_tail, color=ACCENT, alpha=0.35, linewidth=0,
                 label=f"左尾 $P(T\\leq-1.33)\\approx{p_value:.4f}$")

ax.axvline(0, color=INK_SECONDARY, linestyle="--", linewidth=1.2)
ax.text(0, ax.get_ylim()[1] * 0.92, "$\\mu_0=6$\n（$t=0$）", ha="center", va="top",
        color=INK_SECONDARY, fontsize=9.5)

ax.axvline(t_obs, color=ACCENT, linestyle="-", linewidth=1.6)
ax.text(t_obs, ax.get_ylim()[1] * 0.78, "$t=-1.33$", ha="right", va="top",
        color=ACCENT, fontsize=10)

ax.set_xlabel("$t$ 統計量（自由度 24）")
ax.set_ylabel("機率密度")
ax.set_title("單樣本 $t$ 檢定的左尾 p 值：等候時間範例")
ax.legend(loc="upper left")

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; t = {t_obs}, df = {df}, p = {p_value:.4f}")
