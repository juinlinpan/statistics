# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "scipy"]
# ///
"""Chapter 4, worked example 4-5: normal curve with shaded right-tail area.

Package weight X ~ N(mu=12 kg, sigma=2.5 kg). Threshold at 16 kg triggers an
overweight surcharge. z = (16-12)/2.5 = 1.6, so P(X>16) = 1 - Phi(1.6) ~= 0.0548.
Numbers match the chapter's worked example exactly (section "題 4-5").
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

mu, sigma = 12.0, 2.5
threshold = 16.0
z = (threshold - mu) / sigma
tail_prob = 1 - norm.cdf(z)

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 800)
y = norm.pdf(x, mu, sigma)

fig, ax = plt.subplots(figsize=(7.5, 4.5))

ax.plot(x, y, color=CATEGORICAL[0], linewidth=2.2, label="常態曲線 $N(12, 2.5^2)$")

x_tail = np.linspace(threshold, mu + 4 * sigma, 200)
y_tail = norm.pdf(x_tail, mu, sigma)
ax.fill_between(x_tail, y_tail, color=ACCENT, alpha=0.55, linewidth=0,
                 label=f"$P(X>16)\\approx{tail_prob:.4f}$")

ax.axvline(mu, color=INK_SECONDARY, linestyle="--", linewidth=1.2)
ax.text(mu, ax.get_ylim()[1] * 0.92, "$\\mu=12$", ha="center", va="top",
        color=INK_SECONDARY, fontsize=10)

ax.axvline(threshold, color=ACCENT, linestyle="-", linewidth=1.4)
ax.text(threshold, ax.get_ylim()[1] * 0.78, "$x=16$\n$z=1.6$", ha="left", va="top",
        color=ACCENT, fontsize=10)

ax.set_xlabel("包裹重量（公斤）")
ax.set_ylabel("機率密度")
ax.set_title("常態曲線的右尾機率：包裹超重費門檻")
ax.legend(loc="upper left")

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; P(X>16) = {tail_prob:.4f}, z = {z:.4f}")
