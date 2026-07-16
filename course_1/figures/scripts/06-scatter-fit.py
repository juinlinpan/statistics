# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Scatterplot with fitted least-squares line for the chapter's worked example
(類題 m06-line-calc-01｜由相關求迴歸線並做預測).

The chapter gives only summary statistics for this example, not raw data:
xbar=4 hours, sx=2 hours, ybar=70 points, sy=8 points, r=0.50, which imply
b1 = r*(sy/sx) = 2 points/hour and b0 = ybar - b1*xbar = 62 points, so
yhat = 62 + 2x and yhat(7) = 76.

To draw a scatterplot consistent with exactly these summary statistics (not
literal raw observations), we synthesize n points via a Gram-Schmidt
construction: draw two independent standard-normal vectors, standardize the
first to sample mean 0 / sd 1 (x_std), orthogonalize the second against it in
the sample sense and standardize the residual (e_std), then set
y_std = r*x_std + sqrt(1-r^2)*e_std. This makes the *sample* correlation of
(x_std, y_std) equal to r exactly (up to floating point), by construction:
cov(x_std,y_std) = r*var(x_std) + sqrt(1-r^2)*cov(x_std,e_std) = r (since
e_std is exactly orthogonal to x_std in the sample), and var(y_std) =
r^2 + (1-r^2) = 1. Rescaling x = xbar + sx*x_std and y = ybar + sy*y_std then
reproduces xbar, sx, ybar, sy exactly too, so the least-squares line fit to
this synthetic cloud reproduces b1=2, b0=62 exactly (up to floating point).

This is illustrative simulated data consistent with the chapter's summary
statistics, not literal raw observations.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

# Target summary statistics from the chapter's worked example.
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

print(f"sample: xbar={x.mean():.4f}, sx={x.std(ddof=1):.4f}, "
      f"ybar={y.mean():.4f}, sy={y.std(ddof=1):.4f}, r={r_actual:.6f}")
print(f"fitted line: b0={b0:.4f}, b1={b1:.4f}")
print(f"prediction at x=7: {b0 + b1 * 7:.4f}")

fig, ax = plt.subplots(figsize=(7.5, 5.2))

ax.scatter(x, y, s=42, color=CATEGORICAL[0], alpha=0.85,
           edgecolor="white", linewidth=0.6, zorder=3, label="模擬資料點")

x_line = np.array([0, 8.5])
ax.plot(x_line, b0 + b1 * x_line, color=ACCENT, linewidth=2.4, zorder=4,
        label=f"最小平方法迴歸線 $\\hat y={b0:.0f}+{b1:.0f}x$")

# Highlight the chapter's prediction at x = 7.
x_pred, y_pred = 7.0, b0 + b1 * 7.0
ax.plot([x_pred, x_pred], [0, y_pred], color=INK_SECONDARY, linewidth=1.2,
        linestyle="--", zorder=2)
ax.plot([0, x_pred], [y_pred, y_pred], color=INK_SECONDARY, linewidth=1.2,
        linestyle="--", zorder=2)
ax.scatter([x_pred], [y_pred], s=70, color=ACCENT, zorder=5,
           edgecolor="white", linewidth=0.8)
ax.annotate(f"x=7 小時 → 預測 $\\hat y$={y_pred:.0f} 分",
            xy=(x_pred, y_pred), xytext=(x_pred - 3.6, y_pred + 6),
            fontsize=10, color=INK_SECONDARY,
            arrowprops=dict(arrowstyle="-", color=INK_SECONDARY, lw=0.8))

ax.set_xlim(0, 8.5)
ax.set_ylim(40, 95)
ax.set_xlabel("每週練習題時數 x（小時）")
ax.set_ylabel("統計測驗分數 y（分）")
ax.set_title("練習時數與測驗分數：散佈圖與最小平方法迴歸線")
ax.legend(loc="upper left", fontsize=9.5)

fig.tight_layout()
out_path = Path(__file__).resolve().parent.parent / "generated" / "06-scatter-fit.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
