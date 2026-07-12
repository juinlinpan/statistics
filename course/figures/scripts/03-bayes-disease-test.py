# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Prior vs. posterior probability for the chapter's Bayes'-rule worked example (Section 8.1).

Data (exactly as in the chapter text):
- Prevalence (prior): P(D) = 0.01
- Sensitivity: P(+|D) = 0.90
- False-positive rate: P(+|D^c) = 0.05
- Posterior after a positive test: P(D|+) = 0.90*0.01 / (0.90*0.01 + 0.05*0.99) ≈ 0.154

Illustrates that a positive test raises the probability of disease well above
the 1% base rate, but far short of "almost certainly diseased" (still ~85%
chance of no disease), because the disease is rare relative to the
false-positive rate.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _style import apply_style, CATEGORICAL

apply_style()

# apply_style() sets a Latin-only sans-serif stack; extend it here (this
# script only) with a CJK-capable fallback so Traditional Chinese labels
# render as glyphs instead of tofu boxes on this machine.
plt.rcParams["font.sans-serif"] = [
    "PingFang HK",
    "Heiti TC",
    "Arial Unicode MS",
] + plt.rcParams["font.sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

labels = ["檢測前\n(先驗機率)", "檢測陽性後\n(後驗機率)"]
values = [0.01, 90 * 0.01 / (90 * 0.01 + 5 * 0.99)]  # 0.01, ≈0.1538

fig, ax = plt.subplots(figsize=(6.5, 4.5))

bars = ax.bar(labels, values, color=[CATEGORICAL[0], CATEGORICAL[2]], width=0.55)

for bar, v in zip(bars, values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        v + 0.01,
        f"{v * 100:.1f}%",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )

ax.set_ylabel("患病機率")
ax.set_ylim(0, 0.30)
ax.set_title("貝氏法則更新：陽性檢測前後的患病機率")

out_dir = Path(__file__).resolve().parent.parent / "generated"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "03-bayes-disease-test.png"
fig.savefig(out_path)
print(f"Saved {out_path}")
