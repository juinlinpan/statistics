"""Visualize the Tyler price-by-advertising interaction means."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, INK_MUTED, INK_PRIMARY, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "16-interaction-price-advertising.png"


def main() -> None:
    apply_style()
    price = np.array([2.00, 2.50, 3.00])
    sales_50 = np.array([461, 364, 332])
    sales_100 = np.array([808, 646, 375])
    gains = sales_100 - sales_50

    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.plot(price, sales_50, color=CATEGORICAL[0], linestyle="--", marker="o", markersize=7, label="廣告 50,000 美元")
    ax.plot(price, sales_100, color=CATEGORICAL[5], linestyle="-", marker="s", markersize=7, label="廣告 100,000 美元")
    for x, low, high, gain in zip(price, sales_50, sales_100, gains):
        ax.vlines(x, low, high, color=INK_MUTED, linestyle=":", linewidth=1.5)
        ax.text(x + 0.025, (low + high) / 2, f"增益 {gain}", va="center", color=INK_PRIMARY, fontsize=10)
    ax.set(
        title="兩條線不平行：廣告效果會隨價格改變",
        xlabel="單位售價 Price（美元）",
        ylabel="平均銷售量 Sales（千單位）",
        xticks=price,
        xlim=(1.9, 3.15),
        ylim=(250, 860),
    )
    ax.legend(loc="upper right")
    fig.text(0.01, 0.01, "觀察資料的六個組合平均數；垂直虛線標出同一價格下增加廣告的平均增益。", color=INK_MUTED, fontsize=9)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
