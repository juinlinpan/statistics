"""Compare observed and expected counts in the beer preference example."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, INK_MUTED, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "12-beer-observed-expected.png"


def main() -> None:
    apply_style()

    categories = ["淡啤酒\n男性", "淡啤酒\n女性", "普通啤酒\n男性", "普通啤酒\n女性", "深色啤酒\n男性", "深色啤酒\n女性"]
    observed = np.array([51, 39, 56, 21, 25, 8], dtype=float)
    expected = np.array([59.40, 30.60, 50.82, 26.18, 21.78, 11.22])
    contributions = (observed - expected) ** 2 / expected

    x = np.arange(len(categories))
    width = 0.34

    fig, (ax, ax_contrib) = plt.subplots(
        2,
        1,
        figsize=(10.4, 7.2),
        sharex=True,
        gridspec_kw={"height_ratios": [2.1, 1], "hspace": 0.08},
    )

    observed_bars = ax.bar(
        x - width / 2,
        observed,
        width,
        color=CATEGORICAL[0],
        label="觀察次數 O",
    )
    expected_bars = ax.bar(
        x + width / 2,
        expected,
        width,
        facecolor="white",
        edgecolor=CATEGORICAL[5],
        linewidth=1.8,
        hatch="///",
        label="獨立時的期望次數 E",
    )
    ax.bar_label(observed_bars, labels=[f"{value:.0f}" for value in observed], padding=2, fontsize=9)
    ax.bar_label(expected_bars, labels=[f"{value:.2f}" for value in expected], padding=2, fontsize=9)
    ax.set_title("啤酒偏好 × 性別：觀察值與獨立假設的期望值")
    ax.set_ylabel("人數")
    ax.set_ylim(0, 68)
    ax.legend(loc="upper right", ncols=2)

    contribution_bars = ax_contrib.bar(
        x,
        contributions,
        width=0.58,
        color=[CATEGORICAL[5] if value >= 1 else CATEGORICAL[2] for value in contributions],
        edgecolor="white",
    )
    ax_contrib.bar_label(
        contribution_bars,
        labels=[f"{value:.2f}" for value in contributions],
        padding=2,
        fontsize=9,
    )
    ax_contrib.axhline(1, color=INK_MUTED, linestyle="--", linewidth=1.2)
    ax_contrib.set_ylabel(r"各格 $\chi^2$ 貢獻")
    ax_contrib.set_xlabel("啤酒偏好與性別的六個格子")
    ax_contrib.set_xticks(x, categories)
    ax_contrib.set_ylim(0, 2.75)
    ax_contrib.text(
        0.01,
        -0.35,
        r"觀察資料；六格貢獻合計為 $\chi^2=6.45$。",
        transform=ax_contrib.transAxes,
        color=INK_MUTED,
        fontsize=9,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
