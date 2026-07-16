# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Schematic diagram of regression toward the mean for Section 3.1.

This illustrates the chapter's standardized-prediction formula
(zhat_y = r * z_x) using the chapter's own worked numbers: r = 0.70, and a
case where x is 2 SD above its mean, so the predicted y is only
r * 2 = 1.4 SD above its mean (chapter text: "某人的 x 高於平均 2 個 SD，
則預測的 y 高於平均 0.70×2=1.4 個 SD").

This panel is a conceptual line diagram, not a data scatter: it plots the
45-degree "no regression to the mean" reference line z_y = z_x against the
actual standardized prediction line z_y = r * z_x for r = 0.70, and marks the
specific (2, 1.4) example from the text to show the predicted value sits
closer to 0 (the mean) than the observed x value did, whenever |r| < 1. No
raw data is simulated for this figure.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

R = 0.70
z = np.linspace(-3, 3, 200)

fig, ax = plt.subplots(figsize=(6.8, 6.0))

ax.plot(z, z, color=INK_SECONDARY, linewidth=2.0, linestyle="--",
        label="$z_y=z_x$（若無平均值迴歸）")
ax.plot(z, R * z, color=ACCENT, linewidth=2.4,
        label=f"$z_{{\\hat y}}=r\\,z_x$，$r={R:.2f}$")

zx0 = 2.0
zy0 = R * zx0
ax.plot([zx0, zx0], [0, zy0], color=INK_SECONDARY, linewidth=1.1, linestyle=":")
ax.plot([0, zx0], [zy0, zy0], color=INK_SECONDARY, linewidth=1.1, linestyle=":")
ax.scatter([zx0], [zx0], s=55, color=CATEGORICAL[0], zorder=5,
           edgecolor="white", linewidth=0.8, label="觀測 $z_x=2.0$")
ax.scatter([zx0], [zy0], s=55, color=ACCENT, zorder=5,
           edgecolor="white", linewidth=0.8, label=f"預測 $z_{{\\hat y}}={zy0:.1f}$")

ax.annotate("", xy=(zx0, zy0), xytext=(zx0, zx0),
            arrowprops=dict(arrowstyle="-|>", color=INK_SECONDARY, lw=1.4))
ax.text(zx0 + 0.08, (zx0 + zy0) / 2, "預測值向平均\n（0）收縮",
        fontsize=9.5, color=INK_SECONDARY, va="center")

ax.axhline(0, color="#d8d7cf", linewidth=1.0, zorder=0)
ax.axvline(0, color="#d8d7cf", linewidth=1.0, zorder=0)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("$x$ 的標準分數 $z_x$（距平均幾個標準差）")
ax.set_ylabel("預測 $y$ 的標準分數 $z_{\\hat y}$")
ax.set_title("平均值迴歸示意：$r=0.70$ 時預測值較觀測值更靠近平均")
ax.legend(loc="upper left", fontsize=9)

fig.tight_layout()
out_path = Path(__file__).resolve().parent.parent / "generated" / "06-regression-to-mean.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
print(f"zx0={zx0}, zy0={zy0}")
