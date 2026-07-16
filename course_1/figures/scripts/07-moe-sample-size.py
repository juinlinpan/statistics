# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Illustrative curve: margin of error vs. sample size for a proportion.

This is a SCHEMATIC illustration (not observed data) of the relationship
discussed in Section 6 ("信心水準、涵蓋率與誤差範圍"): SE, and therefore the
margin of error, shrinks in proportion to 1/sqrt(n), so quadrupling n only
halves the margin of error.

Reuses the chapter's own support-rate example (Section 4): p_hat = 0.52,
z* = 1.96 for a 95% CI. MOE(n) = 1.96 * sqrt(0.52*0.48/n) is plotted over a
range of n, with the chapter's own n=400 example (MOE ~= 0.049) and its
4x point n=1600 (MOE about half) marked.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL

apply_style()

p_hat = 0.52
z_star = 1.96

n_grid = np.arange(50, 3001, 10)
moe = z_star * np.sqrt(p_hat * (1 - p_hat) / n_grid)

n_marks = [400, 1600]
moe_marks = [z_star * np.sqrt(p_hat * (1 - p_hat) / n) for n in n_marks]

fig, ax = plt.subplots(figsize=(7.5, 5.5))

ax.plot(n_grid, moe, color=CATEGORICAL[0], linewidth=2.2, zorder=2)

marker_color = CATEGORICAL[5]
ax.scatter(n_marks, moe_marks, color=marker_color, s=55, zorder=3, label="章節範例：n=400 與 4 倍樣本數 n=1600")

for n, m in zip(n_marks, moe_marks):
    ax.annotate(
        f"n={n}\nMOE≈{m:.3f}",
        xy=(n, m),
        xytext=(n + 120, m + 0.012),
        fontsize=9,
        ha="left",
    )

ax.plot([n_marks[0], n_marks[0]], [0, moe_marks[0]], color="#c3c2b7", linewidth=1.0, linestyle=":", zorder=1)
ax.plot([n_marks[1], n_marks[1]], [0, moe_marks[1]], color="#c3c2b7", linewidth=1.0, linestyle=":", zorder=1)

ax.set_xlabel("樣本數 n")
ax.set_ylabel("誤差範圍 MOE（比例，95% 信賴區間）")
ax.set_xlim(0, 3000)
ax.set_ylim(0, moe.max() * 1.1)
ax.set_title("樣本數與誤差範圍的關係：n 變 4 倍，MOE 約減半（$\\hat p=0.52$ 之示意）")
ax.legend(loc="upper right", fontsize=9)

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "07-moe-sample-size.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
for n, m in zip(n_marks, moe_marks):
    print(f"n={n}: MOE={m:.5f}")
