# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 12, section 3 worked example: Benjamini-Hochberg step-up procedure.

Matches the chapter's worked example exactly (section 3, "例："): four sorted
p-values 0.005, 0.018, 0.030, 0.200 with q=0.05. BH thresholds (i/m)*q are
0.0125, 0.025, 0.0375, 0.05 for i=1..4. The largest passing rank is k=3
(p_(3)=0.030 <= 0.0375), so the first three ranked hypotheses are rejected
and the fourth (p=0.200) is not.

Plots sorted p-values by rank against the BH threshold line, highlighting
rejected points in ACCENT and the non-rejected point in CATEGORICAL[0].
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

m = 4
q = 0.05
ranks = np.arange(1, m + 1)
p_sorted = np.array([0.005, 0.018, 0.030, 0.200])
thresholds = (ranks / m) * q  # 0.0125, 0.025, 0.0375, 0.05

k = 3  # largest rank with p_(i) <= (i/m)*q, per the chapter's worked example
rejected = ranks <= k

fig, ax = plt.subplots(figsize=(7.5, 5))

# BH threshold line, extended slightly beyond the data for readability.
x_line = np.linspace(0.5, m + 0.5, 100)
ax.plot(x_line, (x_line / m) * q, color=INK_SECONDARY, linewidth=2.0,
        label=r"BH 門檻 $(i/m)q$，$q=0.05$")

colors = [ACCENT if r else CATEGORICAL[0] for r in rejected]
ax.scatter(ranks[rejected], p_sorted[rejected], color=ACCENT, s=90, zorder=5,
           label="拒絕（$p_{(i)}\\leq (i/m)q$）")
ax.scatter(ranks[~rejected], p_sorted[~rejected], color=CATEGORICAL[0], s=90, zorder=5,
           label="不拒絕")

for r, p, t in zip(ranks, p_sorted, thresholds):
    ax.annotate(f"$p_{{({r})}}={p:.3f}$", (r, p), textcoords="offset points",
                xytext=(10, 8), fontsize=9, color="#0b0b0b")

ax.axvline(k + 0.5, color=ACCENT, linewidth=1.0)
ax.text(k + 0.5, 0.19, "$k=3$\n(最大通過排名)", color=ACCENT, fontsize=9,
        ha="left", va="top")

ax.set_xticks(ranks)
ax.set_xlim(0.5, m + 0.5)
ax.set_ylim(0, 0.22)
ax.set_xlabel("排序後的排名 $i$")
ax.set_ylabel("p 值")
ax.set_title("Benjamini–Hochberg 階梯式判定：4 個排序後 p 值，$q=0.05$")
ax.legend(loc="upper left", fontsize=9)

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; thresholds={thresholds}, k={k}")
