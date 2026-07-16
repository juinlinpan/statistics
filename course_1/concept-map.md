# 統計觀念地圖

本頁不重複各章的完整推導，只標出容易混淆的概念群組：它們分別在哪一章第一次出現、又在哪一章被重新對照。詳細比較表在各章正文的「跨章比較與選法」小節，這裡只放索引與連結。

## 1. 一個數字的兩種身分：母數 vs. 統計量 vs. 估計

| 概念 | 第一次出現 | 被重新對照的地方 |
|---|---|---|
| 樣本平均數／樣本標準差（描述手上這批資料） | [第 1 章](chapters/01-descriptive-statistics.md#formula-ch01-sample-mean) | [第 5 章](chapters/05-sampling-distributions-clt.md)：同樣的數字被重新理解成「會隨樣本變動的統計量」 |
| 母數 $\mu,\sigma$、統計量、估計量／估計值 | [第 5 章](chapters/05-sampling-distributions-clt.md) | — |

## 2. 分散度量：SD、SE、FPC

| 概念 | 回答什麼問題 | 定義章節 | 對照章節 |
|---|---|---|---|
| 標準差(SD) | 個別觀測值離平均數多分散 | [第 1 章](chapters/01-descriptive-statistics.md#formula-ch01-sample-standard-deviation) | [第 5 章](chapters/05-sampling-distributions-clt.md#formula-m05-se-sample-mean)：與 SE 對照 |
| 標準誤(SE) | 統計量本身在重複抽樣間多分散 | [第 5 章](chapters/05-sampling-distributions-clt.md#formula-m05-se-sample-mean) | 供[第 7 章](chapters/07-confidence-intervals.md#formula-ci-mean-large-sample)信賴區間、[第 8 章](chapters/08-significance-tests.md#formula-test-statistic-general-ch08)檢定統計量直接使用 |
| 有限母體修正(FPC) | 不放回抽樣佔母體比例較大時的修正 | [第 5 章](chapters/05-sampling-distributions-clt.md#formula-m05-finite-population-correction) | — |
| Bootstrap 標準誤／偏誤 | 用重抽樣估計任意統計量的 SE，不需封閉公式 | [第 9 章](chapters/09-resampling.md#formula-ch09-bootstrap-standard-error) | 與[第 7 章](chapters/07-confidence-intervals.md#formula-bootstrap-standard-error)、[第 8 章](chapters/08-significance-tests.md)的傳統方法對照，見[第 9 章跨章比較](chapters/09-resampling.md) |

## 3. 分配家族：常態、二項、t、卡方、F

| 分配 | 用在哪裡 | 定義章節 | 與相鄰分配的選法 |
|---|---|---|---|
| 常態(z) | 已知 $\sigma$ 或大樣本的位置與機率計算 | [第 4 章](chapters/04-normal-and-binomial.md#formula-ch04-z-score) | 與 t 的選法見[第 8 章](chapters/08-significance-tests.md#formula-one-sample-t-ch08) |
| 二項 | 固定次數、二元結果、固定機率、獨立試驗的成功次數 | [第 4 章](chapters/04-normal-and-binomial.md#formula-ch04-binomial-pmf) | 常態近似見同章[常態近似二項](chapters/04-normal-and-binomial.md#formula-ch04-normal-approx-binomial)；與卡方的關係見[第 10 章](chapters/10-categorical-data.md#formula-ch10-chi-square-statistic) |
| t | $\sigma$ 未知、以 $s$ 估計時的平均數推論 | [第 8 章](chapters/08-significance-tests.md#formula-one-sample-t-ch08) | 與 z 的選法見[第 8 章跨章比較](chapters/08-significance-tests.md) |
| 卡方($\chi^2$) | 類別資料的適合度、同質性、獨立性檢定 | [第 10 章](chapters/10-categorical-data.md#formula-ch10-chi-square-statistic) | 與單一比例常態方法的選法見[第 10 章跨章比較](chapters/10-categorical-data.md) |
| F | 三組以上母體平均數是否全部相等 | [第 11 章](chapters/11-one-way-anova.md#formula-anova-f-statistic) | 與逐對 t／z 檢定的選法見[第 11 章跨章比較](chapters/11-one-way-anova.md) |

## 4. 推論三支柱：信賴區間、顯著性檢定、Bootstrap

| | 回答什麼 | 章節 |
|---|---|---|
| 信賴區間 | 母數合理的範圍 | [第 7 章](chapters/07-confidence-intervals.md#formula-ci-estimate-critical-se) |
| 顯著性檢定 | 特定假設值是否與資料相容 | [第 8 章](chapters/08-significance-tests.md#formula-test-statistic-general-ch08) |
| Bootstrap | 用重抽樣取代封閉公式估計不確定性 | [第 9 章](chapters/09-resampling.md#formula-ch09-bootstrap-standard-error) |

三者的完整兩兩對照（信賴區間 vs. 檢定、傳統方法 vs. bootstrap）見 [`method-selector.md`](method-selector.md)。

## 5. 一次檢定 vs. 很多次檢定

| 概念 | 問題 | 章節 |
|---|---|---|
| 單一顯著性檢定 | 一個假設，一次判斷 | [第 8 章](chapters/08-significance-tests.md#formula-test-statistic-general-ch08) |
| ANOVA 的單一 $F$ 檢定 | 用一次檢定取代很多次逐對 t 檢定，避免誤報膨脹 | [第 11 章](chapters/11-one-way-anova.md#formula-anova-f-statistic) |
| 多重比較校正(Bonferroni／FDR) | ANOVA 顯著後，如何在很多次事後比較中控制整體誤報率 | [第 12 章](chapters/12-multiple-comparisons.md#formula-fwer-independent-tests) |

## 6. 變異的拆解：迴歸的 $R^2$ vs. ANOVA 的組間／組內

| | 拆解對象 | 章節 |
|---|---|---|
| $R^2$ | 連續預測變數解釋了多少 $y$ 的變異 | [第 6 章](chapters/06-regression.md#formula-ch06-r-squared) |
| 組間／組內平方和 | 類別分組解釋了多少總變異 | [第 11 章](chapters/11-one-way-anova.md#formula-anova-sums-of-squares) |

兩者都是「總變異 = 已解釋 + 未解釋」的同一種邏輯，套用在不同的解釋變數類型上；對照見[第 11 章跨章比較](chapters/11-one-way-anova.md)。

## 如何使用本頁

這裡只列出跨章會反覆混淆的概念與其定義／對照位置，不是完整詞彙表；每章章末的「公式與術語速查」仍是該章最完整的定義來源。若要依「我現在有什麼資料、想回答什麼問題」反查方法，請見 [`method-selector.md`](method-selector.md)。
