"""Visualize the Chemline observed counts and chi-square contributions."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import ACCENT, CATEGORICAL, INK_MUTED, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "12-chemline-bin-contributions.png"


def main() -> None:
    apply_style()

    labels = ["<55.10", "55.10–\n59.68", "59.68–\n63.01", "63.01–\n65.82", "65.82–\n68.42", "68.42–\n71.02", "71.02–\n73.83", "73.83–\n77.16", "77.16–\n81.74", ">81.74"]
    observed = np.array([5, 5, 9, 6, 2, 5, 2, 5, 5, 6], dtype=float)
    expected = np.full(10, 5.0)
    contributions = (observed - expected) ** 2 / expected
    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(11.2, 5.8))
    bars = ax.bar(
        x,
        observed,
        color=[ACCENT if value >= 1 else CATEGORICAL[0] for value in contributions],
        edgecolor="white",
        width=0.72,
        label="觀察次數",
    )
    ax.axhline(
        5,
        color=CATEGORICAL[4],
        linestyle="--",
        linewidth=2,
        label="每區期望次數 E=5",
    )
    ax.bar_label(bars, labels=[f"O={value:.0f}" for value in observed], padding=3, fontsize=9)

    for i, contribution in enumerate(contributions):
        if contribution > 0:
            ax.text(
                i,
                0.25,
                rf"貢獻 {contribution:.1f}",
                ha="center",
                va="bottom",
                rotation=90,
                color="white" if contribution >= 1 else INK_MUTED,
                fontsize=8.5,
                fontweight="bold",
            )

    ax.set_title("Chemline 常態適合度：十個區間如何累積卡方值")
    ax.set_xlabel("能力測驗分數區間")
    ax.set_ylabel("求職者人數")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 10.8)
    ax.legend(loc="upper right", ncols=2)
    ax.text(
        0.01,
        -0.24,
        r"觀察資料；紅色柱代表該區對總 $\chi^2=7.2$ 的貢獻至少為 1。",
        transform=ax.transAxes,
        color=INK_MUTED,
        fontsize=9,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
