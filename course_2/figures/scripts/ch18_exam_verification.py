"""Independent numerical checks for the Chapter 18 question set.

This script is intentionally separate from the learner-facing chapter.  It prints
the statistics used in the worked solutions and never reads an answer key.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import comb, sqrt

import numpy as np
from scipy import stats


def sign_test(plus: int, minus: int, alternative: str = "two-sided") -> dict[str, float]:
    """Return exact and continuity-corrected normal sign-test results."""
    n = plus + minus
    low = min(plus, minus)
    if alternative == "two-sided":
        exact = min(1.0, 2 * stats.binom.cdf(low, n, 0.5))
        z = (abs(plus - n / 2) - 0.5) / sqrt(n / 4)
        normal = 2 * stats.norm.sf(z)
    elif alternative == "greater":
        exact = stats.binom.sf(plus - 1, n, 0.5)
        z = (plus - 0.5 - n / 2) / sqrt(n / 4)
        normal = stats.norm.sf(z)
    else:
        exact = stats.binom.cdf(plus, n, 0.5)
        z = (plus + 0.5 - n / 2) / sqrt(n / 4)
        normal = stats.norm.cdf(z)
    return {"n": n, "mu": n / 2, "sigma": sqrt(n / 4), "z_cc": z,
            "p_exact": float(exact), "p_normal_cc": float(normal)}


def rank_sum(x: list[float], y: list[float]) -> dict[str, float]:
    """Course-formula MWW check, plus SciPy's tie-aware asymptotic check."""
    n1, n2 = len(x), len(y)
    ranks = stats.rankdata(np.r_[x, y], method="average")
    w = float(ranks[:n1].sum())
    mu = n1 * (n1 + n2 + 1) / 2
    sigma = sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    z_cc = (abs(w - mu) - 0.5) / sigma
    scipy_result = stats.mannwhitneyu(x, y, alternative="two-sided", method="asymptotic")
    return {"W": w, "mu": mu, "sigma_course": sigma, "z_cc": z_cc,
            "p_course_cc": float(2 * stats.norm.sf(z_cc)),
            "p_scipy_tie_aware": float(scipy_result.pvalue)}


def signed_rank(before: list[float], after: list[float], alternative: str) -> dict[str, float]:
    """Check signed ranks using after-before and an exact/permutation calculation."""
    differences = np.asarray(after, dtype=float) - np.asarray(before, dtype=float)
    nonzero = differences[differences != 0]
    ranks = stats.rankdata(abs(nonzero), method="average")
    t_plus = float(ranks[nonzero > 0].sum())
    t_minus = float(ranks[nonzero < 0].sum())
    permutation_values = [
        sum(rank for rank, is_positive in zip(ranks, signs) if is_positive)
        for signs in product((False, True), repeat=len(ranks))
    ]
    lower = sum(value <= t_plus + 1e-12 for value in permutation_values) / len(permutation_values)
    upper = sum(value >= t_plus - 1e-12 for value in permutation_values) / len(permutation_values)
    if alternative == "greater":
        permutation_p = upper
    elif alternative == "less":
        permutation_p = lower
    else:
        permutation_p = min(1.0, 2 * min(lower, upper))
    return {"n": len(nonzero), "T_plus": t_plus, "T_minus": t_minus,
            "p_exact_sign_permutation": float(permutation_p)}


def spearman(x: list[int], y: list[int]) -> dict[str, float]:
    """Return the textbook coefficient, normal approximation, and exact p if feasible."""
    x_arr, y_arr = np.asarray(x), np.asarray(y)
    n = len(x)
    d2 = int(np.square(x_arr - y_arr).sum())
    rs = 1 - 6 * d2 / (n * (n**2 - 1))
    z = rs * sqrt(n - 1)
    normal_p = 2 * stats.norm.sf(abs(z))
    exact_p = np.nan
    if n <= 8:
        observed = abs(rs)
        extreme = 0
        total = 0
        for perm in permutations(y):
            total += 1
            p_arr = np.asarray(perm)
            p_rs = 1 - 6 * np.square(x_arr - p_arr).sum() / (n * (n**2 - 1))
            extreme += abs(p_rs) >= observed - 1e-12
        exact_p = extreme / total
    return {"n": n, "sum_d2": d2, "rs": rs, "z_normal": z,
            "p_normal": float(normal_p), "p_exact": float(exact_p)}


def kruskal(groups: list[list[float]]) -> dict[str, float]:
    """Return the uncorrected course H and SciPy's tie-corrected result."""
    values = np.concatenate([np.asarray(group, dtype=float) for group in groups])
    ranks = stats.rankdata(values, method="average")
    sizes = [len(group) for group in groups]
    rank_sums = []
    cursor = 0
    for size in sizes:
        rank_sums.append(float(ranks[cursor:cursor + size].sum()))
        cursor += size
    n_total = len(values)
    h_course = 12 / (n_total * (n_total + 1)) * sum(
        r_sum**2 / size for r_sum, size in zip(rank_sums, sizes)
    ) - 3 * (n_total + 1)
    scipy_result = stats.kruskal(*groups)
    return {"sizes": sizes, "rank_sums": rank_sums, "H_course": h_course,
            "H_tie_corrected": float(scipy_result.statistic),
            "p_chi_square": float(scipy_result.pvalue)}


def exact_kruskal_three(groups: list[list[float]]) -> float:
    """Exact randomization p-value for the 5/4/6 sample-size question."""
    pooled = np.concatenate([np.asarray(group, dtype=float) for group in groups])
    ranks = stats.rankdata(pooled, method="average")
    n1, n2, n3 = map(len, groups)
    observed = kruskal(groups)["H_course"]
    indices = range(len(pooled))
    extreme = 0
    total = 0
    for first in combinations(indices, n1):
        remaining = [i for i in indices if i not in first]
        r1 = ranks[list(first)].sum()
        for second_local in combinations(range(len(remaining)), n2):
            second = [remaining[i] for i in second_local]
            third = [i for i in remaining if i not in second]
            r2, r3 = ranks[second].sum(), ranks[third].sum()
            h = 12 / (len(pooled) * (len(pooled) + 1)) * (
                r1**2 / n1 + r2**2 / n2 + r3**2 / n3
            ) - 3 * (len(pooled) + 1)
            total += 1
            extreme += h >= observed - 1e-12
    assert total == comb(n1 + n2 + n3, n1) * comb(n2 + n3, n2)
    return extreme / total


def main() -> None:
    checks: dict[str, object] = {
        "P1": sign_test(250, 140),
        "P2": sign_test(120, 75),
        "P3_given_W": {"mu": 150, "sigma": sqrt(300),
                         "z_cc": (184.5 - 0.5 - 150) / sqrt(300)},
        "P4_given_W": {"mu": 130, "sigma": sqrt(325),
                         "z_cc": (184.5 - 0.5 - 130) / sqrt(325)},
        "P5": rank_sum(
            [257, 280, 200, 250, 284, 295, 297, 265, 330, 350, 340, 272],
            [210, 230, 250, 260, 275, 300, 320, 290, 310, 325, 329, 335],
        ),
        "P6": rank_sum([26, 18, 25, 27, 19, 30, 34, 21, 33, 31],
                        [32, 24, 23, 30, 40, 41, 42, 39, 45, 35]),
        "P7": sign_test(41, 19),
        "P8": spearman([2, 1, 3, 5, 4], [1, 3, 4, 5, 2]),
        "P9": signed_rank([108, 102, 107, 97, 112, 108],
                           [110, 118, 105, 97, 116, 106], "greater"),
        "P10": sign_test(12, 3),
        "P11": sign_test(14, 6),
        "P12": sign_test(50, 60),
        "P13": sign_test(160, 120),
        "P14": signed_rank([59, 57, 60, 66, 68, 59, 72, 52, 58, 63],
                            [57, 62, 60, 63, 69, 63, 74, 56, 64, 64], "greater"),
        "P15": signed_rank([27.1, 28.0, 28.7, 27.6, 26.0, 29.0, 28.2, 28.0, 28.0, 27.0],
                            [27.7, 28.4, 28.9, 27.9, 26.5, 29.1, 28.9, 28.9, 28.8, 28.0], "two-sided"),
        "P16": sign_test(11, 4, "greater"),
        "P17": signed_rank([28, 36, 27, 25, 38, 36, 40, 29, 32, 28, 20, 32, 32, 32, 36],
                            [36, 40, 25, 32, 30, 32, 40, 28, 35, 33, 26, 31, 23, 34, 36], "greater"),
        "P18": sign_test(36, 15),
        "P19_counts_total_85": sign_test(45, 30),
        "P20": rank_sum([31, 32, 26, 34, 24, 35, 39, 28, 44, 42],
                         [31, 25, 29, 30, 27, 33, 37, 39, 38, 36, 40]),
        "P21": kruskal([[24, 16, 21, 15, 19, 26],
                         [23, 17, 22, 25, 18, 29, 27],
                         [30, 20, 23, 25, 34, 36, 28]]),
        "P22": spearman([6, 10, 2, 1, 5, 11, 4, 3, 7, 12, 9, 8],
                         [5, 11, 6, 3, 4, 12, 2, 1, 7, 10, 8, 9]),
        "P23": kruskal([[91, 80, 70, 60, 85], [63, 92, 86, 75, 70, 99],
                         [95, 80, 70, 60, 90]]),
        "P24": spearman([7, 8, 1, 2, 9, 3, 10, 11, 4, 6, 12, 5],
                         [8, 7, 2, 3, 1, 10, 9, 4, 6, 11, 5, 12]),
        "P25": spearman([3, 5, 1, 6, 2, 4, 7, 8], [2, 1, 4, 7, 5, 8, 6, 3]),
        "P26": spearman([3, 1, 8, 2, 5, 7, 4, 6], [6, 2, 5, 1, 7, 8, 3, 4]),
        "P27": spearman([5, 2, 1, 3, 4], [1, 2, 3, 5, 4]),
        "P28": kruskal([[56, 85, 65, 86, 93], [62, 97, 91, 82],
                         [94, 72, 93, 78, 54, 77]]),
    }
    checks["P28_exact_randomization_p"] = exact_kruskal_three(
        [[56, 85, 65, 86, 93], [62, 97, 91, 82], [94, 72, 93, 78, 54, 77]]
    )
    for name, result in checks.items():
        print(name, result)


if __name__ == "__main__":
    main()
