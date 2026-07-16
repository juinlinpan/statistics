"""Show the Jefe residual sequence and its Durbin-Watson decision."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _style import CATEGORICAL, GRIDLINE, INK_MUTED, INK_PRIMARY, apply_style


OUTPUT = Path(__file__).resolve().parents[1] / "generated" / "16-durbin-watson-jefe.png"


def main() -> None:
    apply_style()
    years = np.arange(1, 21)
    residuals = np.array([
        -0.79, -0.81, -0.84, -0.50, -0.38, -0.18, 0.10, 0.22, 0.66, 0.63,
        0.63, 0.35, 0.41, 0.55, 0.59, 0.08, 0.01, 0.40, -0.23, -0.88,
    ])
    numerator = np.sum(np.diff(residuals) ** 2)
    denominator = np.sum(residuals**2)
    dw = numerator / denominator
    d_l = 1.20
    d_u = 1.41

    fig, (ax_resid, ax_dw) = plt.subplots(2, 1, figsize=(9, 7.2), gridspec_kw={"height_ratios": [3, 1.35]})
    ax_resid.axhline(0, color=INK_PRIMARY, linewidth=1.2)
    ax_resid.plot(years, residuals, color=CATEGORICAL[0], linestyle="-", marker="o", markersize=5.5, label="Jefe 殘差")
    ax_resid.fill_between(years, 0, residuals, where=residuals >= 0, color=CATEGORICAL[0], alpha=0.12)
    ax_resid.fill_between(years, 0, residuals, where=residuals < 0, color=CATEGORICAL[5], alpha=0.12, hatch="//")
    ax_resid.set(
        title="相鄰殘差長時間同號，差值通常很小",
        xlabel="年份 Year",
        ylabel="殘差（百萬美元）",
        xticks=np.arange(1, 21),
        xlim=(0.5, 20.5),
        ylim=(-1.02, 0.82),
    )
    ax_resid.legend(loc="upper right")

    ax_dw.axvspan(0, d_l, color=CATEGORICAL[5], alpha=0.20, hatch="//")
    ax_dw.axvspan(d_l, d_u, color=CATEGORICAL[2], alpha=0.24, hatch="..")
    ax_dw.axvspan(d_u, 4, color=CATEGORICAL[1], alpha=0.18)
    ax_dw.axvline(d_l, color=INK_MUTED, linestyle="--")
    ax_dw.axvline(d_u, color=INK_MUTED, linestyle="--")
    ax_dw.scatter([dw], [0.58], color=INK_PRIMARY, marker="v", s=85, zorder=5)
    ax_dw.annotate(f"d = {dw:.3f}", xy=(dw, 0.58), xytext=(0.58, 0.82), arrowprops={"arrowstyle": "->", "color": INK_MUTED}, color=INK_PRIMARY)
    ax_dw.text(d_l / 2, 0.17, "有正自相關證據", ha="center", fontsize=10)
    ax_dw.text((d_l + d_u) / 2, 0.17, "無法\n判定", ha="center", fontsize=9)
    ax_dw.text((d_u + 4) / 2, 0.17, "沒有正自相關證據", ha="center", fontsize=10)
    ax_dw.set(
        title=r"正自相關單尾判斷：$n=20$、1 個自變數、$d_L=1.20$、$d_U=1.41$",
        xlabel="Durbin–Watson 統計量 d",
        xlim=(0, 4),
        ylim=(0, 1),
        yticks=[],
    )
    ax_dw.grid(axis="x", color=GRIDLINE)
    fig.text(0.01, 0.01, f"觀察資料；由表列殘差重算：分子 {numerator:.4f}、分母 {denominator:.4f}、d={dw:.3f}。", color=INK_MUTED, fontsize=9)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT)
    plt.close(fig)


if __name__ == "__main__":
    main()
