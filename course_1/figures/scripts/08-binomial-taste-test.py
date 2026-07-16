# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "scipy"]
# ///
"""Chapter 8, Section 4 worked example: exact binomial right-tailed p-value.

A taster claims she can distinguish two drinks. n=10 independent two-choice
trials; under H0:p=0.5 (guessing), X ~ Binomial(10, 0.5). She got x_obs=8
correct. H0:p=0.5, HA:p>0.5.

p-value = P(X>=8) = [C(10,8)+C(10,9)+C(10,10)] / 2^10 = 56/1024 ~= 0.0547.

Bars for k=8,9,10 (the "at least as extreme" outcomes under the right-tailed
alternative) are colored with the shared ACCENT color; the rest of the pmf
is drawn in the neutral categorical blue. This matches the chapter's point
that the p-value must sum P(X=8)+P(X=9)+P(X=10), not just P(X=8) alone.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

n, p0, x_obs = 10, 0.5, 8
k = np.arange(0, n + 1)
pmf = binom.pmf(k, n, p0)
p_value = binom.sf(x_obs - 1, n, p0)  # P(X >= x_obs)

colors = [ACCENT if ki >= x_obs else CATEGORICAL[0] for ki in k]
alphas = [0.85 if ki >= x_obs else 0.85 for ki in k]

fig, ax = plt.subplots(figsize=(7.5, 4.5))

bars = ax.bar(k, pmf, color=colors, width=0.6, edgecolor="none")
for b, a in zip(bars, alphas):
    b.set_alpha(a)

ax.axvline(x_obs, color=ACCENT, linestyle="--", linewidth=1.4)
ax.text(x_obs, max(pmf) * 1.02, f"$x_{{obs}}=8$", ha="center", va="bottom",
        color=ACCENT, fontsize=10)

ax.set_xticks(k)
ax.set_xlabel("答對次數 $k$（共 10 次試驗）")
ax.set_ylabel("機率 $P(X=k)$，$H_0: p=0.5$")
ax.set_title(
    f"精確二項檢定：$P(X\\geq8)={p_value:.4f}$（味覺測試，$n=10$）"
)

# Legend proxies
from matplotlib.patches import Patch
legend_handles = [
    Patch(facecolor=CATEGORICAL[0], label="未達觀察值：$k<8$"),
    Patch(facecolor=ACCENT, label=f"至少同樣極端：$k\\geq8$，加總＝{p_value:.4f}"),
]
ax.legend(handles=legend_handles, loc="upper left")

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; P(X>=8) = {p_value:.4f}")
