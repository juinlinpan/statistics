"""Independent numerical checks for the Chapter 17 exam solutions."""

from __future__ import annotations

from math import fsum


def linear_trend(values: list[float]) -> tuple[float, float]:
    n = len(values)
    tbar = (n + 1) / 2
    ybar = fsum(values) / n
    b1 = fsum((i - tbar) * (y - ybar) for i, y in enumerate(values, 1)) / fsum(
        (i - tbar) ** 2 for i in range(1, n + 1)
    )
    return ybar - b1 * tbar, b1


def exp_forecasts(values: list[float], alpha: float) -> list[float]:
    forecasts = [values[0]]
    for actual in values[:-1]:
        forecasts.append(alpha * actual + (1 - alpha) * forecasts[-1])
    forecasts.append(alpha * values[-1] + (1 - alpha) * forecasts[-1])
    return forecasts


def trailing_forecasts(values: list[float], k: int) -> list[float]:
    return [fsum(values[i-k:i]) / k for i in range(k, len(values) + 1)]


def mse(actual: list[float], forecast: list[float]) -> float:
    return fsum((a - f) ** 2 for a, f in zip(actual, forecast)) / len(actual)


def decomposition(values: list[float], period: int = 4):
    moving = [fsum(values[i:i+period]) / period for i in range(len(values)-period+1)]
    centered = [(moving[i] + moving[i+1]) / 2 for i in range(len(moving)-1)]
    start = period // 2
    ratios = [[] for _ in range(period)]
    for offset, cma in enumerate(centered):
        index = start + offset
        ratios[index % period].append(values[index] / cma)
    raw = [fsum(group) / len(group) for group in ratios]
    factor = period / fsum(raw)
    adjusted = [x * factor for x in raw]
    return moving, centered, adjusted


def report(label: str, value) -> None:
    print(f"{label}: {value}")


if __name__ == "__main__":
    report("MC2", 0.3 * 61 + 0.7 * 58)
    report("MC12", 158.2 * 0.94 * 1.05 * 0.98)
    report("MC19", 16.23 + 0.52 * 114 + 0.37 * 112)
    for number, values, future in [
        (14, [12, 16, 17, 19, 18, 21, 22], [10]),
        (15, [6.3, 7.7, 8.0, 8.2, 8.8, 8.0], [10]),
        (18, [2, 3, 5, 4, 6, 8, 9, 9], [9]),
        (19, [195, 200, 250, 270, 320, 380, 440, 460, 500, 500], [11]),
        (25, [120, 132, 148, 152, 160, 175, 182, 190, 195, 205], [11, 12]),
        (27, [15.0, 16.2, 17.1, 18.1, 18.8, 19.2, 20.5], [8, 9, 10, 11, 12]),
    ]:
        b0, b1 = linear_trend(values)
        report(f"P{number} trend", (b0, b1, [b0 + b1 * t for t in future]))

    for number, values, alpha in [
        (5, [18, 23, 20, 16], 0.2),
        (6, [18, 25, 30, 40], 0.3),
        (16, [15, 16, 19, 18, 19, 20, 19, 22, 15, 21], 0.3),
        (17, [8, 3, 4, 5, 12, 10], 0.2),
        (22, [105, 90, 95, 110, 105, 100], 0.2),
        (24, [82, 80, 84, 83, 80, 79, 82], 0.2),
    ]:
        forecasts = exp_forecasts(values, alpha)
        report(f"P{number} exp", (forecasts, mse(values[1:], forecasts[1:-1])))

    p23 = [22, 24, 28, 24, 22, 24, 20, 26, 24, 28, 26]
    ma23 = trailing_forecasts(p23, 3)
    exp23 = exp_forecasts(p23, 0.4)
    report("P23", (ma23, mse(p23[3:], ma23[:-1]), exp23, mse(p23[1:], exp23[1:-1])))

    for number, values in [
        (20, [2.5, 1.5, 2.4, 1.6, 2.0, 1.4, 1.7, 1.9, 2.5, 2.0, 2.4, 2.1]),
        (26, [300, 240, 240, 290, 350, 300, 280, 320, 410, 400, 390, 410,
              490, 450, 440, 510, 540, 530, 520, 540]),
        (28, [150, 120, 160, 150, 150, 130, 180, 160, 170, 140, 200, 180,
              200, 150, 230, 200]),
        (31, [160, 180, 190, 170, 200, 210, 260, 230, 210, 240, 290, 260]),
    ]:
        moving, centered, seasonal = decomposition(values)
        report(f"P{number} decomposition", (moving, centered, seasonal))

    p29 = [10, 20, 25, 5, 10, 30, 35, 25, 20, 40, 35, 15, 20, 50, 45, 35]
    p29_s = [0.589, 1.351, 1.335, 0.726]
    p29_d = [y / p29_s[i % 4] for i, y in enumerate(p29)]
    p29_b0, p29_b1 = linear_trend(p29_d)
    p29_f = [(p29_b0 + p29_b1 * t) * p29_s[(t - 1) % 4] for t in range(17, 21)]
    report("P29", (p29_d, p29_b0, p29_b1, p29_f))
