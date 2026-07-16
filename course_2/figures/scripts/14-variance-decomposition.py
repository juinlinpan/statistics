"""Visualize SST = SSR + SSE for the Armand's Pizza example."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import CATEGORICAL, INK_PRIMARY, SURFACE, apply_style


apply_style()

sst = 15_730
ssr = 14_200
sse = 1_530
assert sst == ssr + sse

fig, ax = plt.subplots(figsize=(8.2, 4.2))

ax.barh(
    1,
    sst,
    height=0.48,
    facecolor=SURFACE,
    edgecolor=INK_PRIMARY,
    linewidth=1.6,
    label="SST：總變異",
)
ax.barh(
    0,
    ssr,
    height=0.48,
    color=CATEGORICAL[0],
    edgecolor=INK_PRIMARY,
    hatch="///",
    linewidth=0.8,
    label="SSR：迴歸線解釋的變異",
)
ax.barh(
    0,
    sse,
    left=ssr,
    height=0.48,
    color=CATEGORICAL[2],
    edgecolor=INK_PRIMARY,
    hatch="xx",
    linewidth=0.8,
    label="SSE：尚未解釋的殘差變異",
)

ax.text(sst / 2, 1, "SST = 15,730（100%）", ha="center", va="center", color=INK_PRIMARY)
ax.text(ssr / 2, 0, "SSR = 14,200\n90.27%", ha="center", va="center", color=SURFACE)
ax.annotate(
    "SSE = 1,530\n9.73%",
    xy=(ssr + sse / 2, 0),
    xytext=(13_200, -0.72),
    ha="center",
    va="center",
    arrowprops={"arrowstyle": "->", "color": INK_PRIMARY},
)

ax.set_title("Armand's Pizza：總變異拆成解釋與殘差兩部分")
ax.set_xlabel("平方和（千美元²）")
ax.set_yticks([0, 1], ["SSR + SSE", "SST"])
ax.set_xlim(0, 16_600)
ax.set_ylim(-1.05, 1.55)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=3)

output = Path(__file__).resolve().parents[1] / "generated" / "14-variance-decomposition.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)

