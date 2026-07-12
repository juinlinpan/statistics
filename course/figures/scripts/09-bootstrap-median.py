# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 9, Section 5: non-parametric bootstrap distribution of a median.

Illustrates the chapter's opening motivating example ("為什麼要學這一章"):
40 customers' waiting times, and "樣本中位數有多不穩定". Since the chapter
does not give the actual 40 values, we construct a SIMULATED but
illustrative dataset consistent with the chapter's running waiting-time
context (right-skewed, exponential-like waiting times, echoing the
Exponential(lambda) example in Section 4).

Setup:
- Original sample: n=40 waiting times drawn once from Exponential(mean=5
  minutes), rounded to 1 decimal -- this is the "observed" dataset.
- Non-parametric bootstrap (Section 2.2): resample n=40 values with
  replacement from the original sample, B=5,000 times; compute the sample
  median each time.
- Plot the histogram of the B bootstrap replicate medians (Section 3),
  mark the original sample median with a vertical ACCENT line, and mark
  the 95% percentile bootstrap interval (Section 5) with vertical dashed
  BASELINE lines at the 2.5th/97.5th percentiles of the replicates.

Seeded with np.random.default_rng(42) for reproducibility.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, ACCENT, BASELINE

apply_style()

rng = np.random.default_rng(42)

n = 40
mean_wait = 5.0  # minutes, illustrative population mean

# "Observed" original sample (simulated once, then treated as fixed data).
original_sample = np.round(rng.exponential(scale=mean_wait, size=n), 1)
theta_hat = np.median(original_sample)

# Non-parametric bootstrap: resample with replacement, n=40 each time.
B = 5_000
boot_medians = np.empty(B)
for b in range(B):
    resample = rng.choice(original_sample, size=n, replace=True)
    boot_medians[b] = np.median(resample)

ci_lower, ci_upper = np.percentile(boot_medians, [2.5, 97.5])

fig, ax = plt.subplots(figsize=(7.5, 4.8))

ax.hist(boot_medians, bins=30, color=CATEGORICAL[0], alpha=0.85, edgecolor="none")

ax.axvline(theta_hat, color=ACCENT, linewidth=2.0,
           label=f"原始樣本中位數 $\\hat\\theta={theta_hat:.2f}$ 分鐘")
ax.axvline(ci_lower, color=BASELINE, linewidth=1.6, linestyle="--",
           label=f"95% percentile CI：[{ci_lower:.2f}, {ci_upper:.2f}] 分鐘")
ax.axvline(ci_upper, color=BASELINE, linewidth=1.6, linestyle="--")

ax.set_xlabel("Bootstrap 複本中位數（分鐘）")
ax.set_ylabel("次數（共 $B=5{,}000$ 份複本）")
ax.set_title("非參數 Bootstrap：40 位顧客等待時間中位數的複本分配")
ax.legend(loc="upper right", fontsize=9)

fig.tight_layout()
out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "09-bootstrap-median.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(f"theta_hat (original median) = {theta_hat:.3f} minutes")
print(f"95% percentile CI = [{ci_lower:.3f}, {ci_upper:.3f}] minutes")
