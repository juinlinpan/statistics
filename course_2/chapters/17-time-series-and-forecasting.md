---
chapter: "17"
slug: 17-time-series-and-forecasting
title: 第 17 章：時間數列與預測
source_deck: Quan1150(Forecast).pdf
---

# 第 17 章：時間數列與預測

## 先備知識

本章沒有 course1 的完整先修對應，因此會從「一列資料代表一個時間點」開始自給自足。你只要先記得三件事：平均數描述中心、殘差是實際值減預測值、迴歸線可以用一個變數預測另一個變數。

- **平均數與離散：** 平均數是資料大致圍繞的水準；資料在平均數附近散得多開，則是另一件事。水平型時間數列要求水準和變異大致不隨時間改變。
- **殘差與平方誤差：** 預測太低時殘差為正，預測太高時殘差為負。把誤差取絕對值或平方，是為了避免正負互相抵銷。
- **迴歸直覺：** 本章把時間 $t$ 當成自變數，時間數列值 $Y_t$ 當成應變數，沿用[第 14 章最小平方法](14-simple-linear-regression.md#formula-slr-slope-intercept)找趨勢線；平方趨勢與季節虛擬變數則延伸[第 16 章一般線性模型](16-regression-model-building.md#formula-general-linear-model)。

時間資料最特殊的地方是順序不能任意交換。把 1 月和 12 月互換，資料意義就變了。這也是為什麼本章除了看數值大小，還要看趨勢、季節節奏和相鄰期是否連續。

## 學習目標

讀完本章後，你應該能夠：

- 從時間數列圖辨認水平、趨勢、季節、趨勢加季節及循環型態。
- 分辨時間數列法、因果預測法與以時間為自變數的時間數列迴歸。
- 計算預測誤差、MAE、MSE、MAPE，並說明三者重視的失準面向。
- 使用樸素法、移動平均、加權移動平均與單一指數平滑做短期預測。
- 解釋視窗長度 $k$ 和平滑常數 $\alpha$ 對平滑程度與反應速度的取捨。
- 建立線性、二次與指數趨勢，並避免不合理的遠期外推。
- 用虛擬變數建立只有季節、或同時有季節與線性趨勢的迴歸模型。
- 完成乘法分解：中央移動平均、季節不規則比、季節指數、去季節化、趨勢配適與再季節化預測。

## 本章重點一覽

預測不是先挑一條公式，而是先辨認資料留下什麼時間結構：

1. 先畫時間數列圖，判斷資料是水平、趨勢、季節，還是趨勢與季節並存。
2. 用歷史期間的誤差比較候選方法，但不把樣本內準確度誤當成未來保證。
3. 水平型資料用平滑法；趨勢型資料用趨勢投影；季節型資料用虛擬變數或分解法。
4. 每個方法都在做訊號與雜訊的取捨：平滑越強，隨機起伏越少，但對結構改變的反應也越慢。
5. 預測值只是條件式的合理中心，不是未來一定發生的數字；外推越遠，歷史規律失效的風險越大。

## 內容講解

### 1. 預測方法與時間數列的資料結構

<a id="section-ch17-data-structure"></a>

投影片第 1 至 5 頁先區分**定性預測(qualitative forecasting)** 與**定量預測(quantitative forecasting)** 。歷史資料不存在或已失去參考性時，例如全新產品上市，可依賴專家判斷、Delphi 法或市場研究。歷史資料可量化，而且有理由相信某些過去型態仍會延續時，才適合定量預測。

定量預測又可分為：

| 方法 | 使用的資訊 | 核心問題 |
|---|---|---|
| 時間數列法(time series method) | 目標變數自己的過去值與過去預測誤差 | 過去的水準、趨勢或季節節奏會不會延續？ |
| 因果預測法(causal method) | 目標變數以外的解釋變數 | 價格、廣告、所得等變數能否幫忙預測？ |
| 時間數列迴歸(time series regression) | 把時間 $t$ 當成自變數 | 長期平均水準如何隨時間改變？ |

因果預測的「cause」是建模假設，不代表觀察性迴歸已證明因果。若廣告與銷售一起上升，仍可能是旺季同時拉高兩者。時間數列法也不是只要有日期就能用；觀測間隔應規律，而且歷史型態要對未來仍有參考性。

### 2. 時間數列型態：先看資料長相

<a id="section-ch17-patterns"></a>

投影片第 6 至 16 頁的第一個動作是畫**時間數列圖(time series plot)** ：橫軸放時間，縱軸放觀察值。圖不是裝飾，而是選方法的入口。

![四種時間數列型態分別呈現固定水準、長期趨勢、固定季節節奏與趨勢加季節](../figures/generated/ch17_time_series_patterns.png)

你該注意什麼：水平型的中心大致固定；趨勢型的基準水準逐期移動；季節型在固定週期重複；趨勢加季節則是移動的基準上仍保留固定節奏。圖為示意資料。

#### 2.1 水平型與定態

**水平型(horizontal pattern)** 表示觀察值在固定平均水準附近隨機起伏。投影片的 Gasoline 資料有 12 週銷量，平均為 19.25 千加侖，雖然每週不同，中心沒有明顯上升或下降。

**定態時間數列(stationary time series)** 至少要求資料生成過程的平均數與變異不隨時間改變。定態通常畫出水平型，但只看到水平外觀不能證明定態。例如第 13 週簽下新合約後，平均銷量整段上移；前後各自看似水平，合起來卻不是固定平均。

**定性意義：** 水平型不是「每期都差不多」而是「沒有可辨認的方向或固定節奏，剩下主要是中心附近的雜訊」。若水準突然移動，長期平均雖然很平滑，卻會把舊制度的資料拖進新制度，反應太慢。

#### 2.2 線性與非線性趨勢

<a id="section-ch17-trend-patterns"></a>

**趨勢(trend)** 是長期水準逐步上升或下降。投影片 Bicycle 銷量 10 年間整體上升，適合先檢查線性趨勢；Cholesterol 藥品收入的增幅愈來愈大，較像二次或指數趨勢。

- 線性趨勢：每期大致增加或減少固定量。
- 指數趨勢：每期大致乘上固定倍率，也就是百分比變化較穩定。
- 二次趨勢：每期的增減量本身逐漸改變，可呈現加速、減速或轉折。

趨勢是描述歷史平均路徑，不是保證未來永遠沿同一方向。藥品可能遇到專利到期，人口成長也可能停滯；遠期外推尤其需要商業判斷。

#### 2.3 季節、趨勢加季節與循環

<a id="section-ch17-seasonal-cyclical"></a>

**季節型(seasonal pattern)** 是固定週期內重複的節奏，不必真的與四季有關。每週餐廳銷量、一天內交通流量、每季雨傘銷售都可能有季節性。投影片 Umbrella 資料每年第二季最高、第四季最低，且沒有明顯長期趨勢。

Smartphone 資料同時具有上升趨勢與季度節奏：每年的第二季偏低，第三、四季偏高。此時只用水平平滑會把趨勢當誤差，只用趨勢線又會把固定季節落差當誤差。

**循環型(cyclical pattern)** 指觀察值在趨勢線上下形成持續超過一年的長段落，常與景氣循環有關。循環週期不固定、資料需求很長，也很難預測，因此本章只辨認，不估計獨立循環模型。

| 型態 | 重複尺度 | 規律性 | 本章主要方法 |
|---|---|---|---|
| 季節 | 一年內或其他固定短週期 | 週期通常固定 | 季節虛擬變數、季節指數 |
| 循環 | 多年 | 長度與幅度常改變 | 通常併入趨勢循環，不單獨預測 |
| 不規則 | 無固定週期 | 突發、不可預期 | 視為預測誤差的一部分 |

### 3. 預測誤差與準確度

投影片第 17 頁先用最簡單的**樸素法(naive method)** ：下一期預測等於最近一期實際值。

<a id="formula-ch17-naive-forecast"></a>

**樸素預測與用途** ：作為最基本的短期預測基準。

$$
F_{t+1}=Y_t
$$

$Y_t$ 是第 $t$ 期實際值，$F_{t+1}$ 是第 $t+1$ 期預測值。它等同一階移動平均，也等同 $\alpha=1$ 的單一指數平滑。若複雜方法連樸素法都贏不了，複雜度未必值得。

<a id="formula-ch17-forecast-error"></a>

**預測誤差(forecast error)與用途** ：量第 $t$ 期實際值與先前預測的差。

$$
e_t=Y_t-F_t
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $Y_t$ | 第 $t$ 期實際值 | 與原資料相同 |
| $F_t$ | 在看到第 $t$ 期實際值前做出的預測 | 與原資料相同 |
| $e_t$ | 預測誤差 | 與原資料相同 |

$e_t>0$ 表示實際值高於預測，也就是低估；$e_t<0$ 表示高估。誤差方向很重要，但若直接平均，正負可能抵銷，所以要再用 MAE、MSE 或 MAPE。

#### 3.1 MAE：典型錯幾個原單位

<a id="formula-ch17-mae"></a>

$$
MAE=\frac{\sum_{t=k+1}^{n}|e_t|}{n-k}
$$

$n$ 是總期數，$k$ 是建立第一個預測前需要的歷史期數，$n-k$ 是真正有預測誤差的期數。MAE 與原資料同單位，容易解讀。Gasoline 樸素法有 11 個誤差，絕對誤差總和 41，因此 $MAE=41/11=3.73$ 千加侖。

#### 3.2 MSE：特別不容忍大錯

<a id="formula-ch17-mse"></a>

$$
MSE=\frac{\sum_{t=k+1}^{n}e_t^2}{n-k}
$$

MSE 把大誤差平方，所以少數嚴重失準會有很大影響。Gasoline 的平方誤差總和 179，故 $MSE=179/11=16.27$ 平方千加侖。

![MAE 對誤差採線性懲罰，MSE 則把大誤差平方放大](../figures/generated/ch17_error_metrics.png)

你該注意什麼：MAE 回答一般一期大約錯多少；MSE 更像對重大失準收取高額罰金。不能只因 MSE 數字較大就說模型較差，因為 MSE 的單位已平方。

#### 3.3 MAPE：把失準換成相對百分比

<a id="formula-ch17-mape"></a>

$$
MAPE=\frac{1}{n-k}\sum_{t=k+1}^{n}\left|\frac{e_t}{Y_t}\right|100\%
$$

MAPE 沒有原單位，較適合比較不同量級的數列。Gasoline 的絕對百分比誤差總和 211.69%，故 $MAPE=19.24\%$。

MAPE 的限制是 $Y_t=0$ 時無法計算，$Y_t$ 很接近 0 時比例會爆大，而且正負實際值也會讓商業解讀不自然。此時優先用 MAE、MSE 或另選尺度。

**定性意義：** 三個指標都只量「在已知歷史上重現得多好」。MAE 小代表一般期數的絕對失準較小；MSE 小代表大錯較少或較不嚴重；MAPE 小代表相對於各期規模的誤差較小。它們都不能證明未來準確，更不能把樣本內最佳誤說成資料生成機制永遠不變。

投影片第 21 頁比較 Gasoline 的樸素法與「所有過去值平均」：後者的 MAE、MSE、MAPE 都較小。但若第 13 週水準突然上移，所有歷史平均會反應很慢，樸素法反而更快貼近新水準。準確度與適應結構改變要一起看。

### 4. 水平型資料的三種平滑法

投影片第 22 頁指出，移動平均、加權移動平均與單一指數平滑適合沒有明顯趨勢、循環或季節效果的水平型資料，尤其適合下一期的短期預測。

#### 4.1 移動平均

<a id="formula-ch17-moving-average"></a>

**$k$ 期移動平均(moving average)與用途** ：用最近 $k$ 個實際值的平均預測下一期。

$$
F_{t+1}=\frac{Y_t+Y_{t-1}+\cdots+Y_{t-k+1}}{k}
$$

| 符號 | 意義 |
|---|---|
| $F_{t+1}$ | 第 $t+1$ 期預測 |
| $Y_t$ | 最近一期實際值 |
| $k$ | 納入平均的最近期數 |

Gasoline 的三週移動平均對第 4 週預測為 $(17+21+19)/3=19$。新資料到來後，丟掉最舊一期並加入最新一期，所以視窗會向前移動。

- $k$ 小：反應快，但保留較多短期雜訊。
- $k$ 大：曲線平滑，但遇到水準改變時落後較久。

投影片的三週移動平均得到 $MAE=2.67$、$MSE=10.22$、$MAPE=14.36\%$；試算不同 $k$ 後，$k=6$ 的歷史 MSE 可降到 6.79。這只是該段歷史的最佳值，不是永久最適。

![Gasoline 水準上移後，短移動平均比長移動平均與低 alpha 指數平滑更快追上](../figures/generated/ch17_smoothing_tradeoff.png)

你該注意什麼：平滑越強，隨機起伏越少，但水準真的改變時也越慢追上。這是雜訊過濾和結構反應的根本取捨；圖使用投影片 Gasoline 22 週資料。

#### 4.2 加權移動平均

<a id="formula-ch17-weighted-moving-average"></a>

$$
F_{t+1}=w_tY_t+w_{t-1}Y_{t-1}+\cdots+w_{t-k+1}Y_{t-k+1}
$$

權重必須非負且總和為 1。若最近資料更能代表未來，就給近期較大權重；若數列隨機起伏很大，權重太集中反而容易追著雜訊跑。

Gasoline 三週權重取 $3/6,2/6,1/6$，最近一期最大，則第 4 週預測為：

$$
F_4=\frac{3}{6}(19)+\frac{2}{6}(21)+\frac{1}{6}(17)=19.33
$$

權重 5、3、2 若未正規化，計算時要除以總和 10；不能直接把加權總和當預測。

#### 4.3 單一指數平滑

<a id="formula-ch17-exponential-smoothing"></a>

**單一指數平滑(single exponential smoothing)與用途** ：只選一個平滑常數，自動讓愈久以前的資料權重呈指數衰減。

$$
F_{t+1}=\alpha Y_t+(1-\alpha)F_t,\qquad 0\le\alpha\le1
$$

| 符號 | 意義 |
|---|---|
| $\alpha$ | 給最新實際值的權重 |
| $1-\alpha$ | 給上一期預測的權重 |
| $F_t$ | 第 $t$ 期原先預測 |

通常令第一期預測等於第一期實際值，因此 $F_2=Y_1$。Gasoline 使用 $\alpha=0.2$ 時：

$$
F_3=0.2(21)+0.8(17)=17.80
$$

$$
F_4=0.2(19)+0.8(17.80)=18.04
$$

將遞迴式展開，可見 $F_4=\alpha Y_3+\alpha(1-\alpha)Y_2+(1-\alpha)^2Y_1$。愈久以前的資料仍有影響，但權重按 $(1-\alpha)$ 逐期縮小。

<a id="formula-ch17-exponential-error-correction"></a>

同一公式也可寫成誤差修正式：

$$
F_{t+1}=F_t+\alpha(Y_t-F_t)=F_t+\alpha e_t
$$

**定性意義：** $\alpha$ 是「這次失準要立刻修正多少」。$\alpha$ 大，模型相信最近誤差代表水準真的變了，反應快但容易跟著雜訊擺動；$\alpha$ 小，模型把最近誤差多半當雜訊，較穩但較慢。$\alpha=1$ 就是樸素法，$\alpha=0$ 則永遠不更新。

選 $\alpha$ 時可比較歷史 MSE。投影片 Gasoline 在 $\alpha=0.2$ 下的歷史 MSE 小於 $\alpha=0.3$；這不是說 0.2 普遍較好，而是這段數列的平滑取捨。

### 5. 趨勢投影

#### 5.1 線性趨勢迴歸

<a id="formula-ch17-linear-trend"></a>

$$
T_t=b_0+b_1t
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $T_t$ | 第 $t$ 期的趨勢預測 | 與 $Y$ 相同 |
| $b_0$ | $t=0$ 時趨勢線截距 | 與 $Y$ 相同 |
| $b_1$ | 每過一期，平均趨勢改變量 | $Y$ 單位／期 |
| $t$ | 時間期數 | 月、季、年等 |

<a id="formula-ch17-linear-trend-coefficients"></a>

$$
b_1=\frac{\sum_{t=1}^{n}(t-\bar t)(Y_t-\bar Y)}{\sum_{t=1}^{n}(t-\bar t)^2},\qquad
b_0=\bar Y-b_1\bar t
$$

這就是第 14 章最小平方斜率，只是把自變數明確指定為時間。Bicycle 的 $\bar t=5.5$、$\bar Y=26.45$、交叉離差和 90.75、時間平方離差和 82.50，所以 $b_1=1.10$、$b_0=20.40$：

$$
T_t=20.4+1.10t
$$

$T_{11}=32.5$，即下一年預測 32.5 千輛；斜率表示歷史上每年平均增加 1.1 千輛。

**MSE 分母提醒：** 預測課程把趨勢線在 $n$ 期的平方誤差平均寫成 $SSE/n$；一般迴歸輸出估計誤差變異時則用 $SSE/(n-2)$。兩者目的不同，數字不能混抄。Bicycle 的預測 MSE 是 $30.70/10=3.07$，迴歸 ANOVA 的 MSE 則是 $30.70/8=3.8375$。

**定性意義：** $b_1$ 量長期水準每期平均移動多少，不代表每一期都剛好增加 $b_1$。資料點在趨勢線上下的散布是短期波動；斜率愈大只表示歷史平均方向更陡，不表示預測更穩，也不表示時間造成 $Y$ 改變。

#### 5.2 二次與指數趨勢

<a id="formula-ch17-quadratic-trend"></a>

$$
T_t=b_0+b_1t+b_2t^2
$$

二次項允許邊際變化 $b_1+2b_2t$ 隨時間改變。Cholesterol 例題得到：

$$
\widehat{Revenue}=24.18-2.11Year+0.922Year^2
$$

$R^2=98.12\%$，平方項 p 值 0.001，但一次項 p 值 0.317。保留一次項是為了模型階層與曲線形狀，不應只因一次項不顯著就刪除。

<a id="formula-ch17-exponential-trend"></a>

$$
T_t=b_0e^{b_1t}
$$

取自然對數後：

$$
\ln(T_t)=\ln(b_0)+b_1t
$$

投影片的 Cholesterol 指數趨勢為 $T_t=16.71e^{0.1697t}$。$e^{0.1697}\approx1.185$，表示趨勢每期約乘 1.185，也就是約成長 18.5%，不是每期增加固定 0.1697 個原單位。

二次與指數模型都能配出彎曲，但遠期外推差異巨大。二次曲線可能轉折，指數曲線則持續按比例爆發；應依資料機制、殘差與合理範圍選擇，不能只看樣本內 $R^2$。

### 6. 用虛擬變數表示季節

#### 6.1 只有季節、沒有趨勢

季度有四個類別，保留截距時只需要三個虛擬變數，第四季作參考組。

<a id="formula-ch17-seasonal-dummy"></a>

$$
\widehat Y_t=b_0+b_1Qtr1_t+b_2Qtr2_t+b_3Qtr3_t
$$

Umbrella 例題得到：

$$
\widehat Y_t=95+29Qtr1_t+57Qtr2_t+26Qtr3_t
$$

因此四季預測為 124、152、121、95，恰好等於各季五年平均。$b_0=95$ 是第四季平均；$b_2=57$ 表示第二季平均比第四季高 57，不是第二季預測只有 57。

月資料有 12 個月份，需 11 個虛擬變數；全為 0 的月份是參考月。不能放 12 個月份虛擬變數又保留截距，否則發生完全共線性。

#### 6.2 季節加線性趨勢

<a id="formula-ch17-seasonal-trend-dummy"></a>

$$
\widehat Y_t=b_0+b_1Qtr1_t+b_2Qtr2_t+b_3Qtr3_t+b_4t
$$

Smartphone 例題的正確方程式是：

$$
\widehat{Sales}=6.069-1.363Qtr1-2.034Qtr2-0.304Qtr3+0.1456t
$$

投影片第 46 頁把三個季節欄名都印成 Qtr1，並把第四季誤寫成 Qtr5；由第 44 頁模型、代入的 0-1 編碼及 11e 課本輸出可確認應為 Qtr1、Qtr2、Qtr3 與 Qtr4。

令 $t=17,18,19,20$，得到第 5 年四季預測約 7.18、6.66、8.53、8.98 千支。$b_4=0.1456$ 表示控制固定季度效果後，每季平均上升約 146 支；三個季節係數則是同一時間趨勢下相對第四季的固定差。

**定性意義：** 加法季節模型假設季節差是固定原單位，例如第二季永遠比第四季少約 2.034 千支。若水準愈高、季節振幅也按比例變大，固定差就不適合，應考慮乘法分解。

### 7. 時間數列分解

<a id="section-ch17-decomposition"></a>

分解的目標不只是預測，也是把「長期水準」「固定季節倍率」與「剩餘不規則波動」拆開，避免把正常淡旺季誤判成景氣轉折。

<a id="formula-ch17-additive-decomposition"></a>

加法分解適合季節振幅大致固定：

$$
Y_t=Trend_t+Seasonal_t+Irregular_t
$$

<a id="formula-ch17-multiplicative-decomposition"></a>

投影片聚焦乘法分解：

$$
Y_t=Trend_t\times Seasonal_t\times Irregular_t
$$

$Trend_t$ 用原單位；$Seasonal_t$ 與 $Irregular_t$ 是相對倍率。季節指數 1.14 表示該季通常比趨勢高 14%，0.84 表示通常比趨勢低 16%。它不是增加 1.14 個單位。

#### 7.1 四期中央移動平均

季度資料先算四期移動平均，但第一個四期平均位在 $t=2.5$，第二個位在 $t=3.5$。再平均兩者，才會對準整數期 $t=3$。

<a id="formula-ch17-centered-moving-average"></a>

$$
CMA_t=\frac{Y_{t-2}+2Y_{t-1}+2Y_t+2Y_{t+1}+Y_{t+2}}{8}
$$

這等同相鄰兩個四期移動平均再取平均。Smartphone 第一個 $MA_4=5.35$，第二個 $MA_4=5.60$，所以 $CMA_3=(5.35+5.60)/2=5.475$。

<a id="formula-ch17-seasonal-irregular"></a>

$$
\frac{Y_t}{CMA_t}\approx Seasonal_t\times Irregular_t
$$

第 3 期為 $6.0/5.475=1.096$，表示該期比平滑趨勢高約 9.6%，其中混合了第三季固定效果與該年不規則波動。

#### 7.2 季節指數與去季節化

<a id="formula-ch17-seasonal-index"></a>

同一季跨年平均季節不規則比，可讓正負不規則波動互相淡化：

$$
S_q=\operatorname{average}\left(\frac{Y_t}{CMA_t}:t\text{ 屬於季 }q\right)
$$

Smartphone 四季指數約為 0.93、0.84、1.09、1.14，總和約為 4。若因四捨五入或樣本造成總和不是 4，可乘上 $4/\sum S_q$ 做正規化。

<a id="formula-ch17-deseasonalize"></a>

$$
Deseasonalized_t=\frac{Y_t}{S_q}
$$

去季節化不是刪除某些季節資料，而是把旺季除以大於 1 的倍率、淡季除以小於 1 的倍率，全部換回共同基準。如此看長期變化時，不會因「本月本來就是淡季」而誤判衰退。

![Smartphone 原始銷量經中央移動平均與去季節化後，長期線性上升訊號更清楚](../figures/generated/ch17_multiplicative_decomposition.png)

你該注意什麼：上圖的中央移動平均先壓低季度節奏；下圖除去固定季節倍率後，線性趨勢更清楚。資料來自投影片 Smartphone 例題。

去季節化資料的趨勢線為：

$$
\widehat{Deseasonalized\ Sales}=5.104+0.1476t
$$

第 17 至 20 期的去季節化趨勢預測為 7.613、7.761、7.908、8.056 千支。

<a id="formula-ch17-reseasonalize"></a>

最後把趨勢預測乘回各季指數：

$$
Forecast_t=TrendForecast_t\times S_q
$$

例如第 19 期是第三季，$7908(1.09)=8620$ 支。四季完整預測約為 7080、6519、8620、9184 支。

**定性意義：** 分解是在問「觀察值偏高，是因長期基準變高、這季本來就旺，還是一次性事件？」季節指數愈偏離 1，固定季節節奏愈強；去季節化後若點仍沿趨勢緊密排列，長期訊號相對清楚。這仍不表示不規則成分消失，也不保證季節倍率未來不變。

#### 7.3 簡化季節指數

考古題有些只給每季三年資料並直接提供趨勢式，未要求中央移動平均。此時採每季平均除以全體平均：

<a id="formula-ch17-simple-seasonal-index"></a>

$$
S_q=\frac{\text{第 }q\text{ 季跨年平均}}{\text{所有觀察值總平均}}
$$

這適合題目明確採簡化法、且趨勢影響不強的情況。若數列有明顯趨勢，應優先用中央移動平均的 ratio-to-moving-average 方法，否則前後年份的水準差可能混進季節指數。

### 8. 本章方法選擇流程

<a id="compare-ch17-forecast-methods"></a>
<a id="compare-ch17-method-selection"></a>

1. 先畫圖，確認時間間隔與型態。
2. 水平、無季節：移動平均、加權移動平均或單一指數平滑。
3. 線性趨勢：時間趨勢迴歸。
4. 彎曲趨勢：有機制支持時用二次或指數趨勢。
5. 固定季節差：季節虛擬變數的加法模型。
6. 季節振幅隨水準按比例放大：乘法分解。
7. 用相同歷史評估期間比較 MAE、MSE 或 MAPE，再檢查結構改變與外推風險。

### 9. 把數字翻成真實意義

| 數字或關係 | 變大或變小代表什麼 | 資料世界的意義 | 不能直接推論 |
|---|---|---|---|
| $|e_t|$ | 愈大表示該期預測離實際愈遠 | 單期失準幅度 | 方法未來一定不好 |
| MAE | 愈小表示一般期的原單位失準較小 | 典型預測偏離 | 沒有重大尾端風險 |
| MSE | 愈大常由少數大錯或普遍失準造成 | 對大錯更敏感 | 可與不同尺度資料直接比 |
| MAPE | 愈小表示相對規模失準較小 | 跨量級較易比較 | 實際值接近 0 時仍可靠 |
| $k$ | 愈大，移動平均愈平滑 | 更多舊資料共同決定目前水準 | 反應一定更好 |
| $\alpha$ | 愈大，愈重視最近實際值 | 對水準改變反應快，也較容易追雜訊 | 愈大必然愈準 |
| $b_1$ | 絕對值愈大，長期水準每期移動愈快 | 歷史平均趨勢較陡 | 時間造成結果改變 |
| $S_q$ | 離 1 愈遠，該季相對趨勢的倍率愈強 | 固定淡旺季節奏較明顯 | 每一年都精確乘同一倍率 |
| CMA | 愈平滑，短期季節與雜訊被壓得愈多 | 提取較慢移動的趨勢循環 | 已完全消除所有不規則波動 |

## 跟前面像的東西怎麼分

### 比較 1：一般移動平均 vs 中央移動平均

<a id="compare-ch17-ma-vs-cma"></a>

| 方法 | 要回答的問題 | 能否拿來即時預測下一期 |
|---|---|---|
| [一般移動平均](#formula-ch17-moving-average) | 用最近 $k$ 期預測下一期 | 可以，只用過去資料 |
| [中央移動平均](#formula-ch17-centered-moving-average) | 對齊週期中心，估計歷史趨勢以拆季節 | 不可以直接即時預測，因為用到 $t$ 後面的資料 |

**一句話判斷準則：** 題目說 forecast next period，用尾端移動平均；題目說 decomposition 或 centered moving average，用中央移動平均。

**容易誤選情境：** 用未來兩季資料計算第 $t$ 季的 CMA，再宣稱那是當時可做出的預測。CMA 是歷史分解工具，不是當時的即時預測。

### 比較 2：單一指數平滑 vs 線性趨勢

| 方法 | 適合型態 | 核心參數 |
|---|---|---|
| [單一指數平滑](#formula-ch17-exponential-smoothing) | 水平型，沒有明顯趨勢與季節 | $\alpha$ 控制反應速度 |
| [線性趨勢](#formula-ch17-linear-trend) | 長期水準每期大致固定量移動 | $b_1$ 是每期平均變化 |

**一句話判斷準則：** 中心固定但有隨機起伏用單一平滑；中心本身持續移動用趨勢。

**容易誤選情境：** 銷量每年穩定成長，卻用很小 $\alpha$ 的單一平滑；預測會一直落後趨勢。

### 比較 3：時間趨勢迴歸 vs 因果迴歸

| 方法 | 自變數 | 能回答什麼 |
|---|---|---|
| [時間趨勢迴歸](#formula-ch17-linear-trend) | 時間 $t$ | 歷史平均路徑如何移動 |
| [複迴歸](15-multiple-regression.md#formula-multiple-regression-model) | 價格、廣告、所得等 | 控制其他欄位後的條件關聯與預測 |

**一句話判斷準則：** 只用期數延伸歷史形狀是時間趨勢；用外部解釋變數預測是因果型迴歸框架。

**容易誤選情境：** 銷售與時間一起上升，就說「時間造成銷售」。時間只是趨勢索引，真正機制可能是人口、價格或技術。

### 比較 4：季節虛擬變數 vs 乘法分解

| 方法 | 季節效果形式 | 最適資料長相 |
|---|---|---|
| [季節加趨勢迴歸](#formula-ch17-seasonal-trend-dummy) | 固定原單位差 | 不同年份季節振幅約相同 |
| [乘法分解](#formula-ch17-multiplicative-decomposition) | 固定相對倍率 | 水準愈高，季節振幅也按比例變大 |

**一句話判斷準則：** 旺季永遠多固定數量用加法；旺季永遠高固定百分比用乘法。

**容易誤選情境：** 銷量從 100 成長到 1000，旺季落差也從 20 放大到 200，卻用固定加 20 的虛擬變數模型。

### 比較 5：時間數列預測 vs Durbin-Watson 殘差診斷

| 方法 | 目標 | 輸入 |
|---|---|---|
| 本章平滑、趨勢與分解 | 直接建立未來 $Y_t$ 的預測 | 歷史時間數列 |
| [第 16 章 Durbin-Watson](16-regression-model-building.md#formula-durbin-watson) | 檢查迴歸殘差是否有一階自相關 | 按時間排序的殘差 |

**一句話判斷準則：** 要產生預測用本章模型；要檢查既有迴歸是否留下連續同號誤差，才用 DW。

**容易誤選情境：** 看到月份資料就直接算 DW，卻還沒有先配適模型與取得殘差。DW 檢查的是殘差連續性，不是原始銷量有沒有趨勢。

## 考古題與詳解

題本內頁標為 Chapter 18，但課程投影片封面標為第 17 章；以下依本課程章次收錄，同時忠實保留原題中的 Exhibit 18-x 名稱。題本共 37 題選擇題與 31 題 Problem。

### 選擇題｜第 1–37 題

#### 選擇題 1

##### 題目

> Which of the following is not present in a time series?
>
> a. seasonality<br>
> b. operational variations<br>
> c. trend<br>
> d. cycles

##### 詳解

1. **辨認題型：** 時間數列組成辨識。
2. **選方法：** 依[時間數列型態](#section-ch17-patterns)分辨標準成分。
3. **檢查假設：** 問的是課本標準術語，不需數值假設。
4. **代入計算／推理：** trend、seasonality、cycles 都是標準成分；operational variations 不是。
5. **解讀結論：** 答案是 **b** 。a 是固定週期，c 是長期方向，d 是多年循環；b 只是一般文字，不是本章成分名稱。

#### 選擇題 2

##### 題目

> Given an actual demand of 61, forecast of 58, and an $\alpha$ of .3, what would the forecast for the next period be using simple exponential smoothing?
>
> a. 57.1<br>
> b. 58.9<br>
> c. 61.0<br>
> d. 65.5

##### 詳解

1. **辨認題型：** 單一指數平滑更新。
2. **選方法：** 使用[指數平滑公式](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $0\le0.3\le1$，且 61 是本期實際值、58 是本期預測。
4. **代入計算／推理：** $F_{t+1}=0.3(61)+0.7(58)=58.9$。
5. **解讀結論：** 答案是 **b** 。a 把修正方向弄反；c 等同只看實際值；d 超出兩個輸入的加權平均範圍。

#### 選擇題 3

##### 題目

> Which of the following smoothing constants would make an exponential smoothing forecast equivalent to a naive forecast?
>
> a. 0<br>
> b. 1 divided by the number of periods<br>
> c. 0.5<br>
> d. 1.0

##### 詳解

1. **辨認題型：** 指數平滑與樸素法的邊界關係。
2. **選方法：** 比較[樸素法](#formula-ch17-naive-forecast)與[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 樸素法要令下一期等於最新實際值。
4. **代入計算／推理：** $\alpha=1$ 時，$F_{t+1}=Y_t$。
5. **解讀結論：** 答案是 **d** 。a 完全不更新；b 不是必要關係；c 仍混合舊預測。

#### 選擇題 4

##### 題目

> The time series component which reflects a regular, multi-year pattern of being above and below the trend line is
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

1. **辨認題型：** 多年上下波動的名稱。
2. **選方法：** 依[季節與循環比較](#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 關鍵字是 multi-year 且圍繞趨勢線。
4. **代入計算／推理：** 這是 cyclical component。
5. **解讀結論：** 答案是 **c** 。a 是長期方向；b 通常是一年內固定週期；d 是無規律突發。

#### 選擇題 5

##### 題目

> The time series component that reflects variability during a single year is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

1. **辨認題型：** 一年內固定節奏。
2. **選方法：** 使用[季節型定義](#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 題意是可重複的一年內變動。
4. **代入計算／推理：** 對應 seasonal component。
5. **解讀結論：** 答案是 **b** 。a 不要求一年重複；c 跨多年；d 無固定節奏。

#### 選擇題 6

##### 題目

> The time series component that reflects variability due to natural disasters is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

1. **辨認題型：** 突發事件成分。
2. **選方法：** 對照[不規則成分](#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 天災不是固定週期，也不是可延伸趨勢。
4. **代入計算／推理：** 應歸為 irregular。
5. **解讀結論：** 答案是 **d** 。a、b、c 都暗示某種可辨認規律，與突發天災不符。

#### 選擇題 7

##### 題目

> The time series component that reflects gradual variability over a long time period is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

1. **辨認題型：** 長期逐步移動。
2. **選方法：** 對照[趨勢型](#section-ch17-trend-patterns)。
3. **檢查假設：** 關鍵是 gradual 與 long time period，不是上下循環。
4. **代入計算／推理：** 對應 trend。
5. **解讀結論：** 答案是 **a** 。b 是固定短週期；c 是多年在趨勢上下交替；d 無規則。

#### 選擇題 8

##### 題目

> The trend component is easy to identify by using
>
> a. moving averages<br>
> b. exponential smoothing<br>
> c. regression analysis<br>
> d. the Delphi approach

##### 詳解

1. **辨認題型：** 趨勢估計工具。
2. **選方法：** 使用[線性趨勢迴歸](#formula-ch17-linear-trend)。
3. **檢查假設：** 題目問明確估計趨勢線，不只是平滑短期波動。
4. **代入計算／推理：** 把 $t$ 當自變數的 regression 可估斜率。
5. **解讀結論：** 答案是 **c** 。a、b 未修正時主要處理水平型；d 是定性預測。

#### 選擇題 9

##### 題目

> The forecasting method that is appropriate when the time series has no significant trend, cyclical, or seasonal effect is
>
> a. moving averages<br>
> b. mean squared error<br>
> c. mean average deviation<br>
> d. qualitative forecasting methods

##### 詳解

1. **辨認題型：** 水平型數列選方法。
2. **選方法：** 依[本章方法選擇流程](#compare-ch17-forecast-methods)。
3. **檢查假設：** 已明示無趨勢、循環與季節。
4. **代入計算／推理：** moving averages 是水平型平滑法；MSE、MAD 是誤差指標。
5. **解讀結論：** 答案是 **a** 。b、c 不會產生預測；d 通常用於歷史資料不可用。

#### 選擇題 10

##### 題目

> If data for a time series analysis is collected on an annual basis only, which component may be ignored?
>
> a. trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

1. **辨認題型：** 取樣頻率與季節成分。
2. **選方法：** 依[季節型定義](#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 每年只有一筆，沒有一年內月份或季度位置。
4. **代入計算／推理：** 一年內季節差已無法在年度資料中分辨。
5. **解讀結論：** 答案是 **b** 。年度資料仍可能有趨勢、跨年循環與不規則波動。

#### 選擇題 11

##### 題目

> For the following time series, you are given the moving average forecast.

| Time Period | Time Series Value | Moving Average Forecast |
|---:|---:|---:|
| 1 | 23 |  |
| 2 | 17 |  |
| 3 | 17 |  |
| 4 | 26 | 19 |
| 5 | 11 | 20 |
| 6 | 23 | 18 |
| 7 | 17 | 20 |

> The mean squared error equals
>
> a. 0<br>
> b. 6<br>
> c. 41<br>
> d. 164

##### 詳解

1. **辨認題型：** 已知預測的 MSE。
2. **選方法：** 使用[MSE](#formula-ch17-mse)。
3. **檢查假設：** 只有第 4 至 7 期共 4 個誤差。
4. **代入計算／推理：** 平方誤差為 $7^2+(-9)^2+5^2+(-3)^2=164$，故 $MSE=164/4=41$。
5. **解讀結論：** 答案是 **c** 。d 是平方誤差總和，漏除 4；a、b 都不是依表計算的結果。

#### 選擇題 12

##### 題目

> If the estimate of the trend component is 158.2, the estimate of the seasonal component is 94%, the estimate of the cyclical component is 105%, and the estimate of the irregular component is 98%, then the multiplicative model will produce a forecast of
>
> a. 1.53<br>
> b. 1.53%<br>
> c. 153.02<br>
> d. 153,020,532

##### 詳解

1. **辨認題型：** 乘法分解合成。
2. **選方法：** 使用[乘法分解](#formula-ch17-multiplicative-decomposition)。
3. **檢查假設：** 百分比要換成倍率 0.94、1.05、0.98。
4. **代入計算／推理：** $158.2(0.94)(1.05)(0.98)=153.020532$。
5. **解讀結論：** 答案是 **c** 。a、b 把尺度弄錯；d 未正確把百分比換倍率。

#### 選擇題 13

##### 題目

> Below you are given the first four values of a time series.

| Time Period | Time Series Value |
|---:|---:|
| 1 | 18 |
| 2 | 20 |
| 3 | 25 |
| 4 | 17 |

> Using a 4-period moving average, the forecasted value for period 5 is
>
> a. 2.5<br>
> b. 17<br>
> c. 20<br>
> d. 10

##### 詳解

1. **辨認題型：** 四期移動平均預測。
2. **選方法：** 使用[移動平均](#formula-ch17-moving-average)。
3. **檢查假設：** 第 5 期只使用前四期。
4. **代入計算／推理：** $F_5=(18+20+25+17)/4=20$。
5. **解讀結論：** 答案是 **c** 。b 只抄最近值；a、d 都不是四期平均。

#### 選擇題 14

##### 題目

> Below you are given the first two values of a time series. You are also given the first two values of the exponential smoothing forecast.

| Time Period $(t)$ | Time Series Value $(Y_t)$ | Forecast $(F_t)$ |
|---:|---:|---:|
| 1 | 18 | 18 |
| 2 | 22 | 18 |

> If the smoothing constant equals .3, then the exponential smoothing forecast for time period three is
>
> a. 18<br>
> b. 19.2<br>
> c. 20<br>
> d. 40

##### 詳解

1. **辨認題型：** 指數平滑下一期。
2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 更新時用 $Y_2=22,F_2=18$。
4. **代入計算／推理：** $F_3=0.3(22)+0.7(18)=19.2$。
5. **解讀結論：** 答案是 **b** 。a 未更新；c 是未加權平均；d 是相加未加權。

#### 選擇題 15

##### 題目

> The following linear trend expression was estimated using a time series with 17 time periods.
>
> $$T_t=129.2+3.8t$$
>
> The trend projection for time period 18 is
>
> a. 68.4<br>
> b. 193.8<br>
> c. 197.6<br>
> d. 6.84

##### 詳解

1. **辨認題型：** 線性趨勢代入。
2. **選方法：** 使用[線性趨勢](#formula-ch17-linear-trend)。
3. **檢查假設：** 下一期是 $t=18$，不是再加 18。
4. **代入計算／推理：** $T_{18}=129.2+3.8(18)=197.6$。
5. **解讀結論：** 答案是 **c** 。a 只有斜率乘期數；b 誤用 $t=17$；d 小數位錯。

<a id="quiz-ch17-exhibit-1"></a>

#### 題組 17-1：選擇題 16–17 共用資料

> Exhibit 18-1<br>
> Below you are given the first five values of a quarterly time series. The multiplicative model is appropriate and a four-quarter moving average will be used.

| Year | Quarter | Time Series Value $Y_t$ |
|---:|---:|---:|
| 1 | 1 | 36 |
| 1 | 2 | 24 |
| 1 | 3 | 16 |
| 1 | 4 | 20 |
| 2 | 1 | 44 |

#### 選擇題 16

##### 題目

> Refer to Exhibit 18-1. An estimate of the trend component times the cyclical component $(T_tC_t)$ for Quarter 3 of Year 1, when a four-quarter moving average is used, is
>
> a. 24<br>
> b. 25<br>
> c. 26<br>
> d. 28

##### 詳解

1. **辨認題型：** 偶數週期中央移動平均。
2. **選方法：** 使用[中央移動平均](#formula-ch17-centered-moving-average)。
3. **檢查假設：** 兩個四期平均分別中心在 2.5 與 3.5，再平均才對準第 3 期。
4. **代入計算／推理：** $MA_1=(36+24+16+20)/4=24$，$MA_2=(24+16+20+44)/4=26$，$CMA_3=(24+26)/2=25$。
5. **解讀結論：** 答案是 **b** 。a、c 是未置中的四期平均；d 無此計算來源。

#### 選擇題 17

##### 題目

> Refer to Exhibit 18-1. An estimate of the seasonal-irregular component for Quarter 3 of Year 1 is
>
> a. .64<br>
> b. 1.5625<br>
> c. 5.333<br>
> d. 30

##### 詳解

1. **辨認題型：** 季節不規則比。
2. **選方法：** 使用[$Y_t/CMA_t$](#formula-ch17-seasonal-irregular)。
3. **檢查假設：** 第 3 期實際值 16，趨勢循環估計 25。
4. **代入計算／推理：** $16/25=0.64$。
5. **解讀結論：** 答案是 **a** 。b 是倒數；c、d 不是比例。0.64 表示該期比趨勢低約 36%。

#### 選擇題 18

##### 題目

> You are given the following information on the seasonal-irregular component values for a quarterly time series:

| Quarter | Seasonal-Irregular Component Values $(S_tI_t)$ |
|---:|---|
| 1 | 1.23, 1.15, 1.16 |
| 2 | .86, .89, .83 |
| 3 | .77, .72, .79 |
| 4 | 1.20, 1.13, 1.17 |

> The seasonal index for Quarter 1 is
>
> a. .997<br>
> b. 1.18<br>
> c. 4<br>
> d. 3

##### 詳解

1. **辨認題型：** 同季跨年平均。
2. **選方法：** 使用[季節指數](#formula-ch17-seasonal-index)。
3. **檢查假設：** 只平均 Quarter 1 的三個比值。
4. **代入計算／推理：** $(1.23+1.15+1.16)/3=1.18$。
5. **解讀結論：** 答案是 **b** 。a 接近全部比值總平均；c、d 把季數或筆數當指數。1.18 表示第一季通常高於趨勢約 18%。

#### 選擇題 19

##### 題目

> Below you are given some values of a time series consisting of 26 time periods.

| Time Period | Time Series Value |
|---:|---:|
| 1 | 37 |
| 2 | 48 |
| 3 | 50 |
| 4 | 63 |
| $\vdots$ | $\vdots$ |
| 23 | 105 |
| 24 | 107 |
| 25 | 112 |
| 26 | 114 |

> The estimated regression equation for these data is
>
> $$Y_t=16.23+.52Y_{t-1}+.37Y_{t-2}$$
>
> The forecasted value for time period 27 is
>
> a. 53.23<br>
> b. 109.5<br>
> c. 116.65<br>
> d. 116.95

##### 詳解

1. **辨認題型：** 兩期落後值自我迴歸代入。
2. **選方法：** 依方程式直接使用第 26、25 期，並以[本章方法流程](#compare-ch17-method-selection)確認不是趨勢式。
3. **檢查假設：** $Y_{t-1}=114,Y_{t-2}=112$。
4. **代入計算／推理：** $16.23+0.52(114)+0.37(112)=116.95$。
5. **解讀結論：** 答案是 **d** 。a、b 漏項或索引錯；c 是算術誤差。

#### 選擇題 20

##### 題目

> A group of observations measured at successive time intervals is known as
>
> a. a trend component<br>
> b. a time series<br>
> c. a forecast<br>
> d. an additive time series model

##### 詳解

1. **辨認題型：** 基本定義。
2. **選方法：** 使用[時間數列資料結構](#section-ch17-data-structure)。
3. **檢查假設：** successive time intervals 是關鍵。
4. **代入計算／推理：** 按連續時間間隔量得的一組觀察即 time series。
5. **解讀結論：** 答案是 **b** 。a 只是成分；c 是未來估計；d 是一種分解模型。

#### 選擇題 21

##### 題目

> A component of the time series model that results in the multi-period above-trend and below-trend behavior of a time series is
>
> a. a trend component<br>
> b. a cyclical component<br>
> c. a seasonal component<br>
> d. an irregular component

##### 詳解

1. **辨認題型：** 趨勢線上下的多期段落。
2. **選方法：** 對照[循環型](#section-ch17-seasonal-cyclical)。
3. **檢查假設：** multi-period 指超過短季節的上下段落。
4. **代入計算／推理：** 對應 cyclical component。
5. **解讀結論：** 答案是 **b** 。a 是基準方向；c 固定短週期；d 沒有可重複結構。

#### 選擇題 22

##### 題目

> The model that assumes that the actual time series value is the product of its components is the
>
> a. forecast time series model<br>
> b. multiplicative time series model<br>
> c. additive time series model<br>
> d. None of these alternatives is correct.

##### 詳解

1. **辨認題型：** 分解模型形式。
2. **選方法：** 使用[乘法分解](#formula-ch17-multiplicative-decomposition)。
3. **檢查假設：** product 表示相乘，不是相加。
4. **代入計算／推理：** $Y_t=T_tS_tI_t$ 是 multiplicative model。
5. **解讀結論：** 答案是 **b** 。a 不是標準名稱；c 用加法；d 因 b 正確而錯。

#### 選擇題 23

##### 題目

> A method of smoothing a time series that can be used to identify the combined trend/cyclical component is
>
> a. the moving average<br>
> b. the percent of trend<br>
> c. exponential smoothing<br>
> d. the trend/cyclical index

##### 詳解

1. **辨認題型：** 分解法中提取慢速成分。
2. **選方法：** 使用[中央移動平均](#formula-ch17-centered-moving-average)。
3. **檢查假設：** 週期長度已知，移動平均用來壓低季節與不規則波動。
4. **代入計算／推理：** moving average 估計趨勢循環。
5. **解讀結論：** 答案是 **a** 。b 是比例概念；c 是水平型預測法；d 不是此處計算方法。

#### 選擇題 24

##### 題目

> A method that uses a weighted average of past values for arriving at smoothed time series values is known as
>
> a. a smoothing average<br>
> b. a moving average<br>
> c. an exponential average<br>
> d. an exponential smoothing

##### 詳解

1. **辨認題型：** 指數衰減權重的名稱。
2. **選方法：** 使用[單一指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 題意強調過去值的加權平均，不是等權平均。
4. **代入計算／推理：** 標準名稱是 exponential smoothing。
5. **解讀結論：** 答案是 **d** 。b 通常等權；a、c 不是標準術語。

#### 選擇題 25

##### 題目

> In the linear trend equation, $T=b_0+b_1t$, $b_1$ represents the
>
> a. trend value in period t<br>
> b. intercept of the trend line<br>
> c. slope of the trend line<br>
> d. point in time

##### 詳解

1. **辨認題型：** 線性趨勢符號。
2. **選方法：** 使用[線性趨勢](#formula-ch17-linear-trend)。
3. **檢查假設：** 問的是 $b_1$。
4. **代入計算／推理：** $b_1$ 是時間每增一期，趨勢平均改變量。
5. **解讀結論：** 答案是 **c** 。a 是 $T_t$；b 是 $b_0$；d 是 $t$。

#### 選擇題 26

##### 題目

> In the linear trend equation, $T=b_0+b_1t$, $b_0$ represents the
>
> a. time<br>
> b. slope of the trend line<br>
> c. trend value in period 1<br>
> d. the Y intercept

##### 詳解

1. **辨認題型：** 線性趨勢截距。
2. **選方法：** 使用[線性趨勢](#formula-ch17-linear-trend)。
3. **檢查假設：** 截距是 $t=0$，不是第 1 期。
4. **代入計算／推理：** $b_0$ 為 Y intercept。
5. **解讀結論：** 答案是 **d** 。a 是 $t$；b 是 $b_1$；c 應為 $b_0+b_1$。

#### 選擇題 27

##### 題目

> A parameter of the exponential smoothing model which provides the weight given to the most recent time series value in the calculation of the forecast value is known as the
>
> a. mean square error<br>
> b. mean absolute deviation<br>
> c. smoothing constant<br>
> d. None of these alternatives is correct.

##### 詳解

1. **辨認題型：** 指數平滑參數名稱。
2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 最近實際值的權重為 $\alpha$。
4. **代入計算／推理：** $\alpha$ 稱 smoothing constant。
5. **解讀結論：** 答案是 **c** 。a、b 是誤差指標；d 因 c 正確而錯。

#### 選擇題 28

##### 題目

> One measure of the accuracy of a forecasting model is
>
> a. the smoothing constant<br>
> b. a deseasonalized time series<br>
> c. the mean square error<br>
> d. None of these alternatives is correct.

##### 詳解

1. **辨認題型：** 預測準確度指標。
2. **選方法：** 使用[MSE](#formula-ch17-mse)。
3. **檢查假設：** 問的是 accuracy measure。
4. **代入計算／推理：** mean square error 直接彙總預測誤差。
5. **解讀結論：** 答案是 **c** 。a 是模型設定；b 是調整後資料；d 不成立。

#### 選擇題 29

##### 題目

> A qualitative forecasting method that obtains forecasts through "group consensus" is known as the
>
> a. Autoregressive model<br>
> b. Delphi approach<br>
> c. mean absolute deviation<br>
> d. None of these alternatives is correct.

##### 詳解

1. **辨認題型：** 定性預測術語。
2. **選方法：** 依[預測方法分類](#section-ch17-data-structure)。
3. **檢查假設：** 關鍵字是 group consensus。
4. **代入計算／推理：** 對應 Delphi approach。
5. **解讀結論：** 答案是 **b** 。a 是定量模型；c 是誤差指標；d 因 b 正確而錯。

<a id="quiz-ch17-exhibit-2"></a>

#### 題組 17-2：選擇題 30–33 共用資料

> Exhibit 18-2<br>
> Consider the following time series.

| $t$ | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|
| $Y_i$ | 4 | 7 | 9 | 10 |

以[線性趨勢係數](#formula-ch17-linear-trend-coefficients)獨立重算得 $\bar t=2.5$、$\bar Y=7.5$、$b_1=2$、$b_0=2.5$，所以 $T_t=2.5+2t$。

#### 選擇題 30

##### 題目

> Refer to Exhibit 18-2. The slope of linear trend equation, $b_1$, is
>
> a. 2.5<br>
> b. 2.0<br>
> c. 1.0<br>
> d. 1.25

##### 詳解

1. **辨認題型：** 線性趨勢斜率。
2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 四期等距。
4. **代入計算／推理：** 交叉離差和 10，時間平方離差和 5，故 $b_1=2$。
5. **解讀結論：** 答案是 **b** 。a 是截距；c、d 都不符合最小平方計算。

#### 選擇題 31

##### 題目

> Refer to Exhibit 18-2. The intercept, $b_0$, is
>
> a. 2.5<br>
> b. 2.0<br>
> c. 1.0<br>
> d. 1.25

##### 詳解

1. **辨認題型：** 趨勢截距。
2. **選方法：** 使用 $b_0=\bar Y-b_1\bar t$。
3. **檢查假設：** 已驗得 $b_1=2$。
4. **代入計算／推理：** $b_0=7.5-2(2.5)=2.5$。
5. **解讀結論：** 答案是 **a** 。b 是斜率；c、d 是錯誤代入。

#### 選擇題 32

##### 題目

> Refer to Exhibit 18-2. The forecast for period 5 is
>
> a. 10.0<br>
> b. 2.5<br>
> c. 12.5<br>
> d. 4.5

##### 詳解

1. **辨認題型：** 趨勢投影。
2. **選方法：** 使用 $T_t=2.5+2t$。
3. **檢查假設：** 代入下一期 $t=5$。
4. **代入計算／推理：** $T_5=2.5+2(5)=12.5$。
5. **解讀結論：** 答案是 **c** 。a 是最近實際值；b 只取截距；d 漏乘期數。

#### 選擇題 33

##### 題目

> Refer to Exhibit 18-2. The forecast for period 10 is
>
> a. 10.0<br>
> b. 25.0<br>
> c. 30.0<br>
> d. 22.5

##### 詳解

1. **辨認題型：** 較遠期趨勢外推。
2. **選方法：** 使用 $T_t=2.5+2t$。
3. **檢查假設：** 數值可算，但從第 4 期外推到第 10 期風險較高。
4. **代入計算／推理：** $T_{10}=2.5+20=22.5$。
5. **解讀結論：** 答案是 **d** 。a 是歷史值；b、c 漏截距或誤算。22.5 是條件式外推，不是保證。

<a id="quiz-ch17-exhibit-3"></a>

#### 題組 17-3：選擇題 34–37 共用資料

> Exhibit 18-3<br>
> Consider the following time series.

| Year $(t)$ | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| $Y_i$ | 7 | 5 | 4 | 2 | 1 |

獨立重算得 $\bar t=3$、$\bar Y=3.8$、$b_1=-1.5$、$b_0=8.3$，所以 $T_t=8.3-1.5t$。

#### 選擇題 34

##### 題目

> Refer to Exhibit 18-3. The slope of linear trend equation, $b_1$, is
>
> a. -1.5<br>
> b. +1.5<br>
> c. 8.3<br>
> d. -8.3

##### 詳解

1. **辨認題型：** 下降趨勢斜率。
2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 數列隨時間下降，斜率應為負。
4. **代入計算／推理：** 交叉離差和 $-15$，時間平方離差和 10，故 $b_1=-1.5$。
5. **解讀結論：** 答案是 **a** 。b 方向錯；c 是截距；d 把截距符號誤植。

#### 選擇題 35

##### 題目

> Refer to Exhibit 18-3. The intercept, $b_0$, is
>
> a. -1.5<br>
> b. +1.5<br>
> c. 8.3<br>
> d. -8.3

##### 詳解

1. **辨認題型：** 趨勢截距。
2. **選方法：** 使用 $b_0=\bar Y-b_1\bar t$。
3. **檢查假設：** $b_1=-1.5$。
4. **代入計算／推理：** $b_0=3.8-(-1.5)(3)=8.3$。
5. **解讀結論：** 答案是 **c** 。a、b 是斜率候選；d 符號錯。

#### 選擇題 36

##### 題目

> Refer to Exhibit 18-3. In which time period does the value of $Y_i$ reach zero?
>
> a. 0.000<br>
> b. 0.181<br>
> c. 5.53<br>
> d. 4.21

##### 詳解

1. **辨認題型：** 解趨勢線與 0 的交點。
2. **選方法：** 令 $T_t=8.3-1.5t=0$。
3. **檢查假設：** 這是連續趨勢線的交點，實際離散期數未必剛好為 0。
4. **代入計算／推理：** $t=8.3/1.5=5.533$。
5. **解讀結論：** 答案是 **c** 。a 是預測值；b 是倒數量級；d 是錯誤移項。

#### 選擇題 37

##### 題目

> Refer to Exhibit 18-3. The forecast for period 10 is
>
> a. 6.7<br>
> b. -6.7<br>
> c. 23.3<br>
> d. 15

##### 詳解

1. **辨認題型：** 下降趨勢遠期外推。
2. **選方法：** 使用 $T_t=8.3-1.5t$。
3. **檢查假設：** 數學可外推，但若 $Y$ 不可能為負，模型在第 10 期已失去實質合理性。
4. **代入計算／推理：** $T_{10}=8.3-15=-6.7$。
5. **解讀結論：** 算術答案是 **b** 。a 忘了負號；c、d 誤加。負預測正是不能盲目遠期外推的警訊。

### 計算題｜第 1–31 題

#### 計算題 1

##### 題目

> Consider the time series $(t,Y_t)$: $(1,18),(2,20),(3,22),(4,24),(5,26),(6,28)$.<br>
> a. Develop a linear trend equation.<br>
> b. What is the forecast for $t=17$?

##### 詳解

1. **辨認題型：** 完全線性的趨勢投影。
2. **選方法：** 使用[線性趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 每期等距；外推到 17 很遠，實務風險高。
4. **代入計算／推理：** 每期固定增加 2，$b_1=2,b_0=16$，故 $T_t=16+2t$；$T_{17}=50$。
5. **解讀結論：** 預測為 50；它延續固定增量，不是保證第 17 期一定等於 50。

#### 計算題 2

##### 題目

> Demand from January through June is 40, 45, 57, 60, 75, 87. Use a three-month weighted moving average with weights 5, 3, and 2, largest for the most recent data. Show forecasts for April through July.

##### 詳解

1. **辨認題型：** 三期加權移動平均。
2. **選方法：** 使用[加權移動平均](#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 10，要正規化。
4. **代入計算／推理：** $F_{Apr}=50.0$、$F_{May}=56.1$、$F_{Jun}=66.9$、$F_{Jul}=78.0$。
5. **解讀結論：** July 預測 78；近期需求權重最大，所以預測會比等權平均更靠近 87。

#### 計算題 3

##### 題目

> Use the same January–June demands 40, 45, 57, 60, 75, 87 and weights 6, 4, and 2, largest for the most recent data. Show forecasts for April through July.

##### 詳解

1. **辨認題型：** 改權重的三期加權平均。
2. **選方法：** 使用[加權移動平均](#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 12。
4. **代入計算／推理：** 預測依序為 50.167、56.5、67.0、78.5。
5. **解讀結論：** July 預測 78.5；比題 2 更重視近期，所以在上升資料中稍高。

#### 計算題 4

##### 題目

> Demand from January through June is 80, 83, 87, 90, 95, 98. Use weights 5, 4, and 3, largest for the most recent data. Show forecasts for April through July.

##### 詳解

1. **辨認題型：** 加權移動平均。
2. **選方法：** 使用[加權移動平均](#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 12。
4. **代入計算／推理：** $F_{Apr}=83.917$、$F_{May}=87.25$、$F_{Jun}=91.333$、$F_{Jul}=95.0$。
5. **解讀結論：** July 預測 95；上升趨勢下平滑預測會落後最新值 98。

#### 計算題 5

##### 題目

> Actual sales for January through April are 18, 23, 20, 16. Use exponential smoothing with $\alpha=0.2$ and initial January forecast 18 to forecast May. Show all computations.

##### 詳解

1. **辨認題型：** 遞迴指數平滑。
2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $F_{Jan}=18$。
4. **代入計算／推理：** $F_{Feb}=18$、$F_{Mar}=19$、$F_{Apr}=19.2$、$F_{May}=18.56$。
5. **解讀結論：** May 預測 18.56；小 $\alpha$ 只修正最近下降的一小部分。

#### 計算題 6

##### 題目

> Actual sales for January through April are 18, 25, 30, 40. Use $\alpha=0.3$ and initial January forecast 18 to forecast May.

##### 詳解

1. **辨認題型：** 指數平滑。
2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 水準持續上升，單一平滑可能落後。
4. **代入計算／推理：** $F_{Feb}=18$、$F_{Mar}=20.1$、$F_{Apr}=23.07$、$F_{May}=28.149$。
5. **解讀結論：** May 預測 28.149，明顯低於最新 40，顯示水平型方法追不上趨勢。

#### 計算題 7

##### 題目

> Sales in millions for January–April are 18, 25, 30, 40.<br>
> a. Use $\alpha=.3$, compute MSE and forecast May.<br>
> b. Repeat with $\alpha=.1$.<br>
> c. Which $\alpha$ is better by MSE?

##### 詳解

1. **辨認題型：** 比較平滑常數。
2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)與[MSE](#formula-ch17-mse)。
3. **檢查假設：** MSE 比較共同有實際值的 February–April 三期。
4. **代入計算／推理：** $\alpha=.3$ 的預測為 18、20.1、23.07、28.149，$MSE=144.545$；$\alpha=.1$ 為 18、18.7、19.83、21.847，$MSE=194.506$。
5. **解讀結論：** 歷史 MSE 支持 $\alpha=.3$；上升資料需要較快更新，但兩者都未建模趨勢。

#### 計算題 8

##### 題目

> Actual demand for observations 1–6 is 35, 30, 26, 34, 28, 38; forecasts for 2–6 are 35, 30, 26, 34, 28. Calculate MAE and MSE.

##### 詳解

1. **辨認題型：** 誤差指標。
2. **選方法：** 使用[MAE](#formula-ch17-mae)與[MSE](#formula-ch17-mse)。
3. **檢查假設：** 只有 5 個預測誤差。
4. **代入計算／推理：** 誤差 $-5,-4,8,-6,10$；$MAE=33/5=6.6$，$MSE=241/5=48.2$。
5. **解讀結論：** 一般一期約錯 6.6 單位；MSE 因 8、10 的大錯被放大。

#### 計算題 9

##### 題目

> Naive forecasts accompany actual demands 45, 48, 42, 44, 50, 60 for periods 1–6. Compute MAE and MSE.

##### 詳解

1. **辨認題型：** 樸素法回測。
2. **選方法：** 使用[樸素法](#formula-ch17-naive-forecast)、MAE 與 MSE。
3. **檢查假設：** 第 2–6 期預測為 45、48、42、44、50。
4. **代入計算／推理：** 誤差 $3,-6,2,6,10$；$MAE=27/5=5.4$，$MSE=185/5=37$。
5. **解讀結論：** 樸素法一般錯 5.4，且最後一期的大錯對 MSE 影響最大。

#### 計算題 10

##### 題目

> Monthly values are 12, 14, 10, 16, 29, 22. Using the naive method, compute MAE, MSE, and the forecast for period 7.

##### 詳解

1. **辨認題型：** 樸素預測與準確度。
2. **選方法：** 使用[樸素法](#formula-ch17-naive-forecast)。
3. **檢查假設：** 第 2–6 期誤差共 5 個。
4. **代入計算／推理：** 誤差 $2,-4,6,13,-7$；$MAE=6.4$，$MSE=54.8$，$F_7=22$。
5. **解讀結論：** 第 5 期跳升造成最大平方懲罰；下一期直接沿用 22。

#### 計算題 11

##### 題目

> Quarterly sales (millions) for 2007–2009 are Q1: 170,180,190; Q2: 111,96,120; Q3: 270,280,290; Q4: 250,220,223.<br>
> a. Compute four seasonal indexes.<br>
> b. Given $Trend=174+4t$, forecast Q1 2010.

##### 詳解

1. **辨認題型：** 簡化季節指數加趨勢。
2. **選方法：** 使用[每季平均／總平均](#formula-ch17-simple-seasonal-index)，再乘趨勢。
3. **檢查假設：** 題目未要求 CMA；總平均 200。
4. **代入計算／推理：** 季平均 180、109、280、231，指數 0.900、0.545、1.400、1.155；$T_{13}=226$，Q1 預測 $226(0.9)=203.4$。
5. **解讀結論：** Q1 通常低於總體水準 10%，故季調後預測 203.4 百萬。

#### 計算題 12

##### 題目

> Quarterly sales for 2007–2009 are Q1: 106,135,149; Q2: 256,280,292; Q3: 273,280,290; Q4: 190,180,209. Given $Trend=185.86+5.25t$, compute seasonal indexes, Q1 2010 trend-only forecast, and trend-plus-season forecast.

##### 詳解

1. **辨認題型：** 簡化季節指數。
2. **選方法：** 使用[簡化季節指數](#formula-ch17-simple-seasonal-index)。
3. **檢查假設：** 總平均 220，Q1 2010 是 $t=13$。
4. **代入計算／推理：** 指數為 0.5909、1.2545、1.2773、0.8773；$T_{13}=254.11$；Q1 完整預測 $254.11(0.5909)=150.155$。
5. **解讀結論：** 趨勢基準 254.11，但 Q1 通常僅約 59.1% 基準，所以調整後約 150.16。

#### 計算題 13

##### 題目

> Quarterly sales for 2007–2009 are Q1: 14,28,30; Q2: 20,16,18; Q3: 36,40,38; Q4: 10,14,12. Given $Trend=20.82+.336t$, compute seasonal indexes, Q1 2010 trend-only forecast, and adjusted forecast.

##### 詳解

1. **辨認題型：** 簡化季節指數。
2. **選方法：** 使用[簡化季節指數](#formula-ch17-simple-seasonal-index)。
3. **檢查假設：** 總平均 23，$t=13$。
4. **代入計算／推理：** 指數 1.0435、0.7826、1.6522、0.5217；$T_{13}=25.188$；Q1 預測 $25.188(1.0435)=26.283$。
5. **解讀結論：** Q3 季節性最強，Q4 最弱；Q1 略高於趨勢基準。

#### 計算題 14

##### 題目

> Seven yearly sales values are 12, 16, 17, 19, 18, 21, 22 million. Develop a linear trend and forecast period 10.

##### 詳解

1. **辨認題型：** 線性趨勢。
2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 年距相同；外推三年。
4. **代入計算／推理：** $b_0=12,b_1=1.464286$，$T_t=12+1.464286t$；$T_{10}=26.6429$。
5. **解讀結論：** 預測約 26.64 百萬；平均每年增加約 1.46 百萬。

#### 計算題 15

##### 題目

> University enrollment (thousands) for years 1–6 is 6.30, 7.70, 8.00, 8.20, 8.80, 8.00. Develop a linear trend and forecast year 10.

##### 詳解

1. **辨認題型：** 線性趨勢。
2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 第 6 年回落使線性趨勢不完美。
4. **代入計算／推理：** $T_t=6.63333+0.342857t$；$T_{10}=10.0619$ 千人。
5. **解讀結論：** 預測約 10.06 千人；它平滑掉單年回落，不代表回落可忽略。

#### 計算題 16

##### 題目

> Weekly sales (in thousands of dollars) are 15,16,19,18,19,20,19,22,15,21.<br>
> a. Compute a 4-week moving average. b. Compute MSE. c. Use $\alpha=.3$ for exponential smoothing. d. Forecast week 11.

##### 詳解

1. **辨認題型：** 移動平均與指數平滑比較。
2. **選方法：** 使用[移動平均](#formula-ch17-moving-average)、[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** MA 的誤差期為 5–10；指數平滑令 $F_1=Y_1$。
4. **代入計算／推理：** 四週 MA 對 5–11 期為 17,18,19,19,20,19,19.25，$MSE=46/6=7.667$。指數預測對 2–11 期為 15,15.3,16.41,16.887,17.5209,18.2646,18.4852,19.5397,18.1778,19.0244。
5. **解讀結論：** 指數平滑的 week 11 預測約 19.024；兩方法都將第 9 週低值平滑處理。

#### 計算題 17

##### 題目

> Monthly units sold (thousands) are 8,3,4,5,12,10.<br>
> a. Compute a 3-month moving average (centered). b. Compute MSE. c. Use $\alpha=.2$. d. Forecast month 7.

##### 詳解

1. **辨認題型：** 題目同時寫 forecast 與 centered，來源用語有歧義。
2. **選方法：** 依[一般 MA vs CMA](#compare-ch17-ma-vs-cma)，預測與 MSE 採只用過去的三期 MA。
3. **檢查假設：** 若字面採 CMA，會用到未來值且不能預測第 7 月。
4. **代入計算／推理：** $F_4=5,F_5=4,F_6=7,F_7=9$，$MSE=(0^2+8^2+3^2)/3=24.333$。指數平滑 $F_7=7.8368$。
5. **解讀結論：** 三期 MA 預測 9；指數平滑預測 7.837。來源的 centered 應視為誤植。

#### 計算題 18

##### 題目

> CMM sales (millions) for years 1–8 are 2,3,5,4,6,8,9,9. Develop a linear trend and forecast period 9.

##### 詳解

1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 等距年度。 4. **代入計算／推理：** $T_t=0.928571+1.071429t$，$T_9=10.5714$。
5. **解讀結論：** 預測約 10.57 百萬，歷史平均每年增約 1.07 百萬。

#### 計算題 19

##### 題目

> Auto sales (thousands) for years 1–10 are 195,200,250,270,320,380,440,460,500,500. Develop a linear trend and forecast $t=11$.

##### 詳解

1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[線性趨勢](#formula-ch17-linear-trend)。
3. **檢查假設：** 後兩期趨平，線性延伸需保留疑慮。 4. **代入計算／推理：** $T_t=136+39.181818t$；$T_{11}=567$。
5. **解讀結論：** 預測 567 千輛；近期平台化可能使線性模型高估。

#### 計算題 20

##### 題目

> Amazing Graphics quarterly sales for years 6–8 are: Y6 2.5,1.5,2.4,1.6; Y7 2.0,1.4,1.7,1.9; Y8 2.5,2.0,2.4,2.1.<br>
> a. Compute four-quarter moving averages. b. Compute seasonal factors. c. Use them to adjust the forecast for the effect of season for year 6.

##### 詳解

1. **辨認題型：** 乘法分解；part c 的 “forecast ... year 6” 來源語意不完整。
2. **選方法：** 使用[CMA 與季節指數](#formula-ch17-seasonal-index)。
3. **檢查假設：** 四期 MA 為 2.000,1.875,1.850,1.675,1.750,1.875,2.025,2.200,2.250。
4. **代入計算／推理：** 正規化季節因子 Q1–Q4 為 1.1527,0.8534,1.0823,0.9116。若 c 指去除 year 6 季節效果，則為 $2.5/1.1527=2.169$、$1.5/.8534=1.758$、$2.4/1.0823=2.218$、$1.6/.9116=1.755$。
5. **解讀結論：** Q1、Q3 偏旺，Q2、Q4 偏淡；因題目未給 year 6 的基準預測，以上採「調整 year 6 觀察值」解讀。

#### 計算題 21

##### 題目

> John's tips for days 1–7 are 18,22,17,18,28,20,12. Compute 3-day moving averages, MSE, MAD, and forecast day 7.

##### 詳解

1. **辨認題型：** 三日 MA 回測。 2. **選方法：** 使用[移動平均](#formula-ch17-moving-average)。
3. **檢查假設：** 預測 days 4–7。 4. **代入計算／推理：** 預測 19,19,21,22；誤差 $-1,9,-1,-10$；$MSE=45.75$，$MAD=MAE=5.25$。
5. **解讀結論：** day 7 的事前預測是 22；實際 12 造成最大失準。

#### 計算題 22

##### 題目

> Greeting-card sales for weeks 1–6 are 105,90,95,110,105,100. Use exponential smoothing with $\alpha=.2$, compute MSE and week 7 forecast, then compare $\alpha=.2$ with .3.

##### 詳解

1. **辨認題型：** 選平滑常數。 2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)與 MSE。
3. **檢查假設：** 共同回測 weeks 2–6。 4. **代入計算／推理：** $\alpha=.2$ 預測至 week 7 為 105,102,100.6,102.48,102.984,102.387，$MSE=75.523$；$\alpha=.3$ 的 $MSE=79.332$。
5. **解讀結論：** 歷史上 .2 較佳；week 7 預測 102.387。

#### 計算題 23

##### 題目

> Annual people assisted (hundreds) for years 1–11 are 22,24,28,24,22,24,20,26,24,28,26. Compare 3-year moving-average forecasts for 4–11 with exponential smoothing $\alpha=.4$ for 2–11 using MSE.

##### 詳解

1. **辨認題型：** 不同平滑法回測。 2. **選方法：** 各自只用當期以前資料。
3. **檢查假設：** 兩法評估起點不同，直接比較時應留意。 4. **代入計算／推理：** 三年 MA 對 4–11 為 24.667,25.333,24.667,23.333,22,23.333,23.333,26，$MSE=7.667$；指數平滑 $MSE=8.406$。
5. **解讀結論：** 依各題指定期間，三年 MA 較小；嚴格模型比較最好改用共同 4–11 期間。

#### 計算題 24

##### 題目

> Chicago temperatures for days 1–7 are 82,80,84,83,80,79,82. Use $\alpha=.2$, compute MSE and day 8 forecast, then compare with $\alpha=.3$.

##### 詳解

1. **辨認題型：** 指數平滑比較。 2. **選方法：** 使用[指數平滑](#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $F_1=82$。 4. **代入計算／推理：** .2 的 $MSE=4.033$、$F_8=81.399$；.3 的 $MSE=4.306$、$F_8=81.222$。
5. **解讀結論：** 歷史 MSE 支持 .2，day 8 預測約 81.40 度。

#### 計算題 25

##### 題目

> Yearly values for years 1–10 are 120,132,148,152,160,175,182,190,195,205. Produce forecasts for years 11 and 12.

##### 詳解

1. **辨認題型：** 長期趨勢。 2. **選方法：** 使用[線性趨勢](#formula-ch17-linear-trend)。
3. **檢查假設：** 圖形近似線性。 4. **代入計算／推理：** $T_t=115.2+9.218182t$；$T_{11}=216.6$、$T_{12}=225.818$。
5. **解讀結論：** 預測約 216.6 與 225.82，每年平均增加約 9.22。

#### 計算題 26

##### 題目

> Boat units by quarter for years 1–5 are: 300,240,240,290; 350,300,280,320; 410,400,390,410; 490,450,440,510; 540,530,520,540. Find four-quarter CMAs, plot, compute seasonal-irregular values and seasonal factors, deseasonalize, fit a linear trend, and forecast all quarters of year 6.

##### 詳解

1. **辨認題型：** 完整乘法分解。
2. **選方法：** 依[CMA→季節指數→去季節→再季節化](#section-ch17-decomposition)。
3. **檢查假設：** 季節振幅以倍率表示，四季指數正規化總和 4。
4. **代入計算／推理：** CMA 為 273.75,287.50,300,308.75,320,340,366.25,391.25,412.50,428.75,441.25,460,478.75,495,515,528.75。季節因子為 1.1132,0.9954,0.9056,0.9858。去季節資料配適得 $T_t=216.3001+17.3575t$；year 6 預測為 646.56,595.40,557.43,623.90。
5. **解讀結論：** 長期趨勢向上；Q1 旺、Q3 淡。預測同時反映上升基準與季節倍率。

#### 計算題 27

##### 題目

> John's income (thousands) for years 1–7 is 15.0,16.2,17.1,18.1,18.8,19.2,20.5. Obtain a linear trend and forecast the next 5 years.

##### 詳解

1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[趨勢係數](#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 外推逐年不確定性增加。 4. **代入計算／推理：** $T_t=14.3857+0.864286t$；years 8–12 為 21.300,22.164,23.029,23.893,24.757。
5. **解讀結論：** 歷史平均年增約 0.864 千；第五年預測最依賴趨勢延續假設。

#### 計算題 28

##### 題目

> Ajax quarterly profits for years 1–4 are 150,120,160,150; 150,130,180,160; 170,140,200,180; 200,150,230,200. Find CMAs, seasonal-irregular values, seasonal factors, and the deseasonalized series.

##### 詳解

1. **辨認題型：** 乘法分解至去季節化。 2. **選方法：** 使用[分解流程](#section-ch17-decomposition)。
3. **檢查假設：** 四季因子總和正規化為 4。 4. **代入計算／推理：** CMA 為 145,146.25,150,153.75,157.5,161.25,165,170,176.25,181.25,186.25,192.5；季節因子 1.0395,0.8199,1.1323,1.0083。去季節值逐筆為 $Y_t/S_q$。
5. **解讀結論：** Q3 約高於趨勢 13.2%，Q2 約低 18.0%；除以因子後才能公平比較跨季長期水準。

#### 計算題 29

##### 題目

> Middletown crimes for years 1–4 are 10,20,25,5; 10,30,35,25; 20,40,35,15; 20,50,45,35. Seasonal factors are .589, 1.351, 1.335, .726. Deseasonalize, estimate linear trend, and forecast all quarters of year 5.

##### 詳解

1. **辨認題型：** 已知季節因子的分解預測。 2. **選方法：** 使用[去季節化](#formula-ch17-deseasonalize)與[再季節化](#formula-ch17-reseasonalize)。
3. **檢查假設：** 因子由題目給定，直接使用。 4. **代入計算／推理：** 去季節資料依序約 16.978,14.804,18.727,6.887,16.978,22.206,26.217,34.435,33.956,29.608,26.217,20.661,33.956,37.010,33.708,48.209。趨勢 $T_t=11.1037+1.7860t$；year 5 預測 24.42,58.43,60.13,33.99。
5. **解讀結論：** 基準犯罪數呈上升；Q2、Q3 季節倍率較高。這是描述性預測，不是季節造成犯罪的證明。

#### 計算題 30

##### 題目

> Seasonal factors Q1–Q4 are 1.2, .9, .8, 1.1 and $T=126.23-1.6t$, based on five years of quarterly data. Forecast all quarters of year 6.

##### 詳解

1. **辨認題型：** 趨勢乘季節。 2. **選方法：** 使用[再季節化](#formula-ch17-reseasonalize)。
3. **檢查假設：** year 6 是 $t=21,22,23,24$。 4. **代入計算／推理：** 趨勢 92.63,91.03,89.43,87.83；乘季節後為 111.156,81.927,71.544,96.613。
5. **解讀結論：** 趨勢逐季下降，但 Q1、Q4 旺季倍率使原始預測相對較高。

#### 計算題 31

##### 題目

> Auto quarterly sales for years 8–10 are 160,180,190,170; 200,210,260,230; 210,240,290,260. Compute four-quarter moving averages, seasonal factors, and use the factors to adjust the forecast for the effect of season for year 9.

##### 詳解

1. **辨認題型：** 分解與來源語意中的 year 9 調整。
2. **選方法：** 使用[CMA 與季節指數](#formula-ch17-seasonal-index)。
3. **檢查假設：** 四期 MA 為 175,185,192.5,210,225,227.5,235,242.5,250；CMA 為 180,188.75,201.25,217.5,226.25,231.25,238.75,246.25。
4. **代入計算／推理：** 季節因子 Q1–Q4 為 0.9469,0.9807,1.1144,0.9580。若 adjust year 9 指去季節化，200,210,260,230 分別變成 211.21,214.14,233.31,240.09。
5. **解讀結論：** Q3 是旺季；year 9 去季節化後可比較共同基準。來源未提供另一組 year 9 趨勢預測，因此不臆造。
