# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 10, Section 10.3 worked example: chi-square goodness-of-fit test.

A company claims customer-service case sources split 50% phone / 30% email /
20% instant message. A random sample of 200 cases on one day gave observed
counts 120, 50, 30. Under H0, expected counts are 200*0.50=100, 200*0.30=60,
200*0.20=40.

Per-cell contributions (matches chapter text exactly):
  (120-100)^2/100 = 4
  (50-60)^2/60    ~= 1.67
  (30-40)^2/40    = 2.50
chi-square ~= 8.17, df = 2, right-tail p ~= 0.017 -> reject H0 at alpha=0.05.

This figure shows observed vs. expected counts per category so the reader can
see, before the arithmetic, which category (phone) drives most of the
discrepancy.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL, SURFACE, INK_SECONDARY

apply_style()

categories = ["電話", "電子郵件", "即時訊息"]
observed = [120, 50, 30]
expected = [100, 60, 40]

x = np.arange(len(categories))
width = 0.36

fig, ax = plt.subplots(figsize=(7.5, 4.8))

bars_obs = ax.bar(
    x - width / 2 - 0.01, observed, width=width,
    color=CATEGORICAL[0], edgecolor=SURFACE, linewidth=1.2,
    label="觀察次數 $O$（實際 200 件抽查）",
)
bars_exp = ax.bar(
    x + width / 2 + 0.01, expected, width=width,
    color=CATEGORICAL[0], alpha=0.35, hatch="///",
    edgecolor=CATEGORICAL[0], linewidth=1.2,
    label="期望次數 $E$（$H_0$：50%／30%／20%）",
)

for bars in (bars_obs, bars_exp):
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, h + 2, f"{h:.0f}",
                ha="center", va="bottom", fontsize=10, color=INK_SECONDARY)

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("案件數（件）")
ax.set_ylim(0, 135)
ax.set_title("客服案件來源：觀察次數與期望次數比較")
ax.legend(loc="upper right", fontsize=9.5)

fig.tight_layout()

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "10-customer-service-gof.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
