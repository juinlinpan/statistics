"""Show the responsiveness-versus-smoothing tradeoff for Chapter 17."""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import ACCENT, CATEGORICAL, INK_MUTED, apply_style  # noqa: E402


def trailing_ma(values: np.ndarray, k: int) -> np.ndarray:
    result = np.full(values.size, np.nan)
    for i in range(k, values.size):
        result[i] = np.mean(values[i-k:i])
    return result


def exp_smooth(values: np.ndarray, alpha: float) -> np.ndarray:
    result = np.full(values.size, np.nan)
    result[1] = values[0]
    for i in range(2, values.size):
        result[i] = alpha * values[i-1] + (1-alpha) * result[i-1]
    return result


apply_style()
values = np.array([17, 21, 19, 23, 18, 16, 20, 18, 22, 20, 15, 22,
                   31, 34, 31, 33, 28, 32, 30, 29, 34, 33], dtype=float)
t = np.arange(1, values.size + 1)

fig, ax = plt.subplots(figsize=(10.5, 5.4))
ax.plot(t, values, marker="o", color=CATEGORICAL[0], label="實際銷量")
ax.plot(t, trailing_ma(values, 3), color=CATEGORICAL[1], label="3 期移動平均")
ax.plot(t, trailing_ma(values, 6), color=CATEGORICAL[2], label="6 期移動平均")
ax.plot(t, exp_smooth(values, 0.2), color=CATEGORICAL[4], label=r"指數平滑 $\alpha=0.2$")
ax.axvline(12.5, color=ACCENT, linestyle="--", linewidth=1.5)
ax.text(12.7, 35.0, "第 13 期水準上移", color=ACCENT, va="top")
ax.annotate("短視窗反應快", xy=(14, trailing_ma(values, 3)[13]), xytext=(7, 34),
            arrowprops={"arrowstyle": "->", "color": INK_MUTED}, color=INK_MUTED)
ax.set(title="平滑程度與反應速度不能同時最大", xlabel="週", ylabel="銷量(千加侖)")
ax.set_xticks([1, 4, 8, 12, 13, 16, 20, 22])
ax.legend(ncol=2)
fig.tight_layout()
out = Path(__file__).resolve().parents[1] / "generated" / "ch17_smoothing_tradeoff.png"
fig.savefig(out)
plt.close(fig)
print(out)
