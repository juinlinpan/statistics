"""Plot the Johnson Filtration dummy-variable model as parallel lines."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_SECONDARY, SURFACE, apply_style


apply_style()

months = np.linspace(0, 12, 200)
mechanical = 0.930 + 0.3876 * months
electrical = 2.193 + 0.3876 * months

fig, ax = plt.subplots(figsize=(8.2, 4.8))
ax.plot(months, mechanical, color=CATEGORICAL[0], linestyle="-", label="機械維修：0.930 + 0.3876 × 月數")
ax.plot(months, electrical, color=ACCENT, linestyle="--", label="電氣維修：2.193 + 0.3876 × 月數")

mark_x = 6
mechanical_at_mark = 0.930 + 0.3876 * mark_x
electrical_at_mark = 2.193 + 0.3876 * mark_x
ax.annotate(
    "",
    xy=(mark_x, electrical_at_mark),
    xytext=(mark_x, mechanical_at_mark),
    arrowprops={"arrowstyle": "<->", "color": INK_SECONDARY, "linewidth": 1.8},
)
ax.text(
    mark_x + 0.25,
    (mechanical_at_mark + electrical_at_mark) / 2,
    "固定月數時相差 1.263 小時",
    va="center",
    bbox={"facecolor": SURFACE, "edgecolor": "none", "pad": 2.5},
)

ax.set(xlabel="距上次服務月數", ylabel="估計平均維修時間(小時)", title="虛擬變數改變截距，不改變斜率")
ax.set_xlim(0, 12)
ax.set_ylim(0, 7.4)
ax.legend(loc="upper left")
fig.tight_layout()

output = Path(__file__).resolve().parents[1] / "generated" / "15-partial-slope-dummy.png"
output.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output)
plt.close(fig)
