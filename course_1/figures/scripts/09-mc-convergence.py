# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 9, Section 1.2: Monte Carlo estimate stabilizing as B grows (LLN).

Reuses the chapter's own opening example in Section 1.1: a fair coin is
tossed 20 times; estimate P(at least 14 heads). Each simulated trial b
tosses 20 fair coins and records the indicator I_b = 1{heads >= 14}. The
running Monte Carlo estimate p_hat_MC(B) = mean(I_1, ..., I_B) is plotted
against B on a log scale, alongside the exact true probability p (computed
from the exact binomial pmf, since this small example is enumerable) and
the +/-2*SE_MC(B) envelope from the chapter's Monte Carlo SE formula
SE_MC = sqrt(p(1-p)/B). This is a SIMULATION illustrating the Law of Large
Numbers point in Section 1.2 -- not observed data.

Seeded with np.random.default_rng(9) for reproducibility.
"""

import sys
from math import comb
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, BASELINE

apply_style()

rng = np.random.default_rng(9)

n_flips = 20       # coin tosses per trial (Section 1.1 example)
threshold = 14     # "at least 14 heads"
B_max = 20_000      # maximum number of Monte Carlo simulations

# Exact true probability, computable here because the example is small
# enough to enumerate exactly (used only to draw the reference line; the
# chapter's point is that Monte Carlo approximates this without needing
# the exact formula).
p_true = sum(comb(n_flips, k) * 0.5 ** n_flips for k in range(threshold, n_flips + 1))

# Simulate B_max independent trials of 20 fair-coin tosses.
flips = rng.integers(0, 2, size=(B_max, n_flips))
heads = flips.sum(axis=1)
indicator = (heads >= threshold).astype(float)

B_grid = np.arange(1, B_max + 1)
running_estimate = np.cumsum(indicator) / B_grid

# +/- 2 SE_MC envelope around the true probability (chapter's SE_MC formula).
# Clipped to [0, 1] since this is a probability envelope (the normal-approx
# envelope is only meaningful within that range, especially at small B).
se_mc = np.sqrt(p_true * (1 - p_true) / B_grid)
upper_env = np.clip(p_true + 2 * se_mc, 0, 1)
lower_env = np.clip(p_true - 2 * se_mc, 0, 1)

fig, ax = plt.subplots(figsize=(7.5, 4.8))

ax.plot(B_grid, running_estimate, color=CATEGORICAL[0], linewidth=1.4,
        label=r"累積估計 $\hat{p}_{MC}(B)$")
ax.plot(B_grid, upper_env, color=BASELINE, linewidth=1.2, linestyle="--",
        label=r"$p \pm 2\,SE_{MC}(B)$ 包絡線")
ax.plot(B_grid, lower_env, color=BASELINE, linewidth=1.2, linestyle="--")
ax.axhline(p_true, color=ACCENT, linewidth=1.6, linestyle="-",
           label=f"真實機率 $p={p_true:.4f}$")

ax.set_xscale("log")
ax.set_xlabel("模擬次數 $B$（對數尺度）")
ax.set_ylabel(r"累積 Monte Carlo 估計 $\hat{p}_{MC}$")
ax.set_title("擲 20 枚公平硬幣至少 14 次正面：估計值隨 $B$ 增加而趨於穩定")
ax.legend(loc="upper right", fontsize=9)

fig.tight_layout()
out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "09-mc-convergence.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(f"True p = {p_true:.6f}; final estimate at B={B_max}: {running_estimate[-1]:.6f}")
