# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Square-root law: SE(Xbar) = sigma / sqrt(n), using the chapter's checkout-time
sigma = 6 minutes (Section 5.3).

Marks n=36 (SE=1), n=144 (SE=0.5), n=324 (SE=1/3) to show diminishing returns:
quadrupling n only halves SE. This is a schematic/illustrative curve, not
observed data.
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

SIGMA = 6.0  # checkout-time population SD (Section 5.3 example)

n = np.linspace(4, 500, 500)
se = SIGMA / np.sqrt(n)

marks_n = [36, 144, 324]
marks_se = [SIGMA / np.sqrt(m) for m in marks_n]

fig, ax = plt.subplots(figsize=(7.5, 5))

ax.plot(n, se, color=CATEGORICAL[0], linewidth=2.2)

for m, s in zip(marks_n, marks_se):
    ax.plot([m], [s], marker="o", color=ACCENT, markersize=7, zorder=5)
    ax.plot([m, m], [0, s], color=INK_SECONDARY, linewidth=1.0, linestyle=":")
    ax.plot([0, m], [s, s], color=INK_SECONDARY, linewidth=1.0, linestyle=":")
    ax.annotate(
        f"n={m}\nSE={s:.2f}",
        xy=(m, s),
        xytext=(m + 15, s + 0.35),
        fontsize=9.5,
        color=INK_SECONDARY,
    )

ax.set_xlim(0, 500)
ax.set_ylim(0, SIGMA / np.sqrt(4) * 1.05)
ax.set_xlabel("樣本數 $n$")
ax.set_ylabel("標準誤 $SE(\\bar X)=\\sigma/\\sqrt{n}$（分鐘）")
ax.set_title("平方根律：樣本數 4 倍，SE 才減半（$\\sigma=6$ 分鐘）")

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "05-square-root-law.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(list(zip(marks_n, marks_se)))
