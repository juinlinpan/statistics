"""Plot the right-tail rejection rule for the chapter 12 car example."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_MUTED, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "12-right-tail-rejection.png"


def main() -> None:
    apply_style()

    df = 2
    alpha = 0.05
    critical = 5.991
    observed = 7.89
    p_value = np.exp(-observed / 2)  # df=2 的卡方右尾機率

    x = np.linspace(0, 13, 800)
    density = 0.5 * np.exp(-x / 2)  # df=2 的卡方密度

    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.plot(x, density, color=CATEGORICAL[0], label=r"$df=2$ 的卡方分配")
    ax.fill_between(
        x,
        density,
        where=x >= critical,
        color=ACCENT,
        alpha=0.25,
        hatch="///",
        label=r"拒絕域：右尾 $\alpha=0.05$",
    )
    ax.axvline(critical, color=ACCENT, linestyle="--", linewidth=2)
    ax.axvline(observed, color=CATEGORICAL[4], linestyle="-.", linewidth=2.2)
    ax.scatter(
        [observed],
        [0.5 * np.exp(-observed / 2)],
        color=CATEGORICAL[4],
        marker="D",
        s=55,
        zorder=3,
        label=rf"觀察值 $\chi^2={observed:.2f}$",
    )

    ax.annotate(
        "臨界值 5.991",
        xy=(critical, 0.024),
        xytext=(critical - 2.4, 0.11),
        arrowprops={"arrowstyle": "->", "color": ACCENT},
        color=ACCENT,
    )
    ax.annotate(
        f"觀察值落在拒絕域\np ≈ {p_value:.4f}",
        xy=(observed, 0.5 * np.exp(-observed / 2)),
        xytext=(8.8, 0.10),
        arrowprops={"arrowstyle": "->", "color": CATEGORICAL[4]},
        color=CATEGORICAL[4],
        ha="left",
    )

    ax.set_title("汽車品牌忠誠度：卡方檢定只看右尾")
    ax.set_xlabel(r"卡方統計量 $\chi^2$")
    ax.set_ylabel("機率密度")
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 0.53)
    ax.legend(loc="upper right")
    ax.text(
        0.01,
        -0.18,
        "示意依據：講義汽車例題，df=2、α=0.05。",
        transform=ax.transAxes,
        color=INK_MUTED,
        fontsize=9,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
