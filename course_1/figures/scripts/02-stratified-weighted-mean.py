# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Bar chart for the chapter's three-department stratified weighted mean example (題 2-5).

Data: three departments make up 50%, 30%, 20% of the company; their sample
mean commute times are 20, 25, 30 minutes respectively. Bar widths encode
each department's population weight, so the visual area under each bar
reflects how much it should count toward the company-wide average.

Stratified (weighted) estimate: 0.50(20) + 0.30(25) + 0.20(30) = 23.5 minutes.
Naive (unweighted) average of the three sample means: (20+25+30)/3 = 25 minutes.
The naive average overestimates because it treats the largest department
(50% of staff, shortest commute) as if it were only one-third of the company.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

labels = ["部門 A\n(占比 50%)", "部門 B\n(占比 30%)", "部門 C\n(占比 20%)"]
weights = [0.50, 0.30, 0.20]
means = [20, 25, 30]
colors = [CATEGORICAL[0], CATEGORICAL[1], CATEGORICAL[2]]

weighted_mean = sum(w * m for w, m in zip(weights, means))
naive_mean = sum(means) / len(means)

fig, ax = plt.subplots(figsize=(7.5, 4.8))

x = 0.0
xticks = []
for w, m, c, lab in zip(weights, means, colors, labels):
    ax.bar(x, m, width=w, align="edge", color=c, edgecolor="white", linewidth=1.2)
    ax.text(x + w / 2, m + 0.6, f"{m} 分鐘", ha="center", va="bottom", fontsize=10, color=INK_SECONDARY)
    xticks.append((x + w / 2, lab))
    x += w

ax.axhline(weighted_mean, color=ACCENT, linewidth=2.0, linestyle="-", zorder=5)
ax.axhline(naive_mean, color=INK_SECONDARY, linewidth=2.0, linestyle="--", zorder=5)

ax.text(1.01, weighted_mean, f"分層加權平均 = {weighted_mean:.1f}", color=ACCENT,
        fontsize=10, va="center", ha="left", transform=ax.get_yaxis_transform())
ax.text(1.01, naive_mean, f"未加權平均 = {naive_mean:.0f}", color=INK_SECONDARY,
        fontsize=10, va="center", ha="left", transform=ax.get_yaxis_transform())

ax.set_xticks([t[0] for t in xticks])
ax.set_xticklabels([t[1] for t in xticks])
ax.set_xlim(0, 1)
ax.set_ylim(0, 34)
ax.set_ylabel("樣本平均通勤時間（分鐘）")
ax.set_title("分層加權平均 vs. 未加權平均：長條寬度代表各部門母體占比")

fig.subplots_adjust(right=0.8)
fig.savefig("../generated/02-stratified-weighted-mean.png")
print("Saved ../generated/02-stratified-weighted-mean.png")
print(f"weighted_mean={weighted_mean}, naive_mean={naive_mean}")
