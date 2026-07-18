"""Reproduce the smartphone multiplicative decomposition used in Chapter 17."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import ACCENT, CATEGORICAL, INK_MUTED, apply_style  # noqa: E402


apply_style()
y = np.array([4.8, 4.1, 6.0, 6.5, 5.8, 5.2, 6.8, 7.4,
              6.0, 5.6, 7.5, 7.8, 6.3, 5.9, 8.0, 8.4])
t = np.arange(1, 17)
season = np.array([0.93, 0.84, 1.09, 1.14])
deseasonalized = y / season[(t - 1) % 4]
trend = 5.104 + 0.1476 * t

ma4 = np.convolve(y, np.ones(4) / 4, mode="valid")
cma = (ma4[:-1] + ma4[1:]) / 2
cma_t = np.arange(3, 15)

fig, axes = plt.subplots(2, 1, figsize=(10.4, 7.0), sharex=True)
axes[0].plot(t, y, marker="o", color=CATEGORICAL[0], label="原始銷量")
axes[0].plot(cma_t, cma, marker="s", color=ACCENT, label="四期中央移動平均")
axes[0].set(title="中央移動平均先壓低季節波動", ylabel="銷量(千支)")
axes[0].legend()
axes[1].plot(t, deseasonalized, marker="o", color=CATEGORICAL[1], label="去季節化銷量")
axes[1].plot(t, trend, color=CATEGORICAL[4], label=r"趨勢 $5.104+0.1476t$")
axes[1].fill_between(t, trend, deseasonalized, color=INK_MUTED, alpha=0.10)
axes[1].set(title="去掉固定季節倍率後，長期上升訊號更清楚", xlabel="季度期數",
            ylabel="去季節化銷量(千支)")
axes[1].set_xticks(t)
axes[1].legend()
fig.suptitle("乘法分解：原始值 = 趨勢 × 季節 × 不規則", fontsize=15, fontweight="bold")
fig.tight_layout()
out = Path(__file__).resolve().parents[1] / "generated" / "ch17_multiplicative_decomposition.png"
fig.savefig(out)
plt.close(fig)
print(out)
