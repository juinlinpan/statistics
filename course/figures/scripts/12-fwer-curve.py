# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy"]
# ///
"""Chapter 12, section 1 worked example: FWER = 1-(1-alpha)^m for independent
tests, alpha = 0.05, as the number of tests m grows.

Matches the chapter's opening worked example exactly: m=20 independent tests,
each at alpha=0.05, gives FWER = 1 - 0.95^20 ~= 0.642 (64.2%), which the
chapter states in "為什麼要學這一章" and re-derives in section 1 under
"從一個具體問題開始".

Shows how fast the family-wise error rate inflates as m grows, with the
m=20 point marked to match the chapter's number exactly.
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from _style import apply_style, CATEGORICAL, ACCENT, INK_SECONDARY

apply_style()

alpha = 0.05
m = np.arange(1, 41)
fwer = 1 - (1 - alpha) ** m

m_highlight = 20
fwer_highlight = 1 - (1 - alpha) ** m_highlight  # ~0.6415

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(m, fwer, color=CATEGORICAL[0], linewidth=2.2,
        label=r"獨立檢定的 FWER：$1-(1-\alpha)^m$，$\alpha=0.05$")

ax.axhline(alpha, color=INK_SECONDARY, linewidth=1.2,
            label=r"單一檢定的 $\alpha=0.05$")

ax.scatter([m_highlight], [fwer_highlight], color=ACCENT, s=60, zorder=5,
           label=f"$m=20$：FWER $\\approx {fwer_highlight * 100:.1f}\\%$")
ax.vlines(m_highlight, 0, fwer_highlight, color=ACCENT, linewidth=1.2)
ax.hlines(fwer_highlight, 0, m_highlight, color=ACCENT, linewidth=1.2)

ax.set_xlim(0, 40)
ax.set_ylim(0, 1)
ax.set_xlabel("檢定數 $m$（假設彼此獨立、皆為真 $H_0$）")
ax.set_ylabel("至少一次誤報的機率（FWER）")
ax.set_title(r"檢定愈多，至少一次誤報的機率愈高：$\mathrm{FWER}=1-(1-\alpha)^m$")
ax.legend(loc="lower right", fontsize=9)

fig.tight_layout()
out_path = __file__.replace("scripts", "generated").replace(".py", ".png")
fig.savefig(out_path)
print(f"Saved to {out_path}; FWER(m=20, alpha=0.05) = {fwer_highlight:.6f}")
