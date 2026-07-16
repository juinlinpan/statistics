"""Shared matplotlib style for every course figure.

Every figure script imports this module and calls `apply_style()` before
plotting, then uses the color constants below instead of matplotlib defaults.
This keeps every figure across all 12 chapters visually consistent.

Colors are the validated categorical/sequential/diverging palette from the
project's dataviz skill (light-mode instance; these are static images, not
theme-aware web charts, so only one mode is needed).
"""

import matplotlib.pyplot as plt

SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
BASELINE = "#c3c2b7"

# Fixed-order categorical slots. Assign in this order across series within a
# single figure; never cycle past 8, never assign by rank/sort order.
CATEGORICAL = [
    "#2a78d6",  # 1 blue
    "#1baf7a",  # 2 aqua
    "#eda100",  # 3 yellow
    "#008300",  # 4 green
    "#4a3aa7",  # 5 violet
    "#e34948",  # 6 red
    "#e87ba4",  # 7 magenta
    "#eb6834",  # 8 orange
]

# Single-hue sequential ramp (magnitude), light -> dark.
SEQUENTIAL_BLUE = [
    "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b",
]

# Diverging pair (polarity), neutral midpoint reads as "nothing".
DIVERGING_LOW = "#2a78d6"
DIVERGING_MID = "#f0efec"
DIVERGING_HIGH = "#e34948"

# Reserve red (categorical slot 6) as the shared "highlight/observed value"
# accent across all chapters (e.g. a vertical line marking an observed
# statistic on a null distribution) so its meaning stays consistent.
ACCENT = "#e34948"


def apply_style() -> None:
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
        "font.sans-serif": ["PingFang TC", "Heiti TC", "STHeiti", "Helvetica", "Arial", "DejaVu Sans"],
        "axes.unicode_minus": False,
        "font.size": 11,
        "lines.linewidth": 2.0,
        "legend.frameon": False,
        "figure.dpi": 150,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
    })
