# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Simulation: long-run coverage of 95% confidence intervals for a mean.

This is a SIMULATION illustrating the frequentist interpretation introduced
in Section 1 ("信賴區間是隨機程序的產物") -- it is not observed data.

Setup (echoes the chapter's own customer-wait-time example in Section 3,
but here the population mean is *known* by construction so we can check
coverage):

- Known population: Normal(mu=8.5 minutes, sigma=3.0 minutes)
- Draw 50 independent samples of n=100 from this population
- For each sample, build a 95% CI using the exact formula the chapter
  teaches: x_bar +/- 1.96 * s / sqrt(n)   (s = sample SD, ddof=1)
- Plot each interval as a horizontal errorbar at its own row, with a
  vertical reference line at the true mean mu=8.5
- Intervals that miss mu are colored differently (ACCENT/red) from those
  that contain it (CATEGORICAL[0]/blue)

Seeded with np.random.default_rng(1) for reproducibility.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT

apply_style()

rng = np.random.default_rng(1)

mu_true = 8.5      # minutes, known population mean (simulation truth)
sigma_true = 3.0   # minutes, known population SD
n = 100            # sample size, matches the chapter's worked example
n_samples = 50     # number of independent samples drawn
z_star = 1.96      # 95% normal critical value

lowers = np.empty(n_samples)
uppers = np.empty(n_samples)
centers = np.empty(n_samples)

for i in range(n_samples):
    sample = rng.normal(loc=mu_true, scale=sigma_true, size=n)
    x_bar = sample.mean()
    s = sample.std(ddof=1)
    se = s / np.sqrt(n)
    moe = z_star * se
    centers[i] = x_bar
    lowers[i] = x_bar - moe
    uppers[i] = x_bar + moe

covers = (lowers <= mu_true) & (uppers >= mu_true)
n_cover = int(covers.sum())
coverage_pct = 100 * n_cover / n_samples

fig, ax = plt.subplots(figsize=(7.5, 9.5))

rows = np.arange(1, n_samples + 1)
hit_color = CATEGORICAL[0]
miss_color = ACCENT

for i in range(n_samples):
    color = hit_color if covers[i] else miss_color
    ax.plot([lowers[i], uppers[i]], [rows[i], rows[i]], color=color, linewidth=2.0, zorder=2)
    ax.plot(centers[i], rows[i], marker="o", color=color, markersize=3.5, zorder=3)

ax.axvline(mu_true, color="#0b0b0b", linewidth=1.5, linestyle="--", zorder=1)
ax.text(
    mu_true, n_samples + 1.5, f"真實母體平均數 μ = {mu_true}",
    ha="center", va="bottom", fontsize=10,
)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=hit_color, linewidth=2.0, marker="o", markersize=4, label=f"涵蓋真值 (n={n_cover})"),
    Line2D([0], [0], color=miss_color, linewidth=2.0, marker="o", markersize=4, label=f"未涵蓋真值 (n={n_samples - n_cover})"),
]
ax.legend(handles=legend_elements, loc="upper right", fontsize=9)

ax.set_xlabel("樣本平均數的 95% 信賴區間（分鐘）")
ax.set_ylabel("模擬抽樣編號（每列一次獨立抽樣）")
ax.set_ylim(0, n_samples + 3)
ax.set_title(f"50 次獨立抽樣的 95% 信賴區間模擬（涵蓋率 {n_cover}/{n_samples} = {coverage_pct:.0f}%）")

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "07-ci-coverage.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(f"Coverage: {n_cover}/{n_samples} = {coverage_pct:.1f}%")
