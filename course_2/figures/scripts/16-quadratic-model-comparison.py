"""Compare the Reynolds first- and second-order fitted equations."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "16-quadratic-model-comparison.png"


def main() -> None:
    apply_style()
    months = np.linspace(0, 120, 400)
    linear_sales = 111.2 + 2.377 * months
    quadratic_sales = 45.3 + 6.34 * months - 0.03449 * months**2
    turning_month = 6.34 / (2 * 0.03449)
    turning_sales = 45.3 + 6.34 * turning_month - 0.03449 * turning_month**2

    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.plot(months, linear_sales, color=CATEGORICAL[0], linestyle="--", label=r"一階：$111.2+2.377Months$")
    ax.plot(months, quadratic_sales, color=CATEGORICAL[5], linestyle="-", label=r"二階：$45.3+6.34Months-0.03449Months^2$")
    ax.scatter([turning_month], [turning_sales], s=58, color=INK_PRIMARY, marker="o", zorder=4)
    ax.annotate(
        f"二階模型約在 {turning_month:.1f} 月轉折",
        xy=(turning_month, turning_sales),
        xytext=(58, 300),
        arrowprops={"arrowstyle": "->", "color": INK_MUTED},
        color=INK_PRIMARY,
    )
    ax.set(
        title="直線模型看不見『效果逐漸變小』",
        xlabel="任職月數 Months（月）",
        ylabel="預測銷售量 Sales（台）",
        xlim=(0, 120),
    )
    ax.legend(loc="lower right")
    fig.text(0.01, 0.01, "模型方程式示意；0–120 月用來呈現兩種形狀，不代表原始 15 筆觀察值。", color=INK_MUTED, fontsize=9)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
