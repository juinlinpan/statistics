"""Shared matplotlib style for every course2 figure."""

import matplotlib.pyplot as plt

SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
BASELINE = "#c3c2b7"

CATEGORICAL = [
    "#2a78d6",
    "#1baf7a",
    "#eda100",
    "#008300",
    "#4a3aa7",
    "#e34948",
    "#e87ba4",
    "#eb6834",
]

SEQUENTIAL_BLUE = [
    "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b",
]

DIVERGING_LOW = "#2a78d6"
DIVERGING_MID = "#f0efec"
DIVERGING_HIGH = "#e34948"
ACCENT = "#e34948"


def apply_style() -> None:
    """Apply the validated light-background course figure style."""
    plt.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "text.color": INK_PRIMARY,
        "axes.labelcolor": INK_PRIMARY,
        "axes.edgecolor": BASELINE,
        "axes.titlecolor": INK_PRIMARY,
        "xtick.color": INK_MUTED,
        "ytick.color": INK_MUTED,
        "grid.color": GRIDLINE,
        "grid.linewidth": 1.0,
        "grid.linestyle": "-",
        "axes.grid": True,
        "axes.axisbelow": True,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.family": "sans-serif",
        "font.sans-serif": [
            "PingFang TC", "Heiti TC", "STHeiti", "Helvetica", "Arial", "DejaVu Sans",
        ],
        "axes.unicode_minus": False,
        "font.size": 11,
        "lines.linewidth": 2.0,
        "legend.frameon": False,
        "figure.dpi": 150,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
    })
