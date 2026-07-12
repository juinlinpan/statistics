# 統計方法選擇器

依「資料型態」與「想回答的問題」查表，找到對應方法與章節；每格連結到該方法定義所在的公式錨點，完整的假設與限制請點進該章閱讀。概念之間為何容易混淆、彼此如何對照，見 [`concept-map.md`](concept-map.md)。

## 第一步：你的目標量是什麼類型？

| 目標量類型 | 到下面哪一節 |
|---|---|
| 一個數值變數的中心或分散（單一組） | 第 2 節 |
| 一個數值變數，比較兩組或多組 | 第 3 節 |
| 兩個數值變數的關係 | 第 4 節 |
| 一個類別變數的分布，或兩個類別變數的關聯 | 第 5 節 |
| 一個機率或期望值，難以用公式推導 | 第 6 節 |
| 你已經做完一組檢定，正在煩惱要不要修正 | 第 7 節 |

## 2. 單一數值變數：中心與分散

| 想知道 | 方法 | 章節 |
|---|---|---|
| 這批資料本身的中心、分散、離群值 | 平均數／中位數／IQR／樣本標準差 | [第 1 章](chapters/01-descriptive-statistics.md#formula-ch01-sample-mean) |
| 母體平均數的合理範圍，$\sigma$ 已知或大樣本 | 平均數信賴區間（CLT-based） | [第 7 章](chapters/07-confidence-intervals.md#formula-ci-mean-large-sample) |
| 母體平均數是否等於某假設值，$\sigma$ 未知、樣本不夠大 | 單樣本 t 檢定 | [第 8 章](chapters/08-significance-tests.md#formula-one-sample-t-ch08) |
| 某個沒有簡單 SE 公式的統計量（中位數、相關係數…）的不確定性 | Bootstrap 標準誤／百分位區間 | [第 9 章](chapters/09-resampling.md#formula-ch09-bootstrap-standard-error) |
| 一個比例的合理範圍或是否等於某假設值 | 比例的 Wald 區間／精確二項檢定 | [第 7 章](chapters/07-confidence-intervals.md#formula-ci-proportion-wald)、[第 8 章](chapters/08-significance-tests.md#formula-exact-binomial-pvalue-ch08) |

## 3. 比較數值變數的組間差異

| 資料結構 | 方法 | 章節 |
|---|---|---|
| 兩個獨立組 | 兩樣本 z／t 檢定 | [第 8 章](chapters/08-significance-tests.md#formula-two-sample-z-means-ch08) |
| 同一批受試者前後測，或天然配對 | 成對 t 檢定 | [第 8 章](chapters/08-significance-tests.md#formula-paired-t-ch08) |
| 三組以上獨立組，只想知道「是否全部相等」 | 單因子 ANOVA（F 檢定） | [第 11 章](chapters/11-one-way-anova.md#formula-anova-f-statistic) |
| ANOVA 顯著後，想知道哪幾對不同 | 先看[第 7 節：一次 vs. 多次檢定](#7-一次檢定-vs-很多次檢定) | [第 12 章](chapters/12-multiple-comparisons.md#formula-fwer-independent-tests) |

**常見誤用：** 把成對資料當獨立兩組硬套公式，會低估精確度；把三組以上的比較拆成很多次獨立兩兩 t 檢定，會讓整體誤報率膨脹（見第 7 節）。

## 4. 兩個數值變數的關係

| 想知道 | 方法 | 章節 |
|---|---|---|
| 兩變數線性關聯的方向與強度 | 相關係數 $r$ | [第 6 章](chapters/06-regression.md#formula-ch06-correlation) |
| 用一個變數預測另一個 | 最小平方法迴歸線 | [第 6 章](chapters/06-regression.md#formula-ch06-regression-line) |
| 迴歸模型解釋了多少變異 | $R^2$ | [第 6 章](chapters/06-regression.md#formula-ch06-r-squared) |
| 迴歸斜率的信賴區間或顯著性檢定、迴歸的 bootstrap | 超出本課程正式範圍 / [第 9 章](chapters/09-resampling.md#formula-ch09-residual-bootstrap-response) 的 pairs／residual bootstrap 作為延伸 | 第 6、9 章 |

## 5. 類別資料

| 想知道 | 方法 | 章節 |
|---|---|---|
| 一個二元比例是否等於某假設值 | 常態近似或精確二項方法 | 第 4、7、8 章（見上方第 2 節） |
| 一個類別變數（3 類以上）是否符合指定比例分布 | 卡方適合度檢定 | [第 10 章](chapters/10-categorical-data.md#formula-ch10-gof-expected-count) |
| 多個母體的類別分布是否相同 | 卡方同質性檢定 | [第 10 章](chapters/10-categorical-data.md#formula-ch10-two-way-expected-count) |
| 同一母體中兩個類別變數是否關聯 | 卡方獨立性檢定 | [第 10 章](chapters/10-categorical-data.md#formula-ch10-two-way-expected-count) |
| 關聯強度多大（不只是顯著與否） | Cramér's V | [第 10 章](chapters/10-categorical-data.md#formula-ch10-cramers-v) |

**判斷同質性 vs. 獨立性看的不是表格長相，是抽樣設計：** 是否從多個母體各抽一個樣本（同質性），還是從一個母體抽樣、同時測量兩個變數（獨立性）。詳見[第 10 章](chapters/10-categorical-data.md)。

## 6. 機率、模擬與重抽樣

| 想知道 | 方法 | 章節 |
|---|---|---|
| 一個事件在已知模型下的精確機率 | 機率規則（加法、乘法、條件機率、貝氏定理） | [第 3 章](chapters/03-probability.md#formula-conditional-probability) |
| 同樣的機率，但公式難算或懶得手算 | Monte Carlo 模擬 | [第 9 章](chapters/09-resampling.md#formula-ch09-monte-carlo-event-probability) |
| 某統計量在重複抽樣下的不確定性，且有母體模型公式可套 | 傳統母體模型方法（CLT、t 等） | 第 5、7、8 章 |
| 同樣的問題，但統計量沒有簡單公式，或不想假設常態 | Bootstrap | [第 9 章](chapters/09-resampling.md#formula-ch09-bootstrap-standard-error) |

## 7. 一次檢定 vs. 很多次檢定

先問：**這一批分析算不算同一個「假設族」？**

| 情境 | 方法 | 章節 |
|---|---|---|
| 只有一個事先指定的假設 | 直接用對應的信賴區間或檢定 | 第 7、8 章 |
| 三組以上母體平均數，只想問「是否全部相等」 | 單因子 ANOVA 的單一 F 檢定，取代逐對 t 檢定 | [第 11 章](chapters/11-one-way-anova.md#formula-anova-f-statistic) |
| 同一族內要做很多次檢定，任何一次誤報都代價很高 | Bonferroni 校正，控制 FWER | [第 12 章](chapters/12-multiple-comparisons.md#formula-bonferroni-threshold) |
| 大量候選篩選，可以容忍發現中有一定比例誤報 | Benjamini–Hochberg 程序，控制 FDR | [第 12 章](chapters/12-multiple-comparisons.md#formula-benjamini-hochberg-step-up) |
| 想用同一份資料先探索、再確認 | 資料切分（探索集／確認集） | [第 12 章](chapters/12-multiple-comparisons.md) |

## 使用這份選擇器的方式

先用第一步的表格判斷資料型態與問題種類，再進入對應小節找方法；每個連結指向該方法定義的公式錨點，實際使用前務必回到該章確認假設與適用條件——本頁只幫你「找對候選方法」，不能取代該章的完整推導與限制說明。若想知道「這個方法跟旁邊那個公式差在哪裡」，見 [`concept-map.md`](concept-map.md)。
