"""Visualize how MAE and MSE penalize forecast errors differently."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import ACCENT, CATEGORICAL, apply_style  # noqa: E402


apply_style()
error = np.linspace(-8, 8, 321)
absolute = np.abs(error)
squared = error**2

fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.3))
axes[0].plot(error, absolute, color=CATEGORICAL[0])
axes[0].scatter([-2, 2, -6, 6], [2, 2, 6, 6], color=ACCENT, zorder=3)
axes[0].set(title="MAE：錯 2 就付 2，錯 6 就付 6", xlabel="預測誤差 $e_t$",
            ylabel="絕對誤差 $|e_t|$")
axes[1].plot(error, squared, color=CATEGORICAL[4])
axes[1].scatter([-2, 2, -6, 6], [4, 4, 36, 36], color=ACCENT, zorder=3)
axes[1].set(title="MSE：大錯會被平方放大", xlabel="預測誤差 $e_t$",
            ylabel="平方誤差 $e_t^2$")
fig.suptitle("同樣是量預測失準，懲罰方式不同", fontsize=15, fontweight="bold")
fig.tight_layout()
out = Path(__file__).resolve().parents[1] / "generated" / "ch17_error_metrics.png"
fig.savefig(out)
plt.close(fig)
print(out)
