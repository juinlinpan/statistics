# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "scipy"]
# ///
"""Chapter 4, section 7 worked example: normal approximation to a binomial
distribution with continuity correction.

X ~ Bin(n=100, p=0.4). mu = np = 40, sigma = sqrt(np(1-p)) = sqrt(24) ~= 4.899.
Event "at most 45 successes" (X <= 45) is continuity-corrected to Y < 45.5,
giving z = (45.5-40)/4.899 ~= 1.123 and P(X<=45) ~= Phi(1.123) ~= 0.869.
Numbers match the chapter's worked example exactly (section 7, "例：近似至多 45 次成功").
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

n, p = 100, 0.4
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
cc_boundary = 45.5
z = (cc_boundary - mu) / sigma
approx_prob = norm.cdf(z)

k_min, k_max = 20, 61
k = np.arange(k_min, k_max + 1)
pmf = binom.pmf(k, n, p)

fig, ax = plt.subplots(figsize=(8.5, 5))

ax.bar(k, pmf, width=0.9, color=CATEGORICAL[0], alpha=0.85,
       label="二項機率直方圖 $X\\sim\\mathrm{Bin}(100,0.4)$")

x = np.linspace(k_min - 0.5, k_max + 0.5, 800)
y = norm.pdf(x, mu, sigma)
ax.plot(x, y, color=CATEGORICAL[1], linewidth=2.2,
        label="常態近似曲線 $N(40, 24)$")

x_shade = np.linspace(k_min - 0.5, cc_boundary, 300)
y_shade = norm.pdf(x_shade, mu, sigma)
ax.fill_between(x_shade, y_shade, color=ACCENT, alpha=0.35, linewidth=0,
                 label=f"$P(X\\leq45)\\approx\\Phi(1.123)\\approx{approx_prob:.3f}$")

ax.axvline(cc_boundary, color=ACCENT, linestyle="--", linewidth=1.4)
ax.text(cc_boundary, ax.get_ylim()[1] * 0.95, "連續性修正邊界 45.5",
        ha="left", va="top", color=ACCENT, fontsize=10)

ax.axvline(mu, color=INK_SECONDARY, linestyle=":", linewidth=1.2)
ax.text(mu, ax.get_ylim()[1] * 0.82, "$\\mu=40$", ha="center", va="top",
        color=INK_SECONDARY, fontsize=10)

ax.set_xlabel("成功次數 $k$")
ax.set_ylabel("機率")
ax.set_title("常態近似二項分配：連續性修正 $P(X\\leq45)$")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1, fontsize=9)

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; mu={mu}, sigma={sigma:.4f}, z={z:.4f}, P(X<=45)~={approx_prob:.4f}")
