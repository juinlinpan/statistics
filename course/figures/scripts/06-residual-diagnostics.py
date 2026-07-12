# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Two-panel residual-plot comparison for Section 6 (殘差圖：模型留下了什麼？).

Left panel: residuals (e = y - yhat) vs x from the same synthetic
practice-hours / test-score data used in 06-scatter-fit.py (xbar=4, sx=2,
ybar=70, sy=8, r=0.50, so b1=2, b0=62). Residuals scatter with no systematic
pattern and roughly constant vertical spread -- the "good, boring" residual
plot the chapter describes in 6.1.

Right panel: a separate, clearly-labeled illustrative (non-chapter-data)
example built to fan out as x increases, illustrating the funnel-shaped
heteroscedasticity pattern described in 6.2 (residual spread growing from
about +/-2 at small x to about +/-20 at large x, matching the chapter's own
"若 x 小時預測誤差約 ±2，而 x 大時誤差約 ±20" language). This panel is
schematic/simulated only, not tied to the chapter's summary statistics.

Both panels use the same synthetic-data convention as other chapter-06
figures: simulated points consistent with a stated pattern, not literal raw
observations.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY, GRIDLINE

apply_style()

# --- Left panel: residuals from the chapter's practice-hours example -------
XBAR, SX, YBAR, SY, R = 4.0, 2.0, 70.0, 8.0, 0.50
N = 24
SEED = 21

rng = np.random.default_rng(SEED)
z1 = rng.standard_normal(N)
z2 = rng.standard_normal(N)

x_std = (z1 - z1.mean()) / z1.std(ddof=1)
z2c = z2 - z2.mean()
proj_coef = np.sum(z2c * x_std) / np.sum(x_std**2)
e = z2c - proj_coef * x_std
e_std = (e - e.mean()) / e.std(ddof=1)
y_std = R * x_std + np.sqrt(1 - R**2) * e_std

x = XBAR + SX * x_std
y = YBAR + SY * y_std

r_actual = np.corrcoef(x, y)[0, 1]
b1 = r_actual * (y.std(ddof=1) / x.std(ddof=1))
b0 = y.mean() - b1 * x.mean()
resid = y - (b0 + b1 * x)

print(f"left panel: b0={b0:.4f}, b1={b1:.4f}, residual mean={resid.mean():.2e}")

# --- Right panel: illustrative funnel-shaped heteroscedastic example -------
rng2 = np.random.default_rng(7)
n2 = 60
x2 = np.linspace(1, 10, n2)
# error SD grows roughly linearly with x, from ~2 at x=1 to ~20 at x=10
sd2 = 2 + (20 - 2) * (x2 - 1) / (10 - 1)
resid2 = rng2.normal(loc=0.0, scale=sd2)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8), sharey=False)

ax1, ax2 = axes

ax1.axhline(0, color=GRIDLINE, linewidth=1.4, zorder=1)
ax1.scatter(x, resid, s=40, color=CATEGORICAL[0], alpha=0.85,
            edgecolor="white", linewidth=0.5, zorder=3)
ax1.set_xlabel("每週練習題時數 x（小時）")
ax1.set_ylabel("殘差 e = y − ŷ（分）")
ax1.set_title("(a) 練習時數範例：無明顯型態，寬度大致一致")
ax1.set_ylim(-16, 16)

ax2.axhline(0, color=GRIDLINE, linewidth=1.4, zorder=1)
ax2.scatter(x2, resid2, s=32, color=ACCENT, alpha=0.75,
            edgecolor="white", linewidth=0.4, zorder=3)
ax2.plot(x2, 2 * sd2, color=INK_SECONDARY, linewidth=1.2, linestyle="--", zorder=2)
ax2.plot(x2, -2 * sd2, color=INK_SECONDARY, linewidth=1.2, linestyle="--", zorder=2,
          label="約 ±2 個標準差包絡線")
ax2.set_xlabel("解釋變數 x（示意，非本章資料）")
ax2.set_ylabel("殘差 e（示意單位）")
ax2.set_title("(b) 示意範例：漏斗形，不等變異")
ax2.legend(loc="upper left", fontsize=9)

fig.suptitle("殘差圖比較：無異狀 vs. 不等變異（漏斗形）", y=1.02, fontsize=13)
fig.tight_layout()
out_path = Path(__file__).resolve().parent.parent / "generated" / "06-residual-diagnostics.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
