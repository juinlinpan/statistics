# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Three commonly confused histograms, tied to the chapter's checkout-time example.

Population: right-skewed checkout time, mean 12 min, SD 6 min (Gamma(shape=4,
scale=3), matching Section 5.3's worked example E(Xbar)=12, SE(Xbar)=1 at n=36).

Panel 1: population/probability histogram (simulated large population, N=100,000
draws, standing in for the theoretical checkout-time distribution).
Panel 2: one single sample's data histogram (n=36 individual checkout times).
Panel 3: sampling distribution of the sample mean Xbar across R=10,000 repeated
samples of size n=36 each, with the CLT normal approximation N(12, 1^2) overlaid.

This is a simulation illustrating the general principle described in Section 5.5
("模擬與三種直方圖"), not observed data.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

rng = np.random.default_rng(20260512)

# Population: checkout time, mean 12 min, SD 6 min, right-skewed.
SHAPE, SCALE = 4.0, 3.0
N_POP = 100_000
N = 36  # sample size per draw, matches Section 5.3's checkout-time example
R = 10_000  # number of repeated samples for the sampling-distribution panel

population = rng.gamma(SHAPE, SCALE, size=N_POP)
one_sample = rng.gamma(SHAPE, SCALE, size=N)
sample_means = np.array(
    [rng.gamma(SHAPE, SCALE, size=N).mean() for _ in range(R)]
)

mu = SHAPE * SCALE  # 12
sigma = np.sqrt(SHAPE) * SCALE  # 6
se = sigma / np.sqrt(N)  # 1

fig, axes = plt.subplots(1, 3, figsize=(13, 4.3))

# Panel 1: population histogram
ax = axes[0]
ax.hist(population, bins=40, range=(0, 48), color=CATEGORICAL[0], edgecolor="white", linewidth=0.3, density=True)
ax.axvline(mu, color=INK_SECONDARY, linewidth=1.5, linestyle="--")
ax.set_title(f"① 母體直方圖\n(模擬 N={N_POP:,} 筆，右偏)")
ax.set_xlabel("個別結帳時間（分鐘）")
ax.set_ylabel("密度")
ax.text(mu + 1, ax.get_ylim()[1] * 0.9, f"$\\mu$ = {mu:.0f}", color=INK_SECONDARY, fontsize=10)

# Panel 2: one single sample's data histogram
ax = axes[1]
ax.hist(one_sample, bins=12, range=(0, 48), color=CATEGORICAL[1], edgecolor="white", linewidth=0.6, density=True)
ax.axvline(one_sample.mean(), color=INK_SECONDARY, linewidth=1.5, linestyle="--")
ax.set_title(f"② 單次樣本資料直方圖\n(n={N} 筆結帳時間)")
ax.set_xlabel("個別結帳時間（分鐘）")
ax.set_ylabel("密度")
ax.text(
    one_sample.mean() + 1, ax.get_ylim()[1] * 0.9,
    f"$\\bar x$ = {one_sample.mean():.1f}", color=INK_SECONDARY, fontsize=10,
)

# Panel 3: sampling distribution of Xbar across R repeated samples
ax = axes[2]
ax.hist(sample_means, bins=40, color=CATEGORICAL[2], edgecolor="white", linewidth=0.3, density=True)
xs = np.linspace(mu - 4 * se, mu + 4 * se, 300)
normal_pdf = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((xs - mu) / se) ** 2)
ax.plot(xs, normal_pdf, color=ACCENT, linewidth=2.0, label=f"CLT 近似\n$N({mu:.0f}, {se:.0f}^2)$")
ax.set_title(f"③ $\\bar X$ 的抽樣分配\n(重複 R={R:,} 次，每次 n={N})")
ax.set_xlabel("樣本平均結帳時間（分鐘）")
ax.set_ylabel("密度")
ax.legend(loc="upper right", fontsize=9)

fig.suptitle("三種常被混淆的直方圖：母體、單次樣本、$\\bar X$ 的抽樣分配", fontsize=13, y=1.03)
fig.tight_layout()

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "05-three-histograms.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(f"population mean={population.mean():.3f} sd={population.std():.3f}")
print(f"sample_means mean={sample_means.mean():.3f} sd={sample_means.std():.3f} (theory SE={se})")
