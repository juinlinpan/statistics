# Course2 課程範圍與素材對應

## 課程資訊

- 課程：Quan1150 商業數量方法（政治大學統計系，余清祥老師，2026 夏季密集課程）
- 教材：Anderson, Sweeney, Williams et al., *Statistics for Business and Economics*, **14e Metric Version**（投影片依此版）
- 本地課本 PDF：`course_2/DavidAnderson_Statistics_for_Business_an.pdf` 是 **11e**。兩版章節主題相同但節號可能略有差異（例如 14e 的 7.9 Big Data and Standard Errors 在 11e 沒有）。查核時以內容對照為準，不要硬對節號；11e 找不到的內容以投影片為準並註記。
- **考試範圍：Ch12–18**（有考古題）。**Ch7–10 只是複習**，不直接考，但它是 Ch12 之後所有推論方法的地基。

## 投影片 ↔ 講義對應表

| 投影片檔案（course_2/ppt/） | 授課日期 | 章節 | 講義檔案（course_2/chapters/） |
|---|---|---|---|
| Quan1150_Week2.pdf | 2026/6/29–30 | 第 7–10 章 估計與檢定（複習） | 07-10-review-estimation-and-testing.md |
| Quan1150(Chi-Square).pdf | 2026/7/1–2 | 第 12 章 卡方檢定 | 12-chi-square-tests.md |
| Quan1150(ANOVA).pdf | 2026/7/6–7 | 第 13 章 變異數分析 | 13-anova.md |
| Quan1150(Simple Regression).pdf | 2026/7/8–9 | 第 14 章 簡單線性迴歸 | 14-simple-linear-regression.md |
| Quan1150(Multiple Regression).pdf | 2026/7/13–14 | 第 15 章 複迴歸 | 15-multiple-regression.md |
| Quan1150(Model Construction).pdf | 2026/7/15–16 | 第 16 章 建立迴歸模型 | 16-regression-model-building.md |
| （尚未公布，2026-07-15 時點） | — | 第 17 章 指數 | 17-index-numbers.md |
| （尚未公布，2026-07-15 時點） | — | 第 18 章 時間序列分析與預測 | 18-time-series-and-forecasting.md |

老師公布新投影片後：先更新本表與 `course_2/進度.md`，再對新投影片做 Phase 1。Ch17、18 在投影片公布前不可開始 Phase 1（考古題已在 quiz-set，屆時 Phase 6 素材已備）。

## 考古題

`course_2/quiz-set/Quan1150(Chap12~18)Q-set/` 內有 Ch12–18 各一份考古題 PDF（Phase 6、8 素材）。Ch7–10 複習講義無對應考古題，但仍要執行 Phase 7 定性意義補強。

## 各章主題範圍（供 Phase 1 涵蓋檢查與 Phase 2 查核定位）

以投影片實際內容為權威範圍；下表為課本對應主題的速查。

- **Ch7 抽樣與抽樣分配（複習）**：點估計；$\bar{x}$ 與 $\bar{p}$ 的抽樣分配、期望值、標準誤；中央極限定理；點估計量性質（不偏、有效、一致）；其他抽樣方法。
- **Ch8 區間估計（複習）**：母體平均數信賴區間（σ 已知/未知）；樣本數決定；母體比例信賴區間。
- **Ch9 假設檢定（複習）**：虛無/對立假設；型一、型二誤差；平均數檢定（σ 已知/未知）、比例檢定；單尾雙尾；p 值；區間估計與檢定的關係。
- **Ch10 兩母體推論（複習）**：兩平均數差（獨立樣本，σ 已知/未知）；配對樣本；兩比例差。
- **Ch12 卡方檢定**：適合度檢定（多項母體）；獨立性檢定；（視投影片）Poisson/常態適合度。
- **Ch13 變異數分析**：實驗設計與 ANOVA 概念、假設；完全隨機設計（組間/組內變異、F 檢定、ANOVA 表）；多重比較（Fisher's LSD、型一誤差率）；隨機集區設計；因子實驗。
- **Ch14 簡單線性迴歸**：迴歸模型與最小平方法；判定係數與相關係數;模型假設；顯著性檢定（t、F）；估計與預測區間；殘差分析；離群值與影響點。
- **Ch15 複迴歸**：模型與估計；多元判定係數與調整後 $R^2$；F 與 t 檢定；多重共線性；類別（虛擬）變數；殘差分析；（視投影片）邏輯斯迴歸。
- **Ch16 建立迴歸模型**：一般線性模型（曲線關係、交互作用、變數轉換）；變數增刪判斷；逐步/向前/向後/最佳子集選取；實驗設計的迴歸做法；自相關與 Durbin-Watson 檢定。
- **Ch17 指數**：價格相對比；加權綜合價格指數（Laspeyres、Paasche）；CPI、PPI、道瓊等重要指數；以指數平減；數量指數。
- **Ch18 時間序列分析與預測**：時間序列型態；預測準確度量；移動平均與指數平滑；趨勢投影；季節性與趨勢；時間序列分解。

## course_1 先備知識對應表（Phase 3 用）

course_1（初級統計，`course_1/chapters/`）已完成 12 章。各講義的「先備知識」一節從這裡取材：

| course_2 講義 | course_1 對應章節 |
|---|---|
| 07-10-review | 05-sampling-distributions-clt.md（抽樣分配、CLT、標準誤）、07-confidence-intervals.md、08-significance-tests.md、02-sampling-and-experiments.md（抽樣方法） |
| 12-chi-square | 10-categorical-data.md（卡方三兄弟）、08-significance-tests.md（檢定邏輯、p 值） |
| 13-anova | 11-one-way-anova.md、12-multiple-comparisons.md（多重比較、FWER）、02-sampling-and-experiments.md（實驗設計） |
| 14-simple-regression | 06-regression.md（相關、最小平方、殘差）、07/08（區間與檢定邏輯） |
| 15-multiple-regression | 06-regression.md、08-significance-tests.md；複迴歸本身 course_1 未教，斷層要在講義內補 |
| 16-model-building | 06-regression.md（殘差診斷、轉換）；變數選取、DW 檢定 course_1 未教 |
| 17-index-numbers | 無先修對應（course_1 未涵蓋），講義需自給自足 |
| 18-time-series | 無先修對應（course_1 未涵蓋；僅 01 章的折線圖概念沾邊），講義需自給自足 |

課本第 1–6 章（敘述統計、機率、離散/連續分配）不在授課範圍，但屬於 ch7–10 複習講義的斷層補強來源（Phase 3 第 1 項）。

## 版權界線

投影片、課本、考古題皆為版權教材，PDF 已由 `.gitignore`（`*.pdf`）排除於 git。講義是個人讀書用途的轉化整理：可完整涵蓋投影片教學內容與考古題題目及詳解，但不得公開發布、部署為對外網站、或重製投影片原始圖片版面。
