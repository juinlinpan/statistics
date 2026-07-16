"""Compare the MPG model on the original and back-transformed scales."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, INK_MUTED, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "16-mpg-model-comparison.png"


def main() -> None:
    apply_style()
    weight = np.linspace(2000, 3600, 400)
    original_mpg = 56.1 - 0.011644 * weight
    back_transformed_mpg = np.exp(4.5242 - 0.000501 * weight)

    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.plot(weight, original_mpg, color=CATEGORICAL[0], linestyle="--", label=r"原尺度：$56.1-0.011644Weight$")
    ax.plot(weight, back_transformed_mpg, color=CATEGORICAL[5], linestyle="-", label=r"反轉換：$e^{4.5242-0.000501Weight}$")
    ax.fill_between(
        weight,
        original_mpg,
        back_transformed_mpg,
        color=CATEGORICAL[2],
        alpha=0.14,
        hatch="//",
        edgecolor=CATEGORICAL[2],
        linewidth=0,
        label="同一 MPG 尺度上的預測差",
    )
    ax.set(
        title="先反轉換，兩個模型才在同一單位比較",
        xlabel="車重 Weight（磅）",
        ylabel="預測 MPG（英里／加侖）",
        xlim=(2000, 3600),
    )
    ax.legend(loc="upper right")
    fig.text(0.01, 0.01, "模型曲線使用投影片的 2,000–3,600 磅範圍；不含原始 12 筆觀察點。", color=INK_MUTED, fontsize=9)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
