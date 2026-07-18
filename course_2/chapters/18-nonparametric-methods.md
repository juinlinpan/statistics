---
chapter: "18"
slug: 18-nonparametric-methods
title: 第 18 章：無母數方法
source_deck: Quan1150(Nonparametric).pdf
---

# 第 18 章：無母數方法

## 先備知識

course1 沒有獨立教過無母數方法(nonparametric methods)，所以本章會從「資料能保留多少資訊」開始自給自足。不過以下三塊地基會反覆用到：

- **檢定邏輯與 p 值：** p 值是在 $H_0$ 成立時，得到至少同樣極端資料的機率，不是 $H_0$ 為真的機率。若不熟，先回看 [course1 第 8 章：顯著性檢定](../../course_1/chapters/08-significance-tests.md)。
- **二項分配與常態近似：** 符號檢定把每筆有效資料變成正號或負號，因此正號數服從二項分配；樣本大時再用常態近似。可回看 [course1 第 4 章：常態與二項分配](../../course_1/chapters/04-normal-and-binomial.md)。
- **獨立樣本與配對資料：** 同一人前後各測一次是配對資料；兩群由不同人組成則是獨立樣本。方法選錯會破壞資料原有的依存關係。可回看 [course1 第 2 章：抽樣與實驗設計](../../course_1/chapters/02-sampling-and-experiments.md)。

先把四種測量尺度分清楚，因為題庫會直接考：

| 尺度 | 資訊 | 例子 | 可以做什麼 |
|---|---|---|---|
| 名目尺度(nominal scale) | 只有類別標籤，沒有高低順序 | 婚姻狀態、瑕疵／非瑕疵 | 計數、比例、符號檢定中的二分類 |
| 次序尺度(ordinal scale) | 有順序，但相鄰名次的距離不一定相等 | 優、良、可、差；比賽名次 | 排名、秩和與等級相關 |
| 區間尺度(interval scale) | 差值有意義，零點不是絕對沒有 | 攝氏溫度 | 平均、差值、相關等 |
| 比率尺度(ratio scale) | 差值與倍數都有意義，零點是真正的零 | 速度、時間、銷售額 | 可使用完整的數值運算 |

本章把原始數值轉成「正負方向」或「名次」。這不是把資料變得更準，而是主動放棄一部分距離資訊，換取較少的母體分布假設。

## 學習目標

讀完本章，你應該能夠：

- 說明母數方法與無母數方法的差別，以及「distribution-free」不等於完全沒有假設。
- 依資料是名目、次序或數值，並依樣本是配對或獨立，選擇正確方法。
- 用符號檢定檢查母體中位數或兩種偏好是否相同。
- 用 Wilcoxon signed-rank 檢定分析配對數值資料，處理零差與同名次。
- 用 Mann-Whitney-Wilcoxon 檢定比較兩個獨立母體的分布。
- 用 Kruskal-Wallis 檢定比較三個以上獨立母體。
- 計算 Spearman 等級相關係數，分辨單調關係與線性關係。
- 把檢定統計量翻成群體重疊、名次混合、方向一致與訊號／雜訊的定性意義。

## 本章重點一覽

**母數方法(parametric methods)** 通常先對母體分布形狀作假設，再推論平均數或其他參數。**無母數方法** 不要求指定某個完整分布形狀，因此也稱為**分布自由方法(distribution-free methods)** 。但「分布自由」只表示不必指定常態等特定形狀，仍需要隨機性、觀察值獨立、配對方式正確，以及某些方法特有的對稱或同形狀條件。

本章有五個核心工具：

1. 符號檢定(sign test)：只看高於或低於基準，適合中位數或二選一偏好。
2. Wilcoxon signed-rank 檢定：看配對差的方向，也利用差值大小所形成的名次。
3. Mann-Whitney-Wilcoxon 檢定：把兩個獨立樣本混合排名，檢查兩群名次是否系統性分離。
4. Kruskal-Wallis 檢定：把前一方法擴充到三群以上。
5. Spearman 等級相關：比較同一批對象在兩個變數上的排序是否一致。

一句話先記住：**符號檢定看方向，signed-rank 看配對差的方向與大小名次，MWW 看兩個獨立群的混合名次，Kruskal-Wallis 看三群以上的名次分離，Spearman 看兩套名次是否同向。**

## 內容講解

### 投影片第 1–5 頁：為什麼要有無母數方法

投影片先列出五個方法，再用「淑女與下午茶」帶出檢定思維：一位女士聲稱先倒茶與先倒牛奶喝起來不同，R. A. Fisher 提議用隨機化實驗判斷她的辨識能力是否可能只是亂猜。重點不是故事本身，而是把模糊主張轉成可重複、可計數的結果。

投影片接著用擲筊比賽與連續聖筊新聞提醒我們：連續成功看起來很驚人，但要判斷是否罕見，必須先說明每次成功機率、試驗是否近似獨立，以及總共嘗試了多少次。只看到最後的連勝者，卻忽略大量未成功者，會有選擇性呈現問題。

無母數方法可分析名目、次序與數值資料。對數值資料而言，本章多半先轉成正負號或名次。轉換後對極端值較不敏感，也不需要完整指定常態分布；代價是原始距離資訊減少，在母數模型真的適合時，檢定力可能較低。

### 投影片第 6–15 頁：符號檢定

#### 18.1 母體中位數的符號檢定

要檢查母體中位數是否為 $m_0$，把每筆觀察和 $m_0$ 比較：

- $x_i>m_0$ 記為 `+`。
- $x_i<m_0$ 記為 `-`。
- $x_i=m_0$ 是平手(tie)，刪除後以較小的有效樣本數分析。

若 $m_0$ 真的是連續母體的中位數，高於與低於它的機率各為 $0.5$。令 $X$ 為有效資料中的正號數，便有：

<a id="formula-ch18-sign-binomial"></a>

$$
X\sim\operatorname{Binomial}(n,0.5)
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $X$ | 正號數 | 筆 |
| $n$ | 刪除平手後的有效樣本數 | 筆 |
| $0.5$ | $H_0$ 下出現正號的機率 | 無單位 |

雙尾檢定可寫成 $H_0:p=0.5$ 對 $H_a:p\ne0.5$；左尾或右尾問題則依研究方向改寫。精確 p 值由二項分配尾端機率得到。

**定性意義：** 符號檢定問的是資料落在基準兩側是否近似均衡。正負號接近一半一半，表示樣本在 $m_0$ 兩側的方向平衡；一側明顯較多，表示整個分布的中心位置可能偏向那一側。它完全不看距離，所以一筆高出 1 元與高出 1,000 元都只算一個正號。這讓極端值不會主宰結果，也代表它不能描述效果有多大。

#### Lawler 洋芋片例題：小樣本精確檢定

10 家店每週銷售額為 485、562、415、860、426、474、662、380、515、721 美元。相對於假設中位數 450 美元，共有 7 個正號、3 個負號。雙尾 p 值為：

$$
p\text{-value}=2P(X\ge7)=2(0.1172+0.0439+0.0098+0.0010)=0.3438
$$

在 $\alpha=0.10$ 下不能拒絕 $H_0$。正確結論是「目前沒有足夠證據認為母體中位數不是 450 美元」，不是證明中位數必然等於 450。

![Lawler 銷售額先轉成相對 450 的正負號，再用二項分布計算 7 個以上正號的雙尾機率](../figures/generated/ch18_sign_test_information.png)

你該注意什麼：左圖顯示符號化會丟掉距離資訊；右圖顯示雙尾 p 值必須同時計入另一側同樣極端的結果。

#### 大樣本常態近似與連續性修正

投影片以 $n>20$ 作為改用常態近似的實務門檻。當 $H_0:p=0.5$ 時：

<a id="formula-ch18-sign-normal"></a>

$$
\mu_X=0.5n,\qquad \sigma_X=\sqrt{0.25n}
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\mu_X$ | $H_0$ 下正號數的平均 | 筆 |
| $\sigma_X$ | 正號數重複抽樣的標準差 | 筆 |
| $n$ | 有效正負號總數 | 筆 |

因為正號數是離散整數、常態分布是連續曲線，尾端機率要做 $0.5$ 的**連續性修正(continuity correction)** 。例如 $P(X\le22)$ 用常態近似時改算 $P(Y\le22.5)$。

房價例題有 61 筆資料：22 筆高於 336,000 美元、38 筆低於、1 筆相等。刪除平手後 $n=60$，所以：

$$
\mu_X=30,\qquad \sigma_X=\sqrt{15}=3.873
$$

要檢查中位數是否下降，正號代表高於舊中位數，因此是左尾：

$$
z=\frac{22.5-30}{3.873}=-1.94,\qquad p=0.0262
$$

在 $\alpha=0.05$ 下拒絕 $H_0$，有證據顯示新屋價格的母體中位數低於 336,000 美元。本地 11e 課本同一例題使用 236,000 美元，投影片改為 336,000 美元；考試以投影片數值為準，方法完全相同。

**定性意義：** $\sigma_X$ 描述的是「若公平地一半正、一半負，正號數會自然晃動多少」，不是房價本身的離散程度。觀察到的正號數離 $n/2$ 越遠，相對於這個抽樣雜訊越不尋常。小 p 值只表示方向失衡難由 $p=0.5$ 解釋，不告訴我們房價實際下降多少。

#### 配對偏好的符號檢定

Sun Coast Farms 讓 14 人比較 Citrus Valley 與 Tropical Orange；2 人偏好 Citrus Valley、10 人偏好 Tropical Orange、2 人無偏好。刪除平手後 $n=12$，雙尾 p 值為：

$$
p=2P(X\le2)=2(0.0002+0.0029+0.0161)=0.0384
$$

在 $\alpha=0.05$ 下拒絕 $H_0$，偏好比例不是各半；而且負號較多，所以樣本方向支持 Tropical Orange 較受偏好。檢定單位仍是「人」，不是把每個人品嘗的兩杯飲料當成 28 個獨立觀察。

投影片第 15 頁在說明二項表時誤寫成 $n=10$ trials or stores，但同頁表格、前頁資料與計算全部使用 $n=12$；本講義依彼此一致的 $n=12$ 計算。

### 投影片第 16–20 頁：Wilcoxon signed-rank 檢定

符號檢定只看方向。若配對差是數值，而且差值分布可合理視為對稱，Wilcoxon signed-rank 檢定會再利用差值大小的名次，通常比符號檢定保留更多資訊。

步驟如下：

1. 先固定差值方向，例如 $d_i=A_i-B_i$。
2. 刪除 $d_i=0$ 的配對。
3. 依 $|d_i|$ 由小到大排名；相同絕對差使用平均名次。
4. 把原本正負號放回名次，分別加總成 $T^+$ 與 $T^-$。

<a id="formula-ch18-signed-rank"></a>

$$
T^+=\sum_{d_i>0}\operatorname{rank}(|d_i|),\qquad
T^-=\sum_{d_i<0}\operatorname{rank}(|d_i|)
$$

若 $H_0$ 成立，正負方向應近似隨機分配到各種大小的名次，$T^+$ 與 $T^-$ 應大致平衡。投影片以 $T^+$ 為統計量；$n\ge10$ 時使用：

<a id="formula-ch18-signed-rank-normal"></a>

$$
\mu_{T^+}=\frac{n(n+1)}{4},\qquad
\sigma_{T^+}=\sqrt{\frac{n(n+1)(2n+1)}{24}}
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $d_i$ | 第 $i$ 對依固定方向相減的差值 | 原始變數單位 |
| $T^+$ | 正差所對應名次的總和 | 名次點 |
| $T^-$ | 負差所對應名次的總和 | 名次點 |
| $n$ | 刪除零差後的配對數 | 對 |

適用條件是配對方式正確、各配對彼此獨立，而且差值分布近似對稱。它不要求差值常態，但「不常態」不等於「任意偏斜都可以」。若差值嚴重偏斜，符號檢定較安全。

製造方法例題刪除一個零差後 $n=10$，正名次和為 $T^+=49.5$。因此：

$$
\mu_{T^+}=27.5,\qquad \sigma_{T^+}=9.8107
$$

使用連續性修正後：

$$
z=\frac{49-27.5}{9.8107}=2.19,\qquad p=0.0286
$$

在 $\alpha=0.05$ 下拒絕相同中位位置的假設。因差定義為 A 減 B，且 $T^+$ 特別大，資料支持方法 A 完成時間較長。

**定性意義：** $T^+$ 很大，不只是「正差比較多」，還表示較大的絕對差也多半朝正方向。這是一種方向一致性乘上差距次序的訊號。它比較的是名次，不是平均差；拒絕 $H_0$ 也不能直接說平均數差多少。只有在兩個母體形狀相同、差異主要是位置平移時，才可把結果簡化成中位數位置差。

### 投影片第 21–27 頁：Mann-Whitney-Wilcoxon 檢定

**Mann-Whitney-Wilcoxon 檢定(MWW test)** 也稱 Wilcoxon rank-sum test，用於兩個獨立樣本。它不是先配對相減，而是把兩群資料合併後由小到大排名，再加總第一群名次。

<a id="formula-ch18-mww-w"></a>

$$
W=\sum_{i\in\text{樣本 1}}\operatorname{rank}(x_i)
$$

同值使用平均名次。小樣本要使用 $W$ 的精確分布；投影片規定 $n_1\ge7$ 且 $n_2\ge7$ 時可用常態近似：

<a id="formula-ch18-mww-normal"></a>

$$
\mu_W=\frac{n_1(n_1+n_2+1)}{2},\qquad
\sigma_W=\sqrt{\frac{n_1n_2(n_1+n_2+1)}{12}}
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $W$ | 第一個樣本的名次和 | 名次點 |
| $n_1,n_2$ | 兩個獨立樣本的大小 | 筆 |
| $\mu_W,\sigma_W$ | $H_0$ 下名次和的平均與標準差 | 名次點 |

Showtime 小樣本例題中，4 位大學生的名次和 $W=14$；在 4 人與 5 人所有可能分配的精確分布下，雙尾 $p=0.1904$，不能拒絕兩群分布相同。

銀行例題有 $n_1=12,n_2=10,W=169.5$：

$$
\mu_W=138,\qquad \sigma_W=15.1658
$$

用連續性修正 $W=169$ 後，$z=2.04$、雙尾 $p=0.0286$。拒絕兩分行帳戶餘額分布相同的假設；第一群名次和偏大，表示第一分行餘額傾向較高。

![Wilcoxon signed-rank、Mann-Whitney-Wilcoxon 與 Kruskal-Wallis 分別對應配對差、兩個獨立樣本及三個以上獨立樣本](../figures/generated/ch18_rank_test_structures.png)

你該注意什麼：三種方法都使用名次，但排名對象和資料依存結構不同；不能只因為題目出現「rank」就任選一個。

**定性意義：** $W$ 接近 $\mu_W$ 時，兩群高低名次交錯，分布重疊較多；$W$ 遠離 $\mu_W$ 時，第一群較常占據高名次或低名次，兩群排序較分離。一般虛無假設是兩個完整分布相同，不只平均數相同。只有兩群形狀相同、差異可視為整體平移時，才可把檢定說成中位數差異。

### 投影片第 28–30 頁：Kruskal-Wallis 檢定

Kruskal-Wallis 檢定把 MWW 擴充到 $k\ge3$ 個獨立樣本。先合併全部資料排名，再算每群名次和 $R_i$。

<a id="formula-ch18-kruskal-wallis"></a>

$$
H=\frac{12}{n_T(n_T+1)}\sum_{i=1}^{k}\frac{R_i^2}{n_i}-3(n_T+1),
\qquad n_T=\sum_{i=1}^{k}n_i
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $H$ | Kruskal-Wallis 統計量 | 無單位 |
| $R_i$ | 第 $i$ 群的名次和 | 名次點 |
| $n_i$ | 第 $i$ 群樣本數 | 筆 |
| $n_T$ | 全部樣本總數 | 筆 |
| $k$ | 群數 | 群 |

在 $H_0$ 下，各群應只是從同一分布抽出，名次會近似均勻混合。投影片要求每群 $n_i\ge5$，此時 $H$ 可用自由度 $k-1$ 的卡方分布近似。若有很多同名次，軟體通常會做 ties correction；手算題要依老師投影片指定公式。

Williams 公司例題的三群名次和為 95、27、88，得到：

$$
H=8.92,\qquad df=2,\qquad p=0.0116
$$

在 $\alpha=0.05$ 下拒絕三群分布相同。B 群名次和相對低，顯示 B 群評分傾向較低；但整體檢定本身不告訴我們每一對都不同，仍需後續成對比較才能定位。

**定性意義：** $H$ 大表示群組標籤能把高低名次分開，群間位置訊號相對名次混合雜訊較強；$H$ 小表示各群名次彼此交錯，分布較相似。它不是平均數差，也不能從顯著結果直接說哪一群造成差異或建立因果。

### 投影片第 31–34 頁：Spearman 等級相關

Pearson 相關衡量兩個數值變數的線性關係；**Spearman 等級相關係數(Spearman rank-correlation coefficient)** 衡量兩套排序的單調一致性。沒有同名次時，標準公式是：

<a id="formula-ch18-spearman"></a>

$$
r_s=1-\frac{6\sum_{i=1}^{n}d_i^2}{n(n^2-1)},\qquad d_i=x_i-y_i
$$

| 符號 | 意義 | 單位 |
|---|---|---|
| $r_s$ | 樣本 Spearman 等級相關 | 無單位 |
| $x_i,y_i$ | 第 $i$ 個對象在兩變數中的名次 | 名次 |
| $d_i$ | 兩套名次之差 | 名次 |
| $n$ | 被排名的共同對象數 | 個 |

$r_s$ 介於 $-1$ 與 $1$。接近 1 表示兩套排序大致同向；接近 $-1$ 表示一套越高、另一套越低；接近 0 表示沒有明顯單調排序關係。若有同名次，最穩妥的做法是先取平均名次，再對兩套名次計算 Pearson 相關。

投影片的銷售員表有 $\sum d_i^2=44,n=10$。依標準公式：

$$
r_s=1-\frac{6(44)}{10(10^2-1)}=0.733
$$

投影片第 33 頁把分母印成 $n(n^2+1)$ 並得到 0.739；本地 11e 課本的定義與統計標準都是 $n(n^2-1)$，因此本講義使用 0.733。這是來源公式的誤植，不改變它要表達的正向關聯。

當 $n\ge10$，投影片用下列常態近似檢定 $H_0:\rho_s=0$：

<a id="formula-ch18-spearman-test"></a>

$$
\mu_{r_s}=0,\qquad \sigma_{r_s}=\sqrt{\frac{1}{n-1}},\qquad
z=\frac{r_s}{\sigma_{r_s}}=r_s\sqrt{n-1}
$$

以修正後的 $r_s=0.733$ 計算，$z=2.20$、雙尾 $p\approx0.028$，在 $\alpha=0.05$ 下有顯著正向等級相關。這不表示面試潛力造成銷售表現，也不表示每個人都排序一致。

![同一組模擬資料在原始尺度呈現彎曲但單調的關係，換成名次後接近對角線，Spearman 相關高於線性相關](../figures/generated/ch18_spearman_monotonic.png)

你該注意什麼：Spearman 關心「往上走時另一個變數是否大致也往上」，不要求原始點雲貼近直線；但 U 形等非單調關係仍可能得到接近 0。

**定性意義：** $|r_s|$ 越大，兩套排序越一致，名次差的平方和越小；接近 0 只代表缺乏單調排序，不代表兩變數完全沒有任何關係。相關也不等於因果，高相關不能排除共同原因、選樣偏誤或反向因果。

### 投影片第 35 頁：全章總結

- 無母數方法可處理類別、次序與數值資料；數值資料通常先轉成正負號或名次。
- 符號檢定可檢查母體中位數，也可分析只有偏好方向的配對樣本。
- Wilcoxon signed-rank 使用配對數值差的方向與名次；對稱母體的中位數問題也可使用。
- MWW 比較兩個獨立樣本的混合名次；Kruskal-Wallis 再擴充到三群以上。
- Spearman 相關用兩套名次衡量單調關聯。

這五種工具的共同優點是少依賴特定分布形狀，代價是把部分數值距離壓縮成類別或名次。選方法時，資料是否配對、群數與測量尺度仍比「無母數」三個字更重要。

### 全章解題流程

1. 先判斷資料尺度：只有類別、只有順序，還是保留數值距離。
2. 再判斷資料結構：一個樣本對中位數、配對樣本、兩個獨立樣本、三個以上獨立樣本，或同一批對象的兩套排名。
3. 寫清楚差值或正號方向，刪除規則一致。
4. 處理平手：符號檢定刪除等於基準者；排名方法對同值給平均名次。
5. 依樣本大小選精確分布或常態／卡方近似，近似常態時留意連續性修正。
6. 用 p 值與 $\alpha$ 判斷，再把結論寫回中位數、分布或排序關聯。
7. 不把「分布不同」擅自縮成「平均數不同」，也不把顯著關聯寫成因果。

### 把數字翻成真實意義

| 數字或關係 | 數理變化 | 資料世界中的意思 | 不能直接推論 |
|---|---|---|---|
| 正負號比例 | 越偏離 1:1 越不相容於 $p=0.5$ | 多數觀察落在基準同一側，中心位置或偏好方向失衡 | 效果差多少、平均數差多少 |
| $T^+$ | 遠離中心表示大名次偏向同一符號 | 配對差的方向與相對大小更一致 | 差值平均或所有個體都同方向 |
| MWW 的 $W$ | 遠離 $\mu_W$ 表示第一群占據較多高或低名次 | 兩群排序較分離、重疊較少 | 只差中位數，除非形狀相同 |
| Kruskal-Wallis 的 $H$ | 越大代表群間名次和越不均 | 至少有一群的高低位置傾向不同 | 哪一對不同、因果或平均差 |
| $r_s$ | 越接近 $\pm1$，名次差平方和越小 | 兩套排序更同向或反向 | 線性、因果或沒有離群影響 |
| 轉成名次 | 極端距離被壓成相鄰名次差 | 對離群與尺度較穩健，但丟掉實際距離 | 無母數一定更準或完全無假設 |

## 跟前面像的東西怎麼分

<a id="compare-ch18-method-selection"></a>

### 比較 1：符號檢定 vs Wilcoxon signed-rank vs 配對 t

| 方法 | 資料長相 | 核心條件 | 真正比較的東西 |
|---|---|---|---|
| 符號檢定 | 配對方向或單一樣本相對中位數，只需正負 | 各單位獨立；不要求差值對稱 | 正負方向是否各半 |
| Wilcoxon signed-rank | 配對數值，可排 $|d_i|$ 名次 | 差值分布近似對稱 | 配對差的位置是否為 0 |
| 配對 t | 配對數值，保留原始差距 | 差值近似常態或樣本夠大 | 母體平均差是否為 0 |

**一句話判斷準則：** 只有偏好方向或差值很偏斜，用符號；有配對數值且差值對稱，用 signed-rank；要推論平均差且 t 條件合理，用配對 t。

**容易誤選情境：** 同一批人前後各測一次，卻使用兩獨立樣本方法；這會丟掉每個人的前後對應。

### 比較 2：MWW vs 兩獨立樣本 t

| 方法 | 何時用 | 結論語言 |
|---|---|---|
| MWW | 兩個獨立樣本，資料至少可排序，不想指定常態形狀 | 一般說兩分布是否相同；同形狀時才說中位數位置差 |
| 兩獨立樣本 t | 兩個獨立數值樣本，要比較母體平均數 | 平均數差與其方向、區間 |

**一句話判斷準則：** 要比較平均數用 t；只可靠排序或分布明顯不適合平均數模型時，用 MWW。

**容易誤選情境：** MWW 顯著後直接寫「兩群平均數不同」。名次檢定未直接檢定平均數，這個結論超出方法。

### 比較 3：Kruskal-Wallis vs 單因子 ANOVA

| 方法 | 資料與條件 | 檢定目標 |
|---|---|---|
| Kruskal-Wallis | 三個以上獨立樣本；次序或數值資料；以名次分析 | 各群完整分布是否相同 |
| 單因子 ANOVA | 三個以上獨立數值樣本；誤差近似常態、等變異 | 各母體平均數是否相同 |

**一句話判斷準則：** 問平均數且 ANOVA 條件合理，用 [第 13 章 ANOVA](13-anova.md#formula-anova-f)；問排序位置或只有次序資料，用 Kruskal-Wallis。

**容易誤選情境：** 三群滿意度只有「差、可、好、很好」，卻把 1–4 當等距分數做 ANOVA；這時名次方法更符合尺度。

### 比較 4：Kruskal-Wallis 的卡方近似 vs 第 12 章卡方檢定

兩者都查卡方右尾，但資料來源不同。Kruskal-Wallis 先把數值或次序資料排名，$H$ 再近似卡方；[第 12 章卡方檢定](12-chi-square-tests.md#formula-ch12-chi-square-cell)直接比較類別次數的觀察值與期望值。

**一句話判斷準則：** 表格裡是類別人數，用第 12 章；原始資料能排序、要比較三群位置，用本章 Kruskal-Wallis。

### 比較 5：Spearman vs Pearson 相關

| 方法 | 抓到的關係 | 尺度 |
|---|---|---|
| Spearman | 單調關係，可彎曲 | 至少次序尺度 |
| Pearson | 線性關係 | 數值尺度，且需留意離群值 |

**一句話判斷準則：** 題目給名次或只要求單調排序一致，選 Spearman；保留原始數值並關心直線關係，選 Pearson。

**容易誤選情境：** 點雲呈清楚 U 形，就因為「有關係」而期待 Spearman 很大；U 形不是單調，正負方向會互相抵銷。

## 考古題與詳解

本題庫共有 53 題選擇題與 28 題 Problem。題目原文依 PDF 保留；共用 Exhibit 只出現一次。所有數值另由 `ch18_exam_verification.py` 重算。題庫部分常態近似題沿用原題選項的未修正數值，詳解同時指出依投影片加入連續性修正後的結果；兩者若決策相同，不隱藏差異。

### 選擇題｜第 1–24 題：基本觀念與方法辨認

#### 選擇題 1

##### 題目

> A collection of statistical methods that generally requires very few, if any, assumptions about the population distribution is known as
>
> a. parametric methods<br>
> b. nonparametric methods<br>
> c. distribution-fixed methods<br>
> d. normal

##### 詳解

- **辨認題型：** 無母數方法定義。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，關鍵字是對母體分布形式要求很少。
- **檢查假設：** 這是名詞題；「很少」不等於完全沒有隨機與獨立條件。
- **代入計算／推理：** distribution-free 是 nonparametric 的別稱。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 反而通常指定分布族；b 正確；c 不是本章術語；d 是一種分布，不是一組方法。

#### 選擇題 2

##### 題目

> The collection of statistical methods that require assumptions about the population is known as
>
> a. distribution free methods<br>
> b. nonparametric methods<br>
> c. small populations<br>
> d. parametric methods

##### 詳解

- **辨認題型：** 母數方法定義。
- **選方法：** 回到[母數與無母數的分辨](#compare-ch18-method-selection)。
- **檢查假設：** 題目問方法類別，不是母體大小。
- **代入計算／推理：** 以特定母體分布與參數為基礎的是 parametric methods。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 都是較少指定分布形式的方法；c 不是方法名稱；d 正確。

#### 選擇題 3

##### 題目

> Parametric methods are statistical methods that
>
> a. require some assumptions about the population<br>
> b. require no assumptions about the population<br>
> c. only deal with small samples<br>
> d. considers the sign of two matched samples

##### 詳解

- **辨認題型：** 母數方法特徵。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)先看是否指定母體模型。
- **檢查假設：** 樣本大小不是母數／無母數的定義。
- **代入計算／推理：** 母數方法會對母體分布或參數結構作假設。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 把無母數也誇大成零假設；c 錯在只限小樣本；d 描述符號檢定。

#### 選擇題 4

##### 題目

> Which of the following tests would not be an example of a nonparametric method?
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. t-test

##### 詳解

- **辨認題型：** 方法分類。
- **選方法：** 依[跨方法比較](#compare-ch18-method-selection)，找出以平均數與 t 分布為核心的方法。
- **檢查假設：** `not` 表示要選不是無母數者。
- **代入計算／推理：** t-test 是母數方法；其餘三個都以符號或名次分析。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都是本章方法；d 正確，因 t 檢定直接推論平均數。

#### 選擇題 5

##### 題目

> A sign test is a
>
> a. parametric method for determining the differences between two populations based on two matched samples<br>
> b. nonparametric method for determining the differences between two populations based on two matched samples<br>
> c. nonparametric method for determining the differences between two or more populations based on two or more matched samples<br>
> d. parametric method for determining the differences between two or more populations based on two or more matched samples

##### 詳解

- **辨認題型：** 符號檢定用途。
- **選方法：** 使用[符號檢定的二項模型](#formula-ch18-sign-binomial)，配對結果只保留正負方向。
- **檢查假設：** 這個版本比較兩個配對條件，不是三群以上。
- **代入計算／推理：** 符號檢定是 nonparametric，且可處理兩個 matched samples。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、d 錯在 parametric；b 正確；c 把兩條件擴成兩個以上母體，應另選其他方法。

#### 選擇題 6

##### 題目

> The level of measurement that allows for the rank ordering of data items is
>
> a. nominal measurement<br>
> b. ratio measurement<br>
> c. interval measurement<br>
> d. ordinal measurement

##### 詳解

- **辨認題型：** 測量尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，題幹只保證可以排序。
- **檢查假設：** 沒有說相鄰差距或倍數有意義。
- **代入計算／推理：** 可排序但距離未必等距是 ordinal。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 只有標籤；b、c 都比題幹提供更多數值資訊；d 正確。

#### 選擇題 7

##### 題目

> The level of measurement that is simply a label for the purpose of identifying an item is
>
> a. ordinal measurement<br>
> b. ratio measurement<br>
> c. nominal measurement<br>
> d. internal measurement

##### 詳解

- **辨認題型：** 名目尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，只有辨識標籤、沒有順序。
- **檢查假設：** `internal` 不是標準測量尺度；原題如此拼寫，忠實保留。
- **代入計算／推理：** nominal scale 的功能就是分類與命名。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 還有次序；b 還能談倍數；c 正確；d 不是四種尺度之一。

#### 選擇題 8

##### 題目

> The labeling of parts as "defective" or "non-defective" is an example of
>
> a. ordinal data<br>
> b. ratio data<br>
> c. interval data<br>
> d. nominal data

##### 詳解

- **辨認題型：** 二元類別的尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，兩標籤只區分類別。
- **檢查假設：** defective 與 non-defective 沒有可運算的距離。
- **代入計算／推理：** 這是 nominal data。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 需要有序等級；b、c 需要數值差距；d 正確。

#### 選擇題 9

##### 題目

> In a questionnaire, respondents are asked to mark their marital status. Marital status is an example of the
>
> a. ordinal scale<br>
> b. nominal scale<br>
> c. ratio scale<br>
> d. interval scale

##### 詳解

- **辨認題型：** 類別尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，婚姻狀態只有互斥名稱。
- **檢查假設：** 類別沒有自然的高低順序。
- **代入計算／推理：** 因此是 nominal scale。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 會錯加順序；b 正確；c、d 需要有意義的數值差距。

#### 選擇題 10

##### 題目

> The scale of measurement that is used to rank order the observation for a variable is called the
>
> a. ratio scale<br>
> b. ordinal scale<br>
> c. nominal scale<br>
> d. interval scale

##### 詳解

- **辨認題型：** 排名尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，題幹直接說 rank order。
- **檢查假設：** 沒有保證名次 1 與 2 的差等於 2 與 3 的差。
- **代入計算／推理：** 排序所需的最低尺度是 ordinal。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、d 提供更強的距離資訊；b 正確；c 不能排序。

#### 選擇題 11

##### 題目

> On a teacher evaluation form students are asked to rate their professor's performance as excellent, very good, good, and poor. This is an example of the
>
> a. ordinal scale<br>
> b. ratio scale<br>
> c. nominal scale<br>
> d. interval scale

##### 詳解

- **辨認題型：** 有序評等。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，四個評語有自然順序。
- **檢查假設：** excellent 到 very good 的距離未必等於 good 到 poor。
- **代入計算／推理：** 有序但不保證等距，屬 ordinal。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 要求數值距離；c 忽略既有順序。

#### 選擇題 12

##### 題目

> Temperature is an example of a variable that uses
>
> a. the ratio scale<br>
> b. the interval scale<br>
> c. the ordinal scale<br>
> d. either the ratio or the ordinal scale

##### 詳解

- **辨認題型：** 溫度的測量尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，一般教材中的攝氏或華氏溫度看差值。
- **檢查假設：** 0°C 不代表完全沒有溫度，故不能把 20°C 說成 10°C 的兩倍熱。
- **代入計算／推理：** 差值有意義、零點任意，是 interval scale。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 適合絕對零點尺度；b 正確；c 只保留順序；d 混入不適用的尺度。

#### 選擇題 13

##### 題目

> The speed of an automobile is an example of a variable that uses the
>
> a. ratio scale<br>
> b. interval scale<br>
> c. nominal scale<br>
> d. ordinal scale

##### 詳解

- **辨認題型：** 速度的測量尺度。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，速度有真正的零點。
- **檢查假設：** 0 km/h 表示沒有移動，倍數比較有意義。
- **代入計算／推理：** 因此屬 ratio scale。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 零點可任意；c 只有標籤；d 只有順序。

#### 選擇題 14

##### 題目

> Statistical methods that generally require very few, if any, assumptions about the population distribution are known as
>
> a. parametric<br>
> b. nonparametric<br>
> c. free methods<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 無母數方法定義的重複確認。
- **選方法：** 回到[方法選擇流程](#compare-ch18-method-selection)。
- **檢查假設：** 題目指的是不指定特定母體分布形式。
- **代入計算／推理：** 正式名稱是 nonparametric methods。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 通常有較明確分布假設；b 正確；c 不是完整術語；d 因 b 已正確而錯。

#### 選擇題 15

##### 題目

> Which of the following tests would not be an example of nonparametric method?
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. t test

##### 詳解

- **辨認題型：** 方法分類的重複題。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)找出直接檢定平均數者。
- **檢查假設：** 題幹有 `not`。
- **代入計算／推理：** t test 是母數方法。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都使用符號或名次；d 正確。

#### 選擇題 16

##### 題目

> A nonparametric version of the Parametric analysis of variance test is the
>
> a. Kruskal-Wallis Test<br>
> b. Mann-Whitney-Wilcoxon Test<br>
> c. sign test<br>
> d. Wilcoxon Signed-rank test

##### 詳解

- **辨認題型：** 三群以上方法對照。
- **選方法：** 依[Kruskal-Wallis 公式](#formula-ch18-kruskal-wallis)，它比較 $k$ 個獨立樣本的名次。
- **檢查假設：** ANOVA 的典型問題是三群以上；不是兩群或配對。
- **代入計算／推理：** Kruskal-Wallis 是 one-way ANOVA 的無母數對照。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 只比兩個獨立群；c 只看正負；d 是兩個配對條件。

#### 選擇題 17

##### 題目

> A nonparametric method for determining the differences between two populations based on two matched samples where only preference data is required is the
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. Kruskal-Wallis Test

##### 詳解

- **辨認題型：** 配對偏好資料的方法選擇。
- **選方法：** 依[符號檢定](#formula-ch18-sign-binomial)，只有偏好方向時轉成正負號。
- **檢查假設：** 沒有數值差距可供 signed-rank 排 $|d_i|$。
- **代入計算／推理：** matched samples 加 preference data 指向 sign test。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 是獨立樣本；b 需要配對數值；c 正確；d 是三群以上獨立樣本。

#### 選擇題 18

##### 題目

> When ranking combined data in a Wilcoxon signed rank test, the data that receives a rank of 1 is the
>
> a. lowest value<br>
> b. highest value<br>
> c. middle value<br>
> d. average of the highest and the lowest of values

##### 詳解

- **辨認題型：** 名次配置規則。
- **選方法：** 依[Wilcoxon signed-rank 步驟](#formula-ch18-signed-rank)，實際上是對非零 $|d_i|$ 由小到大排名。
- **檢查假設：** 若最低值同名次，應分配平均名次；題目未給 ties。
- **代入計算／推理：** 最小絕對差得到 rank 1。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 應得最大名次；c 沒有固定名次；d 不是排名規則。

#### 選擇題 19

##### 題目

> Statistical methods that require assumptions about the population are known as
>
> a. distribution free<br>
> b. nonparametric<br>
> c. either distribution free of nonparametric<br>
> d. parametric

##### 詳解

- **辨認題型：** 母數方法定義。
- **選方法：** 回到[方法選擇流程](#compare-ch18-method-selection)。
- **檢查假設：** 原題 c 的 `of` 疑為 `or`，不影響選項意義。
- **代入計算／推理：** 要求母體假設的是 parametric methods。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都指無母數；d 正確。

#### 選擇題 20

##### 題目

> The Spearman rank-correlation coefficient is
>
> a. a correlation measure based on the average of data items<br>
> b. a correlation measure based on rank-ordered data for two variables<br>
> c. a correlation measure based on the median of data items<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** Spearman 定義。
- **選方法：** 使用[Spearman 公式](#formula-ch18-spearman)。
- **檢查假設：** 兩套名次必須來自同一批對象。
- **代入計算／推理：** $r_s$ 以兩變數的 rank-ordered data 衡量單調關聯。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、c 都不是公式依據；b 正確；d 因 b 已正確而錯。

#### 選擇題 21

##### 題目

> A nonparametric test for the equivalence of two populations would be used instead of a parametric test for the equivalence of the population parameters if
>
> a. the samples are very large<br>
> b. the samples are not independent<br>
> c. no information about the populations is available<br>
> d. The parametric test is always used in this situation.

##### 詳解

- **辨認題型：** 何時選無母數方法。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，若無法合理指定母體分布，就考慮無母數方法。
- **檢查假設：** 無母數方法仍不能修復不獨立；b 不是使用理由。
- **代入計算／推理：** 缺乏母體分布資訊時，依名次或符號的方法較合適。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 大樣本本身不迫使改方法；b 違反兩類方法共同的重要條件；c 正確；d 過度絕對。

#### 選擇題 22

##### 題目

> A nonparametric test would be used if
>
> a. nominal data is available<br>
> b. interval data is available<br>
> c. it is known that the population is normally distributed<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 資料尺度與方法。
- **選方法：** 依[方法選擇流程](#compare-ch18-method-selection)，名目資料無法直接使用平均數型母數方法。
- **檢查假設：** 區間資料也能用無母數，但「有區間資料」本身不是必要理由；已知常態通常支持母數法。
- **代入計算／推理：** nominal data 常需要符號或類別方法。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 資訊較完整，仍需看目標與條件；c 反而支持母數法；d 因 a 正確而錯。

#### 選擇題 23

##### 題目

> If a null hypothesis that states that two populations are identical is rejected using a nonparametric test, then it is safe to assume that
>
> a. neither the means nor the variances are equal<br>
> b. the means of the populations are not the same<br>
> c. the variances of the populations are not the same<br>
> d. We cannot be sure of the way in which the populations differ from each other.

##### 詳解

- **辨認題型：** 分布檢定的結論界線。
- **選方法：** 依[MWW 的一般假設](#formula-ch18-mww-w)，拒絕的是兩個完整分布相同。
- **檢查假設：** 若未另假設兩群形狀相同，不能只歸因於平均、中位數或變異數。
- **代入計算／推理：** 顯著只說至少某種分布特徵不同。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 太強；b、c 都擅自指定差異來源；d 正確。

#### 選擇題 24

##### 題目

> The Spearman rank-correlation coefficient for 20 pairs of data when $\Sigma d_i^2=50$ is.
>
> a. 0.0063<br>
> b. 0.0376<br>
> c. 0.9624<br>
> d. 0.9937

##### 詳解

- **辨認題型：** Spearman 係數計算。
- **選方法：** 使用[標準 Spearman 公式](#formula-ch18-spearman)。
- **檢查假設：** 題目未提 ties，故可直接用 $d_i$ 公式。
- **代入計算／推理：** $r_s=1-6(50)/[20(20^2-1)]=1-300/7980=0.9624$。
- **解讀結論：** 答案是 **c** ；兩套排序高度同向。
- **選項檢討：** a、b 是把扣除量或分母處理錯；c 正確；d 對應過小的名次差。

### 選擇題｜第 25–53 題：共用 Exhibit 與計算

#### 題組 18-1：選擇題 25–28 共用資料

> Exhibit 18-1
>
> Fifteen people were given two types of cereal, Brand X and Brand Y. Two people preferred Brand X and thirteen people preferred Brand Y. We want to determine whether or not customers prefer one brand over the other.

#### 選擇題 25

##### 題目

> Refer to Exhibit 18-1. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

- **辨認題型：** 兩品牌偏好的符號檢定。
- **選方法：** 使用[符號檢定二項模型](#formula-ch18-sign-binomial)。
- **檢查假設：** 每人只表達一個偏好，且受試者彼此獨立。
- **代入計算／推理：** 無偏好差異表示偏好任一品牌的機率 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 把機率誤寫成平均數；c 把機率寫成不可能的 5；d 正確。

#### 選擇題 26

##### 題目

> Refer to Exhibit 18-1. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. Poisson<br>
> d. binomial

##### 詳解

- **辨認題型：** 小樣本符號檢定參考分布。
- **選方法：** 使用[精確二項分布](#formula-ch18-sign-binomial)。
- **檢查假設：** $n=15\le20$，投影片規則用 exact binomial。
- **代入計算／推理：** 每人偏好 X／Y 是兩結果、$p=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 是大樣本近似；b、c 不符合兩結果計數；d 正確。

#### 選擇題 27

##### 題目

> Refer to Exhibit 18-1. The p-value for this test is
>
> a. 0.0005<br>
> b. 0.001<br>
> c. 0.0037<br>
> d. 0.0074

##### 詳解

- **辨認題型：** 雙尾精確符號檢定。
- **選方法：** 依[精確二項模型](#formula-ch18-sign-binomial)，從較小的 2 人那一尾計算再乘 2。
- **檢查假設：** 有效樣本 $n=15$，觀察到 $X=2$。
- **代入計算／推理：** $p=2P(X\le2)=2(1+15+105)/2^{15}=0.007385\approx0.0074$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 漏加部分尾端或漏乘 2；c 是單尾值；d 正確。

#### 選擇題 28

##### 題目

> Refer to Exhibit 18-1. At 95% confidence, the null hypothesis should
>
> a. be rejected<br>
> b. not be rejected<br>
> c. be revised<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 以 p 值作決策。
- **選方法：** 沿用[符號檢定](#formula-ch18-sign-binomial)。
- **檢查假設：** 95% confidence 對應 $\alpha=0.05$。
- **代入計算／推理：** $p=0.0074<0.05$。
- **解讀結論：** 答案是 **a** ；兩品牌偏好並非各半，樣本方向偏向 Brand Y。
- **選項檢討：** a 正確；b 與 p 值比較相反；c 不是標準決策；d 因 a 正確而錯。

#### 題組 18-2：選擇題 29–34 共用資料

> Exhibit 18-2
>
> Students in statistics classes were asked whether they preferred a 10-minute break or to get out of class 10 minutes early. In a sample of 150 students, 40 preferred a 10-minute break, 80 preferred to get out of class 10 minutes early, and 30 had no preference. We want to determine if there is a difference in students' preferences.

原題第 29–34 題誤寫為 `Exhibit 19-2`；實際上都指這份 Exhibit 18-2。刪除 30 位無偏好者後，有效樣本 $n=120$。

#### 選擇題 29

##### 題目

> Refer to Exhibit 19-2. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

- **辨認題型：** 兩種偏好的符號檢定。
- **選方法：** 使用[符號檢定](#formula-ch18-sign-binomial)。
- **檢查假設：** 無偏好者不給正負號，已刪除。
- **代入計算／推理：** 無差異時，偏好提早下課的機率 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 的 $\mu$ 不是二項機率；c 超出機率範圍；d 正確。

#### 選擇題 30

##### 題目

> Refer to Exhibit 19-2. The mean and the standard deviation of the sampling distribution of the number of students who preferred to get out early are
>
> a. 50 and 30<br>
> b. 60 and 30<br>
> c. 50 and 5.478<br>
> d. 60 and 5.478

##### 詳解

- **辨認題型：** 符號數的常態近似參數。
- **選方法：** 使用[符號檢定常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 有效 $n=120$，不是原始 150。
- **代入計算／推理：** $\mu=0.5(120)=60$，$\sigma=\sqrt{0.25(120)}=\sqrt{30}=5.478$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、c 錯把有效人數算成 100；b 把變異數 30 當標準差；d 正確。

#### 選擇題 31

##### 題目

> Refer to Exhibit 19-2. To test the null hypothesis, the appropriate probability distribution to use is the
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

- **辨認題型：** 大樣本符號檢定的課堂計算法。
- **選方法：** 依[常態近似](#formula-ch18-sign-normal)，$n=120>20$。
- **檢查假設：** 精確分布本質仍是 binomial，但投影片的大樣本計算選 normal approximation。
- **代入計算／推理：** $np=n(1-p)=60$，近似充足。
- **解讀結論：** 依題庫預期答案是 **a** 。
- **選項檢討：** a 正確；b、c 不處理二項正號數；d 是精確模型，但本題問大樣本採用的計算分布。

#### 選擇題 32

##### 題目

> Refer to Exhibit 19-2. The test statistic based on the number of students who preferred to get out early equals
>
> a. 1.825<br>
> b. 0.67<br>
> c. 0.82<br>
> d. 3.65

##### 詳解

- **辨認題型：** 正號數的標準化。
- **選方法：** 使用[常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 原題選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(80-60)/5.478=3.65$。若依投影片加修正，$z=(79.5-60)/5.478=3.56$，決策不變。
- **解讀結論：** 對應選項答案是 **d** 。
- **選項檢討：** a 是少除約一半；b、c 是錯誤分母；d 正確對應題庫算法。

#### 選擇題 33

##### 題目

> Refer to Exhibit 19-2. The p-value for testing the hypotheses is
>
> a. less than 0.002<br>
> b. between 0.002 and 0.05<br>
> c. between 0.05 and 0.10<br>
> d. greater than 0.10

##### 詳解

- **辨認題型：** 雙尾 p 值區間。
- **選方法：** 由[常態近似](#formula-ch18-sign-normal)取 $2P(Z\ge|z|)$。
- **檢查假設：** 不論用 $z=3.65$ 或連續性修正的 3.56，都是雙尾。
- **代入計算／推理：** 未修正 $p\approx0.00026$；修正後約 $0.00037$，都小於 0.002。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、c、d 都把極端的 $z$ 誤配成過大的 p 值。

#### 選擇題 34

##### 題目

> Refer to Exhibit 19-2. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** p 值決策。
- **選方法：** 沿用[符號檢定常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 題目未另給 $\alpha$，依常見 0.05；前題 p 值遠小於 0.002。
- **代入計算／推理：** $p<0.05$，拒絕 $H_0$。
- **解讀結論：** 答案是 **a** ；偏好提早下課的人顯著較多。
- **選項檢討：** a 正確；b 與 p 值矛盾；c 不是檢定決策；d 因 a 正確而錯。

#### 題組 18-3：選擇題 35–39 共用資料

> Exhibit 18-3
>
> It is believed that the median yearly income in a suburb of Atlanta is \$70,000. A sample of 67 residents was taken. Thirty-eight had yearly incomes above \$70,000, 26 had yearly incomes below \$70,000, and 3 had yearly incomes equal to \$70,000. The null hypothesis to be tested is $H_0$: median = \$70,000.

刪除 3 位剛好等於 70,000 美元者後，有效樣本 $n=64$。

#### 選擇題 35

##### 題目

> Refer to Exhibit 18-3. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

- **辨認題型：** 大樣本中位數符號檢定。
- **選方法：** 使用[符號檢定常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 有效 $n=64>20$。
- **代入計算／推理：** 正號數的二項分布以常態分布近似。
- **解讀結論：** 題庫預期答案是 **a** 。
- **選項檢討：** a 正確；b、c 不符合正負計數；d 是精確母分布，但題庫依大樣本規則選 normal。

#### 選擇題 36

##### 題目

> Refer to Exhibit 18-3. The mean and the standard deviation (respectively) for this test about the median are
>
> a. 32 and 4<br>
> b. 32 and 16<br>
> c. 33.5 and 4<br>
> d. 33.5 and 16

##### 詳解

- **辨認題型：** 常態近似參數。
- **選方法：** 使用[常態近似公式](#formula-ch18-sign-normal)。
- **檢查假設：** 平手已刪除，$n=64$。
- **代入計算／推理：** $\mu=32$，$\sigma=\sqrt{16}=4$。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 把變異數 16 當標準差；c、d 未刪除平手。

#### 選擇題 37

##### 題目

> Refer to Exhibit 18-3. The test statistic has a value of
>
> a. 1.00<br>
> b. 1.50<br>
> c. 2.00<br>
> d. 2.50

##### 詳解

- **辨認題型：** 正號數標準化。
- **選方法：** 使用[常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(38-32)/4=1.50$；修正後為 $(37.5-32)/4=1.375$。
- **解讀結論：** 對應選項答案是 **b** 。
- **選項檢討：** a、c、d 是錯誤中心或尺度；b 符合題庫算法。

#### 選擇題 38

##### 題目

> Refer to Exhibit 18-3. The p-value for this test is
>
> a. 0.4332<br>
> b. 0.8664<br>
> c. 0.0668<br>
> d. 0.1336

##### 詳解

- **辨認題型：** 雙尾 p 值。
- **選方法：** 由[常態近似](#formula-ch18-sign-normal)計算 $2P(Z\ge1.50)$。
- **檢查假設：** 題庫沿用未修正 $z$；若修正，p 值約 0.1691。
- **代入計算／推理：** $2(0.0668)=0.1336$。
- **解讀結論：** 對應答案是 **d** 。
- **選項檢討：** a、b 使用錯誤中央面積；c 是單尾；d 是題庫的雙尾值。

#### 選擇題 39

##### 題目

> Refer to Exhibit 18-3. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 中位數檢定決策。
- **選方法：** 沿用[符號檢定](#formula-ch18-sign-binomial)。
- **檢查假設：** 以常見 $\alpha=0.05$ 判斷；修正與未修正 p 值都大於 0.05。
- **代入計算／推理：** $0.1336>0.05$。
- **解讀結論：** 答案是 **b** ；沒有足夠證據認為中位數不是 70,000 美元。
- **選項檢討：** a 過度拒絕；b 正確；c 不是標準決策；d 因 b 正確而錯。

#### 題組 18-4：選擇題 40–43 共用資料

> Exhibit 18-4
>
> A company advertises that food preparation time can be significantly reduced with the Handy Dandy Slicer. A sample of 12 individuals prepared the ingredients for a meal with and without the slicer. You are given the preparation times below.

| Person | With Slicer | Without Slicer |
|---:|---:|---:|
| 1 | 20 | 22 |
| 2 | 12 | 18 |
| 3 | 20 | 18 |
| 4 | 14 | 22 |
| 5 | 19 | 19 |
| 6 | 20 | 21 |
| 7 | 19 | 18 |
| 8 | 15 | 12 |
| 9 | 22 | 18 |
| 10 | 19 | 25 |
| 11 | 21 | 26 |
| 12 | 23 | 20 |

#### 選擇題 40

##### 題目

> Refer to Exhibit 18-4. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. Normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. Binomial

##### 詳解

- **辨認題型：** 配對數值的 Wilcoxon signed-rank 檢定。
- **選方法：** 使用[signed-rank 常態近似](#formula-ch18-signed-rank-normal)。
- **檢查假設：** 刪除 Person 5 的零差後 $n=11\ge10$，且差值需近似對稱。
- **代入計算／推理：** 投影片以 $T^+$ 的 normal approximation 作參考分布。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 不處理配對名次；c 是配對 t 的參考分布；d 是只看正負的符號檢定。

#### 選擇題 41

##### 題目

> Refer to Exhibit 18-4. The test statistic equals
>
> a. -0.81 or 0.81<br>
> b. -0.89 or 0.89<br>
> c. -10 or 10<br>
> d. -20 or 20

##### 詳解

- **辨認題型：** signed-rank 的常態標準化。
- **選方法：** 依[signed-rank 公式](#formula-ch18-signed-rank-normal)計算 $T^+$。
- **檢查假設：** 以 `With - Without` 為差，零差刪除；同絕對差用平均名次。
- **代入計算／推理：** $T^+=23$，$\mu=33$，$\sigma=\sqrt{126.5}=11.247$，未修正 $z=(23-33)/11.247=-0.89$。
- **解讀結論：** 答案是 **b** ；正負號依差值方向而定，絕對值相同。
- **選項檢討：** a 來自錯誤名次和或尺度；b 正確；c、d 把未標準化差距當 z。

#### 選擇題 42

##### 題目

> Refer to Exhibit 18-4. The p-value for this test is
>
> a. 0.3133<br>
> b. 0.6266<br>
> c. 0.3734<br>
> d. 0.8167

##### 詳解

- **辨認題型：** 雙尾 signed-rank p 值。
- **選方法：** 由[signed-rank 常態近似](#formula-ch18-signed-rank-normal)取 $2P(Z\le-0.89)$。
- **檢查假設：** 題庫使用未修正 z。
- **代入計算／推理：** $p\approx2(0.1867)=0.3734$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a、b、d 是單尾、倍數或中央面積的誤讀；c 正確。

#### 選擇題 43

##### 題目

> Refer to Exhibit 18-4. The null hypothesis should
>
> a. be rejected<br>
> b. not be rejected<br>
> c. be revised<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 配對檢定決策。
- **選方法：** 沿用[Wilcoxon signed-rank](#formula-ch18-signed-rank)。
- **檢查假設：** 以 $\alpha=0.05$ 判斷。
- **代入計算／推理：** $p=0.3734>0.05$。
- **解讀結論：** 答案是 **b** ；沒有足夠證據認為使用切片器會造成整體位置差異。
- **選項檢討：** a 忽略大 p 值；b 正確；c 不是決策；d 因 b 正確而錯。

#### 題組 18-5：選擇題 44–46 共用資料

> Exhibit 18-5
>
> It has been hypothesized that there is no difference in the mathematical ability of men and women. To test this hypothesis, it was decided to use the Mann-Whitney-Wilcoxon test. A sample of men and women were given math tests. The scores on the tests are given below.

| Women | Score | Men | Score |
|---:|---:|---:|---:|
| 1 | 95 | 1 | 80 |
| 2 | 86 | 2 | 87 |
| 3 | 100 | 3 | 93 |
| 4 | 100 | 4 | 95 |
| 5 | 99 | 5 | 97 |
| 6 | 98 | 6 | 82 |
| 7 | 88 | 7 | 89 |
| 8 | 92 | 8 | 86 |
| 9 | 94 | 9 | 75 |
| 10 | 89 | 10 | 82 |
|  |  | 11 | 79 |

#### 選擇題 44

##### 題目

> Refer to Exhibit 18-5. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

- **辨認題型：** 兩個獨立樣本的 MWW。
- **選方法：** 使用[MWW 常態近似](#formula-ch18-mww-normal)。
- **檢查假設：** $n_1=10,n_2=11$ 都至少 7，符合投影片門檻。
- **代入計算／推理：** $W$ 的抽樣分布以 normal approximation 處理。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 不符合秩和；c 是比較平均數的 t 方法。

#### 選擇題 45

##### 題目

> Refer to Exhibit 18-5. The mean ($\mu_T$) is
>
> a. 10<br>
> b. 110<br>
> c. 66<br>
> d. 55

##### 詳解

- **辨認題型：** 第一群名次和的期望值。
- **選方法：** 使用[MWW 平均公式](#formula-ch18-mww-normal)。
- **檢查假設：** 第一群 women 有 $n_1=10$，第二群 $n_2=11$。
- **代入計算／推理：** $\mu_W=10(10+11+1)/2=110$。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 只是樣本數；b 正確；c、d 是錯誤乘除。

#### 選擇題 46

##### 題目

> Refer to Exhibit 18-5. The standard deviation ($\sigma_T$) is
>
> a. 10<br>
> b. 11.5<br>
> c. 14.2<br>
> d. 110

##### 詳解

- **辨認題型：** MWW 名次和標準差。
- **選方法：** 使用[MWW 標準差公式](#formula-ch18-mww-normal)。
- **檢查假設：** 題庫公式未另做 ties correction。
- **代入計算／推理：** $\sigma_W=\sqrt{10(11)(22)/12}=14.20$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a、b 是錯誤根號或分母；c 正確；d 是平均數。

#### 題組 18-6：選擇題 47–53 共用資料

> Exhibit 18-6
>
> Forty-one individuals from a sample of 60 indicated they oppose legalized abortion. We are interested in determining whether or not there is a significant difference between the proportions of opponents and proponents of legalized abortion.

#### 選擇題 47

##### 題目

> Refer to Exhibit 18-6. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

- **辨認題型：** 兩種立場比例是否相同。
- **選方法：** 使用[符號檢定二項模型](#formula-ch18-sign-binomial)。
- **檢查假設：** 每人落入支持或反對其中一類，樣本共 60。
- **代入計算／推理：** 沒有比例差異即 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 把比例寫成平均數；c 機率不可能為 5；d 正確。

#### 選擇題 48

##### 題目

> Refer to Exhibit 18-6. $\mu$ in this situation is
>
> a. 60<br>
> b. 30<br>
> c. 41<br>
> d. 2

##### 詳解

- **辨認題型：** 正號數的虛無平均。
- **選方法：** 使用[常態近似公式](#formula-ch18-sign-normal)。
- **檢查假設：** $n=60,p=0.5$。
- **代入計算／推理：** $\mu=0.5(60)=30$。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 是總樣本；b 正確；c 是觀察到的反對數；d 是類別數。

#### 選擇題 49

##### 題目

> Refer to Exhibit 18-6. $\sigma$ in this problem is
>
> a. 15<br>
> b. 5.47<br>
> c. 3.87<br>
> d. 7.45

##### 詳解

- **辨認題型：** 正號數標準差。
- **選方法：** 使用[常態近似公式](#formula-ch18-sign-normal)。
- **檢查假設：** $n=60$。
- **代入計算／推理：** $\sigma=\sqrt{0.25(60)}=\sqrt{15}=3.873$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 是變異數；b 對應 $n=120$；c 正確；d 無此計算來源。

#### 選擇題 50

##### 題目

> Refer to Exhibit 18-6. The test statistics is
>
> a. 3.87<br>
> b. 2.84<br>
> c. 60<br>
> d. 0.5

##### 詳解

- **辨認題型：** 符號數 z 統計量。
- **選方法：** 使用[常態近似](#formula-ch18-sign-normal)。
- **檢查假設：** 選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(41-30)/3.873=2.84$；修正後為 $(40.5-30)/3.873=2.71$。
- **解讀結論：** 對應答案是 **b** 。
- **選項檢討：** a 是標準差；b 正確對應題庫；c 是樣本數；d 是虛無機率。

#### 選擇題 51

##### 題目

> Refer to Exhibit 18-6. p-value is
>
> a. 0.0023<br>
> b. 0.0046<br>
> c. 0.4954<br>
> d. 0.4977

##### 詳解

- **辨認題型：** 雙尾常態 p 值。
- **選方法：** 由[常態近似](#formula-ch18-sign-normal)取 $2P(Z\ge2.84)$。
- **檢查假設：** 題庫採未修正 z；精確二項 p 值為 0.00622。
- **代入計算／推理：** $2(0.0023)=0.0046$。
- **解讀結論：** 題庫對應答案是 **b** 。
- **選項檢討：** a 是單尾；b 正確；c、d 把尾端與中央面積混淆。

#### 選擇題 52

##### 題目

> Refer to Exhibit 18-6. The null hypothesis should be
>
> a. Rejected<br>
> b. not rejected<br>
> c. Not enough information is given to answer this question.<br>
> d. None of these alternatives.

##### 詳解

- **辨認題型：** 符號檢定決策。
- **選方法：** 沿用[符號檢定](#formula-ch18-sign-binomial)。
- **檢查假設：** 以 $\alpha=0.05$；題庫近似與精確 p 值都小於 0.05。
- **代入計算／推理：** $p\approx0.0046$，拒絕 $H_0$。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 與 p 值矛盾；c 的資料已足夠；d 因 a 正確而錯。

#### 選擇題 53

##### 題目

> Refer to Exhibit 18-6. The conclusion is that there
>
> a. is no significant difference between the proportions<br>
> b. is a significant difference between the proportions<br>
> c. could be a difference in proportions, depending on the sample size<br>
> d. None of these alternatives is correct.

##### 詳解

- **辨認題型：** 把檢定決策翻成情境語言。
- **選方法：** 依[符號檢定](#formula-ch18-sign-binomial)解讀比例是否各半。
- **檢查假設：** 結論只談比例差異，不談立場形成的因果。
- **代入計算／推理：** 已拒絕 $P=0.5$，且 41 對 19 顯示反對者較多。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 與拒絕結果相反；b 正確；c 忽略已完成的檢定；d 因 b 正確而錯。

### 計算題｜第 1–28 題：完整推論與獨立驗算

#### 計算題 1

##### 題目

> In a sample of 400 people, 250 indicated that they prefer domestic wines, while 140 said they prefer European wines, and 10 indicated no preference. We want to use the sign test to determine if there is evidence of a significant difference in the preferences for the two types of wine.
>
> a. Provide the hypotheses to be tested.<br>
> b. Compute the mean.<br>
> c. Compute the standard deviation.<br>
> d. At 95% confidence, test to determine if there is evidence of a significant difference in the preferences for the two types of wine.

##### 詳解

1. **辨認題型：** 兩種偏好的符號檢定；無偏好者不提供方向。
2. **選方法：** 使用[大樣本符號檢定](#formula-ch18-sign-normal)，檢定 $H_0:p=0.5$ 對 $H_a:p\ne0.5$。
3. **檢查假設：** 刪除 10 位無偏好者後 $n=390$；每人的偏好應彼此獨立，且 $np=n(1-p)=195$ 足夠大。
4. **代入計算／推理：** $\mu=195$，$\sigma=\sqrt{97.5}=9.874$。以 domestic 為正號，連續性修正後 $z=(249.5-195)/9.874=5.519$，雙尾 $p=3.40\times10^{-8}$；精確二項驗算 $p=2.77\times10^{-8}$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；國產酒偏好顯著較多。這不表示每位消費者都偏好國產酒，也不量化偏好強度。

#### 計算題 2

##### 題目

> In a sample of 200 racquetball players, 120 indicated they prefer Penn racquetballs, 75 favored Ektelon, and 5 were indifferent. We want to use the sign test to determine if there is evidence of a significant difference in the preferences for the two types of racquetballs.
>
> a. Provide the hypotheses to be tested.<br>
> b. Compute the mean.<br>
> c. Compute the standard deviation.<br>
> d. At 95% confidence, test to determine if there is evidence of a significant difference in the preferences for the two types of racquetballs.

##### 詳解

1. **辨認題型：** Penn 與 Ektelon 的二選一偏好。
2. **選方法：** 使用[符號檢定常態近似](#formula-ch18-sign-normal)，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 刪除 5 位 indifferent，$n=195$；兩個期望次數都是 97.5。
4. **代入計算／推理：** $\mu=97.5$，$\sigma=\sqrt{48.75}=6.982$；修正後 $z=(119.5-97.5)/6.982=3.151$，雙尾 $p=0.00163$；精確二項 $p=0.00156$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；樣本方向顯示 Penn 較受偏好。

#### 計算題 3

##### 題目

> The monthly sales records of two branches of a department store (Branch A and Branch B) over the last year (12 months) were gathered. It was decided to use the Mann-Whitney-Wilcoxon test to determine if there has been a significant difference between the sales of the two branches.
>
> a. Provide the hypotheses for this test.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute the standard deviation $\sigma_T$.<br>
> d. The sum of the ranks for branch A was determined to be 184.5. Compute the test statistic Z.<br>
> e. Use $\alpha=0.05$ and test to determine if there is a significant difference in the populations of the sales of the two branches.

##### 詳解

1. **辨認題型：** 題目指定兩群 MWW，$H_0$ 為兩分店銷售分布相同，$H_a$ 為不同。
2. **選方法：** 使用[MWW 常態近似](#formula-ch18-mww-normal)。
3. **檢查假設：** 題目把兩分店當獨立樣本，且 $n_1=n_2=12\ge7$。若同月份有共同景氣衝擊，實務上應考慮配對方法；此處依原題指定作答。
4. **代入計算／推理：** $\mu_W=12(25)/2=150$，$\sigma_W=\sqrt{12(12)(25)/12}=\sqrt{300}=17.321$。上尾的連續性修正 $z=(184.5-0.5-150)/17.321=1.963$，雙尾 $p\approx0.0496$。
5. **解讀結論：** 在 0.05 水準勉強拒絕 $H_0$；A 的名次和偏高，顯示 A 銷售傾向較高。結論對連續性修正與獨立性設定敏感，不能忽略月份配對疑慮。

#### 計算題 4

##### 題目

> Independent random samples of the scores of 10 daily quizzes from day students and 15 quizzes from evening students were gathered. It was decided to use the Mann-Whitney-Wilcoxon test to determine if there is a significant difference between the scores of the two groups of students.
>
> a. Provide the hypotheses for this test.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute the standard deviation $\sigma_T$.<br>
> d. The sum of the ranks for the day students was determined to be 184.5. Compute the test statistic Z.<br>
> e. Use $\alpha=0.05$ and test to determine if there is a significant difference in the populations of the scores of the two groups.

##### 詳解

1. **辨認題型：** 日間與夜間兩個獨立群的 MWW。
2. **選方法：** 使用[MWW 常態近似](#formula-ch18-mww-normal)，$H_0$ 為兩分布相同。
3. **檢查假設：** $n_1=10,n_2=15$ 都至少 7；兩群樣本需獨立。
4. **代入計算／推理：** $\mu_W=10(26)/2=130$，$\sigma_W=\sqrt{10(15)(26)/12}=18.028$；修正後 $z=(184.5-0.5-130)/18.028=2.995$，雙尾 $p\approx0.00274$。
5. **解讀結論：** $p<0.05$，拒絕兩群分布相同；日間生名次和偏高，分數傾向較高，但不直接等同平均分數差。

#### 計算題 5

##### 題目

> The sales records of two branches of a department store over the last 12 months are shown below. (Sales figures are in thousands of dollars.) We want to use the Mann-Whitney-Wilcoxon test to determine if there is a significant difference in the sales of the two branches.

| Month | Branch A | Branch B |
|---:|---:|---:|
| 1 | 257 | 210 |
| 2 | 280 | 230 |
| 3 | 200 | 250 |
| 4 | 250 | 260 |
| 5 | 284 | 275 |
| 6 | 295 | 300 |
| 7 | 297 | 320 |
| 8 | 265 | 290 |
| 9 | 330 | 310 |
| 10 | 350 | 325 |
| 11 | 340 | 329 |
| 12 | 272 | 335 |

> a. Compute the sum of the ranks (T) for branch A.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute $\sigma_T$.<br>
> d. Use $\alpha=0.05$ and test to determine if there is a significant difference in the populations of the sales of the two branches.

##### 詳解

1. **辨認題型：** 題目指定兩群獨立樣本 MWW。
2. **選方法：** 合併 24 筆資料，使用[MWW 名次和與常態近似](#formula-ch18-mww-normal)。
3. **檢查假設：** 兩群各 12 筆；250 同值使用平均名次。月份可能形成天然配對，但依原題指定 MWW。
4. **代入計算／推理：** Branch A 的名次和 $W=148.5$，$\mu_W=150$，$\sigma_W=17.321$；修正後 $|z|=(|148.5-150|-0.5)/17.321=0.058$，雙尾 $p=0.9540$。tie-aware 軟體驗算 $p=0.95395$。
5. **解讀結論：** 不拒絕 $H_0$；兩分店名次高度混合，沒有足夠證據認為銷售分布不同。

#### 計算題 6

##### 題目

> Independent random samples of ten day students and ten evening students at a university showed the following age distributions. We want to use the Mann-Whitney-Wilcoxon test to determine if there is a significant difference in the age distribution of the two groups.

| Day | Evening |
|---:|---:|
| 26 | 32 |
| 18 | 24 |
| 25 | 23 |
| 27 | 30 |
| 19 | 40 |
| 30 | 41 |
| 34 | 42 |
| 21 | 39 |
| 33 | 45 |
| 31 | 35 |

> a. Compute the sum of the ranks (T) for the day students.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute $\sigma_T$.<br>
> d. Use $\alpha=0.05$ and test for any significant differences in the age distribution of the two populations.

##### 詳解

1. **辨認題型：** 日間與夜間學生是兩個獨立樣本。
2. **選方法：** 使用[MWW](#formula-ch18-mww-normal)，檢查兩群年齡分布是否相同。
3. **檢查假設：** 兩群各 10 人且獨立；30 歲同值給平均名次。
4. **代入計算／推理：** 日間組 $W=74.5$，$\mu_W=105$，$\sigma_W=13.229$；連續性修正後 $z=-2.268$，雙尾 $p=0.02334$，tie-aware 驗算 $p=0.02329$。
5. **解讀結論：** $p<0.05$，拒絕兩群年齡分布相同；日間生名次和偏低，年齡傾向較小。

#### 計算題 7

##### 題目

> From the courthouse records, it is found that in 60 divorce cases, the filing for divorce was initiated by the wife 41 times. Using the sign test, test for a difference in filing between husband and wives. Let $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 60 件案件中由妻／夫提出的二元比例是否各半。
2. **選方法：** 使用[符號檢定](#formula-ch18-sign-binomial)，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 各案件應可合理視為獨立，沒有平手；$n=60$ 可常態近似。
4. **代入計算／推理：** $\mu=30$，$\sigma=3.873$；修正後 $z=(40.5-30)/3.873=2.711$，雙尾近似 $p=0.00671$，精確二項 $p=0.00622$。
5. **解讀結論：** $p<0.05$，拒絕各半；妻子提出的比例顯著較高。法院紀錄是觀察資料，不能由此推論造成離婚的原因。

#### 計算題 8

##### 題目

> Two employers (A and B) ranked five candidates for a new position. Their rankings of the candidates are shown below.

| Candidate | Rank by A | Rank by B |
|---|---:|---:|
| Nancy | 2 | 1 |
| Mary | 1 | 3 |
| John | 3 | 4 |
| Lynda | 5 | 5 |
| Steve | 4 | 2 |

> Compute the Spearman rank-correlation and test it for significance. Let $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 同五位候選人的兩套完整排名。
2. **選方法：** 使用[Spearman 等級相關](#formula-ch18-spearman)，$H_0:\rho_s=0$。
3. **檢查假設：** 沒有同名次；但 $n=5<10$，不能套投影片的大樣本常態近似作正式決策。
4. **代入計算／推理：** $\sum d_i^2=10$，$r_s=1-6(10)/[5(25-1)]=0.500$。窮舉 $5!=120$ 種排列，雙尾精確 $p=0.450$。
5. **解讀結論：** 不拒絕 $H_0$；樣本呈中度正向排序，但五人太少，沒有足夠證據認定母體排序相關。

#### 計算題 9

##### 題目

> The following data show the test scores of six individuals on a standardized test before and after attending a preparation seminar for the test.

| Person | Before | After |
|---|---:|---:|
| A | 108 | 110 |
| B | 102 | 118 |
| C | 107 | 105 |
| D | 97 | 97 |
| E | 112 | 116 |
| F | 108 | 106 |

> Use the Wilcoxon Signed-Rank test in order to determine whether or nor the seminar has been effective. Hint: This is a one tailed test. Let $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 同一人課前／課後，是配對數值；有效表示課後較高。
2. **選方法：** 使用[Wilcoxon signed-rank](#formula-ch18-signed-rank)，令 $d=After-Before$，$H_a$ 為位置差大於 0。
3. **檢查假設：** D 的零差刪除，剩 $n=5$；需假設非零差近似對稱。小樣本使用精確／排列概念。
4. **代入計算／推理：** 差值為 2、16、-2、0、4、-2；平均名次後 $T^+=11,T^-=4$。枚舉五個非零名次的 $2^5=32$ 種正負配置，一尾精確 $p=0.250$。
5. **解讀結論：** $p>0.05$，沒有足夠證據認為研習使分數整體提高；少數大幅進步不足以壓過小樣本不確定性。

#### 計算題 10

##### 題目

> Fifteen people were asked to indicate their preference for domestic versus imported cars. The following data showed their preferences.

| Individual | Domestic vs. Imported |
|---:|:---:|
| 1 | + |
| 2 | + |
| 3 | - |
| 4 | + |
| 5 | + |
| 6 | + |
| 7 | - |
| 8 | + |
| 9 | + |
| 10 | + |
| 11 | + |
| 12 | + |
| 13 | + |
| 14 | + |
| 15 | - |

> With $\alpha=0.05$, test for a significant difference in the preferences for cars. A "+" indicates a preference for imported cars.

##### 詳解

1. **辨認題型：** 15 個二元偏好的小樣本符號檢定。
2. **選方法：** 使用[精確二項符號檢定](#formula-ch18-sign-binomial)，$H_0:p=0.5$。
3. **檢查假設：** 12 個正號、3 個負號，沒有平手；每人應獨立。
4. **代入計算／推理：** 雙尾 $p=2P(X\ge12)=2P(X\le3)=0.035156$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；正號較多，樣本支持進口車較受偏好。

#### 計算題 11

##### 題目

> The following data show the preference of 20 people for a candidate to a public office. A "+" indicates a preference for the Democratic candidate, and a "-" indicates a preference for the Republican candidate.

| Individual | Republicans vs. Democrats | Individual | Republicans vs. Democrats |
|---:|:---:|---:|:---:|
| 1 | + | 11 | + |
| 2 | - | 12 | - |
| 3 | + | 13 | - |
| 4 | + | 14 | + |
| 5 | + | 15 | + |
| 6 | + | 16 | - |
| 7 | - | 17 | - |
| 8 | + | 18 | + |
| 9 | + | 19 | + |
| 10 | + | 20 | + |

> With $\alpha=0.05$, test for a significant difference in the preference for the candidates.

##### 詳解

1. **辨認題型：** 20 人兩候選人偏好的符號檢定。
2. **選方法：** 使用[精確二項模型](#formula-ch18-sign-binomial)，$H_0:p=0.5$。
3. **檢查假設：** 14 個正號、6 個負號；投影片在 $n\le20$ 使用 exact binomial。
4. **代入計算／推理：** 雙尾 $p=2P(X\ge14)=0.115318$。
5. **解讀結論：** $p>0.05$，不能拒絕各半；雖民主黨候選人在樣本中較多，證據尚不足以推廣到母體。

#### 計算題 12

##### 題目

> In a sample of 120 people, 50 indicated that they prefer domestic automobiles, 60 said they prefer foreign-made cars, and 10 indicated no difference in their preference. At a 0.05 level of significance, determine if there is evidence of a significant difference in the preferences for the two makes of automobiles.

##### 詳解

1. **辨認題型：** 兩車種偏好的大樣本符號檢定。
2. **選方法：** 使用[符號檢定常態近似](#formula-ch18-sign-normal)。
3. **檢查假設：** 刪除 10 位無差異者，$n=110$；正負期望各 55。
4. **代入計算／推理：** $\sigma=\sqrt{27.5}=5.244$；修正後 $|z|=(|60-55|-0.5)/5.244=0.858$，雙尾 $p=0.3908$；精確 p $=0.3909$。
5. **解讀結論：** 不拒絕 $H_0$；沒有足夠證據認為國產與進口車偏好比例不同。

#### 計算題 13

##### 題目

> In a sample of 300 shoppers, 160 indicated they prefer fluoride toothpaste, 120 favored nonfluoride, and 20 were indifferent. At a 0.05 level of significance, test for a difference in the preference for the two kinds of toothpaste.

##### 詳解

1. **辨認題型：** 含平手的兩種牙膏偏好。
2. **選方法：** 使用[大樣本符號檢定](#formula-ch18-sign-normal)。
3. **檢查假設：** 刪除 20 位 indifferent，$n=280$，$\mu=140$。
4. **代入計算／推理：** $\sigma=\sqrt{70}=8.367$；修正後 $z=(159.5-140)/8.367=2.331$，雙尾 $p=0.01977$；精確 p $=0.01961$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；含氟牙膏在樣本中較受偏好。

#### 計算題 14

##### 題目

> Test scores of ten individuals before and after a training program are shown below.

| Individual | Score Before the Program | Score After the Program |
|---:|---:|---:|
| 1 | 59 | 57 |
| 2 | 57 | 62 |
| 3 | 60 | 60 |
| 4 | 66 | 63 |
| 5 | 68 | 69 |
| 6 | 59 | 63 |
| 7 | 72 | 74 |
| 8 | 52 | 56 |
| 9 | 58 | 64 |
| 10 | 63 | 64 |

> At $\alpha=0.05$, what can be concluded about the effectiveness of the training program?

##### 詳解

1. **辨認題型：** 同十人的前後分數，問訓練是否使分數提高。
2. **選方法：** 使用[Wilcoxon signed-rank](#formula-ch18-signed-rank)，令 $d=After-Before$，作右尾檢定。
3. **檢查假設：** 第 3 人零差刪除後 $n=9$；非零差需近似對稱。樣本小，使用精確／排列處理。
4. **代入計算／推理：** $T^+=36.5,T^-=8.5$；枚舉九個非零名次的 $2^9=512$ 種正負配置，一尾精確 $p=0.05469$。
5. **解讀結論：** $p$ 略高於 0.05，不能拒絕 $H_0$；樣本有進步方向，但證據剛好未達門檻。若改用某些 ties 的大樣本近似可能跨過 0.05，因此應優先報告本題小樣本精確結果與個人差值。

#### 計算題 15

##### 題目

> Ten drivers were asked to drive two models of a car. Each car was given one gallon of gasoline. The distance that each automobile traveled on a gallon of gasoline is shown below.

| Driver | Model A | Model B |
|---:|---:|---:|
| 1 | 27.7 | 27.1 |
| 2 | 28.4 | 28.0 |
| 3 | 28.9 | 28.7 |
| 4 | 27.9 | 27.6 |
| 5 | 26.5 | 26.0 |
| 6 | 29.1 | 29.0 |
| 7 | 28.9 | 28.2 |
| 8 | 28.9 | 28.0 |
| 9 | 28.8 | 28.0 |
| 10 | 28.0 | 27.0 |

> At $\alpha=0.05$, what can be concluded about the performance of the two models?

##### 詳解

1. **辨認題型：** 同十位駕駛測兩車，是配對數值比較。
2. **選方法：** 使用[Wilcoxon signed-rank](#formula-ch18-signed-rank)，令 $d=A-B$，作雙尾比較。
3. **檢查假設：** 十個差值都非零且全為正；需假設配對差近似對稱。
4. **代入計算／推理：** $T^+=55,T^-=0$；精確雙尾 $p=2/2^{10}=0.001953$。
5. **解讀結論：** $p<0.05$，兩車表現有差；所有駕駛下 A 都跑得更遠，方向支持 Model A 的每加侖里程較高。

#### 計算題 16

##### 題目

> A PTA group wishes to determine whether a barrage of letters sent to the local station has reduced the amount of violence broadcast between the hours of 4 P.M. and 9 P.M. The results of a survey of viewers are given here.

| Response | Number of Respondents |
|---|---:|
| More Violence | 4 |
| Less Violence | 11 |
| No Change | 6 |

> Carry out a sign test to determine whether or not the letters were effective in reducing the amount of violence during the 4 to 9 p.m. period. Use a .05 level of significance. Be sure to state the null and alternative hypotheses.

##### 詳解

1. **辨認題型：** 觀眾認為暴力增加／減少的方向資料，問是否減少，是單尾符號檢定。
2. **選方法：** 使用[精確符號檢定](#formula-ch18-sign-binomial)。令正號為 Less Violence，$H_0:p\le0.5$、$H_a:p>0.5$。
3. **檢查假設：** 6 位 No Change 刪除，有效 $n=15$；受訪者意見需近似獨立。
4. **代入計算／推理：** 觀察正號 11 個，一尾 $p=P(X\ge11)=0.05923$。
5. **解讀結論：** $p>0.05$，不能拒絕 $H_0$；樣本多數認為暴力減少，但證據尚未達 5% 門檻，不能宣稱信件有效。

#### 計算題 17

##### 題目

> A clothing manufacturer purchased some newly designed sewing machines in the hopes that production would be increased. The production records of a random sample of workers are shown below.

| Worker | Old Machine | New Machine |
|---:|---:|---:|
| 1 | 28 | 36 |
| 2 | 36 | 40 |
| 3 | 27 | 25 |
| 4 | 25 | 32 |
| 5 | 38 | 30 |
| 6 | 36 | 32 |
| 7 | 40 | 40 |
| 8 | 29 | 28 |
| 9 | 32 | 35 |
| 10 | 28 | 33 |
| 11 | 20 | 26 |
| 12 | 32 | 31 |
| 13 | 32 | 23 |
| 14 | 32 | 34 |
| 15 | 36 | 36 |

> Use the Wilcoxon signed-rank test to determine whether the new machines have significantly increased production. Use a .05 level of significance.

##### 詳解

1. **辨認題型：** 同一批工人的新舊機器產量，問新機器是否提高，是配對右尾檢定。
2. **選方法：** 使用[Wilcoxon signed-rank](#formula-ch18-signed-rank)，令 $d=New-Old$。
3. **檢查假設：** Workers 7、15 零差刪除，$n=13$；差值分布需近似對稱。
4. **代入計算／推理：** 平均同名次後 $T^+=53.5,T^-=37.5$；枚舉 $2^{13}=8,192$ 種正負配置，一尾精確 $p=0.29993$。
5. **解讀結論：** $p>0.05$，沒有足夠證據認為新機器提升產量；正負差與大名次沒有一致朝增加方向集中。

#### 計算題 18

##### 題目

> The president of a company wants to see if the new anti-smoking campaign is having any influence on his employees. A sample of 100 employees who smoked prior to the campaign is taken. Thirty-six employees said they smoked less, 15 employees said they smoked more, and 49 employees said there was no change.
>
> a. State the null and alternative hypotheses.<br>
> b. Test the null hypothesis at the 1% level of significance.

##### 詳解

1. **辨認題型：** 抽菸變少／變多的方向是否失衡；`any influence` 表示雙尾。
2. **選方法：** 使用[符號檢定](#formula-ch18-sign-binomial)，令正號為 smoked less，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 刪除 49 位 no change，$n=51$；各員工回應應近似獨立。
4. **代入計算／推理：** $\mu=25.5$，$\sigma=3.571$；修正後 $z=(35.5-25.5)/3.571=2.801$，雙尾近似 $p=0.00510$，精確 p $=0.00460$。
5. **解讀結論：** $p<0.01$，拒絕無影響；方向顯示回報抽得較少者較多。這是自陳的前後變化，不能單靠檢定排除其他同期因素。

#### 計算題 19

##### 題目

> It is believed that the median age of college students is 21 years. A sample of 80 college students is taken. Thirty of the students were under 21, 45 of the students were over 21, and 10 were 21 years old.
>
> a. State the null and alternative hypotheses.<br>
> b. Test the null hypothesis at the 1% level of significance.

##### 詳解

1. **辨認題型：** 母體中位數 21 歲的雙尾符號檢定。
2. **選方法：** 使用[符號檢定](#formula-ch18-sign-binomial)，$H_0:\text{Median}=21$、$H_a:\text{Median}\ne21$。
3. **檢查假設：** 原題有來源疑義：30 + 45 + 10 = 85，與宣稱的樣本 80 不一致。題幹無法同時全部成立，因此不能無條件給唯一答案。
4. **代入計算／推理：** 若忠實採三個分類次數，刪除 10 位平手後 $n=75$，正號 45、負號 30；精確雙尾 $p=0.10534$，連續性修正近似 $p=0.10597$。
5. **解讀結論：** 在上述可驗算處理下 $p>0.01$，不拒絕中位數 21 歲；但正式作答應先向出題者確認總樣本或其中一個分類數，不能把不一致資料悄悄修掉。

#### 計算題 20

##### 題目

> We want to see if the workers on the day and night shifts differ significantly in their productivity levels. A sample of workers from both shifts was taken.

| Day Shift | Output | Night Shift | Output |
|---:|---:|---:|---:|
| 1 | 31 | 1 | 31 |
| 2 | 32 | 2 | 25 |
| 3 | 26 | 3 | 29 |
| 4 | 34 | 4 | 30 |
| 5 | 24 | 5 | 27 |
| 6 | 35 | 6 | 33 |
| 7 | 39 | 7 | 37 |
| 8 | 28 | 8 | 39 |
| 9 | 44 | 9 | 38 |
| 10 | 42 | 10 | 36 |
|  |  | 11 | 40 |

> a. State the null and alternative hypotheses.<br>
> b. Test the null hypothesis at the 5% level of significance.

##### 詳解

1. **辨認題型：** 日班與夜班是兩個獨立群，問生產力分布是否不同。
2. **選方法：** 使用[MWW](#formula-ch18-mww-normal)，$H_0$ 為兩母體分布相同，$H_a$ 為不同。
3. **檢查假設：** $n_1=10,n_2=11$ 都至少 7；兩班工人彼此獨立；31、39 同值用平均名次。
4. **代入計算／推理：** 日班名次和 $W=111$，$\mu_W=110$，$\sigma_W=14.201$；修正後 $|z|=0.035$，雙尾 $p=0.9719$，tie-aware 驗算一致。
5. **解讀結論：** 不拒絕 $H_0$；兩班高低名次幾乎完全混合，沒有分布差異證據。

#### 計算題 21

##### 題目

> The manager of a company believes that differences in sales performance depends upon the salesperson's age. Independent samples of salespeople were taken and their weekly sales record is reported below.

| Below 30 Years | Between 30 & 45 Years | Over 45 Years |
|---:|---:|---:|
| 24 | 23 | 30 |
| 16 | 17 | 20 |
| 21 | 22 | 23 |
| 15 | 25 | 25 |
| 19 | 18 | 34 |
| 26 | 29 | 36 |
|  | 27 | 28 |

> a. State the null and alternative hypotheses.<br>
> b. At 95% confidence, test the hypotheses.

##### 詳解

1. **辨認題型：** 三個獨立年齡群的銷售分布比較。
2. **選方法：** 使用[Kruskal-Wallis](#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同，$H_a$ 為至少一群不同。
3. **檢查假設：** 樣本數為 6、7、7，均至少 5；各業務員獨立；同值採平均名次並做 ties correction。
4. **代入計算／推理：** 名次和為 40、69、101；未修正 $H=5.688$，ties-corrected $H=5.697$，$df=2$，$p=0.05793$。
5. **解讀結論：** $p>0.05$，不能拒絕三群分布相同。45 歲以上名次偏高是樣本線索，但尚未達顯著，更不能推論年齡造成銷售差異。

#### 計算題 22

##### 題目

> Two faculty members ranked 12 candidates for scholarships. Calculate the Spearman rank-correlation coefficient and test it for significance. Use a .02 level of significance.

| Candidate | Rank by Professor A | Rank by Professor B |
|---:|---:|---:|
| 1 | 6 | 5 |
| 2 | 10 | 11 |
| 3 | 2 | 6 |
| 4 | 1 | 3 |
| 5 | 5 | 4 |
| 6 | 11 | 12 |
| 7 | 4 | 2 |
| 8 | 3 | 1 |
| 9 | 7 | 7 |
| 10 | 12 | 10 |
| 11 | 9 | 8 |
| 12 | 8 | 9 |

##### 詳解

1. **辨認題型：** 同 12 人的兩套完整排名。
2. **選方法：** 使用[Spearman 係數與常態檢定](#formula-ch18-spearman-test)，$H_0:\rho_s=0$、$H_a:\rho_s\ne0$。
3. **檢查假設：** 無 ties，$n=12\ge10$，符合投影片近似門檻。
4. **代入計算／推理：** $\sum d_i^2=38$，$r_s=1-6(38)/[12(12^2-1)]=0.8671$；$z=r_s\sqrt{11}=2.876$，雙尾 $p=0.00403$。
5. **解讀結論：** $p<0.02$，拒絕零等級相關；兩位教授的排序高度同向，但並非完全一致。

#### 計算題 23

##### 題目

> A comprehensive statistics examination is given to 16 students in order to determine whether or not there is a significant difference in the performance of students majoring in the various disciplines of Business Administration. The following data show the scores of the 16 students (5 majoring in accounting, 6 majoring in management, and 5 majoring in marketing).

| Accounting | Management | Marketing |
|---:|---:|---:|
| 91 | 63 | 95 |
| 80 | 92 | 80 |
| 70 | 86 | 70 |
| 60 | 75 | 60 |
| 85 | 70 | 90 |
|  | 99 |  |

> At $\alpha=0.05$ level of significance, test to see if there is a significant difference in the performance of the students in the three majors.

##### 詳解

1. **辨認題型：** 三個獨立主修群的考試分數比較。
2. **選方法：** 使用[Kruskal-Wallis](#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同。
3. **檢查假設：** 群大小 5、6、5，符合投影片每群至少 5；學生獨立；60、70、80 等 ties 要平均名次並修正。
4. **代入計算／推理：** 名次和 38、56、42；未修正 $H=0.3647$，ties-corrected $H=0.3680$，$df=2$，$p=0.8320$。
5. **解讀結論：** 不拒絕 $H_0$；三群名次高度混合，沒有足夠證據認為表現分布不同。

#### 計算題 24

##### 題目

> A survey of male and female students showed the following ranking of 12 professors in the management department:

| Professor | Ranking By Female Students | Ranking By Male Students |
|---:|---:|---:|
| 1 | 7 | 8 |
| 2 | 8 | 7 |
| 3 | 1 | 2 |
| 4 | 2 | 3 |
| 5 | 9 | 1 |
| 6 | 3 | 10 |
| 7 | 10 | 9 |
| 8 | 11 | 4 |
| 9 | 4 | 6 |
| 10 | 6 | 11 |
| 11 | 12 | 5 |
| 12 | 5 | 12 |

> Do the rankings given by the female students agree with the rankings given by the male students? Use $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 同 12 位教授的兩套排名是否一致。
2. **選方法：** 使用[Spearman 等級相關檢定](#formula-ch18-spearman-test)。
3. **檢查假設：** 兩欄都是 1–12 的完整排名，無 ties；$n=12\ge10$。
4. **代入計算／推理：** $\sum d_i^2=294$，$r_s=-0.02797$；$z=-0.0928$，雙尾 $p=0.9261$。
5. **解讀結論：** 不拒絕 $\rho_s=0$；兩組學生的排序幾乎沒有單調一致性。這不是證明兩組對每位教授都持相反看法。

#### 計算題 25

##### 題目

> Two individuals were asked to rank the performances of eight different automobiles. The following show their rankings.

| Automobile | Ranking by First Person | Ranking by Second Person |
|---:|---:|---:|
| 1 | 3 | 2 |
| 2 | 5 | 1 |
| 3 | 1 | 4 |
| 4 | 6 | 7 |
| 5 | 2 | 5 |
| 6 | 4 | 8 |
| 7 | 7 | 6 |
| 8 | 8 | 3 |

> Determine the Spearman rank-correlation coefficient; and at 95% confidence, test for its significance.

##### 詳解

1. **辨認題型：** 八輛車的兩套完整排名。
2. **選方法：** 使用[Spearman 係數](#formula-ch18-spearman)，檢查 $H_0:\rho_s=0$。
3. **檢查假設：** 無 ties；$n=8<10$，正式決策用精確排列，不用投影片的大樣本 z。
4. **代入計算／推理：** $\sum d_i^2=78$，$r_s=1-6(78)/[8(8^2-1)]=0.07143$；窮舉 $8!=40,320$ 種排列得雙尾精確 $p=0.8820$。
5. **解讀結論：** 不拒絕零相關；兩人的排序幾乎沒有同向單調關聯。

#### 計算題 26

##### 題目

> Two groups of students were asked to rank the activities sponsored by the Student Government Association on campus. The following show their rankings.

| Activity | Resident Student Ranking | Nonresident Student Ranking |
|---:|---:|---:|
| 1 | 3 | 6 |
| 2 | 1 | 2 |
| 3 | 8 | 5 |
| 4 | 2 | 1 |
| 5 | 5 | 7 |
| 6 | 7 | 8 |
| 7 | 4 | 3 |
| 8 | 6 | 4 |

> Determine the Spearman rank-correlation coefficient and test for a significant correlation with $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 八項活動在住宿生與非住宿生中的兩套排名。
2. **選方法：** 使用[Spearman 係數](#formula-ch18-spearman)。
3. **檢查假設：** 無 ties；$n=8<10$，以精確排列 p 值作決策。
4. **代入計算／推理：** $\sum d_i^2=30$，$r_s=0.64286$；精確雙尾 $p=0.09618$。若誤用常態近似會得約 0.089，決策仍相同。
5. **解讀結論：** $p>0.05$，不能認定母體排序相關；樣本有中度正向一致，但八項活動的證據不足。

#### 計算題 27

##### 題目

> Two faculty members (X and Y) ranked five candidates for scholarships. The rankings are shown below.

| Candidate | Rank By X | Rank By Y |
|---|---:|---:|
| Peter | 5 | 1 |
| Nancy | 2 | 2 |
| Michael | 1 | 3 |
| Mary | 3 | 5 |
| Judy | 4 | 4 |

> Compute the Spearman rank-correlation and test it for significance. Let $\alpha=0.05$.

##### 詳解

1. **辨認題型：** 五位候選人的兩套排名。
2. **選方法：** 使用[Spearman 係數](#formula-ch18-spearman)。
3. **檢查假設：** 無 ties；$n=5<10$，使用精確排列。
4. **代入計算／推理：** $\sum d_i^2=24$，$r_s=-0.200$；$5!=120$ 種排列的雙尾精確 $p=0.7833$。
5. **解讀結論：** 不拒絕零相關；觀察到的輕微反向排序很可能只是小樣本波動。

#### 計算題 28

##### 題目

> Three universities in your state have decided to administer the same comprehensive examination to the recipients of MBA degrees. From each institution, a random sample of MBA recipients has been selected and given the test. The following table shows the scores of the students from each university.

| Northern University | Central University | Southern University |
|---:|---:|---:|
| 56 | 62 | 94 |
| 85 | 97 | 72 |
| 65 | 91 | 93 |
| 86 | 82 | 78 |
| 93 |  | 54 |
|  |  | 77 |

> Use the Kruskal-Wallis test to determine if there is a significant difference in the average scores of the students from the three universities. Let $\alpha=0.01$.

##### 詳解

1. **辨認題型：** 三所大學的獨立分數樣本；原題雖寫 average scores，但指定 Kruskal-Wallis，檢定的是分布／名次位置。
2. **選方法：** 使用[Kruskal-Wallis](#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同。
3. **檢查假設：** 樣本獨立且隨機；群大小為 5、4、6。Central 只有 4 人，未達投影片每群 $n_i\ge5$ 的卡方近似門檻，因此另做精確隨機化驗算。
4. **代入計算／推理：** 名次和為 37.5、37、45.5；未修正 $H=0.4271$，ties-corrected $H=0.4278$。卡方近似 $p=0.8074$；枚舉所有保持 5／4／6 群大小的標籤分配，精確右尾 $p=0.8234$。
5. **解讀結論：** 兩種算法都遠大於 0.01，不拒絕 $H_0$；沒有足夠證據認為三校分數分布不同。這不是證明三校平均數完全相等。
