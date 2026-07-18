# 第 12 章：卡方檢定｜考古題詳解

## 考古題詳解

本章收錄 82 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–47 題

#### 選擇題 1 <a id="exam-ch12-mc-1"></a>

##### 題目

> A population where each element of the population is assigned to one and only one of several classes or categories is a
>
> a. multinomial population<br>
> b. Poisson population<br>
> c. normal population<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 這是類別資料的定義題。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，每個元素只落入一個互斥類別，就是多項母體。
- **檢查假設：** 類別需互斥且完整；題幹已明示。
- **計算／推理：** 不需數值計算；對照[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)的資料結構即可。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b 會讓人因「事件次數」想到 Poisson，但題幹只談分類；c 會讓人因常見分配而誤選，但常態是連續數值模型；d 錯，因 a 已精確描述。

#### 選擇題 2 <a id="exam-ch12-mc-2"></a>

##### 題目

> The sampling distribution for a goodness of fit test is the
>
> a. Poisson distribution<br>
> b. t distribution<br>
> c. normal distribution<br>
> d. chi-square distribution

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 適合度檢定的參考分配。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，觀察與期望次數的整體落差使用卡方分配。
- **檢查假設：** 期望次數需足夠大。
- **計算／推理：** [卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)在 $H_0$ 下以卡方分配近似。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 可能是被檢查的理論模型，不是檢定統計量的參考分配；b 用於平均數推論；c 常用於 $z$ 推論；d 正確。

#### 選擇題 3 <a id="exam-ch12-mc-3"></a>

##### 題目

> A goodness of fit test is always conducted as a
>
> a. lower-tail test<br>
> b. upper-tail test<br>
> c. middle test<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** 拒絕域方向題。
- **選方法：** 適合度檢定使用右尾規則。
- **檢查假設：** 卡方統計量為非負，越大越不符合 $H_0$。
- **計算／推理：** 由[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)，極端方向是 $P(\chi^2\ge\chi^2_{obs})$。
- **解讀結論：** 答案是 **b**。
- **選項檢討：** a 把小統計量誤當不相符；b 正確；c 不是標準檢定名稱；d 錯，因 b 明確正確。

#### 選擇題 4 <a id="exam-ch12-mc-4"></a>

##### 題目

> An important application of the chi-square distribution is
>
> a. making inferences about a single population variance<br>
> b. testing for goodness of fit<br>
> c. testing for the independence of two variables<br>
> d. All of these alternatives are correct.

##### 詳解

> **回看投影片講義：** [卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)


- **辨認題型：** 卡方分配用途題。
- **選方法：** 分別辨識變異數推論、適合度與獨立性。
- **檢查假設：** 三者各有自己的資料與抽樣條件。
- **計算／推理：** 本章的[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)涵蓋 b、c；單一常態母體變異數推論也使用卡方分配。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a、b、c 各自都是真用途，單選任一會漏掉其他正確敘述；d 才完整。

#### 選擇題 5 <a id="exam-ch12-mc-5"></a>

##### 題目

> The number of degrees of freedom for the appropriate chi-square distribution in a test of independence is
>
> a. $n-1$<br>
> b. $K-1$<br>
> c. number of rows minus 1 times number of columns minus 1<br>
> d. a chi-square distribution is not used

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** 列聯表獨立性自由度。
- **選方法：** 使用獨立性檢定，不是單一類別適合度。
- **檢查假設：** 表格有 $r$ 列、$c$ 欄。
- **計算／推理：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)是 $(r-1)(c-1)$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 把樣本變異數自由度搬來；b 只適用一般 $k$ 類適合度；c 正確；d 錯，獨立性正是卡方用途。

#### 選擇題 6 <a id="exam-ch12-mc-6"></a>

##### 題目

> In order not to violate the requirements necessary to use the chi-square distribution, each expected frequency in a goodness of fit test must be
>
> a. at least 5<br>
> b. at least 10<br>
> c. no more than 5<br>
> d. less than 2

##### 詳解

> **回看投影片講義：** [適合度期望公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 卡方近似條件。
- **選方法：** 檢查每類期望次數。
- **檢查假設：** 本課採每個期望次數至少 5 的規則。
- **計算／推理：** 期望次數由[適合度期望公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)計算，再逐格檢查。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b 比課程規則更嚴但不是題目指定門檻；c、d 都把方向顛倒，期望次數太小才是問題。

#### 選擇題 7 <a id="exam-ch12-mc-7"></a>

##### 題目

> A statistical test conducted to determine whether to reject or not reject a hypothesized probability distribution for a population is known as a
>
> a. contingency test<br>
> b. probability test<br>
> c. goodness of fit test<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 方法名稱定義題。
- **選方法：** 一個樣本分布和指定機率分布比較，就是適合度檢定。
- **檢查假設：** 類別互斥完整，期望次數足夠。
- **計算／推理：** 對應[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 容易和 contingency table 混淆，但題目沒有兩個變數；b 不是標準方法名；c 正確；d 錯。

#### 選擇題 8 <a id="exam-ch12-mc-8"></a>

##### 題目

> The degrees of freedom for a contingency table with 12 rows and 12 columns is
>
> a. 144<br>
> b. 121<br>
> c. 12<br>
> d. 120

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** $12\times12$ 列聯表自由度。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** 題目給的是列與欄類別數，不是樣本數。
- **計算／推理：** $df=(12-1)(12-1)=121$。
- **解讀結論：** 答案是 **b**。
- **選項檢討：** a 是直接乘 $12\times12$；b 正確；c 只保留一個維度；d 類似 $n-1$ 的誤套。

#### 選擇題 9 <a id="exam-ch12-mc-9"></a>

##### 題目

> The degrees of freedom for a contingency table with 6 rows and 3 columns is
>
> a. 18<br>
> b. 15<br>
> c. 6<br>
> d. 10

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** $6\times3$ 列聯表自由度。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** $r=6,c=3$。
- **計算／推理：** $df=(6-1)(3-1)=10$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 是未減 1 就相乘；b 只將列減 1；c 誤把列數當自由度；d 正確。

#### 選擇題 10 <a id="exam-ch12-mc-10"></a>

##### 題目

> The degrees of freedom for a contingency table with 10 rows and 11 columns is
>
> a. 100<br>
> b. 110<br>
> c. 21<br>
> d. 90

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** $10\times11$ 列聯表自由度。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** $r=10,c=11$。
- **計算／推理：** $df=(10-1)(11-1)=90$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 只減了其中一邊後誤乘；b 是格子總數；c 是列欄相加；d 正確。

#### 題組 12-1：選擇題 11–15 共用資料

> When individuals in a sample of 150 were asked whether or not they supported capital punishment, the following information was obtained. We are interested in determining whether the opinions are uniformly distributed.

| Do you support capital punishment? | Number of individuals |
|---|---:|
| Yes | 40 |
| No | 60 |
| No Opinion | 50 |

在均勻分布下，每類機率是 $1/3$，所以期望次數都是 $150/3=50$。

#### 選擇題 11 <a id="exam-ch12-mc-11"></a>

##### 題目

> Refer to Exhibit 12-1. The expected frequency for each group is
>
> a. 0.333<br>
> b. 0.50<br>
> c. 1/3<br>
> d. 50

##### 詳解

> **回看投影片講義：** [多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 均勻多項適合度的期望次數。
- **選方法：** 一個類別變數對指定均勻比例，選適合度檢定。
- **檢查假設：** 三類互斥完整，$n=150$。
- **計算／推理：** 依[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)，$E=150(1/3)=50$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a、c 是機率而非次數；b 既不是每類機率也不是期望次數；d 正確。

#### 選擇題 12 <a id="exam-ch12-mc-12"></a>

##### 題目

> Refer to Exhibit 12-1. The calculated value for the test statistic equals
>
> a. 2<br>
> b. -2<br>
> c. 20<br>
> d. 4

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 均勻適合度卡方值。
- **選方法：** 使用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 三個期望次數皆為 50，均至少 5。
- **計算／推理：** $\chi^2=(40-50)^2/50+(60-50)^2/50+(50-50)^2/50=4$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 只算了一個偏離 10 的格子；b 忘了平方後不會為負；c 把差距直接加總；d 正確。

#### 選擇題 13 <a id="exam-ch12-mc-13"></a>

##### 題目

> Refer to Exhibit 12-1. The number of degrees of freedom associated with this problem is
>
> a. 150<br>
> b. 149<br>
> c. 2<br>
> d. 3

##### 詳解

> **回看投影片講義：** [估計參數時的通式](./course2-slides-handout.html#formula-ch12-df-estimated-gof)


- **辨認題型：** 三類適合度自由度。
- **選方法：** 使用一般多項適合度的 $k-1$。
- **檢查假設：** 沒有從資料估計額外分配參數。
- **計算／推理：** $df=3-1=2$，可對照[估計參數時的通式](./course2-slides-handout.html#formula-ch12-df-estimated-gof)，此處 $m=0$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 是樣本數；b 是 $n-1$；c 正確；d 忘了總數約束要減 1。

#### 選擇題 14 <a id="exam-ch12-mc-14"></a>

##### 題目

> Refer to Exhibit 12-1. The p-value is
>
> a. larger than 0.1<br>
> b. less than 0.1<br>
> c. less than 0.05<br>
> d. larger than 0.9

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** $\chi^2=4,df=2$ 的右尾 p 值。
- **選方法：** 使用[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)。
- **檢查假設：** 期望次數條件通過。
- **計算／推理：** $p=P(\chi^2_2\ge4)=0.1353>0.1$。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b、c 把 p 值估得太小；d 又過大，$0.1353$ 並非超過 $0.9$。

#### 選擇題 15 <a id="exam-ch12-mc-15"></a>

##### 題目

> Refer to Exhibit 12-1. The conclusion of the test at 95% confidence is that the
>
> a. distribution is uniform<br>
> b. distribution is not uniform<br>
> c. test is inconclusive<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** 在 $\alpha=0.05$ 下解讀適合度檢定。
- **選方法：** 比較 p 值與 $\alpha$。
- **檢查假設：** 隨機性需由抽樣設計支持；期望次數已通過。
- **計算／推理：** $p=0.1353>0.05$，依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)不能拒絕均勻分布。
- **解讀結論：** 題庫措辭下答案是 **a**；嚴格說法是「沒有足夠證據認定分布不均勻」，不是證明均勻。
- **選項檢討：** a 是題庫預期答案但語氣過強；b 與檢定結果相反；c 容易因「不能證明」而想選，但標準選項把不能拒絕寫成 a；d 不符題庫意圖。

#### 題組 12-2：選擇題 16–20 共用資料

> Last school year, the student body consisted of 30% freshmen, 24% sophomores, 26% juniors, and 20% seniors. A sample of 300 students from this year contained 83 freshmen, 68 sophomores, 85 juniors, and 64 seniors. Determine whether the classifications changed.

| Classification | Observed | Historical proportion | Expected |
|---|---:|---:|---:|
| Freshmen | 83 | 0.30 | 90 |
| Sophomores | 68 | 0.24 | 72 |
| Juniors | 85 | 0.26 | 78 |
| Seniors | 64 | 0.20 | 60 |

#### 選擇題 16 <a id="exam-ch12-mc-16"></a>

##### 題目

> Refer to Exhibit 12-2. The expected number of freshmen is
>
> a. 83<br>
> b. 90<br>
> c. 30<br>
> d. 10

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 指定歷史比例的適合度。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，使用 $E=np$。
- **檢查假設：** $n=300,p=0.30$。
- **計算／推理：** 依[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)，$E=300(0.30)=90$。
- **解讀結論：** 答案是 **b**。
- **選項檢討：** a 是觀察值；b 正確；c 是百分比數字誤當人數；d 是無關的除法結果。

#### 選擇題 17 <a id="exam-ch12-mc-17"></a>

##### 題目

> Refer to Exhibit 12-2. The expected frequency of seniors is
>
> a. 60<br>
> b. 20%<br>
> c. 68<br>
> d. 64

##### 詳解

> **回看投影片講義：** [期望次數公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** senior 類別的期望次數。
- **選方法：** 適合度 $E=np$。
- **檢查假設：** $n=300,p=0.20$。
- **計算／推理：** $E=300(0.20)=60$，引用[期望次數公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b 是機率不是次數；c 是 sophomores 的觀察值；d 是 seniors 的觀察值。

#### 選擇題 18 <a id="exam-ch12-mc-18"></a>

##### 題目

> Refer to Exhibit 12-2. The calculated value for the test statistic equals
>
> a. 0.5444<br>
> b. 300<br>
> c. 1.6615<br>
> d. 6.6615

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 四類適合度統計量。
- **選方法：** 使用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望值 90、72、78、60 均至少 5。
- **計算／推理：** 四格貢獻加總為 $\chi^2=1.661538\approx1.6615$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 只反映部分貢獻；b 是樣本數；c 正確；d 多加了 5。

#### 選擇題 19 <a id="exam-ch12-mc-19"></a>

##### 題目

> Refer to Exhibit 12-2. The p-value is
>
> a. less than .005<br>
> b. between .025 and 0.05<br>
> c. between .05 and 0.1<br>
> d. greater than 0.1

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** $\chi^2=1.6615,df=3$ 的右尾 p 值。
- **選方法：** 使用[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)。
- **檢查假設：** 四類、無估計參數，所以 $df=4-1=3$。
- **計算／推理：** $p=0.6455>0.1$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a、b、c 都把小統計量誤判成小 p 值；d 正確。

#### 選擇題 20 <a id="exam-ch12-mc-20"></a>

##### 題目

> Refer to Exhibit 12-2. At 95% confidence, the null hypothesis
>
> a. should not be rejected<br>
> b. should be rejected<br>
> c. was designed wrong<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** $\alpha=0.05$ 的決策題。
- **選方法：** 比較 $p=0.6455$ 與 $0.05$。
- **檢查假設：** 適合度條件通過。
- **計算／推理：** 依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)，$p>\alpha$，不能拒絕 $H_0$。
- **解讀結論：** 答案是 **a**；沒有足夠證據認定今年比例改變。
- **選項檢討：** a 正確；b 顛倒決策；c 無統計依據；d 錯，因 a 可明確作答。

#### 題組 12-3：選擇題 21–25 共用資料

> One group received medication and another received sugar pills. Determine whether the medication was effective in curing the common cold.

| Treatment | Patients Cured | Patients Not Cured | Total |
|---|---:|---:|---:|
| Received medication | 70 | 10 | 80 |
| Received sugar pills | 20 | 50 | 70 |
| Total | 90 | 60 | 150 |

#### 選擇題 21 <a id="exam-ch12-mc-21"></a>

##### 題目

> Refer to Exhibit 12-3. The expected frequency of those who received medication and were cured is
>
> a. 70<br>
> b. 150<br>
> c. 28<br>
> d. 48

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** $2\times2$ 獨立性檢定的期望格數。
- **選方法：** 兩個類別變數，依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)選獨立性。
- **檢查假設：** 觀察單位應獨立；所有期望次數將至少為 5。
- **計算／推理：** 依[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)，$E=80(90)/150=48$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 是觀察值；b 是總樣本；c 是 sugar-pill/not-cured 的期望值；d 正確。

#### 選擇題 22 <a id="exam-ch12-mc-22"></a>

##### 題目

> Refer to Exhibit 12-3. The test statistic is
>
> a. 10.08<br>
> b. 54.02<br>
> c. 1.96<br>
> d. 1.645

##### 詳解

> **回看投影片講義：** [卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)


- **辨認題型：** $2\times2$ 獨立性卡方值。
- **選方法：** 使用[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)。
- **檢查假設：** 期望表為 $[[48,32],[42,28]]$，皆至少 5。
- **計算／推理：** 四格貢獻加總 $\chi^2=54.0179\approx54.02$。
- **解讀結論：** 答案是 **b**。
- **選項檢討：** a 是漏算格子的結果；b 正確；c、d 是常見 $z$ 臨界值，不是卡方統計量。

#### 選擇題 23 <a id="exam-ch12-mc-23"></a>

##### 題目

> Refer to Exhibit 12-3. The number of degrees of freedom associated with this problem is
>
> a. 4<br>
> b. 149<br>
> c. 1<br>
> d. 3

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** $2\times2$ 列聯表自由度。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** $r=c=2$。
- **計算／推理：** $df=(2-1)(2-1)=1$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 是格子數；b 是 $n-1$；c 正確；d 是格子數減 1 的誤套。

#### 選擇題 24 <a id="exam-ch12-mc-24"></a>

##### 題目

> Refer to Exhibit 12-3. The hypothesis is to be tested at the 5% level of significance. The critical value from the table equals
>
> a. 3.84<br>
> b. 7.81<br>
> c. 5.99<br>
> d. 9.34

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** $df=1,\alpha=0.05$ 的卡方臨界值。
- **選方法：** 使用右尾臨界值。
- **檢查假設：** 自由度已由列聯表算得 1。
- **計算／推理：** $\chi^2_{0.05,1}=3.841\approx3.84$，依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b 是 $df=3$；c 是 $df=2$；d 不對應本題自由度。

#### 選擇題 25 <a id="exam-ch12-mc-25"></a>

##### 題目

> Refer to Exhibit 12-3. The p-value is
>
> a. less than .005<br>
> b. between .005 and .01<br>
> c. between .01 and .025<br>
> d. between .025 and .05

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** $\chi^2=54.02,df=1$ 的右尾 p 值。
- **選方法：** 使用[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)。
- **檢查假設：** 卡方近似條件通過。
- **計算／推理：** 精確 p 值約 $1.99\times10^{-13}<0.005$。
- **解讀結論：** 答案是 **a**；治療與痊癒結果有關聯，但因果解讀仍取決於是否隨機分派。
- **選項檢討：** a 正確；b、c、d 都遠高估 p 值。

#### 題組 12-4：選擇題 26–31 共用資料

> In the past, 35% of students were in Business, 35% in Liberal Arts, and 30% in Education. In a sample of 300, the observed counts were 90, 120, and 90. Determine whether the proportions changed.

#### 選擇題 26 <a id="exam-ch12-mc-26"></a>

##### 題目

> Refer to Exhibit 12-4. This problem is an example of a
>
> a. normally distributed variable<br>
> b. test for independence<br>
> c. Poisson distributed variable<br>
> d. multinomial population

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 一個樣本的三類結果對歷史比例。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，是多項適合度。
- **檢查假設：** 每人只屬一個 college，類別互斥完整。
- **計算／推理：** 資料符合[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)的結構。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 需要連續數值；b 需要兩個類別變數；c 需要事件次數模型；d 正確。

#### 選擇題 27 <a id="exam-ch12-mc-27"></a>

##### 題目

> Refer to Exhibit 12-4. The expected frequency for the Business College is
>
> a. 0.3<br>
> b. 0.35<br>
> c. 90<br>
> d. 105

##### 詳解

> **回看投影片講義：** [期望次數公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 指定比例下的期望次數。
- **選方法：** 使用 $E=np$。
- **檢查假設：** Business 的歷史比例是 0.35，不是觀察比例 0.30。
- **計算／推理：** $E=300(0.35)=105$，引用[期望次數公式](./course2-slides-handout.html#formula-ch12-expected-multinomial)。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 是樣本比例；b 是歷史機率；c 是觀察次數；d 正確。

#### 選擇題 28 <a id="exam-ch12-mc-28"></a>

##### 題目

> Refer to Exhibit 12-4. The calculated value for the test statistic equals
>
> a. 0.01<br>
> b. 0.75<br>
> c. 4.29<br>
> d. 4.38

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 三類適合度卡方值。
- **選方法：** 使用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望次數為 105、105、90，皆至少 5。
- **計算／推理：** $\chi^2=225/105+225/105+0/90=4.2857\approx4.29$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a、b 漏算主要貢獻；c 正確；d 是錯誤四捨五入或算術。

#### 選擇題 29 <a id="exam-ch12-mc-29"></a>

##### 題目

> Refer to Exhibit 12-4. The hypothesis is to be tested at the 5% level of significance. The critical value from the table equals
>
> a. 1.645<br>
> b. 1.96<br>
> c. 5.991<br>
> d. 7.815

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** 三類適合度的臨界值。
- **選方法：** $df=3-1=2$，查右尾卡方。
- **檢查假設：** 沒有估計額外分配參數。
- **計算／推理：** $\chi^2_{0.05,2}=5.991$，引用[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a、b 是 $z$ 臨界值；c 正確；d 是 $df=3$ 的卡方臨界值。

#### 選擇題 30 <a id="exam-ch12-mc-30"></a>

##### 題目

> Refer to Exhibit 12-4. The p-value is
>
> a. greater than 0.1<br>
> b. between 0.05 and 0.1<br>
> c. between 0.025 and 0.05<br>
> d. between 0.01 and .025

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** $\chi^2=4.2857,df=2$ 的 p 值。
- **選方法：** 使用[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)。
- **檢查假設：** 期望次數條件通過。
- **計算／推理：** $p=0.1173>0.1$。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b、c、d 都把 p 值估得太小。

#### 選擇題 31 <a id="exam-ch12-mc-31"></a>

##### 題目

> Refer to Exhibit 12-4. The conclusion of the test is that the
>
> a. proportions have changed significantly<br>
> b. proportions have not changed significantly<br>
> c. test is inconclusive<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** $\alpha=0.05$ 的適合度結論。
- **選方法：** 比較 $p=0.1173$ 與 $0.05$。
- **檢查假設：** 適合度條件通過。
- **計算／推理：** $p>\alpha$，不能拒絕歷史比例，依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)。
- **解讀結論：** 答案是 **b**；更精確地說，沒有足夠證據認定比例改變。
- **選項檢討：** a 顛倒決策；b 是題庫預期且可改寫成較嚴謹語句；c 不是標準結論；d 錯。

#### 題組 12-5：選擇題 32–35 共用資料

> The table gives beverage preferences for random samples of teens and adults. Test for independence between age and drink preference.

| Beverage | Teens | Adults | Total |
|---|---:|---:|---:|
| Coffee | 50 | 200 | 250 |
| Tea | 100 | 150 | 250 |
| Soft Drink | 200 | 200 | 400 |
| Other | 50 | 50 | 100 |
| Total | 400 | 600 | 1,000 |

#### 選擇題 32 <a id="exam-ch12-mc-32"></a>

##### 題目

> Refer to Exhibit 12-5. With a .05 level of significance, the critical value for the test is
>
> a. 1.645<br>
> b. 7.815<br>
> c. 14.067<br>
> d. 15.507

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** $4\times2$ 獨立性檢定臨界值。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，兩類別變數選獨立性。
- **檢查假設：** $df=(4-1)(2-1)=3$。
- **計算／推理：** $\chi^2_{0.05,3}=7.815$，引用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **解讀結論：** 答案是 **b**。
- **選項檢討：** a 是 $z$ 臨界值；b 正確；c 是 $df=7$；d 不對應本題設定。

#### 選擇題 33 <a id="exam-ch12-mc-33"></a>

##### 題目

> Refer to Exhibit 12-5. The expected number of adults who prefer coffee is
>
> a. 0.25<br>
> b. 0.33<br>
> c. 150<br>
> d. 200

##### 詳解

> **回看投影片講義：** [列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)


- **辨認題型：** 列聯表單格期望次數。
- **選方法：** 使用列總數乘欄總數除以總數。
- **檢查假設：** coffee 列總數 250，adults 欄總數 600，總數 1,000。
- **計算／推理：** 依[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)，$E=250(600)/1000=150$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 是 coffee 邊際比例；b 不是正確比例；c 正確；d 是觀察次數。

#### 選擇題 34 <a id="exam-ch12-mc-34"></a>

##### 題目

> Refer to Exhibit 12-5. The test statistic for this test of independence is
>
> a. 0<br>
> b. 8.4<br>
> c. 62.5<br>
> d. 82.5

##### 詳解

> **回看投影片講義：** [卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)


- **辨認題型：** $4\times2$ 獨立性卡方值。
- **選方法：** 使用[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)。
- **檢查假設：** 期望表為 $[[100,150],[100,150],[160,240],[40,60]]$，均至少 5。
- **計算／推理：** 八格貢獻加總 $\chi^2=62.5$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 假設觀察等於期望；b 是其他題常見值；c 正確；d 多加 20。

#### 選擇題 35 <a id="exam-ch12-mc-35"></a>

##### 題目

> Refer to Exhibit 12-5. The p-value is
>
> a. between .1 and .05<br>
> b. between .05 and .025<br>
> c. between .025 and .01<br>
> d. less than 0.005

##### 詳解

> **回看投影片講義：** [右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)


- **辨認題型：** $\chi^2=62.5,df=3$ 的 p 值。
- **選方法：** 使用[右尾 p 值](./course2-slides-handout.html#formula-ch12-p-value-right-tail)。
- **檢查假設：** 期望次數通過。
- **計算／推理：** $p\approx1.72\times10^{-13}<0.005$。
- **解讀結論：** 答案是 **d**；年齡群與飲料偏好有關聯。
- **選項檢討：** a、b、c 都遠高估 p 值；d 正確。

#### 題組 12-6：選擇題 36–39 共用資料

> A car-wash owner tests whether arrivals follow a Poisson distribution. In 150 ten-minute intervals the observed frequencies for 0 through 9 cars are 3, 10, 15, 23, 30, 24, 20, 13, 8, and 4.

加權平均為 $\hat\lambda=\sum xf_x/150=4.4$。依題庫的分組方式，將 0–1 合併，並將 9 與未列出的 10 以上右尾合併成 9+，得到 $\chi^2\approx2.89$。

#### 選擇題 36 <a id="exam-ch12-mc-36"></a>

##### 題目

> Refer to Exhibit 12-6. The expected frequency of exactly 3 cars arriving in a 10-minute interval is
>
> a. 0.1533<br>
> b. 0.1743<br>
> c. 23<br>
> d. 26.145

##### 詳解

> **回看投影片講義：** [Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)


- **辨認題型：** Poisson 單一類別的期望次數。
- **選方法：** 題目指定事件次數模型，使用 Poisson 適合度。
- **檢查假設：** 以樣本估計 $\lambda=4.4$；固定區間與獨立事件需由情境支持。
- **計算／推理：** 依[Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)，$P(X=3)=0.174305$，故 $E=150(0.174305)=26.1458$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 是錯誤機率；b 是正確機率但題目問 frequency；c 是觀察次數；d 正確。

#### 選擇題 37 <a id="exam-ch12-mc-37"></a>

##### 題目

> Refer to Exhibit 12-6. The calculated value for the test statistic equals
>
> a. -0.18<br>
> b. 0.18<br>
> c. 1.72<br>
> d. 2.89

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** Poisson 適合度卡方值。
- **選方法：** 先算 Poisson 期望值，再用卡方統計量。
- **檢查假設：** 為滿足期望次數至少 5，合併 0–1 與 9+；右尾不能丟掉。
- **計算／推理：** 依[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)，合併後加總為 $\chi^2=2.8913$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 不可能，卡方不為負；b、c 是漏格或錯誤合併；d 正確。

#### 選擇題 38 <a id="exam-ch12-mc-38"></a>

##### 題目

> Refer to Exhibit 12-6. The p-value is
>
> a. greater than 0.1<br>
> b. between 0.05 and 0.1<br>
> c. between .025 and .05<br>
> d. between .01 and .025

##### 詳解

> **回看投影片講義：** [估計參數自由度](./course2-slides-handout.html#formula-ch12-df-estimated-gof)


- **辨認題型：** Poisson 適合度 p 值區間。
- **選方法：** 使用右尾卡方；估計一個 $\lambda$ 要扣自由度。
- **檢查假設：** 合併後 9 類，$df=9-1-1=7$。
- **計算／推理：** 依[估計參數自由度](./course2-slides-handout.html#formula-ch12-df-estimated-gof)，$P(\chi^2_7\ge2.8913)>0.1$。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b、c、d 都把很小的卡方值解成過小 p 值。

#### 選擇題 39 <a id="exam-ch12-mc-39"></a>

##### 題目

> Refer to Exhibit 12-6. At 95% confidence, the conclusion of the test is that the
>
> a. arrival of cars follows a Poisson distribution<br>
> b. arrival of cars does not follow a Poisson distribution<br>
> c. test is inconclusive<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** Poisson 適合度結論。
- **選方法：** 比較 p 值與 $0.05$。
- **檢查假設：** 分組後期望次數足夠。
- **計算／推理：** p 值大於 0.1，所以不能拒絕 Poisson 模型，依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)。
- **解讀結論：** 題庫預期答案是 **a**；嚴格說法是資料沒有提供反對 Poisson 模型的充分證據。
- **選項檢討：** a 符合題庫意圖但不能解成證明；b 與結果相反；c 不是標準決策用語；d 不符題意。

#### 題組 12-7：選擇題 40–44 共用資料

> Test whether the following 30 observations follow a normal distribution. The sample mean is 11.83 and the sample standard deviation is 4.53.
>
> 2, 3, 5, 5, 7, 8, 8, 9, 9, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 14, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19.

本題用 6 個等機率區間，每區期望次數 $30/6=5$。以 $\bar x=11.83,s=4.53$ 算出的五個切點約為 7.448、9.879、11.830、13.781、16.212；觀察次數為 5、4、3、7、6、5。

#### 選擇題 40 <a id="exam-ch12-mc-40"></a>

##### 題目

> Refer to Exhibit 12-7. The number of intervals or categories used to test the hypothesis is
>
> a. 4<br>
> b. 5<br>
> c. 6<br>
> d. 10

##### 詳解

> **回看投影片講義：** [常態區間期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)


- **辨認題型：** 常態適合度的分組數。
- **選方法：** 用等機率區間並維持每區期望至少 5。
- **檢查假設：** $n=30$，所以最多可用 $30/5=6$ 個等機率區間。
- **計算／推理：** 依[常態區間期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)，選 $k=6$。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a、b 可行但不是題庫採用分組；c 正確；d 會讓每區期望只有 3，違反門檻。

#### 選擇題 41 <a id="exam-ch12-mc-41"></a>

##### 題目

> Refer to Exhibit 12-7. The expected frequency in the 3rd interval is
>
> a. 3<br>
> b. 4<br>
> c. 5<br>
> d. 10

##### 詳解

> **回看投影片講義：** [常態期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)


- **辨認題型：** 等機率區間的期望次數。
- **選方法：** 六區各占 $1/6$。
- **檢查假設：** $n=30,k=6$。
- **計算／推理：** $E=30(1/6)=5$，引用[常態期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 是第三區觀察次數；b 是第二區觀察次數；c 正確；d 是錯誤分組。

#### 選擇題 42 <a id="exam-ch12-mc-42"></a>

##### 題目

> Refer to Exhibit 12-7. The calculated value for the test statistic equals
>
> a. 0<br>
> b. 1.67<br>
> c. 2<br>
> d. 6

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 常態適合度卡方值。
- **選方法：** 以六區觀察次數和共同期望值 5 計算。
- **檢查假設：** 各區期望正好為 5。
- **計算／推理：** $\chi^2=\sum(O-5)^2/5=2.0$，引用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **解讀結論：** 答案是 **c**。
- **選項檢討：** a 假設完全吻合；b 是錯誤加總；c 正確；d 把區間數當統計量。

#### 選擇題 43 <a id="exam-ch12-mc-43"></a>

##### 題目

> Refer to Exhibit 12-7. The p-value is
>
> a. greater than 0.1<br>
> b. between .05 and 0.1<br>
> c. between .025 and .05<br>
> d. between .01 and .025

##### 詳解

> **回看投影片講義：** [常態適合度自由度](./course2-slides-handout.html#formula-ch12-df-normal)


- **辨認題型：** 常態適合度右尾 p 值。
- **選方法：** 平均數與標準差由樣本估計，使用 $df=k-3$。
- **檢查假設：** $df=6-3=3$。
- **計算／推理：** 依[常態適合度自由度](./course2-slides-handout.html#formula-ch12-df-normal)，$p=P(\chi^2_3\ge2)=0.5724>0.1$。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b、c、d 都將小統計量誤解成小 p 值。

#### 選擇題 44 <a id="exam-ch12-mc-44"></a>

##### 題目

> Refer to Exhibit 12-7. At 95% confidence, the conclusion of the test is that the
>
> a. data follows a normal distribution<br>
> b. data does not follow a normal distribution<br>
> c. test is inconclusive<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)


- **辨認題型：** 常態適合度結論。
- **選方法：** 依[右尾拒絕規則](./course2-slides-handout.html#formula-ch12-rejection-right-tail)，比較 $p=0.5724$ 與 $0.05$。
- **檢查假設：** 六區期望皆為 5。
- **計算／推理：** $p>\alpha$，不能拒絕常態模型。
- **解讀結論：** 題庫預期答案是 **a**；嚴格說法是沒有足夠證據認定資料不服從常態。
- **選項檢討：** a 符合題庫意圖但語氣過強；b 顛倒決策；c 不是標準結論；d 不符題意。

#### 題組 12-8：選擇題 45–47 共用資料

> In a sample of 300, support for a new tax proposal was recorded as Democrats 100, Republicans 120, and Independents 80. Determine whether opinions are uniformly distributed across the three groups.

#### 選擇題 45 <a id="exam-ch12-mc-45"></a>

##### 題目

> Refer to Exhibit 12-8. The expected frequency for each group is
>
> a. 0.333<br>
> b. 0.50<br>
> c. 50<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 三類均勻適合度的期望次數。
- **選方法：** 一個類別變數對均勻基準。
- **檢查假設：** $n=300,k=3$。
- **計算／推理：** 依[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)，$E=300/3=100$。
- **解讀結論：** 選項沒有 100，所以答案是 **d**。
- **選項檢討：** a 是機率不是次數；b 不是三類均勻機率；c 少了一半；d 正確。

#### 選擇題 46 <a id="exam-ch12-mc-46"></a>

##### 題目

> Refer to Exhibit 12-8. The calculated value for the test statistic equals
>
> a. 300<br>
> b. 4<br>
> c. 0<br>
> d. 8

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 三類均勻適合度統計量。
- **選方法：** 使用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 三個期望次數均為 100。
- **計算／推理：** $\chi^2=0^2/100+20^2/100+(-20)^2/100=8$。
- **解讀結論：** 答案是 **d**。
- **選項檢討：** a 是樣本數；b 只算一個偏離格；c 假設完全一致；d 正確。

#### 選擇題 47 <a id="exam-ch12-mc-47"></a>

##### 題目

> Refer to Exhibit 12-8. The number of degrees of freedom associated with this problem is
>
> a. 2<br>
> b. 3<br>
> c. 300<br>
> d. 299

##### 詳解

> **回看投影片講義：** [估計參數自由度通式](./course2-slides-handout.html#formula-ch12-df-estimated-gof)


- **辨認題型：** 三類適合度自由度。
- **選方法：** 沒有估計額外參數，使用 $k-1$。
- **檢查假設：** $k=3$。
- **計算／推理：** $df=3-1=2$，可由[估計參數自由度通式](./course2-slides-handout.html#formula-ch12-df-estimated-gof)令 $m=0$ 得到。
- **解讀結論：** 答案是 **a**。
- **選項檢討：** a 正確；b 忘了減 1；c 是樣本數；d 是 $n-1$ 的誤套。

### 計算題｜第 1–35 題

#### 計算題 1 <a id="exam-ch12-problem-1"></a>

##### 題目

> ```text
> In the last presidential election, before the candidates started their major campaigns, the percentages of
>     registered voters who favored the various candidates were as follows.
>
>                                                                                    Percentages
>                                         Republicans                                   34%
>                                         Democrats                                     43%
>                                         Independents                                  23%
>      After the major campaigns began, a random sample of 400 voters showed that 172 favored the
>      Republican candidate; 164 were in favor of the Democratic candidate; and 64 favored the Independent
>      candidate. We are interested in determining whether the proportion of voters who favored the
>      various candidates had changed.
>      a.   Compute the test statistic.
>      b.   Using the p-value approach, test to see if the proportions have changed.
>      c.   Using the critical value approach, test the hypotheses.
> ```

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)、[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)、[卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 一個樣本的三類偏好和既有比例比較，是多項適合度。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)，用[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)與[卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 題目說是 random sample；三類互斥完整；期望次數 136、172、92 均至少 5。
- **代入計算：** $H_0:(p_R,p_D,p_I)=(0.34,0.43,0.23)$。$\chi^2=18.4232$，$df=2$，$p=0.0000999$；在 $\alpha=0.05$ 下臨界值為 5.991。
- **解讀結論：** $p<0.05$ 且 $18.4232>5.991$，拒絕 $H_0$；競選後的偏好比例已有顯著改變。

#### 計算題 2 <a id="exam-ch12-problem-2"></a>

##### 題目

> ```text
> During the first few weeks of the new television season, the evening news audience proportions were
>     recorded as ABC- 31%, CBS- 34%, and NBC- 35%. A sample of 600 homes yielded the following
>     viewing audience data.
>                                     Number of
>                                      Homes
>                                          150
>            ABC
>
>            CBS                           200
>
>            NBC                           250
>
>      We want to determine whether or not there has been a significant change in the number of viewing
>      audience of the three networks.
>
>      a.   State the null and alternative hypotheses to be tested.
>      b.   Compute the expected frequencies.
>      c.   Compute the test statistic.
>      d.   The null hypothesis is to be tested at 95% confidence. Determine the critical value for this
>           test. What do you conclude?
>      e.   Determine the p-value and perform the test.
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 三類收視分布對既有比例的適合度。
- **選方法：** 一個類別變數加外部基準，選[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 住戶應隨機且彼此獨立；期望次數 186、204、210 均至少 5。
- **代入計算：** $H_0:(p_A,p_C,p_N)=(0.31,0.34,0.35)$；$H_a$ 為至少一個比例不同。$\chi^2=14.6652$，$df=2$，$p=0.0006539$；$\chi^2_{0.05,2}=5.991$。
- **解讀結論：** 兩種判斷都拒絕 $H_0$；三家晚間新聞的收視比例已有顯著變化。

#### 計算題 3 <a id="exam-ch12-problem-3"></a>

##### 題目

> ```text
> The results of a recent study regarding smoking and three types of illness are shown in the following
>     table.
>
>                             Illness                          Non-Smokers               Smokers              Totals
>                             Emphysema                            20                      60                   80
>                             Heart problem                        70                      80                  150
>                             Cancer                                   30                   40                  70
>                             Totals                                  120                   180                300
>
>
>    We are interested in determining whether or not illness is independent of smoking.
>
>    a.    State the null and alternative hypotheses to be tested.
>    b.    Show the contingency table of the expected frequencies.
>    c.    Compute the test statistic.
>    d.    The null hypothesis is to be tested at 95% confidence. Determine the critical value for this
>          test. What do you conclude?
>    e.    Determine the p-value and perform the test.
> ```

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 同一批人的 illness 與 smoking 是兩個類別變數。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)選獨立性檢定。
- **檢查假設：** 觀察值應獨立；期望表 $[[32,48],[60,90],[28,42]]$ 全部至少 5。
- **代入計算：** $H_0:$ illness 與 smoking 獨立。由[列聯表公式](./course2-slides-handout.html#formula-ch12-expected-cell)及[卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)，$\chi^2=10.5159$，$df=2$，$p=0.005206$，臨界值 5.991。
- **解讀結論：** 拒絕 $H_0$；疾病類型與吸菸狀態有關聯，但觀察資料本身不證明吸菸造成特定疾病。

#### 計算題 4 <a id="exam-ch12-problem-4"></a>

##### 題目

> ```text
> Among 1,000 managers with degrees in business administration, the following data have been
>    accumulated as to their fields of concentration.
>
>                             Major                  Top Management                   Middle Management                  TOTAL
>
>                      Management                             280                                220                       500
>                      Marketing                              120                                80                        200
>                      Accounting                             150                                150                       300
>                      TOTAL                                  550                                450                       1000
>
>    We want to determine if the position in management is independent of field (major) of concentration.
>
>    a.    Compute the test statistic.
>    b.    Using the p-value approach at 90% confidence, test to determine if management position is
>          independent of major.
>    c.    Using the critical value approach, test the hypotheses. Let α = 0.10.
> ```

##### 詳解

> **回看投影片講義：** [獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** 職位與主修的 $3\times2$ 獨立性檢定。
- **選方法：** 使用[獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** 期望表為 $[[275,225],[110,90],[165,135]]$，均至少 5；個人應彼此獨立。
- **代入計算：** $\chi^2=5.2525$，$df=2$，$p=0.07235$；$\alpha=0.10$ 臨界值 $\chi^2_{0.10,2}=4.605$。
- **解讀結論：** $p<0.10$ 且統計量超過臨界值，拒絕獨立性；管理職位與主修有關聯。

#### 計算題 5 <a id="exam-ch12-problem-5"></a>

##### 題目

> ```text
> From a poll of 800 television viewers, the following data have been accumulated as to their levels of
>    education and their preference of television stations. We are interested in determining if the selection
>    of a TV station is independent of the level of education.
>
>                                                           Educational Level
>                                        High School             Bachelor                    Graduate                     TOTAL
>
>    Public Broadcasting                        50                     150                        80                         280
>    Commercial Stations                       150                     250                       120                         520
>
>    TOTAL                           200              400            200                  800
>    a. State the null and the alternative hypotheses.
>    b. Show the contingency table of the expected frequencies.
>    c. Compute the test statistic.
>    d. The null hypothesis is to be tested at 95% confidence. Determine the critical value for this
>       test.
>    e. Determine the p-value and perform the test.
> ```

##### 詳解

> **回看投影片講義：** [列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)


- **辨認題型：** 教育程度與電視台偏好的獨立性。
- **選方法：** 兩個類別變數，使用[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)。
- **檢查假設：** 期望表 $[[70,140,70],[130,260,130]]$ 均至少 5；抽樣單位應獨立。
- **代入計算：** $H_0:$ 兩變數獨立。$\chi^2=12.0879$，$df=2$，$p=0.002372$；臨界值 5.991。
- **解讀結論：** 拒絕 $H_0$；電視台選擇與教育程度有關聯。

#### 計算題 6 <a id="exam-ch12-problem-6"></a>

##### 題目

> ```text
> Before the start of the Winter Olympics, it was expected that the percentages of medals awarded to the
>    top contenders to be as follows.
>
>
>
>
>                                              Percentages
>    United States                                25%
>    Germany                                      22%
>    Norway                                       18%
>    Austria                                      14%
>    Russia                                       11%
>    France                                       10%
>
>    Midway through the Olympics, of the 120 medals awarded, the following distribution was observed.
>
>                                         Number of Medals
>    United States                              33
>    Germany                                    36
>    Norway                                     18
>    Austria                                    15
>    Russia                                     12
>    France                                      6
>
>    We want to test to see if there is a significant difference between the expected and actual awards given.
>    a. Compute the test statistic.
>    b. Using the p-value approach, test to see if there is a significant difference between the expected
>       and the actual values. Let α = .05.
>    c. At 95% confidence, test for a significant difference using the critical value approach.
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 六類獎牌次數對指定比例的適合度。
- **選方法：** 使用[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望次數為 30、26.4、21.6、16.8、13.2、12，均至少 5。
- **代入計算：** $\chi^2=7.6929$，$df=5$，$p=0.1740$；$\chi^2_{0.05,5}=11.070$。
- **解讀結論：** 不能拒絕 $H_0$；目前資料不足以認定實際獎牌分配偏離原先比例。

#### 計算題 7 <a id="exam-ch12-problem-7"></a>

##### 題目

> ```text
> A medical journal reported the following frequencies of deaths due to cardiac arrest for each day of the
>    week:
>
>           Cardiac Death by Day of the Week
>    Day                                  f
>    Monday                              40
>    Tuesday                             17
>    Wednesday                           16
>    Thursday                            29
>    Friday                              15
>    Saturday                            20
>    Sunday                              17
>
>    We want to determine whether the number of deaths is uniform over the week.
>    a. Compute the test statistic.
>    b. Using the p-value approach at 95% confidence, test for the uniformity of death over the week.
>    c. Using the critical value approach, perform the test for uniformity.
> ```

##### 詳解

> **回看投影片講義：** [多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 七類均勻適合度。
- **選方法：** 一個 weekday 類別對均勻比例，使用[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)。
- **檢查假設：** 總數 154，所以每日期望 22；均至少 5。每天事件是否可視為獨立仍需研究設計支持。
- **代入計算：** $\chi^2=23.2727$，$df=6$，$p=0.0007101$；臨界值 $\chi^2_{0.05,6}=12.592$。
- **解讀結論：** 拒絕均勻分布；心臟驟停死亡次數在星期各日並不均勻。

#### 計算題 8 <a id="exam-ch12-problem-8"></a>

##### 題目

> ```text
> Before the presidential debates, it was expected that the percentages of registered voters in favor of
>    various candidates would be as follows.
>
>                                                              Percentages
>    Democrats                                                    48%
>    Republicans                                                  38%
>    Independent                                                   4%
>    Undecided                                                    10%
>
>
>
>
>
>      After the presidential debates, a random sample of 1200 voters showed that 540 favored the
>      Democratic candidate; 480 were in favor of the Republican candidate; 40 were in favor of the
>      Independent candidate, and 140 were undecided. We want to see if the proportion of voters has
>      changed.
>      a. Compute the test statistic.
>      b. Use the p-value approach to test the hypotheses. Let α = .05.
>      c. Using the critical value approach, test the hypotheses. Let α = .05.
> ```

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 四類政治偏好對辯論前比例的適合度。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)選多項適合度。
- **檢查假設：** 期望次數 576、456、48、120 均至少 5；題目指出 random sample。
- **代入計算：** $\chi^2=8.1798$，$df=3$，$p=0.04244$；臨界值 7.815。
- **解讀結論：** $p<0.05$ 且統計量超過臨界值，拒絕 $H_0$；辯論後偏好比例有顯著改變。

#### 計算題 9 <a id="exam-ch12-problem-9"></a>

##### 題目

> ```text
> Last school year, in the school of Business Administration, 30% were Accounting majors, 24%
>     Management majors, 26% Marketing majors, and 20% Economics majors. A sample of 300 students
>     taken from this year's students of the school showed the following number of students in each major:
>
>      Accounting                                    83
>      Management                                    68
>      Marketing                                     85
>      Economics                                     64
>      Total                                         300
>
>      We want to see if there has been a significant change in the number of students in each major.
>      a. Compute the test statistic.
>      b. Has there been any significant change in the number of students in each major between the last
>         school year and this school year. Use the p-value approach and let α = .05.
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 四類主修分布對歷史比例的適合度。
- **選方法：** 使用[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望值 90、72、78、60 均至少 5。
- **代入計算：** $\chi^2=1.6615$，$df=3$，$p=0.6455$。
- **解讀結論：** 不能拒絕 $H_0$；沒有足夠證據認定今年主修比例與去年不同。

#### 計算題 10 <a id="exam-ch12-problem-10"></a>

##### 題目

> ```text
> The personnel department of a large corporation reported sixty resignations during the last year. The
>     following table groups these resignations according to the season in which they occurred:
>
>                                                          Number of
>      Season                                             Resignations
>      Winter                                                  10
>      Spring                                                  22
>      Summer                                                  19
>      Fall                                                    9
>
>      Test to see if the number of resignations is uniform over the four seasons.
>      Let α = 0.05.
> ```

##### 詳解

> **回看投影片講義：** [多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 四季均勻適合度。
- **選方法：** 使用[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)。
- **檢查假設：** 每季期望 $60/4=15$，均至少 5。
- **代入計算：** $\chi^2=8.4$，$df=3$，$p=0.03843$；臨界值 7.815。
- **解讀結論：** 拒絕均勻分布；離職次數隨季節有顯著差異，但不代表季節本身造成離職。

#### 計算題 11 <a id="exam-ch12-problem-11"></a>

##### 題目

> ```text
> In 2002, forty percent of the students at a major university were Business majors, 35% were
>     Engineering majors and the rest of the students were majoring in other fields. In a sample of 600
>     students from the same university taken in 2003, two hundred were Business majors, 220 were
>     Engineering majors and the remaining students in the sample were majoring in other fields. At 95%
>     confidence, test to see if there has been a significant change in the proportions between 2002 and 2003.
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 三類主修對歷史比例的適合度。
- **選方法：** 使用[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望次數 240、210、150 均至少 5。
- **代入計算：** $\chi^2=13.1429$，$df=2$，$p=0.001400$；臨界值 5.991。
- **解讀結論：** 拒絕 $H_0$；2002 與 2003 的主修比例有顯著改變。

#### 計算題 12 <a id="exam-ch12-problem-12"></a>

##### 題目

> ```text
> Before the rush began for Christmas shopping, a department store had noted that the percentage of its
>     customers who use the store's credit card, the percentage of those who use a major credit card, and the
>     percentage of those who pay cash are the same. During the Christmas rush in a sample of 150 shoppers,
>     46 used the store's credit card; 43 used a major credit card; and 61 paid cash. With α = 0.05, test to see
>     if the methods of payment have changed during the Christmas rush.
> ```

##### 詳解

> **回看投影片講義：** [多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)


- **辨認題型：** 三類均勻適合度。
- **選方法：** 使用[多項期望次數](./course2-slides-handout.html#formula-ch12-expected-multinomial)。
- **檢查假設：** 每類期望 50，均至少 5；每位顧客只計一次。
- **代入計算：** $\chi^2=3.72$，$df=2$，$p=0.1557$；臨界值 5.991。
- **解讀結論：** 不能拒絕 $H_0$；資料不足以認定聖誕購物潮改變付款方式比例。

#### 計算題 13 <a id="exam-ch12-problem-13"></a>

##### 題目

> ```text
> A major automobile manufacturer claimed that the frequencies of repairs on all five models of its cars
>     are the same. A sample of 200 repair services showed the following frequencies on the various makes
>     of cars.
>
>            Model of Car                        Frequency
>                A                                   32
>                B                                   45
>                C                                   43
>                D                                   34
>                E                                   46
>
>      At α = 0.05, test the manufacturer's claim.
> ```

##### 詳解

> **回看投影片講義：** [多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 五類均勻適合度。
- **選方法：** 使用[多項卡方統計量](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 每款期望 $200/5=40$，均至少 5。
- **代入計算：** $\chi^2=4.25$，$df=4$，$p=0.3732$；臨界值 9.488。
- **解讀結論：** 不能拒絕等頻率主張；這不等於證明五款維修率完全相同。

#### 計算題 14 <a id="exam-ch12-problem-14"></a>

##### 題目

> ```text
> A lottery is conducted that involves the random selection of numbers from 0 to 4. To make sure that
>     the lottery is fair, a sample of 250 was taken. The following results were obtained:
>
>                 Value                          Frequency
>                   0                                40
>                   1                                45
>                   2                                55
>                   3                                60
>                   4                                50
>
>      a.   State the null and alternative hypotheses to be tested.
>      b.   Compute the test statistic.
>      c.   The null hypothesis is to be tested at the 5% level of significance. Determine the critical value
>           from the table.
>      d.   What do you conclude about the fairness of this lottery?
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 五個號碼應均勻出現的適合度。
- **選方法：** $H_0:p_0=\cdots=p_4=0.20$，使用[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 每次抽號應獨立；每類期望 50。
- **代入計算：** $\chi^2=5.0$，$df=4$，$p=0.2873$；臨界值 9.488。
- **解讀結論：** 不能拒絕公平均勻模型；樣本沒有顯示彩票不公平，但也不能證明機制一定公平。

#### 計算題 15 <a id="exam-ch12-problem-15"></a>

##### 題目

> ```text
> The makers of Compute-All know that in the past, 40% of their sales were from people under 30 years
>     old, 45% of their sales were from people who are between 30 and 50 years old, and 15% of their sales
>     were from people who are over 50 years old. A sample of 300 customers was taken to see if the market
>     shares had changed. In the sample, 100 of the people were under 30 years old, 150 people were
>     between 30 and 50 years old, and 50 people were over 50 years old.
>     a. State the null and alternative hypotheses to be tested.
>     b. Compute the test statistic.
>     c. The null hypothesis is to be tested at the 1% level of significance. Determine the critical value
>          from the table.
>     d. What do you conclude?
> ```

##### 詳解

> **回看投影片講義：** [多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)


- **辨認題型：** 三類年齡分布對歷史比例的適合度。
- **選方法：** 使用[多項適合度](./course2-slides-handout.html#formula-ch12-chi-square-gof)。
- **檢查假設：** 期望次數 120、135、45 均至少 5。
- **代入計算：** $\chi^2=5.5556$，$df=2$，$p=0.06218$；在 $\alpha=0.01$ 下臨界值 9.210。
- **解讀結論：** 不能拒絕 $H_0$；在嚴格的 1% 顯著水準下，沒有足夠證據認定市場年齡結構改變。

#### 計算題 16 <a id="exam-ch12-problem-16"></a>

##### 題目

> ```text
> The following table shows the results of recent study regarding gender of individuals and their selected
>     field of study.
>
>      Field of study              Male           Female           TOTAL
>      Medicine                     80              40              120
>      Business                     60              20               80
>      Engineering                 160              40              200
>      TOTAL                       300             100              400
>
>
>
>
>      We want to determine if the selected field of study is independent of gender.
>      a. Compute the test statistic.
>      b. Using the p-value approach at 90% confidence, test to see if the field of study is independent of
>         gender.
>      c. Using the critical method approach at 90% confidence, test for the independence of major and
>         gender.
> ```

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** field 與 gender 的 $3\times2$ 獨立性。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)使用獨立性檢定。
- **檢查假設：** 期望表 $[[90,30],[60,20],[150,50]]$ 均至少 5；個人應彼此獨立。
- **代入計算：** 依[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)，$\chi^2=7.1111$，$df=2$，$p=0.02857$；$\alpha=0.10$ 臨界值 4.605。
- **解讀結論：** 拒絕獨立性；在 10% 顯著水準下，性別與選擇的領域有關聯。

#### 計算題 17 <a id="exam-ch12-problem-17"></a>

##### 題目

> ```text
> Shown below is 3 x 2 contingency table with observed values from a sample of 1,500. At 95%
>     confidence, test for independence of the row and column factors.
>
>                                                             Column Factor
>      Row Factor                                     X                                 Y                              Total
>      A                                             450                               300                              750
>      B                                             300                               300                              600
>      C                                             100                                50                              150
>      Total                                         850                               650                             1,500
> ```

##### 詳解

> **回看投影片講義：** [列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)


- **辨認題型：** $3\times2$ 列聯表獨立性。
- **選方法：** 使用[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)。
- **檢查假設：** 期望表 $[[425,325],[340,260],[85,65]]$ 均至少 5。
- **代入計算：** $\chi^2=20.3620$，$df=2$，$p=0.0000379$；臨界值 5.991。
- **解讀結論：** 拒絕 $H_0$；row factor 與 column factor 不獨立。

#### 計算題 18 <a id="exam-ch12-problem-18"></a>

##### 題目

> ```text
> Shown below is 2 x 3 contingency table with observed values from a sample of 500. At 95%
>     confidence using the critical value approach, test for independence of the row and column factors.
>
>                                                  Column Factor
>      Row Factor                             X                           Y                           Z
>      A                                      40                          50                         110
>      B                                      60                         100                         140
> ```

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** $2\times3$ 獨立性檢定。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)與卡方臨界值法。
- **檢查假設：** 期望表 $[[40,60,100],[60,90,150]]$ 均至少 5。
- **代入計算：** $\chi^2=4.4444$，$df=2$；$\chi^2_{0.05,2}=5.991$。獨立驗算的 p 值為 0.1084。
- **解讀結論：** $4.4444<5.991$，不能拒絕獨立性；資料不足以認定 row 與 column factors 有關聯。

#### 計算題 19 <a id="exam-ch12-problem-19"></a>

##### 題目

> ```text
> A sample of 150 individuals (males and females) was surveyed, and the individuals were asked to
>     indicate their yearly incomes. Their incomes were categorized as follows.
>
>      Category 1                                  $20,000         up to        $40,000
>      Category 2                                  $40,000         up to        $60,000
>      Category 3                                  $60,000         up to        $80,000
>
>      The results of the survey are shown below.
>
>               Income Category                                Male                            Female
>                  Category 1                                   10                               30
>                  Category 2                                   35                               15
>                  Category 3                                   15                               45
>
>      We want to determine if yearly income is independent of gender.
>      a. Compute the test statistic.
>      b. Using the p-value approach, test to determine if yearly income is independent of gender.
> ```

##### 詳解

> **回看投影片講義：** [方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)


- **辨認題型：** 收入類別與性別的 $3\times2$ 獨立性。
- **選方法：** 依[方法判斷準則](./course2-slides-handout.html#compare-ch12-method-selection)使用獨立性檢定。
- **檢查假設：** 期望表 $[[16,24],[20,30],[24,36]]$ 均至少 5。
- **代入計算：** $\chi^2=28.125$，$df=2$，$p=7.81\times10^{-7}$，引用[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)。
- **解讀結論：** 拒絕獨立性；收入類別與性別有顯著關聯。

#### 計算題 20 <a id="exam-ch12-problem-20"></a>

##### 題目

> ```text
> A group of 2000 individuals from 3 different cities were asked whether they owned a foreign or a
>     domestic car. The following contingency table shows the results of the survey.
>
>                                                                    CITY
>      Type of Car                                       Detroit               Atlanta               Denver                  Total
>      Domestic                                           80                    200                    520                    800
>      Foreign                                            120                   600                    480                   1200
>      Total                                              200                   800                   1000                   2000
>
>
>
>      At α = 0.05 using the p-value approach, test to determine if the type of car purchased is independent of
>      the city in which the purchasers live.
> ```

##### 詳解

> **回看投影片講義：** [列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)


- **辨認題型：** 車種與城市的 $2\times3$ 獨立性。
- **選方法：** 使用[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)。
- **檢查假設：** 期望表 $[[80,320,400],[120,480,600]]$ 均至少 5。
- **代入計算：** $\chi^2=135.0$，$df=2$，$p=4.84\times10^{-30}$。
- **解讀結論：** 拒絕獨立性；購買車種與城市有極強的統計關聯，但不能由此單獨推論城市造成購車選擇。

#### 計算題 21 <a id="exam-ch12-problem-21"></a>

##### 題目

> ```text
> Dr. Sherri Brock's diet pills are supposed to cause significant weight loss. The following table shows
>     the results of a recent study where some individuals took the diet pills and some did not.
>
>                                                          Diet Pills                 No Diet Pills                      Total
>      No Weight Loss                                         80                           20                            100
>      Weight Loss                                           100                          100                            200
>      Total                                                 180                          120                            300
>
>      We want to see if losing weight is independent of taking the diet pills.
>      a. Compute the test statistic.
>      b. Using the p-value approach at 95% confidence, test to determine if weight loss is independent
>         on taking the pill.
>      c. Use the critical method approach and test for independence.
> ```

##### 詳解

> **回看投影片講義：** [獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** 是否服藥與是否減重的 $2\times2$ 獨立性。
- **選方法：** 使用[獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** 期望表 $[[60,40],[120,80]]$ 均至少 5；是否能說因果取決於有無隨機分派與盲法。
- **代入計算：** $\chi^2=25.0$，$df=1$，$p=5.73\times10^{-7}$；臨界值 3.841。
- **解讀結論：** 拒絕獨立性；服藥狀態與減重結果有關聯。觀察比例顯示服藥組減重率較低，與題幹宣稱方向相反。

#### 計算題 22 <a id="exam-ch12-problem-22"></a>

##### 題目

> ```text
> Five hundred randomly selected automobile owners were questioned on the main reason they had
>     purchased their current automobile. The results are given below.
>
>                                    Styling                 Engineering                Fuel Economy                      Total
>      Male                            70                       130                          150                           350
>      Female                          30                        20                          100                           150
>      Total                           100                      150                          250                           500
>
>      a.   State the null and alternative hypotheses for a contingency table test.
>      b.   State the decision rule for the critical value approach. Let α = .01.
>      c.   Calculate the χ² test statistic.
>      d.   Give your conclusion for this test.
> ```

##### 詳解

> **回看投影片講義：** [卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)


- **辨認題型：** 性別與購車主因的 $2\times3$ 獨立性。
- **選方法：** $H_0:$ sex 與 reason 獨立；使用[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)。
- **檢查假設：** 期望表 $[[70,105,175],[30,45,75]]$ 均至少 5；題目說 random sample。
- **代入計算：** $\chi^2=31.7460$，$df=2$，$p=1.28\times10^{-7}$；$\alpha=0.01$ 的臨界值 9.210，規則為 $\chi^2\ge9.210$ 時拒絕。
- **解讀結論：** 拒絕獨立性；性別與主要購車理由有關聯。

#### 計算題 23 <a id="exam-ch12-problem-23"></a>

##### 題目

> ```text
> A group of 500 individuals were asked to cast their votes regarding a particular issue of the Equal
>     Rights Amendment. The following contingency table shows the results of the votes:
>
>             Sex                  Favor                 Undecided                     Oppose                     TOTAL
>
>           Female                  180                        80                         40                         300
>            Male                   150                        20                         30                         200
>           TOTAL                   330                       100                         70                         500
>
>      At α = .05 using the p-value approach, test to determine if the votes cast were independent of the sex
>      of the individuals.
> ```

##### 詳解

> **回看投影片講義：** [列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)


- **辨認題型：** 投票態度與性別的獨立性。
- **選方法：** 使用[列聯表期望公式](./course2-slides-handout.html#formula-ch12-expected-cell)。
- **檢查假設：** 期望表 $[[198,60,42],[132,40,28]]$ 均至少 5。
- **代入計算：** $\chi^2=20.9957$，$df=2$，$p=0.0000276$。
- **解讀結論：** 拒絕獨立性；投票態度與性別有顯著關聯。

#### 計算題 24 <a id="exam-ch12-problem-24"></a>

##### 題目

> ```text
> Two hundred fifty managers with degrees in business administration indicated their fields of
>     concentration as shown below.
>
>            Major                     Top Management                     Middle Management                     TOTAL
>      Management                            65                                   60                             125
>      Marketing                             30                                   20                              50
>      Accounting                            25                                   50                              75
>      TOTAL                                120                                  130                             250
>
>
>      At α = .01 using the p-value approach, test to determine if the position in management is independent
>      of the major of concentration.
> ```

##### 詳解

> **回看投影片講義：** [獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** position 與 major 的 $3\times2$ 獨立性。
- **選方法：** 使用[獨立性檢定](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** 期望表 $[[60,65],[24,26],[36,39]]$ 均至少 5。
- **代入計算：** $\chi^2=10.1496$，$df=2$，$p=0.006252$；1% 臨界值 9.210。
- **解讀結論：** $p<0.01$，拒絕獨立性；職位與主修有顯著關聯。

#### 計算題 25 <a id="exam-ch12-problem-25"></a>

##### 題目

> ```text
> From a poll of 800 television viewers, the following data have been accumulated as to their levels of
>     education and their preference of television stations.
>
>                                                      Level of Education
>
>                                                High School               Bachelor              Graduate               TOTAL
>      Public Broadcasting                           110                     190                   100                   400
>      Commercial Stations                            80                     220                   100                   400
>      TOTAL                                         190                     410                   200                   800
>
>      Test at α = .05 to determine if the selection of a TV station is dependent upon the level of education.
>      Use the p-value approach.
> ```

##### 詳解

> **回看投影片講義：** [卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)


- **辨認題型：** station 與 education 的獨立性。
- **選方法：** 使用[卡方格子統計量](./course2-slides-handout.html#formula-ch12-chi-square-cell)。
- **檢查假設：** 期望表 $[[95,205,100],[95,205,100]]$ 均至少 5。
- **代入計算：** $\chi^2=6.9320$，$df=2$，$p=0.03124$。
- **解讀結論：** $p<0.05$，拒絕獨立性；電視台選擇依教育程度而有差異。

#### 計算題 26 <a id="exam-ch12-problem-26"></a>

##### 題目

> ```text
> The data below represents the fields of specialization for a randomly selected sample of undergraduate
>     students. We want to determine whether there is a significant difference in the fields of specialization
>     between regions of the country.
>
>                                    Northeast             Midwest                South                 West                 Total
>      Business                         54                   65                    28                    93                  240
>      Engineering                      15                   24                     8                    33                   80
>      Liberal Arts                     65                   84                    33                    98                  280
>      Fine Arts                        13                   15                     7                    25                   60
>      Health Sciences                   3                   12                     4                    21                   40
>                                      150                  200                    80                   270                  700
>
>      a.   Determine the critical value of the chi-square χ² for this test of independence.
>      b.   Calculate the value of the test statistic.
>      c.   What is the conclusion for this test? Let α = .05.
> ```

##### 詳解

> **回看投影片講義：** [獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)


- **辨認題型：** field 與 region 的 $5\times4$ 獨立性。
- **選方法：** 使用[獨立性自由度](./course2-slides-handout.html#formula-ch12-df-independence)。
- **檢查假設：** $df=(5-1)(4-1)=12$；最小期望次數為 $40(80)/700=4.571<5$，所以本課的逐格門檻未完全通過，卡方近似需保留警語或合併合理類別。
- **代入計算：** 若照原題未合併計算，$\chi^2=8.6738$，$p=0.7305$；臨界值 $\chi^2_{0.05,12}=21.026$。
- **解讀結論：** 數值上不能拒絕獨立性，但因一格期望值低於 5，這個近似結論需審慎。原題未提醒此條件，是題庫的一項方法限制。

#### 計算題 27 <a id="exam-ch12-problem-27"></a>

##### 題目

> ```text
> A department store believes that telephone calls come into the switchboard at 10-minute intervals,
>     according to a Poisson distribution. Before ordering new equipment, the store wishes to determine
>     whether the Poisson model is a valid assumption. Records on the number of calls received were kept
>     for a random selection of 150 ten-minute intervals. The results are shown below.
>
>           Number of Calls                      Frequency
>                0                                    5
>                1                                   18
>                2                                   24
>                3                                   30
>                4                                   32
>                5                                   13
>                6                                   20
>                7                                    8
>                                                   150
>
>
>
>
>      a.    What is the average number of calls during these ten-minute intervals?
>      b.    Generate the expected number of calls using a Poisson probability table.
>      c.    Give the null and alternative hypotheses for the appropriate test.
>      d.    Determine the number of degrees of freedom for this test.
>      e.    Calculate the value of the test statistic.
>      f.    Determine the p-value and state whether or not the Poisson model is a valid model for the
>            phone calls?
> ```

##### 詳解

> **回看投影片講義：** [Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)


- **辨認題型：** 固定十分鐘內的電話次數，題目指定 Poisson 適合度。
- **選方法：** 使用[Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)，再用卡方適合度。
- **檢查假設：** 區間應可比較、事件率大致穩定、事件近似獨立。為使 $E\ge5$，合併 0–1，並把 7 與所有未列出的 8+ 合成 7+。
- **代入計算：** $\hat\lambda=525/150=3.5$。合併後 $(O,E)$ 為 0–1 $(23,20.383)$、2 $(24,27.744)$、3 $(30,32.368)$、4 $(32,28.322)$、5 $(13,19.825)$、6 $(20,11.565)$、7+ $(8,9.793)$。$\chi^2=10.3228$，$k=7$，依[估計參數自由度](./course2-slides-handout.html#formula-ch12-df-estimated-gof)得 $df=7-2=5$，$p=0.06659$。
- **解讀結論：** 在 $\alpha=0.05$ 下不能拒絕 Poisson 模型；資料沒有顯示它不適用，但不能說已證明模型正確。

#### 計算題 28 <a id="exam-ch12-problem-28"></a>

##### 題目

> ```text
> It is believed that sales of books at a local bookstore follow a Poisson distribution. Below you are
>     given information on the number of books sold during a sample of 15-minute intervals.
>
>           Number of Books                       Frequency
>                 0                                    2
>                 1                                    3
>                 2                                   12
>                 3                                   16
>                 4                                   19
>                 5                                   20
>                 6                                   18
>                 7                                   16
>                 8                                    9
>                 9                                    5
>                                                    120
>
>      a.    What is the average number of books sold during a 15-minute period?
>      b.    Using the Poisson distribution, find the probability associated with the number of books sold.
>      c.    Generate the expected number of books sold using a Poisson probability table.
>      d.    State the null and alternative hypotheses.
>      e.    Calculate the test statistic.
>      f.    Use the p-value approach to test the hypotheses. What is your conclusion? Let α = .05.
> ```

##### 詳解

> **回看投影片講義：** [Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)


- **辨認題型：** 固定 15 分鐘內的銷售本數，Poisson 適合度。
- **選方法：** 用[Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)建立每類期望值。
- **檢查假設：** 合併 0–1，並把 9 與未列出的 10+ 合成 9+；所有合併後期望值至少 5。
- **代入計算：** $\hat\lambda=588/120=4.9$。0–1、2、3、4、5、6、7、8、9+ 的期望值依序為 5.272、10.728、17.522、21.464、21.035、17.178、12.025、7.365、7.411。$\chi^2=3.1317$，$k=9$，$df=7$，$p=0.8726$。
- **解讀結論：** 不能拒絕 Poisson 模型；觀察分布與 $\lambda=4.9$ 的 Poisson 分布相容。

#### 計算題 29 <a id="exam-ch12-problem-29"></a>

##### 題目

> ```text
> The number of emergency calls per day at a hospital over a period of 120 days is shown below.
>
>                      Number of                                                   Observed
>                   Emergency Calls (x)                                          Frequency (f)
>                           0                                                         9
>                           1                                                         12
>                           2                                                         30
>                           3                                                         27
>                           4                                                         22
>                           5                                                         13
>                           6                                                         7
>                         Total                                                      120
>
>      Use α = 0.05 and the p-value approach to see if the above data have a Poisson distribution.
> ```

##### 詳解

> **回看投影片講義：** [Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)


- **辨認題型：** 每日緊急電話次數的 Poisson 適合度。
- **選方法：** 使用[Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)。
- **檢查假設：** 把 6 與未列出的 7+ 合成 6+，其餘期望值均至少 5。
- **代入計算：** $\hat\lambda=348/120=2.9$。0、1、2、3、4、5、6+ 的期望值為 6.603、19.148、27.765、26.839、19.458、11.286、8.901。$\chi^2=4.7179$，$df=7-2=5$，$p=0.4513$。
- **解讀結論：** $p>0.05$，不能拒絕 Poisson 模型。

#### 計算題 30 <a id="exam-ch12-problem-30"></a>

##### 題目

> ```text
> An insurance company has gathered the following information regarding the number of accidents
>     reported per day over a period of 100 days.
>
>
>
>
>                Accidents Per Day                          Number of Days (f )
>                        0                                          5
>                        1                                         18
>                        2                                         25
>                        3                                         24
>                        4                                         20
>                        5                                          8
>
>      Using the critical value approach test to see if the above data have a Poisson distribution. Let α = 0.05.
> ```

##### 詳解

> **回看投影片講義：** [Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)


- **辨認題型：** 每日事故件數的 Poisson 適合度。
- **選方法：** 使用[Poisson 機率](./course2-slides-handout.html#formula-ch12-poisson-probability)與臨界值法。
- **檢查假設：** 把 5 與未列出的 6+ 合成 5+；合併後每類期望至少 5。
- **代入計算：** $\hat\lambda=260/100=2.6$。0、1、2、3、4、5+ 的期望值為 7.427、19.311、25.104、21.757、14.142、12.258。$\chi^2=5.0192$，$k=6$，$df=4$；臨界值 $\chi^2_{0.05,4}=9.488$。獨立驗算 p 值為 0.2853。
- **解讀結論：** $5.0192<9.488$，不能拒絕 Poisson 模型。

#### 計算題 31 <a id="exam-ch12-problem-31"></a>

##### 題目

> ```text
> A professor believes that the final examination scores in statistics are normally distributed. A sample
>     of 40 final scores has been taken. You are given the sample below. The mean of the scores is 83.1, and
>     the standard deviation is 10.43.
>
>           56     63        65         68        72         72        73        75        77         78
>           78     79        80         80        80         80        80        80        81         81
>           82     84        84         86        86         87        88        90        90         92
>           92     93        93         94        95         96        97        98       100        100
>
>      a.    State the null and alternative hypotheses.
>      b.    Compute the test statistic for the goodness of fit test.
>      c.    At 99% confidence using the p-value approach, test the hypotheses. What do you conclude
>            about the distribution of final examination scores?
> ```

##### 詳解

> **回看投影片講義：** [常態切點](./course2-slides-handout.html#formula-ch12-normal-cutoff)、[常態自由度](./course2-slides-handout.html#formula-ch12-df-normal)


- **辨認題型：** 連續分數是否符合常態的適合度。
- **選方法：** 用 8 個等機率區間，使每區期望值為 $40/8=5$；引用[常態切點](./course2-slides-handout.html#formula-ch12-normal-cutoff)。
- **檢查假設：** 題目提供樣本，仍需假設觀察值獨立；每區期望正好為 5。原始資料重算為 $\bar x=83.125,s=10.380$，和題目給的 83.1、10.43 略有四捨五入差異，以下依題目指定值作答。
- **代入計算：** 七個切點約為 71.102、76.065、79.777、83.100、86.423、90.135、95.098；觀察次數為 4、4、4、9、4、4、6、5。$\chi^2=4.4$，依[常態自由度](./course2-slides-handout.html#formula-ch12-df-normal)得 $df=8-3=5$，$p=0.4934$。
- **解讀結論：** 在 $\alpha=0.01$ 下不能拒絕常態模型；資料沒有顯示期末考分數不服從常態。

#### 計算題 32 <a id="exam-ch12-problem-32"></a>

##### 題目

> ```text
> A manager believes that the shelf life of apple juice is normally distributed. A sample of 30 containers
>     of juice was taken and the shelf life was recorded. You are given the results below. The average shelf
>     life in the sample was 23.07 days with a standard deviation of 4.29 days.
>
>           15         17        19         20         20         20        21          21         21        21
>           21         21        21         22         22         22        22          22         22        22
>           24         24        25         25         27         29        30          31         32        33
>
>      a.    State the null and alternative hypotheses.
>      b.    Compute the test statistic for the goodness of fit test.
>      c.    At 95% confidence using the p-value approach, test the hypotheses. What do you conclude
>            about the distribution?
> ```

##### 詳解

> **回看投影片講義：** [常態期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)


- **辨認題型：** 保存天數的常態適合度。
- **選方法：** 用 6 個等機率區間，每區期望 5，引用[常態期望次數](./course2-slides-handout.html#formula-ch12-normal-expected)。
- **檢查假設：** 樣本應獨立；題目給的 23.07、4.29 與原始資料重算的 23.0667、4.2906 一致至題目精度。
- **代入計算：** 切點約為 18.920、21.222、23.070、24.918、27.220；觀察次數為 2、11、7、2、3、5。$\chi^2=12.4$，$df=6-3=3$，$p=0.006131$。
- **解讀結論：** $p<0.05$，拒絕常態模型；保存期限資料顯示明顯偏離常態。

#### 計算題 33 <a id="exam-ch12-problem-33"></a>

##### 題目

> ```text
> The following data show the grades of a sample of 40 students who have taken statistics.
>
>      98         64        96         69
>      45         94        58         59
>      63         49        88         83
>      85         87        68         77
>      56         63        86         89
>      84         73        52         63
>      64         80        69         68
>      79         73        78         79
>      72         82        78         88
>      83         76        66         76
>
>
>
>      Use α = 0.1 and conduct a goodness of fit test to determine if the sample comes from a population that
>      has a normal distribution. Use the critical value approach.
> ```

##### 詳解

> **回看投影片講義：** [樣本平均數](./course2-slides-handout.html#formula-ch12-sample-mean)、[樣本標準差](./course2-slides-handout.html#formula-ch12-sample-standard-deviation)


- **辨認題型：** 40 筆成績的常態適合度。
- **選方法：** 先由資料估計 $\bar x,s$，再切成 8 個等機率區間。
- **檢查假設：** 觀察值應獨立；每區期望 5。
- **代入計算：** [樣本平均數](./course2-slides-handout.html#formula-ch12-sample-mean)與[樣本標準差](./course2-slides-handout.html#formula-ch12-sample-standard-deviation)為 $\bar x=74.0,s=12.8921$。切點約 59.170、65.304、69.892、74.000、78.108、82.696、88.830；觀察次數 6、5、5、3、5、4、8、4。$\chi^2=3.2$，$df=5$，10% 臨界值 9.236。
- **解讀結論：** $3.2<9.236$，不能拒絕常態模型；獨立驗算 p 值為 0.6692。

#### 計算題 34 <a id="exam-ch12-problem-34"></a>

##### 題目

> ```text
> Use α = 0.05 to determine if the following sample comes from a normal distribution. Use the critical
>     value approach.
>
>      105         260          314          400         520
>      300         306          115          200         208
>      418         110          410          312         360
>      310         314          418          316         412
>      516         480          490          504         518
>      280         270          516          419         520
>      420         438          511          708         300
>      420         519          702          690         518
>      510         700          650          670         612
>      460         600          680          692         600
> ```

##### 詳解

> **回看投影片講義：** [常態切點公式](./course2-slides-handout.html#formula-ch12-normal-cutoff)


- **辨認題型：** 50 筆連續資料的常態適合度。
- **選方法：** 題目未寫分組法；依同一題庫下一題的明示，採 10 個等機率區間，每區期望 5，並用[常態切點公式](./course2-slides-handout.html#formula-ch12-normal-cutoff)建立區間。
- **檢查假設：** 觀察值應獨立；每區期望正好 5。
- **代入計算：** $\bar x=440.42,s=163.2129$。九個切點約為 231.254、303.057、354.831、399.070、440.420、481.770、526.009、577.783、649.586；觀察次數為 5、5、6、1、9、2、11、0、3、8。$\chi^2=23.2$，$df=10-3=7$；5% 臨界值 14.067。
- **解讀結論：** $23.2>14.067$，拒絕常態模型；獨立驗算 p 值為 0.001573。

#### 計算題 35 <a id="exam-ch12-problem-35"></a>

##### 題目

> ```text
> We want to determine if the following sample comes from a normal distribution.
>
>                           105                260                 314                400                       520
>                           300                306                 115                200                       208
>                           418                110                 410                312                       360
>                           310                314                 418                316                       412
>                           516                480                 490                504                       518
>                           280                270                 516                419                       520
>                           420                438                 511                708                       300
>                           420                519                 702                690                       518
>                           510                700                 650                670                       612
>                           460                600                 680                692                       600
>
>      a.    Compute the mean and the standard deviation.
>      b.    Compute the test statistic. Hint: divide the distribution into 10 equal intervals.
>      c.    At 95% confidence using the critical value approach, test to determine if the sample comes
>            from a normal population.
>      d.    Compute the p-value.
> ```

##### 詳解

> **回看投影片講義：** [常態切點公式](./course2-slides-handout.html#formula-ch12-normal-cutoff)、[常態自由度](./course2-slides-handout.html#formula-ch12-df-normal)


- **辨認題型：** 與 Problem 34 相同資料的常態適合度，這題明示 10 個等機率區間。
- **選方法：** 使用[常態切點公式](./course2-slides-handout.html#formula-ch12-normal-cutoff)與[常態自由度](./course2-slides-handout.html#formula-ch12-df-normal)。
- **檢查假設：** 觀察值應獨立；每區期望 $50/10=5$。
- **代入計算：** $\bar x=440.42,s=163.2129$；切點與觀察次數同 Problem 34。$\chi^2=23.2$，$df=7$，臨界值 14.067，$p=0.001573$。
- **解讀結論：** 拒絕 $H_0$；此樣本提供充分證據認定母體分布不是常態。

<div class="page-break" style="page-break-after: always;"></div>

# 第 13 章：變異數分析｜考古題詳解

## 考古題詳解

本章收錄 115 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–29 題：基本觀念與公式

#### 選擇題 1 <a id="exam-ch13-mc-1"></a>

##### 題目

> In the analysis of variance procedure (ANOVA), "factor" refers to
> a. the dependent variable
> b. the independent variable
> c. different levels of a treatment
> d. the critical value of F

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)、[完全隨機設計](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 名詞辨認。**選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)先分清解釋變數與數值反應，再回看[完全隨機設計](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 概念題不需計算分配假設。**代入推理：** factor 是用來分組或安排處理的解釋變數。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 是 response/dependent variable，容易因「研究關心它」而誤選；b 正確；c 把方向顛倒，treatments 才是 factor 的 levels；d 是檢定門檻，不是變數。

#### 選擇題 2 <a id="exam-ch13-mc-2"></a>

##### 題目

> The ANOVA procedure is a statistical approach for determining whether or not
> a. the means of two samples are equal
> b. the means of two or more samples are equal
> c. the means of more than two samples are equal
> d. the means of two or more populations are equal

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 推論目標。**選方法：** 用[整體 F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** ANOVA 推論母體，不只描述已知樣本。**代入推理：** $H_0$ 寫的是母體平均數相等。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a、b、c 都把母體問題誤寫成樣本平均數；d 正確，而且兩組時 ANOVA 也可做，只是 t 檢定更直接。

#### 選擇題 3 <a id="exam-ch13-mc-3"></a>

##### 題目

> The variable of interest in an ANOVA procedure is called
> a. a partition
> b. a treatment
> c. either a partition or a treatment
> d. a factor

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** ANOVA 用語。**選方法：** 回到[整體 F 檢定](./course2-slides-handout.html#formula-anova-f)中的分組變數。**檢查假設：** 無計算假設。**代入推理：** 本題教材把欲研究其不同水準效果的 variable 稱 factor。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a 是變異分解動作；b 是 factor 的一個水準；c 因兩詞都不等同 variable 而錯；d 正確。

#### 選擇題 4 <a id="exam-ch13-mc-4"></a>

##### 題目

> In the ANOVA, treatment refers to
> a. experimental units
> b. different levels of a factor
> c. the dependent variable
> d. applying antibiotic to a wound

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)


- **辨認題型：** treatment 定義。**選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)辨認 factor 與 levels。**檢查假設：** 無。**代入推理：** 每個 factor level 就是一個 treatment。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 是接受處理的對象；b 正確；c 是 response；d 是日常語意，不是統計定義。

#### 選擇題 5 <a id="exam-ch13-mc-5"></a>

##### 題目

> In factorial designs, the response produced when the treatments of one factor interact with the treatments of another in influencing the response variable is known as
> a. main effect
> b. replication
> c. interaction
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [主效果 vs 交互作用](./course2-slides-handout.html#compare-ch13-method-selection)、[交互作用平方和](./course2-slides-handout.html#formula-anova-ssab)


- **辨認題型：** 二因子名詞。**選方法：** 用[主效果 vs 交互作用](./course2-slides-handout.html#compare-ch13-method-selection)及[交互作用平方和](./course2-slides-handout.html#formula-anova-ssab)。**檢查假設：** 題意已有兩因子。**代入推理：** 一因子的效果隨另一因子改變就是 interaction。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a 是平均掉另一因子的邊際效果；b 是每格觀察次數；c 正確；d 因 c 已正確而錯。

#### 選擇題 6 <a id="exam-ch13-mc-6"></a>

##### 題目

> An experimental design where the experimental units are randomly assigned to the treatments is known as
> a. factor block design
> b. random factor design
> c. completely randomized design
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [完全隨機 vs 集區](./course2-slides-handout.html#compare-ch13-method-selection)


- **辨認題型：** 設計辨認。**選方法：** 用[完全隨機 vs 集區](./course2-slides-handout.html#compare-ch13-method-selection)。**檢查假設：** 每個單位隨機分到一種處理。**代入推理：** 這正是 completely randomized design。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a、b 不是本章標準設計名稱；c 正確；d 因 c 已正確而錯。

#### 選擇題 7 <a id="exam-ch13-mc-7"></a>

##### 題目

> The number of times each experimental condition is observed in a factorial design is known as
> a. partition
> b. replication
> c. experimental condition
> d. factor

##### 詳解

> **回看投影片講義：** [二因子自由度](./course2-slides-handout.html#formula-anova-factorial-df)


- **辨認題型：** 名詞辨認。**選方法：** 連到[二因子自由度](./course2-slides-handout.html#formula-anova-factorial-df)，其中 $r$ 是每格重複數。**檢查假設：** 每個條件可重複觀察。**代入推理：** 次數稱 replication。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 是分解；b 正確；c 是條件本身；d 是變數，不是次數。

#### 選擇題 8 <a id="exam-ch13-mc-8"></a>

##### 題目

> In an analysis of variance problem involving 3 treatments and 10 observations per treatment, SSE = 399.6. The MSE for this situation is
> a. 133.2
> b. 13.32
> c. 14.8
> d. 30.0

##### 詳解

> **回看投影片講義：** [組內平均平方](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** MSE。**選方法：** 用[組內平均平方](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** $N=30,k=3$，誤差自由度 $27$。**代入計算：** $MSE=399.6/27=14.8$。**解讀結論：** 答案是 **c** ，代表組內變異估計。
- **逐項判讀：** a 誤除以 3；b 誤除以 30；c 正確；d 把總樣本數當答案。

#### 選擇題 9 <a id="exam-ch13-mc-9"></a>

##### 題目

> When an analysis of variance is performed on samples drawn from K populations, the mean square between treatments (MSTR) is
> a. $SSTR/n_T$
> b. $SSTR/(n_T-1)$
> c. $SSTR/K$
> d. $SSTR/(K-1)$

##### 詳解

> **回看投影片講義：** [處理平均平方](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR 公式。**選方法：** 用[處理平均平方](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** 處理自由度為 $K-1$。**代入推理：** $MSTR=SSTR/(K-1)$。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a、b 用總樣本自由度；c 少減 1；d 正確。

#### 選擇題 10 <a id="exam-ch13-mc-10"></a>

##### 題目

> In an analysis of variance where the total sample size for the experiment is $n_T$ and the number of populations is K, the mean square within treatments is
> a. $SSE/(n_T-K)$
> b. $SSTR/(n_T-K)$
> c. $SSE/(K-1)$
> d. $SSE/K$

##### 詳解

> **回看投影片講義：** [組內平均平方](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** MSE 公式。**選方法：** 用[組內平均平方](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** 誤差自由度是 $n_T-K$。**代入推理：** $MSE=SSE/(n_T-K)$。**解讀結論：** 答案是 **a** 。
- **逐項判讀：** a 正確；b 把 SSTR 放錯；c、d 用了處理數而非組內自由度。

#### 選擇題 11 <a id="exam-ch13-mc-11"></a>

##### 題目

> The F ratio in a completely randomized ANOVA is the ratio of
> a. MSTR/MSE
> b. MST/MSE
> c. MSE/MSTR
> d. MSE/MST

##### 詳解

> **回看投影片講義：** [ANOVA F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F 統計量。**選方法：** 用[ANOVA F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 分子是處理、分母是誤差。**代入推理：** $F=MSTR/MSE$。**解讀結論：** 答案是 **a** 。
- **逐項判讀：** a 正確；b、d 的 MST 不是此表標準列；c 把比值顛倒。

#### 選擇題 12 <a id="exam-ch13-mc-12"></a>

##### 題目

> The critical F value with 6 numerator and 60 denominator degrees of freedom at $\alpha=.05$ is
> a. 3.74
> b. 2.25
> c. 2.37
> d. 1.96

##### 詳解

> **回看投影片講義：** [右尾 F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F 臨界值。**選方法：** 依[右尾 F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 自由度順序是 $(6,60)$、右尾 $0.05$。**代入計算：** $F_{0.05;6,60}\approx2.25$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a、c 是別組自由度或尾面積的表值；b 正確；d 是常見常態臨界值，會因看到 95% 而誤選。

#### 選擇題 13 <a id="exam-ch13-mc-13"></a>

##### 題目

> An ANOVA procedure is applied to data obtained from 6 samples where each sample contains 20 observations. The degrees of freedom for the critical value of F are
> a. 6 numerator and 20 denominator
> b. 5 numerator and 20 denominator
> c. 5 numerator and 114 denominator
> d. 6 numerator and 20 denominator

##### 詳解

> **回看投影片講義：** [平方和與自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 自由度。**選方法：** 用[平方和與自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $K=6,N=120$。**代入計算：** $df_1=5,df_2=120-6=114$。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a、d 未各減掉相應限制；b 分母錯用單組樣本數；c 正確。

#### 選擇題 14 <a id="exam-ch13-mc-14"></a>

##### 題目

> The mean square is the sum of squares divided by
> a. the total number of observations
> b. its corresponding degrees of freedom
> c. its corresponding degrees of freedom minus one
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)、[MSE](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** mean square 定義。**選方法：** 比照[MSTR](./course2-slides-handout.html#formula-anova-between)與[MSE](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** 每個來源有自己的 df。**代入推理：** $MS=SS/df$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 忽略來源；b 正確；c 又多減一次；d 因 b 正確而錯。

#### 選擇題 15 <a id="exam-ch13-mc-15"></a>

##### 題目

> In an analysis of variance problem if SST = 120 and SSTR = 80, then SSE is
> a. 200
> b. 40
> c. 80
> d. 120

##### 詳解

> **回看投影片講義：** [$SST=SSTR+SSE$](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 平方和分解。**選方法：** 用[$SST=SSTR+SSE$](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 完全隨機單因子設計。**代入計算：** $SSE=120-80=40$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 誤相加；b 正確；c 重抄 SSTR；d 重抄 SST。

#### 選擇題 16 <a id="exam-ch13-mc-16"></a>

##### 題目

> The required condition for using an ANOVA procedure on data from several populations is that the
> a. selected samples are dependent on each other
> b. sampled populations are all uniform
> c. sampled populations have equal variances
> d. sampled populations have equal means

##### 詳解

> **回看投影片講義：** [ANOVA F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** ANOVA 假設。**選方法：** 回看[ANOVA F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 獨立、組內近似常態、共同變異數。**代入推理：** 選項中只有 equal variances 是所需條件。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a 應是獨立而非相依；b 不是標準假設；c 正確；d 是要檢定的虛無假設，不是使用前必須為真。

#### 選擇題 17 <a id="exam-ch13-mc-17"></a>

##### 題目

> An ANOVA procedure is used for data obtained from four sample groups each comprised of five observations. The degrees of freedom for the critical value of F are
> a. 3 and 20
> b. 3 and 16
> c. 4 and 17
> d. 3 and 19

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** F 自由度。**選方法：** 用[自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $K=4,N=20$。**代入計算：** $(df_1,df_2)=(3,16)$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 分母沒扣 K；b 正確；c 分子未減 1；d 把總 df 當分母。

#### 選擇題 18 <a id="exam-ch13-mc-18"></a>

##### 題目

> In ANOVA, which of the following is not affected by whether or not the population means are equal?
> a. $\bar{\bar{x}}$
> b. between-samples estimate of $\sigma^2$
> c. within-samples estimate of $\sigma^2$
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)、[MSE](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** 組間與組內變異。**選方法：** 比較[MSTR](./course2-slides-handout.html#formula-anova-between)與[MSE](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** 共同變異數模型。**代入推理：** 母體平均不同會拉大組間估計，組內 MSE 仍估計共同 $\sigma^2$。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a 的位置會隨各組平均改變；b 正是會被平均差拉大的估計；c 正確；d 因 c 正確而錯。

#### 選擇題 19 <a id="exam-ch13-mc-19"></a>

##### 題目

> A term that means the same as the term "variable" in an ANOVA procedure is
> a. factor
> b. treatment
> c. replication
> d. variance within

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)


- **辨認題型：** 名詞。**選方法：** 用[方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)。**檢查假設：** 無。**代入推理：** 教材將分組 variable 稱 factor。**解讀結論：** 答案是 **a** 。
- **逐項判讀：** a 正確；b 是 factor level；c 是重複次數；d 是誤差變異。

#### 選擇題 20 <a id="exam-ch13-mc-20"></a>

##### 題目

> In order to determine whether or not the means of two populations are equal,
> a. a t test must be performed
> b. an analysis of variance must be performed
> c. either a t test or an analysis of variance can be performed
> d. a chi-square test must be performed

##### 詳解

> **回看投影片講義：** [ANOVA vs 兩獨立樣本 t](./course2-slides-handout.html#compare-ch13-method-selection)


- **辨認題型：** 兩組平均數方法。**選方法：** 用[ANOVA vs 兩獨立樣本 t](./course2-slides-handout.html#compare-ch13-method-selection)。**檢查假設：** 同一套等變異單因子模型下，兩組 ANOVA 的 $F=t^2$。**代入推理：** 兩法皆可。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a、b 的「must」太強；c 正確；d 用於類別次數，不是數值平均數。

#### 選擇題 21 <a id="exam-ch13-mc-21"></a>

##### 題目

> The process of allocating the total sum of squares and degrees of freedom is called
> a. factoring
> b. blocking
> c. replicating
> d. partitioning

##### 詳解

> **回看投影片講義：** [平方和分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** ANOVA 名詞。**選方法：** 看[平方和分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 無。**代入推理：** 把總和分配到來源叫 partitioning。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a 是因子化的一般詞；b 是設計；c 是重複；d 正確。

#### 選擇題 22 <a id="exam-ch13-mc-22"></a>

##### 題目

> An experimental design that permits statistical conclusions about two or more factors is a
> a. randomized block design
> b. factorial design
> c. completely randomized design
> d. randomized design

##### 詳解

> **回看投影片講義：** [主效果 vs 交互作用](./course2-slides-handout.html#compare-ch13-method-selection)


- **辨認題型：** 設計選擇。**選方法：** 用[主效果 vs 交互作用](./course2-slides-handout.html#compare-ch13-method-selection)。**檢查假設：** 題目有兩個以上因子。**代入推理：** factorial design 同時安排因子組合。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 通常是一處理因子加控制用 block；b 正確；c 通常指單因子基本設計；d 太籠統。

#### 選擇題 23 <a id="exam-ch13-mc-23"></a>

##### 題目

> In a completely randomized design involving three treatments: sample sizes are 5, 10, 5 and sample means are 4, 8, 9. The overall mean is
> a. 7.00
> b. 6.67
> c. 7.25
> d. 4.89

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** 不等樣本數總平均。**選方法：** 依[MSTR](./course2-slides-handout.html#formula-anova-between)所需的加權 grand mean。**檢查假設：** 權重是各組 $n_j$。**代入計算：** $\bar{\bar{x}}=(5\times4+10\times8+5\times9)/20=7.25$。**解讀結論：** 答案是 **c** 。
- **逐項判讀：** a、b 是未正確依樣本數加權的直覺值；c 正確；d 無對應計算。

#### 選擇題 24 <a id="exam-ch13-mc-24"></a>

##### 題目

> In a completely randomized design involving four treatments: sample sizes are 50, 18, 15, 17 and sample means are 32, 38, 42, 48. The grand mean is
> a. 40.0
> b. 37.3
> c. 48.0
> d. 37.0

##### 詳解

> **回看投影片講義：** [處理平方和](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** 加權總平均。**選方法：** 用[處理平方和](./course2-slides-handout.html#formula-anova-between)前的 grand mean。**檢查假設：** $N=100$。**代入計算：** $(50\times32+18\times38+15\times42+17\times48)/100=37.3$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 是未加權平均；b 正確；c 是最大組平均；d 是過早取整。

#### 選擇題 25 <a id="exam-ch13-mc-25"></a>

##### 題目

> Five samples, each comprised of 20 observations, were taken from five populations. The numerator and denominator degrees of freedom for F are
> a. 5 and 20
> b. 4 and 20
> c. 4 and 99
> d. 4 and 95

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 自由度。**選方法：** 用[自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $K=5,N=100$。**代入計算：** $(4,100-5)=(4,95)$。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a、b 把單組 n 當分母；c 把總 df 當誤差 df；d 正確。

#### 選擇題 26 <a id="exam-ch13-mc-26"></a>

##### 題目

> The critical F value with 8 numerator and 29 denominator degrees of freedom at $\alpha=0.01$ is
> a. 2.28
> b. 3.20
> c. 3.33
> d. 3.64

##### 詳解

> **回看投影片講義：** [右尾 F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F 表。**選方法：** 用[右尾 F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $(df_1,df_2)=(8,29)$、右尾 0.01。**代入計算：** 表值約 $3.20$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 較像 0.05 的表值；b 正確；c、d 是其他自由度組合。

#### 選擇題 27 <a id="exam-ch13-mc-27"></a>

##### 題目

> Four samples, each comprised of 30 observations, were taken from four populations. The numerator and denominator degrees of freedom for F are
> a. 3 and 30
> b. 4 and 30
> c. 3 and 119
> d. 3 and 116

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 自由度。**選方法：** 用[自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $K=4,N=120$。**代入計算：** $(3,116)$。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a、b 誤用單組 n；c 是 total df；d 正確。

#### 選擇題 28 <a id="exam-ch13-mc-28"></a>

##### 題目

> Which of the following is not a required assumption for the analysis of variance?
> a. Each population has a normal probability distribution.
> b. The variance is the same for each population.
> c. At least 2 populations are under consideration.
> d. Populations have equal means.

##### 詳解

> **回看投影片講義：** [ANOVA F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 假設辨認。**選方法：** 連到[ANOVA F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 常態、等變異、獨立是模型條件。**代入推理：** 平均數相等是 $H_0$，不是資料使用 ANOVA 前必須成立。**解讀結論：** 答案是 **d** 。
- **逐項判讀：** a、b 是標準條件；c 是方法要有的比較結構；d 正確，否則檢定永遠無從發現差異。

#### 選擇題 29 <a id="exam-ch13-mc-29"></a>

##### 題目

> In an analysis of variance, one estimate of $\sigma^2$ is based upon the differences between the treatment means and the
> a. means of each sample
> b. overall sample mean
> c. sum of observations
> d. populations have equal means

##### 詳解

> **回看投影片講義：** [SSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** 組間變異。**選方法：** 用[SSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** 每組平均與 grand mean 比。**代入推理：** $SSTR=\sum n_j(\bar{x}_j-\bar{\bar{x}})^2$。**解讀結論：** 答案是 **b** 。
- **逐項判讀：** a 會變成平均數彼此互比；b 正確；c 尺度不對；d 不是可代入的量。

### 選擇題｜第 30–34 題：題組 13-1

#### 題組 13-1：選擇題 30–34 共用資料

> $SSTR=6,750$, $SSE=8,000$, $n_T=20$
> $H_0:\mu_1=\mu_2=\mu_3=\mu_4$
> $H_a$: at least one mean is different.

#### 選擇題 30 <a id="exam-ch13-mc-30"></a>

##### 題目

> The mean square between treatments (MSTR) equals: a. 400; b. 500; c. 1,687.5; d. 2,250.

##### 詳解

> **回看投影片講義：** [MSTR 公式](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR。**選方法：** [MSTR 公式](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** $K=4,df_1=3$。**代入計算：** $6750/3=2250$。**解讀結論：** **d** 。
- **逐項判讀：** a 是錯誤平均；b 是本題 MSE；c 誤除以 4；d 正確。

#### 選擇題 31 <a id="exam-ch13-mc-31"></a>

##### 題目

> The mean square within treatments (MSE) equals: a. 400; b. 500; c. 1,687.5; d. 2,250.

##### 詳解

> **回看投影片講義：** [MSE 公式](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** MSE。**選方法：** [MSE 公式](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** $df_2=20-4=16$。**代入計算：** $8000/16=500$。**解讀結論：** **b** 。
- **逐項判讀：** a 誤除以 20；b 正確；c、d 是 SSTR 的錯誤或正確平均平方。

#### 選擇題 32 <a id="exam-ch13-mc-32"></a>

##### 題目

> The test statistic equals: a. 0.22; b. 0.84; c. 4.22; d. 4.5.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 分子 MSTR、分母 MSE。**代入計算：** $F=2250/500=4.5$。**解讀結論：** **d** 。
- **逐項判讀：** a 是倒數近似；b、c 為錯誤配除；d 正確。

#### 選擇題 33 <a id="exam-ch13-mc-33"></a>

##### 題目

> At the 5% level, the p-value is: a. less than .01; b. between .01 and .025; c. between .025 and .05; d. between .05 and .10.

##### 詳解


- **辨認題型：** p 值區間。**選方法：** 右尾 $F(3,16)$。**檢查假設：** 自由度沿用 Exhibit。**代入計算：** $P(F_{3,16}\ge4.5)\approx0.018$。**解讀結論：** **b** 。
- **逐項判讀：** a 太小；b 正確；c、d 都比獨立重算值大。

#### 選擇題 34 <a id="exam-ch13-mc-34"></a>

##### 題目

> The null hypothesis: a. should be rejected; b. should not be rejected; c. was designed incorrectly; d. None is correct.

##### 詳解

> **回看投影片講義：** [F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 檢定決策。**選方法：** [F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $\alpha=.05$。**代入推理：** $p\approx.018<.05$。**解讀結論：** **a** ，至少一個母體平均數不同。
- **逐項判讀：** a 正確；b 忽略小 p 值；c 的假設寫法正確；d 因 a 正確而錯。

### 選擇題｜第 35–40 題：題組 13-2

#### 題組 13-2：選擇題 35–40 共用資料

> Part of a randomized-block ANOVA table:

| Source | Sum of Squares | df | Mean Square |
| --- | ---: | ---: | ---: |
| Between Treatments | 2,073.6 | 4 |  |
| Between Blocks | 6,000 | 5 | 1,200 |
| Error |  | 20 | 288 |
| Total |  | 29 |  |

#### 選擇題 35 <a id="exam-ch13-mc-35"></a>

##### 題目

> The null hypothesis is: a. $\mu_1=\cdots=\mu_4$; b. $\mu_1=\cdots=\mu_5$; c. $\mu_1=\cdots=\mu_6$; d. $\mu_1=\cdots=\mu_{20}$.

##### 詳解

> **回看投影片講義：** [集區自由度](./course2-slides-handout.html#formula-anova-block-df)


- **辨認題型：** 由 df 找處理數。**選方法：** 用[集區自由度](./course2-slides-handout.html#formula-anova-block-df)。**檢查假設：** treatment df $=k-1=4$。**代入計算：** $k=5$。**解讀結論：** **b** 。
- **逐項判讀：** a 少一處理；b 正確；c 把 block 數當處理數；d 把 error df 當處理數。

#### 選擇題 36 <a id="exam-ch13-mc-36"></a>

##### 題目

> The mean square between treatments equals: a. 288; b. 518.4; c. 1,200; d. 8,294.4.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR。**選方法：** [MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** treatment df $=4$。**代入計算：** $2073.6/4=518.4$。**解讀結論：** **b** 。
- **逐項判讀：** a 是 MSE；b 正確；c 是 block MS；d 誤乘 df。

#### 選擇題 37 <a id="exam-ch13-mc-37"></a>

##### 題目

> The sum of squares due to error equals: a. 14.4; b. 2,073.6; c. 5,760; d. 6,000.

##### 詳解

> **回看投影片講義：** [MSE 定義](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** SSE。**選方法：** [MSE 定義](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** error df $=20$。**代入計算：** $SSE=288\times20=5760$。**解讀結論：** **c** 。
- **逐項判讀：** a 誤除；b 是 treatment SS；c 正確；d 是 block SS。

#### 選擇題 38 <a id="exam-ch13-mc-38"></a>

##### 題目

> The test statistic equals: a. 0.432; b. 1.8; c. 4.17; d. 28.8.

##### 詳解

> **回看投影片講義：** [集區分解](./course2-slides-handout.html#formula-anova-block-decomp)


- **辨認題型：** 集區設計的處理 F。**選方法：** 用[集區分解](./course2-slides-handout.html#formula-anova-block-decomp)後算 $MSTR/MSE$。**檢查假設：** block 只是控制來源。**代入計算：** $518.4/288=1.8$。**解讀結論：** **b** 。
- **逐項判讀：** a 是錯誤比值；b 正確；c、d 使用 block MS 或錯置小數。

#### 選擇題 39 <a id="exam-ch13-mc-39"></a>

##### 題目

> At the 5% level, the p-value is: a. greater than .10; b. between .10 and .05; c. between .05 and .025; d. between .025 and .01.

##### 詳解


- **辨認題型：** p 值區間。**選方法：** 右尾 $F(4,20)$。**檢查假設：** 自由度來自 treatment 與 error。**代入計算：** $P(F\ge1.8)\approx0.168$。**解讀結論：** **a** 。
- **逐項判讀：** a 正確；b、c、d 都把證據判得過強。

#### 選擇題 40 <a id="exam-ch13-mc-40"></a>

##### 題目

> The null hypothesis: a. should be rejected; b. should not be rejected; c. should be revised; d. None is correct.

##### 詳解

> **回看投影片講義：** [F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 決策。**選方法：** [F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $\alpha=.05$。**代入推理：** $p\approx.168>.05$。**解讀結論：** **b** ，資料不足以判定五個處理平均數不同。
- **逐項判讀：** a 與 p 值矛盾；b 正確；c 不因未拒絕就改假設；d 因 b 正確而錯。

### 選擇題｜第 41–46 題：題組 13-3

#### 題組 13-3：選擇題 41–46 共用資料

> To test whether there is a difference between treatments A, B, and C, 12 observations were randomly assigned:

| Treatment | Observations |
| --- | --- |
| A | 20, 30, 25, 33 |
| B | 22, 26, 20, 28 |
| C | 40, 30, 28, 22 |

#### 選擇題 41 <a id="exam-ch13-mc-41"></a>

##### 題目

> The null hypothesis is: a. $\mu_1=\mu_2$; b. $\mu_1=\mu_2=\mu_3$; c. through $\mu_4$; d. through $\mu_{12}$.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** ANOVA 假設。**選方法：** [整體 F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 三個 treatments。**代入推理：** $H_0$ 比三個母體平均數。**解讀結論：** **b** 。
- **逐項判讀：** a 漏 C；b 正確；c 把每組觀察數誤當組數；d 把每筆資料當母體。

#### 選擇題 42 <a id="exam-ch13-mc-42"></a>

##### 題目

> MSTR equals: a. 1.872; b. 5.86; c. 34; d. 36.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** 組間變異。**選方法：** [MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** 各組 $n=4$，平均數為 27、24、30，grand mean 27。**代入計算：** $SSTR=72, MSTR=72/2=36$。**解讀結論：** **d** 。
- **逐項判讀：** a、b 無對應；c 是 MSE；d 正確。

#### 選擇題 43 <a id="exam-ch13-mc-43"></a>

##### 題目

> MSE equals: a. 1.872; b. 5.86; c. 34; d. 36.

##### 詳解

> **回看投影片講義：** [MSE](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** 組內變異。**選方法：** [MSE](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** error df $=12-3=9$。**代入計算：** $SSE=306,MSE=306/9=34$。**解讀結論：** **c** 。
- **逐項判讀：** a、b 為錯誤平均；c 正確；d 是 MSTR。

#### 選擇題 44 <a id="exam-ch13-mc-44"></a>

##### 題目

> The test statistic equals: a. 0.944; b. 1.059; c. 3.13; d. 19.231.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 分子 36、分母 34。**代入計算：** $F=36/34=1.059$。**解讀結論：** **b** 。
- **逐項判讀：** a 是倒數；b 正確；c、d 為錯誤配除。

#### 選擇題 45 <a id="exam-ch13-mc-45"></a>

##### 題目

> At the 1% level, the p-value is: a. greater than .1; b. between .1 and .05; c. between .05 and .025; d. between .025 and .01.

##### 詳解


- **辨認題型：** p 值。**選方法：** $F(2,9)$ 右尾。**檢查假設：** 自由度正確。**代入計算：** $p\approx0.386>.1$。**解讀結論：** **a** 。
- **逐項判讀：** a 正確；其餘都誇大平均差證據。

#### 選擇題 46 <a id="exam-ch13-mc-46"></a>

##### 題目

> The null hypothesis: a. should be rejected; b. should not be rejected; c. should be revised; d. None is correct.

##### 詳解

> **回看投影片講義：** [F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 決策。**選方法：** [F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $\alpha=.01$。**代入推理：** $p\approx.386>.01$。**解讀結論：** **b** 。
- **逐項判讀：** a 錯；b 正確；c 不是統計決策；d 因 b 正確而錯。

### 選擇題｜第 47–53 題：題組 13-4

#### 題組 13-4：選擇題 47–53 共用資料

> Five treatments, 13 observations each, so $n_T=65$. $SSTR=200$ and $SST=800$.

#### 選擇題 47 <a id="exam-ch13-mc-47"></a>

##### 題目

> SSE is: a. 1,000; b. 600; c. 200; d. 1,600.

##### 詳解

> **回看投影片講義：** [$SST=SSTR+SSE$](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** SS 分解。**選方法：** [$SST=SSTR+SSE$](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 單因子完全隨機。**代入計算：** $800-200=600$。**解讀結論：** **b** 。
- **逐項判讀：** a 誤加；b 正確；c 重抄 SSTR；d 無對應。

#### 選擇題 48 <a id="exam-ch13-mc-48"></a>

##### 題目

> Between-treatments df is: a. 60; b. 59; c. 5; d. 4.

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** df。**選方法：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $k=5$。**代入計算：** $5-1=4$。**解讀結論：** **d** 。
- **逐項判讀：** a 是 error df；b 無對應；c 未減 1；d 正確。

#### 選擇題 49 <a id="exam-ch13-mc-49"></a>

##### 題目

> Within-treatments df is: a. 60; b. 59; c. 5; d. 4.

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** error df。**選方法：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $N=65,k=5$。**代入計算：** $65-5=60$。**解讀結論：** **a** 。
- **逐項判讀：** a 正確；b 是錯誤 total df；c、d 是處理數與處理 df。

#### 選擇題 50 <a id="exam-ch13-mc-50"></a>

##### 題目

> MSTR is: a. 3.34; b. 10.00; c. 50.00; d. 12.00.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR。**選方法：** [MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** treatment df 4。**代入計算：** $200/4=50$。**解讀結論：** **c** 。
- **逐項判讀：** a 誤除 60；b 是 MSE；c 正確；d 無對應。

#### 選擇題 51 <a id="exam-ch13-mc-51"></a>

##### 題目

> MSE is: a. 50; b. 10; c. 200; d. 600.

##### 詳解

> **回看投影片講義：** [MSE](./course2-slides-handout.html#formula-anova-within)


- **辨認題型：** MSE。**選方法：** [MSE](./course2-slides-handout.html#formula-anova-within)。**檢查假設：** error df 60。**代入計算：** $600/60=10$。**解讀結論：** **b** 。
- **逐項判讀：** a 是 MSTR；b 正確；c、d 是平方和。

#### 選擇題 52 <a id="exam-ch13-mc-52"></a>

##### 題目

> The test statistic is: a. 0.2; b. 5.0; c. 3.75; d. 15.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $50/10$。**代入計算：** $F=5$。**解讀結論：** **b** 。
- **逐項判讀：** a 是倒數；b 正確；c、d 為錯誤比值。

#### 選擇題 53 <a id="exam-ch13-mc-53"></a>

##### 題目

> At 95% confidence, the p-value is: a. .05 to .10; b. .025 to .05; c. .01 to .025; d. less than .01.

##### 詳解


- **辨認題型：** p 值區間。**選方法：** $F(4,60)$ 右尾。**檢查假設：** 自由度正確。**代入計算：** $p\approx0.0015<.01$。**解讀結論：** **d** 。
- **逐項判讀：** a、b、c 都太大；d 正確。

### 選擇題｜第 54–57 題：題組 13-5

#### 題組 13-5：選擇題 54–57 共用資料

> Part of an ANOVA table is shown below.

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F |
| --- | ---: | ---: | ---: | ---: |
| Between Treatments | 180 | 3 |  |  |
| Within Treatments (Error) |  |  |  |  |
| Total | 480 | 18 |  |  |

#### 選擇題 54 <a id="exam-ch13-mc-54"></a>

##### 題目

> MSTR is: a. 20; b. 60; c. 300; d. 15.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR。**選方法：** [MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** df 3。**代入計算：** $180/3=60$。**解讀結論：** **b** 。
- **逐項判讀：** a 是 MSE；b 正確；c 是 SSE；d 為錯誤平均。

#### 選擇題 55 <a id="exam-ch13-mc-55"></a>

##### 題目

> MSE is: a. 60; b. 15; c. 300; d. 20.

##### 詳解

> **回看投影片講義：** [SS 與 df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** MSE。**選方法：** [SS 與 df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $SSE=480-180=300$，error df $=18-3=15$。**代入計算：** $MSE=300/15=20$。**解讀結論：** **d** 。
- **逐項判讀：** a 是 MSTR；b 是 df；c 是 SSE；d 正確。

#### 選擇題 56 <a id="exam-ch13-mc-56"></a>

##### 題目

> The test statistic is: a. 2.25; b. 6; c. 2.67; d. 3.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $60/20$。**代入計算：** $F=3$。**解讀結論：** **d** 。
- **逐項判讀：** a、b、c 為錯誤配除；d 正確。

#### 選擇題 57 <a id="exam-ch13-mc-57"></a>

##### 題目

> At 95% confidence, the p-value is: a. .01 to .025; b. .025 to .05; c. .05 to .1; d. greater than .1.

##### 詳解


- **辨認題型：** p 值區間。**選方法：** $F(3,15)$。**檢查假設：** 右尾。**代入計算：** $p\approx0.0638$。**解讀結論：** **c** 。
- **逐項判讀：** a、b 太小；c 正確；d 太大。

### 選擇題｜第 58–62 題：題組 13-6

#### 題組 13-6：選擇題 58–62 共用資料

> Part of an ANOVA table is shown below.

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F |
| --- | ---: | ---: | ---: | ---: |
| Between Treatments | 64 |  |  | 8 |
| Within Treatments (Error) |  |  | 2 |  |
| Total | 100 |  |  |  |

#### 選擇題 58 <a id="exam-ch13-mc-58"></a>

##### 題目

> Between-treatments df is: a. 18; b. 2; c. 4; d. 3.

##### 詳解

> **回看投影片講義：** [F](./course2-slides-handout.html#formula-anova-f)、[MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** 反推 df。**選方法：** [F](./course2-slides-handout.html#formula-anova-f)與[MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** $MSTR=F\times MSE=16$。**代入計算：** $df_1=SSTR/MSTR=64/16=4$。**解讀結論：** **c** 。
- **逐項判讀：** a 是 error df；b 是 MSE；c 正確；d 少 1。

#### 選擇題 59 <a id="exam-ch13-mc-59"></a>

##### 題目

> Within-treatments df is: a. 22; b. 4; c. 5; d. 18.

##### 詳解

> **回看投影片講義：** [SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** error df。**選方法：** [SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $SSE=100-64=36$。**代入計算：** $df_2=SSE/MSE=36/2=18$。**解讀結論：** **d** 。
- **逐項判讀：** a 是 total df；b 是 treatment df；c 是 treatment 數；d 正確。

#### 選擇題 60 <a id="exam-ch13-mc-60"></a>

##### 題目

> MSTR is: a. 36; b. 16; c. 64; d. 15.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** MSTR。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $MSE=2,F=8$。**代入計算：** $MSTR=16$。**解讀結論：** **b** 。
- **逐項判讀：** a 是 SSE；b 正確；c 是 SSTR；d 無對應。

#### 選擇題 61 <a id="exam-ch13-mc-61"></a>

##### 題目

> At 95% confidence, the p-value is: a. greater than .1; b. .05 to .1; c. .025 to .05; d. less than .01.

##### 詳解


- **辨認題型：** p 值。**選方法：** $F(4,18)$。**檢查假設：** 右尾。**代入計算：** $p\approx0.0007<.01$。**解讀結論：** **d** 。
- **逐項判讀：** a、b、c 都太大；d 正確。

#### 選擇題 62 <a id="exam-ch13-mc-62"></a>

##### 題目

> The conclusion is that the means: a. are equal; b. may be equal; c. are not equal; d. None is correct.

##### 詳解

> **回看投影片講義：** [F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 結論。**選方法：** [F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $p<.01<.05$。**代入推理：** 拒絕全部平均相等。**解讀結論：** 題庫措辭下選 **c** ；嚴謹說法是「至少一個母體平均數不同」。
- **逐項判讀：** a 把未檢定成立當成結論；b 不符小 p 值；c 最接近且正確；d 因 c 可選而錯。

### 選擇題｜第 63–68 題：題組 13-7

#### 題組 13-7：選擇題 63–68 共用資料

> The following is part of an ANOVA table obtained from three treatments and 15 observations.

| Source of Variation | Sum of Squares | Degrees of Freedom |
| --- | ---: | ---: |
| Between Treatments | 64 |  |
| Error (Within Treatments) | 96 |  |

#### 選擇題 63 <a id="exam-ch13-mc-63"></a>

##### 題目

> Between-treatments df is: a. 12; b. 2; c. 3; d. 4.

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** df。**選方法：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $k=3$。**代入計算：** $df_1=2$。**解讀結論：** **b** 。
- **逐項判讀：** a 是 error df；b 正確；c 未減 1；d 無對應。

#### 選擇題 64 <a id="exam-ch13-mc-64"></a>

##### 題目

> Within-treatments df is: a. 12; b. 2; c. 3; d. 15.

##### 詳解

> **回看投影片講義：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** error df。**選方法：** [自由度分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** $N=15,k=3$。**代入計算：** $15-3=12$。**解讀結論：** **a** 。
- **逐項判讀：** a 正確；b 是 treatment df；c 是 k；d 是 N。

#### 選擇題 65 <a id="exam-ch13-mc-65"></a>

##### 題目

> MSTR is: a. 36; b. 16; c. 8; d. 32.

##### 詳解

> **回看投影片講義：** [MSTR](./course2-slides-handout.html#formula-anova-between)


- **辨認題型：** MSTR。**選方法：** [MSTR](./course2-slides-handout.html#formula-anova-between)。**檢查假設：** df 2。**代入計算：** $64/2=32$。**解讀結論：** **d** 。
- **逐項判讀：** a 無對應；b 是錯除；c 是 MSE；d 正確。

#### 選擇題 66 <a id="exam-ch13-mc-66"></a>

##### 題目

> The computed test statistic is: a. 32; b. 8; c. 0.667; d. 4.

##### 詳解

> **回看投影片講義：** [F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** F。**選方法：** [F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $MSE=96/12=8$。**代入計算：** $F=32/8=4$。**解讀結論：** **d** 。
- **逐項判讀：** a、b 是兩個 mean squares；c 是平方和比值；d 正確。

#### 選擇題 67 <a id="exam-ch13-mc-67"></a>

##### 題目

> At 95% confidence, the p-value is: a. .01 to .025; b. .025 to .05; c. .05 to .1; d. greater than .1.

##### 詳解


- **辨認題型：** p 值。**選方法：** $F(2,12)$。**檢查假設：** 右尾。**代入計算：** $p\approx0.0467$。**解讀結論：** **b** 。
- **逐項判讀：** a 太小；b 正確；c、d 太大。

#### 選擇題 68 <a id="exam-ch13-mc-68"></a>

##### 題目

> The conclusion is that the means: a. are equal; b. may be equal; c. are not equal; d. None is correct.

##### 詳解

> **回看投影片講義：** [F 檢定](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 決策。**選方法：** [F 檢定](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** $p\approx.0467<.05$。**代入推理：** 拒絕全部相等。**解讀結論：** 題庫語句下選 **c** ；精確說法是至少一個平均數不同。
- **逐項判讀：** a、b 不符檢定；c 正確；d 因 c 正確而錯。

### 計算題｜第 1–16 題：完全隨機單因子 ANOVA

#### 計算題 1 <a id="exam-ch13-problem-1"></a>

##### 題目

> Information regarding the ACT scores of samples of students in three different majors is given below.

| Major | Management | Finance | Accounting |
| --- | ---: | ---: | ---: |
| Sample size | 12 | 9 | 12 |
| Average | 24 | 25 | 26 |
| Sample variance | 18 | 7 | 10 |

> a. Compute the overall sample mean.
> b. Set up the ANOVA table including the test statistic.
> c. At 95% confidence, determine the critical value of F.
> d. Use the critical-value approach.
> e. Determine the p-value and use it for the test.

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)、[整體 F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三個獨立科系的數值平均數。**選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch13-method-selection)使用完全隨機單因子 ANOVA 與[整體 F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 各學生獨立、各科系分數近似常態、母體變異數相同；題目只給摘要，無法由此檢查離群與形狀。
- **代入計算：** $N=33$，加權總平均 $=(12\times24+9\times25+12\times26)/33=25$。由[組間](./course2-slides-handout.html#formula-anova-between)與[組內](./course2-slides-handout.html#formula-anova-within)公式得 $SSTR=24,SSE=364,SST=388$。

  | Source | SS | df | MS | F |
  | --- | ---: | ---: | ---: | ---: |
  | Treatments | 24 | 2 | 12 | 0.989 |
  | Error | 364 | 30 | 12.133 |  |
  | Total | 388 | 32 |  |  |

  $F_{.05;2,30}=3.316$，且 $p=0.3837$。
- **解讀結論：** $0.989<3.316$ 且 $p>.05$，不拒絕 $H_0$；沒有足夠證據認為三科系母體平均 ACT 分數不同。

#### 計算題 2 <a id="exam-ch13-problem-2"></a>

##### 題目

> Starting salaries (in \$1,000) for four majors:

| Major | Management | Marketing | Finance | Accounting |
| --- | ---: | ---: | ---: | ---: |
| Sample size | 12 | 10 | 9 | 14 |
| Average | 26 | 31 | 22 | 25 |
| Sample variance | 10 | 7 | 15 | 9 |

> a. Compute the overall sample mean. b. Set up the ANOVA table. c. Find the 95% F critical value. d. Test by the critical-value approach. e. Determine the p-value.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 四個獨立科系平均起薪。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 個人獨立、各組起薪近似常態、等變異；只有摘要資料，診斷受限。
- **代入計算：** $N=45$，$\bar{\bar{x}}=26$；$SSTR=408,SSE=410,SST=818$。

  | Source | SS | df | MS | F |
  | --- | ---: | ---: | ---: | ---: |
  | Treatments | 408 | 3 | 136 | 13.600 |
  | Error | 410 | 41 | 10 |  |
  | Total | 818 | 44 |  |  |

  $F_{.05;3,41}=2.833$，$p=2.66\times10^{-6}$。
- **解讀結論：** 拒絕 $H_0$，至少一個科系的平均起薪不同。原題 d 寫「three populations」但表格明明有四組；這是原題文字疑義，計算依四組進行。

#### 計算題 3 <a id="exam-ch13-problem-3"></a>

##### 題目

> Sales (in \$1,000): Store 1 = 80, 75, 76, 89, 80; Store 2 = 85, 86, 81, 80; Store 3 = 79, 85, 88. Compute the overall mean, state hypotheses, complete the ANOVA table, and test at 95% confidence using critical value and p-value.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三家獨立門市、不等樣本數。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 每筆銷售獨立、各店近似常態且等變異；若是同一天配對門市則不應視為獨立，但題目未提供配對。
- **代入計算：** 組平均為 80、83、84，$\bar{\bar{x}}=82$；$SSTR=36,SSE=190,SST=226$。df 為 2、9、11；$MSTR=18,MSE=21.111,F=0.853$；$F_{.05;2,9}=4.256$，$p=0.4580$。
- **解讀結論：** 不拒絕 $H_0:\mu_1=\mu_2=\mu_3$；沒有足夠證據顯示三店平均銷售不同。

#### 計算題 4 <a id="exam-ch13-problem-4"></a>

##### 題目

> Heating bills (dollars): Natural Gas = 84, 64, 93, 88, 71; Central Electric = 95, 60, 89, 96, 90; Heat Pump = 85, 93, 90, 92, 80. Test at $\alpha=.05$ by both p-value and critical-value approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三種供暖類型的平均帳單。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 房屋彼此獨立；各類帳單近似常態且等變異；沒有同戶跨類型重測。
- **代入計算：** 組平均 80、86、88，grand mean $84.667$；$SSTR=173.333,SSE=1586,SST=1759.333$；df $=(2,12,14)$；$MSTR=86.667,MSE=132.167,F=0.656$。$F_{.05;2,12}=3.885$，$p=0.5367$。
- **解讀結論：** 不拒絕 $H_0$；樣本沒有顯示三種供暖房屋的平均帳單不同。

#### 計算題 5 <a id="exam-ch13-problem-5"></a>

##### 題目

> A completely randomized design used 18, 10, and 15 units for three treatments. The table gives $MSE=6$ and $F=3.0$.
> a. Fill in all blanks. b. Test at 95% confidence.

##### 詳解

> **回看投影片講義：** [MSE](./course2-slides-handout.html#formula-anova-within)、[F](./course2-slides-handout.html#formula-anova-f)、[分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 由 $n_j,MSE,F$ 反推 ANOVA 表。**選方法：** [MSE](./course2-slides-handout.html#formula-anova-within)、[F](./course2-slides-handout.html#formula-anova-f)與[分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $N=43,k=3$，df 為 treatment 2、error 40、total 42。$MSTR=3\times6=18$，故 $SSTR=36$；$SSE=6\times40=240$；$SST=276$。$F_{.05;2,40}=3.232$，$p=0.0611$。
- **解讀結論：** $F=3.0<3.232$ 且 $p>.05$，不拒絕三個母體平均數相等。

#### 計算題 6 <a id="exam-ch13-problem-6"></a>

##### 題目

> Treatment 1 = 37, 33, 36, 38; Treatment 2 = 43, 39, 35, 38, 40; Treatment 3 = 28, 32, 33. Compute the overall mean and test at 95% confidence by critical value and p-value.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組獨立樣本且 $n$ 不等。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)，grand mean 必須加權。**檢查假設：** 觀測獨立、組內近似常態、等變異。
- **代入計算：** 組平均 36、39、31，grand mean 36；$SSTR=120,SSE=62,SST=182$；df $=(2,9,11)$；$MSTR=60,MSE=6.889,F=8.710$。$F_{.05;2,9}=4.256$，$p=0.00786$。
- **解讀結論：** 拒絕 $H_0$；至少一組平均數不同。

#### 計算題 7 <a id="exam-ch13-problem-7"></a>

##### 題目

> A completely randomized design used 7, 9, and 14 units. The table gives $MSE=4$ and $F=4.5$. Fill in all blanks and test at 95% confidence using both approaches.

##### 詳解

> **回看投影片講義：** [MSE、MSTR 與 F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 反推 ANOVA 表。**選方法：** [MSE、MSTR 與 F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $N=30,k=3$；df 為 2、27、29。$MSTR=4.5\times4=18$；$SSTR=36$；$SSE=108$；$SST=144$。$F_{.05;2,27}=3.354$，$p=0.0206$。
- **解讀結論：** $4.5>3.354$ 且 $p<.05$，拒絕 $H_0$。

#### 計算題 8 <a id="exam-ch13-problem-8"></a>

##### 題目

> Treatment 1 = 45, 41, 37, 40, 42; Treatment 2 = 31, 34, 35, 40; Treatment 3 = 39, 35, 40. Compute the overall mean and test at 95% confidence.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組不等 $n$。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 獨立、近似常態、等變異。
- **代入計算：** 組平均 41、35、38；加權 grand mean $38.25$。$SSTR=80.25,SSE=90,SST=170.25$；df $=(2,9,11)$；$MSTR=40.125,MSE=10,F=4.0125$；$F_{.05;2,9}=4.256$，$p=0.0568$。
- **解讀結論：** 在 .05 水準不拒絕 $H_0$；雖接近門檻，仍不能寫成「有顯著差異」。

#### 計算題 9 <a id="exam-ch13-problem-9"></a>

##### 題目

> Eight printers per brand. Average life (months): A 62, B 52, C 60. Sample variances: 36, 25, 49. Compute grand mean, state hypotheses, complete ANOVA, and test at 95% confidence using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組等樣本摘要。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 印表機獨立、品牌內壽命近似常態、共同變異數；只有摘要無法檢查離群。
- **代入計算：** grand mean 58；$SSTR=448,SSE=770,SST=1218$；df $=(2,21,23)$；$MSTR=224,MSE=36.667,F=6.109$。$F_{.05;2,21}=3.467$，$p=0.00811$。
- **解讀結論：** 拒絕 $H_0:\mu_A=\mu_B=\mu_C$；至少一品牌平均壽命不同。

#### 計算題 10 <a id="exam-ch13-problem-10"></a>

##### 題目

> Sample 1 = 31, 28, 34, 32, 26, 29; Sample 2 = 37, 32, 34, 24, 32, 33; Sample 3 = 37, 31, 32, 39, 30, 35. Test at $\alpha=.05$ using critical value and p-value.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組獨立平均數。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 獨立、近似常態、等變異。
- **代入計算：** 組平均 30、32、34，grand mean 32；$SSTR=48,SSE=200,SST=248$；df $=(2,15,17)$；$MSTR=24,MSE=13.333,F=1.8$。$F_{.05;2,15}=3.682$，$p=0.1992$。
- **解讀結論：** 不拒絕 $H_0$；沒有足夠證據顯示三平均數不同。

#### 計算題 11 <a id="exam-ch13-problem-11"></a>

##### 題目

> Instructor A = 83, 60, 80, 85, 71; B = 90, 55, 84, 91, 85; C = 85, 90, 90, 95, 80. Test at $\alpha=.05$ using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三位教師的獨立學生平均成績。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 學生獨立、各組近似常態且等變異；若學生不是隨機分配，差異也不能直接解讀為教師因果效果。
- **代入計算：** 組平均 75.8、81、88，grand mean 81.6；$SSTR=374.8,SSE=1438.8,SST=1813.6$；df $=(2,12,14)$；$MSTR=187.4,MSE=119.9,F=1.563$。臨界值 3.885，$p=0.2493$。
- **解讀結論：** 不拒絕 $H_0$；資料不足以認為三位教師母體平均成績不同。

#### 計算題 12 <a id="exam-ch13-problem-12"></a>

##### 題目

> University A = 89, 95, 75, 92, 99, 90; B = 60, 95, 89, 80, 66; C = 82, 70, 90, 79. Compute grand mean and test at $\alpha=.01$ using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三校不等樣本數。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 個體獨立、校內近似常態、等變異；觀察比較不自動支持學校造成差異。
- **代入計算：** 組平均 90、78、80.25；grand mean 83.4。$SSTR=446.85,SSE=1422.75,SST=1869.6$；df $=(2,12,14)$；$MSTR=223.425,MSE=118.5625,F=1.884$。$F_{.01;2,12}=6.927$，$p=0.1942$。
- **解讀結論：** 不拒絕 $H_0$；在 1% 水準沒有足夠證據顯示三校平均分數不同。

#### 計算題 13 <a id="exam-ch13-problem-13"></a>

##### 題目

> Three treatments, 11 units each. $SSTR=1,500$ and $SST=6,000$. Fill in the ANOVA table and test at 95% confidence.

##### 詳解

> **回看投影片講義：** [SS/df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)、[F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 由平方和與樣本數完成表。**選方法：** [SS/df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)與[F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $N=33,k=3$；$SSE=4500$。df $=(2,30,32)$；$MSTR=750,MSE=150,F=5$。$F_{.05;2,30}=3.316$，$p=0.01336$。
- **解讀結論：** 拒絕 $H_0$；至少一個母體平均數不同。

#### 計算題 14 <a id="exam-ch13-problem-14"></a>

##### 題目

> Store 1 = 88, 84, 88, 82, 93; Store 2 = 76, 78, 60, 62; Store 3 = 85, 67, 58. Compute grand mean and show complete ANOVA work; test at 95% confidence using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三店不等 $n$。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 銷售觀測獨立、各店近似常態且等變異；若按同日配對則應改成集區設計。
- **代入計算：** 組平均 87、69、70，grand mean 76.75；$SSTR=902.25,SSE=710,SST=1612.25$；df $=(2,9,11)$；$MSTR=451.125,MSE=78.889,F=5.718$。$F_{.05;2,9}=4.256$，$p=0.02496$。
- **解讀結論：** 拒絕 $H_0$；至少一店平均銷售不同。

#### 計算題 15 <a id="exam-ch13-problem-15"></a>

##### 題目

> Ten tires per brand. Average mileage (1,000 miles): A 37, B 38, C 33. Sample variances: 3, 4, 2. Test equal means at $\alpha=.05$ using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三品牌平均里程。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 輪胎獨立、品牌內近似常態、等變異；三個樣本變異數在同量級。
- **代入計算：** grand mean 36；$SSTR=140,SSE=81,SST=221$；df $=(2,27,29)$；$MSTR=70,MSE=3,F=23.333$。$F_{.05;2,27}=3.354$，$p=1.30\times10^{-6}$。
- **解讀結論：** 拒絕 $H_0$；至少一品牌平均里程不同。

#### 計算題 16 <a id="exam-ch13-problem-16"></a>

##### 題目

> Fifteen cars per model. Average MPG: A 42, B 49, C 44. Sample standard deviations: 4, 5, 3. Test equal means at $\alpha=.05$ using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三車款平均 MPG。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 車輛獨立、各車款 MPG 近似常態、等變異；注意題給的是標準差，需先平方。
- **代入計算：** 變異數為 16、25、9；grand mean 45。$SSTR=390,SSE=700,SST=1090$；df $=(2,42,44)$；$MSTR=195,MSE=16.667,F=11.7$。$F_{.05;2,42}=3.220$，$p=9.14\times10^{-5}$。
- **解讀結論：** 拒絕 $H_0$；至少一車款平均 MPG 不同。原題用 gasoline consumption 描述 MPG，解讀時以實際量測單位 miles/gallon 為準。

### 計算題｜第 17–32 題：完整表、LSD、集區與二因子

#### 計算題 17 <a id="exam-ch13-problem-17"></a>

##### 題目

> At $\alpha=.05$, test whether the means are equal using both approaches.
> Sample 1 = 60, 78, 72, 66; Sample 2 = 84, 78, 93, 81; Sample 3 = 60, 57, 69, 66.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組獨立平均數。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 獨立、近似常態、等變異。
- **代入計算：** 組平均 69、84、63，grand mean 72；$SSTR=936,SSE=396,SST=1332$；df $=(2,9,11)$；$MSTR=468,MSE=44,F=10.636$。$F_{.05;2,9}=4.256$，$p=0.00426$。
- **解讀結論：** 拒絕 $H_0$；至少一組母體平均數不同。

#### 計算題 18 <a id="exam-ch13-problem-18"></a>

##### 題目

> Method I = 182, 170, 179; Method II = 170, 192, 190; Method III = 162, 166.
> a. Compute the overall mean. b. At $\alpha=.05$, show the complete ANOVA table and use both approaches.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三種方法、不等 $n$。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 每個生產單位獨立、各方法近似常態、等變異。
- **代入計算：** 組平均 177、184、164；grand mean $176.375$。$SSTR=481.875,SSE=382,SST=863.875$；df $=(2,5,7)$；$MSTR=240.9375,MSE=76.4,F=3.154$。$F_{.05;2,5}=5.786$，$p=0.1300$。
- **解讀結論：** 不拒絕 $H_0$；小樣本下沒有足夠證據認為三方法平均產量不同。

#### 計算題 19 <a id="exam-ch13-problem-19"></a>

##### 題目

> Diet A = 14, 18, 20, 12, 20, 18; Diet B = 12, 10, 22, 12, 16, 12; Diet C = 25, 32, 18, 14, 17, 14.
> a. State hypotheses. b. Calculate the test statistic. c. Advise the dietician at .05.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 18 人隨機分派到三飲食法。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 人與人獨立、各飲食組減重近似常態、等變異；隨機分派支持處理比較。
- **代入計算：** $H_0:\mu_A=\mu_B=\mu_C$；組平均 17、14、20。$SSTR=108,SSE=404$；df $=(2,15)$；$MSTR=54,MSE=26.933,F=2.005$；$p=0.1692$，臨界值 3.682。
- **解讀結論：** 不拒絕 $H_0$；目前資料不足以認為三種飲食法平均減重不同，不能據此推薦某一法為最佳。

#### 計算題 20 <a id="exam-ch13-problem-20"></a>

##### 題目

> Program A = 150, 130, 120, 180, 145; B = 150, 120, 135, 160, 110; C = 185, 220, 190, 180, 175; D = 175, 150, 120, 130, 175.
> a. State hypotheses. b. Construct ANOVA. c. Advise at .05 using both approaches. d. Use Fisher's LSD at .05.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-anova-f)、[Fisher LSD](./course2-slides-handout.html#formula-anova-lsd-threshold)


- **辨認題型：** 四方案整體平均數，顯著後定位差異。**選方法：** 先用[整體 F](./course2-slides-handout.html#formula-anova-f)，再用[Fisher LSD](./course2-slides-handout.html#formula-anova-lsd-threshold)。**檢查假設：** 員工獨立且隨機分派、各組近似常態、等變異。
- **代入計算：** 組平均 A 145、B 135、C 190、D 150；grand mean 155。$SSTR=8750,SSE=7600,SST=16350$；df $=(3,16,19)$；$MSTR=2916.667,MSE=475,F=6.140$。$F_{.05;3,16}=3.239$，$p=0.00557$，故整體顯著。$LSD=t_{.025,16}\sqrt{475(1/5+1/5)}=29.221$。
- **解讀結論：** C-A 差 45、C-B 差 55、C-D 差 40，均超過 LSD；A-B 10、A-D 5、B-D 15 均未超過。方案 C 的平均產量顯著高於另外三方案；A、B、D 間沒有足夠差異證據。

#### 計算題 21 <a id="exam-ch13-problem-21"></a>

##### 題目

> Sales table:

| Box | Store 1 | Store 2 | Store 3 | Store 4 | Store 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Box 1 | 210 | 230 | 190 | 180 | 190 |
| Box 2 | 195 | 170 | 200 | 190 | 193 |
| Box 3 | 295 | 275 | 290 | 275 | 265 |

> a. State hypotheses. b. Construct ANOVA. c. Conclude. d. Use Fisher's LSD at $\alpha=.01$.

##### 詳解

> **回看投影片講義：** [完全隨機 vs 集區](./course2-slides-handout.html#compare-ch13-method-selection)、[隨機集區分解](./course2-slides-handout.html#formula-anova-block-decomp)


- **辨認題型：** 每家 store 同時測三盒型，store 是集區。**選方法：** 依[完全隨機 vs 集區](./course2-slides-handout.html#compare-ch13-method-selection)採[隨機集區分解](./course2-slides-handout.html#formula-anova-block-decomp)，不是把 15 筆當獨立。**檢查假設：** 各店獨立；扣除盒型與店別後誤差近似常態、等變異且加成；每格一筆，無法另估交互作用。
- **代入計算：** 盒型平均 200、189.6、280；grand mean 223.2。$SSTR=24467.2,SSBL=711.067,SSE=2022.133,SST=27200.4$；df $=(2,4,8,14)$；$MSTR=12233.6,MSE=252.767,F=48.399$。在 .01，臨界值 8.649，$p=3.40\times10^{-5}$。$LSD=t_{.005,8}\sqrt{252.767(2/5)}=33.739$。
- **解讀結論：** 整體拒絕 $H_0$。Box 3 與 Box 1 差 80、與 Box 2 差 90.4，皆顯著；Box 1 與 2 差 10.4，不顯著。Box 3 平均銷售最高。

#### 計算題 22 <a id="exam-ch13-problem-22"></a>

##### 題目

> ANOVA table entries: treatment df $=3$, treatment MS $=1,198.8$; block SS $=5,040$, block df $=6$, block MS $=840$; error SS $=5,994$, error df $=18$; total df $=27$.
> a. State hypotheses. b. Compute treatment SS. c. Compute MSE. d. Compute total SS. e. Compute F. f. Test at 1%.

##### 詳解

> **回看投影片講義：** [集區平方和與 df](./course2-slides-handout.html#formula-anova-block-decomp)


- **辨認題型：** 隨機集區 ANOVA 缺格。**選方法：** [集區平方和與 df](./course2-slides-handout.html#formula-anova-block-decomp)。**檢查假設：** 四處理、七集區；集區獨立、加成誤差近似常態且等變異。
- **代入計算：** $H_0:\mu_1=\mu_2=\mu_3=\mu_4$。$SSTR=1198.8\times3=3596.4$；$MSE=5994/18=333$；$SST=3596.4+5040+5994=14630.4$；$F=1198.8/333=3.6$。$F_{.01;3,18}=5.092$，$p=0.03385$。
- **解讀結論：** 在 1% 水準不拒絕 $H_0$；雖然 $p<.05$，題目指定的是更嚴格的 .01。

#### 計算題 23 <a id="exam-ch13-problem-23"></a>

##### 題目

> Four populations, each $n=11$. Sample means = 40, 35, 39, 37; sample variances = 23.4, 21.6, 25.2, 24.6. Test at .05.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 四組等樣本摘要。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 題目已假設等變異；仍需獨立與近似常態。
- **代入計算：** grand mean 37.75；$SSTR=162.25,SSE=948,SST=1110.25$；df $=(3,40,43)$；$MSTR=54.083,MSE=23.7,F=2.282$。$F_{.05;3,40}=2.839$，$p=0.09383$。
- **解讀結論：** 不拒絕 $H_0$；沒有足夠證據認為四母體平均數不同。

#### 計算題 24 <a id="exam-ch13-problem-24"></a>

##### 題目

> Hours of use:

| Radio | Brand 1 | Brand 2 | Brand 3 | Brand 4 |
| --- | ---: | ---: | ---: | ---: |
| A | 25 | 27 | 20 | 28 |
| B | 29 | 38 | 24 | 37 |
| C | 21 | 28 | 16 | 19 |

> a. Ignore radios and analyze as completely randomized at .05. b. Analyze radios as blocks. c. Compare.

##### 詳解

> **回看投影片講義：** [設計比較準則](./course2-slides-handout.html#compare-ch13-method-selection)、[整體 F](./course2-slides-handout.html#formula-anova-f)、[集區分解](./course2-slides-handout.html#formula-anova-block-decomp)


- **辨認題型：** 同一資料比較完全隨機與集區。**選方法：** 依[設計比較準則](./course2-slides-handout.html#compare-ch13-method-selection)，a 用[整體 F](./course2-slides-handout.html#formula-anova-f)，b 用[集區分解](./course2-slides-handout.html#formula-anova-block-decomp)。**檢查假設：** 電池觀測獨立於其他電池；集區版本另假設 radio 效果可加、無可估交互作用。
- **代入計算：** 品牌平均 25、31、20、28，grand mean 26。忽略 radio：$SSTR=198,SSE=300$，df $=(3,8)$，$MSTR=66,MSE=37.5,F=1.76,p=0.2323$，不拒絕。以 radio 集區：$SSBL=248$，$SSE=52$，df $=(3,2,6)$，$MSE=8.667,F=7.615,p=0.01808$，臨界值 $4.757$。
- **解讀結論：** 集區後拒絕四品牌平均壽命相等；忽略 radio 則不拒絕。radio 差異從 error 中移出，使 MSE 從 37.5 降至 8.667，顯示正確設計能提高檢定力。

#### 計算題 25 <a id="exam-ch13-problem-25"></a>

##### 題目

> Factor A is program; Factor B is sex. Observations:

| Program | Male | Female |
| --- | --- | --- |
| A | 320, 240 | 380, 300 |
| B | 160, 180 | 240, 210 |
| C | 240, 290 | 360, 380 |

> a. Set up the ANOVA table. b. Advise MNM at .05.

##### 詳解

> **回看投影片講義：** [二因子分解](./course2-slides-handout.html#formula-anova-factorial-decomp)


- **辨認題型：** $3\times2$ 因子實驗，每格重複 2 次。**選方法：** 用[二因子分解](./course2-slides-handout.html#formula-anova-factorial-decomp)，分別檢定 program、sex、interaction。**檢查假設：** 12 位員工獨立；每格誤差近似常態、共同變異數；每格重複讓交互作用可估。
- **代入計算：** grand mean 275。$SSA=36150,SSB=16133.333,SSAB=1516.667,SSE=8500,SST=62300$。df 為 2、1、2、6、11；$MSA=18075,MSB=16133.333,MSAB=758.333,MSE=1416.667$。$F_A=12.759,p=.00690$；$F_B=11.388,p=.01496$；$F_{AB}=0.535,p=.6111$。
- **解讀結論：** 在 .05，program 與 sex 主效果顯著，交互作用不顯著。Program B 平均 197.5，低於 A 310 與 C 317.5；female 平均 311.667，高於 male 238.333。整體 F 不直接指出 A 與 C 是否不同，若要定位需另做適當多重比較。

#### 計算題 26 <a id="exam-ch13-problem-26"></a>

##### 題目

> Class A = 92, 85, 96, 95; B = 91, 85, 90, 86; C = 85, 93, 82, 84. Test at $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三班平均成績。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 學生獨立、班內近似常態、等變異；觀察比較不等於授課因果。
- **代入計算：** 平均 92、88、86；grand mean 88.667。$SSTR=74.667,SSE=170$；df $=(2,9)$；$MSTR=37.333,MSE=18.889,F=1.976$；$p=0.1943$，臨界值 4.256。
- **解讀結論：** 不拒絕 $H_0$。

#### 計算題 27 <a id="exam-ch13-problem-27"></a>

##### 題目

> Process 1 = 33, 30, 28, 29; Process 2 = 33, 35, 30, 38; Process 3 = 28, 36, 30, 34. Test at .05 using both approaches.

##### 詳解

> **回看投影片講義：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 隨機分派到三製程。**選方法：** [完全隨機 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 個體獨立、各製程近似常態、等變異。
- **代入計算：** 平均 30、34、32；$SSTR=32,SSE=88,SST=120$；df $=(2,9,11)$；$MSTR=16,MSE=9.778,F=1.636$；$p=0.2477$，臨界值 4.256。
- **解讀結論：** 不拒絕 $H_0$；沒有顯著平均產量差異。

#### 計算題 28 <a id="exam-ch13-problem-28"></a>

##### 題目

> Department A = 40, 37, 43, 41, 35, 38; B = 46, 41, 43, 33, 41, 42; C = 46, 40, 41, 48, 39, 44. Test at .05 using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三部門平均年所得。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 員工獨立、各部門所得近似常態、等變異；非隨機分派，不作部門因果解讀。
- **代入計算：** 平均 39、41、43；$SSTR=48,SSE=200$；df $=(2,15)$；$F=24/13.333=1.8$；$p=0.1992$，臨界值 3.682。
- **解讀結論：** 不拒絕 $H_0$。

#### 計算題 29 <a id="exam-ch13-problem-29"></a>

##### 題目

> Gas = 83, 80, 82, 83, 82; Central Electric = 90, 88, 87, 82, 83; Heat Pump = 81, 83, 80, 82, 79. Test at .05 using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三種供暖平均帳單。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 房屋獨立、組內近似常態、等變異。
- **代入計算：** 平均 82、86、81；grand mean 83。$SSTR=70,SSE=62,SST=132$；df $=(2,12,14)$；$MSTR=35,MSE=5.167,F=6.774$；$F_{.05;2,12}=3.885$，$p=0.01074$。
- **解讀結論：** 拒絕 $H_0$；至少一供暖類型平均帳單不同。

#### 計算題 30 <a id="exam-ch13-problem-30"></a>

##### 題目

> Northern = 75, 80, 84, 85, 81; Central = 85, 89, 86, 88; Southern = 80, 81, 84, 79, 83, 85. Test at $\alpha=.01$ using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三校不等樣本數。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 個體獨立、校內近似常態、等變異；不可由觀察資料直接談學校因果。
- **代入計算：** 平均 81、87、82；grand mean 83。$SSTR=90,SSE=100$；df $=(2,12)$；$MSTR=45,MSE=8.333,F=5.4$；$F_{.01;2,12}=6.927$，$p=0.02126$。
- **解讀結論：** 在 .01 不拒絕 $H_0$。注意 $p<.05$ 但仍大於題目指定的 .01。

#### 計算題 31 <a id="exam-ch13-problem-31"></a>

##### 題目

> Manufacturer A = 180, 175, 179, 176, 190; B = 177, 180, 167, 172; C = 175, 176, 177. Test at .05 using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三廠牌平均速度、不等 $n$。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 測試車獨立、各廠牌近似常態、等變異。
- **代入計算：** 平均 180、174、176；grand mean 177。$SSTR=84,SSE=242$；df $=(2,9)$；$MSTR=42,MSE=26.889,F=1.562$；$p=0.2616$，臨界值 4.256。
- **解讀結論：** 不拒絕 $H_0$。

#### 計算題 32 <a id="exam-ch13-problem-32"></a>

##### 題目

> Part of an ANOVA table: $SSTR=90$, treatment df $=3$; $SSE=120$, error df $=20$.
> a. Fill in MS and F, and test at $\alpha=.01$. b. How many groups? c. What total number of observations?

##### 詳解

> **回看投影片講義：** [SS/df 與 F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 由 df 與 SS 完成表。**選方法：** [SS/df 與 F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $MSTR=90/3=30$；$MSE=120/20=6$；$F=5$。$k=3+1=4$；$N=df_E+k=24$，total df 23，$SST=210$。$F_{.01;3,20}=4.938$，$p=0.00951$。
- **解讀結論：** 因 $p<.01$，拒絕四個母體平均數全部相等。

### 計算題｜第 33–47 題：混合題型與最後總複習

#### 計算題 33 <a id="exam-ch13-problem-33"></a>

##### 題目

> Eight groups. $SSTR=126$, $SSE=240$, and total df $=67$.
> a. Complete all missing values. b. Test at $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [自由度與 SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 由組數與 total df 完成表。**選方法：** [自由度與 SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $k=8,N=68$；df treatment $=7$、error $=60$。$SST=366$；$MSTR=126/7=18$；$MSE=240/60=4$；$F=4.5$。$F_{.05;7,60}=2.167$，$p=0.000441$。
- **解讀結論：** 拒絕八個母體平均數全部相等。

#### 計算題 34 <a id="exam-ch13-problem-34"></a>

##### 題目

> Store 1 = 9, 8, 7, 8; Store 2 = 10, 11, 10, 13; Store 3 = 6, 7, 8, 11. Test at 95% confidence using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三店平均每日銷售。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 每筆銷售獨立、店內近似常態、等變異；若三店是同日成組觀察，應考慮日期集區，但原題未給日期結構。
- **代入計算：** 組平均 8、11、8；grand mean 9。$SSTR=24,SSE=22,SST=46$；df $=(2,9,11)$；$MSTR=12,MSE=2.444,F=4.909$；$F_{.05;2,9}=4.256$，$p=0.03618$。
- **解讀結論：** 拒絕 $H_0$；至少一店平均銷售不同。

#### 計算題 35 <a id="exam-ch13-problem-35"></a>

##### 題目

> Five drivers test both automobiles:

| Automobile | Driver 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 30 | 31 | 30 | 27 | 32 |
| B | 36 | 35 | 28 | 31 | 30 |

> Treat automobiles as treatments and drivers as blocks; test MPG difference at $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [完全隨機 vs 集區 vs 配對](./course2-slides-handout.html#compare-ch13-method-selection)、[隨機集區 ANOVA](./course2-slides-handout.html#formula-anova-block-decomp)


- **辨認題型：** 同一駕駛測兩車款，兩處理、五集區。**選方法：** 依[完全隨機 vs 集區 vs 配對](./course2-slides-handout.html#compare-ch13-method-selection)用[隨機集區 ANOVA](./course2-slides-handout.html#formula-anova-block-decomp)；兩處理時也等價於配對 t 的平方。**檢查假設：** 駕駛彼此獨立，車款效果與駕駛效果可加，差值近似常態。
- **代入計算：** 車款平均 A 30、B 32；grand mean 31。$SSTR=10,SSBL=32,SSE=28,SST=70$；df $=(1,4,4,9)$；$MSTR=10,MSE=7,F=1.429$；$F_{.05;1,4}=7.709$，$p=0.2980$。
- **解讀結論：** 不拒絕兩車款平均 MPG 相等；樣本不足以支持車款差異。

#### 計算題 36 <a id="exam-ch13-problem-36"></a>

##### 題目

> Factor A level 1: under B1 = 14, 16; under B2 = 18, 12.
> Factor A level 2: under B1 = 18, 20; under B2 = 16, 14.
> Set up ANOVA and test all main and interaction effects at $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [二因子分解](./course2-slides-handout.html#formula-anova-factorial-decomp)


- **辨認題型：** $2\times2$ 因子實驗，每格兩次重複。**選方法：** [二因子分解](./course2-slides-handout.html#formula-anova-factorial-decomp)。**檢查假設：** 八筆觀測獨立、各格誤差近似常態與共同變異數、每格有重複。
- **代入計算：** grand mean 16；A 邊際平均 15、17；B 邊際平均 17、15。$SSA=8,SSB=8,SSAB=8,SSE=24,SST=48$；df 為 1、1、1、4、7；三個效果的 MS 都是 8，$MSE=6$，所以三個 $F=1.333$、三個 $p=0.3125$，臨界值皆 7.709。
- **解讀結論：** A 主效果、B 主效果與交互作用均不顯著。

#### 計算題 37 <a id="exam-ch13-problem-37"></a>

##### 題目

> Ten observations from each of 3 populations. $SSTR=82.4$, $SSE=158.4$.
> a. Test at .05. b. If significant, determine which mean differs; $\bar{x}_1=24.8,\bar{x}_2=23.4,\bar{x}_3=27.4$.

##### 詳解

> **回看投影片講義：** [F](./course2-slides-handout.html#formula-anova-f)、[LSD 門檻](./course2-slides-handout.html#formula-anova-lsd-threshold)


- **辨認題型：** 整體 F 後做 Fisher LSD。**選方法：** [F](./course2-slides-handout.html#formula-anova-f)後接[LSD 門檻](./course2-slides-handout.html#formula-anova-lsd-threshold)。**檢查假設：** 三組獨立、近似常態、等變異；每組 $n=10$。
- **代入計算：** df $=(2,27)$；$MSTR=41.2,MSE=158.4/27=5.867,F=7.023$；$p=0.00350$，臨界值 3.354，整體顯著。$LSD=t_{.025,27}\sqrt{5.867(2/10)}=2.223$。差值 $|24.8-23.4|=1.4$ 不顯著；$|24.8-27.4|=2.6$、$|23.4-27.4|=4.0$ 顯著。
- **解讀結論：** 第 3 組平均數高於第 1、2 組；第 1、2 組間沒有足夠差異證據。

#### 計算題 38 <a id="exam-ch13-problem-38"></a>

##### 題目

> Three equal-size treatments. $SSTR=390.58$, $SSE=158.4$, $SST=548.98$, total df $=23$. Means are 17.000, 21.625, 26.875. Test at .05 and use Fisher LSD.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-anova-f)、[LSD](./course2-slides-handout.html#formula-anova-lsd-threshold)


- **辨認題型：** ANOVA + LSD。**選方法：** [整體 F](./course2-slides-handout.html#formula-anova-f)後接[LSD](./course2-slides-handout.html#formula-anova-lsd-threshold)。**檢查假設：** total $N=24$，故每組 $n=8$；獨立、常態、等變異。
- **代入計算：** df $=(2,21)$；$MSTR=195.29,MSE=7.543,F=25.891$；$p=2.15\times10^{-6}$，臨界值 3.467。$LSD=t_{.025,21}\sqrt{7.543(2/8)}=2.856$。三組差分為 4.625、5.25、9.875，全部大於 LSD。
- **解讀結論：** 三個母體平均數兩兩皆有顯著差異，順序為第 3 組 > 第 2 組 > 第 1 組。

#### 計算題 39 <a id="exam-ch13-problem-39"></a>

##### 題目

> Eight observations from each of 3 populations, $SSTR=216$, $SSE=252$. Test at .05.

##### 詳解

> **回看投影片講義：** [F 公式](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 由 SS 完成 F。**選方法：** [F 公式](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 三組獨立、近似常態、等變異。
- **代入計算：** $N=24$；df $=(2,21)$；$MSTR=108,MSE=12,F=9$。$F_{.05;2,21}=3.467$，$p=0.00150$。
- **解讀結論：** 拒絕 $H_0$；至少一母體平均數不同。

#### 計算題 40 <a id="exam-ch13-problem-40"></a>

##### 題目

> City I = 260, 280, 240, 260, 300; City II = 178, 190, 220, 240; City III = 211, 190, 250. Test at $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三城市不等樣本數平均時間。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 個人獨立、各城近似常態、等變異；觀察比較不能證明城市造成觀看時間差。
- **代入計算：** 組平均 268、207、217；grand mean 234.917。$SSTR=9552.917,SSE=6322,SST=15874.917$；df $=(2,9,11)$；$MSTR=4776.458,MSE=702.444,F=6.800$；$p=0.01587$，臨界值 4.256。
- **解讀結論：** 拒絕 $H_0$；至少一城市平均觀看時間不同。

#### 計算題 41 <a id="exam-ch13-problem-41"></a>

##### 題目

> Ten tires per brand. Mean mileage = 37, 38, 33; sample variances = 3, 4, 2. Test at 95% confidence.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三品牌摘要 ANOVA。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 輪胎獨立、品牌內近似常態、等變異。
- **代入計算：** 與 Problem 15 同一組數據，獨立重算仍得 $SSTR=140,SSE=81$；df $=(2,27)$；$MSTR=70,MSE=3,F=23.333$；$p=1.30\times10^{-6}$。
- **解讀結論：** 拒絕三品牌平均里程相等。題庫確實重複這組資料，仍依清冊收錄，沒有把它當排版殘留刪除。

#### 計算題 42 <a id="exam-ch13-problem-42"></a>

##### 題目

> Store 1 = 46, 47, 45, 42, 45; Store 2 = 34, 36, 35, 39; Store 3 = 33, 31, 35.
> a. Compute overall mean. b. Test at 95% confidence.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三店不等樣本數。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 銷售觀測獨立、各店近似常態、等變異。
- **代入計算：** 組平均 45、36、33；grand mean 39。$SSTR=324,SSE=36,SST=360$；df $=(2,9,11)$；$MSTR=162,MSE=4,F=40.5$；$p=3.16\times10^{-5}$，臨界值 4.256。
- **解讀結論：** 拒絕 $H_0$；至少一店平均銷售不同。

#### 計算題 43 <a id="exam-ch13-problem-43"></a>

##### 題目

> Four treatments, 11 units each. $SSTR=1,500$ and $SST=5,500$. Fill in the ANOVA table.

##### 詳解

> **回看投影片講義：** [SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)、[MS/F](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 完成平方和與 df。**選方法：** [SS 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)及[MS/F](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 完全隨機、獨立、常態、等變異。
- **代入計算：** $N=44,k=4$；$SSE=4000$。df 為 treatment 3、error 40、total 43；$MSTR=500,MSE=100,F=5$。
- **解讀結論：** 題目只要求填表；若另以 .05 檢定，$p=0.00488$，會拒絕平均數全部相等。

#### 計算題 44 <a id="exam-ch13-problem-44"></a>

##### 題目

> Sample 1 = 10, 13, 12, 13 (mean 12, variance 2.0); Sample 2 = 16, 14, 15 (mean 15, variance 1.0); Sample 3 = 15, 18 (mean 16.5, variance 4.5).
> a. Compute grand mean. b. Set up ANOVA. c. Test at 95% confidence using both approaches.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三組不等且很小的樣本。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 獨立、組內近似常態、等變異；因 $n$ 很小，常態與離群假設尤其重要，僅靠表格無法驗證。
- **代入計算：** 加權 grand mean $14$；$SSTR=31.5,SSE=12.5,SST=44$；df $=(2,6,8)$；$MSTR=15.75,MSE=2.083,F=7.56$。$F_{.05;2,6}=5.143$，$p=0.02293$。
- **解讀結論：** 拒絕 $H_0$；至少一母體平均數不同，但小樣本使模型診斷很重要。

#### 計算題 45 <a id="exam-ch13-problem-45"></a>

##### 題目

> Fourteen units for each of five treatments. The table gives $MSTR=800$ and $SST=10,600$; fill in all blanks.

##### 詳解

> **回看投影片講義：** [MS 與 SS/df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)


- **辨認題型：** 由 $k,n,MSTR,SST$ 反推表格。**選方法：** [MS 與 SS/df 分解](./course2-slides-handout.html#formula-anova-ss-decomposition)。**檢查假設：** 完全隨機、獨立、常態、等變異。原版數字後的問號是「待填空」排版記號，不是數值不確定。
- **代入計算：** $N=70$；df treatment $=4$、error $=65$、total $=69$。$SSTR=800\times4=3200$；$SSE=10600-3200=7400$；$MSE=7400/65=113.846$；$F=800/113.846=7.027$。
- **解讀結論：** 題目只要求填表；若以 .05 檢定，$p=9.15\times10^{-5}$，會拒絕全部平均數相等。

#### 計算題 46 <a id="exam-ch13-problem-46"></a>

##### 題目

> Tennessee = 12, 13, 17, 10, 18; Kentucky = 15, 19, 20; Texas = 16, 18.
> a. Compute grand mean. b. State hypotheses. c. Complete ANOVA. d. Find the 95% critical value and conclude. e. Determine p-value.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三州不等樣本數平均每日銷售。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 各日觀測獨立、各州近似常態、等變異；時間上若連續日期有相關，獨立假設可能不成立，原題未提供日期順序。
- **代入計算：** 組平均 14、18、17；grand mean 15.8。$SSTR=33.6,SSE=62,SST=95.6$；df $=(2,7,9)$；$MSTR=16.8,MSE=8.857,F=1.897$。$F_{.05;2,7}=4.737$，$p=0.2197$。
- **解讀結論：** 不拒絕 $H_0:\mu_{TN}=\mu_{KY}=\mu_{TX}$；沒有足夠證據顯示三州平均每日銷售不同。

#### 計算題 47 <a id="exam-ch13-problem-47"></a>

##### 題目

> Annual salaries (thousands of dollars):

| Specialty | Pediatrics | Radiology | Pathology |
| --- | ---: | ---: | ---: |
| Sample size | 12 | 10 | 11 |
| Average salary | 120 | 186 | 240 |
| Sample variance | 16 | 18 | 20 |

> a. Compute grand mean. b. State hypotheses. c. Complete ANOVA. d. Find the 95% critical value and conclude. e. Determine p-value.

##### 詳解

> **回看投影片講義：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)


- **辨認題型：** 三專科不等樣本數平均薪資。**選方法：** [單因子 ANOVA](./course2-slides-handout.html#formula-anova-f)。**檢查假設：** 醫師獨立、各專科薪資近似常態、等變異；摘要變異數相近，但原始分布仍無法由摘要檢查。
- **代入計算：** 加權 grand mean $180$。$SSTR=83160,SSE=538,SST=83698$；df $=(2,30,32)$；$MSTR=41580,MSE=17.933,F=2318.587$。$F_{.05;2,30}=3.316$，$p=1.32\times10^{-33}$。
- **解讀結論：** 拒絕 $H_0$；至少一專科平均薪資不同。F 極大來自組間平均差遠大於題給的組內變異，但仍不能只靠這題主張專科選擇造成薪資差。

<div class="page-break" style="page-break-after: always;"></div>

# 第 14 章：簡單線性迴歸｜考古題詳解

## 考古題詳解

本章收錄 146 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–15 題：模型、名稱、區間與假設

#### 選擇題 1 <a id="exam-ch14-mc-1"></a>

##### 題目

> In a regression analysis, the error term $\epsilon$ is a random variable with a mean or expected value of
>
> a. zero<br>
> b. one<br>
> c. any positive value<br>
> d. any value

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[母體模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 模型假設。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，回到[母體模型](./course2-slides-handout.html#formula-slr-model)的誤差中心。③ **檢查假設：** 題目問的是 $E(\epsilon)$，不是變異數。④ **代入計算／推理：** 平均線要滿足 $E(Y\mid X=x)=\beta_0+\beta_1x$，所以必須有 $E(\epsilon)=0$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確，誤差以 0 為中心；b 會把平均線整體抬高 1；c 沒有固定為正；d 會破壞平均線的定義。

#### 選擇題 2 <a id="exam-ch14-mc-2"></a>

##### 題目

> The coefficient of determination
>
> a. cannot be negative<br>
> b. is the square root of the coefficient of correlation<br>
> c. is the same as the coefficient of correlation<br>
> d. can be negative or positive

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$ 公式](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$ 範圍。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$ 公式](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 本章是含截距最小平迴歸。④ **代入計算／推理：** $R^2=SSR/SST=1-SSE/SST$，範圍是 $0$ 到 $1$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 把平方與開根號方向顛倒；c 混淆有方向的 $r$ 與無方向的 $R^2$；d 錯在 $R^2$ 不會為負。

#### 選擇題 3 <a id="exam-ch14-mc-3"></a>

##### 題目

> If the coefficient of determination is a positive value, then the coefficient of correlation
>
> a. must also be positive<br>
> b. must be zero<br>
> c. can be either negative or positive<br>
> d. must be larger than 1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 與 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 簡單迴歸含截距。④ **代入計算／推理：** $r=\operatorname{sign}(b_1)\sqrt{R^2}$，同一個正 $R^2$ 可配正斜率或負斜率。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a 忘了負斜率；b 只有 $R^2=0$ 才成立；c 正確；d 違反 $-1\le r\le1$。

#### 選擇題 4 <a id="exam-ch14-mc-4"></a>

##### 題目

> In regression analysis, the model in the form $y=\beta_0+\beta_1x+\epsilon$ is called
>
> a. regression equation<br>
> b. correlation equation<br>
> c. estimated regression equation<br>
> d. regression model

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[母體模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 名稱辨識。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)辨認含 $\epsilon$ 的[母體模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** $\beta_0,\beta_1$ 是母體參數。④ **代入計算／推理：** 含隨機誤差的是 regression model。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 通常指平均方程式；b 不是本章術語；c 應使用 $b_0,b_1$ 與 $\hat y$；d 正確。

#### 選擇題 5 <a id="exam-ch14-mc-5"></a>

##### 題目

> The mathematical equation relating the independent variable to the expected value of the dependent variable; that is, $E(y)=\beta_0+\beta_1x$, is known as
>
> a. regression equation<br>
> b. correlation equation<br>
> c. estimated regression equation<br>
> d. regression model

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[母體平均迴歸線](./course2-slides-handout.html#formula-slr-mean-line)


**五步詳解：** ① **辨認題型：** 母體平均線名稱。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[母體平均迴歸線](./course2-slides-handout.html#formula-slr-mean-line)。③ **檢查假設：** 式中沒有個體誤差 $\epsilon$。④ **代入計算／推理：** 它描述 $E(Y\mid X=x)$，名稱是 regression equation。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 相關沒有這種方程式；c 樣本式應為 $\hat y=b_0+b_1x$；d 完整模型還要有 $\epsilon$。

#### 選擇題 6 <a id="exam-ch14-mc-6"></a>

##### 題目

> The model developed from sample data that has the form of $\hat y=b_0+b_1x$ is known as
>
> a. regression equation<br>
> b. correlation equation<br>
> c. estimated regression equation<br>
> d. regression model

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計迴歸方程式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 樣本估計式名稱。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計迴歸方程式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** 題式用 $b_0,b_1$，不是未知的 $\beta_0,\beta_1$。④ **代入計算／推理：** 它由樣本建立，故是 estimated regression equation。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a 是母體平均式的名稱；b 非本章術語；c 正確；d 應含 $\epsilon$。

#### 選擇題 7 <a id="exam-ch14-mc-7"></a>

##### 題目

> In the following estimated regression equation $\hat y=b_0+b_1x$
>
> a. $b_1$ is the slope<br>
> b. $b_1$ is the intercept<br>
> c. $b_0$ is the slope<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距公式](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 係數角色。② **選方法：** 看[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率截距公式](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $x$ 前的係數控制每增加 1 單位的改變。④ **代入計算／推理：** $b_1$ 乘在 $x$ 前，所以是斜率。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b、c 把 $b_0,b_1$ 對調；d 因 a 正確而錯。

#### 選擇題 8 <a id="exam-ch14-mc-8"></a>

##### 題目

> In regression analysis, the unbiased estimate of the variance is
>
> a. coefficient of correlation<br>
> b. coefficient of determination<br>
> c. mean square error<br>
> d. slope of the regression equation

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)


**五步詳解：** ① **辨認題型：** 誤差變異估計。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$MSE$](./course2-slides-handout.html#formula-slr-mse)。③ **檢查假設：** 簡單迴歸估了兩個係數，誤差自由度是 $n-2$。④ **代入計算／推理：** $MSE=SSE/(n-2)$ 是 $\sigma^2$ 的不偏估計。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a、b 都無單位且描述關係；c 正確；d 是平均改變量，不是變異。

#### 選擇題 9 <a id="exam-ch14-mc-9"></a>

##### 題目

> The interval estimate of the mean value of $y$ for a given value of $x$ is
>
> a. prediction interval estimate<br>
> b. confidence interval estimate<br>
> c. average regression<br>
> d. x versus y correlation interval

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[平均反應 CI](./course2-slides-handout.html#formula-slr-mean-ci)


**五步詳解：** ① **辨認題型：** 平均反應或個體預測。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[平均反應 CI](./course2-slides-handout.html#formula-slr-mean-ci)。③ **檢查假設：** 主詞是 mean value。④ **代入計算／推理：** 母體平均位置用 confidence interval。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 用於單一新個體；b 正確；c、d 不是標準區間名稱。

#### 選擇題 10 <a id="exam-ch14-mc-10"></a>

##### 題目

> The interval estimate of an individual value of $y$ for a given value of $x$ is
>
> a. prediction interval estimate<br>
> b. confidence interval estimate<br>
> c. average regression<br>
> d. x versus y correlation interval

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[個別預測 PI](./course2-slides-handout.html#formula-slr-prediction-interval)


**五步詳解：** ① **辨認題型：** 單一個體區間。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[個別預測 PI](./course2-slides-handout.html#formula-slr-prediction-interval)。③ **檢查假設：** 主詞是 an individual value。④ **代入計算／推理：** 要納入新個體自身波動，故用 prediction interval。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 只估平均線；c、d 不是本章方法。

#### 選擇題 11 <a id="exam-ch14-mc-11"></a>

##### 題目

> The standard error is the
>
> a. $t$-statistic squared<br>
> b. square root of SSE<br>
> c. square root of SST<br>
> d. square root of MSE

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[標準估計誤差](./course2-slides-handout.html#formula-slr-standard-error)


**五步詳解：** ① **辨認題型：** 標準估計誤差。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[標準估計誤差](./course2-slides-handout.html#formula-slr-standard-error)。③ **檢查假設：** 要把變異單位平方開根號回到 $y$ 單位。④ **代入計算／推理：** $s=\sqrt{MSE}$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 無此關係；b 漏除自由度；c 是總變異；d 正確。

#### 選擇題 12 <a id="exam-ch14-mc-12"></a>

##### 題目

> If only MSE is known, you can compute the
>
> a. r square<br>
> b. coefficient of determination<br>
> c. standard error<br>
> d. all of these alternatives are correct

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$s=\sqrt{MSE}$](./course2-slides-handout.html#formula-slr-standard-error)


**五步詳解：** ① **辨認題型：** 已知量可推出什麼。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$s=\sqrt{MSE}$](./course2-slides-handout.html#formula-slr-standard-error)。③ **檢查假設：** 沒有 $SST$ 或 $SSR$。④ **代入計算／推理：** 只能直接算 $s$；$R^2$ 還需平方和。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a、b 都缺 $SST$；c 正確；d 因 a、b 不成立而錯。

#### 選擇題 13 <a id="exam-ch14-mc-13"></a>

##### 題目

> The value of the coefficient of correlation $(R)$
>
> a. can be equal to the value of the coefficient of determination $(R^2)$<br>
> b. can never be equal to the value of the coefficient of determination $(R^2)$<br>
> c. is always smaller than the value of the coefficient of determination<br>
> d. is always larger than the value of the coefficient of determination

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 與 $r^2$ 的特殊值。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 比較數值，不是在說兩個指標意義相同。④ **代入計算／推理：** 當 $r=0$ 或 $r=1$ 時，$r=r^2$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確，確實「可能」相等；b 忽略 0 與 1；c、d 都不是對所有 $r\in[-1,1]$ 成立。

#### 選擇題 14 <a id="exam-ch14-mc-14"></a>

##### 題目

> In a regression analysis the standard error is determined to be 4. In this situation the MSE
>
> a. is 2<br>
> b. is 16<br>
> c. depends on the sample size<br>
> d. depends on the degrees of freedom

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[標準估計誤差](./course2-slides-handout.html#formula-slr-standard-error)


**五步詳解：** ① **辨認題型：** $s$ 與 $MSE$ 互換。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[標準估計誤差](./course2-slides-handout.html#formula-slr-standard-error)。③ **檢查假設：** 已給 $s=4$。④ **代入計算／推理：** $MSE=s^2=4^2=16$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 誤把平方變成除 2；b 正確；c、d 在已知 $s$ 後不再需要。

#### 選擇題 15 <a id="exam-ch14-mc-15"></a>

##### 題目

> In regression analysis, which of the following is not a required assumption about the error term $\epsilon$?
>
> a. The expected value of the error term is one.<br>
> b. The variance of the error term is the same for all values of $X$.<br>
> c. The values of the error term are independent.<br>
> d. The error term is normally distributed.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[母體模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 找不屬於模型假設者。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[母體模型](./course2-slides-handout.html#formula-slr-model)旁的四項假設。③ **檢查假設：** 正確中心是 0。④ **代入計算／推理：** b、c、d 都是本章推論假設，a 把 0 寫成 1。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正是錯誤敘述；b 是等變異；c 是獨立性；d 是小樣本 $t/F$ 推論的常態性。

### 選擇題｜第 16–42 題：斜率、$r$、$R^2$ 與平方和

#### 選擇題 16 <a id="exam-ch14-mc-16"></a>

##### 題目

> A regression analysis between sales ($Y$ in $\$1000$) and advertising ($X$ in dollars) resulted in $\hat Y=30{,}000+4X$. The above equation implies that an
>
> a. increase of $\$4$ in advertising is associated with an increase of $\$4{,}000$ in sales<br>
> b. increase of $\$1$ in advertising is associated with an increase of $\$4$ in sales<br>
> c. increase of $\$1$ in advertising is associated with an increase of $\$34{,}000$ in sales<br>
> d. increase of $\$1$ in advertising is associated with an increase of $\$4{,}000$ in sales

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計迴歸式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 斜率與單位。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)讀[估計迴歸式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $Y$ 的 1 單位是 $\$1{,}000$，$X$ 的 1 單位是 $\$1$。④ **代入計算／推理：** $X$ 增 1，$\hat Y$ 增 4 個千美元，即 $\$4{,}000$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 把 $X$ 的增加量誤成 4；b 忘了 $Y$ 以千美元計；c 把截距也當成增量；d 正確。

#### 選擇題 17 <a id="exam-ch14-mc-17"></a>

##### 題目

> Regression analysis is a statistical procedure for developing a mathematical equation that describes how
>
> a. one independent and one or more dependent variables are related<br>
> b. several independent and several dependent variables are related<br>
> c. one dependent and one or more independent variables are related<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[母體模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 迴歸的角色。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[母體模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** 一個模型有一個依變數，可有一或多個自變數。④ **代入計算／推理：** c 符合簡單與複迴歸。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a、b 都把多個依變數混入本章架構；c 正確；d 因 c 正確而錯。

#### 選擇題 18 <a id="exam-ch14-mc-18"></a>

##### 題目

> In a simple regression analysis (where $Y$ is dependent and $X$ independent), if the $Y$ intercept is positive, then
>
> a. there is a positive correlation between $X$ and $Y$<br>
> b. if $X$ is increased, $Y$ must also increase<br>
> c. if $Y$ is increased, $X$ must also increase<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距不代表方向。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** 正截距只說 $x=0$ 時的估計值。④ **代入計算／推理：** 關係方向由 $b_1$ 決定，題目沒給。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b 都把截距誤當斜率；c 還把預測方向倒轉；d 正確。

#### 選擇題 19 <a id="exam-ch14-mc-19"></a>

##### 題目

> In regression analysis, the variable that is being predicted is the
>
> a. dependent variable<br>
> b. independent variable<br>
> c. intervening variable<br>
> d. is usually $x$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[迴歸模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 變數角色。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[迴歸模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** 本章以 $x$ 解釋或預測 $y$。④ **代入計算／推理：** 被預測的是 dependent variable $Y$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 是預測者；c 非本章角色；d $x$ 通常是自變數。

#### 選擇題 20 <a id="exam-ch14-mc-20"></a>

##### 題目

> The equation that describes how the dependent variable $(y)$ is related to the independent variable $(x)$ is called
>
> a. the correlation model<br>
> b. the regression model<br>
> c. correlation analysis<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[迴歸模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 模型名稱。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)看[迴歸模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** 題目問 equation/model，不是強度指標。④ **代入計算／推理：** 描述 $Y$ 如何隨 $X$ 改變的是 regression model。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、c 是相關術語且不產生預測式；b 正確；d 因 b 正確而錯。

#### 選擇題 21 <a id="exam-ch14-mc-21"></a>

##### 題目

> In regression analysis, the independent variable is
>
> a. used to predict other independent variables<br>
> b. used to predict the dependent variable<br>
> c. called the intervening variable<br>
> d. the variable that is being predicted

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計迴歸式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 自變數角色。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計迴歸式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** 式中把 $x$ 代入以取得 $\hat y$。④ **代入計算／推理：** independent variable 用來預測 dependent variable。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、c 非定義；b 正確；d 描述的是 $Y$。

#### 選擇題 22 <a id="exam-ch14-mc-22"></a>

##### 題目

> Larger values of $r^2$ imply that the observations are more closely grouped about the
>
> a. average value of the independent variables<br>
> b. average value of the dependent variable<br>
> c. least squares line<br>
> d. origin

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 配適程度。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 同一資料的 $SST$ 固定。④ **代入計算／推理：** $R^2$ 越大代表 $SSE/SST$ 越小，點越貼近最小平線。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a、b 是平均值而非整條線；c 正確；d 原點沒有必然角色。

#### 選擇題 23 <a id="exam-ch14-mc-23"></a>

##### 題目

> In a regression analysis, the coefficient of determination is $0.4225$. The coefficient of correlation in this situation is
>
> a. $0.65$<br>
> b. $0.1785$<br>
> c. any positive value<br>
> d. any value

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 由 $R^2$ 求 $r$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 題目未提供斜率方向。④ **代入計算／推理：** $|r|=\sqrt{0.4225}=0.65$，所以 $r=+0.65$ 或 $-0.65$。⑤ **解讀結論：** **原題沒有完整正確選項** ；若另知斜率為正才可選 a。

**選項逐一：** a 只涵蓋正斜率；b 是把 $0.4225$ 再平方；c 不可任取正值；d「任何值」太廣，真正只有 $\pm0.65$。

#### 選擇題 24 <a id="exam-ch14-mc-24"></a>

##### 題目

> In a regression analysis, the coefficient of correlation is $0.16$. The coefficient of determination is
>
> a. $0.4000$<br>
> b. $0.0256$<br>
> c. $4$<br>
> d. $2.56$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 轉 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數關係式](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 簡單迴歸含截距。④ **代入計算／推理：** $R^2=r^2=0.16^2=0.0256$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 是錯誤開根號；b 正確；c、d 超過 1 或小數點錯位。

#### 選擇題 25 <a id="exam-ch14-mc-25"></a>

##### 題目

> In simple linear regression analysis, which of the following is not true?
>
> a. The $F$ test and the $t$ test yield the same conclusion.<br>
> b. The $F$ test and the $t$ test may or may not yield the same conclusion.<br>
> c. The relationship between $X$ and $Y$ is represented by means of a straight line.<br>
> d. The value of $F=t^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)、[迴歸 $F$](./course2-slides-handout.html#formula-slr-f-test)


**五步詳解：** ① **辨認題型：** 簡單迴歸 $t/F$ 等價。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)與[迴歸 $F$](./course2-slides-handout.html#formula-slr-f-test)。③ **檢查假設：** 只有一個斜率且檢定同一個 $H_0$。④ **代入計算／推理：** 此時 $F=t^2$，所以結論相同。⑤ **解讀結論：** 不正確的是 **b** 。

**選項逐一：** a、d 是等價性的結果；b 錯；c 是簡單「線性」迴歸的模型形式。

#### 選擇題 26 <a id="exam-ch14-mc-26"></a>

##### 題目

> Correlation analysis is used to determine
>
> a. the equation of the regression line<br>
> b. the strength of the relationship between the dependent and the independent variables<br>
> c. a specific value of the dependent variable for a given value of the independent variable<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 相關與迴歸用途。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 問的是 correlation analysis。④ **代入計算／推理：** $r$ 摘要線性方向與強度。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、c 是迴歸估計用途；b 正確；d 因 b 正確而錯。

#### 選擇題 27 <a id="exam-ch14-mc-27"></a>

##### 題目

> In a regression and correlation analysis if $r^2=1$, then
>
> a. SSE must also be equal to one<br>
> b. SSE must be equal to zero<br>
> c. SSE can be any positive value<br>
> d. SSE must be negative

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2=1-SSE/SST$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 完全配適。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2=1-SSE/SST$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $SST>0$。④ **代入計算／推理：** $1=1-SSE/SST$，故 $SSE=0$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、c 不符合完全配適；b 正確；d 平方和不會負。

#### 選擇題 28 <a id="exam-ch14-mc-28"></a>

##### 題目

> In a regression and correlation analysis if $r^2=1$, then
>
> a. $SSE=SST$<br>
> b. $SSE=1$<br>
> c. $SSR=SSE$<br>
> d. $SSR=SST$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$SST=SSR+SSE$](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 平方和分解。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$SST=SSR+SSE$](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** $r^2=1$ 使 $SSE=0$。④ **代入計算／推理：** 因此全部總變異都由迴歸解釋，$SSR=SST$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 反而對應 $R^2=0$；b 無根據；c 只有兩者都 0 的退化情況；d 正確。

#### 選擇題 29 <a id="exam-ch14-mc-29"></a>

##### 題目

> The regression equation is $y=12-6x$. If $SSE=510$ and $SST=1000$, then the coefficient of correlation is
>
> a. $-0.7$<br>
> b. $+0.7$<br>
> c. $0.49$<br>
> d. $-0.49$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 平方和與斜率決定 $r$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)及[$r$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率 $-6$ 提供負號。④ **代入計算／推理：** $R^2=1-510/1000=0.49$，故 $r=-\sqrt{0.49}=-0.7$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 忘了負斜率；c、d 是 $R^2$ 而非 $r$。

#### 選擇題 30 <a id="exam-ch14-mc-30"></a>

##### 題目

> If $SSE=200$ and $SSR=300$, then the coefficient of determination is
>
> a. $0.6667$<br>
> b. $0.6000$<br>
> c. $0.4000$<br>
> d. $1.5000$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 由兩平方和求 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** $SST=SSR+SSE$。④ **代入計算／推理：** $R^2=300/(300+200)=0.6000$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 用錯分母；b 正確；c 是未解釋比例；d 以 $SSR/SSE$ 錯算且超過 1。

#### 選擇題 31 <a id="exam-ch14-mc-31"></a>

##### 題目

> If the coefficient of determination is equal to 1, then the coefficient of correlation
>
> a. must also be equal to 1<br>
> b. can be either $-1$ or $+1$<br>
> c. can be any value between $-1$ to $+1$<br>
> d. must be $-1$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $R^2=1$ 的符號。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 未知斜率方向。④ **代入計算／推理：** $|r|=1$，正負由斜率決定。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、d 各只涵蓋一個方向；b 正確；c 不是任意值。

#### 選擇題 32 <a id="exam-ch14-mc-32"></a>

##### 題目

> In a regression analysis, the variable that is being predicted
>
> a. must have the same units as the variable doing the predicting<br>
> b. is the independent variable<br>
> c. is the dependent variable<br>
> d. usually is denoted by $x$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 變數角色與單位。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** $X,Y$ 可有不同單位。④ **代入計算／推理：** 被預測的是 $Y$，即依變數。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a 沒有同單位要求；b、d 描述 $X$；c 正確。

#### 選擇題 33 <a id="exam-ch14-mc-33"></a>

##### 題目

> Demand $(Y)$ and price $(X)$ have estimated equation $\hat Y=120-10X$. If price is increased by 2 units, demand is expected to
>
> a. increase by 120 units<br>
> b. increase by 100 units<br>
> c. increase by 20 units<br>
> d. decease by 20 units

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 斜率乘改變量。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** 改變量是 $\Delta X=2$，截距不參與差值。④ **代入計算／推理：** $\Delta\hat Y=-10(2)=-20$。⑤ **解讀結論：** 答案是 **d** ；原文 `decease` 應理解為 `decrease`。

**選項逐一：** a 把截距當改變量；b 混合截距與斜率；c 符號錯；d 數值與方向正確。

#### 選擇題 34 <a id="exam-ch14-mc-34"></a>

##### 題目

> The coefficient of correlation
>
> a. is the square of the coefficient of determination<br>
> b. is the square root of the coefficient of determination<br>
> c. is the same as r-square<br>
> d. can never be negative

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$r=\operatorname{sign}(b_1)\sqrt{R^2}$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 與 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$r=\operatorname{sign}(b_1)\sqrt{R^2}$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 必須保留斜率符號。④ **代入計算／推理：** 最接近的是 b，但嚴格說應是「帶斜率符號的平方根」。⑤ **解讀結論：** 依選項取 **b** ，並補上符號限制。

**選項逐一：** a 次方方向錯；b 是最接近正解但漏寫 $\pm$；c 混淆兩指標；d 負相關時 $r<0$。

#### 選擇題 35 <a id="exam-ch14-mc-35"></a>

##### 題目

> If the coefficient of correlation is a positive value, then the regression equation
>
> a. must have a positive slope<br>
> b. must have a negative slope<br>
> c. could have either a positive or a negative slope<br>
> d. must have a positive $y$ intercept

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 與斜率同號。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 簡單迴歸含截距。④ **代入計算／推理：** $r>0$ 代表 $b_1>0$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b、c 違反同號關係；d 截距與相關方向無關。

#### 選擇題 36 <a id="exam-ch14-mc-36"></a>

##### 題目

> If the coefficient of correlation is $0.8$, the percentage of variation in the dependent variable explained by the independent variable is
>
> a. $0.80\%$<br>
> b. $80\%$<br>
> c. $0.64\%$<br>
> d. $64\%$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $r$ 轉解釋百分比。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 百分比要把比例乘 100%。④ **代入計算／推理：** $R^2=0.8^2=0.64=64\%$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、c 小數與百分比錯位；b 忘了平方；d 正確。

#### 選擇題 37 <a id="exam-ch14-mc-37"></a>

##### 題目

> If SSE and SST are known, then with this information the
>
> a. coefficient of determination can be computed<br>
> b. slope of the line can be computed<br>
> c. Y intercept can be computed<br>
> d. x intercept can be computed

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2=1-SSE/SST$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 平方和可推出的量。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2=1-SSE/SST$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 沒有 $x,y$ 平均或交叉乘積。④ **代入計算／推理：** 可直接算 $R^2$，不能算線的位置。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b、c、d 都需要更多資料。

#### 選擇題 38 <a id="exam-ch14-mc-38"></a>

##### 題目

> If the independent variable is measured in pounds, the dependent variable
>
> a. must also be in pounds<br>
> b. must be in some unit of weight<br>
> c. cannot be in pounds<br>
> d. can be any units

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[模型符號表](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 變數單位。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[模型符號表](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** 迴歸只要求兩者是可解讀的數值變數。④ **代入計算／推理：** $Y$ 可是成本、時間或其他單位；斜率會帶 $Y/X$ 單位。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b 加入不存在的限制；c 也不對；d 正確。

#### 選擇題 39 <a id="exam-ch14-mc-39"></a>

##### 題目

> If there is a very weak correlation between two variables, then the coefficient of determination must be
>
> a. much larger than 1, if the correlation is positive<br>
> b. much smaller than $-1$, if the correlation is negative<br>
> c. much larger than one<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 弱相關的 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** $0\le R^2\le1$。④ **代入計算／推理：** 弱相關使 $|r|$ 小、$R^2$ 接近 0，不會超過 1 或為負。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b、c 都違反 $R^2$ 範圍；d 正確。

#### 選擇題 40 <a id="exam-ch14-mc-40"></a>

##### 題目

> SSE can never be
>
> a. larger than SST<br>
> b. smaller than SST<br>
> c. equal to 1<br>
> d. equal to zero

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 平方和範圍。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** 本章含截距最小平迴歸。④ **代入計算／推理：** $SST=SSR+SSE$ 且 $SSR\ge0$，所以 $SSE\le SST$。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 常可發生；c 取決於量尺；d 完全配適時可發生。

#### 選擇題 41 <a id="exam-ch14-mc-41"></a>

##### 題目

> If the coefficient of correlation is $-0.4$, then the slope of the regression line
>
> a. must also be $-0.4$<br>
> b. can be either negative or positive<br>
> c. must be negative<br>
> d. must be $0.16$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 相關與斜率符號。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 同號不代表同數值。④ **代入計算／推理：** $r<0$ 必有 $b_1<0$，但斜率大小受單位影響。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a 把無單位 $r$ 當斜率；b 符號不是任意；c 正確；d 是 $r^2$。

#### 選擇題 42 <a id="exam-ch14-mc-42"></a>

##### 題目

> If the coefficient of correlation is a negative value, then the coefficient of determination
>
> a. must also be negative<br>
> b. must be zero<br>
> c. can be either negative or positive<br>
> d. must be positive

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2=r^2$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 負相關平方。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2=r^2$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 題目說 negative value，故 $r\ne0$。④ **代入計算／推理：** 負數平方為正，因此 $R^2>0$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、c 忘了平方不負；b 只在 $r=0$；d 正確。

### 選擇題｜第 43–63 題：解讀、單位與點預測

#### 選擇題 43 <a id="exam-ch14-mc-43"></a>

##### 題目

> It is possible for the coefficient of determination to be
>
> a. larger than 1<br>
> b. less than one<br>
> c. less than $-1$<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$ 範圍。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 本章含截距。④ **代入計算／推理：** $0\le R^2\le1$，所以可能小於 1。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、c 超出範圍；b 正確；d 因 b 正確而錯。

#### 選擇題 44 <a id="exam-ch14-mc-44"></a>

##### 題目

> If two variables, $x$ and $y$, have a strong linear relationship, then
>
> a. there may or may not be any causal relationship between $x$ and $y$<br>
> b. $x$ causes $y$ to happen<br>
> c. $y$ causes $x$ to happen<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 關聯與因果。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)回到[模型](./course2-slides-handout.html#formula-slr-model)的解讀限制。③ **檢查假設：** 只知道觀察到強線性關係，沒有隨機實驗或因果設計。④ **代入計算／推理：** 強相關可能有因果，也可能由混淆因素造成。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b、c 都把方向性關聯誤當因果；d 因 a 正確而錯。

#### 選擇題 45 <a id="exam-ch14-mc-45"></a>

##### 題目

> If the coefficient of determination is $0.81$, the coefficient of correlation
>
> a. is $0.6561$<br>
> b. could be either $+0.9$ or $-0.9$<br>
> c. must be positive<br>
> d. must be negative

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 由 $R^2$ 求 $r$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 未給斜率方向。④ **代入計算／推理：** $|r|=\sqrt{0.81}=0.9$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 把 0.81 再平方；b 正確；c、d 都只給一種方向。

#### 選擇題 46 <a id="exam-ch14-mc-46"></a>

##### 題目

> A least squares regression line
>
> a. may be used to predict a value of $y$ if the corresponding $x$ value is given<br>
> b. implies a cause-effect relationship between $x$ and $y$<br>
> c. can only be determined if a good linear relationship exists between $x$ and $y$<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 最小平線用途。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** 預測仍應檢查線性與資料範圍。④ **代入計算／推理：** 給 $x$ 可代入求 $\hat y$；計算一條線本身不證明因果，也不要求關係先「很好」。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 把關聯當因果；c 即使配適差仍能算線，只是不宜使用；d 因 a 正確而錯。

#### 選擇題 47 <a id="exam-ch14-mc-47"></a>

##### 題目

> If all the points of a scatter diagram lie on the least squares regression line, then the coefficient of determination is
>
> a. $0$<br>
> b. $1$<br>
> c. either $1$ or $-1$, depending upon whether the relationship is positive or negative<br>
> d. could be any value between $-1$ and $1$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 完全配適。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 所有殘差為 0。④ **代入計算／推理：** $SSE=0$，所以 $R^2=1$；$R^2$ 沒有負號。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 是無解釋力；b 正確；c 把 $r$ 的符號套到 $R^2$；d 不是任意值。

#### 選擇題 48 <a id="exam-ch14-mc-48"></a>

##### 題目

> If a data set has $SSR=400$ and $SSE=100$, then the coefficient of determination is
>
> a. $0.10$<br>
> b. $0.25$<br>
> c. $0.40$<br>
> d. $0.80$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 平方和求 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** $SST=400+100=500$。④ **代入計算／推理：** $R^2=400/500=0.80$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b、c 是錯誤分母或比例；d 正確。

#### 選擇題 49 <a id="exam-ch14-mc-49"></a>

##### 題目

> Compared to the confidence interval estimate for a particular value of $y$, the interval estimate for an average value of $y$ will be
>
> a. narrower<br>
> b. wider<br>
> c. the same<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)、[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)


**五步詳解：** ① **辨認題型：** 平均 CI 與個別 PI。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)與[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)。③ **檢查假設：** 相同 $x^*$ 與信心水準。④ **代入計算／推理：** 個別 PI 根號內多一個 $1$，所以平均 CI 較窄。⑤ **解讀結論：** 答案是 **a** 。

**選項逐一：** a 正確；b 方向相反；c 忽略個體誤差；d 因 a 正確而錯。

#### 選擇題 50 <a id="exam-ch14-mc-50"></a>

##### 題目

> Sales are measured in $\$1000$ and price in dollars. The equation is $\hat Y=60-8X$. It implies that an
>
> a. increase of $\$1$ in price is associated with a decrease of $\$8$ in sales<br>
> b. increase of $\$8$ in price is associated with a decrease of $\$52{,}000$ in sales<br>
> c. increase of $\$1$ in price is associated with a decrease of $\$52$ in sales<br>
> d. increase of $\$1$ in price is associated with a decrease of $\$8000$ in sales

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 斜率單位。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $Y$ 一單位是 $\$1{,}000$。④ **代入計算／推理：** $X$ 增 $\$1$，$\hat Y$ 減 8 千美元。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 忘了千美元；b、c 錯把截距混入；d 正確。

#### 選擇題 51 <a id="exam-ch14-mc-51"></a>

##### 題目

> If $SST=500$ and $SSE=300$, then the coefficient of determination is
>
> a. $0.20$<br>
> b. $1.67$<br>
> c. $0.60$<br>
> d. $0.40$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $SST,SSE$ 求 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $SSE\le SST$。④ **代入計算／推理：** $R^2=1-300/500=0.40$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 算錯差額；b 超過範圍；c 是未解釋比例；d 正確。

#### 選擇題 52 <a id="exam-ch14-mc-52"></a>

##### 題目

> Sales are in $\$1000$, advertising is in $\$100$, and $\hat Y=500+4X$. If advertising is $\$10{,}000$, the point estimate for sales in dollars is
>
> a. $\$900$<br>
> b. $\$900{,}000$<br>
> c. $\$40{,}500$<br>
> d. $\$505{,}000$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 尺度換算後點預測。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $X=10{,}000/100=100$。④ **代入計算／推理：** $\hat Y=500+4(100)=900$ 千美元，即 $\$900{,}000$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 忘了 $Y$ 的千倍；b 正確；c、d 代入或單位錯。

#### 選擇題 53 <a id="exam-ch14-mc-53"></a>

##### 題目

> The coefficient of correlation
>
> a. is the square of the coefficient of determination<br>
> b. is the square root of the coefficient of determination<br>
> c. is the same as r-square<br>
> d. can never be negative

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 與第 34 題同型。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 要保留斜率正負。④ **代入計算／推理：** $r=\operatorname{sign}(b_1)\sqrt{R^2}$。⑤ **解讀結論：** 依選項取 **b** ，但原句漏了符號。

**選項逐一：** a 次方方向錯；b 最接近；c 混淆 $r$ 與 $R^2$；d 負相關可為負。

#### 選擇題 54 <a id="exam-ch14-mc-54"></a>

##### 題目

> If the coefficient of correlation is $0.4$, the percentage of variation explained is
>
> a. $40\%$<br>
> b. $16\%$<br>
> c. $4\%$<br>
> d. can be any positive value

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $r$ 轉百分比。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 解釋比例為 $r^2$。④ **代入計算／推理：** $0.4^2=0.16=16\%$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 忘了平方；b 正確；c 小數點錯；d 不是任意值。

#### 選擇題 55 <a id="exam-ch14-mc-55"></a>

##### 題目

> If the dependent variable is measured in dollars, the independent variable
>
> a. must also be in dollars<br>
> b. must be in some units of currency<br>
> c. can be any units<br>
> d. cannot be in dollars

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[模型](./course2-slides-handout.html#formula-slr-model)


**五步詳解：** ① **辨認題型：** 單位限制。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[模型](./course2-slides-handout.html#formula-slr-model)。③ **檢查假設：** 只要變數與斜率有合理情境解讀。④ **代入計算／推理：** $X$ 可以是人口、時間或金額。⑤ **解讀結論：** 答案是 **c** 。

**選項逐一：** a、b 限制過度；c 正確；d 也可能同為美元。

#### 選擇題 56 <a id="exam-ch14-mc-56"></a>

##### 題目

> If there is a very strong correlation between two variables then the coefficient of determination must be
>
> a. much larger than 1, if the correlation is positive<br>
> b. much smaller than $-1$, if the correlation is negative<br>
> c. any value larger than 1<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 強相關下 $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** $R^2$ 範圍仍是 $[0,1]$。④ **代入計算／推理：** 強相關使 $R^2$ 接近 1，而不是超過 1 或為負。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b、c 都違反範圍；d 正確。

#### 選擇題 57 <a id="exam-ch14-mc-57"></a>

##### 題目

> If the coefficient of correlation is $0.90$, then the coefficient of determination
>
> a. is also $0.9$<br>
> b. is either $0.81$ or $-0.81$<br>
> c. can be either negative or positive<br>
> d. must be $0.81$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 平方關係。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $R^2$ 不帶方向。④ **代入計算／推理：** $0.90^2=0.81$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 忘了平方；b、c 讓 $R^2$ 為負；d 正確。

#### 選擇題 58 <a id="exam-ch14-mc-58"></a>

##### 題目

> Demand is in 1000 units, price is in dollars, and $\hat Y=9-3X$. If price increases by $\$1$, demand is expected to
>
> a. increase by 6 units<br>
> b. decrease by 3 units<br>
> c. decrease by 6,000 units<br>
> d. decrease by 3,000 units

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 斜率單位。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $Y$ 一單位是 1,000 units。④ **代入計算／推理：** $\Delta\hat Y=-3$ 千單位，即減少 3,000。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 符號與截距皆誤用；b 忘了千倍；c 大小錯；d 正確。

#### 選擇題 59 <a id="exam-ch14-mc-59"></a>

##### 題目

> If $SST=4500$ and $SSE=1575$, then the coefficient of determination is
>
> a. $0.35$<br>
> b. $0.65$<br>
> c. $2.85$<br>
> d. $0.45$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $SSE/SST=1575/4500=0.35$。④ **代入計算／推理：** $R^2=1-0.35=0.65$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a 是未解釋比例；b 正確；c 超過 1；d 算術錯。

#### 選擇題 60 <a id="exam-ch14-mc-60"></a>

##### 題目

> Sales are in $\$10{,}000$, advertising is in $\$100$, and $\hat Y=50+8X$. If advertising is $\$1{,}000$, the point estimate for sales in dollars is
>
> a. $\$8{,}050$<br>
> b. $\$130$<br>
> c. $\$130{,}000$<br>
> d. $\$1{,}300{,}000$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 雙重尺度換算。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $X=1000/100=10$。④ **代入計算／推理：** $\hat Y=50+8(10)=130$ 個 $\$10{,}000$，即 $\$1{,}300{,}000$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 直接混用美元；b 忘記換回美元；c 少一個 10 倍；d 正確。

#### 選擇題 61 <a id="exam-ch14-mc-61"></a>

##### 題目

> If the coefficient of correlation is a positive value, then
>
> a. the intercept must also be positive<br>
> b. the coefficient of determination can be either negative or positive, depending on the value of the slope<br>
> c. the regression equation could have either a positive or a negative slope<br>
> d. the slope of the line must be positive

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$ 與斜率同號。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** PDF 的題幹符號在文字層遺失；逐頁畫面顯示空格後接 `is a positive value`，依選項脈絡應為 correlation coefficient。④ **代入計算／推理：** $r>0$ 必有 $b_1>0$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a 截距無關；b $R^2$ 不負；c 違反同號；d 正確。

#### 選擇題 62 <a id="exam-ch14-mc-62"></a>

##### 題目

> If the coefficient of determination is $0.9$, the percentage of variation in the dependent variable explained by the independent variable
>
> a. is $0.90\%$<br>
> b. is $90\%$<br>
> c. is $81\%$<br>
> d. $0.81\%$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$ 解讀](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 比例轉百分比。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$ 解讀](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 已給的是 $R^2$，不用再平方。④ **代入計算／推理：** $0.9\times100\%=90\%$。⑤ **解讀結論：** 答案是 **b** 。

**選項逐一：** a、d 小數百分比錯；b 正確；c 不應再平方。

#### 選擇題 63 <a id="exam-ch14-mc-63"></a>

##### 題目

> Sales are in $\$1{,}000$, advertising is in $\$100$, and $\hat Y=80+6.2X$. If advertising is $\$10{,}000$, the point estimate for sales in dollars is
>
> a. $\$62{,}080$<br>
> b. $\$142{,}000$<br>
> c. $\$700$<br>
> d. $\$700{,}000$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 點預測與單位。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $X=10{,}000/100=100$。④ **代入計算／推理：** $\hat Y=80+6.2(100)=700$ 千美元，即 $\$700{,}000$。⑤ **解讀結論：** 答案是 **d** 。

**選項逐一：** a、b 代入錯；c 忘了 $Y$ 的千倍；d 正確。

### 選擇題｜第 64–82 題：題組 14-1 至 14-4

#### 題組 14-1：選擇題 64–68 共用資料

> The following information regarding a dependent variable $(Y)$ and an independent variable $(X)$ is provided.

| $Y$ | $X$ |
|---:|---:|
| 4 | 2 |
| 3 | 1 |
| 4 | 4 |
| 6 | 3 |
| 8 | 5 |

> $SSE=6$, $SST=16$.

獨立驗算得到 $\bar x=3$、$\bar y=5$、$S_{xx}=10$、$S_{xy}=10$，所以 $b_1=1$、$b_0=2$、$R^2=1-6/16=0.625$、$r=+0.7906$、$MSE=6/(5-2)=2$。

#### 選擇題 64 <a id="exam-ch14-mc-64"></a>

##### 題目

> Refer to Exhibit 14-1. The least squares estimate of the $Y$ intercept is<br>
> a. 1　b. 2　c. 3　d. 4

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $x$ 有變異。④ **代入計算／推理：** $b_0=\bar y-b_1\bar x=5-1(3)=2$。⑤ **解讀結論：** **b** 。

**選項逐一：** a、c、d 都不滿足樣本平均點 $(3,5)$；b 正確。

#### 選擇題 65 <a id="exam-ch14-mc-65"></a>

##### 題目

> Refer to Exhibit 14-1. The least squares estimate of the slope is<br>
> a. 1　b. 2　c. 3　d. 4

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率公式](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率公式](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $S_{xx}=10>0$。④ **代入計算／推理：** $b_1=S_{xy}/S_{xx}=10/10=1$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b、c、d 都不是交叉乘積除以 $S_{xx}$。

#### 選擇題 66 <a id="exam-ch14-mc-66"></a>

##### 題目

> Refer to Exhibit 14-1. The coefficient of determination is<br>
> a. 0.7096　b. -0.7906　c. 0.625　d. 0.375

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 已知 $SSE,SST$。④ **代入計算／推理：** $R^2=1-6/16=0.625$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 數值無來源；b $R^2$ 不負且該數是 $r$ 的量級；c 正確；d 是未解釋比例。

#### 選擇題 67 <a id="exam-ch14-mc-67"></a>

##### 題目

> Refer to Exhibit 14-1. The coefficient of correlation is<br>
> a. 0.7906　b. -0.7906　c. 0.625　d. 0.375

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率為正。④ **代入計算／推理：** $r=+\sqrt{0.625}=0.7906$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c 是 $R^2$；d 是未解釋比例。

#### 選擇題 68 <a id="exam-ch14-mc-68"></a>

##### 題目

> Refer to Exhibit 14-1. The MSE is<br>
> a. 1　b. 2　c. 3　d. 4

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)


**五步詳解：** ① **辨認題型：** $MSE$。② **選方法：** 用[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$MSE$](./course2-slides-handout.html#formula-slr-mse)。③ **檢查假設：** $n=5$，自由度 $3$。④ **代入計算／推理：** $MSE=6/3=2$。⑤ **解讀結論：** **b** 。

**選項逐一：** a、c、d 分母不對；b 正確。

#### 題組 14-2：選擇題 69–73 共用資料

> You are given the following information about $y$ and $x$.

| $y$ (dependent) | $x$ (independent) |
|---:|---:|
| 5 | 1 |
| 4 | 2 |
| 3 | 3 |
| 2 | 4 |
| 1 | 5 |

五點完全落在 $\hat y=6-x$ 上，所以 $b_1=-1$、$b_0=6$、$r=-1$、$R^2=1$。

#### 選擇題 69 <a id="exam-ch14-mc-69"></a>

##### 題目

> Refer to Exhibit 14-2. The least squares estimate of $b_1$ (slope) equals<br>
> a. 1　b. -1　c. 6　d. 5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** 每當 $x$ 增 1，$y$ 減 1。④ **代入計算／推理：** $b_1=-1$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 符號錯；b 正確；c 是截距；d 是資料值。

#### 選擇題 70 <a id="exam-ch14-mc-70"></a>

##### 題目

> Refer to Exhibit 14-2. The least squares estimate of $b_0$ (intercept) equals<br>
> a. 1　b. -1　c. 6　d. 5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=\bar y=3$。④ **代入計算／推理：** $b_0=3-(-1)(3)=6$。⑤ **解讀結論：** **c** 。

**選項逐一：** a、b 是斜率候選；c 正確；d 只是最大 $y$。

#### 選擇題 71 <a id="exam-ch14-mc-71"></a>

##### 題目

> Refer to Exhibit 14-2. The point estimate of $y$ when $x=10$ is<br>
> a. -10　b. 10　c. -4　d. 4

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 點預測。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $x=10$ 遠超出觀察範圍 1–5，是危險外插。④ **代入計算／推理：** $\hat y=6-10=-4$。⑤ **解讀結論：** 算術答案 **c** ，實務上不可把外插當可靠預測。

**選項逐一：** a 忘了截距；b、d 符號或代入錯；c 正確算值。

#### 選擇題 72 <a id="exam-ch14-mc-72"></a>

##### 題目

> Refer to Exhibit 14-2. The sample correlation coefficient equals<br>
> a. 0　b. +1　c. -1　d. -0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 完全負線性。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 所有點在負斜率直線。④ **代入計算／推理：** $r=-1$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 無線性；b 方向錯；c 正確；d 強度不足。

#### 選擇題 73 <a id="exam-ch14-mc-73"></a>

##### 題目

> Refer to Exhibit 14-2. The coefficient of determination equals<br>
> a. 0　b. -1　c. +1　d. -0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $SSE=0$。④ **代入計算／推理：** $R^2=(-1)^2=1$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 非完全配適；b、d 不可能為負；c 正確。

#### 題組 14-3：選擇題 74–77 共用資料

| $y$ (dependent) | $x$ (independent) |
|---:|---:|
| 12 | 4 |
| 3 | 6 |
| 7 | 2 |
| 6 | 4 |

獨立驗算：$\bar x=4$、$\bar y=7$、$S_{xx}=8$、$S_{xy}=-8$、$S_{yy}=42$，故 $b_1=-1$、$b_0=11$、$r=-0.4364$、$R^2=0.1905$。

#### 選擇題 74 <a id="exam-ch14-mc-74"></a>

##### 題目

> Refer to Exhibit 14-3. The least squares estimate of $b_1$ equals<br>
> a. 1　b. -1　c. -11　d. 11

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $S_{xx}=8$。④ **代入計算／推理：** $b_1=-8/8=-1$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 符號錯；b 正確；c、d 把截距大小混入。

#### 選擇題 75 <a id="exam-ch14-mc-75"></a>

##### 題目

> Refer to Exhibit 14-3. The least squares estimate of $b_0$ equals<br>
> a. 1　b. -1　c. -11　d. 11

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=4,\bar y=7$。④ **代入計算／推理：** $b_0=7-(-1)(4)=11$。⑤ **解讀結論：** **d** 。

**選項逐一：** a、b 是斜率候選；c 符號錯；d 正確。

#### 選擇題 76 <a id="exam-ch14-mc-76"></a>

##### 題目

> Refer to Exhibit 14-3. The sample correlation coefficient equals<br>
> a. -0.4364　b. 0.4364　c. -0.1905　d. 0.1905

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率為負。④ **代入計算／推理：** $r=-8/\sqrt{8(42)}=-0.4364$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c、d 是 $R^2$ 的量級。

#### 選擇題 77 <a id="exam-ch14-mc-77"></a>

##### 題目

> Refer to Exhibit 14-3. The coefficient of determination equals<br>
> a. -0.4364　b. 0.4364　c. -0.1905　d. 0.1905

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $R^2$ 非負。④ **代入計算／推理：** $(-0.4364)^2\approx0.1905$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 是 $r$；b 少平方；c 不可負；d 正確。

#### 題組 14-4：選擇題 78–82 共用資料

> Regression analysis was applied between sales data ($Y$ in $\$1{,}000$s) and advertising data ($x$ in $\$100$s):
>
> $\hat Y=12+1.8x$, $n=17$, $SSR=225$, $SSE=75$, $s_{b_1}=0.2683$.

由 $df_E=15$ 得 $MSE=75/15=5$、$F=225/5=45$、$t=1.8/0.2683=6.708$。

#### 選擇題 78 <a id="exam-ch14-mc-78"></a>

##### 題目

> If advertising is $\$3{,}000$, the point estimate for sales in dollars is<br>
> a. $\$66{,}000$　b. $\$5{,}412$　c. $\$66$　d. $\$17{,}400$

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 單位點預測。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $x=3000/100=30$。④ **代入計算／推理：** $\hat Y=12+1.8(30)=66$ 千美元。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 直接乘錯；c 忘千倍；d 混入樣本數。

#### 選擇題 79 <a id="exam-ch14-mc-79"></a>

##### 題目

> The $F$ statistic is<br>
> a. 3　b. 45　c. 48　d. 50

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$F$](./course2-slides-handout.html#formula-slr-f-test)


**五步詳解：** ① **辨認題型：** 迴歸 $F$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$F$](./course2-slides-handout.html#formula-slr-f-test)。③ **檢查假設：** $df_R=1,df_E=15$。④ **代入計算／推理：** $F=(225/1)/(75/15)=45$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 是 $SSR/SSE$；b 正確；c、d 分母錯。

#### 選擇題 80 <a id="exam-ch14-mc-80"></a>

##### 題目

> To perform an $F$ test, the p-value is<br>
> a. less than .01　b. between .01 and .025　c. between .025 and .05　d. between .05 and .1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$F$ 檢定](./course2-slides-handout.html#formula-slr-f-test)


**五步詳解：** ① **辨認題型：** $F$ 右尾範圍。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$F$ 檢定](./course2-slides-handout.html#formula-slr-f-test)。③ **檢查假設：** $F(1,15)=45$。④ **代入計算／推理：** 獨立計算 $p\approx7.01\times10^{-6}<.01$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b、c、d 都把極大的 $F$ 對應到過大的尾機率。

#### 選擇題 81 <a id="exam-ch14-mc-81"></a>

##### 題目

> The $t$ statistic for testing the significance of the slope is<br>
> a. 1.80　b. 1.96　c. 6.708　d. 0.555

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)


**五步詳解：** ① **辨認題型：** 斜率 $t$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$t$](./course2-slides-handout.html#formula-slr-t-test)。③ **檢查假設：** $s_{b_1}=0.2683$。④ **代入計算／推理：** $t=1.8/0.2683=6.708$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 只取係數；b 是常態臨界值；c 正確；d 顛倒相除。

#### 選擇題 82 <a id="exam-ch14-mc-82"></a>

##### 題目

> The critical $t$ value for testing the significance of the slope at 95% confidence is<br>
> a. 1.753　b. 2.131　c. 1.746　d. 2.120

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)


**五步詳解：** ① **辨認題型：** 雙尾臨界值。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)。③ **檢查假設：** $df=n-2=15$、$\alpha/2=.025$。④ **代入計算／推理：** $t_{.025,15}=2.131$。⑤ **解讀結論：** **b** 。

**選項逐一：** a、c 是單尾或其他自由度值；b 正確；d 是 $df=16$ 的近似值。

### 選擇題｜第 83–113 題：題組 14-5 至 14-10

#### 題組 14-5：選擇題 83–87 共用資料

| $Y$ | $X$ |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |

五點完全落在 $\hat y=x$：$b_0=0$、$b_1=1$、$r=1$、$R^2=1$、$MSE=0$。

#### 選擇題 83 <a id="exam-ch14-mc-83"></a>

##### 題目

> The least squares estimate of the $Y$ intercept is<br>
> a. 1　b. 0　c. -1　d. 3

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $y=x$。④ **代入計算／推理：** $b_0=0$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 是斜率；b 正確；c、d 不通過資料點。

#### 選擇題 84 <a id="exam-ch14-mc-84"></a>

##### 題目

> The least squares estimate of the slope is<br>
> a. 1　b. -1　c. 0　d. 3

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $x$ 每增 1，$y$ 增 1。④ **代入計算／推理：** $b_1=1$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 方向錯；c 非水平線；d 增量過大。

#### 選擇題 85 <a id="exam-ch14-mc-85"></a>

##### 題目

> The coefficient of correlation is<br>
> a. 0　b. -1　c. 0.5　d. 1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** 完全正相關。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 所有點在正斜率線。④ **代入計算／推理：** $r=1$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 無關聯；b 方向錯；c 非完全；d 正確。

#### 選擇題 86 <a id="exam-ch14-mc-86"></a>

##### 題目

> The coefficient of determination is<br>
> a. 0　b. -1　c. 0.5　d. 1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 完全配適。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $SSE=0$。④ **代入計算／推理：** $R^2=1$。⑤ **解讀結論：** **d** 。

**選項逐一：** a、c 不是完全配適；b 不可負；d 正確。

#### 選擇題 87 <a id="exam-ch14-mc-87"></a>

##### 題目

> The MSE is<br>
> a. 0　b. -1　c. 1　d. 0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)


**五步詳解：** ① **辨認題型：** 殘差變異。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$MSE$](./course2-slides-handout.html#formula-slr-mse)。③ **檢查假設：** 每筆殘差為 0。④ **代入計算／推理：** $MSE=SSE/(n-2)=0$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 平方量不負；c、d 都假設存在殘差。

#### 題組 14-6：選擇題 88–91 共用資料

> For the following data the value of $SSE=0.4130$.

| $y$ | $x$ |
|---:|---:|
| 15 | 4 |
| 17 | 6 |
| 23 | 2 |
| 17 | 4 |

逐筆資料獨立驗算得到 $\bar x=4$、$\bar y=18$、$b_1=-1.5$、$b_0=24$、$SST=36$、$SSE=18$、$R^2=0.5$。因此題幹的 `SSE=0.4130` 與表內資料矛盾；第 91 題的選項也只與表內資料算出的 $R^2=0.5$ 相容。

#### 選擇題 88 <a id="exam-ch14-mc-88"></a>

##### 題目

> The slope of the regression equation is<br>
> a. 18　b. 24　c. 0.707　d. -1.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** 直接使用四筆原始資料，不使用矛盾的 SSE。④ **代入計算／推理：** $S_{xy}=-12,S_{xx}=8$，故 $b_1=-1.5$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 是平均數量級；b 是截距；c 像相關量；d 正確。

#### 選擇題 89 <a id="exam-ch14-mc-89"></a>

##### 題目

> The $y$ intercept is<br>
> a. -1.5　b. 24　c. 0.50　d. -0.707

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=4,\bar y=18$。④ **代入計算／推理：** $b_0=18-(-1.5)(4)=24$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 是斜率；b 正確；c、d 是無單位量。

#### 選擇題 90 <a id="exam-ch14-mc-90"></a>

##### 題目

> The total sum of squares $(SST)$ equals<br>
> a. 36　b. 18　c. 9　d. 1296

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$SST$](./course2-slides-handout.html#formula-slr-sst)


**五步詳解：** ① **辨認題型：** $SST$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$SST$](./course2-slides-handout.html#formula-slr-sst)。③ **檢查假設：** $\bar y=18$。④ **代入計算／推理：** $(-3)^2+(-1)^2+5^2+(-1)^2=36$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 是資料算出的 SSE；c 漏項；d 是把總偏差錯誤平方。

#### 選擇題 91 <a id="exam-ch14-mc-91"></a>

##### 題目

> The coefficient of determination $(r^2)$ equals<br>
> a. 0.7071　b. -0.7071　c. 0.5　d. -0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** 有矛盾資料的 $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 以原始四筆資料為權威可重算基礎。④ **代入計算／推理：** $R^2=1-18/36=0.5$。⑤ **解讀結論：** **c** ；若硬用題幹 `SSE=0.4130` 會得 0.9885，並不在選項中。

**選項逐一：** a 是 $|r|$ 的近似；b、d 不可為負；c 與資料一致。

#### 題組 14-7：選擇題 92–95 共用資料

| $y$ | $x$ |
|---:|---:|
| 5 | 4 |
| 7 | 6 |
| 9 | 2 |
| 11 | 4 |

驗算得 $\bar x=4$、$\bar y=8$、$S_{xx}=8$、$S_{xy}=-4$，所以 $b_1=-0.5$、$b_0=10$、$r=-0.3162$、$R^2=0.10$。

#### 選擇題 92 <a id="exam-ch14-mc-92"></a>

##### 題目

> The least squares estimate of $b_1$ equals<br>
> a. -10　b. 10　c. 0.5　d. -0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $S_{xx}=8$。④ **代入計算／推理：** $b_1=-4/8=-0.5$。⑤ **解讀結論：** **d** 。

**選項逐一：** a、b 是截距量級；c 符號錯；d 正確。

#### 選擇題 93 <a id="exam-ch14-mc-93"></a>

##### 題目

> The least squares estimate of $b_0$ equals<br>
> a. -10　b. 10　c. 0.5　d. -0.5

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=4,\bar y=8$。④ **代入計算／推理：** $b_0=8-(-0.5)(4)=10$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 符號錯；b 正確；c、d 是斜率候選。

#### 選擇題 94 <a id="exam-ch14-mc-94"></a>

##### 題目

> The sample correlation coefficient equals<br>
> a. 0.3162　b. -0.3162　c. 0.10　d. -0.10

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率負。④ **代入計算／推理：** $r=-\sqrt{0.10}=-0.3162$。⑤ **解讀結論：** **b** 。

**選項逐一：** a 符號錯；b 正確；c、d 是 $R^2$ 量級。

#### 選擇題 95 <a id="exam-ch14-mc-95"></a>

##### 題目

> The coefficient of determination equals<br>
> a. 0.3162　b. -0.3162　c. 0.10　d. -0.10

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 不帶方向。④ **代入計算／推理：** $R^2=(-0.3162)^2\approx0.10$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 是 $|r|$；b、d 不可負；c 正確。

#### 題組 14-8：選擇題 96–101 共用資料

> $\sum X=90$, $\sum Y=340$, $n=4$, $SSR=104$,<br>
> $\sum(Y-\bar Y)(X-\bar X)=-156$, $\sum(X-\bar X)^2=234$, $\sum(Y-\bar Y)^2=1974$.

因此 $\bar x=22.5$、$\bar y=85$、$SST=1974$、$SSE=1974-104=1870$、$MSE=1870/2=935$、$b_1=-156/234=-0.667$、$b_0=100$、$r=-0.2295$。

#### 選擇題 96 <a id="exam-ch14-mc-96"></a>

##### 題目

> The total sum of squares $(SST)$ is<br>
> a. -156　b. 234　c. 1870　d. 1974

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$SST$](./course2-slides-handout.html#formula-slr-sst)


**五步詳解：** ① **辨認題型：** 辨認摘要符號。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$SST$](./course2-slides-handout.html#formula-slr-sst)。③ **檢查假設：** $SST=\sum(Y-\bar Y)^2$。④ **代入計算／推理：** 直接讀得 1974。⑤ **解讀結論：** **d** 。

**選項逐一：** a 是交叉乘積；b 是 $S_{xx}$；c 是 SSE；d 正確。

#### 選擇題 97 <a id="exam-ch14-mc-97"></a>

##### 題目

> The sum of squares due to error $(SSE)$ is<br>
> a. -156　b. 234　c. 1870　d. 1974

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$SST=SSR+SSE$](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 變異分解。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$SST=SSR+SSE$](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** $SSR=104$。④ **代入計算／推理：** $SSE=1974-104=1870$。⑤ **解讀結論：** **c** 。

**選項逐一：** a、b 是其他摘要；c 正確；d 是 SST。

#### 選擇題 98 <a id="exam-ch14-mc-98"></a>

##### 題目

> The mean square error $(MSE)$ is<br>
> a. 1870　b. 13　c. 1974　d. 935

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)


**五步詳解：** ① **辨認題型：** $MSE$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$MSE$](./course2-slides-handout.html#formula-slr-mse)。③ **檢查假設：** $df_E=n-2=2$。④ **代入計算／推理：** $1870/2=935$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 是 SSE；b 把自由度算錯；c 是 SST；d 正確。

#### 選擇題 99 <a id="exam-ch14-mc-99"></a>

##### 題目

> The slope of the regression equation is<br>
> a. -0.667　b. 0.667　c. 100　d. -100

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** 分母 234 為正。④ **代入計算／推理：** $b_1=-156/234=-0.667$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c、d 是截距量級。

#### 選擇題 100 <a id="exam-ch14-mc-100"></a>

##### 題目

> The $Y$ intercept is<br>
> a. -0.667　b. 0.667　c. 100　d. -100

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=22.5,\bar y=85$。④ **代入計算／推理：** $b_0=85-(-0.667)(22.5)=100$。⑤ **解讀結論：** **c** 。

**選項逐一：** a、b 是斜率；c 正確；d 符號錯。

#### 選擇題 101 <a id="exam-ch14-mc-101"></a>

##### 題目

> The coefficient of correlation is<br>
> a. -0.2295　b. 0.2295　c. 0.0527　d. -0.0572

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率負。④ **代入計算／推理：** $r=-156/\sqrt{234(1974)}=-0.2295$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c 是 $R^2$ 近似；d 數值錯。

#### 題組 14-9：選擇題 102–106 共用資料

> $\sum X=90$, $\sum Y=170$, $n=10$, $SSE=505.98$,<br>
> $\sum(Y-\bar Y)(X-\bar X)=466$, $\sum(X-\bar X)^2=234$, $\sum(Y-\bar Y)^2=1434$.

驗算得 $\bar x=9$、$\bar y=17$、$b_1=1.991$、$b_0=-0.923$、$SSR=1434-505.98=928.02$、$r=0.8045$、$R^2=0.6472$。

#### 選擇題 102 <a id="exam-ch14-mc-102"></a>

##### 題目

> The least squares estimate of $b_1$ equals<br>
> a. 0.923　b. 1.991　c. -1.991　d. -0.923

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $S_{xx}=234$。④ **代入計算／推理：** $466/234=1.991$。⑤ **解讀結論：** **b** 。

**選項逐一：** a、d 是截距量級；b 正確；c 符號錯。

#### 選擇題 103 <a id="exam-ch14-mc-103"></a>

##### 題目

> The least squares estimate of $b_0$ equals<br>
> a. 0.923　b. 1.991　c. -1.991　d. -0.923

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=9,\bar y=17$。④ **代入計算／推理：** $17-1.991(9)\approx-0.923$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 符號錯；b、c 是斜率量級；d 正確。

#### 選擇題 104 <a id="exam-ch14-mc-104"></a>

##### 題目

> The sum of squares due to regression $(SSR)$ is<br>
> a. 1434　b. 505.98　c. 50.598　d. 928.02

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)


**五步詳解：** ① **辨認題型：** 平方和分解。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)。③ **檢查假設：** $SST=1434$。④ **代入計算／推理：** $SSR=1434-505.98=928.02$。⑤ **解讀結論：** **d** 。

**選項逐一：** a 是 SST；b 是 SSE；c 把 SSE 除 10；d 正確。

#### 選擇題 105 <a id="exam-ch14-mc-105"></a>

##### 題目

> The sample correlation coefficient equals<br>
> a. 0.8045　b. -0.8045　c. 0　d. 1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[相關係數](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[相關係數](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** $S_{xy}>0$。④ **代入計算／推理：** $466/\sqrt{234(1434)}=0.8045$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c 忽略正交叉乘積；d 非完全配適。

#### 選擇題 106 <a id="exam-ch14-mc-106"></a>

##### 題目

> The coefficient of determination equals<br>
> a. 0.6472　b. -0.6472　c. 0　d. 1

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** 不帶負號。④ **代入計算／推理：** $928.02/1434=0.6472$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 不可負；c、d 都不符有殘差的資料。

#### 題組 14-10：選擇題 107–113 共用資料

> $\sum X=16$, $\sum Y=28$, $n=4$, $SSE=34$,<br>
> $\sum(X-\bar X)(Y-\bar Y)=-8$, $\sum(X-\bar X)^2=8$, $SST=42$.

驗算得 $\bar x=4$、$\bar y=7$、$b_1=-1$、$b_0=11$、$R^2=1-34/42=0.1905$、$r=-0.4364$、$MSE=34/2=17$。

#### 選擇題 107 <a id="exam-ch14-mc-107"></a>

##### 題目

> The slope of the regression function is<br>
> a. -1　b. 1.0　c. 11　d. 0.0

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 斜率。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[斜率](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $S_{xx}=8$。④ **代入計算／推理：** $b_1=-8/8=-1$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 符號錯；c 是截距；d 忽略交叉乘積。

#### 選擇題 108 <a id="exam-ch14-mc-108"></a>

##### 題目

> The $Y$ intercept is<br>
> a. -1　b. 1.0　c. 11　d. 0.0

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[截距](./course2-slides-handout.html#formula-slr-slope-intercept)


**五步詳解：** ① **辨認題型：** 截距。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[截距](./course2-slides-handout.html#formula-slr-slope-intercept)。③ **檢查假設：** $\bar x=4,\bar y=7$。④ **代入計算／推理：** $b_0=7-(-1)(4)=11$。⑤ **解讀結論：** **c** 。

**選項逐一：** a、b 是斜率；c 正確；d 不通過平均點。

#### 選擇題 109 <a id="exam-ch14-mc-109"></a>

##### 題目

> The coefficient of determination is<br>
> a. 0.1905　b. -0.1905　c. 0.4364　d. -0.4364

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


**五步詳解：** ① **辨認題型：** $R^2$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。③ **檢查假設：** $R^2$ 不負。④ **代入計算／推理：** $1-34/42=0.1905$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b、d 不可負；c 是 $|r|$。

#### 選擇題 110 <a id="exam-ch14-mc-110"></a>

##### 題目

> The coefficient of correlation is<br>
> a. 0.1905　b. -0.1905　c. 0.4364　d. -0.4364

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


**五步詳解：** ① **辨認題型：** $r$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。③ **檢查假設：** 斜率負。④ **代入計算／推理：** $r=-\sqrt{0.1905}=-0.4364$。⑤ **解讀結論：** **d** 。

**選項逐一：** a、b 是 $R^2$ 量級；c 符號錯；d 正確。

#### 選擇題 111 <a id="exam-ch14-mc-111"></a>

##### 題目

> The MSE is<br>
> a. 17　b. 8　c. 34　d. 42

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)


**五步詳解：** ① **辨認題型：** $MSE$。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[$MSE$](./course2-slides-handout.html#formula-slr-mse)。③ **檢查假設：** $df_E=4-2=2$。④ **代入計算／推理：** $MSE=34/2=17$。⑤ **解讀結論：** **a** 。

**選項逐一：** a 正確；b 是 $S_{xx}$；c 是 SSE；d 是 SST。

#### 選擇題 112 <a id="exam-ch14-mc-112"></a>

##### 題目

> The point estimate of $Y$ when $X=3$ is<br>
> a. 11　b. 14　c. 8　d. 0

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 點預測。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $\hat y=11-x$。④ **代入計算／推理：** $11-3=8$。⑤ **解讀結論：** **c** 。

**選項逐一：** a 只取截距；b 符號錯；c 正確；d 無此結果。

#### 選擇題 113 <a id="exam-ch14-mc-113"></a>

##### 題目

> The point estimate of $Y$ when $X=-3$ is<br>
> a. 11　b. 14　c. 8　d. 0

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


**五步詳解：** ① **辨認題型：** 點預測與外插。② **選方法：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)與[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。③ **檢查假設：** $x=-3$ 是否合理須看原始資料範圍；此處只做代數。④ **代入計算／推理：** $\hat y=11-(-3)=14$。⑤ **解讀結論：** 算術答案 **b** ，但負 $x$ 若不具情境意義便不可作實務預測。

**選項逐一：** a 忘記代入項；b 正確；c 把 $-3$ 當 $+3$；d 無此結果。

### 計算題｜第 1–11 題：完整資料、輸出判讀與區間

#### 計算題 1 <a id="exam-ch14-problem-1"></a>

##### 題目

> Assume you have noted the following prices for books and the number of pages that each book contains.

| Book | Pages $(x)$ | Price $(y)$ |
|---|---:|---:|
| A | 500 | $\$7.00$ |
| B | 700 | $7.50$ |
| C | 750 | $9.00$ |
| D | 590 | $6.50$ |
| E | 540 | $7.50$ |
| F | 650 | $7.00$ |
| G | 480 | $4.50$ |

> a. Develop a least-squares estimated regression line.<br>
> b. Compute the coefficient of determination and explain its meaning.<br>
> c. Compute the correlation coefficient between the price and the number of pages. Test to see if $x$ and $y$ are related. Use $\alpha=0.10$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$r$](./course2-slides-handout.html#formula-slr-correlation)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)


1. **辨認題型：** 兩個數值變數的簡單迴歸、配適與斜率檢定。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$r$](./course2-slides-handout.html#formula-slr-correlation)與[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)。
3. **檢查假設：** 書本是不同觀察值；應先看散佈圖是否近似線性、無極端離群、誤差獨立且散布大致等寬。$n=7$ 很小，常態性尤其重要。
4. **代入計算／推理：** $\bar x=601.4286$、$\bar y=7$、$S_{xx}=63085.7143$，得 $b_1=0.009907$、$b_0=1.04155$，所以 $\hat y=1.04155+0.009907x$。$SST=11$、$SSE=4.80803$，故 $R^2=0.56291$、$r=+0.75027$。$MSE=0.96161$、$s_{b_1}=0.003904$，$t=2.5376$、$df=5$、雙尾 $p=0.05205$。
5. **解讀結論：** 約 $56.29\%$ 的書價樣本變異由頁數的線性關係解釋；在 $\alpha=.10$ 下拒絕 $H_0:\beta_1=0$，有正線性關係證據，但不表示頁數必然造成價格。

#### 計算題 2 <a id="exam-ch14-problem-2"></a>

##### 題目

> Use the same seven-book data from Problem 1.<br>
> a. Perform an $F$ test at $\alpha=0.01$.<br>
> b. Perform a $t$ test at $\alpha=0.01$.<br>
> c. Develop a 90% confidence interval for the average price of books that contain 800 pages.<br>
> d. Develop a 90% confidence interval for the price of a specific book that has 800 pages.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)、[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)


1. **辨認題型：** 整體 $F$、斜率 $t$、平均反應 CI 與個別 PI。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)與[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)。
3. **檢查假設：** 沿用 Problem 1 的線性、獨立、等變異、常態假設。$x^*=800$ 超過樣本最大 750，是輕度外插，區間公式算得出但可信度較弱。
4. **代入計算／推理：** $F=6.4392$、$F(1,5)$ 的 $p=0.05205$；$t=2.5376$、$p=0.05205$。兩者在 $\alpha=.01$ 都不拒絕。$\hat y^*=8.9673$，90% 的 $t_{.05,5}=2.0150$；平均 CI 為 $(7.2357,10.6988)$ 美元，個別 PI 為 $(6.3400,11.5946)$ 美元。
5. **解讀結論：** 在 1% 顯著水準下證據不足；同為 800 頁時，單一本書的 PI 較寬，因為還含個體價格波動。

#### 計算題 3 <a id="exam-ch14-problem-3"></a>

##### 題目

> The following data represent the number of flash drives sold per day at a local computer shop and their prices.

| Price $(x)$ | Units Sold $(y)$ |
|---:|---:|
| \$34 | 3 |
| 36 | 4 |
| 32 | 6 |
| 35 | 5 |
| 30 | 9 |
| 38 | 2 |
| 40 | 1 |

> a. Develop a least-squares regression line and explain the slope.<br>
> b. Compute and interpret the coefficient of determination.<br>
> c. Compute the sample correlation coefficient and test the relationship at $\alpha=0.01$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)


1. **辨認題型：** 價格預測銷量的負向簡單迴歸。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)與[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)。
3. **檢查假設：** 七天資料應近似獨立；若有星期循環，獨立性可能失效。也要檢查線性、等變異與常態殘差。
4. **代入計算／推理：** $\hat y=29.7857-0.72857x$。$R^2=0.85559$，$r=-0.92498$。$t=-5.4428$、$df=5$、$p=0.002842$。
5. **解讀結論：** 價格每增 $\$1$，預估日銷量平均減少約 0.729 支；模型解釋約 $85.56\%$ 的樣本銷量變異。在 1% 水準拒絕 $H_0$，有負線性關係證據。

#### 計算題 4 <a id="exam-ch14-problem-4"></a>

##### 題目

> Use the same flash-drive data from Problem 3.<br>
> a. Perform an $F$ test at $\alpha=0.01$.<br>
> b. Perform a $t$ test at $\alpha=0.01$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$t$](./course2-slides-handout.html#formula-slr-t-test)


1. **辨認題型：** 同一斜率虛無假設的 $F$ 與 $t$ 檢定。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，比較[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$t$](./course2-slides-handout.html#formula-slr-t-test)。
3. **檢查假設：** 沿用 Problem 3；簡單迴歸只有一個斜率，因此應有 $F=t^2$。
4. **代入計算／推理：** $F=29.6241$、$df=(1,5)$、$p=0.002842$；$t=-5.4428$、$df=5$、同一雙尾 $p=0.002842$，且 $t^2=29.6241$。
5. **解讀結論：** 兩種方法都在 1% 水準拒絕 $H_0:\beta_1=0$，結論一致。

#### 計算題 5 <a id="exam-ch14-problem-5"></a>

##### 題目

> A portion of Excel output relating $Y$ and $X$ is:

| Source | $df$ | $SS$ |
|---|---:|---:|
| Regression | 1 | 110 |
| Residual | 8 | 74 |
| Total | 9 | 184 |

| Term | Coefficient | Standard Error |
|---|---:|---:|
| Intercept | 39.222 | 5.943 |
| $x$ | -0.5556 | 0.1611 |

> a. Find the sample size.<br>
> b. Perform a $t$ test at $\alpha=0.05$.<br>
> c. Perform an $F$ test at $\alpha=0.05$.<br>
> d. Compute $R^2$.<br>
> e. Interpret $R^2$ specifically.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[ANOVA 表](./course2-slides-handout.html#formula-slr-f-test)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 讀電腦輸出。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[ANOVA 表](./course2-slides-handout.html#formula-slr-f-test)、[斜率 $t$](./course2-slides-handout.html#formula-slr-t-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** 推論仍需線性、獨立、等變異與常態殘差；輸出本身不會自動證明。
4. **代入計算／推理：** $n=df_T+1=10$。$t=-0.5556/0.1611=-3.4488$、$df=8$、$p\approx0.00871$。$MSE=74/8=9.25$，$F=110/9.25=11.8919$、$p\approx0.00871$。$R^2=110/184=0.59783$。
5. **解讀結論：** 在 5% 水準，$X$ 與平均 $Y$ 有顯著負線性關係；模型解釋約 $59.78\%$ 的這批 $Y$ 樣本變異，不能解讀成因果比例。

#### 計算題 6 <a id="exam-ch14-problem-6"></a>

##### 題目

> A computer output gives $SSR=24.011$, $df_R=1$, $SSE=67.989$, $df_E=8$, intercept $11.065$ (SE $2.043$), and slope $-0.511$ (SE $0.304$).<br>
> a. Find $n$. b. Perform a $t$ test at .05. c. Perform an $F$ test at .05. d. Compute $R^2$. e. Interpret it.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 部分迴歸輸出。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** 同 Problem 5；$n=8+2=10$。
4. **代入計算／推理：** $t=-0.511/0.304=-1.6809$、$p\approx0.1313$；$MSE=67.989/8=8.4986$、$F=24.011/8.4986=2.8253$、$p\approx0.1313$；$R^2=24.011/(24.011+67.989)=0.26099$。
5. **解讀結論：** 在 5% 水準不拒絕 $H_0$；約 $26.10\%$ 的樣本 $Y$ 變異由線性模型解釋，尚不足以宣稱母體斜率非零。

#### 計算題 7 <a id="exam-ch14-problem-7"></a>

##### 題目

> Fill every `?` in this Excel output.

| Regression Statistics | Value |
|---|---:|
| Multiple R | 0.1347 |
| R Square | ? |
| Adjusted R Square | ? |
| Standard Error | 3.3838 |
| Observations | ? |

| Source | $df$ | $SS$ | $MS$ | $F$ | Significance F |
|---|---:|---:|---:|---:|---:|
| Regression | ? | 2.7500 | ? | ? | 0.632 |
| Residual | ? | ? | 11.45 |  |  |
| Total | 14 | ? |  |  |  |

| Term | Coefficient | SE | $t$ | $p$ |
|---|---:|---:|---:|---:|
| Intercept | 8.6 | 2.2197 | ? | 0.0019 |
| $x$ | 0.25 | 0.5101 | ? | 0.632 |

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)、[$F$](./course2-slides-handout.html#formula-slr-f-test)


1. **辨認題型：** Excel 空格反推。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，串起[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)與[$F$](./course2-slides-handout.html#formula-slr-f-test)。
3. **檢查假設：** 簡單迴歸 $df_R=1$；$df_T=n-1=14$，故 $n=15$、$df_E=13$。
4. **代入計算／推理：** $R^2=0.1347^2=0.01814$；adjusted $R^2=1-(1-R^2)(14/13)\approx-0.05738$。$SSE=11.45(13)=148.85$，$SST=151.60$。$MSR=2.75$，$F=2.75/11.45=0.2402$。截距 $t=8.6/2.2197=3.8744$；斜率 $t=0.25/0.5101=0.4901$。
5. **解讀結論：** 應填：$R^2=0.0181$、adjusted $R^2=-0.0574$、$n=15$；ANOVA 的 $df=(1,13,14)$、$SS=(2.75,148.85,151.60)$、$MSR=2.75$、$F=0.2402$；兩個 $t$ 分別 3.8744 與 0.4901。負 adjusted $R^2$ 表示這條線甚至不比單用平均數有實質優勢。

#### 計算題 8 <a id="exam-ch14-problem-8"></a>

##### 題目

> A computer output gives $SSR=115.064$, $df_R=1$, $SSE=82.936$, $df_E=13$, intercept $15.532$ (SE $1.457$), and slope $-1.106$ (SE $0.261$).<br>
> a. Perform a $t$ test using p-value at .05. b. Perform an $F$ test using p-value. c. Compute and interpret $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** $t/F$ 等價與配適。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)及[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $n=15$；須檢查殘差條件。
4. **代入計算／推理：** $t=-1.106/0.261=-4.2375$、$p\approx0.000969$。$MSE=82.936/13=6.3797$，$F=115.064/6.3797=18.036$、$p\approx0.000953$；小差異來自輸出係數四捨五入。$R^2=115.064/198=0.58113$。
5. **解讀結論：** 在 5% 水準拒絕 $H_0$；有顯著負線性關係，模型解釋約 $58.11\%$ 的樣本 $Y$ 變異。

#### 計算題 9 <a id="exam-ch14-problem-9"></a>

##### 題目

> Fill every `?` in this Excel output: $R^2=0.5149$, Standard Error $=7.3413$, Observations $=11$, total $SS=1000$, Significance F $=0.0129$; intercept SE $=29.4818$, $t=3.7946$, $p=.0043$; slope SE $=.7000$, $t=-3.0911$, $p=.0129$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)、[$F$](./course2-slides-handout.html#formula-slr-f-test)


1. **辨認題型：** 由摘要反推完整輸出。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)、[$MSE$](./course2-slides-handout.html#formula-slr-mse)與[$F$](./course2-slides-handout.html#formula-slr-f-test)。
3. **檢查假設：** $n=11$，故 $df=(1,9,10)$。
4. **代入計算／推理：** Multiple R $=\sqrt{.5149}=0.7176$；adjusted $R^2=1-(1-.5149)(10/9)=0.4610$。$SSR=514.9$、$SSE=485.1$；$MSR=514.9$、$MSE\approx7.3413^2=53.8947$，$F\approx9.553$。截距係數 $=29.4818(3.7946)\approx111.89$；斜率係數 $=.7000(-3.0911)\approx-2.1638$。
5. **解讀結論：** Excel 的 Multiple R 顯示絕對值；因斜率為負，實際樣本相關為約 $-0.7176$。平方和由四捨五入後的標準誤反推會有約 0.05 的尾差，應以題目給的 $SST=1000$ 與 $R^2=.5149$ 為主。

#### 計算題 10 <a id="exam-ch14-problem-10"></a>

##### 題目

> Demand $(Y)$ and unit price $(X)$ output: $SSR=5048.818$, $df_R=1$, $SSE=3132.661$, $df_E=46$, $SST=8181.479$; intercept $80.390$ (SE $3.102$), slope $-2.137$ (SE $0.248$).<br>
> a. $t$ test at .05. b. $F$ test at .05. c. Compute and interpret $R^2$. d. Compute and explain $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 價格與需求的輸出判讀。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** $n=48$；仍需殘差診斷，且價格與需求的關聯不單獨證明價格造成需求變化。
4. **代入計算／推理：** $t=-2.137/.248=-8.6169$、$p<10^{-10}$。$MSE=3132.661/46=68.1013$，$F=74.1369$、$p<10^{-10}$。$R^2=5048.818/8181.479=0.61710$；$r=-\sqrt{R^2}=-0.78556$。
5. **解讀結論：** 在 5% 水準有顯著負線性關係；單價的線性關係解釋約 $61.71\%$ 的需求樣本變異，關聯強度約為 $r=-0.786$。

#### 計算題 11 <a id="exam-ch14-problem-11"></a>

##### 題目

> Supply $(Y$ in thousands of units) and unit price $(X$ in thousands of dollars) output: $SSR=354.689$, $df_R=1$, $SSE=7035.262$, $df_E=39$; intercept $54.076$ (SE $2.358$), slope $0.029$ (SE $0.021$).<br>
> a. Find $n$. b. $t$ test at .05. c. $F$ test at .05. d. Compute and interpret $R^2$. e. Compute and explain $r$. f. Predict supply in units when price is $\$50{,}000$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


1. **辨認題型：** 輸出推論、配適與單位預測。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)和[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。
3. **檢查假設：** $n=39+2=41$。輸出係數只有三位小數，因此 $t^2$ 與 ANOVA $F$ 會有可見四捨五入差。
4. **代入計算／推理：** 係數列給 $t=.029/.021=1.381$、$p\approx.1752$；平方和給 $F=354.689/(7035.262/39)=1.9662$、$p\approx.1688$。$R^2=354.689/7389.951=0.04800$，$r=+0.2191$。價格 $\$50{,}000$ 對應 $x=50$，$\hat y=54.076+.029(50)=55.526$ 千單位，即約 55,526 單位。
5. **解讀結論：** 不論採四捨五入係數或 ANOVA 平方和，5% 水準都不拒絕 $H_0$；線性模型只解釋約 $4.80\%$ 的供給樣本變異。預測值僅在 $x=50$ 位於合理資料範圍時才可信。

### 計算題｜第 12–23 題：原始資料與部分輸出

#### 計算題 12 <a id="exam-ch14-problem-12"></a>

##### 題目

> Four observations are $(x,y)=(2,4),(6,7),(9,8),(9,9)$.<br>
> a. Develop the least squares equation. b. At 95% confidence, test whether the slope differs from zero. c. Perform an $F$ test at .05. d. Compute $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 小樣本簡單迴歸全套。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $n=4$、$df=2$，常態與離群值非常敏感；四點應先畫散佈圖。
4. **代入計算／推理：** $\hat y=2.86364+0.63636x$；$SSE=.63636$、$MSE=.31818$、$s_{b_1}=.09819$。$t=6.4807$、$p=.02299$；$F=42$、同一 $p$；$R^2=.95455$。
5. **解讀結論：** 在 5% 水準拒絕 $H_0$，模型顯著，解釋約 $95.45\%$ 的樣本 $Y$ 變異；但樣本極小，結論高度依賴假設。

#### 計算題 13 <a id="exam-ch14-problem-13"></a>

##### 題目

> Five observations are $(2,4),(3,4),(4,3),(5,2),(6,1)$.<br>
> a. Develop the equation. b. Test the slope at 95% confidence. c. Perform an $F$ test at .05. d. Compute $R^2$. e. Compute $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 負向小樣本迴歸。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** 五點需檢查直線形狀、等變異與常態殘差。
4. **代入計算／推理：** $\hat y=6-0.8x$；$SSE=.4$、$MSE=.13333$、$t=-6.9282$、$df=3$、$p=.006165$；$F=48$；$R^2=.94118$；$r=-.97014$。
5. **解讀結論：** 在 5% 水準有顯著負線性關係，約 $94.12\%$ 的樣本變異被解釋。

#### 計算題 14 <a id="exam-ch14-problem-14"></a>

##### 題目

> A sample of 8 gives intercept $13.251$ (SE $10.77$), slope $0.803$ (SE $0.385$), residual $SS=41.674$, total $SS=71.875$.<br>
> a. Develop the line. b. Test the slope at .05. c. Perform an $F$ test at .05. d. Determine $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 部分輸出補算。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[估計式](./course2-slides-handout.html#formula-slr-estimated-line)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $df_E=6$；輸出係數已四捨五入。
4. **代入計算／推理：** $\hat y=13.251+0.803x$。$t=.803/.385=2.0857$、$p=.0821$。$SSR=71.875-41.674=30.201$，$F=30.201/(41.674/6)=4.3482$、$p=.0821$。$R^2=30.201/71.875=.42019$。
5. **解讀結論：** 在 5% 水準不拒絕 $H_0$；雖樣本內解釋約 $42.02\%$ 變異，證據仍不足以確認母體斜率非零。

#### 計算題 15 <a id="exam-ch14-problem-15"></a>

##### 題目

> A sample of 8 gives intercept $-9.462$ (SE $7.032$), slope $0.769$ (SE $0.184$), regression $SS=400$, residual $SS=138$.<br>
> a. Develop the line. b. Test the slope at .05. c. Perform an $F$ test at .05. d. Determine $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 部分輸出判讀。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $df_E=6$；係數與平方和的四捨五入可能使 $t^2$ 與 $F$ 略不同。
4. **代入計算／推理：** $\hat y=-9.462+.769x$。$t=.769/.184=4.1793$、$p=.00582$。$F=400/(138/6)=17.3913$、$p=.00588$。$R^2=400/538=.74349$。
5. **解讀結論：** 在 5% 水準拒絕 $H_0$；有顯著正線性關係，模型解釋約 $74.35\%$ 的樣本變異。

#### 計算題 16 <a id="exam-ch14-problem-16"></a>

##### 題目

> A company's yearly sales and advertising over 8 years are:

| Sales $Y$ (millions of dollars) | Advertising $X$ (in $\$10{,}000$) |
|---:|---:|
| 15 | 32 |
| 16 | 33 |
| 18 | 35 |
| 17 | 34 |
| 16 | 36 |
| 19 | 37 |
| 19 | 39 |
| 24 | 42 |

> a. Develop and explain a scatter diagram. b. Compute the estimated line. c. Predict sales at $\$400{,}000$ advertising. d. Interpret the slope. e. Compute and interpret $R^2$. f. Use an $F$ test at .05. g. Use a $t$ test at .05. h. Develop a 95% CI for average sales when advertising is $\$400{,}000$. i. Compute $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t/F$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)


1. **辨認題型：** 原始資料的完整迴歸分析與平均反應 CI。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，串起[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t/F$](./course2-slides-handout.html#formula-slr-t-test)與[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)。
3. **檢查假設：** 依年份排列，誤差可能有時間自相關；散佈圖呈明顯正趨勢，但仍需看殘差。$x^*=40$ 位於 32–42 範圍內。
4. **代入計算／推理：** 散佈圖為近似正線性。$\hat y=-10.4211+.78947x$。當廣告 $\$400{,}000$ 時 $x=40$，$\hat y=21.1579$ 百萬美元，即約 $\$21{,}157{,}895$。斜率表示廣告每增加 $\$10{,}000$，平均年銷售估增約 $0.7895$ 百萬美元。$R^2=.84586$、$r=.91971$。$F=32.9268$、$t=5.7382$、$p=.001217$。95% 平均 CI 為 $(19.4579,22.8579)$ 百萬美元。
5. **解讀結論：** 在 5% 水準模型與斜率皆顯著，約 $84.59\%$ 的樣本銷售變異被解釋；但年度資料的獨立性要另外確認。

#### 計算題 17 <a id="exam-ch14-problem-17"></a>

##### 題目

> Five observations are $(10,7),(20,5),(30,4),(40,2),(50,1)$.<br>
> a. Develop the equation. b. Test the slope at 95% confidence. c. Perform an $F$ test at .05. d. Compute $R^2$. e. Compute $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 強負線性迴歸。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** $n=5$ 很小；需確認無離群與常態殘差。
4. **代入計算／推理：** $\hat y=8.3-.15x$；$t=-15$、$df=3$、$p=.000643$；$F=225$；$R^2=.98684$；$r=-.99340$。
5. **解讀結論：** 在 5% 水準有極強的顯著負線性關係，模型解釋約 $98.68\%$ 的樣本變異。

#### 計算題 18 <a id="exam-ch14-problem-18"></a>

##### 題目

> A sample of 14 gives constant $6.428$ (SE $1.202$), slope $0.470$ (SE $0.035$), regression $SS=958.584$, total $SS=1021.429$.<br>
> a. Develop the line. b. Test slope at .05. c. Perform an $F$ test at .05. d. Determine $R^2$. e. Determine $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 部分輸出與缺少 SSE。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[變異分解](./course2-slides-handout.html#formula-slr-variance-decomposition)、[$t$](./course2-slides-handout.html#formula-slr-t-test)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** $df_E=12$。
4. **代入計算／推理：** $\hat y=6.428+.470x$；$SSE=62.845$。$t=13.4286$、$p<10^{-7}$；$F=958.584/(62.845/12)=183.038$；$R^2=.93847$；$r=+.96875$。
5. **解讀結論：** 在 5% 水準有顯著正線性關係，模型解釋約 $93.85\%$ 的樣本變異。

#### 計算題 19 <a id="exam-ch14-problem-19"></a>

##### 題目

> A sample of 21 gives constant $30.139$ (SE $1.181$), slope $-0.252$ (SE $0.022$), regression $SS=1759.481$, error $SS=259.186$.<br>
> a. Develop the line. b. Test slope at .05. c. Perform an $F$ test at .05. d. Determine $R^2$. e. Determine $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 負斜率的部分輸出。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** $df_E=19$；須確認殘差條件。
4. **代入計算／推理：** $\hat y=30.139-.252x$。$t=-11.4545$、$p<10^{-9}$；$F=1759.481/(259.186/19)=128.981$；$R^2=.87161$；$r=-.93360$。
5. **解讀結論：** 在 5% 水準有顯著且很強的負線性關係，約 $87.16\%$ 的樣本變異被解釋。

#### 計算題 20 <a id="exam-ch14-problem-20"></a>

##### 題目

> An automobile dealer observes four months:

| Monthly Sales $Y$ | Interest Rate $X$ (%) |
|---:|---:|
| 22 | 9.2 |
| 20 | 7.6 |
| 10 | 10.4 |
| 45 | 5.3 |

> The estimated equation is $\hat Y=75.061-6.254X$.<br>
> a. Obtain a fit measure. b. State hypotheses for a 1% test. c. Test at 99% confidence. d. Construct a 99% CI for average monthly sales at 10%. e. Construct a 99% PI for one month at 10%.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)、[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)


1. **辨認題型：** 極小樣本的配適、檢定與兩種區間。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)與[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)。
3. **檢查假設：** $n=4$、$df=2$，任何離群點都會主導結果；月份可能有時間依賴。$x^*=10$ 在 5.3–10.4 範圍內。
4. **代入計算／推理：** $R^2=.86865$。$H_0:\beta_1=0$ 對 $H_a:\beta_1\ne0$。$t=-3.6369$、$p=.06798>.01$，不拒絕。當 $x^*=10$，$\hat y=12.5244$；$t_{.005,2}=9.9248$，99% 平均 CI 為 $(-33.1485,58.1974)$，個別 PI 為 $(-67.0652,92.1140)$。
5. **解讀結論：** 樣本內 $R^2$ 很高，但 1% 水準仍不顯著；區間極寬且下界為負，顯示資料太少，實務上銷量的非負限制也提醒線性常態模型在尾端不理想。

#### 計算題 21 <a id="exam-ch14-problem-21"></a>

##### 題目

> Six days of coffee sales and temperature are:

| Cups Sold $Y$ | Temperature $X$ |
|---:|---:|
| 350 | 50 |
| 200 | 60 |
| 210 | 70 |
| 100 | 80 |
| 60 | 90 |
| 40 | 100 |

> a. Identify the dependent variable. b. Compute the line. c. Compute $r$. d. Test at .05 with hypotheses. e. Predict sales at 90 degrees.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$r$](./course2-slides-handout.html#formula-slr-correlation)、[$t$](./course2-slides-handout.html#formula-slr-t-test)


1. **辨認題型：** 溫度預測咖啡銷量。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$r$](./course2-slides-handout.html#formula-slr-correlation)與[$t$](./course2-slides-handout.html#formula-slr-t-test)。
3. **檢查假設：** $Y$ 是 cups sold，$X$ 是 temperature；不同天可能有星期或趨勢依賴，需檢查。
4. **代入計算／推理：** $\hat y=605.7143-5.94286x$；$r=-.95197$。$H_0:\beta_1=0$ 對 $H_a:\beta_1\ne0$；$t=-6.2180$、$df=4$、$p=.003405$。在 90 度，$\hat y=70.8571$ 杯。
5. **解讀結論：** 在 5% 水準有顯著負線性關係；90 度日預估約售 71 杯。

#### 計算題 22 <a id="exam-ch14-problem-22"></a>

##### 題目

> Hours of television watched and age are:

| Hours of Television $Y$ | Age $X$ |
|---:|---:|
| 1 | 45 |
| 3 | 30 |
| 4 | 22 |
| 3 | 25 |
| 6 | 5 |

> a. Identify the dependent variable. b. Compute the line. c. Test at .05 with hypotheses. d. Compute and interpret $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 年齡預測看電視時數。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** 依題目排列，hours 是 $Y$、age 是 $X$；$n=5$，需特別檢查線性與離群。
4. **代入計算／推理：** $\hat y=6.56433-.12458x$。$H_0:\beta_1=0$；$t=-12.0179$、$df=3$、$p=.001240$。$R^2=.97965$。
5. **解讀結論：** 在 5% 水準有顯著負線性關係；年齡的線性關係解釋約 $97.97\%$ 的這五人看電視時數變異，但樣本極小，不能外推整體人口。

#### 計算題 23 <a id="exam-ch14-problem-23"></a>

##### 題目

> Seven observations are $(2,12),(3,9),(6,8),(7,7),(8,6),(7,5),(9,2)$.<br>
> a. Develop the equation. b. Test the slope at 95% confidence. c. Perform an $F$ test at .05. d. Compute $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 負向原始資料迴歸。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** 七點應檢查散佈與殘差；重複 $x=7$ 可幫助看同一 $x$ 的個體波動。
4. **代入計算／推理：** $\hat y=13.75-1.125x$；$t=-5.1962$、$df=5$、$p=.003478$；$F=27$、同一 $p$；$R^2=.84375$。
5. **解讀結論：** 在 5% 水準有顯著負線性關係，模型解釋約 $84.38\%$ 的樣本變異。

### 計算題｜第 24–33 題：商業情境、預測與完整推論

#### 計算題 24 <a id="exam-ch14-problem-24"></a>

##### 題目

> A retail store has weekly data:

| Week | Advertising Cost $X$ ($) | Profit $Y$ ($) |
|---:|---:|---:|
| 1 | 0 | 200 |
| 2 | 50 | 270 |
| 3 | 250 | 420 |
| 4 | 150 | 300 |
| 5 | 125 | 325 |

> a. Write the appropriate linear relationship and identify variables. b. Calculate the line. c. Predict profit at $\$200$ advertising. d. Test significance at 95% confidence. e. Compute $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 廣告成本 $X$ 預測利潤 $Y$。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** 週資料可能有時間依賴；$n=5$ 很小。$x=200$ 在觀察範圍內。
4. **代入計算／推理：** 模型 $Y=\beta_0+\beta_1X+\epsilon$；$\hat y=210.0676+.808108x$。$x=200$ 時 $\hat y=371.6892$ 美元。$t=6.4964$、$df=3$、$p=.007406$；$R^2=.93363$。
5. **解讀結論：** 在 5% 水準有顯著正線性關係，約 $93.36\%$ 的樣本利潤變異由廣告成本的線性關係解釋；預測利潤約 $\$371.69$。

#### 計算題 25 <a id="exam-ch14-problem-25"></a>

##### 題目

> A bakery records customer expenditure $Y$ and income $X$ (in thousands):

| Expenditure $Y$ | Income $X$ |
|---:|---:|
| 0.45 | 20 |
| 10.75 | 19 |
| 5.40 | 22 |
| 7.80 | 25 |
| 5.60 | 14 |

> The least squares line is $\hat Y=4.348+0.0826X$.<br>
> a. Obtain a fit measure. b. Test the relationship at 5% and state hypotheses. c. Construct a 95% CI for average expenditure at income $\$20{,}000$. d. Construct a 95% PI for one customer at income $\$20{,}000$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)、[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)


1. **辨認題型：** 配適、斜率檢定、平均 CI 與個別 PI。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[平均 CI](./course2-slides-handout.html#formula-slr-mean-ci)與[個別 PI](./course2-slides-handout.html#formula-slr-prediction-interval)。
3. **檢查假設：** PDF 第一筆是 **0.45** ，不是 45；逐頁畫面與文字層已交叉確認。$x^*=20$ 恰為 $\bar x$。樣本只有 5 人，常態與離群值很敏感。
4. **代入計算／推理：** 用未四捨五入係數得 $\hat y=4.34848+.082576x$。$R^2=.007878$。$H_0:\beta_1=0$ 對 $H_a:\beta_1\ne0$；$t=.15434$、$df=3$、$p=.88714$。在 $x=20$，$\hat y=6.00$；95% 平均 CI 為 $(-0.1860,12.1860)$，個別 PI 為 $(-9.1526,21.1526)$。
5. **解讀結論：** 在 5% 水準沒有線性關係證據，模型只解釋約 $0.79\%$ 變異。負下界也顯示小樣本常態線性區間對非負支出的實務限制；PI 比 CI 寬。

#### 計算題 26 <a id="exam-ch14-problem-26"></a>

##### 題目

> Annual income $Y$ (thousands) and years of college $X$ are $(28,0),(40,3),(36,2),(28,1),(48,4)$.<br>
> a. Develop the equation. b. Estimate income at 6 years. c. Compute $R^2$. d. Test slope at .05. e. Perform an $F$ test at .05.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)


1. **辨認題型：** 教育年數預測收入。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)及[$t/F$](./course2-slides-handout.html#formula-slr-f-test)。
3. **檢查假設：** $x=6$ 超過樣本 0–4，是外插；樣本只有 5。
4. **代入計算／推理：** $\hat y=25.6+5.2x$；$x=6$ 時 $\hat y=56.8$ 千美元。$R^2=.93889$；$t=6.7890$、$df=3$、$p=.006533$；$F=46.0909$、同一 $p$。
5. **解讀結論：** 在 5% 水準有顯著正線性關係，約 $93.89\%$ 樣本變異被解釋；$\$56{,}800$ 是外插預測，可信度比樣本範圍內低。

#### 計算題 27 <a id="exam-ch14-problem-27"></a>

##### 題目

> A woman's age $X$ and annual book expenditure $Y$ are $(18,210),(22,180),(21,220),(28,280)$.<br>
> a. Develop the equation. b. Compute $R^2$. c. Test slope at .05. d. Perform an $F$ test at .05.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 極小樣本正斜率迴歸。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-t-test)和[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $n=4$、$df=2$；結果會被單點強烈影響。
4. **代入計算／推理：** $\hat y=54.8341+7.53555x$；$R^2=.56784$；$t=1.6211$、$p=.24645$；$F=2.62796$、同一 $p$。
5. **解讀結論：** 在 5% 水準不拒絕 $H_0$；樣本內雖解釋約 $56.78\%$，仍不足以確認母體線性關係。

#### 計算題 28 <a id="exam-ch14-problem-28"></a>

##### 題目

> Heavy-equipment salespeople data:

| Years of College $X$ | Annual Income $Y$ (thousands) |
|---:|---:|
| 2 | 20 |
| 2 | 23 |
| 3 | 25 |
| 4 | 26 |
| 3 | 28 |
| 1 | 29 |
| 4 | 27 |
| 3 | 30 |
| 4 | 33 |
| 4 | 35 |

> a. Identify variables. b. Determine the line. c. Predict income at one year of college. d. Test at .05. e. Compute $R^2$. f. Compute and interpret $r$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$r$](./course2-slides-handout.html#formula-slr-correlation)


1. **辨認題型：** 教育年數 $X$ 預測年收入 $Y$。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)與[$r$](./course2-slides-handout.html#formula-slr-correlation)。
3. **檢查假設：** 同一年數有不同收入，符合個體誤差概念；仍需檢查線性、等變異、獨立與離群。
4. **代入計算／推理：** $\hat y=21.6+2x$。$x=1$ 時預測 $23.6$ 千美元。$t=1.5097$、$df=8$、$p=.16956$；$R^2=.22173$；$r=.47088$。
5. **解讀結論：** 在 5% 水準沒有顯著線性證據；約 $22.17\%$ 的樣本收入變異被解釋，相關為中度正向但不顯著。

#### 計算題 29 <a id="exam-ch14-problem-29"></a>

##### 題目

> Yearly income $Y$ (thousands) and age $X$ for seven individuals are $(20,18),(24,20),(24,23),(25,34),(26,24),(27,27),(34,27)$, where each pair is $(Y,X)$.<br>
> a. Develop the equation. b. Estimate income at age 30. c. Compute $R^2$. d. Test slope at .05. e. Perform an $F$ test at .05.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 年齡預測收入。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t/F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $n=7$；需留意同為 27 歲卻收入差 7 千美元，並檢查離群與等變異。
4. **代入計算／推理：** $\hat y=16.2039+.384812x$。30 歲預測 $27.7483$ 千美元。$R^2=.22657$；$t=1.2102$、$df=5$、$p=.28027$；$F=1.46468$。
5. **解讀結論：** 在 5% 水準不顯著；模型只解釋約 $22.66\%$ 的樣本收入變異，30 歲點預測約 $\$27{,}748$。

#### 計算題 30 <a id="exam-ch14-problem-30"></a>

##### 題目

> Aptitude test score $Y$ and GPA $X$ for 10 students are $(26,1.8),(31,2.3),(28,2.6),(30,2.4),(34,2.8),(38,3.0),(41,3.4),(44,3.2),(40,3.6),(43,3.8)$, written as $(Y,X)$.<br>
> a. Develop the line. b. Compute $R^2$ and comment on strength. c. Test slope at .05. d. Perform an $F$ test at .05.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$t/F$](./course2-slides-handout.html#formula-slr-t-test)


1. **辨認題型：** GPA 預測測驗分數。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[最小平線](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)與[$t/F$](./course2-slides-handout.html#formula-slr-t-test)。
3. **檢查假設：** 學生觀察值應獨立；散佈圖需近似直線且無極端點。
4. **代入計算／推理：** $\hat y=8.17092+9.45643x$。$R^2=.83005$；$t=6.2508$、$df=8$、$p=.000245$；$F=39.0729$。
5. **解讀結論：** 在 5% 水準有顯著且強的正線性關係，GPA 的線性關係解釋約 $83.01\%$ 的樣本測驗分數變異。

#### 計算題 31 <a id="exam-ch14-problem-31"></a>

##### 題目

> Sales $Y$ are in millions of dollars and advertising $X$ in thousands of dollars. Output: constant $4.00$ (SE $.800$), slope $.12$ (SE $.045$), regression $df=1$, $SS=1400$, error $df=18$, $SS=3600$.<br>
> a. Find $n$. b. Test relationship at .05. c. Compute $R^2$. d. Interpret it. e. Predict sales for $\$4{,}000$ advertising in dollars.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[估計式](./course2-slides-handout.html#formula-slr-estimated-line)


1. **辨認題型：** 輸出判讀與尺度換算。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)和[估計式](./course2-slides-handout.html#formula-slr-estimated-line)。
3. **檢查假設：** $n=18+2=20$；$X$ 單位為千美元、$Y$ 為百萬美元。
4. **代入計算／推理：** $t=.12/.045=2.6667$、$df=18$、$p\approx.0157$。$R^2=1400/(1400+3600)=.28$。$\$4{,}000$ 對應 $x=4$，$\hat y=4+.12(4)=4.48$ 百萬美元。
5. **解讀結論：** 在 5% 水準有顯著正線性關係；廣告的線性關係解釋約 $28\%$ 的樣本銷售變異，預測銷售為 $\$4{,}480{,}000$。

#### 計算題 32 <a id="exam-ch14-problem-32"></a>

##### 題目

> Daily demand $Y$ is in thousands of units and unit price $X$ in hundreds of dollars. $n=15$, $\sum X=75$, $\sum Y=135$, $S_{xy}=-59$, $S_{xx}=94$, $SST=100$, $SSE=62.9681$.<br>
> a. Develop the line. b. Compute $R^2$. c. Perform an $F$ test at .05. d. Would demand reach zero, and at what price?

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)、[$F$](./course2-slides-handout.html#formula-slr-f-test)


1. **辨認題型：** 摘要統計建立負斜率模型、推論與零點外插。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)與[$F$](./course2-slides-handout.html#formula-slr-f-test)。
3. **檢查假設：** $\bar x=5$、$\bar y=9$；線性模型的零點若遠離資料範圍只能視為數學外插。
4. **代入計算／推理：** $b_1=-59/94=-.627660$，$b_0=9-(-.627660)(5)=12.1383$，故 $\hat y=12.1383-.627660x$。$R^2=1-62.9681/100=.370319$。$SSR=37.0319$、$MSE=62.9681/13=4.8437$、$F=7.6454$、$p=.01607$。令 $\hat y=0$ 得 $x=19.34$ 個百美元，約 $\$1{,}934$。
5. **解讀結論：** 在 5% 水準有顯著負線性關係，約 $37.03\%$ 樣本需求變異被解釋。模型數學上在約 $\$1{,}934$ 預測零需求，但若該價格超出觀察範圍，不應宣稱真實需求必然在此歸零。

#### 計算題 33 <a id="exam-ch14-problem-33"></a>

##### 題目

> A regression analysis gives $\sum X=42$, $\sum Y=63$, $n=7$, $S_{xy}=37$, $S_{xx}=84$, $SST=28$, and $SSE=11.7024$.<br>
> a. Develop the equation. b. Test slope at 95% confidence. c. Perform an $F$ test at .05. d. Compute $R^2$.

##### 詳解

> **回看投影片講義：** [方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)、[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)、[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)


1. **辨認題型：** 摘要統計的完整迴歸推論。
2. **選方法：** 依[方法選擇](./course2-slides-handout.html#compare-ch14-method-selection)，用[斜率截距](./course2-slides-handout.html#formula-slr-slope-intercept)、[$t$](./course2-slides-handout.html#formula-slr-t-test)、[$F$](./course2-slides-handout.html#formula-slr-f-test)與[$R^2$](./course2-slides-handout.html#formula-slr-r-squared)。
3. **檢查假設：** $\bar x=6$、$\bar y=9$、$df_E=5$；推論仍依賴殘差假設。
4. **代入計算／推理：** $b_1=37/84=.440476$，$b_0=9-.440476(6)=6.35714$，故 $\hat y=6.35714+.440476x$。$SSR=28-11.7024=16.2976$，$MSE=11.7024/5=2.34048$，$F=6.96336$、$p=.04604$；簡單迴歸 $t=\sqrt F=2.6388$，正斜率故取正值；$R^2=16.2976/28=.582057$。
5. **解讀結論：** 在 5% 水準剛好拒絕 $H_0:\beta_1=0$，有正線性關係證據；模型解釋約 $58.21\%$ 的樣本 $Y$ 變異。由於 $p$ 接近 .05，四捨五入與假設診斷都很重要。

<div class="page-break" style="page-break-after: always;"></div>

# 第 15 章：複迴歸｜考古題詳解

## 考古題詳解

本章收錄 115 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–20 題：模型、假設與基本名詞

#### 選擇題 1 <a id="exam-ch15-mc-1"></a>

##### 題目

> The mathematical equation relating the expected value of the dependent variable to the value of the independent variables, which has the form of $E(y)=\beta_0+\beta_1x_1+\beta_2x_2+\cdots+\beta_px_p$, is
>
> a. a simple linear regression model<br>
> b. a multiple nonlinear regression model<br>
> c. an estimated multiple regression equation<br>
> d. a multiple regression equation

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[複迴歸平均方程式](./course2-slides-handout.html#formula-multiple-regression-mean)


1. **辨認題型：** 這是母體平均反應方程式的名稱辨認。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，看到多個 $x$ 與母體參數 $\beta$，回看[複迴歸平均方程式](./course2-slides-handout.html#formula-multiple-regression-mean)。
3. **檢查假設：** 題目只辨認符號，不需用樣本做推論；注意式中沒有誤差項。
4. **代入計算／推理：** $E(y)$ 與 $\beta$ 表示母體的 multiple regression equation，故選 d。選項 a 只有一個 $x$；b 誤稱非線性；c 應使用樣本係數 $b$ 與 $\hat y$。
5. **解讀結論：** 正確答案是 **d** ；它描述固定各 $x$ 時的母體平均 $y$。

**選項逐一：** a 容易因看到 regression 而選，但 simple 只能有一個 $x$；b 錯在此式對各 $x$ 是線性的；c 錯在估計式應使用 $b_j$ 與 $\hat y$；d 正確，這是用母體參數表示的複迴歸平均方程式。

#### 選擇題 2 <a id="exam-ch15-mc-2"></a>

##### 題目

> The estimate of the multiple regression equation based on the sample data, which has the form of $\hat y=b_0+b_1x_1+b_2x_2+\cdots+b_px_p$, is
>
> a. a simple linear regression model<br>
> b. a multiple nonlinear regression model<br>
> c. an estimated multiple regression equation<br>
> d. a multiple regression equation

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 樣本估計式名稱辨認。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，回看[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 只需分清 $b$ 是樣本估計、$\beta$ 是母體參數。
4. **代入計算／推理：** 式中是 $\hat y$ 與 $b_j$，故為 estimated multiple regression equation。a 少了多個 $x$；b 不是非線性；d 通常指母體平均方程式。
5. **解讀結論：** 正確答案是 **c** ；它用樣本估計給定 $x$ 時的平均反應。

**選項逐一：** a 錯在 simple 只含一個解釋變數；b 錯在方程式仍是線性加總；c 正確，$\hat y$ 與 $b_j$ 表示由樣本得到的估計式；d 容易與母體方程式混淆，但母體式應使用 $\beta_j$。

#### 選擇題 3 <a id="exam-ch15-mc-3"></a>

##### 題目

> The mathematical equation that explains how the dependent variable $y$ is related to several independent variables $x_1,x_2,\ldots,x_p$ and the error term $\epsilon$ is
>
> a. a simple nonlinear regression model<br>
> b. a multiple regression model<br>
> c. an estimated multiple regression equation<br>
> d. a multiple regression equation

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 含誤差項的母體模型名稱辨認。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)。
3. **檢查假設：** 題幹明示 several independent variables 與 $\epsilon$。
4. **代入計算／推理：** $y=\beta_0+\sum\beta_jx_j+\epsilon$ 是 multiple regression model。a 誤稱 simple/nonlinear；c 沒有母體誤差項；d 指 $E(y)$ 的平均方程式。
5. **解讀結論：** 正確答案是 **b** ；模型包含平均結構與個別觀測的隨機誤差。

**選項逐一：** a 同時錯在 simple 與 nonlinear；b 正確，個別 $y$、多個 $x$ 與 $\epsilon$ 構成複迴歸模型；c 錯在估計式使用 $b_j$ 且不含母體誤差項；d 是不含 $\epsilon$ 的平均方程式，不是完整模型。

#### 選擇題 4 <a id="exam-ch15-mc-4"></a>

##### 題目

> A measure of the effect of an unusual $x$ value on the regression results is called
>
> a. Cook's D<br>
> b. Leverage<br>
> c. odd ratio<br>
> d. unusual regression

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[槓桿值規則](./course2-slides-handout.html#formula-leverage-rule)


1. **辨認題型：** 異常 $x$ 位置的診斷量。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，只問 $x$ 離中心多遠時看[槓桿值規則](./course2-slides-handout.html#formula-leverage-rule)。
3. **檢查假設：** 題目只問 unusual $x$，沒有同時要求殘差大小。
4. **代入計算／推理：** leverage 只由 $x$ 位置決定，故 b。Cook's D 同時看槓桿與殘差；odd ratio 屬 logistic；d 不是標準術語。
5. **解讀結論：** 正確答案是 **b** ；高槓桿代表 $x$ 組合不尋常，不等於一定有影響力。

**選項逐一：** a Cook's D 也談影響力，容易誤選，但它同時結合殘差與槓桿；b 正確，leverage 專門衡量 $x$ 位置是否異常；c odds ratio 屬於邏輯斯迴歸；d 不是標準統計術語。

#### 選擇題 5 <a id="exam-ch15-mc-5"></a>

##### 題目

> A variable that cannot be measured in terms of how much or how many but instead is assigned values to represent categories is called
>
> a. an interaction<br>
> b. a constant variable<br>
> c. a category variable<br>
> d. a qualitative variable

##### 詳解

> **回看投影片講義：** [連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)


1. **辨認題型：** 變數型態辨認。
2. **選方法：** 依[連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，先判斷數字是否有數量意義。
3. **檢查假設：** 題幹說數值只是代表類別，不能做有意義的加減距離。
4. **代入計算／推理：** 標準名稱是 qualitative variable，故 d。a 是模型項；b 是不變量；c 口語接近但不是本題教材採用的術語。
5. **解讀結論：** 正確答案是 **d** ；進入迴歸時通常要轉成虛擬變數。

**選項逐一：** a interaction 是變數共同作用的模型項；b constant variable 不隨觀測改變；c category variable 口語上相近，容易誤選，但本題教材採用的正式名稱不是它；d qualitative variable 是正確術語。

#### 選擇題 6 <a id="exam-ch15-mc-6"></a>

##### 題目

> In order to test for the significance of a regression model involving 3 independent variables and 47 observations, the numerator and denominator degrees of freedom (respectively) for the critical value of $F$ are
>
> a. 47 and 3<br>
> b. 3 and 47<br>
> c. 2 and 43<br>
> d. 3 and 43

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)、[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$ 檢定自由度。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)，使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=3$、$n=47$，模型含截距。
4. **代入計算／推理：** 分子 $df=p=3$；分母 $df=n-p-1=47-3-1=43$。a、b 忘記誤差自由度；c 又少算一個斜率。
5. **解讀結論：** 正確答案是 **d** ，查 $F_{3,43}$。

**選項逐一：** a 把樣本數與變數數放錯位置；b 雖把 3 放分子，但分母不能直接用 $n=47$；c 把分子自由度誤算為 2；d 正確，$(df_1,df_2)=(3,47-3-1)=(3,43)$。

#### 選擇題 7 <a id="exam-ch15-mc-7"></a>

##### 題目

> In regression analysis, an outlier is an observation whose
>
> a. mean is larger than the standard deviation<br>
> b. residual is zero<br>
> c. mean is zero<br>
> d. residual is much larger than the rest of the residual values

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[標準化殘差](./course2-slides-handout.html#formula-standardized-residual)


1. **辨認題型：** 離群值定義。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，以[標準化殘差](./course2-slides-handout.html#formula-standardized-residual)比較偏離程度。
3. **檢查假設：** 離群是相對迴歸面而言，不是比較樣本平均數。
4. **代入計算／推理：** 異常大的殘差符合 d。a、c 混淆平均；b 反而表示觀測落在配適面上。
5. **解讀結論：** 正確答案是 **d** ；實務上再用標準化或 deleted residual 判斷。

**選項逐一：** a 平均數與標準差的大小不能定義迴歸離群值；b 殘差為 0 代表點落在配適面上；c 平均為 0 與單一觀測是否離群無關；d 正確，離群值的殘差相對其他觀測特別大。

#### 選擇題 8 <a id="exam-ch15-mc-8"></a>

##### 題目

> A variable that takes on the values of 0 or 1 and is used to incorporate the effect of qualitative variables in a regression model is called
>
> a. an interaction<br>
> b. a constant variable<br>
> c. a dummy variable<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)


1. **辨認題型：** 0/1 類別編碼名稱。
2. **選方法：** 依[連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)判斷。
3. **檢查假設：** 題目說 0/1 是為了表示 qualitative variable。
4. **代入計算／推理：** 這正是 dummy variable，故 c。a 通常是變數乘積；b 不隨觀測改變；d 因 c 已正確而錯。
5. **解讀結論：** 正確答案是 **c** ；係數要相對 0 所代表的參考組解讀。

**選項逐一：** a interaction 不是單純的 0/1 類別編碼；b constant variable 不會在 0 與 1 間隨組別改變；c 正確，這就是 dummy variable；d 錯，因為 c 已給出正確名稱。

#### 選擇題 9 <a id="exam-ch15-mc-9"></a>

##### 題目

> In a multiple regression model, the error term $\epsilon$ is assumed to be a random variable with a mean of
>
> a. zero<br>
> b. $-1$<br>
> c. 1<br>
> d. any value

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 誤差假設。
2. **選方法：** 依[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)的 $E(\epsilon)=0$。
3. **檢查假設：** 是對固定 $x$ 條件下的誤差平均而言。
4. **代入計算／推理：** 平均為 0 才使 $E(y)=\beta_0+\sum\beta_jx_j$，故 a。b、c 會造成系統偏差；d 不足以定義平均反應。
5. **解讀結論：** 正確答案是 **a** ；不是說每筆誤差都等於 0。

**選項逐一：** a 正確，模型假設固定 $x$ 時 $E(\epsilon)=0$；b 錯在平均設為 $-1$ 會造成系統性負偏差；c 錯在平均設為 1 會造成系統性正偏差；d 容易因誤差是隨機變數而選，但它的平均不能任意，必須指定為 0。

#### 選擇題 10 <a id="exam-ch15-mc-10"></a>

##### 題目

> In regression analysis, the response variable is the
>
> a. independent variable<br>
> b. dependent variable<br>
> c. slope of the regression function<br>
> d. intercept

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 迴歸角色名稱。
2. **選方法：** 回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)，反應變數是左側的 $y$。
3. **檢查假設：** 只需區分被解釋的 $y$ 與解釋變數 $x$。
4. **代入計算／推理：** response variable 就是 dependent variable，故 b。a 是 $x$；c、d 是模型參數角色。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a independent variable 是用來解釋的 $x$；b 正確，response variable 就是 dependent variable $y$；c slope 是係數而不是變數；d intercept 也是係數而不是反應變數。

#### 選擇題 11 <a id="exam-ch15-mc-11"></a>

##### 題目

> A multiple regression model has
>
> a. only one independent variable<br>
> b. more than one dependent variable<br>
> c. more than one independent variable<br>
> d. at least 2 dependent variables

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)


1. **辨認題型：** 複迴歸定義。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)。
3. **檢查假設：** 本章模型仍只有一個反應 $y$。
4. **代入計算／推理：** multiple 指多個 independent variables，故 c。a 是簡單迴歸；b、d 誤把多重放在 $y$。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 只有一個 independent variable 是簡單迴歸；b 錯在複迴歸仍只有一個 dependent variable；c 正確，複迴歸有多個 independent variables 但仍只有一個 $y$；d 同樣錯在宣稱至少有 2 個 dependent variables。

#### 選擇題 12 <a id="exam-ch15-mc-12"></a>

##### 題目

> A measure of goodness of fit for the estimated regression equation is the
>
> a. multiple coefficient of determination<br>
> b. mean square due to error<br>
> c. mean square due to regression<br>
> d. sample size

##### 詳解

> **回看投影片講義：** [$R^2$ 與調整後 $R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 配適度摘要辨認。
2. **選方法：** 依[$R^2$ 與調整後 $R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)，回看[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** 題目問解釋變異比例，不是單一均方。
4. **代入計算／推理：** multiple coefficient of determination 即 $R^2$，故 a。MSE 描述殘差尺度；MSR 用於 $F$；樣本數不是配適指標。
5. **解讀結論：** 正確答案是 **a** ；高 $R^2$ 仍不代表因果或模型假設成立。

**選項逐一：** a 正確，multiple coefficient of determination 即 $R^2$，直接摘要配適；b MSE 描述殘差變異尺度；c MSR 是整體 $F$ 的分子成分；d sample size 影響精確度，但不是配適度量。

#### 選擇題 13 <a id="exam-ch15-mc-13"></a>

##### 題目

> The numerical value of the coefficient of determination
>
> a. is always larger than the coefficient of correlation<br>
> b. is always smaller than the coefficient of correlation<br>
> c. is negative if the coefficient of determination is negative<br>
> d. can be larger or smaller than the coefficient of correlation

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 與相關係數數值比較。
2. **選方法：** 回看[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)；在簡單迴歸中 $R^2=r^2$，而 $r$ 可正可負。
3. **檢查假設：** $R^2$ 不會為負；題目未限定 $r$ 的符號與大小。
4. **代入計算／推理：** 例如 $r=0.5$ 時 $R^2=0.25<r$；$r=-0.5$ 時 $R^2=0.25>r$，故 d。a、b 不是永遠；c 的前提不可能。
5. **解讀結論：** 正確答案是 **d** ；不要把相關方向和解釋比例混為一談。

**選項逐一：** a 不一定，正相關時 $r^2$ 常小於 $r$；b 也不一定，若比較帶正負號的 $r$，負相關時 $r^2>r$，且端點還可能相等；c 錯在 $R^2$ 不會因相關為負而變負；d 正確，按題目使用帶正負號的 correlation coefficient 時，$R^2$ 可大於或小於 $r$。

#### 選擇題 14 <a id="exam-ch15-mc-14"></a>

##### 題目

> The adjusted multiple coefficient of determination is adjusted for
>
> a. the number of dependent variables<br>
> b. the number of independent variables<br>
> c. the number of equations<br>
> d. detrimental situations

##### 詳解

> **回看投影片講義：** [$R^2$ 與調整後 $R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)、[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)


1. **辨認題型：** 調整後 $R^2$ 的調整來源。
2. **選方法：** 依[$R^2$ 與調整後 $R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)，回看[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)。
3. **檢查假設：** 公式同時使用 $n$ 與獨立變數數 $p$。
4. **代入計算／推理：** 它對加入 independent variables 的複雜度調整，故 b。a 本章只有一個 $y$；c、d 不是公式成分。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 本章只有一個 dependent variable，並非調整來源；b 正確，adjusted $R^2$ 對 independent variables 的數量與樣本數作修正；c 方程式數量不在公式中；d 不是統計定義。

#### 選擇題 15 <a id="exam-ch15-mc-15"></a>

##### 題目

> In a multiple regression model, the variance of the error term $\epsilon$ is assumed to be
>
> a. the same for all values of the dependent variable<br>
> b. zero<br>
> c. the same for all values of the independent variable<br>
> d. $-1$

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 等變異假設。
2. **選方法：** 回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)的 $Var(\epsilon\mid x)=\sigma^2$。
3. **檢查假設：** 應在不同 $x$ 條件下比較誤差散布。
4. **代入計算／推理：** 變異對所有 independent-variable values 相同，故 c。a 把條件方向說反；b、d 都不可能作一般隨機誤差變異。
5. **解讀結論：** 正確答案是 **c** ；殘差圖若呈漏斗形就值得懷疑此假設。

**選項逐一：** a 容易因想到 $y$ 的散布而選，但等變異是假設固定不同 $x$ 值時誤差變異相同；b 變異為 0 會表示完全沒有隨機誤差；c 正確；d 變異不可能是負數。

#### 選擇題 16 <a id="exam-ch15-mc-16"></a>

##### 題目

> In multiple regression analysis, the correlation among the independent variables is termed
>
> a. homoscedasticity<br>
> b. linearity<br>
> c. multicollinearity<br>
> d. adjusted coefficient of determination

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 解釋變數彼此相關的名稱。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)旁的共線性提醒。
3. **檢查假設：** 題目說的是 independent variables 彼此相關，不是誤差變異。
4. **代入計算／推理：** 名稱是 multicollinearity，故 c。a 是等變異；b 是模型形狀；d 是配適指標。
5. **解讀結論：** 正確答案是 **c** ；它可能放大個別係數標準誤。

**選項逐一：** a homoscedasticity 是誤差等變異；b linearity 是平均反應形式；c 正確，解釋變數彼此相關稱 multicollinearity；d adjusted coefficient of determination 是配適指標。

#### 選擇題 17 <a id="exam-ch15-mc-17"></a>

##### 題目

> In a multiple regression model, the values of the error term $\epsilon$ are assumed to be
>
> a. zero<br>
> b. dependent on each other<br>
> c. independent of each other<br>
> d. always negative

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 誤差獨立假設。
2. **選方法：** 回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)的推論條件。
3. **檢查假設：** 是不同觀測的誤差彼此獨立，不是每個誤差等於 0。
4. **代入計算／推理：** 故 c。a 混淆平均為 0；b 正好違反假設；d 沒有理論依據。
5. **解讀結論：** 正確答案是 **c** ；時間序列資料尤其要檢查這點。

**選項逐一：** a 把『誤差平均為 0』誤解成每個誤差都為 0；b 正好違反獨立性假設；c 正確，不同觀測的誤差應彼此獨立；d 誤差可正可負，不會永遠為負。

#### 選擇題 18 <a id="exam-ch15-mc-18"></a>

##### 題目

> In a multiple regression model, the error term $\epsilon$ is assumed to
>
> a. have a mean of 1<br>
> b. have a variance of zero<br>
> c. have a standard deviation of 1<br>
> d. be normally distributed

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 小樣本推論的誤差分配假設。
2. **選方法：** 回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)的常態誤差條件。
3. **檢查假設：** 平均應為 0、變異為未知 $\sigma^2>0$，不是固定為 1。
4. **代入計算／推理：** d 是教材假設。a 平均錯；b 會使資料完全無隨機散布；c 不要求標準差恰為 1。
5. **解讀結論：** 正確答案是 **d** ；這是推論假設，不表示觀測值本身都呈標準常態。

**選項逐一：** a 平均應為 0 而不是 1；b 變異應為未知的 $\sigma^2>0$；c 標準差不必固定為 1；d 正確，教材的小樣本推論假設誤差近似常態。

#### 選擇題 19 <a id="exam-ch15-mc-19"></a>

##### 題目

> In multiple regression analysis,
>
> a. there can be any number of dependent variables but only one independent variable<br>
> b. there must be only one independent variable<br>
> c. the coefficient of determination must be larger than 1<br>
> d. there can be several independent variables, but only one dependent variable

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)


1. **辨認題型：** 複迴歸資料結構。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)。
3. **檢查假設：** 本章是單一連續 $y$、多個 $x$。
4. **代入計算／推理：** d 正確。a、b 把變數數目說反；c 違反 $0\le R^2\le1$。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 把 dependent 與 independent 的數量說反；b 是簡單迴歸的限制；c 錯在 $R^2$ 不會大於 1；d 正確，複迴歸容許多個 $x$，但本章仍只有一個 $y$。

#### 選擇題 20 <a id="exam-ch15-mc-20"></a>

##### 題目

> A regression model in which more than one independent variable is used to predict the dependent variable is called
>
> a. a simple linear regression model<br>
> b. a multiple regression model<br>
> c. an independent model<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)


1. **辨認題型：** 模型名稱辨認。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)。
3. **檢查假設：** 題幹明示 more than one independent variable。
4. **代入計算／推理：** 這就是 multiple regression model，故 b。a 只有一個 $x$；c 不是標準名稱；d 因 b 正確而錯。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a simple linear regression 只有一個解釋變數；b 正確，多於一個 independent variable 就是 multiple regression；c independent model 不是標準名稱；d 錯，因為 b 已正確。

### 選擇題｜第 21–44 題：方法選擇、自由度與變異分解

#### 選擇題 21 <a id="exam-ch15-mc-21"></a>

##### 題目

> A term used to describe the case when the independent variables in a multiple regression model are correlated is
>
> a. regression<br>
> b. correlation<br>
> c. multicollinearity<br>
> d. None of the above answers is correct.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 解釋變數互相關聯的術語。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)判斷共線性。
3. **檢查假設：** 關聯發生在多個 $x$ 之間。
4. **代入計算／推理：** c 的 multicollinearity 是專名；a 是分析方法；b 太籠統；d 因 c 正確而錯。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a regression 是整體分析名稱，不是 $x$ 間相關的專名；b correlation 只泛指關聯，沒有指出複迴歸中的問題；c 正確，這種情況稱 multicollinearity；d 錯，因為 c 已正確。

#### 選擇題 22 <a id="exam-ch15-mc-22"></a>

##### 題目

> A variable that cannot be measured in numerical terms is called
>
> a. a nonmeasurable random variable<br>
> b. a constant variable<br>
> c. a dependent variable<br>
> d. a qualitative variable

##### 詳解

> **回看投影片講義：** [連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)


1. **辨認題型：** 類別型變數名稱。
2. **選方法：** 依[連續變數與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)。
3. **檢查假設：** 題幹表示類別而非有單位的數量。
4. **代入計算／推理：** d 是標準術語；a 不是教材名稱；b 是固定值；c 只說模型角色。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a nonmeasurable random variable 不是教材術語；b constant variable 是固定不變的量；c dependent variable 描述模型角色，仍可為數值；d 正確，不能以數量尺度衡量的變數稱 qualitative variable。

#### 選擇題 23 <a id="exam-ch15-mc-23"></a>

##### 題目

> In logistic regression,
>
> a. there can only be two independent variables<br>
> b. there are two dependent variables<br>
> c. the dependent variable only assumes two discrete values<br>
> d. the dependent variable only assumes two continuous values

##### 詳解

> **回看投影片講義：** [線性機率與 logistic 比較](./course2-slides-handout.html#compare-ch15-linear-probability-vs-logistic)、[logistic 模型](./course2-slides-handout.html#formula-logistic-regression)


1. **辨認題型：** logistic 適用的 $y$ 型態。
2. **選方法：** 依[線性機率與 logistic 比較](./course2-slides-handout.html#compare-ch15-linear-probability-vs-logistic)，回看[logistic 模型](./course2-slides-handout.html#formula-logistic-regression)。
3. **檢查假設：** $y$ 是單一變數，常編為 0/1；$x$ 數量不受限於 2。
4. **代入計算／推理：** c 正確。a 限錯 $x$ 數；b 把兩個值誤當兩個變數；d 把離散說成連續。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a logistic regression 的解釋變數數量不限於 2；b 仍只有一個 dependent variable；c 正確，dependent variable 只取兩個離散值；d 錯在二元結果不是兩個連續值。

#### 選擇題 24 <a id="exam-ch15-mc-24"></a>

##### 題目

> In a situation where the dependent variable can assume only one of the two possible discrete values,
>
> a. we must use multiple regression<br>
> b. there can only be two independent variables<br>
> c. logistic regression should be applied<br>
> d. all the independent variables must have values of either zero or one

##### 詳解

> **回看投影片講義：** [線性機率與 logistic 比較](./course2-slides-handout.html#compare-ch15-linear-probability-vs-logistic)


1. **辨認題型：** 二元結果的方法選擇。
2. **選方法：** 依[線性機率與 logistic 比較](./course2-slides-handout.html#compare-ch15-linear-probability-vs-logistic)。
3. **檢查假設：** 二元的是 $y$；$x$ 可為連續或類別。
4. **代入計算／推理：** 應用 logistic，故 c。a 的普通複迴歸可能預測越界；b、d 對 $x$ 作了不存在的限制。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 普通 multiple regression 可能產生小於 0 或大於 1 的預測；b independent variables 的數量不限於 2；c 正確，二元 dependent variable 應考慮 logistic regression；d 錯在解釋變數可為連續數值，不必全是 0/1。

#### 選擇題 25 <a id="exam-ch15-mc-25"></a>

##### 題目

> In a regression model involving more than one independent variable, which of the following tests must be used in order to determine if the relationship between the dependent variable and the set of independent variables is significant?
>
> a. $t$ test<br>
> b. $F$ test<br>
> c. Either a $t$ test or a chi-square test can be used.<br>
> d. chi-square test

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)、[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體模型顯著性。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)，使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 問的是整組連續結果複迴歸，不是單一係數或 logistic。
4. **代入計算／推理：** b 正確。a 一次檢查一個係數；c、d 的卡方不是普通複迴歸整體檢定。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a $t$ test 只檢查指定的個別斜率；b 正確，整組普通複迴歸的顯著性用 $F$ test；c 把個別 $t$ 與 logistic 的卡方混在一起；d chi-square test 不是普通連續 $y$ 複迴歸的整體檢定。

#### 選擇題 26 <a id="exam-ch15-mc-26"></a>

##### 題目

> For a multiple regression model, $SSR=600$ and $SSE=200$. The multiple coefficient of determination is
>
> a. 0.333<br>
> b. 0.275<br>
> c. 0.300<br>
> d. 0.75

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 計算。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=SSR+SSE=800$。
4. **代入計算／推理：** $R^2=600/800=0.75$，故 d。a 是 $SSE/SSR$；b、c 無正確分母。
5. **解讀結論：** 正確答案是 **d** ；樣本中 75% 的 $y$ 變異由模型解釋。

**選項逐一：** a 是 $SSE/SSR=200/600$，分母錯；b 的 0.275 不是任何正確平方和比例；c 的 0.300 也沒有使用正確的 $SSR/SST$；d 正確，$R^2=600/(600+200)=0.75$。

#### 選擇題 27 <a id="exam-ch15-mc-27"></a>

##### 題目

> In a multiple regression analysis involving 15 independent variables and 200 observations, $SST=800$ and $SSE=240$. The coefficient of determination is
>
> a. 0.300<br>
> b. 0.192<br>
> c. 0.500<br>
> d. 0.700

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 由 $SST,SSE$ 算 $R^2$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SSR=800-240=560$；變數數和樣本數不影響普通 $R^2$ 此步。
4. **代入計算／推理：** $R^2=1-240/800=0.700$，故 d。a 是未解釋比例；b、c 不是此比值。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是未解釋比例 $SSE/SST=0.300$；b 容易因混入變數數量而誤算；c 沒有對應的平方和比例；d 正確，$R^2=1-240/800=0.700$。

#### 選擇題 28 <a id="exam-ch15-mc-28"></a>

##### 題目

> A regression model involved 5 independent variables and 136 observations. The critical value of $t$ for testing the significance of each of the independent variable's coefficients will have
>
> a. 121 degrees of freedom<br>
> b. 135 degrees of freedom<br>
> c. 130 degrees of freedom<br>
> d. 4 degrees of freedom

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別斜率 $t$ 自由度。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=136,p=5$，模型含截距。
4. **代入計算／推理：** $df=n-p-1=130$，故 c。b 忘記估計斜率與截距；d 把自由度誤寫成 $p-1$；a 無此來源。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 容易由錯誤扣除 15 個量而得到，但公式不是如此；b 是 $n-1$，只適用總自由度；c 正確，$df=136-5-1=130$；d 是 $p-1$，不是誤差自由度。

#### 選擇題 29 <a id="exam-ch15-mc-29"></a>

##### 題目

> The multiple coefficient of determination is
>
> a. $MSR/MST$<br>
> b. $MSR/MSE$<br>
> c. $SSR/SST$<br>
> d. $SSE/SSR$

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 公式辨認。
2. **選方法：** 回看[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** 要比較總變異中被模型解釋的比例。
4. **代入計算／推理：** c 正確。b 是 $F$；a 不是標準比例；d 比較錯兩種平方和。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a $MSR/MST$ 不是判定係數公式；b $MSR/MSE$ 是整體 $F$；c 正確，$R^2=SSR/SST$；d $SSE/SSR$ 比較的是未解釋與已解釋平方和。

#### 選擇題 30 <a id="exam-ch15-mc-30"></a>

##### 題目

> A multiple regression model has the form $\hat y=7+2x_1+9x_2$. As $x_1$ increases by 1 unit (holding $x_2$ constant), $y$ is expected to
>
> a. increase by 9 units<br>
> b. decrease by 9 units<br>
> c. increase by 2 units<br>
> d. decrease by 2 units

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)、[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 部分斜率解讀。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)，回看[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 固定 $x_2$，只讓 $x_1$ 增加 1。
4. **代入計算／推理：** $x_1$ 係數是 $+2$，故 c。a、b 誤讀 $x_2$ 係數；d 看錯正負號。
5. **解讀結論：** 正確答案是 **c** ；預測平均 $y$ 增加 2 單位。

**選項逐一：** a 把 $x_2$ 的係數 9 當成 $x_1$ 的效果；b 不但用錯係數也看錯方向；c 正確，固定 $x_2$ 時 $x_1$ 增加 1 使預測 $y$ 增加 2；d 看錯 $+2$ 的正號。

#### 選擇題 31 <a id="exam-ch15-mc-31"></a>

##### 題目

> The correct relationship between $SST$, $SSR$, and $SSE$ is given by
>
> a. $SSR=SST+SSE$<br>
> b. $SSR=SST-SSE$<br>
> c. $SSE=SSR-SST$<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 變異分解。
2. **選方法：** 回看[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)中的 $SST=SSR+SSE$。
3. **檢查假設：** 含截距的最小平方法模型使用此分解。
4. **代入計算／推理：** 移項得 $SSR=SST-SSE$，故 b。a 多加一次；c 符號反；d 因 b 正確而錯。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 把 $SSE$ 重複加到總變異；b 正確，由 $SST=SSR+SSE$ 移項即得；c 會把非負的 $SSE$ 寫成錯誤負差；d 錯，因為 b 已是正確關係。

#### 選擇題 32 <a id="exam-ch15-mc-32"></a>

##### 題目

> In a multiple regression analysis $SSR=1,000$ and $SSE=200$. The $F$ statistic for this model is
>
> a. 5.0<br>
> b. 1,200<br>
> c. 800<br>
> d. Not enough information is provided to answer this question.

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$ 是否可由平方和直接算。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 還需要 $p$ 與 $n-p-1$ 才能把平方和轉成均方。
4. **代入計算／推理：** $F=(SSR/p)/(SSE/(n-p-1))$，題目未給 $n,p$，故 d。a 只是 $SSR/SSE$；b 是 $SST$；c 是差值。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a $SSR/SSE=5$ 容易誤選，但 $F$ 比較的是均方而非平方和；b 是 $SST=1,200$；c 是兩平方和的差；d 正確，缺少 $n$ 與 $p$ 就無法算 $MSR$、$MSE$。

#### 選擇題 33 <a id="exam-ch15-mc-33"></a>

##### 題目

> The ratio of $MSE/MSR$ yields
>
> a. $SST$<br>
> b. the $F$ statistic<br>
> c. $SSR$<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $F$ 比率方向。
2. **選方法：** 回看[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $F=MSR/MSE$，不是倒數。
4. **代入計算／推理：** $MSE/MSR=1/F$，不等於 a、b、c，故 d。b 是最容易因順序顛倒而選的誘答。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a $SST$ 是平方和，不會由兩個均方直接相除得到；b 容易因記得 $F$ 是均方比而誤選，但正確方向是 $MSR/MSE$；c $SSR$ 也不是均方比；d 正確，$MSE/MSR=1/F$。

#### 選擇題 34 <a id="exam-ch15-mc-34"></a>

##### 題目

> In a multiple regression analysis involving 12 independent variables and 166 observations, $SSR=878$ and $SSE=122$. The coefficient of determination is
>
> a. 0.1389<br>
> b. 0.1220<br>
> c. 0.878<br>
> d. 0.7317

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 計算。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=878+122=1,000$。
4. **代入計算／推理：** $R^2=878/1,000=0.878$，故 c。b 是 $SSE/SST$；a、d 不是正確比例。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 約為 $SSE/SSR$，比較錯誤；b 是未解釋比例 $SSE/SST$；c 正確，$R^2=878/(878+122)=0.878$；d 不是本題的判定係數。

#### 選擇題 35 <a id="exam-ch15-mc-35"></a>

##### 題目

> A regression analysis involved 8 independent variables and 99 observations. The critical value of $t$ for testing the significance of each of the independent variable's coefficients will have
>
> a. 98 degrees of freedom<br>
> b. 97 degrees of freedom<br>
> c. 90 degrees of freedom<br>
> d. 7 degrees of freedom

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別 $t$ 自由度。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=99,p=8$。
4. **代入計算／推理：** $df=99-8-1=90$，故 c。a、b 少扣參數；d 是 $p-1$。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 是總自由度 $n-1$；b 只扣 2，沒有扣除全部 8 個斜率；c 正確，$df=99-8-1=90$；d 是 $p-1$。

#### 選擇題 36 <a id="exam-ch15-mc-36"></a>

##### 題目

> In order to test for the significance of a regression model involving 14 independent variables and 255 observations, the numerator and denominator degrees of freedom (respectively) for the critical value of $F$ are
>
> a. 14 and 255<br>
> b. 255 and 14<br>
> c. 13 and 240<br>
> d. 14 and 240

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$ 自由度。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=14,n=255$。
4. **代入計算／推理：** $(df_1,df_2)=(14,255-14-1)=(14,240)$，故 d。a 未扣參數；b 顛倒；c 分子少 1。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 分子 14 正確但分母不能直接用 $n=255$；b 把兩自由度顛倒；c 把分子錯減 1；d 正確，$(df_1,df_2)=(14,240)$。

#### 選擇題 37 <a id="exam-ch15-mc-37"></a>

##### 題目

> A multiple regression model has the form $\hat Y=5+6X+7W$. As $X$ increases by 1 unit (holding $W$ constant), $Y$ is expected to
>
> a. increase by 11 units<br>
> b. decrease by 11 units<br>
> c. increase by 6 units<br>
> d. decrease by 6 units

##### 詳解

> **回看投影片講義：** [估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 部分斜率。
2. **選方法：** 回看[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 固定 $W$，只增加 $X$。
4. **代入計算／推理：** $X$ 係數為 $+6$，故 c。a 把截距與斜率相加；b、d 看錯方向。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 把截距 5 與斜率 6 相加，截距不是單位變化；b 又把該錯誤總和改成負向；c 正確，$X$ 的部分斜率是 $+6$；d 看錯正號。

#### 選擇題 38 <a id="exam-ch15-mc-38"></a>

##### 題目

> In a multiple regression analysis involving 10 independent variables and 81 observations, $SST=120$ and $SSE=42$. The coefficient of determination is
>
> a. 0.81<br>
> b. 0.11<br>
> c. 0.35<br>
> d. 0.65

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 計算。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SSR=120-42=78$。
4. **代入計算／推理：** $R^2=78/120=0.65$，故 d。c 是未解釋比例；a 混入樣本數；b 無正確來源。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 把觀測數 81 當成比例資訊；b 沒有正確平方和來源；c 是未解釋比例 $42/120=0.35$；d 正確，$R^2=1-42/120=0.65$。

#### 選擇題 39 <a id="exam-ch15-mc-39"></a>

##### 題目

> For a multiple regression model, $SST=200$ and $SSE=50$. The multiple coefficient of determination is
>
> a. 0.25<br>
> b. 4.00<br>
> c. 250<br>
> d. 0.75

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 計算。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SSR=150$。
4. **代入計算／推理：** $R^2=1-50/200=0.75$，故 d。a 是未解釋比例；b 是倒數；c 把平方和相加。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是未解釋比例 $SSE/SST$；b 是 $SST/SSE$ 的倒數式結果；c 把兩個平方和相加卻未轉成比例；d 正確，$R^2=1-50/200=0.75$。

#### 選擇題 40 <a id="exam-ch15-mc-40"></a>

##### 題目

> A regression model involved 18 independent variables and 200 observations. The critical value of $t$ for testing the significance of each of the independent variable's coefficients will have
>
> a. 18 degrees of freedom<br>
> b. 200 degrees of freedom<br>
> c. 199 degrees of freedom<br>
> d. 181 degrees of freedom

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別 $t$ 自由度。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=200,p=18$。
4. **代入計算／推理：** $df=200-18-1=181$，故 d。a 是變數數；b、c 未扣完整參數。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是 independent variables 數量；b 是樣本數；c 是總自由度 $n-1$；d 正確，個別 $t$ 使用 $df=200-18-1=181$。

#### 選擇題 41 <a id="exam-ch15-mc-41"></a>

##### 題目

> In order to test for the significance of a regression model involving 8 independent variables and 121 observations, the numerator and denominator degrees of freedom (respectively) for the critical value of $F$ are
>
> a. 8 and 121<br>
> b. 7 and 120<br>
> c. 8 and 112<br>
> d. 7 and 112

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$ 自由度。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=8,n=121$。
4. **代入計算／推理：** $(df_1,df_2)=(8,121-8-1)=(8,112)$，故 c。a 未扣參數；b、d 分子錯。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 分子正確但分母不能用 $n$；b 把分子錯減 1 且分母用總自由度；c 正確，$(df_1,df_2)=(8,112)$；d 的分子 7 錯在把 $p$ 減 1。

#### 選擇題 42 <a id="exam-ch15-mc-42"></a>

##### 題目

> In a multiple regression analysis involving 5 independent variables and 30 observations, $SSR=360$ and $SSE=40$. The coefficient of determination is
>
> a. 0.80<br>
> b. 0.90<br>
> c. 0.25<br>
> d. 0.15

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$ 計算。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=400$。
4. **代入計算／推理：** $R^2=360/400=0.90$，故 b。a、c、d 都不是解釋平方和占總平方和。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 的 0.80 不是解釋平方和占總平方和的比例；b 正確，$R^2=360/(360+40)=0.90$；c 的 0.25 沒有由題給平方和得到的正確意義；d 的 0.15 也不是正確的平方和比例。

#### 選擇題 43 <a id="exam-ch15-mc-43"></a>

##### 題目

> A regression analysis involved 6 independent variables and 27 observations. The critical value of $t$ for testing the significance of each of the independent variable's coefficients will have
>
> a. 27 degrees of freedom<br>
> b. 26 degrees of freedom<br>
> c. 21 degrees of freedom<br>
> d. 20 degrees of freedom

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別 $t$ 自由度。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=27,p=6$。
4. **代入計算／推理：** $df=27-6-1=20$，故 d。c 忘了截距；a、b 未扣斜率。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是樣本數而非自由度；b 是總自由度 $n-1$；c 是 $n-p$，忘記再扣截距；d 正確，$df=27-6-1=20$。

#### 選擇題 44 <a id="exam-ch15-mc-44"></a>

##### 題目

> In order to test for the significance of a regression model involving 4 independent variables and 36 observations, the numerator and denominator degrees of freedom (respectively) for the critical value of $F$ are
>
> a. 4 and 36<br>
> b. 3 and 35<br>
> c. 4 and 31<br>
> d. 4 and 32

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$ 自由度。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=4,n=36$。
4. **代入計算／推理：** $(df_1,df_2)=(4,36-4-1)=(4,31)$，故 c。a 未扣參數；b 分子少 1；d 忘記截距。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 分子 4 正確但分母不能直接用樣本數 36；b 把分子減 1 且使用總自由度；c 正確，$(df_1,df_2)=(4,31)$；d 是 $n-p$，漏扣截距。

### 選擇題｜第 45–64 題：題組 15-1 至 15-5

#### 題組 15-1：選擇題 45–47 共用資料

> In a regression model involving 44 observations, the following estimated regression equation was obtained:
>
> $$\hat Y=29+18X_1+43X_2+87X_3$$
>
> For this model $SSR=600$ and $SSE=400$.

#### 選擇題 45 <a id="exam-ch15-mc-45"></a>

##### 題目

> Refer to Exhibit 15-1. The coefficient of determination for the above model is
>
> a. 0.667<br>
> b. 0.600<br>
> c. 0.336<br>
> d. 0.400

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=600+400=1,000$。
4. **代入計算／推理：** $R^2=600/1,000=0.600$，故 b。a 是 $SSR/SSE$；d 是未解釋比例；c 無正確來源。
5. **解讀結論：** 正確答案是 **b** ；模型解釋 60% 的樣本變異。

**選項逐一：** a 是 $SSR/SSE=1.5$ 的倒數方向誤用；b 正確，$R^2=600/(600+400)=0.600$；c 沒有正確平方和來源；d 是未解釋比例 $SSE/SST$。

#### 選擇題 46 <a id="exam-ch15-mc-46"></a>

##### 題目

> Refer to Exhibit 15-1. $MSR$ for this model is
>
> a. 200<br>
> b. 10<br>
> c. 1,000<br>
> d. 43

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 迴歸均方。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)中的 $MSR=SSR/p$。
3. **檢查假設：** 方程式有 $p=3$ 個解釋變數。
4. **代入計算／推理：** $MSR=600/3=200$，故 a。b 是後面會得到的 $MSE$；c 是 $SST$；d 是總自由度。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，三個解釋變數使 $MSR=600/3=200$；b 是後續的 $MSE=400/40=10$；c 是 $SST$；d 是總自由度 $n-1=43$。

#### 選擇題 47 <a id="exam-ch15-mc-47"></a>

##### 題目

> Refer to Exhibit 15-1. The computed $F$ statistic for testing the significance of the above model is
>
> a. 1.500<br>
> b. 20.00<br>
> c. 0.600<br>
> d. 0.6667

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=3,n=44$，誤差 $df=40$。
4. **代入計算／推理：** $MSR=600/3=200$，$MSE=400/40=10$，故 $F=20$，選 b。a 是平方和比；c 是 $R^2$；d 是其餘錯誤比值。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 是未除自由度的 $SSR/SSE=1.5$；b 正確，$F=(600/3)/(400/40)=20$；c 是 $R^2$；d 是另一個未使用正確均方的比例。

<a id="quiz-ch15-exhibit-15-2"></a>

#### 題組 15-2：選擇題 48–52 共用資料

> A regression model between sales ($Y$ in \$1,000), unit price ($X_1$ in dollars), and television advertisement ($X_2$ in dollars) resulted in
>
> $$\hat Y=7-3X_1+5X_2.$$
>
> For this model $SSR=3,500$, $SSE=1,500$, and $n=18$.

#### 選擇題 48 <a id="exam-ch15-mc-48"></a>

##### 題目

> Refer to Exhibit 15-2. The coefficient of the unit price indicates that if the unit price is
>
> a. increased by \$1 (holding advertising constant), sales are expected to increase by \$3<br>
> b. decreased by \$1 (holding advertising constant), sales are expected to decrease by \$3<br>
> c. increased by \$1 (holding advertising constant), sales are expected to increase by \$4,000<br>
> d. increased by \$1 (holding advertising constant), sales are expected to decrease by \$3,000

##### 詳解

> **回看投影片講義：** [估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 部分斜率與單位。
2. **選方法：** 回看[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 固定廣告；$Y$ 以千美元計，$X_1$ 以美元計。
4. **代入計算／推理：** $b_1=-3$，價格增加 \$1，預測銷售減少 $3\times1,000=3,000$ 美元(即 \$3,000)，故 d。a 看錯正負；b 同時把 $X$ 方向與 $Y$ 方向處理錯；c 數字和方向都錯。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 看錯負斜率且忘了 $Y$ 以千美元計；b 容易因價格『減少』而選，但負斜率表示價格減少時銷售反而增加；c 同時看錯方向與係數；d 正確，價格增加 1 美元時預測銷售減少 3 千美元。

#### 選擇題 49 <a id="exam-ch15-mc-49"></a>

##### 題目

> Refer to Exhibit 15-2. The coefficient of $X_2$ indicates that if television advertising is increased by \$1 (holding the unit price constant), sales are expected to
>
> a. increase by \$5<br>
> b. increase by \$12,000<br>
> c. increase by \$5,000<br>
> d. decrease by \$2,000

##### 詳解

> **回看投影片講義：** [估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 部分斜率與單位。
2. **選方法：** 回看[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 固定價格；$Y$ 單位是千美元。
4. **代入計算／推理：** $b_2=5$，所以廣告增加 \$1，銷售增加 \$5,000，故 c。a 忘記 $Y$ 單位；b 把截距與係數相加；d 看錯方向與數字。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 把係數 5 直接當 5 美元，忘記 $Y$ 以千美元計；b 容易把截距 7 與斜率 5 相加；c 正確，廣告增加 1 美元時預測銷售增加 5 千美元；d 看錯正號與數值。

#### 選擇題 50 <a id="exam-ch15-mc-50"></a>

##### 題目

> Refer to Exhibit 15-2. To test for the significance of the model, the test statistic $F$ is
>
> a. 2.33<br>
> b. 0.70<br>
> c. 17.5<br>
> d. 1.75

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=2,n=18$，誤差 $df=15$。
4. **代入計算／推理：** $MSR=3,500/2=1,750$；$MSE=1,500/15=100$；$F=17.5$，故 c。a 是平方和比；b 是 $R^2$；d 少一個十倍。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 是 $SSR/SSE=2.33$，沒有先除自由度；b 是 $R^2=0.70$；c 正確，$F=(3500/2)/(1500/15)=17.5$；d 是把 1,750 錯置小數點，且不是完整均方比。

#### 選擇題 51 <a id="exam-ch15-mc-51"></a>

##### 題目

> Refer to Exhibit 15-2. To test for the significance of the model, the p-value is
>
> a. less than 0.01<br>
> b. between 0.01 and 0.025<br>
> c. between 0.025 and 0.05<br>
> d. between 0.05 and 0.10

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 由 $F$ 判 p-value 區間。
2. **選方法：** 使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $F=17.5$，自由度 $(2,15)$，右尾。
4. **代入計算／推理：** 獨立重算得 p-value 約 $0.00012<0.01$，故 a。b、c、d 都把右尾面積估得過大。
5. **解讀結論：** 正確答案是 **a** ；模型整體顯著，但不代表每個斜率都顯著。

**選項逐一：** a 正確，$F=17.5$、自由度 $(2,15)$ 的右尾 p-value 約 0.00012；b 的 0.01 到 0.025 區間過大；c 的 0.025 到 0.05 區間更大；d 的 0.05 到 0.10 最不符合此 $F$ 的極端程度。

#### 選擇題 52 <a id="exam-ch15-mc-52"></a>

##### 題目

> Refer to Exhibit 15-2. The multiple coefficient of correlation for this problem is
>
> a. 0.70<br>
> b. 0.8367<br>
> c. 0.49<br>
> d. 0.2289

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 由 $R^2$ 求 multiple $R$。
2. **選方法：** 先用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)，再取非負平方根。
3. **檢查假設：** $R^2=3,500/(3,500+1,500)=0.70$。
4. **代入計算／推理：** $R=\sqrt{0.70}=0.83666\approx0.8367$，故 b。a 是 $R^2$；c 是 $R^4$；d 無正確來源。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 是 $R^2=0.70$，容易忘記開根號；b 正確，multiple $R=\sqrt{0.70}=0.8367$；c 是把 0.70 再平方；d 不是由題給平方和導出的值。

<a id="quiz-ch15-exhibit-15-3"></a>

#### 題組 15-3：選擇題 53–56 共用資料

> In a regression model involving 30 observations, the following estimated regression equation was obtained:
>
> $$\hat Y=17+4X_1-3X_2+8X_3+8X_4.$$
>
> For this model $SSR=700$ and $SSE=100$.

#### 選擇題 53 <a id="exam-ch15-mc-53"></a>

##### 題目

> Refer to Exhibit 15-3. The coefficient of determination for the above model is approximately
>
> a. $-0.875$<br>
> b. 0.875<br>
> c. 0.125<br>
> d. 0.144

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=800$。
4. **代入計算／推理：** $R^2=700/800=0.875$，故 b。a 不可能為負；c 是未解釋比例；d 約為 $SSE/SSR$。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 錯在 $R^2$ 不會是負數；b 正確，$R^2=700/800=0.875$；c 是未解釋比例 $SSE/SST$；d 約為 $SSE/SSR$。

#### 選擇題 54 <a id="exam-ch15-mc-54"></a>

##### 題目

> Refer to Exhibit 15-3. The computed $F$ statistic for testing the significance of the above model is
>
> a. 43.75<br>
> b. 0.875<br>
> c. 50.19<br>
> d. 7.00

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=4,n=30$，誤差 $df=25$。
4. **代入計算／推理：** $MSR=700/4=175$；$MSE=100/25=4$；$F=43.75$，故 a。b 是 $R^2$；d 是平方和比；c 不是正確均方比。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，$F=(700/4)/(100/25)=43.75$；b 是 $R^2$；c 來自錯誤自由度或錯誤均方；d 是未除自由度的 $SSR/SSE$。

#### 選擇題 55 <a id="exam-ch15-mc-55"></a>

##### 題目

> Refer to Exhibit 15-3. The critical $F$ value at 95% confidence is
>
> a. 2.53<br>
> b. 2.69<br>
> c. 2.76<br>
> d. 2.99

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $F$ 臨界值。
2. **選方法：** 依[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)查右尾 $\alpha=0.05$。
3. **檢查假設：** 自由度 $(4,25)$。
4. **代入計算／推理：** 軟體重算 $F_{0.05;4,25}=2.7587\approx2.76$，故 c。其餘選項是錯誤自由度或近似誘答。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 的 2.53 是使用錯誤自由度所得；b 的 2.69 仍不是 $(4,25)$ 對應值；c 正確，$F_{0.05;4,25}=2.7587\approx2.76$；d 的 2.99 也來自錯誤自由度或查表位置。

#### 選擇題 56 <a id="exam-ch15-mc-56"></a>

##### 題目

> Refer to Exhibit 15-3. The conclusion is that the
>
> a. model is not significant<br>
> b. model is significant<br>
> c. slope of $X_1$ is significant<br>
> d. slope of $X_2$ is significant

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 整體檢定結論。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $F=43.75>2.76$；題目沒有個別係數標準誤。
4. **代入計算／推理：** 拒絕所有斜率皆 0 的 $H_0$，故 b。a 與比較相反；c、d 不能由整體 $F$ 指定哪個斜率顯著。
5. **解讀結論：** 正確答案是 **b** ；至少一個斜率提供資訊。

**選項逐一：** a 錯，因為 $F=43.75$ 遠大於臨界值；b 正確，整體模型顯著；c 錯在整體 $F$ 不能單獨判定 $X_1$ 的斜率顯著；d 同理，整體 $F$ 不能單獨判定 $X_2$ 的斜率顯著。

<a id="quiz-ch15-exhibit-15-4"></a>

#### 題組 15-4：選擇題 57–59 共用資料

> Equation A: $Y=\beta_0+\beta_1X_1+\beta_2X_2+\epsilon$<br>
> Equation B: $E(Y)=\beta_0+\beta_1X_1+\beta_2X_2+\epsilon$<br>
> Equation C: $\hat Y=b_0+b_1X_1+b_2X_2$<br>
> Equation D: $E(Y)=\beta_0+\beta_1X_1+\beta_2X_2$

#### 選擇題 57 <a id="exam-ch15-mc-57"></a>

##### 題目

> Which equation describes the multiple regression model?
>
> a. Equation A<br>
> b. Equation B<br>
> c. Equation C<br>
> d. Equation D

##### 詳解

> **回看投影片講義：** [複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)


1. **辨認題型：** 含誤差項的母體模型。
2. **選方法：** 回看[複迴歸模型](./course2-slides-handout.html#formula-multiple-regression-model)。
3. **檢查假設：** 模型左側是個別 $Y$，右側含 $\epsilon$。
4. **代入計算／推理：** Equation A 符合，故 a。B 不應在 $E(Y)$ 後保留隨機誤差；C 是樣本估計；D 是母體平均方程式。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，個別 $Y$ 的母體模型必須包含 $\epsilon$；b 錯在 $E(Y)$ 右側不應再放平均為 0 的隨機誤差；c 是樣本估計式；d 是母體平均方程式。

#### 選擇題 58 <a id="exam-ch15-mc-58"></a>

##### 題目

> Which equation gives the estimated regression line?
>
> a. Equation A<br>
> b. Equation B<br>
> c. Equation C<br>
> d. Equation D

##### 詳解

> **回看投影片講義：** [估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 樣本估計式。
2. **選方法：** 回看[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 要找 $\hat Y$ 與樣本係數 $b$。
4. **代入計算／推理：** Equation C 符合，故 c。A、B、D 使用母體 $\beta$；A、B 還含誤差。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 是含誤差的母體模型；b 是把期望值與誤差混寫的錯誤式；c 正確，$\hat Y$ 與 $b_j$ 給出 estimated regression line；d 使用母體參數，並非樣本估計。

#### 選擇題 59 <a id="exam-ch15-mc-59"></a>

##### 題目

> Which equation describes the multiple regression equation?
>
> a. Equation A<br>
> b. Equation B<br>
> c. Equation C<br>
> d. Equation D

##### 詳解

> **回看投影片講義：** [複迴歸平均方程式](./course2-slides-handout.html#formula-multiple-regression-mean)


1. **辨認題型：** 母體平均方程式。
2. **選方法：** 回看[複迴歸平均方程式](./course2-slides-handout.html#formula-multiple-regression-mean)。
3. **檢查假設：** $E(Y)$ 不含個別隨機誤差。
4. **代入計算／推理：** Equation D 符合，故 d。A 是模型；B 多放 $\epsilon$；C 是估計式。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是含 $\epsilon$ 的完整模型；b 錯把 $\epsilon$ 留在 $E(Y)$ 中；c 是 estimated equation；d 正確，這是用 $\beta_j$ 表示且不含誤差的 multiple regression equation。

<a id="quiz-ch15-exhibit-15-5"></a>

#### 題組 15-5：選擇題 60–64 共用資料

> Partial Minitab output based on $n=25$ observations:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 145.321 | 48.682 |
> | $X_1$ | 25.625 | 9.150 |
> | $X_2$ | $-5.720$ | 3.575 |
> | $X_3$ | 0.823 | 0.183 |

#### 選擇題 60 <a id="exam-ch15-mc-60"></a>

##### 題目

> Refer to Exhibit 15-5. The estimated regression equation is
>
> a. $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\epsilon$<br>
> b. $E(Y)=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3$<br>
> c. $\hat Y=145.321+25.625X_1-5.720X_2+0.823X_3$<br>
> d. $\hat Y=48.682+9.15X_1+3.575X_2+1.183X_3$

##### 詳解

> **回看投影片講義：** [估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 從係數表寫估計式。
2. **選方法：** 使用[估計複迴歸方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 用 Coefficient 欄，不用 Standard Error 欄。
4. **代入計算／推理：** 由係數表重建為 $\hat Y=145.321+25.625X_1-5.720X_2+0.823X_3$。a、b 是母體式；d 把標準誤當係數；c 與係數表完全一致。
5. **解讀結論：** 正確答案是 **c**。

**選項逐一：** a 是含誤差的母體模型，並非由輸出得到的估計式；b 是母體平均方程式；c 正確，完整使用 Coefficient 欄；d 錯把 Standard Error 欄當成係數。

#### 選擇題 61 <a id="exam-ch15-mc-61"></a>

##### 題目

> Refer to Exhibit 15-5. The interpretation of the coefficient on $X_1$ is that
>
> a. a one unit change in $X_1$ will lead to a 25.625 unit change in $Y$<br>
> b. a one unit change in $X_1$ will lead to a 25.625 unit increase in $Y$ when all other variables are held constant<br>
> c. a one unit change in $X_1$ will lead to a 25.625 unit increase in $X_2$ when all other variables are held constant<br>
> d. It is impossible to interpret the coefficient.

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)


1. **辨認題型：** 部分斜率解讀。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)。
3. **檢查假設：** 需說明其他變數固定，且反應是 $Y$。
4. **代入計算／推理：** b 完整。a 漏掉控制條件與方向；c 把反應誤寫成 $X_2$；d 忽略可做條件式解讀。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 只說 change，既漏掉正向 increase，也漏掉固定其他變數；b 正確，這是 $X_1$ 的部分斜率解讀；c 把應變數誤寫成 $X_2$；d 錯，係數可以在其他變數固定下解讀。

#### 選擇題 62 <a id="exam-ch15-mc-62"></a>

##### 題目

> Refer to Exhibit 15-5. We want to test whether the parameter $\beta_1$ is significant. The test statistic equals
>
> a. 0.357<br>
> b. 2.8<br>
> c. 14<br>
> d. 1.96

##### 詳解

> **回看投影片講義：** [個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別斜率 $t$。
2. **選方法：** 使用[個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $H_0:\beta_1=0$，係數 25.625、標準誤 9.150。
4. **代入計算／推理：** $t=25.625/9.150=2.8005\approx2.8$，故 b。a 是倒數附近；c、d 不是代入結果。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 接近標準誤與係數比值的倒數，方向錯；b 正確，$t=25.625/9.150\approx2.8$；c 不是係數除標準誤；d 是常態近似的常見臨界值，不是本題統計量。

#### 選擇題 63 <a id="exam-ch15-mc-63"></a>

##### 題目

> Refer to Exhibit 15-5. The $t$ value obtained from the table to test an individual parameter at the 5% level is
>
> a. 2.06<br>
> b. 2.069<br>
> c. 2.074<br>
> d. 2.080

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 雙尾 $t$ 臨界值。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=25,p=3$，$df=21$；$\alpha=0.05$ 雙尾查 $t_{0.025,21}$。
4. **代入計算／推理：** 軟體值 $2.0796\approx2.080$，故 d。a–c 對應其他自由度或較粗誤差。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 的 2.06 是其他自由度或過度粗略的臨界值；b 的 2.069 仍低於正確臨界值；c 的 2.074 也不是自由度 21 的查表值；d 正確，$n=25,p=3$ 給 $df=21$，所以 $t_{0.025,21}\approx2.080$。

#### 選擇題 64 <a id="exam-ch15-mc-64"></a>

##### 題目

> Refer to Exhibit 15-5. Carry out the test of significance for the parameter $\beta_1$ at the 5% level. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 個別 $t$ 決策。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $|t|=2.8005>2.0796$，模型推論假設需合理。
4. **代入計算／推理：** 拒絕 $H_0:\beta_1=0$，故 a。b 與比較相反；c 不是檢定決策；d 因 a 正確而錯。
5. **解讀結論：** 正確答案是 **a** ；控制其他變數後，$X_1$ 有顯著線性關係。

**選項逐一：** a 正確，$|t|=2.8005>2.0796$，故拒絕 $H_0$；b 的比較方向相反；c 「修訂虛無假設」不是檢定決策；d 錯，因為 a 已正確。

### 選擇題｜第 65–85 題：題組 15-6 至 15-8

#### 題組 15-6：選擇題 65–74 共用資料

> Partial computer output based on $n=16$ observations:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 12.924 | 4.425 |
> | $X_1$ | $-3.682$ | 2.630 |
> | $X_2$ | 45.216 | 12.560 |
>
> | Source | Sum of Squares | Mean Square |
> |---|---:|---:|
> | Regression | 4,853 | 2,426.5 |
> | Error |  | 485.3 |

#### 選擇題 65 <a id="exam-ch15-mc-65"></a>

##### 題目

> Refer to Exhibit 15-6. The estimated regression equation is
>
> a. $Y=\beta_0+\beta_1X_1+\beta_2X_2+\epsilon$<br>
> b. $E(Y)=\beta_0+\beta_1X_1+\beta_2X_2$<br>
> c. $\hat Y=12.924-3.682X_1+45.216X_2$<br>
> d. $\hat Y=4.425+2.63X_1+12.56X_2$

##### 詳解

> **回看投影片講義：** [估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 從係數表寫估計式。
2. **選方法：** 使用[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
3. **檢查假設：** 係數與標準誤不可混用。
4. **代入計算／推理：** c 正確。a、b 是母體式；d 把標準誤當係數並漏掉負號。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 是含誤差的母體模型；b 是用母體參數表示的平均方程式；c 正確，直接使用 Coefficient 欄；d 錯把 Standard Error 欄當成係數。

#### 選擇題 66 <a id="exam-ch15-mc-66"></a>

##### 題目

> Refer to Exhibit 15-6. The interpretation of the coefficient of $X_1$ is that
>
> a. a one unit change in $X_1$ will lead to a 3.682 unit decrease in $Y$<br>
> b. a one unit increase in $X_1$ will lead to a 3.682 unit decrease in $Y$ when all other variables are held constant<br>
> c. a one unit increase in $X_1$ will lead to a 3.682 unit decrease in $X_2$ when all other variables are held constant<br>
> d. It is impossible to interpret the coefficient.

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)


1. **辨認題型：** 部分斜率。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)。
3. **檢查假設：** 固定其他變數，解讀 $Y$ 的預測平均差。
4. **代入計算／推理：** b 完整。a 漏控制條件；c 把反應寫成 $X_2$；d 錯在係數可條件式解讀。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 雖抓到減少 3.682，但漏掉固定其他變數；b 正確，是完整的部分斜率解讀；c 把反應錯寫成 $X_2$；d 錯，控制其他變數後可以解讀。

#### 選擇題 67 <a id="exam-ch15-mc-67"></a>

##### 題目

> Refer to Exhibit 15-6. We want to test whether the parameter $\beta_1$ is significant. The test statistic equals
>
> a. $-1.4$<br>
> b. 1.4<br>
> c. 3.6<br>
> d. 5

##### 詳解

> **回看投影片講義：** [個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 個別斜率 $t$。
2. **選方法：** 使用[個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** 係數 $-3.682$、標準誤 2.630。
4. **代入計算／推理：** $t=-3.682/2.630=-1.400$，故 a。b 忘記負號；c、d 不是係數除標準誤。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，$t=-3.682/2.630\approx-1.4$；b 只取絕對值而遺失係數方向；c 是 $X_2$ 的 $t$ 值約 3.6，答錯參數；d 是整體 $F$ 約 5，不是個別 $t$。

#### 選擇題 68 <a id="exam-ch15-mc-68"></a>

##### 題目

> Refer to Exhibit 15-6. The $t$ value obtained from the table which is used to test an individual parameter at the 1% level is
>
> a. 2.65<br>
> b. 2.921<br>
> c. 2.977<br>
> d. 3.012

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 1% 雙尾 $t$ 臨界值。
2. **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $p=2,n=16$，$df=13$；查 $t_{0.005,13}$。
4. **代入計算／推理：** 軟體值 $3.0123\approx3.012$，故 d。a–c 來自錯誤尾數或自由度。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 的 2.65 容易與其他顯著水準混淆；b 的 2.921 是其他自由度的 1% 臨界值；c 的 2.977 也不是自由度 13 的臨界值；d 正確，$df=16-2-1=13$ 時 $t_{0.005,13}\approx3.012$。

#### 選擇題 69 <a id="exam-ch15-mc-69"></a>

##### 題目

> Refer to Exhibit 15-6. Carry out the test of significance for the parameter $\beta_1$ at the 1% level. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 個別 $t$ 決策。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $|t|=1.400<3.012$。
4. **代入計算／推理：** 未拒絕 $H_0:\beta_1=0$，故 b。a 比較方向錯；c 不是標準決策；d 因 b 正確而錯。
5. **解讀結論：** 正確答案是 **b** ；不能說已證明 $\beta_1=0$。

**選項逐一：** a 錯，$|t|=1.4$ 沒有超過 3.012；b 正確，應未拒絕 $H_0$；c 不是標準檢定決策；d 錯，因為 b 已正確。

#### 選擇題 70 <a id="exam-ch15-mc-70"></a>

##### 題目

> Refer to Exhibit 15-6. The degrees of freedom for the sum of squares explained by the regression ($SSR$) are
>
> a. 2<br>
> b. 3<br>
> c. 13<br>
> d. 15

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 迴歸自由度。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 有 $p=2$ 個解釋變數。
4. **代入計算／推理：** regression $df=p=2$，故 a。b 把截距算入；c 是誤差自由度；d 是總自由度。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，regression 自由度等於解釋變數數 $p=2$；b 把截距也算進 regression df；c 是 error df；d 是 total df。

#### 選擇題 71 <a id="exam-ch15-mc-71"></a>

##### 題目

> Refer to Exhibit 15-6. The sum of squares due to error ($SSE$) equals
>
> a. 37.33<br>
> b. 485.3<br>
> c. 4,853<br>
> d. 6,308.9

##### 詳解

> **回看投影片講義：** [$MSE=SSE/(n-p-1)$](./course2-slides-handout.html#formula-mse-error-variance)


1. **辨認題型：** 由 $MSE$ 還原 $SSE$。
2. **選方法：** 使用[$MSE=SSE/(n-p-1)$](./course2-slides-handout.html#formula-mse-error-variance)。
3. **檢查假設：** 誤差 $df=16-2-1=13$。
4. **代入計算／推理：** $SSE=485.3(13)=6,308.9$，故 d。b 是均方；c 是 $SSR$；a 是錯誤除法。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是把 $MSE$ 再除以 13 的錯誤結果附近；b 只是 $MSE$，不是 $SSE$；c 是 $SSR$；d 正確，$SSE=485.3(13)=6308.9$。

#### 選擇題 72 <a id="exam-ch15-mc-72"></a>

##### 題目

> Refer to Exhibit 15-6. The test statistic used to determine if there is a relationship among the variables equals
>
> a. $-1.4$<br>
> b. 0.2<br>
> c. 0.77<br>
> d. 5

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 問整組變數，使用 $MSR/MSE$。
4. **代入計算／推理：** $F=2,426.5/485.3=5.000$，故 d。a 是個別 $t$；b 是倒數；c 無正確來源。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 是 $X_1$ 的個別 $t$；b 是 $MSE/MSR$ 的倒數方向；c 不是正確均方比；d 正確，整體 $F=2426.5/485.3\approx5$。

#### 選擇題 73 <a id="exam-ch15-mc-73"></a>

##### 題目

> Refer to Exhibit 15-6. The $F$ value obtained from the table used to test if there is a relationship among the variables at the 5% level equals
>
> a. 3.41<br>
> b. 3.63<br>
> c. 3.81<br>
> d. 19.41

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $F$ 臨界值。
2. **選方法：** 使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 自由度 $(2,13)$，右尾 $\alpha=0.05$。
4. **代入計算／推理：** 軟體值 $F_{0.05;2,13}=3.8056\approx3.81$，故 c。其餘來自錯誤自由度或尾端。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 的 3.41 是使用其他分母自由度得到的臨界值；b 的 3.63 也不是 $(2,13)$ 的正確查表值；c 正確，$F_{0.05;2,13}\approx3.81$；d 的 19.41 遠大於正確值，可能混入其他統計量。

#### 選擇題 74 <a id="exam-ch15-mc-74"></a>

##### 題目

> Refer to Exhibit 15-6. Carry out the test to determine if there is a relationship among the variables at the 5% level. The null hypothesis should
>
> a. be rejected<br>
> b. not be rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 整體 $F$ 決策。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $F=5.00>3.81$。
4. **代入計算／推理：** 拒絕 $H_0:\beta_1=\beta_2=0$，故 a。b 比較方向錯；c 不是決策；d 因 a 正確而錯。
5. **解讀結論：** 正確答案是 **a** ；至少一個斜率有線性資訊。

**選項逐一：** a 正確，$F=5.00>3.81$，所以拒絕整體 $H_0$；b 的比較方向相反；c 不是檢定決策；d 錯，因為 a 已正確。

<a id="quiz-ch15-exhibit-15-7"></a>

#### 題組 15-7：選擇題 75–77 共用資料

> A regression model involving 4 independent variables and a sample of 15 periods resulted in $SSR=165$ and $SSE=60$.

#### 選擇題 75 <a id="exam-ch15-mc-75"></a>

##### 題目

> Refer to Exhibit 15-7. The coefficient of determination is
>
> a. 0.3636<br>
> b. 0.7333<br>
> c. 0.275<br>
> d. 0.5

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $SST=225$。
4. **代入計算／推理：** $R^2=165/225=0.7333$，故 b。a 是 $SSE/SSR$；c、d 不是正確比例。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 是 $SSE/SSR=60/165$，分母錯；b 正確，$R^2=165/(165+60)=0.7333$；c 的 0.275 不是正確的解釋平方和比例；d 的 0.5 也沒有由題給平方和得到。

#### 選擇題 76 <a id="exam-ch15-mc-76"></a>

##### 題目

> Refer to Exhibit 15-7. If we want to test for the significance of the model at 95% confidence, the critical $F$ value (from the table) is
>
> a. 3.06<br>
> b. 3.48<br>
> c. 3.34<br>
> d. 3.11

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $F$ 臨界值。
2. **選方法：** 使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=4,n=15$，自由度 $(4,10)$。
4. **代入計算／推理：** $F_{0.05;4,10}=3.478\approx3.48$，故 b。其餘是錯誤自由度的查表值。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 的 3.06 是使用其他自由度得到的查表誘答；b 正確，$p=4,n=15$ 給 $F_{0.05;4,10}\approx3.48$；c 的 3.34 不是 $(4,10)$ 的臨界值；d 的 3.11 也來自錯誤自由度。

#### 選擇題 77 <a id="exam-ch15-mc-77"></a>

##### 題目

> Refer to Exhibit 15-7. The test statistic from the information provided is
>
> a. 2.110<br>
> b. 3.480<br>
> c. 4.710<br>
> d. 6.875

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $MSR=165/4=41.25$；$MSE=60/10=6$。
4. **代入計算／推理：** $F=41.25/6=6.875$，故 d。b 是臨界值；a、c 不是均方比。
5. **解讀結論：** 正確答案是 **d** ；且 $6.875>3.48$，模型顯著。

**選項逐一：** a 的 2.110 不是 $MSR/MSE$ 的正確結果；b 的 3.480 是前一題臨界值，容易誤當成檢定統計量；c 的 4.710 也不是正確均方比；d 正確，$F=(165/4)/(60/10)=6.875$。

<a id="quiz-ch15-exhibit-15-8"></a>

#### 題組 15-8：選擇題 78–85 共用資料

> The following estimated regression model relates yearly income ($Y$ in \$1,000s) of 30 individuals to age ($X_1$) and gender ($X_2$; 0 if male and 1 if female):
>
> $$\hat Y=30+0.7X_1+3X_2.$$
>
> Also, $SST=1,200$ and $SSE=384$.

#### 選擇題 78 <a id="exam-ch15-mc-78"></a>

##### 題目

> Refer to Exhibit 15-8. From the above function, it can be said that the expected yearly income of
>
> a. males is \$3 more than females<br>
> b. females is \$3 more than males<br>
> c. males is \$3,000 more than females<br>
> d. females is \$3,000 more than males

##### 詳解

> **回看投影片講義：** [連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)


1. **辨認題型：** 虛擬變數係數與單位。
2. **選方法：** 依[連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)。
3. **檢查假設：** 固定年齡；男性為參考組 $X_2=0$，女性 $X_2=1$；$Y$ 以千美元計。
4. **代入計算／推理：** 女性減男性為 $3$ 千美元，故 d。a、b 忘記千美元單位；c 看反參考組方向。
5. **解讀結論：** 正確答案是 **d** ；這是條件平均差，不是因果證明。

**選項逐一：** a 忘記 $Y$ 以千美元計，而且看反組別方向；b 的方向正確但忘記千美元單位；c 的金額單位正確但看反參考組；d 正確，女性相對男性高 3 千美元。

#### 選擇題 79 <a id="exam-ch15-mc-79"></a>

##### 題目

> Refer to Exhibit 15-8. The yearly income of a 24-year-old female individual is
>
> a. \$19.80<br>
> b. \$19,800<br>
> c. \$49.80<br>
> d. \$49,800

##### 詳解

> **回看投影片講義：** [複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 含虛擬變數的點預測。
2. **選方法：** 使用[複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** 女性 $X_2=1$、年齡 $X_1=24$，輸出單位為千美元。
4. **代入計算／推理：** $30+0.7(24)+3=49.8$ 千美元，即 \$49,800，故 d。a、b 漏截距與／或單位；c 未換成美元。
5. **解讀結論：** 正確答案是 **d** 。

**選項逐一：** a 只保留部分計算且單位也錯；b 的 19,800 是漏掉截距後的金額；c 的 49.80 是模型輸出的千美元數值，卻未換成題目要的美元；d 正確，$49.8$ 千美元即 49,800 美元。

#### 選擇題 80 <a id="exam-ch15-mc-80"></a>

##### 題目

> Refer to Exhibit 15-8. The yearly income of a 24-year-old male individual is
>
> a. \$13.80<br>
> b. \$13,800<br>
> c. \$46,800<br>
> d. \$49,800

##### 詳解

> **回看投影片講義：** [複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 點預測。
2. **選方法：** 使用[複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** 男性 $X_2=0$。
4. **代入計算／推理：** $30+0.7(24)+3(0)=46.8$ 千美元，即 \$46,800，故 c。a、b 漏截距；d 錯把男性設成 1。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 的 13.80 漏掉截距且單位錯誤；b 的 13,800 雖換算單位，仍漏掉截距；c 正確，男性代 $X_2=0$ 得 46.8 千美元，即 46,800 美元；d 的 49,800 是把男性錯代成女性 $X_2=1$ 的結果。

#### 選擇題 81 <a id="exam-ch15-mc-81"></a>

##### 題目

> Refer to Exhibit 15-8. The multiple coefficient of determination is
>
> a. 0.32<br>
> b. 0.42<br>
> c. 0.68<br>
> d. 0.50

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** $R^2$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $R^2=1-SSE/SST$。
4. **代入計算／推理：** $1-384/1,200=0.68$，故 c。a 是未解釋比例；b、d 不是此比值。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 是未解釋比例 $SSE/SST=0.32$；b 沒有正確平方和來源；c 正確，$R^2=1-384/1200=0.68$；d 不是題給平方和的比值。

#### 選擇題 82 <a id="exam-ch15-mc-82"></a>

##### 題目

> Refer to Exhibit 15-8. If we want to test for the significance of the model, the critical value of $F$ at 95% confidence is
>
> a. 3.33<br>
> b. 3.35<br>
> c. 3.34<br>
> d. 2.96

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $F$ 臨界值。
2. **選方法：** 使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=2,n=30$，自由度 $(2,27)$。
4. **代入計算／推理：** 軟體值 $3.354$，傳統表格四捨五入約 3.35，故 b。a、c 是較粗或錯誤自由度近似；d 不符 $(2,27)$。
5. **解讀結論：** 正確答案是 **b** 。

**選項逐一：** a 的 3.33 是相鄰四捨五入誘答，但不符合精確查表值；b 正確，$F_{0.05;2,27}=3.354\approx3.35$；c 的 3.34 同樣不是正確四捨五入結果；d 的 2.96 是其他自由度下的臨界值。

#### 選擇題 83 <a id="exam-ch15-mc-83"></a>

##### 題目

> Refer to Exhibit 15-8. The test statistic for testing the significance of the model is
>
> a. 0.73<br>
> b. 1.47<br>
> c. 28.69<br>
> d. 5.22

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 整體 $F$。
2. **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $SSR=1,200-384=816$，$p=2$，誤差 $df=27$。
4. **代入計算／推理：** $F=(816/2)/(384/27)=28.6875\approx28.69$，故 c。a 近 $R^2$；b、d 是錯誤均方比。
5. **解讀結論：** 正確答案是 **c** 。

**選項逐一：** a 的 0.73 容易與 $R^2=0.68$ 的量級混淆；b 的 1.47 來自錯誤的均方或自由度；c 正確，$F=(816/2)/(384/27)=28.69$；d 的 5.22 也不是正確均方比。

#### 選擇題 84 <a id="exam-ch15-mc-84"></a>

##### 題目

> Refer to Exhibit 15-8. The model
>
> a. is significant<br>
> b. is not significant<br>
> c. would be significant if the sample size was larger than 30<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 整體 $F$ 結論。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $F=28.69>3.35$。
4. **代入計算／推理：** 拒絕整體虛無假設，故 a。b 與比較相反；c 忽略現有樣本已顯著；d 因 a 正確而錯。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，$F=28.69>3.35$，模型整體顯著；b 錯在結論與 $F$ 比較結果相反；c 錯在現有 $n=30$ 已足以拒絕 $H_0$；d 錯，因為 a 已正確。

#### 選擇題 85 <a id="exam-ch15-mc-85"></a>

##### 題目

> Refer to Exhibit 15-8. The estimated income of a 30-year-old male is
>
> a. \$51,000<br>
> b. \$5,100<br>
> c. \$510<br>
> d. \$51

##### 詳解

> **回看投影片講義：** [複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 點預測與單位。
2. **選方法：** 使用[複迴歸點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** 男性 $X_2=0$，年齡 $X_1=30$；$Y$ 單位為千美元。
4. **代入計算／推理：** $30+0.7(30)=51$ 千美元，即 \$51,000，故 a。b、c、d 都漏掉正確單位換算。
5. **解讀結論：** 正確答案是 **a** 。

**選項逐一：** a 正確，男性代 $X_2=0$ 得 51 千美元，即 51,000 美元；b 的 5,100 美元少乘一個 10；c 的 510 美元少乘兩個 10；d 的 51 美元仍未完成由千美元到美元的換算。

### 計算題｜第 1–10 題：方程式、個別 t 與整體 F

#### 計算題 1 <a id="exam-ch15-problem-1"></a>

##### 題目

> The prices of Rawlston, Inc. stock ($y$) over a period of 12 days, the number of shares (in 100s) of company's stocks sold ($x_1$), and the volume of exchange (in millions) on the New York Stock Exchange ($x_2$) are shown below.
>
> | Day | $y$ | $x_1$ | $x_2$ |
> |---:|---:|---:|---:|
> | 1 | 87.50 | 950 | 11.00 |
> | 2 | 86.00 | 945 | 11.25 |
> | 3 | 84.00 | 940 | 11.75 |
> | 4 | 83.00 | 930 | 11.75 |
> | 5 | 84.50 | 935 | 12.00 |
> | 6 | 84.00 | 935 | 13.00 |
> | 7 | 82.00 | 932 | 13.25 |
> | 8 | 80.00 | 938 | 14.50 |
> | 9 | 78.50 | 925 | 15.00 |
> | 10 | 79.00 | 900 | 16.50 |
> | 11 | 77.00 | 875 | 17.00 |
> | 12 | 77.50 | 870 | 17.50 |
>
> Excel output:
>
> | Source | df | SS | MS | F | Significance F |
> |---|---:|---:|---:|---:|---:|
> | Regression | 2 | 118.8474 | 59.4237 | 40.9216 | 0.0000 |
> | Residual | 9 | 13.0692 | 1.4521 |  |  |
> | Total | 11 | 131.9167 |  |  |  |
>
> | Term | Coefficient | Standard Error | t Stat | P-value |
> |---|---:|---:|---:|---:|
> | Intercept | 118.5059 | 33.5753 | 3.5296 | 0.0064 |
> | $x_1$ | $-0.0163$ | 0.0315 | $-0.5171$ | 0.6176 |
> | $x_2$ | $-1.5726$ | 0.3590 | $-4.3807$ | 0.0018 |
>
> a. Use the output shown above and write an equation that can be used to predict the price of the stock.<br>
> b. Interpret the coefficients of the estimated regression equation that you found in Part a.<br>
> c. At 95% confidence, determine which variables are significant and which are not.<br>
> d. If in a given day, the number of shares sold was 94,500 and the volume of exchange was 16 million, what would you expect the price of the stock to be?

##### 詳解

> **回看投影片講義：** [方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)、[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 軟體輸出轉方程式、部分斜率、個別 $t$ 與點預測。
2. **選方法：** 依[方法選擇準則](./course2-slides-handout.html#compare-ch15-method-selection)，分別使用[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)與[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** 12 天觀測若有時間相依會影響推論；題目未給殘差診斷，計算暫依線性、獨立、等變異與常態誤差合理。$x_1$ 以「百股」計。
4. **代入計算／推理：**<br>
   a. $\hat y=118.5059-0.0163x_1-1.5726x_2$。<br>
   b. 固定交易所量，股票多成交 100 股，預測股價平均減少 \$0.0163；固定本公司成交股數，交易所總量增加 1 百萬，預測股價平均減少 \$1.5726。截距對 $x_1=x_2=0$，遠離資料範圍，不宜作商業解讀。<br>
   c. $\alpha=0.05$：$x_1$ 的 p-value 0.6176，不顯著；$x_2$ 的 p-value 0.0018，顯著。<br>
   d. 94,500 股是 $x_1=945$：$\hat y=118.5059-0.0163(945)-1.5726(16)=77.9408$。
5. **解讀結論：** 預測股價約 **\$77.94** ；控制交易所量後，樣本沒有足夠證據顯示本公司成交股數係數不為 0，但這不等於證明它沒有關係。

#### 計算題 2 <a id="exam-ch15-problem-2"></a>

##### 題目

> Multiple regression analysis was used to study how an individual's income ($Y$ in thousands of dollars) is influenced by age ($X_1$ in years), level of education ($X_2$ ranging from 1 to 5), and gender ($X_3$, where 0 = female and 1 = male). A sample of 20 gave:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | $X_1$ | 0.6251 | 0.094 |
> | $X_2$ | 0.9210 | 0.190 |
> | $X_3$ | $-0.510$ | 0.920 |
>
> | Source | Sum of Squares |
> |---|---:|
> | Regression | 84 |
> | Error | 112 |
>
> a. Compute the coefficient of determination.<br>
> b. Perform a $t$ test for the coefficient of level of education at $\alpha=0.05$.<br>
> c. Perform an $F$ test for the model at $\alpha=0.05$.<br>
> d. Fully interpret the coefficient of $X_3$.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)、[虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)


1. **辨認題型：** $R^2$、個別 $t$、整體 $F$、虛擬變數。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)與[虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)。
3. **檢查假設：** $n=20,p=3$，誤差 $df=16$；推論需線性、獨立、等變異、常態近似。教育 1–5 被當成等距數值，這是額外建模假設。
4. **代入計算／推理：**<br>
   a. $R^2=84/(84+112)=0.4286$。<br>
   b. $t=0.9210/0.190=4.847$，$t_{0.025,16}=2.120$，拒絕 $H_0:\beta_2=0$。<br>
   c. $F=(84/3)/(112/16)=4.000$；$F_{0.05;3,16}=3.239$，p-value $\approx0.0266$，拒絕整體 $H_0$。<br>
   d. 固定年齡與教育，男性($X_3=1$)的預測平均所得比女性($X_3=0$)少 $0.510$ 千美元，即 **\$510** 。
5. **解讀結論：** 模型解釋約 42.86% 的所得變異；教育係數與整體模型在 5% 水準顯著。性別係數是條件平均差，不是因果效果。

#### 計算題 3 <a id="exam-ch15-problem-3"></a>

##### 題目

> A multiple regression analysis between yearly income ($Y$ in \$1,000s), college GPA ($X_1$), age ($X_2$), and gender ($X_3$; 0 = female, 1 = male) was performed on 10 people.
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 4.0928 | 1.4400 |
> | $X_1$ | 10.0230 | 1.6512 |
> | $X_2$ | 0.1020 | 0.1225 |
> | $X_3$ | $-4.4811$ | 1.4400 |
>
> | Source | SS |
> |---|---:|
> | Regression | 360.59 |
> | Residual | 23.91 |
>
> a. Write the regression equation.<br>
> b. Interpret the coefficient of $X_3$.<br>
> c. Compute $R^2$.<br>
> d. Is the coefficient of $X_1$ significant? Use $\alpha=0.05$.<br>
> e. Is the coefficient of $X_2$ significant? Use $\alpha=0.05$.<br>
> f. Is the coefficient of $X_3$ significant? Use $\alpha=0.05$.<br>
> g. Perform an $F$ test and determine whether or not the model is significant.

##### 詳解

> **回看投影片講義：** [估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 完整複迴歸輸出判讀。
2. **選方法：** 用[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $n=10,p=3,df_E=6$；小樣本尤其依賴誤差常態與無嚴重離群。
4. **代入計算／推理：**<br>
   a. $\hat Y=4.0928+10.0230X_1+0.1020X_2-4.4811X_3$。<br>
   b. 固定 GPA 與年齡，男性預測平均年所得比女性少 $4.4811$ 千美元。<br>
   c. $R^2=360.59/(360.59+23.91)=0.9378$。<br>
   d.–f. $t_1=6.070$、$t_2=0.833$、$t_3=-3.112$；$t_{0.025,6}=2.447$，故 $X_1,X_3$ 顯著，$X_2$ 不顯著。<br>
   g. $F=(360.59/3)/(23.91/6)=30.162$；臨界值 $4.757$，p-value $\approx0.00051$，整體顯著。
5. **解讀結論：** 樣本內解釋約 93.78% 變異；整體顯著不表示三個變數都顯著，正好可由 $X_2$ 看出差別。

#### 計算題 4 <a id="exam-ch15-problem-4"></a>

##### 題目

> The following results were obtained from a multiple regression analysis.
>
> | Source | df | SS | MS |
> |---|---:|---:|---:|
> | Regression |  | 384 | 48 |
> | Error |  |  | 20 |
> | Total |  | 704 |  |
>
> a. How many independent variables were involved?<br>
> b. How many observations were involved?<br>
> c. Determine the $F$ statistic.

##### 詳解

> **回看投影片講義：** [整體 F 公式與自由度](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 從 ANOVA 缺格反推 $p,n,F$。
2. **選方法：** 使用[整體 F 公式與自由度](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $MSR=SSR/p$、$MSE=SSE/df_E$、$SST=SSR+SSE$。
4. **代入計算／推理：**<br>
   a. $p=384/48=8$。<br>
   b. $SSE=704-384=320$，$df_E=320/20=16$，故 $n=p+df_E+1=25$。<br>
   c. $F=48/20=2.40$。
5. **解讀結論：** 模型有 **8** 個解釋變數、**25** 筆觀測，整體統計量為 **2.40** ；是否顯著仍要指定 $\alpha$ 或 p-value。

#### 計算題 5 <a id="exam-ch15-problem-5"></a>

##### 題目

> Partial regression output:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 10.00 | 2.00 |
> | $X_1$ | $-2.00$ | 1.50 |
> | $X_2$ | 6.00 | 2.00 |
> | $X_3$ | $-4.00$ | 1.00 |
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression |  | 60 |
> | Error |  |  |
> | Total | 19 | 140 |
>
> a. Write the regression equation.<br>
> b. Compute and interpret $R^2$.<br>
> c. Test the relation between $X_1$ and $Y$ at $\alpha=0.05$.<br>
> d. Test the relation between $X_3$ and $Y$.<br>
> e. Test the overall model with $F$.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 係數、個別 $t$、整體 $F$。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** total $df=19$ 給 $n=20$；$p=3,df_E=16$。
4. **代入計算／推理：**<br>
   a. $\hat Y=10-2X_1+6X_2-4X_3$。<br>
   b. $R^2=60/140=0.4286$，解釋約 42.86% 的 $Y$ 樣本變異。<br>
   c. $t_1=-2/1.5=-1.333$，$|t|<2.120$，未拒絕 $H_0:\beta_1=0$。<br>
   d. $t_3=-4/1=-4.000$，拒絕 $H_0:\beta_3=0$。<br>
   e. $SSE=80$，$F=(60/3)/(80/16)=4.000>3.239$，p-value $\approx0.0266$，整體顯著。
5. **解讀結論：** 整體模型顯著、$X_3$ 顯著、$X_1$ 不顯著；不能從整體 $F$ 推成每個變數都顯著。

#### 計算題 6 <a id="exam-ch15-problem-6"></a>

##### 題目

> Sales volume ($Y$ in millions of dollars) is modeled by advertising expenditure ($X_1$ in millions) and number of salespeople ($X_2$), using 10 years.
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 7.0174 | 1.8972 |
> | $X_1$ | 8.6233 | 2.3968 |
> | $X_2$ | 0.0858 | 0.1845 |
>
> | Source | SS |
> |---|---:|
> | Regression | 321.11 |
> | Residual | 63.39 |
>
> a. Write the prediction equation.<br>
> b. Estimate sales for advertising of 3.5 million and 45 salespeople, in dollars.<br>
> c. Test the overall model at $\alpha=0.05$.<br>
> d. Test $\beta_1$ at $\alpha=0.05$.<br>
> e. Compute $R^2$.<br>
> f. Compute adjusted $R^2$.

##### 詳解

> **回看投影片講義：** [點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)


1. **辨認題型：** 預測、整體與個別推論、兩種 $R^2$。
2. **選方法：** 用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)。
3. **檢查假設：** $n=10,p=2,df_E=7$；10 年資料可能有自相關，原題未提供診斷。
4. **代入計算／推理：**<br>
   a. $\hat Y=7.0174+8.6233X_1+0.0858X_2$。<br>
   b. $\hat Y=41.05995$ 百萬，即約 **\$41,059,950** 。<br>
   c. $F=(321.11/2)/(63.39/7)=17.730>4.737$，p-value $\approx0.00182$，整體顯著。<br>
   d. $t_1=8.6233/2.3968=3.598>t_{0.025,7}=2.365$，廣告顯著。<br>
   e. $R^2=321.11/384.50=0.8351$。<br>
   f. $R_a^2=1-(1-0.8351)(9/7)=0.7880$。
5. **解讀結論：** 模型解釋約 83.51% 樣本變異；調整複雜度後約 78.80%。

#### 計算題 7 <a id="exam-ch15-problem-7"></a>

##### 題目

> Automobiles sold per day ($Y$) is modeled by price ($X_1$ in \$1,000) and advertising spots ($X_2$), using 7 days.
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 0.8051 |  |
> | $X_1$ | 0.4977 | 0.4617 |
> | $X_2$ | 0.4733 | 0.0387 |
>
> | Source | SS |
> |---|---:|
> | Regression | 40.700 |
> | Error | 1.016 |
>
> a. Determine the least-squares function.<br>
> b. Predict sales at a price of \$20,000 and 10 spots.<br>
> c. Test the overall model at $\alpha=0.05$.<br>
> d. Test price at 95% confidence.<br>
> e. Test advertising spots at 95% confidence.<br>
> f. Determine $R^2$.

##### 詳解

> **回看投影片講義：** [估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 小樣本複迴歸完整判讀。
2. **選方法：** 使用[估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=7,p=2,df_E=4$，推論對常態與離群非常敏感；價格 \$20,000 要代 $X_1=20$。
4. **代入計算／推理：**<br>
   a. $\hat Y=0.8051+0.4977X_1+0.4733X_2$。<br>
   b. $\hat Y=0.8051+0.4977(20)+0.4733(10)=15.4921$，約 15.5 台。<br>
   c. $F=(40.700/2)/(1.016/4)=80.118>6.944$，p-value $\approx0.00059$。<br>
   d. $t_1=0.4977/0.4617=1.078<2.776$，價格不顯著。<br>
   e. $t_2=0.4733/0.0387=12.230>2.776$，廣告顯著。<br>
   f. $R^2=40.700/(40.700+1.016)=0.9756$。
5. **解讀結論：** 整體模型顯著且樣本內配適很高，但只有廣告係數顯著；小樣本結果須審慎。

#### 計算題 8 <a id="exam-ch15-problem-8"></a>

##### 題目

> Regression of sales ($Y$ in millions), advertising ($X_1$ in thousands), and salespeople ($X_2$), with $n=10$:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | $-11.340$ | 20.412 |
> | $X_1$ | 0.798 | 0.332 |
> | $X_2$ | 0.141 | 0.278 |
>
> a. Write the regression equation.<br>
> b. Interpret the coefficients.<br>
> c. Test advertising at $\alpha=0.05$.<br>
> d. Test salespeople at $\alpha=0.05$.<br>
> e. Predict sales for \$50,000 advertising and 800 salespersons, in dollars.

##### 詳解

> **回看投影片講義：** [簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 係數解讀、個別 $t$、單位換算。
2. **選方法：** 依[簡單與複迴歸比較](./course2-slides-handout.html#compare-ch15-simple-vs-multiple)，用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)與[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** $p=2,n=10,df_E=7$；$X_1=50$，$X_2=800$；結果單位為百萬美元。
4. **代入計算／推理：**<br>
   a. $\hat Y=-11.340+0.798X_1+0.141X_2$。<br>
   b. 固定人數，廣告多 \$1,000，平均銷售預測多 0.798 百萬；固定廣告，多 1 位業務，平均銷售預測多 0.141 百萬。截距遠離合理範圍。<br>
   c. $t_1=2.404>2.365$，p-value 約 0.047，廣告剛達顯著。<br>
   d. $t_2=0.507<2.365$，人數不顯著。<br>
   e. $\hat Y=-11.340+0.798(50)+0.141(800)=141.36$ 百萬，即 **\$141,360,000** 。
5. **解讀結論：** 在模型單位與資料範圍合理的前提下，預測銷售約 1.4136 億美元；廣告的顯著結論很接近 5% 邊界。

#### 計算題 9 <a id="exam-ch15-problem-9"></a>

##### 題目

> ANOVA for sales ($Y$ in millions), advertising ($X_1$ in thousands), and salespeople ($X_2$):
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression | 2 | 822.088 |
> | Error | 7 | 736.012 |
>
> a. Test the model at $\alpha=0.05$.<br>
> b. Determine $R^2$.<br>
> c. Determine adjusted $R^2$.<br>
> d. Determine the sample size.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)


1. **辨認題型：** ANOVA 表與配適指標。
2. **選方法：** 使用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)。
3. **檢查假設：** $p=2,df_E=7$，故 $n=10$；推論條件需合理。
4. **代入計算／推理：**<br>
   a. $F=(822.088/2)/(736.012/7)=3.909$；$F_{0.05;2,7}=4.737$，p-value $\approx0.0724$，未拒絕整體 $H_0$。<br>
   b. $R^2=822.088/(822.088+736.012)=0.5276$。<br>
   c. 以未先四捨五入的 $R^2$ 計算，$R_a^2=1-(1-0.527622)(9/7)=0.3927$。<br>
   d. $n=p+df_E+1=10$。
5. **解讀結論：** 樣本內解釋約 52.76%，但在 5% 水準整體未顯著；「$R^2$ 看似不小」不能代替 $F$ 檢定。

#### 計算題 10 <a id="exam-ch15-problem-10"></a>

##### 題目

> Partial output based on 12 observations relating personal computers sold per month ($Y$), unit price ($X_1$ in \$1,000), and television spots ($X_2$):
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 17.145 | 7.865 |
> | $X_1$ | $-0.104$ | 3.282 |
> | $X_2$ | 1.376 | 0.250 |
>
> a. Write the prediction equation.<br>
> b. Interpret the coefficients.<br>
> c. Predict sales at a \$2,000 price and 10 spots.<br>
> d. Test price at $\alpha=0.05$.<br>
> e. Test spots at $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 方程式、部分斜率、個別 $t$。
2. **選方法：** 使用[估計方程式](./course2-slides-handout.html#formula-estimated-multiple-regression)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=12,p=2,df_E=9$；價格 \$2,000 代 $X_1=2$。
4. **代入計算／推理：**<br>
   a. $\hat Y=17.145-0.104X_1+1.376X_2$。<br>
   b. 固定廣告，價格多 \$1,000，預測月銷量少 0.104 台；固定價格，多一個廣告，預測月銷量多 1.376 台。截距未必有實務意義。<br>
   c. $\hat Y=17.145-0.104(2)+1.376(10)=30.697$ 台。<br>
   d. $t_1=-0.104/3.282=-0.0317$，不顯著。<br>
   e. $t_2=1.376/0.250=5.504>t_{0.025,9}=2.262$，顯著。
5. **解讀結論：** 預測約 30.7 台；控制另一變數後，只有廣告係數在 5% 水準顯著。

### 計算題｜第 11–20 題：ANOVA 補表、曲線項與模型顯著性

#### 計算題 11 <a id="exam-ch15-problem-11"></a>

##### 題目

> Partial ANOVA based on 12 observations relating computers sold ($Y$), unit price ($X_1$ in \$1,000), and advertising spots ($X_2$):
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression | 2 | 655.955 |
> | Residual | 9 |  |
> | Total |  | 838.917 |
>
> a. Test whether the model is significant at $\alpha=0.05$.<br>
> b. Determine $R^2$.<br>
> c. Determine adjusted $R^2$.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)


1. **辨認題型：** 由部分 ANOVA 補出整體檢定與配適。
2. **選方法：** 用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[調整後 $R^2$](./course2-slides-handout.html#formula-adjusted-r-squared)。
3. **檢查假設：** $n=12,p=2,df_E=9$。
4. **代入計算／推理：** $SSE=838.917-655.955=182.962$；$F=(655.955/2)/(182.962/9)=16.133$，p-value $\approx0.00106$，拒絕整體 $H_0$。$R^2=655.955/838.917=0.7819$；$R_a^2=1-(1-0.7819)(11/9)=0.7334$。
5. **解讀結論：** 模型整體顯著，解釋約 78.19% 樣本變異；調整後約 73.34%。

#### 計算題 12 <a id="exam-ch15-problem-12"></a>

##### 題目

> Output based on 30 days of stock price ($Y$ in dollars), Dow Jones average ($X_1$), and competitor stock price ($X_2$ in dollars):
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Constant | 20.000 | 5.455 |
> | $X_1$ | 0.006 | 0.002 |
> | $X_2$ | $-0.70$ | 0.200 |
>
> a. Write the prediction equation.<br>
> b. Predict when $X_1=10,000$ and the competitor price $X_2$ is \$50.<br>
> c. Test the Dow Jones coefficient at $\alpha=0.05$.<br>
> d. Test the competitor-price coefficient at $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 點預測與兩個個別 $t$。
2. **選方法：** 用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=30,p=2,df_E=27$；30 日價格可能有時間相依，原題未提供殘差診斷。
4. **代入計算／推理：**<br>
   a. $\hat Y=20+0.006X_1-0.70X_2$。<br>
   b. $20+0.006(10,000)-0.70(50)=45$，預測 **\$45** 。<br>
   c. $t_1=0.006/0.002=3.00>2.052$，顯著。<br>
   d. $t_2=-0.70/0.200=-3.50$，絕對值大於 2.052，顯著。
5. **解讀結論：** 控制另一價格後，兩個係數都顯著；這仍不表示股市變數對公司股價有因果效果。

#### 計算題 13 <a id="exam-ch15-problem-13"></a>

##### 題目

> Partial ANOVA relating company stock price ($Y$), Dow Jones average ($X_1$), and competitor price ($X_2$):
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression |  |  |
> | Residual | 20 | 40 |
> | Total |  | 800 |
>
> a. Determine the sample size.<br>
> b. Test the model at $\alpha=0.05$.<br>
> c. Determine $R^2$.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** ANOVA 自由度、$F$、$R^2$。
2. **選方法：** 使用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $p=2,df_E=20$。
4. **代入計算／推理：** $n=20+2+1=23$；$SSR=800-40=760$；$F=(760/2)/(40/20)=190$，臨界值 $F_{0.05;2,20}=3.493$，p-value $<10^{-12}$；$R^2=760/800=0.95$。
5. **解讀結論：** 樣本數 23，模型整體顯著，樣本內解釋 95% 變異；時間相依仍可能讓傳統 p-value 過度樂觀。

#### 計算題 14 <a id="exam-ch15-problem-14"></a>

##### 題目

> A regression was performed on 16 observations:
>
> $$\hat Y=23.5-14.28X_1+6.72X_2+15.68X_3.$$
>
> The standard errors are $s_{b_1}=4.2$，$s_{b_2}=5.6$，$s_{b_3}=2.8$。For this model, $SST=3,809.6$ and $SSR=3,285.4$.
>
> a. Compute the appropriate $t$ ratios.<br>
> b. Test $\beta_1,\beta_2,\beta_3$ at 5%.<br>
> c. Should any variable be dropped? Explain.<br>
> d. Compute $R^2$ and adjusted $R^2$; interpret $R^2$.<br>
> e. Test the overall relationship at 5%.

##### 詳解

> **回看投影片講義：** [個別 t 與整體 F 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)、[$R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)


1. **辨認題型：** 個別 $t$、模型簡化、兩種 $R^2$、整體 $F$。
2. **選方法：** 依[個別 t 與整體 F 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)及[$R^2$ 比較](./course2-slides-handout.html#compare-ch15-r2-vs-adjusted-r2)。
3. **檢查假設：** $n=16,p=3,df_E=12$；刪變數還需考慮理論、共線性與模型階層，不能只看一次 p-value。
4. **代入計算／推理：** $t_1=-14.28/4.2=-3.40$；$t_2=6.72/5.6=1.20$；$t_3=15.68/2.8=5.60$。臨界值 $2.179$，故 $X_1,X_3$ 顯著，$X_2$ 不顯著。$R^2=3285.4/3809.6=0.8624$；$R_a^2=1-(1-0.8624)(15/12)=0.8280$。$SSE=524.2$，$F=(3285.4/3)/(524.2/12)=25.070$，p-value $\approx1.87\times10^{-5}$。
5. **解讀結論：** 模型整體顯著並解釋約 86.24% 樣本變異。$X_2$ 可列為候選刪除項，但應先檢查理論必要性與刪除後係數是否穩定。

#### 計算題 15 <a id="exam-ch15-problem-15"></a>

##### 題目

> Multiple regression of supermarket profit ($Y$ in thousands) on food sales ($X_1$) and nonfood sales ($X_2$), also in thousands:
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression | 2 | 562.363 |
> | Residual | 9 | 225.326 |
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | $-15.0621$ |  |
> | $X_1$ | 0.0972 | 0.054 |
> | $X_2$ | 0.2484 | 0.092 |
>
> a. Write the equation.<br>
> b. Compute and interpret $R^2$.<br>
> c. Test the overall model at 0.05.<br>
> d. Test $X_1$ at 0.05.<br>
> e. Determine the number of supermarkets.

##### 詳解

> **回看投影片講義：** [估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 方程式、$R^2$、整體 $F$、個別 $t$、樣本數。
2. **選方法：** 使用[估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $p=2,df_E=9$，故 $n=12$。
4. **代入計算／推理：** $\hat Y=-15.0621+0.0972X_1+0.2484X_2$。$R^2=562.363/(562.363+225.326)=0.7140$。$F=(562.363/2)/(225.326/9)=11.231>4.256$，p-value $\approx0.00358$。$t_1=0.0972/0.054=1.800<2.262$，$X_1$ 不顯著。樣本數 $n=9+2+1=12$。
5. **解讀結論：** 模型解釋約 71.40% 樣本利潤變異且整體顯著，但控制非食品銷售後，食品銷售係數未達 5% 顯著。

#### 計算題 16 <a id="exam-ch15-problem-16"></a>

##### 題目

> A regression on 20 observations included $X$ and $Z$ with $Z=X^2$:
>
> $$\hat Y=23.72+12.61X+0.798Z.$$
>
> The standard errors are $s_{b_1}=4.85$ and $s_{b_2}=0.21$。For this model, $SSR=520.2$ and $SSE=340.6$.
>
> a. Estimate $Y$ when $X=5$.<br>
> b. Compute the $t$ ratios.<br>
> c. Test the coefficients at 5%.<br>
> d. Compute $R^2$ and adjusted $R^2$; interpret $R^2$.<br>
> e. Test the overall relationship at 5%.

##### 詳解

> **回看投影片講義：** [複迴歸估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)


1. **辨認題型：** 二次項模型中的預測與推論。
2. **選方法：** 仍按[複迴歸估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)處理，但先依關係算 $Z=X^2$。
3. **檢查假設：** $n=20,p=2,df_E=17$；因 $X$ 與 $X^2$ 屬同一曲線結構，解讀與刪除要維持模型階層。
4. **代入計算／推理：** $X=5$ 時 $Z=25$，$\hat Y=23.72+12.61(5)+0.798(25)=106.72$。$t_X=12.61/4.85=2.600$；$t_Z=0.798/0.21=3.800$；兩者均大於 $t_{0.025,17}=2.110$。$R^2=520.2/860.8=0.6043$；$R_a^2=0.5577$。$F=(520.2/2)/(340.6/17)=12.982$，p-value $\approx0.000378$。
5. **解讀結論：** 預測 $Y=106.72$；兩項及整體模型在 5% 水準顯著，模型解釋約 60.43% 樣本變異。

#### 計算題 17 <a id="exam-ch15-problem-17"></a>

##### 題目

> Family spending ($Y$), income ($X_1$), family size ($X_2$), and additions to savings ($X_3$); $Y,X_1,X_3$ are in thousands of dollars:
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression | 3 | 45.9634 |
> | Residual | 11 | 2.6218 |
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 0.0136 |  |
> | $X_1$ | 0.7992 | 0.074 |
> | $X_2$ | 0.2280 | 0.190 |
> | $X_3$ | $-0.5796$ | 0.920 |
>
> a. Write the equation.<br>
> b. Compute $R^2$ and discuss strength.<br>
> c. Test the overall model at 0.05.<br>
> d. Test $X_3$ at 0.05.

##### 詳解

> **回看投影片講義：** [整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)


1. **辨認題型：** 配適、整體與個別顯著性。
2. **選方法：** 依[整體 F 與個別 t 比較](./course2-slides-handout.html#compare-ch15-overall-f-vs-individual-t)。
3. **檢查假設：** $n=15,p=3,df_E=11$；家庭資料應為彼此獨立樣本。
4. **代入計算／推理：** $\hat Y=0.0136+0.7992X_1+0.2280X_2-0.5796X_3$。$R^2=45.9634/(45.9634+2.6218)=0.9460$。$F=(45.9634/3)/(2.6218/11)=64.281$，p-value $\approx2.93\times10^{-7}$。$t_3=-0.5796/0.920=-0.630$，未達 $|t|>t_{0.025,11}=2.201$。
5. **解讀結論：** 樣本內關係很強且整體顯著，但控制所得與家庭人數後，儲蓄增加額係數不顯著。

#### 計算題 18 <a id="exam-ch15-problem-18"></a>

##### 題目

> A regression model involving 3 independent variables for 20 periods resulted in $SSR=90$ and $SSE=100$.
>
> a. Compute and explain $R^2$.<br>
> b. Test the overall relationship at $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** $R^2$ 與整體 $F$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $n=20,p=3,df_E=16$；periods 可能有時間相依，需另查殘差。
4. **代入計算／推理：** $R^2=90/(90+100)=0.4737$。$F=(90/3)/(100/16)=4.800$；$F_{0.05;3,16}=3.239$，p-value $\approx0.0143$，拒絕整體 $H_0$。
5. **解讀結論：** 模型解釋約 47.37% 的樣本變異，且在 5% 水準整體顯著。

#### 計算題 19 <a id="exam-ch15-problem-19"></a>

##### 題目

> A regression model involving 8 independent variables for 69 periods resulted in $SSE=306$ and $SST=1,800$.
>
> a. Compute $R^2$.<br>
> b. Test whether the model is significant at $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 由 $SSE,SST$ 算配適與 $F$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $n=69,p=8,df_E=60$；periods 提醒需檢查獨立性。
4. **代入計算／推理：** $SSR=1,800-306=1,494$；$R^2=1,494/1,800=0.8300$。$F=(1,494/8)/(306/60)=36.618$；臨界值 $2.097$，p-value 約 $2.61\times10^{-20}$。
5. **解讀結論：** 模型解釋 83% 樣本變異並整體顯著；若誤差自相關，傳統顯著性仍需重新評估。

#### 計算題 20 <a id="exam-ch15-problem-20"></a>

##### 題目

> In a regression model involving 46 observations, the estimated equation was
>
> $$\hat Y=17+4X_1-3X_2+8X_3+5X_4+8X_5.$$
>
> For this model, $SST=3,410$ and $SSE=510$.
>
> a. Compute $R^2$.<br>
> b. Perform an $F$ test for the model.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** 由方程式數出 $p$，再算 $R^2,F$。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** 方程式有 $p=5$，$n=46,df_E=40$。
4. **代入計算／推理：** $SSR=3,410-510=2,900$；$R^2=2,900/3,410=0.8504$。$F=(2,900/5)/(510/40)=45.490$，$F_{0.05;5,40}=2.449$，p-value $\approx1.83\times10^{-15}$。
5. **解讀結論：** 模型解釋約 85.04% 樣本變異且整體高度顯著；仍不能由此判定每個 $X_j$ 都顯著。

### 計算題｜第 21–30 題：單位換算與虛擬變數

#### 計算題 21 <a id="exam-ch15-problem-21"></a>

##### 題目

> A microcomputer manufacturer models sales ($Y$ in \$10,000s) with price per unit (Price in \$100s), advertising (ADV in \$1,000s), and number of product lines (Lines).
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 1.0211 | 22.8752 |
> | Price | $-0.1524$ | 0.1411 |
> | ADV | 0.8849 | 0.2886 |
> | Lines | $-0.1463$ | 1.5340 |
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression |  | 2,708.61 |
> | Error | 14 | 2,840.51 |
>
> a. Write the prediction equation.<br>
> b. Predict sales for 10 product lines, advertising of \$40,000, and price \$3,000, in dollars.<br>
> c. Compute and interpret $R^2$.<br>
> d. Test Price at $\alpha=0.05$.<br>
> e. Test Lines at $\alpha=0.05$.<br>
> f. Test the overall model.<br>
> g. Interpret the Price coefficient.<br>
> h. Determine sample size.

##### 詳解

> **回看投影片講義：** [估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 完整輸出、不同金額單位與個別／整體檢定。
2. **選方法：** 使用[估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[$R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $p=3,df_E=14$，故 $n=18$；Price \$3,000 代 30，ADV \$40,000 代 40，$Y$ 最後乘 \$10,000。
4. **代入計算／推理：**<br>
   a. $\hat Y=1.0211-0.1524\text{Price}+0.8849\text{ADV}-0.1463\text{Lines}$。<br>
   b. $\hat Y=1.0211-0.1524(30)+0.8849(40)-0.1463(10)=30.3821$，即 **\$303,821** 。<br>
   c. $R^2=2708.61/(2708.61+2840.51)=0.4881$。<br>
   d. $t_{Price}=-0.1524/0.1411=-1.080$，不顯著。<br>
   e. $t_{Lines}=-0.1463/1.5340=-0.095$，不顯著。<br>
   f. $F=(2708.61/3)/(2840.51/14)=4.450>3.344$，p-value $\approx0.0215$，整體顯著。<br>
   g. 固定廣告與產品線，每提高 \$100 單價，預測平均銷售減少 $0.1524\times10,000=1,524$ 美元(即 \$1,524)。<br>
   h. $n=14+3+1=18$。
5. **解讀結論：** 整體模型顯著，但 Price 與 Lines 個別不顯著；這可能與 ADV 提供主要資訊或共線性有關。

#### 計算題 22 <a id="exam-ch15-problem-22"></a>

##### 題目

> Regression of sales ($Y$ in millions), advertising ($X_1$ in thousands), and salespeople ($X_2$), based on 10 observations:
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 40.00 | 7.00 |
> | $X_1$ | 8.00 | 2.50 |
> | $X_2$ | 6.00 | 3.00 |
>
> a. Predict sales for \$40,000 advertising and 30 salespersons, in dollars.<br>
> b. Test advertising at $\alpha=0.05$.<br>
> c. Test salespeople at $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 點預測與兩個個別 $t$。
2. **選方法：** 使用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=10,p=2,df_E=7$；廣告代 $X_1=40$，輸出為百萬美元。
4. **代入計算／推理：** $\hat Y=40+8(40)+6(30)=540$ 百萬，即 **\$540,000,000** 。$t_1=8/2.5=3.20>2.365$，廣告顯著；$t_2=6/3=2.00<2.365$，業務人數不顯著。
5. **解讀結論：** 預測銷售 5.4 億美元；控制另一變數後，只有廣告係數在 5% 水準顯著。

#### 計算題 23 <a id="exam-ch15-problem-23"></a>

##### 題目

> Sherri Cola models sales ($Y$ in \$10,000s) with PRICE (dollars), COMPRICE (dollars), ADV (in \$1,000s), and CONTAIN (1 = Cans, 0 = Bottles), with $n=25$.
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 443.143 |  |
> | PRICE | $-57.170$ | 20.426 |
> | COMPRICE | 27.681 | 19.991 |
> | ADV | 0.025 | 0.023 |
> | CONTAIN | $-95.353$ | 91.027 |
>
> a. Predict sales for cans, own price \$1.25, advertising \$200,000, and competitor price \$1.50, in dollars.<br>
> b. Test PRICE at 0.05.<br>
> c. Test ADV at 0.05.<br>
> d. Test CONTAIN at 0.05.<br>
> e. Test COMPRICE at 0.05.

##### 詳解

> **回看投影片講義：** [連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 混合連續與虛擬變數的點預測與個別 $t$。
2. **選方法：** 依[連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $p=4,n=25,df_E=20$；cans 代 1，廣告 \$200,000 代 ADV=200，輸出乘 \$10,000。
4. **代入計算／推理：** $\hat Y=443.143-57.170(1.25)+27.681(1.50)+0.025(200)-95.353(1)=322.849$，即 **\$3,228,490** 。臨界值 $t_{0.025,20}=2.086$：$t_{PRICE}=-2.799$ 顯著；$t_{ADV}=1.087$、$t_{CONTAIN}=-1.047$、$t_{COMPRICE}=1.385$，均不顯著。
5. **解讀結論：** 預測約 322.849 萬美元；控制其餘變數後，只有自家價格係數在 5% 水準顯著。

#### 計算題 24 <a id="exam-ch15-problem-24"></a>

##### 題目

> Brock Juice models sales ($Y$ in \$10,000s) with four independent variables: price ($X_1$), competitor price ($X_2$), advertising ($X_3$ in \$1,000s), and container ($X_4$; 1 = Cans, 0 = Bottles).
>
> | Source | df | SS |
> |---|---:|---:|
> | Regression | 4 | 283,940.60 |
> | Error | 18 | 621,735.14 |
>
> a. Compute and interpret $R^2$.<br>
> b. Test whether the model is significant at $\alpha=0.05$ and explain.<br>
> c. Determine sample size.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


1. **辨認題型：** ANOVA 的 $R^2$、整體 $F$、樣本數。
2. **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
3. **檢查假設：** $p=4,df_E=18$，故 $n=23$。
4. **代入計算／推理：** $R^2=283940.60/(283940.60+621735.14)=0.3135$。$F=(283940.60/4)/(621735.14/18)=2.055$；$F_{0.05;4,18}=2.928$，p-value $\approx0.1294$，未拒絕整體 $H_0$。$n=18+4+1=23$。
5. **解讀結論：** 模型解釋約 31.35% 樣本變異，但在 5% 水準沒有足夠證據認為至少一個斜率不為 0；這不是證明所有變數都無關。

#### 計算題 25 <a id="exam-ch15-problem-25"></a>

##### 題目

> The following model predicts furniture-store sales:
>
> $$\hat Y=10-4X_1+7X_2+18X_3,$$
>
> where $X_1$ is competitor's previous day's sales (in \$1,000s), $X_2$ is population within 1 mile (in 1,000s), $X_3=1$ if any advertising was used and 0 otherwise, and $\hat Y$ is sales (in \$1,000s).
>
> a. Interpret the coefficient of $X_3$.<br>
> b. Predict sales in dollars for competitor sales of \$3,000, population 10,000, and six radio advertisements.

##### 詳解

> **回看投影片講義：** [連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 虛擬變數解讀與點預測。
2. **選方法：** 依[連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，使用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** $X_3$ 表示「有無」廣告，不是廣告次數；六次仍代 $X_3=1$。$X_1=3,X_2=10$。
4. **代入計算／推理：** a. 固定競爭者銷售與人口，有使用任何廣告的店，預測平均銷售比無廣告店多 \$18,000。b. $\hat Y=10-4(3)+7(10)+18(1)=86$ 千美元。
5. **解讀結論：** 預測銷售 **\$86,000** ；原題給「六次」只是確認有廣告，不能把 6 代進 0/1 指標。

#### 計算題 26 <a id="exam-ch15-problem-26"></a>

##### 題目

> A sample of 30 houses modeled value ($Y$) using rooms ($X_1$), lot size ($X_2$), bathrooms ($X_3$), and garage dummy ($X_4=0$ if no garage, 1 otherwise).
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 15,232.5 | 8,462.5 |
> | $X_1$ | 2,178.4 | 778.0 |
> | $X_2$ | 7.8 | 2.2 |
> | $X_3$ | 2,675.2 | 2,229.3 |
> | $X_4$ | 1,157.8 | 463.1 |
>
> | Source | SS | MS |
> |---|---:|---:|
> | Regression | 204,242.88 | 51,060.72 |
> | Residual | 205,890.00 | 8,235.60 |
>
> a. Write the equation.<br>
> b. Interpret rooms.<br>
> c. Interpret the garage dummy.<br>
> d. Give regression and error degrees of freedom.<br>
> e. Test the overall model at 0.05 with hypotheses.<br>
> f. Test $\beta_1$ at 0.05 with hypotheses.<br>
> g. Compute and interpret $R^2$.<br>
> h. Estimate a house with 9 rooms, lot 7,500, 2 bathrooms, and 2 garages.

##### 詳解

> **回看投影片講義：** [虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[t](./course2-slides-handout.html#formula-multiple-regression-t-test)


1. **辨認題型：** 連續與虛擬變數的完整推論。
2. **選方法：** 依[虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，使用[估計式](./course2-slides-handout.html#formula-estimated-multiple-regression)、[F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
3. **檢查假設：** $n=30,p=4,df_E=25$；$X_4$ 只表示有無車庫，「2 garages」仍代 1，模型無法估每多一個車庫的效果。
4. **代入計算／推理：** $\hat Y=15232.5+2178.4X_1+7.8X_2+2675.2X_3+1157.8X_4$。固定其餘條件，多一房間預測價值多 \$2,178.4；有車庫比無車庫多 \$1,157.8。自由度為 4 與 25。整體假設 $H_0:\beta_1=\cdots=\beta_4=0$；$F=51060.72/8235.60=6.20>2.759$，p-value $\approx0.00131$，拒絕。房間檢定 $H_0:\beta_1=0$；$t=2178.4/778.0=2.800>2.060$，拒絕。$R^2=204242.88/(204242.88+205890)=0.4980$。預測 $=15232.5+2178.4(9)+7.8(7500)+2675.2(2)+1157.8(1)=99846.3$。
5. **解讀結論：** 預測價值 **\$99,846.30** ；模型整體與房間係數顯著，解釋約 49.80% 樣本房價變異。兩個車庫不能代 2，因為原變數只記錄「有／無」。

#### 計算題 27 <a id="exam-ch15-problem-27"></a>

##### 題目

> A sample of 25 families modeled monthly food expenditure using family members ($X_1$), meals outside home ($X_2$), and diet dummy ($X_3=1$ if a member is on a diet, 0 otherwise).
>
> | Term | Coefficient | Standard Error |
> |---|---:|---:|
> | Intercept | 450.08 | 53.6 |
> | $X_1$ | 49.92 | 9.6 |
> | $X_2$ | 10.12 | 2.2 |
> | $X_3$ | $-0.60$ | 12.0 |
>
> | Source | SS | MS |
> |---|---:|---:|
> | Regression | 3,078.39 | 1,026.13 |
> | Residual | 2,013.90 | 95.90 |
>
> a. Write the equation.<br>
> b. Interpret all coefficients.<br>
> c. Test $\beta_1,\beta_2,\beta_3$ at 1%.<br>
> d. Give regression and error degrees of freedom.<br>
> e. Test the overall model at 1% with hypotheses.<br>
> f. Compute and explain $R^2$.<br>
> g. Estimate expenditure for 4 members, 3 meals out, and no one on a diet.

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


1. **辨認題型：** 虛擬變數、個別 1% $t$、整體 1% $F$。
2. **選方法：** 使用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)與[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
3. **檢查假設：** $n=25,p=3,df_E=21$；1% 雙尾臨界值 $t_{0.005,21}=2.831$。
4. **代入計算／推理：** $\hat Y=450.08+49.92X_1+10.12X_2-0.60X_3$。截距是三個 $X$ 都 0 的預測；固定其餘變數，每多 1 人多 \$49.92，每多一次外食多 \$10.12，有節食成員相對無節食者少 \$0.60。$t_1=5.20$、$t_2=4.60$ 顯著；$t_3=-0.05$ 不顯著。自由度 3 與 21。整體 $H_0:\beta_1=\beta_2=\beta_3=0$；$F=1026.13/95.90=10.70>F_{0.01;3,21}\approx4.87$，拒絕。$R^2=3078.39/(3078.39+2013.90)=0.6045$。預測 $450.08+49.92(4)+10.12(3)=680.12$。
5. **解讀結論：** 預測月食物支出 **\$680.12** ；模型整體、家庭人數與外食次數在 1% 水準顯著，節食指標不顯著，解釋約 60.45% 樣本變異。

#### 計算題 28 <a id="exam-ch15-problem-28"></a>

##### 題目

> The following model predicts fast-food outlet sales:
>
> $$\hat Y=18-2X_1+7X_2+15X_3,$$
>
> where $X_1$ is competitors within 1 mile, $X_2$ is population within 1 mile (in 1,000s), $X_3=1$ if drive-up windows are present and 0 otherwise, and $\hat Y$ is sales (in \$1,000s).
>
> a. Interpret the coefficient 15 on $X_3$.<br>
> b. Predict for 2 competitors, population 10,000, and one drive-up window.<br>
> c. Predict for the same store with no drive-up window.

##### 詳解

> **回看投影片講義：** [連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 虛擬變數的組別差與兩次預測。
2. **選方法：** 依[連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，使用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** 固定競爭者與人口；人口 10,000 代 $X_2=10$。
4. **代入計算／推理：** a. 有 drive-up window 的店比沒有的店，預測平均銷售多 \$15,000。b. $18-2(2)+7(10)+15(1)=99$ 千美元。c. 改代 $X_3=0$ 得 $84$ 千美元。
5. **解讀結論：** 有窗口預測 **\$99,000** ，無窗口預測 **\$84,000** ；差額正好是虛擬變數係數 \$15,000。

#### 計算題 29 <a id="exam-ch15-problem-29"></a>

##### 題目

> The following model predicts computer-store sales:
>
> $$\hat Y=50-3X_1+20X_2+10X_3,$$
>
> where $X_1$ is competitor's previous day's sales (in \$1,000s), $X_2$ is population within 1 mile (in 1,000s), $X_3=1$ if radio advertising was used and 0 otherwise, and $\hat Y$ is sales (in \$1,000s).
>
> Predict sales in dollars for competitor sales of \$5,000, population 20,000, and nine radio advertisements.

##### 詳解

> **回看投影片講義：** [虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 含廣告虛擬變數的點預測。
2. **選方法：** 依[虛擬變數準則](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，使用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** $X_1=5,X_2=20$；九次廣告只代表「有使用」，所以 $X_3=1$，不是 9。
4. **代入計算／推理：** $\hat Y=50-3(5)+20(20)+10(1)=445$ 千美元。
5. **解讀結論：** 預測銷售 **\$445,000** ；若把 9 代進 $X_3$，就錯把指標變數當次數變數。

#### 計算題 30 <a id="exam-ch15-problem-30"></a>

##### 題目

> The following model predicts monthly shoe-store sales:
>
> $$\hat Y=40-3X_1+12X_2+10X_3,$$
>
> where $X_1$ is competitor's previous month's sales (in \$1,000s), $X_2$ is the store's previous month's sales (in \$1,000s), $X_3=1$ if radio advertising was used and 0 otherwise, and $\hat Y$ is sales (in \$1,000s).
>
> a. Predict sales for competitor sales \$9,000, own previous sales \$30,000, and no radio advertisements.<br>
> b. Predict for the same values with 10 radio advertisements.

##### 詳解

> **回看投影片講義：** [連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)、[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


1. **辨認題型：** 只改虛擬變數的情境比較。
2. **選方法：** 依[連續與虛擬變數比較](./course2-slides-handout.html#compare-ch15-continuous-vs-dummy)，使用[點估計](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
3. **檢查假設：** $X_1=9,X_2=30$；無廣告代 0，有 10 次廣告仍只代 1。
4. **代入計算／推理：** a. $40-3(9)+12(30)+10(0)=373$ 千美元。b. $40-3(9)+12(30)+10(1)=383$ 千美元。
5. **解讀結論：** 無廣告預測 **\$373,000** ；有廣告預測 **\$383,000** 。模型只估「有／無」帶來的 \$10,000 差異，無法區分 1 次與 10 次廣告。

<div class="page-break" style="page-break-after: always;"></div>

# 第 16 章：建立迴歸模型｜考古題詳解

## 考古題詳解

本章收錄 77 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–48 題

#### 選擇題 1 <a id="exam-ch16-mc-1"></a>

##### 題目

> A model in the form of $y=\beta_0+\beta_1z_1+\beta_2z_2+\cdots+\beta_pz_p+\epsilon$ where each independent variable $z_j$ (for $j=1,2,\ldots,p$) is a function of $x_j$. $x_j$ is known as the
>
> a. general linear model
>
> b. general curvilinear model
>
> c. multiplicative model
>
> d. multiplicative curvilinear model

##### 詳解

> **回看投影片講義：** [一般線性模型](./course2-slides-handout.html#formula-general-linear-model)


- **辨認題型：** 一般線性模型的定義題。
- **選方法：** 對照[一般線性模型](./course2-slides-handout.html#formula-general-linear-model)；重點是加工後的 $z_j$ 仍以係數的一次方進入模型。
- **檢查假設：** 這是術語辨識，不需抽樣假設。原文最後把「model」誤寫成 `$x_j$`，依前句判讀其本意。
- **代入計算／推理：** 方程式正是一般線性模型的標準形式。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確；b 會把「原始 $x$ 可彎曲」誤當成模型名稱；c、d 都不是本章採用的標準名稱。

#### 選擇題 2 <a id="exam-ch16-mc-2"></a>

##### 題目

> A test used to determine whether or not first order autocorrelation is present is
>
> a. z test
>
> b. t test
>
> c. Chi-square test
>
> d. Durbin-Watson Test

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch16-method-selection)、[Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)


- **辨認題型：** 一階自相關的檢定工具。
- **選方法：** 有時間順序且問相鄰誤差，依[方法選擇流程](./course2-slides-handout.html#compare-ch16-method-selection)使用[Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)。
- **檢查假設：** 應先有按時間排列的迴歸殘差；不是任意列次。
- **代入計算／推理：** z、t、卡方都不是本章的一階自相關專用檢定。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a、b 容易因「也是檢定」而誤選；c 是類別次數方法；d 才直接檢查一階自相關。

#### 選擇題 3 <a id="exam-ch16-mc-3"></a>

##### 題目

> In multiple regression analysis, the general linear model
>
> a. can not be used to accommodate curvilinear relationships between dependent variables and independent variables
>
> b. can be used to accommodate curvilinear relationships between the independent variables and dependent variable
>
> c. must contain more than 2 independent variables
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [二次模型](./course2-slides-handout.html#formula-quadratic-regression)


- **辨認題型：** 「線性」是否排除曲線的概念題。
- **選方法：** 看[二次模型](./course2-slides-handout.html#formula-quadratic-regression)：加入 $x^2$ 後仍對參數線性。
- **檢查假設：** 曲線形式要有圖形、理論或殘差支持；不是只為提高 $R^2$。
- **代入計算／推理：** 一般線性模型可以把 $x^2$ 當成加工變數。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 把參數線性誤成圖形直線；b 正確；c 錯在一個原始預測變數也能建立一般線性模型；d 因 b 正確而錯。

#### 選擇題 4 <a id="exam-ch16-mc-4"></a>

##### 題目

> The following model $Y=\beta_0+\beta_1X_1+\epsilon$ is referred to as a
>
> a. curvilinear model
>
> b. curvilinear model with one predictor variable
>
> c. simple second-order model with one predictor variable
>
> d. simple first-order model with one predictor variable

##### 詳解

> **回看投影片講義：** [一階模型](./course2-slides-handout.html#formula-first-order-regression)


- **辨認題型：** 依最高次方命名模型。
- **選方法：** 對照[一階模型](./course2-slides-handout.html#formula-first-order-regression)。
- **檢查假設：** 只辨識形式；$X_1$ 只有一次項。
- **代入計算／推理：** 沒有平方項或其他曲線項，所以是單一預測變數的一階模型。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a、b 都錯把直線稱曲線；c 需要 $X_1^2$；d 完整描述原式。

#### 選擇題 5 <a id="exam-ch16-mc-5"></a>

##### 題目

> In multiple regression analysis, the word linear in the term "general linear model" refers to the fact that
>
> a. $\beta_0,\beta_1,\ldots,\beta_p$ all have exponents of 0
>
> b. $\beta_0,\beta_1,\ldots,\beta_p$ all have exponents of 1
>
> c. $\beta_0,\beta_1,\ldots,\beta_p$ all have exponents of at least 1
>
> d. $\beta_0,\beta_1,\ldots,\beta_p$ all have exponents of less than 1

##### 詳解

> **回看投影片講義：** [一般線性模型](./course2-slides-handout.html#formula-general-linear-model)


- **辨認題型：** 參數線性的定義。
- **選方法：** 回看[一般線性模型](./course2-slides-handout.html#formula-general-linear-model)。
- **檢查假設：** 判斷的是參數 $\beta_j$，不是原始變數 $x_j$ 的次方。
- **代入計算／推理：** 每個參數都只以一次方出現。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 會讓係數全變成 1；b 正確；c 允許二次方參數，已非參數線性；d 也不符合定義。

#### 選擇題 6 <a id="exam-ch16-mc-6"></a>

##### 題目

> Serial correlation is
>
> a. the correlation between serial numbers of products
>
> b. the same as autocorrelation
>
> c. the same as leverage
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [一階自相關誤差模型](./course2-slides-handout.html#formula-ar-error-process)


- **辨認題型：** 術語同義辨識。
- **選方法：** 對照[一階自相關誤差模型](./course2-slides-handout.html#formula-ar-error-process)。
- **檢查假設：** 這裡的 serial 指按時間或順序的誤差，不是商品序號。
- **代入計算／推理：** serial correlation 與 autocorrelation 在本章同義。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 是字面誤導；b 正確；c 的 leverage 是自變數位置異常；d 因 b 正確而錯。

#### 選擇題 7 <a id="exam-ch16-mc-7"></a>

##### 題目

> The joint effect of two variables acting together is called
>
> a. autocorrelation
>
> b. interaction
>
> c. serial correlation
>
> d. joint regression

##### 詳解

> **回看投影片講義：** [交互作用模型](./course2-slides-handout.html#formula-interaction-regression)


- **辨認題型：** 交互作用術語題。
- **選方法：** 看[交互作用模型](./course2-slides-handout.html#formula-interaction-regression)。
- **檢查假設：** 「一起作用」指一個變數的效果隨另一個變數改變，不只是兩者相關。
- **代入計算／推理：** 乘積項 $X_1X_2$ 表示 interaction。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a、c 都是相鄰時間誤差的關係；b 正確；d 不是標準術語。

#### 選擇題 8 <a id="exam-ch16-mc-8"></a>

##### 題目

> A test to determine whether or not first-order autocorrelation is present is
>
> a. a t test
>
> b. an F test
>
> c. a test of interaction
>
> d. a chi-square test

##### 詳解

> **回看投影片講義：** [Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)


- **辨認題型：** 一階自相關檢定工具。
- **選方法：** 應使用[Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)。
- **檢查假設：** 需要有時間順序的迴歸殘差。
- **代入計算／推理：** a、b、c、d 都不是題目所問的專用檢定。
- **解讀結論：** **原題沒有正確選項**；應補上 “Durbin-Watson test”。
- **逐項判讀：** a 檢查單一係數；b 檢查整體或一組係數；c 檢查效果是否依條件改變；d 用於類別次數等問題，四者都不對。

#### 選擇題 9 <a id="exam-ch16-mc-9"></a>

##### 題目

> Which of the following tests is used to determine whether an additional variable makes a significant contribution to a multiple regression model?
>
> a. a t test
>
> b. a Z test
>
> c. an F test
>
> d. a chi-square test

##### 詳解

> **回看投影片講義：** [巢套 $F$](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 單一新增變數的貢獻。
- **選方法：** 題庫把「新增變數是否改善模型」放在模型建立脈絡，預期使用[巢套 $F$](./course2-slides-handout.html#formula-nested-model-f)；若只新增一個變數，[個別 $t$](./course2-slides-handout.html#formula-multiple-regression-t-test)也會給相同決策。
- **檢查假設：** 同一批資料、同一個 $y$，完整模型只多這一個變數，且一般迴歸條件合理。
- **代入計算／推理：** 單一新增參數時，巢套 $F=t^2$，所以 a 與 c 的統計決策等價；但本章題庫問的是模型加入變數後的額外貢獻，預期術語是 F test。
- **解讀結論：** 題庫預期答案是 **c**；由於只新增一個變數時 a 也數學等價，原題存在答案不唯一的問題。
- **逐項判讀：** a 可檢定單一新增係數，因此數學上也成立，但不是題庫的預期答案；b、d 不適用；c 是本章以小模型和完整模型比較新增貢獻的預期答案。

#### 選擇題 10 <a id="exam-ch16-mc-10"></a>

##### 題目

> A variable such as $Z$, whose value is $Z=X_1X_2$, is added to a general linear model in order to account for potential effects of two variables $X_1$ and $X_2$ acting together. This type of effect is
>
> a. impossible to occur
>
> b. called interaction
>
> c. called multicollinearity effect
>
> d. called transformation effect

##### 詳解

> **回看投影片講義：** [交互作用模型](./course2-slides-handout.html#formula-interaction-regression)


- **辨認題型：** 乘積項的用途。
- **選方法：** 對照[交互作用模型](./course2-slides-handout.html#formula-interaction-regression)。
- **檢查假設：** 應同時保留合理的主效果，並依題意或圖形支持交互作用。
- **代入計算／推理：** $X_1X_2$ 讓 $X_1$ 的斜率隨 $X_2$ 改變。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 明顯錯；b 正確；c 是自變數高度相關；d 太籠統，未指出共同效果。

#### 選擇題 11 <a id="exam-ch16-mc-11"></a>

##### 題目

> The following regression model $Y=\beta_0+\beta_1X_1+\beta_2X_1^2+\epsilon$ is known as
>
> a. first-order model with one predictor variable
>
> b. second-order model with two predictor variables
>
> c. second-order model with one predictor variable
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [二次模型](./course2-slides-handout.html#formula-quadratic-regression)


- **辨認題型：** 二次模型命名。
- **選方法：** 看[二次模型](./course2-slides-handout.html#formula-quadratic-regression)。
- **檢查假設：** $X_1$ 與 $X_1^2$ 是同一個原始預測變數的兩個加工項。
- **代入計算／推理：** 最高次方為 2，原始 predictor 只有 $X_1$。
- **解讀結論：** 答案是 **c**。
- **逐項判讀：** a 漏看平方項；b 把加工項誤算成兩個原始變數；c 正確；d 因 c 正確而錯。

#### 選擇題 12 <a id="exam-ch16-mc-12"></a>

##### 題目

> The parameters of nonlinear models have exponents
>
> a. larger than zero
>
> b. larger than 1
>
> c. larger than 2
>
> d. larger than 3

##### 詳解

> **回看投影片講義：** [指數模型線性化](./course2-slides-handout.html#formula-exponential-linearization)


- **辨認題型：** 題庫對非線性參數的簡化定義。
- **選方法：** 和[指數模型線性化](./course2-slides-handout.html#formula-exponential-linearization)對照，真正關鍵是參數不是以線性方式出現。
- **檢查假設：** 非線性不只可能來自「指數大於 1」，也可能來自參數相乘、位於分母或指數中。
- **代入計算／推理：** 依四個選項和題庫本意，選「larger than 1」。
- **解讀結論：** 題庫預期答案是 **b**，但敘述是過度簡化。
- **逐項判讀：** a 包含一次方線性模型；b 最接近題庫定義；c、d 又把範圍限得太窄。

#### 選擇題 13 <a id="exam-ch16-mc-13"></a>

##### 題目

> All the variables in a multiple regression analysis
>
> a. must be quantitative
>
> b. must be either quantitative or qualitative but not a mix of both
>
> c. must be positive
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)


- **辨認題型：** 複迴歸可接受的變數型態。
- **選方法：** 類別自變數可依[虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)編碼。
- **檢查假設：** 應變數在一般線性迴歸通常是數量型；自變數可混合連續與適當編碼的類別變數。
- **代入計算／推理：** a、b、c 都不是必要條件。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 忽略 dummy；b 錯在可以混用；c 負值也可進迴歸；d 正確。

#### 選擇題 14 <a id="exam-ch16-mc-14"></a>

##### 題目

> The range of the Durbin-Watson statistic is between
>
> a. $-1$ to $1$
>
> b. $0$ to $1$
>
> c. $-\infty$ to $+\infty$
>
> d. $0$ to $4$

##### 詳解

> **回看投影片講義：** [Durbin-Watson 公式](./course2-slides-handout.html#formula-durbin-watson)


- **辨認題型：** DW 統計量範圍。
- **選方法：** 回看[Durbin-Watson 公式](./course2-slides-handout.html#formula-durbin-watson)。
- **檢查假設：** 問的是 $d$，不是相關係數 $\rho$。
- **代入計算／推理：** $d$ 的範圍約為 0 到 4。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是相關係數常見範圍；b 太窄；c 無界不對；d 正確。

#### 選擇題 15 <a id="exam-ch16-mc-15"></a>

##### 題目

> The correlation in error terms that arises when the error terms at successive points in time are related is termed
>
> a. leverage
>
> b. multicorrelation
>
> c. autocorrelation
>
> d. parallel correlation

##### 詳解

> **回看投影片講義：** [一階自相關誤差模型](./course2-slides-handout.html#formula-ar-error-process)


- **辨認題型：** 時間相鄰誤差的名稱。
- **選方法：** 看[一階自相關誤差模型](./course2-slides-handout.html#formula-ar-error-process)。
- **檢查假設：** successive points 表示時間順序有意義。
- **代入計算／推理：** 相鄰誤差相關稱 autocorrelation。
- **解讀結論：** 答案是 **c**。
- **逐項判讀：** a 是高槓桿點；b、d 不是本章標準術語；c 正確。

#### 選擇題 16 <a id="exam-ch16-mc-16"></a>

##### 題目

> What value of Durbin-Watson statistic indicates no autocorrelation is present?
>
> a. 1
>
> b. 2
>
> c. -2
>
> d. 0

##### 詳解

> **回看投影片講義：** [Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)


- **辨認題型：** DW 的直覺判讀。
- **選方法：** 使用[Durbin-Watson 統計量](./course2-slides-handout.html#formula-durbin-watson)。
- **檢查假設：** 正式檢定仍要查 $d_L,d_U$；「2」是直覺中心，不是所有其他條件都成立的證明。
- **代入計算／推理：** $d\approx2$ 表示沒有明顯一階自相關。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 不是基準；b 正確；c 超出範圍；d 是強烈正自相關線索。

#### 選擇題 17 <a id="exam-ch16-mc-17"></a>

##### 題目

> When dealing with the problem of non-constant variance, the reciprocal transformation means using
>
> a. $1/X$ as the independent variable instead of $X$
>
> b. $X^2$ as the independent variable instead of $X$
>
> c. $Y^2$ as the dependent variable instead of $Y$
>
> d. $1/Y$ as the dependent variable instead of $Y$

##### 詳解

> **回看投影片講義：** [平方項 vs 轉換應變數](./course2-slides-handout.html#compare-ch16-method-selection)


- **辨認題型：** 應變數倒數轉換。
- **選方法：** 依[平方項 vs 轉換應變數](./course2-slides-handout.html#compare-ch16-method-selection)，漏斗型變異問題可考慮改變 $Y$ 尺度。
- **檢查假設：** $Y$ 不可為 0；轉換後要重新檢查殘差，且解讀在新尺度。
- **代入計算／推理：** reciprocal transformation 在本章指用 $1/Y$ 作應變數。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 改的是自變數；b 是平方項；c 是平方轉換；d 才是倒數應變數。

<a id="quiz-ch16-exhibit-1"></a>

#### 題組 16-1：選擇題 18–25 共用資料

> In a regression analysis involving 25 observations, the following estimated regression equation was developed.
>
> $$\widehat Y=10-18X_1+32X_2+14X_3$$
>
> Also, the following standard errors and the sum of squares were obtained.

| 量 | 數值 |
|---|---:|
| $S_{b_1}$ | 3 |
| $S_{b_2}$ | 6 |
| $S_{b_3}$ | 7 |
| $SST$ | 4,800 |
| $SSE$ | 1,296 |

這個 Exhibit 有 $n=25$、$k=3$，所以個別 t 與誤差的自由度都是 $25-3-1=21$。

#### 選擇題 18 <a id="exam-ch16-mc-18"></a>

##### 題目

> Refer to Exhibit 16-1. If you want to determine whether or not the coefficients of the independent variables are significant, the critical value of t statistic at $\alpha=0.05$ is
>
> a. 2.080
>
> b. 2.060
>
> c. 2.064
>
> d. 1.96

##### 詳解

> **回看投影片講義：** [個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** 個別係數的雙尾 t 檢定。
- **選方法：** 使用[個別 t 檢定](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** 一般迴歸誤差條件合理；df $=n-k-1=21$。
- **代入計算／推理：** $t_{0.025,21}=2.080$。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 對應 df 21；b、c 是其他自由度的近似值；d 是大樣本常態臨界值。

#### 選擇題 19 <a id="exam-ch16-mc-19"></a>

##### 題目

> Refer to Exhibit 16-1. The coefficient of $X_1$
>
> a. is significant
>
> b. is not significant
>
> c. can not be tested, because not enough information is provided
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** $\beta_1=0$ 的個別 t 檢定。
- **選方法：** 用[個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** Exhibit 給了係數、標準誤及 df 21，資訊足夠。
- **代入計算／推理：** $t=-18/3=-6$，$|t|>2.080$。
- **解讀結論：** 答案是 **a**；控制其他變數後，$X_1$ 的係數顯著不為 0。
- **逐項判讀：** a 正確；b 忽略了大 t 值；c 錯在資料足夠；d 因 a 正確而錯。

#### 選擇題 20 <a id="exam-ch16-mc-20"></a>

##### 題目

> Refer to Exhibit 16-1. The coefficient of $X_2$
>
> a. is significant
>
> b. is not significant
>
> c. can not be tested, because not enough information is provided
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** $\beta_2=0$ 的個別 t 檢定。
- **選方法：** 用[個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** df 21，雙尾 $\alpha=0.05$。
- **代入計算／推理：** $t=32/6=5.333$，大於 2.080。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確；b 把係數大小和標準誤關係看反；c 錯在可計算；d 不成立。

#### 選擇題 21 <a id="exam-ch16-mc-21"></a>

##### 題目

> Refer to Exhibit 16-1. The coefficient of $X_3$
>
> a. is significant
>
> b. is not significant
>
> c. can not be tested, because not enough information is provided
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** $\beta_3=0$ 的個別 t 檢定。
- **選方法：** 用[個別 t 公式](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** df 21，雙尾檢定。
- **代入計算／推理：** $t=14/7=2.000<2.080$。
- **解讀結論：** 答案是 **b**；在 5% 水準沒有足夠證據說 $\beta_3\ne0$。
- **逐項判讀：** a 容易因 2 看起來大而誤選；b 正確；c 錯在資訊足夠；d 不成立。

#### 選擇題 22 <a id="exam-ch16-mc-22"></a>

##### 題目

> Refer to Exhibit 16-1. The multiple coefficient of determination is
>
> a. 0.27
>
> b. 0.73
>
> c. 0.50
>
> d. 0.33

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** 多元 $R^2$。
- **選方法：** 用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
- **檢查假設：** $SST$ 與 $SSE$ 來自同一模型和同一應變數。
- **代入計算／推理：** $R^2=1-1296/4800=0.73$。
- **解讀結論：** 答案是 **b**；模型解釋樣本中 73% 的 $Y$ 變異。
- **逐項判讀：** a 是未解釋比例；b 正確；c、d 都沒有由平方和得到。

#### 選擇題 23 <a id="exam-ch16-mc-23"></a>

##### 題目

> Refer to Exhibit 16-1. If we are interested in testing for the significance of the relationship among the variables (i.e., significance of the model), the critical value of F at $\alpha=0.05$ is
>
> a. 2.76
>
> b. 2.78
>
> c. 3.10
>
> d. 3.07

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 複迴歸整體 F 的臨界值。
- **選方法：** 使用[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** 分子 df $=k=3$，分母 df $=21$。
- **代入計算／推理：** $F_{0.05;3,21}=3.072\approx3.07$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a、b、c 對應錯誤的自由度或四捨五入；d 對應 $(3,21)$。

#### 選擇題 24 <a id="exam-ch16-mc-24"></a>

##### 題目

> Refer to Exhibit 16-1. The test statistic for testing the significance of the model is
>
> a. 0.730
>
> b. 18.926
>
> c. 3.703
>
> d. 1.369

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 由平方和算整體 F。
- **選方法：** 用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $SSR=SST-SSE=3504$，df 為 3 與 21。
- **代入計算／推理：** $F=(3504/3)/(1296/21)=18.926$。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 是 $R^2$；b 正確；c、d 是錯誤除法組合。

#### 選擇題 25 <a id="exam-ch16-mc-25"></a>

##### 題目

> Refer to Exhibit 16-1. The p-value for testing the significance of the regression model is
>
> a. less than 0.01
>
> b. between 0.01 and 0.025
>
> c. between 0.025 and 0.05
>
> d. between 0.05 and 0.1

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體 F 的 p 值區間。
- **選方法：** 延續[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $F=18.926$，df $(3,21)$。
- **代入計算／推理：** 獨立重算得 $p\approx3.51\times10^{-6}<0.01$。
- **解讀結論：** 答案是 **a**；整體模型顯著，但不表示每個係數都顯著。
- **逐項判讀：** a 包含重算值；b、c、d 都太大。

<a id="quiz-ch16-exhibit-2"></a>

#### 題組 16-2：選擇題 26–34 共用資料

> In a regression model involving 30 observations, the following estimated regression equation was obtained.
>
> $$\widehat Y=170+34X_1-3X_2+8X_3+58X_4+3X_5$$
>
> For this model, $SSR=1{,}740$ and $SST=2{,}000$.

此處 $n=30$、$k=5$，所以迴歸、誤差、總自由度依序為 5、24、29。

#### 選擇題 26 <a id="exam-ch16-mc-26"></a>

##### 題目

> Refer to Exhibit 16-2. The value of SSE is
>
> a. 3,740
>
> b. 170
>
> c. 260
>
> d. 2000

##### 詳解

> **回看投影片講義：** [多元 $R^2$ 段落](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** ANOVA 平方和分解。
- **選方法：** 由[多元 $R^2$ 段落](./course2-slides-handout.html#formula-multiple-r-squared)使用 $SST=SSR+SSE$。
- **檢查假設：** 三個平方和來自同一資料與模型。
- **代入計算／推理：** $SSE=2000-1740=260$。
- **解讀結論：** 答案是 **c**。
- **逐項判讀：** a 錯把兩者相加；b 是截距；c 正確；d 是 SST。

#### 選擇題 27 <a id="exam-ch16-mc-27"></a>

##### 題目

> Refer to Exhibit 16-2. The degrees of freedom associated with SSR are
>
> a. 24
>
> b. 6
>
> c. 19
>
> d. 5

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 迴歸自由度。
- **選方法：** 依[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)，$df_R=k$。
- **檢查假設：** 方程式有五個斜率，不含截距。
- **代入計算／推理：** $df_R=5$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是誤差 df；b 把截距算進去；c 無對應；d 正確。

#### 選擇題 28 <a id="exam-ch16-mc-28"></a>

##### 題目

> Refer to Exhibit 16-2. The degrees of freedom associated with SSE are
>
> a. 24
>
> b. 6
>
> c. 19
>
> d. 5

##### 詳解

> **回看投影片講義：** [誤差均方](./course2-slides-handout.html#formula-mse-error-variance)


- **辨認題型：** 誤差自由度。
- **選方法：** 使用[誤差均方](./course2-slides-handout.html#formula-mse-error-variance)中的 $n-k-1$。
- **檢查假設：** $n=30,k=5$。
- **代入計算／推理：** $df_E=30-5-1=24$。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確；b 多算錯截距；c、d 都不是殘差 df。

#### 選擇題 29 <a id="exam-ch16-mc-29"></a>

##### 題目

> Refer to Exhibit 16-2. The degrees of freedom associated with SST are
>
> a. 24
>
> b. 6
>
> c. 19
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 總自由度。
- **選方法：** 回到[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)的 ANOVA 架構，其中 $df_T=n-1$。
- **檢查假設：** 有截距的標準迴歸 ANOVA。
- **代入計算／推理：** $df_T=30-1=29$，前三項都不是 29。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是殘差 df；b、c 皆錯；d 正確涵蓋 29 未列出的情況。

#### 選擇題 30 <a id="exam-ch16-mc-30"></a>

##### 題目

> Refer to Exhibit 16-2. The value of MSR is
>
> a. 10.40
>
> b. 348
>
> c. 10.83
>
> d. 52

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 迴歸均方。
- **選方法：** 使用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)中的 $MSR=SSR/k$。
- **檢查假設：** $SSR=1740,k=5$。
- **代入計算／推理：** $MSR=1740/5=348$。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a、c 接近 MSE；b 正確；d 是錯誤除數結果。

#### 選擇題 31 <a id="exam-ch16-mc-31"></a>

##### 題目

> Refer to Exhibit 16-2. The value of MSE is
>
> a. 348
>
> b. 10.40
>
> c. 10.83
>
> d. 32.13

##### 詳解

> **回看投影片講義：** [誤差均方公式](./course2-slides-handout.html#formula-mse-error-variance)


- **辨認題型：** 殘差均方。
- **選方法：** 用[誤差均方公式](./course2-slides-handout.html#formula-mse-error-variance)。
- **檢查假設：** $SSE=260,df_E=24$。
- **代入計算／推理：** $MSE=260/24=10.833\approx10.83$。
- **解讀結論：** 答案是 **c**。
- **逐項判讀：** a 是 MSR；b 是錯誤四捨五入或 df；c 正確；d 接近 F 而非 MSE。

#### 選擇題 32 <a id="exam-ch16-mc-32"></a>

##### 題目

> Refer to Exhibit 16-2. The test statistic F for testing the significance of the above model is
>
> a. 32.12
>
> b. 6.69
>
> c. 4.8
>
> d. 58

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體 F。
- **選方法：** 用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $MSR=348,MSE=10.833$。
- **代入計算／推理：** $F=348/(260/24)=32.123\approx32.12$。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確；b、c、d 都不是正確均方比。

#### 選擇題 33 <a id="exam-ch16-mc-33"></a>

##### 題目

> Refer to Exhibit 16-2. The p-value for testing the significance of the regression model is
>
> a. less than 0.01
>
> b. between 0.01 and 0.025
>
> c. between 0.025 and 0.05
>
> d. between 0.05 and 0.1

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體 F 的 p 值範圍。
- **選方法：** 使用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $F=32.123$，df $(5,24)$。
- **代入計算／推理：** 此 F 遠大於 5% 臨界值，重算 p 值遠小於 0.01。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確涵蓋極小 p 值；b、c、d 都太大。

#### 選擇題 34 <a id="exam-ch16-mc-34"></a>

##### 題目

> Refer to Exhibit 16-2. The coefficient of determination for this model is
>
> a. 0.6923
>
> b. 0.1494
>
> c. 0.1300
>
> d. 0.8700

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** $R^2$。
- **選方法：** 用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
- **檢查假設：** $SSR$ 與 $SST$ 同源。
- **代入計算／推理：** $R^2=1740/2000=0.8700$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a、b 不是平方和比；c 是未解釋比例；d 正確。

<a id="quiz-ch16-exhibit-3"></a>

#### 題組 16-3：選擇題 35–37 共用資料

> Below you are given a partial computer output based on a sample of 25 observations.

| 變數 | Coefficient | Standard Error |
|---|---:|---:|
| Constant | 145 | 29 |
| $X_1$ | 20 | 5 |
| $X_2$ | -18 | 6 |
| $X_3$ | 4 | 4 |

此處 $n=25,k=3$，所以誤差自由度為 21。

#### 選擇題 35 <a id="exam-ch16-mc-35"></a>

##### 題目

> Refer to Exhibit 16-3. The estimated regression equation is
>
> a. $Y=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3+\epsilon$
>
> b. $E(Y)=\beta_0+\beta_1X_1+\beta_2X_2+\beta_3X_3$
>
> c. $\widehat Y=29+5X_1+6X_2+4X_3$
>
> d. $\widehat Y=145+20X_1-18X_2+4X_3$

##### 詳解

> **回看投影片講義：** [估計複迴歸式](./course2-slides-handout.html#formula-estimated-multiple-regression)


- **辨認題型：** 從係數輸出寫估計式。
- **選方法：** 對照前章的[估計複迴歸式](./course2-slides-handout.html#formula-estimated-multiple-regression)。
- **檢查假設：** Coefficient 欄是 $b_j$；Standard Error 不能當係數。
- **代入計算／推理：** 依序放入 145、20、-18、4。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是含未知參數與誤差的母體模型；b 是母體平均式；c 誤用標準誤；d 才是估計式。

#### 選擇題 36 <a id="exam-ch16-mc-36"></a>

##### 題目

> Refer to Exhibit 16-3. We want to test whether the parameter $\beta_2$ is significant. The test statistic equals
>
> a. 4
>
> b. 5
>
> c. 3
>
> d. -3

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** $\beta_2=0$ 的 t 統計量。
- **選方法：** 用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** 係數為 -18、標準誤為 6。
- **代入計算／推理：** $t=-18/6=-3$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是 $X_1$ 的 t；b 是截距的 t；c 漏掉負號；d 正確。

#### 選擇題 37 <a id="exam-ch16-mc-37"></a>

##### 題目

> Refer to Exhibit 16-3. The critical t value obtained from the table to test an individual parameter at the 5% level is
>
> a. 2.06
>
> b. 2.069
>
> c. 2.074
>
> d. 2.080

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** 個別係數雙尾 t 臨界值。
- **選方法：** 使用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** df $=25-3-1=21$。
- **代入計算／推理：** $t_{0.025,21}=2.080$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a、b、c 是其他 df 或較粗略值；d 正確。

<a id="quiz-ch16-exhibit-4"></a>

#### 題組 16-4：選擇題 38–48 共用資料

> In a laboratory experiment, data were gathered on the life span ($Y$ in months) of 33 rats, units of daily protein intake ($X_1$), and whether or not agent $X_2$ (a proposed life extending agent) was added to the rats' diet ($X_2=0$ if agent $X_2$ was not added, and $X_2=1$ if agent was added). From the results of the experiment, the following regression model was developed.
>
> $$\widehat Y=36+0.8X_1-1.7X_2$$
>
> Also provided are $SSR=60$ and $SST=180$.

此處 $n=33,k=2$，所以 $SSE=120$，迴歸、誤差自由度為 2、30。$X_2$ 是 0-1 虛擬變數，不能解讀成劑量。

#### 選擇題 38 <a id="exam-ch16-mc-38"></a>

##### 題目

> Refer to Exhibit 16-4. From the above function, it can be said that the life expectancy of rats that were given agent $X_2$ is
>
> a. 1.7 months more than those who did not take agent $X_2$
>
> b. 1.7 months less than those who did not take agent $X_2$
>
> c. 0.8 months less than those who did not take agent $X_2$
>
> d. 0.8 months more than those who did not take agent $X_2$

##### 詳解

> **回看投影片講義：** [虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)


- **辨認題型：** 虛擬變數係數解讀。
- **選方法：** 使用[虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)。
- **檢查假設：** 比較時固定蛋白質攝取量 $X_1$。
- **代入計算／推理：** $X_2$ 從 0 變 1，預測值改變 $-1.7$ 個月。
- **解讀結論：** 答案是 **b**；這是模型中的平均差，不自動證明因果。
- **逐項判讀：** a 符號相反；b 正確；c、d 誤把蛋白質斜率 0.8 當 agent 效果。

#### 選擇題 39 <a id="exam-ch16-mc-39"></a>

##### 題目

> Refer to Exhibit 16-4. The life expectancy of a rat that was given 3 units of protein daily, and who took agent $X_2$ is
>
> a. 36.7
>
> b. 36
>
> c. 49
>
> d. 38.4

##### 詳解

> **回看投影片講義：** [複迴歸點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


- **辨認題型：** 虛擬變數模型的點預測。
- **選方法：** 用前章的[複迴歸點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
- **檢查假設：** 代入 $X_1=3,X_2=1$，且條件在資料合理範圍內。
- **代入計算／推理：** $36+0.8(3)-1.7(1)=36.7$。
- **解讀結論：** 答案是 **a**，單位是月。
- **逐項判讀：** a 正確；b 只取截距；c 錯誤相加；d 忽略 agent 的 -1.7。

#### 選擇題 40 <a id="exam-ch16-mc-40"></a>

##### 題目

> Refer to Exhibit 16-4. The life expectancy of a rat that was not given any protein and that did not take agent $X_2$ is
>
> a. 36.7
>
> b. 34.3
>
> c. 36
>
> d. 38.4

##### 詳解

> **回看投影片講義：** [估計複迴歸式](./course2-slides-handout.html#formula-estimated-multiple-regression)


- **辨認題型：** 截距解讀。
- **選方法：** 依[估計複迴歸式](./course2-slides-handout.html#formula-estimated-multiple-regression)代入條件。
- **檢查假設：** $X_1=0,X_2=0$，並注意 0 蛋白質是否在資料範圍會影響實務可信度。
- **代入計算／推理：** $\widehat Y=36$。
- **解讀結論：** 答案是 **c**。
- **逐項判讀：** a 是上一題；b 是 agent 組在零蛋白質；c 正確；d 是只加蛋白質效果的錯誤值。

#### 選擇題 41 <a id="exam-ch16-mc-41"></a>

##### 題目

> Refer to Exhibit 16-4. The life expectancy of a rat that was given 2 units of agent $X_2$ daily, but was not given any protein is
>
> a. 32.6
>
> b. 36
>
> c. 38
>
> d. 34.3

##### 詳解

> **回看投影片講義：** [虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)


- **辨認題型：** 虛擬變數編碼的適用範圍。
- **選方法：** 依[虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)，$X_2$ 只能是 0 或 1。
- **檢查假設：** 原題說「2 units of agent」卻令 $X_2$ 為 0-1 指標，條件不合法。
- **代入計算／推理：** 若機械代入 $X_2=2$，得到 $36-1.7(2)=32.6$；但這是超出模型定義的數字。
- **解讀結論：** 題庫預期 **a**，統計上應答「無法用此 0-1 模型預測兩單位劑量」。
- **逐項判讀：** a 是非法外插的機械結果；b 是無 agent；c 沒有公式依據；d 是合法的 $X_2=1$ 預測。原題本身有編碼矛盾。

#### 選擇題 42 <a id="exam-ch16-mc-42"></a>

##### 題目

> Refer to Exhibit 16-4. The degrees of freedom associated with SSR are
>
> a. 2
>
> b. 33
>
> c. 32
>
> d. 30

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 迴歸自由度。
- **選方法：** 依[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)，$df_R=k$。
- **檢查假設：** 模型有 $X_1,X_2$ 兩個斜率。
- **代入計算／推理：** $df_R=2$。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 正確；b 是樣本數；c 是總 df；d 是誤差 df。

#### 選擇題 43 <a id="exam-ch16-mc-43"></a>

##### 題目

> Refer to Exhibit 16-4. The degrees of freedom associated with SSE are
>
> a. 3
>
> b. 33
>
> c. 32
>
> d. 30

##### 詳解

> **回看投影片講義：** [誤差均方](./course2-slides-handout.html#formula-mse-error-variance)


- **辨認題型：** 誤差自由度。
- **選方法：** 用[誤差均方](./course2-slides-handout.html#formula-mse-error-variance)的 $n-k-1$。
- **檢查假設：** $n=33,k=2$。
- **代入計算／推理：** $df_E=33-2-1=30$。
- **解讀結論：** 答案是 **d**。
- **逐項判讀：** a 是參數總數但不是 residual df；b 是 n；c 是總 df；d 正確。

#### 選擇題 44 <a id="exam-ch16-mc-44"></a>

##### 題目

> Refer to Exhibit 16-4. The multiple coefficient of determination is
>
> a. 0.2
>
> b. 0.5
>
> c. 0.333
>
> d. 5

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** 多元 $R^2$。
- **選方法：** 用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
- **檢查假設：** $SSR=60,SST=180$。
- **代入計算／推理：** $R^2=60/180=0.333$。
- **解讀結論：** 答案是 **c**；模型解釋約 33.3% 樣本變異。
- **逐項判讀：** a、b 是錯誤比例；c 正確；d 超出 $R^2$ 範圍。

#### 選擇題 45 <a id="exam-ch16-mc-45"></a>

##### 題目

> Refer to Exhibit 16-4. If we want to test for the significance of the model, the critical value of F at 95% confidence is
>
> a. 4.17
>
> b. 3.32
>
> c. 2.92
>
> d. 1.96

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體 F 臨界值。
- **選方法：** 使用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** df $(2,30)$，$\alpha=0.05$。
- **代入計算／推理：** $F_{0.05;2,30}=3.316\approx3.32$。
- **解讀結論：** 答案是 **b**。
- **逐項判讀：** a 常見於 $(1,30)$；b 正確；c 對應別的 df；d 是常態臨界值。

#### 選擇題 46 <a id="exam-ch16-mc-46"></a>

##### 題目

> Refer to Exhibit 16-4. The test statistic for testing the significance of the model is
>
> a. 0.50
>
> b. 5.00
>
> c. 0.25
>
> d. 0.33

##### 詳解

> **回看投影片講義：** [整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 由平方和計算整體 F。
- **選方法：** 使用[整體 F 公式](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $SSE=180-60=120$，df 為 2 與 30。
- **代入計算／推理：** $F=(60/2)/(120/30)=30/4=7.50$。
- **解讀結論：** **原題沒有正確選項**；正確統計量是 7.50。
- **逐項判讀：** a、c、d 都是平方和比例的錯誤組合；b 也不是正確均方比。

#### 選擇題 47 <a id="exam-ch16-mc-47"></a>

##### 題目

> Refer to Exhibit 16-4. The p-value for testing the significance of the regression model is
>
> a. less than 0.01
>
> b. between 0.01 and 0.025
>
> c. between 0.025 and 0.05
>
> d. between 0.05 and 0.10

##### 詳解

> **回看投影片講義：** [整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體 F 的 p 值。
- **選方法：** 延續[整體 F 檢定](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** 使用正確的 $F=7.50$ 與 df $(2,30)$。
- **代入計算／推理：** 重算 $p\approx0.00228<0.01$。
- **解讀結論：** 答案是 **a**。
- **逐項判讀：** a 包含正確 p 值；b、c、d 都太大。

#### 選擇題 48 <a id="exam-ch16-mc-48"></a>

##### 題目

> Refer to Exhibit 16-4. The model
>
> a. is significant
>
> b. is not significant
>
> c. Not enough information is provided to answer this question.
>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 整體模型顯著性結論。
- **選方法：** 用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $F=7.50>3.32$ 且 $p\approx0.00228$。
- **代入計算／推理：** 在 5% 水準拒絕所有斜率同為 0。
- **解讀結論：** 答案是 **a**；至少一個斜率非 0，不代表兩個都顯著。
- **逐項判讀：** a 正確；b 與數值相反；c 錯在資訊足夠；d 不成立。

### 計算題｜第 1–29 題

#### 計算題 1 <a id="exam-ch16-problem-1"></a>

##### 題目

> In a regression analysis involving 21 observations and 4 independent variables, the following information was obtained.
>
> $$r^2=0.80,\qquad S=5.0$$
>
> Based on the above information, fill in all the blanks in the following ANOVA.
>
> Hint: $r^2=SSR/SST$, but also $r^2=1-SSE/SST$.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)


- **辨認題型：** 由 $R^2$ 與迴歸標準誤回填 ANOVA。
- **選方法：** 用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)和[估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)。
- **檢查假設：** $n=21,k=4$；$S=\sqrt{MSE}$，所以誤差 df 為 16。
- **代入計算／推理：** $MSE=5^2=25$，$SSE=25(16)=400$。由 $0.80=1-400/SST$ 得 $SST=2000$、$SSR=1600$；$MSR=1600/4=400$，$F=400/25=16$。
- **解讀結論：** 完整表如下；F 很大表示四個斜率合起來有強烈訊號，但題目未要求顯著性結論。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 4 | 1,600 | 400 | 16.00 |
| Error (Residual) | 16 | 400 | 25 |  |
| Total | 20 | 2,000 |  |  |

#### 計算題 2 <a id="exam-ch16-problem-2"></a>

##### 題目

> We are interested in determining what type of model best describes the relationship between two variables x and y.
>
> a. For a given data set, an estimated regression equation relating x and y of the form $\widehat y=b_0+b_1x$ was developed, using Excel. Comment on the adequacy of this equation for predicting y. Let $\alpha=.05$.

| Regression Statistics | Value |
|---|---:|
| Multiple R | 0.5095 |
| R Square | 0.2596 |
| Adjusted R Square | 0.1362 |
| Standard Error | 2.0745 |
| Observations | 8 |

| Source | df | SS | MS | F | Significance F |
|---|---:|---:|---:|---:|---:|
| Regression | 1 | 9.0536 | 9.0536 | 2.1037 | 0.1971 |
| Residual | 6 | 25.8214 | 4.3036 |  |  |
| Total | 7 | 34.875 |  |  |  |

| Term | Coefficient | Standard Error | t Stat | P-value |
|---|---:|---:|---:|---:|
| Intercept | 2.7857 | 1.6164 | 1.7234 | 0.1356 |
| x | 0.4643 | 0.3201 | 1.4504 | 0.1971 |

> b. An estimated regression equation for the same data set of the form $\widehat y=b_0+b_1x+b_2x^2$ was developed. Comment on the adequacy of this equation for predicting y. Let $\alpha=.05$.

| Regression Statistics | Value |
|---|---:|
| Multiple R | 0.9680 |
| R Square | 0.9370 |
| Adjusted R Square | 0.9118 |
| Standard Error | 0.6628 |
| Observations | 8 |

| Source | df | SS | MS | F | Significance F |
|---|---:|---:|---:|---:|---:|
| Regression | 2 | 32.6786 | 16.3392 | 37.1951 | 0.0010 |
| Residual | 5 | 2.1964 | 0.4393 |  |  |
| Total | 7 | 34.875 |  |  |  |

| Term | Coefficient | Standard Error | t Stat | P-value |
|---|---:|---:|---:|---:|
| Intercept | -2.8393 | 0.9247 | -3.0706 | 0.0278 |
| x | 3.8393 | 0.4714 | 8.1437 | 0.0005 |
| x-squared | -0.3750 | 0.0511 | -7.3335 | 0.0007 |

> c. Use the results of Part b and predict y when $x=4$.

##### 詳解

> **回看投影片講義：** [平方項 vs 轉換應變數](./course2-slides-handout.html#compare-ch16-method-selection)、[二次模型](./course2-slides-handout.html#formula-quadratic-regression)


- **辨認題型：** 直線與二次模型的比較，再做點預測。
- **選方法：** 依[平方項 vs 轉換應變數](./course2-slides-handout.html#compare-ch16-method-selection)，平均走勢需要彎曲時用[二次模型](./course2-slides-handout.html#formula-quadratic-regression)。
- **檢查假設：** 兩模型用同一組 8 筆資料；除顯著性外仍應看殘差，但題目未提供殘差圖。$x=4$ 應位於資料合理範圍才適合預測。
- **代入計算／推理：** a 的整體 p 值 0.1971，大於 0.05，直線模型沒有顯著關係且 $R^2=0.2596$。b 的整體 p 值 0.0010，$x^2$ 的 p 值 0.0007，且 adjusted $R^2$ 升至 0.9118，支持曲線。c：$\widehat y=-2.8393+3.8393(4)-0.375(4^2)=6.5179$。
- **解讀結論：** 在已給輸出下，二次模型明顯較合適；$x=4$ 時預測 $y\approx6.52$。顯著與高 $R^2$ 仍不能取代殘差診斷。

#### 計算題 3 <a id="exam-ch16-problem-3"></a>

##### 題目

> Consider the following data for two variables x and y.

| x | y |
|---:|---:|
| 1 | 1 |
| 4 | 6 |
| 7 | 9 |
| 8 | 7 |
| 9 | 4 |
| 10 | 3 |

> a. An estimated regression equation of the form $\widehat y=b_0+b_1x$ was developed. Comment on the adequacy of this equation for predicting y. Let $\alpha=.05$.

| Statistic | Linear model |
|---|---:|
| Multiple R | 0.3052 |
| R Square | 0.0932 |
| Adjusted R Square | -0.1335 |
| Standard Error | 3.0857 |
| Observations | 6 |
| Regression df / SS / MS | 1 / 3.9130 / 3.9130 |
| Residual df / SS / MS | 4 / 38.0870 / 9.5217 |
| F / Significance F | 0.4110 / 0.5564 |
| Intercept: coefficient / SE / t / p | 3.3043 / 2.9297 / 1.1279 / 0.3224 |
| x: coefficient / SE / t / p | 0.2609 / 0.4069 / 0.6411 / 0.5564 |

> b. A regression equation of the form $\widehat y=b_0+b_1x+b_2x^2$ was developed. Comment on the adequacy of this equation for predicting y. Let $\alpha=.05$.

| Statistic | Quadratic model |
|---|---:|
| Multiple R | 0.9508 |
| R Square | 0.9041 |
| Adjusted R Square | 0.8401 |
| Standard Error | 1.1588 |
| Observations | 6 |
| Regression df / SS / MS | 2 / 37.9713 / 18.9856 |
| Residual df / SS / MS | 3 / 4.0287 / 1.3430 |
| F / Significance F | 14.1376 / 0.0297 |
| Intercept: coefficient / SE / t / p | -2.6808 / 1.6196 / -1.655 / 0.1964 |
| x: coefficient / SE / t / p | 3.6803 / 0.6960 / 5.2879 / 0.0132 |
| x-squared: coefficient / SE / t / p | -0.3133 / 0.0622 / -5.036 / 0.0151 |

> c. Predict the value of y when $x=5$.

##### 詳解

> **回看投影片講義：** [二次模型](./course2-slides-handout.html#formula-quadratic-regression)


- **辨認題型：** 由先升後降的資料選二次模型並預測。
- **選方法：** 依[二次模型](./course2-slides-handout.html#formula-quadratic-regression)處理平均曲線。
- **檢查假設：** 六筆樣本很小；正式使用仍要看殘差。$x=5$ 位於 1 到 10 之間，是內插。
- **代入計算／推理：** 直線模型 p=0.5564、$R^2=0.0932$，不適合；二次模型 p=0.0297，平方項 p=0.0151，$R^2=0.9041$。預測為 $-2.6808+3.6803(5)-0.3133(25)=7.8882$。
- **解讀結論：** 二次模型較能描述先升後降；$x=5$ 時 $\widehat y\approx7.89$。

#### 計算題 4 <a id="exam-ch16-problem-4"></a>

##### 題目

> The following estimated regression equation has been developed for the relationship between y, the dependent variable, and x, the independent variable.
>
> $$\widehat y=60+200x-6x^2$$
>
> The sample size for this regression model was 23, and $SSR=600$ and $SSE=400$.
> a. Compute the coefficient of determination.
>
> b. Using $\alpha=.05$, test for a significant relationship.

##### 詳解

> **回看投影片講義：** [二次模型](./course2-slides-handout.html#formula-quadratic-regression)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 二次模型的 $R^2$ 與整體 F。
- **選方法：** 模型形式連到[二次模型](./course2-slides-handout.html#formula-quadratic-regression)，檢定用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $n=23,k=2$，誤差 df 20；迴歸誤差條件需合理。
- **代入計算／推理：** $R^2=600/(600+400)=0.60$。$F=(600/2)/(400/20)=15.00$；$F_{0.05;2,20}=3.493$，$p\approx0.000105$。
- **解讀結論：** 模型解釋 60% 樣本變異；拒絕 $H_0:\beta_1=\beta_2=0$，至少一個曲線係數有關，但不能只靠此檢定宣稱形狀完全正確。

#### 計算題 5 <a id="exam-ch16-problem-5"></a>

##### 題目

> A data set consisting of 7 observations of a dependent variable y and two independent variables $x_1$ and $x_2$ was used in a regression analysis. Using $x_1$ as the only independent variable,
>
> $$\widehat y=0.408+1.338x_1,\qquad SSE_q=39.535.$$
>
> Using both $x_1$ and $x_2$ yields
>
> $$\widehat y=0.805+0.498x_1-0.477x_2,\qquad SSE_p=1.015.$$
>
> Use an F test and determine if $x_2$ contributes significantly to the model. Let $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [巢套 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)、[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增單一變數的巢套模型檢定。
- **選方法：** 依[巢套 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** 同一批 7 筆資料、同一個 y，小模型可由完整模型令 $\beta_2=0$ 得到；$q=1,p=2$。
- **代入計算／推理：** $F=((39.535-1.015)/1)/(1.015/(7-2-1))=151.803$。df $(1,4)$，臨界值 7.709，$p\approx0.000249$。
- **解讀結論：** 拒絕 $H_0:\beta_2=0$；$x_2$ 對樣本內模型有顯著額外貢獻。樣本只有 7，仍要小心穩定性。

#### 計算題 6 <a id="exam-ch16-problem-6"></a>

##### 題目

> Monthly total production costs and the number of units produced at a local company over a period of 10 months are shown below.

| Month | Production Costs $Y_i$ (millions of dollars) | Units Produced $X_i$ (millions) |
|---:|---:|---:|
| 1 | 1 | 2 |
| 2 | 1 | 3 |
| 3 | 1 | 4 |
| 4 | 2 | 5 |
| 5 | 2 | 6 |
| 6 | 4 | 7 |
| 7 | 5 | 8 |
| 8 | 7 | 9 |
| 9 | 9 | 10 |
| 10 | 12 | 10 |

> a. Draw a scatter diagram for the above data.
>
> b. Assume that a model in the form $Y=\beta_0+\beta_1X^2+\epsilon$ best describes the relationship between X and Y. Estimate the parameters of this curvilinear regression equation.

##### 詳解

> **回看投影片講義：** [一般線性模型](./course2-slides-handout.html#formula-general-linear-model)


- **辨認題型：** 將 $Z=X^2$ 當解釋變數的曲線迴歸。
- **選方法：** 使用[一般線性模型](./course2-slides-handout.html#formula-general-linear-model)；此原題沒有一次項，必須照題目配適 $Y$ 對 $X^2$。
- **檢查假設：** 散點隨 X 上升且向上彎；月份提供順序，若做推論還應檢查時間自相關。本題只要求估計。
- **代入計算／推理：** 最小平方法對設計矩陣 $[1,X^2]$ 重算得 $b_0=-0.495935$、$b_1=0.101156$。
- **解讀結論：** 散點呈加速上升，估計式為 $\widehat Y=-0.4959+0.10116X^2$，Y 為百萬美元。注意本式不同於通常同時保留 $X$ 的二次模型。

#### 計算題 7 <a id="exam-ch16-problem-7"></a>

##### 題目

> Consider the following data.

| $Y_i$ | $X_i$ |
|---:|---:|
| 2 | 1 |
| 3 | 4 |
| 5 | 6 |
| 8 | 7 |
| 10 | 8 |

> a. Draw a scatter diagram. Does the relationship between X and Y appear to be linear?
>
> b. Assume the relationship can best be given by $Y=\beta_0+\beta_1X^2+\epsilon$. Estimate the parameters.

##### 詳解

> **回看投影片講義：** [一般線性模型](./course2-slides-handout.html#formula-general-linear-model)


- **辨認題型：** $X^2$ 單一加工變數的迴歸。
- **選方法：** 依[一般線性模型](./course2-slides-handout.html#formula-general-linear-model)令 $Z=X^2$。
- **檢查假設：** 散點整體上升，斜率隨 X 增大而變陡，曲線比固定斜率更合理；樣本僅 5 筆。
- **代入計算／推理：** 對 $[1,X^2]$ 最小平方重算得 $b_0=1.253190$、$b_1=0.130928$。
- **解讀結論：** 關係不是很像固定斜率直線；估計式為 $\widehat Y=1.2532+0.13093X^2$。

#### 計算題 8 <a id="exam-ch16-problem-8"></a>

##### 題目

> Part of an Excel output relating Y and 4 independent variables, $X_1$ through $X_4$, is shown below.

| Regression Statistics | Value |
|---|---:|
| Multiple R | ? |
| R Square | ? |
| Adjusted R Square | ? |
| Standard Error | 72.6093 |
| Observations | 20 |

| Source | df | SS | MS | F | Significance F |
|---|---:|---:|---:|---:|---:|
| Regression | ? | 422,975.2376 | ? | ? | 0.0000 |
| Residual | ? | ? | ? |  |  |
| Total | ? | ? |  |  |  |

| Term | Coefficient | Standard Error | t Stat | P-value |
|---|---:|---:|---:|---:|
| Intercept | -203.6125 | 100.2940 | ? | 0.0605 |
| $X_1$ | 0.6483 | 0.1110 | ? | 0.0000 |
| $X_2$ | 0.0190 | 0.0065 | ? | 0.0101 |
| $X_3$ | 40.4577 | 7.5940 | ? | 0.0001 |
| $X_4$ | -0.1032 | 20.7823 | ? | 0.9961 |

> a. Fill in all the blanks marked with “?”.
>
> b. At 95% confidence, which independent variables are significant and which ones are not? Fully explain.

##### 詳解

> **回看投影片講義：** [估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** 由標準誤與部分輸出回填複迴歸表，並做個別 t 判斷。
- **選方法：** 用[估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)與[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)。
- **檢查假設：** $n=20,k=4$，df 為 4、15、19。輸出只給四位小數，回算會有四捨五入差。
- **代入計算／推理：** $MSE=72.6093^2=5272.1104$，$SSE=5272.1104(15)=79081.6567$，$SST=502056.8943$。因此 Multiple R $=0.91787$、$R^2=0.84248$、adjusted $R^2=0.80048$、$MSR=105743.8094$、$F=20.0572$。t 值依序為 -2.0302、5.8405、2.9231、5.3276、-0.0050。
- **解讀結論：** 95% 水準下 $X_1,X_2,X_3$ 顯著，$X_4$ 不顯著；截距是否顯著不是題目重點。回填表如下。

| Source | df | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 4 | 422,975.2376 | 105,743.8094 | 20.0572 |
| Residual | 15 | 79,081.6567 | 5,272.1104 |  |
| Total | 19 | 502,056.8943 |  |  |

#### 計算題 9 <a id="exam-ch16-problem-9"></a>

##### 題目

> In a regression analysis involving 20 observations and five independent variables, the following information was obtained: total sum of squares $SST=990$ and residual mean square $MSE=30$. Fill in all blanks in the ANOVA table.

##### 詳解

> **回看投影片講義：** [誤差均方](./course2-slides-handout.html#formula-mse-error-variance)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 由 MSE 與 SST 回填 ANOVA。
- **選方法：** 用[誤差均方](./course2-slides-handout.html#formula-mse-error-variance)及[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $n=20,k=5$，df 為 5、14、19。
- **代入計算／推理：** $SSE=30(14)=420$，$SSR=990-420=570$，$MSR=570/5=114$，$F=114/30=3.80$。
- **解讀結論：** 完整表如下。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 5 | 570 | 114 | 3.80 |
| Error | 14 | 420 | 30 |  |
| Total | 19 | 990 |  |  |

#### 計算題 10 <a id="exam-ch16-problem-10"></a>

##### 題目

> A researcher is trying to decide whether or not to add another variable to his model. From $n=28$ observations, the smaller model is
>
> $$\widehat Y=23.62+18.86X_1+24.72X_2,$$
>
> with $SSE_q=1425$ and $SSR_q=1326$. With an additional variable $X_3$,
>
> $$\widehat Y=25.32+15.29X_1+7.63X_2+12.72X_3,$$
>
> with $SSE_p=1300$ and $SSR_p=1451$. What advice would you give? Use $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增一個變數的巢套 F。
- **選方法：** 使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)，其中 $q=2,p=3$。
- **檢查假設：** 兩模型使用同一批資料與同一 Y，且小模型由完整模型令 $\beta_3=0$ 得到。
- **代入計算／推理：** $F=((1425-1300)/1)/(1300/(28-3-1))=2.3077$。df $(1,24)$，臨界值 4.2597，$p\approx0.1418$。
- **解讀結論：** 不拒絕 $H_0:\beta_3=0$；在 5% 水準沒有足夠證據支持加入 $X_3$。這不等於證明它永遠無用，還可考慮預測成本與外部驗證。

#### 計算題 11 <a id="exam-ch16-problem-11"></a>

##### 題目

> We want to test whether or not the addition of 3 variables to a model will be statistically significant. Based on $n=25$ observations, the smaller model is
>
> $$\widehat Y=62.42-1.836X_1+25.62X_2,$$
>
> with $SSE_q=725$ and $SSR_q=526$. Including the 3 variables gives
>
> $$\widehat Y=59.23-1.762X_1+25.638X_2+16.237X_3+15.297X_4-18.723X_5,$$
>
> with $SSE_p=520$ and $SSR_p=731$.
> a. State the null and alternative hypotheses.
>
> b. Test the null hypothesis at the 5% level.

##### 詳解

> **回看投影片講義：** [一次問一組係數用 F](./course2-slides-handout.html#compare-ch16-method-selection)、[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 一次新增三個變數的巢套 F。
- **選方法：** 依[一次問一組係數用 F](./course2-slides-handout.html#compare-ch16-method-selection)，使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** 同一批 25 筆資料；$q=2,p=5$；完整模型誤差 df $=19$。
- **代入計算／推理：** $H_0:\beta_3=\beta_4=\beta_5=0$；$H_a$：至少一個不為 0。$F=((725-520)/3)/(520/19)=2.4968$，臨界值 $F_{0.05;3,19}=3.1274$，$p\approx0.0908$。
- **解讀結論：** 不拒絕 $H_0$；5% 水準下，三個新增變數合起來沒有顯著改善證據。

#### 計算題 12 <a id="exam-ch16-problem-12"></a>

##### 題目

> Multiple regression analysis was used to study Y with three independent variables $X_1,X_2,X_3$, involving 20 observations.

| Term | Coefficient | Standard Error |
|---|---:|---:|
| Intercept | 20.00 | 5.00 |
| $X_1$ | 15.00 | 3.00 |
| $X_2$ | 8.00 | 5.00 |
| $X_3$ | -18.00 | 10.00 |

| Source | Given information |
|---|---:|
| Regression | $MSR=80$ |
| Error | $SSE=320$ |

> a. Compute the coefficient of determination.
>
> b. Test whether $\beta_1$ differs from zero at $\alpha=.05$.
>
> c. Test whether $\beta_2$ differs from zero.
>
> d. Test whether $\beta_3$ differs from zero.
> e. Test whether the regression model is significant.

##### 詳解

> **回看投影片講義：** [整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)、[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 同時考 $R^2$、個別 t 與整體 F。
- **選方法：** 依[整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)，單一係數用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)，全體用[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $n=20,k=3$，誤差 df 16；$t_{0.025,16}=2.120$，一般迴歸條件需合理。
- **代入計算／推理：** $SSR=80(3)=240$，$SST=240+320=560$，$R^2=240/560=0.4286$。$t_1=15/3=5$，$t_2=8/5=1.6$，$t_3=-18/10=-1.8$。$MSE=320/16=20$，$F=80/20=4.00$，$F_{0.05;3,16}=3.239$，$p\approx0.0266$。
- **解讀結論：** 模型解釋 42.86% 樣本變異；$X_1$ 顯著，$X_2,X_3$ 不顯著；整體模型顯著。整體顯著與部分個別係數不顯著可以同時發生。

#### 計算題 13 <a id="exam-ch16-problem-13"></a>

##### 題目

> Multiple regression analysis was used to study Y with four independent variables $X_1,X_2,X_3,X_4$, involving 31 observations.

| Term | Coefficient | Standard Error |
|---|---:|---:|
| Intercept | 18.00 | 6.00 |
| $X_1$ | 12.00 | 8.00 |
| $X_2$ | 24.00 | 48.00 |
| $X_3$ | -36.00 | 36.00 |
| $X_4$ | 16.00 | 2.00 |

| Source | Given information |
|---|---:|
| Regression | $MSR=125$ |
| Total | $SST=760$ |

> a. Compute the coefficient of determination.
>
> b. Test whether $\beta_1$ differs from zero at $\alpha=.05$.
>
> c. Test whether $\beta_4$ differs from zero.
>
> d. Test whether the regression model is significant.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)


- **辨認題型：** 多元 $R^2$、個別 t、整體 F。
- **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)及[整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)。
- **檢查假設：** $n=31,k=4$，誤差 df 26；$t_{0.025,26}=2.056$。
- **代入計算／推理：** $SSR=125(4)=500$，$SSE=760-500=260$，$R^2=500/760=0.6579$，$MSE=260/26=10$。$t_1=12/8=1.5$ 不顯著；$t_4=16/2=8$ 顯著。$F=125/10=12.5$，$p\approx8.40\times10^{-6}$。
- **解讀結論：** 模型解釋 65.79% 樣本變異；$X_1$ 無顯著額外貢獻證據，$X_4$ 有；整體模型顯著。

#### 計算題 14 <a id="exam-ch16-problem-14"></a>

##### 題目

> A regression model relating Y with one independent variable $X_1$ resulted in $SSE_q=400$. Another model with $X_1$ and $X_2$ resulted in $SSE_p=320$. At $\alpha=.05$, determine if $X_2$ contributed significantly. The sample size for both models was 20.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增單一變數的巢套 F。
- **選方法：** 用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)，$q=1,p=2$。
- **檢查假設：** 兩模型同資料、同 Y、確實巢套；完整模型誤差 df 17。
- **代入計算／推理：** $F=((400-320)/1)/(320/17)=4.25$。臨界值 4.451，$p\approx0.0549$。
- **解讀結論：** 不拒絕 $H_0:\beta_2=0$；結果很接近 0.05，但仍不能把 0.0549 說成顯著。

#### 計算題 15 <a id="exam-ch16-problem-15"></a>

##### 題目

> A regression model with $X_1$ resulted in $SSE_q=50$. When $X_2$ was added, $SSE_p=40$. At $\alpha=.05$, determine if $X_2$ contributes significantly. The sample size was 30.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增單一變數。
- **選方法：** 使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** $q=1,p=2,n=30$，完整模型誤差 df 27。
- **代入計算／推理：** $F=(50-40)/(40/27)=6.75$，臨界值 4.210，$p\approx0.0150$。
- **解讀結論：** 拒絕 $H_0$；$X_2$ 對模型有顯著額外貢獻。

#### 計算題 16 <a id="exam-ch16-problem-16"></a>

##### 題目

> A model relating sales Y to product price $X_1$ had $SSE_q=495$. A second model using product price $X_1$ and competitor's product price $X_2$ had $SSE_p=396$. At $\alpha=.05$, determine if competitor's price contributed significantly. The sample size was 33.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增競品價格的巢套 F。
- **選方法：** 用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** $q=1,p=2,n=33$，完整模型誤差 df 30。
- **代入計算／推理：** $F=(495-396)/(396/30)=7.50$，臨界值 4.171，$p\approx0.0103$。
- **解讀結論：** 拒絕 $H_0$；控制自家價格後，競品價格有顯著額外關聯。這不自動證明因果。

#### 計算題 17 <a id="exam-ch16-problem-17"></a>

##### 題目

> A regression model relating units sold (Y), price ($X_1$), and whether promotion was used ($X_2=1$ if used, 0 otherwise) resulted in
>
> $$\widehat Y=120-0.03X_1+0.7X_2.$$
>
> Also, $n=15$, $S_{b_1}=0.01$, $S_{b_2}=0.1$.
> a. Is price a significant variable?
>
> b. Is promotion significant?

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)


- **辨認題型：** 兩個個別係數的 t 檢定，其中 $X_2$ 是虛擬變數。
- **選方法：** 使用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)；promotion 的解讀連到[虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)。
- **檢查假設：** $k=2$，df $=15-2-1=12$，雙尾臨界值 2.179。
- **代入計算／推理：** price: $t=-0.03/0.01=-3.00$，$p\approx0.0111$；promotion: $t=0.7/0.1=7.00$，$p\approx1.43\times10^{-5}$。
- **解讀結論：** 兩者在 5% 水準都顯著。控制 promotion 後價格每增一單位，預測銷量減 0.03；控制價格後，有促銷的預測銷量比無促銷高 0.7 單位。

#### 計算題 18 <a id="exam-ch16-problem-18"></a>

##### 題目

> A regression model relating yearly income (Y), age ($X_1$), and gender ($X_2=1$ if female and 0 if male) resulted in
>
> $$\widehat Y=5000+1.2X_1+0.9X_2.$$
>
> $n=20$, $SSE=500$, $SSR=1500$, $S_{b_1}=0.2$, $S_{b_2}=0.1$.
> a. Is gender a significant variable?
>
> b. Determine the multiple coefficient of determination.

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** 虛擬變數的個別 t 與 $R^2$。
- **選方法：** 用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)及[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
- **檢查假設：** $k=2$，df 17，$X_2$ 為 0-1；收入的單位未明示，係數只能用題目單位解讀。
- **代入計算／推理：** gender 的 $t=0.9/0.1=9.0$，遠大於 $t_{0.025,17}=2.110$；$R^2=1500/(1500+500)=0.75$。
- **解讀結論：** gender 係數顯著；模型解釋 75% 樣本收入變異。觀察到性別差異不等於性別造成收入差異，仍可能有職級等混雜。

#### 計算題 19 <a id="exam-ch16-problem-19"></a>

##### 題目

> A regression analysis with 8 independent variables obtained $R^2=0.80$, $SSR=4280$, and $n=56$.
> a. Fill in the ANOVA table.
>
> b. Is the model significant? Let $\alpha=.05$.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** 由 $R^2$、SSR 回填 ANOVA 並做整體 F。
- **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)及[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $n=56,k=8$，df 為 8、47、55。
- **代入計算／推理：** $SST=4280/0.80=5350$，$SSE=1070$；$MSR=535$，$MSE=1070/47=22.766$，$F=23.50$，臨界值 2.143，$p\approx5.47\times10^{-14}$。
- **解讀結論：** 整體模型顯著；至少一個斜率非 0。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 8 | 4,280 | 535.000 | 23.50 |
| Error | 47 | 1,070 | 22.766 |  |
| Total | 55 | 5,350 |  |  |

#### 計算題 20 <a id="exam-ch16-problem-20"></a>

##### 題目

> In a regression analysis involving 18 observations and four independent variables: Multiple R $=0.6000$, R Square $=0.3600$, Standard Error $=4.8000$. Fill in all blanks in the ANOVA table.

##### 詳解

> **回看投影片講義：** [估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** 由 $R^2$ 與標準誤回填 ANOVA。
- **選方法：** 用[估計標準誤](./course2-slides-handout.html#formula-standard-error-estimate)和[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)。
- **檢查假設：** $n=18,k=4$，df 為 4、13、17。
- **代入計算／推理：** $MSE=4.8^2=23.04$，$SSE=23.04(13)=299.52$。因 $SSE=(1-0.36)SST$，$SST=468.00$、$SSR=168.48$；$MSR=42.12$，$F=1.8281$。
- **解讀結論：** 完整表如下；若額外做 5% 檢定，$p\approx0.184$，整體不顯著。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 4 | 168.48 | 42.12 | 1.8281 |
| Error | 13 | 299.52 | 23.04 |  |
| Total | 17 | 468.00 |  |  |

#### 計算題 21 <a id="exam-ch16-problem-21"></a>

##### 題目

> Partial results of a regression analysis involving sales (Y in millions of dollars), advertising expenditures ($X_1$ in thousands of dollars), and number of salespeople ($X_2$), based on 10 observations:

| Term | Coefficient | Standard Error |
|---|---:|---:|
| Constant | 50.00 | 20.00 |
| $X_1$ | 3.60 | 1.20 |
| $X_2$ | 0.20 | 0.20 |

> a. At $\alpha=.05$, test the coefficient of advertising.
>
> b. If the company uses \$20,000 in advertisement and has 300 salespersons, what are expected sales in dollars?

##### 詳解

> **回看投影片講義：** [個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)、[點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


- **辨認題型：** 個別 t 與帶單位的點預測。
- **選方法：** 用[個別 t](./course2-slides-handout.html#formula-multiple-regression-t-test)和[點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)。
- **檢查假設：** $n=10,k=2$，df 7；$20{,}000$ 美元要換成 $X_1=20$ 個千美元，$X_2=300$。
- **代入計算／推理：** $t=3.6/1.2=3.00$，$t_{0.025,7}=2.365$，$p\approx0.0199$。$\widehat Y=50+3.6(20)+0.2(300)=182$ 百萬美元。
- **解讀結論：** advertising 係數顯著；預期銷售為 **\$182,000,000** 。若忘記單位換算，答案會差一千倍。

#### 計算題 22 <a id="exam-ch16-problem-22"></a>

##### 題目

> A regression analysis with 4 independent variables obtained $R^2=0.80$, $SSR=680$, and $n=45$.
> a. Fill in the ANOVA table.
>
> b. At $\alpha=.05$, test whether the model is significant.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** ANOVA 回填與整體 F。
- **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)及[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $k=4$，df 為 4、40、44。
- **代入計算／推理：** $SST=680/0.8=850$，$SSE=170$，$MSR=170$，$MSE=4.25$，$F=40.00$；臨界值 2.606，$p\approx1.78\times10^{-13}$。
- **解讀結論：** 整體模型顯著。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 4 | 680 | 170.00 | 40.00 |
| Error | 40 | 170 | 4.25 |  |
| Total | 44 | 850 |  |  |

#### 計算題 23 <a id="exam-ch16-problem-23"></a>

##### 題目

> A regression analysis involving 45 observations and two independent variables resulted in
>
> $$\widehat Y=0.408+1.3387X_1+2X_2,$$
>
> with $SSE_q=49$. When two other independent variables were added,
>
> $$\widehat Y=1.2+3.0X_1+12X_2+4.0X_3+8X_4,$$
>
> with $SSE_p=40$. At 95% confidence, test whether the two added variables contribute significantly.

##### 詳解

> **回看投影片講義：** [一組新增係數用 F](./course2-slides-handout.html#compare-ch16-method-selection)、[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 一次新增 $X_3,X_4$ 的巢套 F。
- **選方法：** 依[一組新增係數用 F](./course2-slides-handout.html#compare-ch16-method-selection)，使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** $n=45,q=2,p=4$；完整模型誤差 df 40。
- **代入計算／推理：** $H_0:\beta_3=\beta_4=0$。$F=((49-40)/2)/(40/40)=4.50$；臨界值 3.232，$p\approx0.0173$。
- **解讀結論：** 拒絕 $H_0$；兩個新增變數合起來有顯著額外貢獻，但不能據此保證兩者個別都顯著。

#### 計算題 24 <a id="exam-ch16-problem-24"></a>

##### 題目

> A computer manufacturer developed a model relating Sales (Y in \$10,000) with Price (dollars), Competitor's Price (dollars), Advertising (\$1000), and Type (0 desktop, 1 laptop).

| Source | df | SS | MS |
|---|---:|---:|---:|
| Regression | 4 | 27,641,631.121 | 6,910,407.780 |
| Residual | 35 | 42,277,876.624 | 1,207,939.332 |

| Term | Coefficient | Standard Error |
|---|---:|---:|
| Intercept | 2,268.233 | 1,237.880 |
| Price | -0.803 | 0.316 |
| Competitor's Price | 0.859 | 0.281 |
| Advertising | 0.216 | 0.079 |
| Type | 567.806 | 373.400 |

> a. What was the sample size?
>
> b. Determine the coefficient of determination.
>
> c. Compute t for each of the four independent variables.
>
> d. Determine their p-values.
> e. At 95% confidence, which variables are significant?
> f. Test whether the model is significant.

##### 詳解

> **回看投影片講義：** [整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)


- **辨認題型：** 完整複迴歸輸出重建、個別 t 與整體 F。
- **選方法：** 依[整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)分開回答；Type 的解讀用[虛擬變數模型](./course2-slides-handout.html#formula-dummy-variable-anova)。
- **檢查假設：** $df_R=4,df_E=35$，所以 $n=4+35+1=40$；個別 t 使用 df 35。
- **代入計算／推理：** $R^2=27{,}641{,}631.121/(27{,}641{,}631.121+42{,}277{,}876.624)=0.39534$。四個 t 依序為 -2.541、3.057、2.734、1.521；雙尾 p 值約 0.0156、0.00426、0.00974、0.1373。整體 $F=6{,}910{,}407.780/1{,}207{,}939.332=5.7208$，$p\approx0.00119$。
- **解讀結論：** 樣本數 40，$R^2\approx39.53\%$。Price、Competitor's Price、Advertising 顯著；Type 不顯著。整體模型顯著，表示至少一個斜率非 0。

#### 計算題 25 <a id="exam-ch16-problem-25"></a>

##### 題目

> Thirty-four observations of Y and two independent variables resulted in $SSE_q=300$. When a third variable was added, $SSE_p=250$. At 95% confidence, determine whether the third variable contributes significantly.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增單一變數的巢套 F。
- **選方法：** 使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** $n=34,q=2,p=3$，完整模型誤差 df 30。
- **代入計算／推理：** $F=(300-250)/(250/30)=6.00$，臨界值 4.171，$p\approx0.0204$。
- **解讀結論：** 拒絕 $H_0$；第三個變數有顯著額外貢獻。

#### 計算題 26 <a id="exam-ch16-problem-26"></a>

##### 題目

> Forty-eight observations of Y and five independent variables resulted in $SSE_q=438$. When two additional variables were added, $SSE_p=375$. At 95% confidence, determine whether the two variables contribute significantly.

##### 詳解

> **回看投影片講義：** [巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)


- **辨認題型：** 新增兩個變數的巢套 F。
- **選方法：** 使用[巢套模型 F](./course2-slides-handout.html#formula-nested-model-f)。
- **檢查假設：** $n=48,q=5,p=7$，完整模型誤差 df 40。
- **代入計算／推理：** $F=((438-375)/2)/(375/40)=3.36$，臨界值 3.232，$p\approx0.0448$。
- **解讀結論：** 在 5% 水準剛好拒絕 $H_0$；兩個新增變數合起來有顯著貢獻。因 p 值接近 0.05，換樣本可能不穩定。

#### 計算題 27 <a id="exam-ch16-problem-27"></a>

##### 題目

> A regression analysis with 4 independent variables obtained $R^2=0.60$, $SSR=4800$, and $n=35$.
> a. Fill in the ANOVA table.
>
> b. At $\alpha=.05$, test whether the model is significant.

##### 詳解

> **回看投影片講義：** [多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)、[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)


- **辨認題型：** ANOVA 回填與整體 F。
- **選方法：** 使用[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)及[整體 F](./course2-slides-handout.html#formula-multiple-regression-f-test)。
- **檢查假設：** $n=35,k=4$，df 為 4、30、34。
- **代入計算／推理：** $SST=4800/0.60=8000$，$SSE=3200$；$MSR=1200$，$MSE=106.667$，$F=11.25$，臨界值 2.690，$p\approx1.07\times10^{-5}$。
- **解讀結論：** 整體模型顯著。

| Source | DF | SS | MS | F |
|---|---:|---:|---:|---:|
| Regression | 4 | 4,800 | 1,200.000 | 11.25 |
| Error | 30 | 3,200 | 106.667 |  |
| Total | 34 | 8,000 |  |  |

#### 計算題 28 <a id="exam-ch16-problem-28"></a>

##### 題目

> A regression analysis relating a company's sales, advertising expenditure, price, and time resulted in the following.

| Regression Statistics | Value |
|---|---:|
| Multiple R | 0.8800 |
| R Square | 0.7744 |
| Adjusted R Square | 0.7560 |
| Standard Error | 232.29 |
| Observations | 25 |

| Source | df | SS | MS | F | Significance F |
|---|---:|---:|---:|---:|---:|
| Regression | 3 | 53,184,931.86 | 17,728,310.62 | 328.56 | 0.0000 |
| Residual | 21 | 1,133,108.30 | 53,957.54 |  |  |
| Total | 24 | 54,318,040.16 |  |  |  |

| Term | Coefficient | Standard Error | t Stat | P-value |
|---|---:|---:|---:|---:|
| Intercept | 927.23 | 1,229.86 | 0.75 | 0.4593 |
| Advertising ($X_1$) | 1.02 | 3.09 | 0.33 | 0.7450 |
| Price ($X_2$) | 15.61 | 5.62 | 2.78 | 0.0112 |
| Time ($X_3$) | 170.53 | 28.18 | 6.05 | 0.0000 |

> a. At 95% confidence, determine whether the regression model is significant and explain what it means.
>
> b. Determine which variables are significant.
>
> c. Fully explain the meaning of R-square with numerical detail.

##### 詳解

> **回看投影片講義：** [整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)、[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)


- **辨認題型：** 整體 F、個別 t、$R^2$ 解讀。
- **選方法：** 用[整體 F vs 個別 t](./course2-slides-handout.html#compare-ch16-method-selection)，並以[多元 $R^2$](./course2-slides-handout.html#formula-multiple-r-squared)解讀比例。
- **檢查假設：** 結論建立在迴歸誤差條件合理上；Time 表示趨勢，若資料有時間順序還應檢查[Durbin-Watson](./course2-slides-handout.html#formula-durbin-watson)。
- **代入計算／推理：** 整體 $F=328.56$、p 值小於顯示精度，故整體顯著。Advertising p=0.7450 不顯著；Price p=0.0112、Time p<0.0001 顯著。原題 Regression Statistics 報告 $R^2=0.7744$，但 ANOVA 平方和重算為 $53{,}184{,}931.86/54{,}318{,}040.16=0.979139$；兩者不能同時成立。$F=328.56$ 與標準誤 232.29 都和 ANOVA 的 $0.979139$ 相容，顯示來源很可能混入不同模型的摘要數字。
- **解讀結論：** 至少一個斜率非 0；控制其他變數後 Price 與 Time 有額外訊號，Advertising 沒有。若依題目明列的 R-square 作答，應解讀為解釋 77.44%、未解釋 22.56%；若依同頁 ANOVA 平方和重建，則是解釋 97.91%。考試時先依題目指定欄位回答並註明內部不一致，不能把兩個數字寫成同一個等式。無論採哪個數字，$R^2$ 都不是預測正確率或因果比例。

#### 計算題 29 <a id="exam-ch16-problem-29"></a>

##### 題目

> Ziba, Inc. provided partial sales data for January through December 2009.

| Year 2009 | Sales Y (\$100,000) | Advertising $X_1$ (\$10,000) | Time $X_2$ |
|---|---:|---:|---:|
| January | … | … | 1 |
| February | … | … | 2 |
| … | … | … | … |
| November | 36 | 26 | 11 |
| December | 37 | 28 | 12 |

| Term | Coefficient | Standard Error | t Stat | P-value |
|---|---:|---:|---:|---:|
| Intercept | 13.01 | 0.6334 | 20.5379 | 0.0000 |
| Advertising ($X_1$ in \$10,000) | 0.31 | 0.1293 | 2.3784 | 0.0413 |
| Time ($X_2$) | 1.39 | 0.2863 | 4.8390 | 0.0009 |

> a. The company plans to increase advertising by 5% per month for January and February 2010. What would advertising be in dollars?
>
> b. Use the model to forecast sales for January and February 2010, showing computations in dollars.

##### 詳解

> **回看投影片講義：** [複迴歸點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)


- **辨認題型：** 連續成長的單位換算與含時間趨勢的點預測。
- **選方法：** 使用[複迴歸點預測](./course2-slides-handout.html#formula-multiple-regression-point-estimate)；因資料按月，預測可靠性還應留意[自相關檢查](./course2-slides-handout.html#formula-durbin-watson)。
- **檢查假設：** December advertising 是 28 個 \$10,000。January 的 Time=13，February=14；第二個月的 5% 是在 January 水準上再乘 1.05。
- **代入計算／推理：** January advertising $=28(1.05)=29.4$ 單位，即 \$294,000；February $=29.4(1.05)=30.87$ 單位，即 \$308,700。模型為 $\widehat Y=13.01+0.31X_1+1.39X_2$。January：$13.01+0.31(29.4)+1.39(13)=40.194$ 個 \$100,000；February：$13.01+0.31(30.87)+1.39(14)=42.0397$ 個 \$100,000。
- **解讀結論：** January 預測銷售 **\$4,019,400** ；February **\$4,203,970** 。這是外推到樣本後兩個月，若殘差有自相關或趨勢改變，不確定性會比單一點數顯示的更大。

<div class="page-break" style="page-break-after: always;"></div>

# 第 17 章：時間數列與預測｜考古題詳解

## 考古題詳解

本章收錄 68 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–37 題

#### 選擇題 1 <a id="exam-ch17-mc-1"></a>

##### 題目

> Which of the following is not present in a time series?
>
> a. seasonality<br>
> b. operational variations<br>
> c. trend<br>
> d. cycles

##### 詳解

> **回看投影片講義：** [時間數列型態](./course2-slides-handout.html#section-ch17-patterns)


1. **辨認題型：** 時間數列組成辨識。
2. **選方法：** 依[時間數列型態](./course2-slides-handout.html#section-ch17-patterns)分辨標準成分。
3. **檢查假設：** 問的是課本標準術語，不需數值假設。
4. **代入計算／推理：** trend、seasonality、cycles 都是標準成分；operational variations 不是。
5. **解讀結論：** 答案是 **b** 。a 是固定週期，c 是長期方向，d 是多年循環；b 只是一般文字，不是本章成分名稱。

#### 選擇題 2 <a id="exam-ch17-mc-2"></a>

##### 題目

> Given an actual demand of 61, forecast of 58, and an $\alpha$ of .3, what would the forecast for the next period be using simple exponential smoothing?
>
> a. 57.1<br>
> b. 58.9<br>
> c. 61.0<br>
> d. 65.5

##### 詳解

> **回看投影片講義：** [指數平滑公式](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 單一指數平滑更新。
2. **選方法：** 使用[指數平滑公式](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $0\le0.3\le1$，且 61 是本期實際值、58 是本期預測。
4. **代入計算／推理：** $F_{t+1}=0.3(61)+0.7(58)=58.9$。
5. **解讀結論：** 答案是 **b** 。a 把修正方向弄反；c 等同只看實際值；d 超出兩個輸入的加權平均範圍。

#### 選擇題 3 <a id="exam-ch17-mc-3"></a>

##### 題目

> Which of the following smoothing constants would make an exponential smoothing forecast equivalent to a naive forecast?
>
> a. 0<br>
> b. 1 divided by the number of periods<br>
> c. 0.5<br>
> d. 1.0

##### 詳解

> **回看投影片講義：** [樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)、[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數平滑與樸素法的邊界關係。
2. **選方法：** 比較[樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)與[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 樸素法要令下一期等於最新實際值。
4. **代入計算／推理：** $\alpha=1$ 時，$F_{t+1}=Y_t$。
5. **解讀結論：** 答案是 **d** 。a 完全不更新；b 不是必要關係；c 仍混合舊預測。

#### 選擇題 4 <a id="exam-ch17-mc-4"></a>

##### 題目

> The time series component which reflects a regular, multi-year pattern of being above and below the trend line is
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

> **回看投影片講義：** [季節與循環比較](./course2-slides-handout.html#section-ch17-seasonal-cyclical)


1. **辨認題型：** 多年上下波動的名稱。
2. **選方法：** 依[季節與循環比較](./course2-slides-handout.html#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 關鍵字是 multi-year 且圍繞趨勢線。
4. **代入計算／推理：** 這是 cyclical component。
5. **解讀結論：** 答案是 **c** 。a 是長期方向；b 通常是一年內固定週期；d 是無規律突發。

#### 選擇題 5 <a id="exam-ch17-mc-5"></a>

##### 題目

> The time series component that reflects variability during a single year is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

> **回看投影片講義：** [季節型定義](./course2-slides-handout.html#section-ch17-seasonal-cyclical)


1. **辨認題型：** 一年內固定節奏。
2. **選方法：** 使用[季節型定義](./course2-slides-handout.html#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 題意是可重複的一年內變動。
4. **代入計算／推理：** 對應 seasonal component。
5. **解讀結論：** 答案是 **b** 。a 不要求一年重複；c 跨多年；d 無固定節奏。

#### 選擇題 6 <a id="exam-ch17-mc-6"></a>

##### 題目

> The time series component that reflects variability due to natural disasters is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

> **回看投影片講義：** [不規則成分](./course2-slides-handout.html#section-ch17-seasonal-cyclical)


1. **辨認題型：** 突發事件成分。
2. **選方法：** 對照[不規則成分](./course2-slides-handout.html#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 天災不是固定週期，也不是可延伸趨勢。
4. **代入計算／推理：** 應歸為 irregular。
5. **解讀結論：** 答案是 **d** 。a、b、c 都暗示某種可辨認規律，與突發天災不符。

#### 選擇題 7 <a id="exam-ch17-mc-7"></a>

##### 題目

> The time series component that reflects gradual variability over a long time period is called
>
> a. a trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

> **回看投影片講義：** [趨勢型](./course2-slides-handout.html#section-ch17-trend-patterns)


1. **辨認題型：** 長期逐步移動。
2. **選方法：** 對照[趨勢型](./course2-slides-handout.html#section-ch17-trend-patterns)。
3. **檢查假設：** 關鍵是 gradual 與 long time period，不是上下循環。
4. **代入計算／推理：** 對應 trend。
5. **解讀結論：** 答案是 **a** 。b 是固定短週期；c 是多年在趨勢上下交替；d 無規則。

#### 選擇題 8 <a id="exam-ch17-mc-8"></a>

##### 題目

> The trend component is easy to identify by using
>
> a. moving averages<br>
> b. exponential smoothing<br>
> c. regression analysis<br>
> d. the Delphi approach

##### 詳解

> **回看投影片講義：** [線性趨勢迴歸](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 趨勢估計工具。
2. **選方法：** 使用[線性趨勢迴歸](./course2-slides-handout.html#formula-ch17-linear-trend)。
3. **檢查假設：** 題目問明確估計趨勢線，不只是平滑短期波動。
4. **代入計算／推理：** 把 $t$ 當自變數的 regression 可估斜率。
5. **解讀結論：** 答案是 **c** 。a、b 未修正時主要處理水平型；d 是定性預測。

#### 選擇題 9 <a id="exam-ch17-mc-9"></a>

##### 題目

> The forecasting method that is appropriate when the time series has no significant trend, cyclical, or seasonal effect is
>
> a. moving averages<br>
> b. mean squared error<br>
> c. mean average deviation<br>
> d. qualitative forecasting methods

##### 詳解

> **回看投影片講義：** [本章方法選擇流程](./course2-slides-handout.html#compare-ch17-forecast-methods)


1. **辨認題型：** 水平型數列選方法。
2. **選方法：** 依[本章方法選擇流程](./course2-slides-handout.html#compare-ch17-forecast-methods)。
3. **檢查假設：** 已明示無趨勢、循環與季節。
4. **代入計算／推理：** moving averages 是水平型平滑法；MSE、MAD 是誤差指標。
5. **解讀結論：** 答案是 **a** 。b、c 不會產生預測；d 通常用於歷史資料不可用。

#### 選擇題 10 <a id="exam-ch17-mc-10"></a>

##### 題目

> If data for a time series analysis is collected on an annual basis only, which component may be ignored?
>
> a. trend<br>
> b. seasonal<br>
> c. cyclical<br>
> d. irregular

##### 詳解

> **回看投影片講義：** [季節型定義](./course2-slides-handout.html#section-ch17-seasonal-cyclical)


1. **辨認題型：** 取樣頻率與季節成分。
2. **選方法：** 依[季節型定義](./course2-slides-handout.html#section-ch17-seasonal-cyclical)。
3. **檢查假設：** 每年只有一筆，沒有一年內月份或季度位置。
4. **代入計算／推理：** 一年內季節差已無法在年度資料中分辨。
5. **解讀結論：** 答案是 **b** 。年度資料仍可能有趨勢、跨年循環與不規則波動。

#### 選擇題 11 <a id="exam-ch17-mc-11"></a>

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

> **回看投影片講義：** [MSE](./course2-slides-handout.html#formula-ch17-mse)


1. **辨認題型：** 已知預測的 MSE。
2. **選方法：** 使用[MSE](./course2-slides-handout.html#formula-ch17-mse)。
3. **檢查假設：** 只有第 4 至 7 期共 4 個誤差。
4. **代入計算／推理：** 平方誤差為 $7^2+(-9)^2+5^2+(-3)^2=164$，故 $MSE=164/4=41$。
5. **解讀結論：** 答案是 **c** 。d 是平方誤差總和，漏除 4；a、b 都不是依表計算的結果。

#### 選擇題 12 <a id="exam-ch17-mc-12"></a>

##### 題目

> If the estimate of the trend component is 158.2, the estimate of the seasonal component is 94%, the estimate of the cyclical component is 105%, and the estimate of the irregular component is 98%, then the multiplicative model will produce a forecast of
>
> a. 1.53<br>
> b. 1.53%<br>
> c. 153.02<br>
> d. 153,020,532

##### 詳解

> **回看投影片講義：** [乘法分解](./course2-slides-handout.html#formula-ch17-multiplicative-decomposition)


1. **辨認題型：** 乘法分解合成。
2. **選方法：** 使用[乘法分解](./course2-slides-handout.html#formula-ch17-multiplicative-decomposition)。
3. **檢查假設：** 百分比要換成倍率 0.94、1.05、0.98。
4. **代入計算／推理：** $158.2(0.94)(1.05)(0.98)=153.020532$。
5. **解讀結論：** 答案是 **c** 。a、b 把尺度弄錯；d 未正確把百分比換倍率。

#### 選擇題 13 <a id="exam-ch17-mc-13"></a>

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

> **回看投影片講義：** [移動平均](./course2-slides-handout.html#formula-ch17-moving-average)


1. **辨認題型：** 四期移動平均預測。
2. **選方法：** 使用[移動平均](./course2-slides-handout.html#formula-ch17-moving-average)。
3. **檢查假設：** 第 5 期只使用前四期。
4. **代入計算／推理：** $F_5=(18+20+25+17)/4=20$。
5. **解讀結論：** 答案是 **c** 。b 只抄最近值；a、d 都不是四期平均。

#### 選擇題 14 <a id="exam-ch17-mc-14"></a>

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

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數平滑下一期。
2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 更新時用 $Y_2=22,F_2=18$。
4. **代入計算／推理：** $F_3=0.3(22)+0.7(18)=19.2$。
5. **解讀結論：** 答案是 **b** 。a 未更新；c 是未加權平均；d 是相加未加權。

#### 選擇題 15 <a id="exam-ch17-mc-15"></a>

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

> **回看投影片講義：** [線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 線性趨勢代入。
2. **選方法：** 使用[線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)。
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

#### 選擇題 16 <a id="exam-ch17-mc-16"></a>

##### 題目

> Refer to Exhibit 18-1. An estimate of the trend component times the cyclical component $(T_tC_t)$ for Quarter 3 of Year 1, when a four-quarter moving average is used, is
>
> a. 24<br>
> b. 25<br>
> c. 26<br>
> d. 28

##### 詳解

> **回看投影片講義：** [中央移動平均](./course2-slides-handout.html#formula-ch17-centered-moving-average)


1. **辨認題型：** 偶數週期中央移動平均。
2. **選方法：** 使用[中央移動平均](./course2-slides-handout.html#formula-ch17-centered-moving-average)。
3. **檢查假設：** 兩個四期平均分別中心在 2.5 與 3.5，再平均才對準第 3 期。
4. **代入計算／推理：** $MA_1=(36+24+16+20)/4=24$，$MA_2=(24+16+20+44)/4=26$，$CMA_3=(24+26)/2=25$。
5. **解讀結論：** 答案是 **b** 。a、c 是未置中的四期平均；d 無此計算來源。

#### 選擇題 17 <a id="exam-ch17-mc-17"></a>

##### 題目

> Refer to Exhibit 18-1. An estimate of the seasonal-irregular component for Quarter 3 of Year 1 is
>
> a. .64<br>
> b. 1.5625<br>
> c. 5.333<br>
> d. 30

##### 詳解

> **回看投影片講義：** [$Y_t/CMA_t$](./course2-slides-handout.html#formula-ch17-seasonal-irregular)


1. **辨認題型：** 季節不規則比。
2. **選方法：** 使用[$Y_t/CMA_t$](./course2-slides-handout.html#formula-ch17-seasonal-irregular)。
3. **檢查假設：** 第 3 期實際值 16，趨勢循環估計 25。
4. **代入計算／推理：** $16/25=0.64$。
5. **解讀結論：** 答案是 **a** 。b 是倒數；c、d 不是比例。0.64 表示該期比趨勢低約 36%。

#### 選擇題 18 <a id="exam-ch17-mc-18"></a>

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

> **回看投影片講義：** [季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)


1. **辨認題型：** 同季跨年平均。
2. **選方法：** 使用[季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)。
3. **檢查假設：** 只平均 Quarter 1 的三個比值。
4. **代入計算／推理：** $(1.23+1.15+1.16)/3=1.18$。
5. **解讀結論：** 答案是 **b** 。a 接近全部比值總平均；c、d 把季數或筆數當指數。1.18 表示第一季通常高於趨勢約 18%。

#### 選擇題 19 <a id="exam-ch17-mc-19"></a>

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

> **回看投影片講義：** [本章方法流程](./course2-slides-handout.html#compare-ch17-method-selection)


1. **辨認題型：** 兩期落後值自我迴歸代入。
2. **選方法：** 依方程式直接使用第 26、25 期，並以[本章方法流程](./course2-slides-handout.html#compare-ch17-method-selection)確認不是趨勢式。
3. **檢查假設：** $Y_{t-1}=114,Y_{t-2}=112$。
4. **代入計算／推理：** $16.23+0.52(114)+0.37(112)=116.95$。
5. **解讀結論：** 答案是 **d** 。a、b 漏項或索引錯；c 是算術誤差。

#### 選擇題 20 <a id="exam-ch17-mc-20"></a>

##### 題目

> A group of observations measured at successive time intervals is known as
>
> a. a trend component<br>
> b. a time series<br>
> c. a forecast<br>
> d. an additive time series model

##### 詳解

> **回看投影片講義：** [時間數列資料結構](./course2-slides-handout.html#section-ch17-data-structure)


1. **辨認題型：** 基本定義。
2. **選方法：** 使用[時間數列資料結構](./course2-slides-handout.html#section-ch17-data-structure)。
3. **檢查假設：** successive time intervals 是關鍵。
4. **代入計算／推理：** 按連續時間間隔量得的一組觀察即 time series。
5. **解讀結論：** 答案是 **b** 。a 只是成分；c 是未來估計；d 是一種分解模型。

#### 選擇題 21 <a id="exam-ch17-mc-21"></a>

##### 題目

> A component of the time series model that results in the multi-period above-trend and below-trend behavior of a time series is
>
> a. a trend component<br>
> b. a cyclical component<br>
> c. a seasonal component<br>
> d. an irregular component

##### 詳解

> **回看投影片講義：** [循環型](./course2-slides-handout.html#section-ch17-seasonal-cyclical)


1. **辨認題型：** 趨勢線上下的多期段落。
2. **選方法：** 對照[循環型](./course2-slides-handout.html#section-ch17-seasonal-cyclical)。
3. **檢查假設：** multi-period 指超過短季節的上下段落。
4. **代入計算／推理：** 對應 cyclical component。
5. **解讀結論：** 答案是 **b** 。a 是基準方向；c 固定短週期；d 沒有可重複結構。

#### 選擇題 22 <a id="exam-ch17-mc-22"></a>

##### 題目

> The model that assumes that the actual time series value is the product of its components is the
>
> a. forecast time series model<br>
> b. multiplicative time series model<br>
> c. additive time series model<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [乘法分解](./course2-slides-handout.html#formula-ch17-multiplicative-decomposition)


1. **辨認題型：** 分解模型形式。
2. **選方法：** 使用[乘法分解](./course2-slides-handout.html#formula-ch17-multiplicative-decomposition)。
3. **檢查假設：** product 表示相乘，不是相加。
4. **代入計算／推理：** $Y_t=T_tS_tI_t$ 是 multiplicative model。
5. **解讀結論：** 答案是 **b** 。a 不是標準名稱；c 用加法；d 因 b 正確而錯。

#### 選擇題 23 <a id="exam-ch17-mc-23"></a>

##### 題目

> A method of smoothing a time series that can be used to identify the combined trend/cyclical component is
>
> a. the moving average<br>
> b. the percent of trend<br>
> c. exponential smoothing<br>
> d. the trend/cyclical index

##### 詳解

> **回看投影片講義：** [中央移動平均](./course2-slides-handout.html#formula-ch17-centered-moving-average)


1. **辨認題型：** 分解法中提取慢速成分。
2. **選方法：** 使用[中央移動平均](./course2-slides-handout.html#formula-ch17-centered-moving-average)。
3. **檢查假設：** 週期長度已知，移動平均用來壓低季節與不規則波動。
4. **代入計算／推理：** moving average 估計趨勢循環。
5. **解讀結論：** 答案是 **a** 。b 是比例概念；c 是水平型預測法；d 不是此處計算方法。

#### 選擇題 24 <a id="exam-ch17-mc-24"></a>

##### 題目

> A method that uses a weighted average of past values for arriving at smoothed time series values is known as
>
> a. a smoothing average<br>
> b. a moving average<br>
> c. an exponential average<br>
> d. an exponential smoothing

##### 詳解

> **回看投影片講義：** [單一指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數衰減權重的名稱。
2. **選方法：** 使用[單一指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 題意強調過去值的加權平均，不是等權平均。
4. **代入計算／推理：** 標準名稱是 exponential smoothing。
5. **解讀結論：** 答案是 **d** 。b 通常等權；a、c 不是標準術語。

#### 選擇題 25 <a id="exam-ch17-mc-25"></a>

##### 題目

> In the linear trend equation, $T=b_0+b_1t$, $b_1$ represents the
>
> a. trend value in period t<br>
> b. intercept of the trend line<br>
> c. slope of the trend line<br>
> d. point in time

##### 詳解

> **回看投影片講義：** [線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 線性趨勢符號。
2. **選方法：** 使用[線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)。
3. **檢查假設：** 問的是 $b_1$。
4. **代入計算／推理：** $b_1$ 是時間每增一期，趨勢平均改變量。
5. **解讀結論：** 答案是 **c** 。a 是 $T_t$；b 是 $b_0$；d 是 $t$。

#### 選擇題 26 <a id="exam-ch17-mc-26"></a>

##### 題目

> In the linear trend equation, $T=b_0+b_1t$, $b_0$ represents the
>
> a. time<br>
> b. slope of the trend line<br>
> c. trend value in period 1<br>
> d. the Y intercept

##### 詳解

> **回看投影片講義：** [線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 線性趨勢截距。
2. **選方法：** 使用[線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)。
3. **檢查假設：** 截距是 $t=0$，不是第 1 期。
4. **代入計算／推理：** $b_0$ 為 Y intercept。
5. **解讀結論：** 答案是 **d** 。a 是 $t$；b 是 $b_1$；c 應為 $b_0+b_1$。

#### 選擇題 27 <a id="exam-ch17-mc-27"></a>

##### 題目

> A parameter of the exponential smoothing model which provides the weight given to the most recent time series value in the calculation of the forecast value is known as the
>
> a. mean square error<br>
> b. mean absolute deviation<br>
> c. smoothing constant<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數平滑參數名稱。
2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 最近實際值的權重為 $\alpha$。
4. **代入計算／推理：** $\alpha$ 稱 smoothing constant。
5. **解讀結論：** 答案是 **c** 。a、b 是誤差指標；d 因 c 正確而錯。

#### 選擇題 28 <a id="exam-ch17-mc-28"></a>

##### 題目

> One measure of the accuracy of a forecasting model is
>
> a. the smoothing constant<br>
> b. a deseasonalized time series<br>
> c. the mean square error<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [MSE](./course2-slides-handout.html#formula-ch17-mse)


1. **辨認題型：** 預測準確度指標。
2. **選方法：** 使用[MSE](./course2-slides-handout.html#formula-ch17-mse)。
3. **檢查假設：** 問的是 accuracy measure。
4. **代入計算／推理：** mean square error 直接彙總預測誤差。
5. **解讀結論：** 答案是 **c** 。a 是模型設定；b 是調整後資料；d 不成立。

#### 選擇題 29 <a id="exam-ch17-mc-29"></a>

##### 題目

> A qualitative forecasting method that obtains forecasts through "group consensus" is known as the
>
> a. Autoregressive model<br>
> b. Delphi approach<br>
> c. mean absolute deviation<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [預測方法分類](./course2-slides-handout.html#section-ch17-data-structure)


1. **辨認題型：** 定性預測術語。
2. **選方法：** 依[預測方法分類](./course2-slides-handout.html#section-ch17-data-structure)。
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

以[線性趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)獨立重算得 $\bar t=2.5$、$\bar Y=7.5$、$b_1=2$、$b_0=2.5$，所以 $T_t=2.5+2t$。

#### 選擇題 30 <a id="exam-ch17-mc-30"></a>

##### 題目

> Refer to Exhibit 18-2. The slope of linear trend equation, $b_1$, is
>
> a. 2.5<br>
> b. 2.0<br>
> c. 1.0<br>
> d. 1.25

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 線性趨勢斜率。
2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 四期等距。
4. **代入計算／推理：** 交叉離差和 10，時間平方離差和 5，故 $b_1=2$。
5. **解讀結論：** 答案是 **b** 。a 是截距；c、d 都不符合最小平方計算。

#### 選擇題 31 <a id="exam-ch17-mc-31"></a>

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

#### 選擇題 32 <a id="exam-ch17-mc-32"></a>

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

#### 選擇題 33 <a id="exam-ch17-mc-33"></a>

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

#### 選擇題 34 <a id="exam-ch17-mc-34"></a>

##### 題目

> Refer to Exhibit 18-3. The slope of linear trend equation, $b_1$, is
>
> a. -1.5<br>
> b. +1.5<br>
> c. 8.3<br>
> d. -8.3

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 下降趨勢斜率。
2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 數列隨時間下降，斜率應為負。
4. **代入計算／推理：** 交叉離差和 $-15$，時間平方離差和 10，故 $b_1=-1.5$。
5. **解讀結論：** 答案是 **a** 。b 方向錯；c 是截距；d 把截距符號誤植。

#### 選擇題 35 <a id="exam-ch17-mc-35"></a>

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

#### 選擇題 36 <a id="exam-ch17-mc-36"></a>

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

#### 選擇題 37 <a id="exam-ch17-mc-37"></a>

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

#### 計算題 1 <a id="exam-ch17-problem-1"></a>

##### 題目

> Consider the time series $(t,Y_t)$: $(1,18),(2,20),(3,22),(4,24),(5,26),(6,28)$.<br>
> a. Develop a linear trend equation.<br>
> b. What is the forecast for $t=17$?

##### 詳解

> **回看投影片講義：** [線性趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 完全線性的趨勢投影。
2. **選方法：** 使用[線性趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 每期等距；外推到 17 很遠，實務風險高。
4. **代入計算／推理：** 每期固定增加 2，$b_1=2,b_0=16$，故 $T_t=16+2t$；$T_{17}=50$。
5. **解讀結論：** 預測為 50；它延續固定增量，不是保證第 17 期一定等於 50。

#### 計算題 2 <a id="exam-ch17-problem-2"></a>

##### 題目

> Demand from January through June is 40, 45, 57, 60, 75, 87. Use a three-month weighted moving average with weights 5, 3, and 2, largest for the most recent data. Show forecasts for April through July.

##### 詳解

> **回看投影片講義：** [加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)


1. **辨認題型：** 三期加權移動平均。
2. **選方法：** 使用[加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 10，要正規化。
4. **代入計算／推理：** $F_{Apr}=50.0$、$F_{May}=56.1$、$F_{Jun}=66.9$、$F_{Jul}=78.0$。
5. **解讀結論：** July 預測 78；近期需求權重最大，所以預測會比等權平均更靠近 87。

#### 計算題 3 <a id="exam-ch17-problem-3"></a>

##### 題目

> Use the same January–June demands 40, 45, 57, 60, 75, 87 and weights 6, 4, and 2, largest for the most recent data. Show forecasts for April through July.

##### 詳解

> **回看投影片講義：** [加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)


1. **辨認題型：** 改權重的三期加權平均。
2. **選方法：** 使用[加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 12。
4. **代入計算／推理：** 預測依序為 50.167、56.5、67.0、78.5。
5. **解讀結論：** July 預測 78.5；比題 2 更重視近期，所以在上升資料中稍高。

#### 計算題 4 <a id="exam-ch17-problem-4"></a>

##### 題目

> Demand from January through June is 80, 83, 87, 90, 95, 98. Use weights 5, 4, and 3, largest for the most recent data. Show forecasts for April through July.

##### 詳解

> **回看投影片講義：** [加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)


1. **辨認題型：** 加權移動平均。
2. **選方法：** 使用[加權移動平均](./course2-slides-handout.html#formula-ch17-weighted-moving-average)。
3. **檢查假設：** 權重總和 12。
4. **代入計算／推理：** $F_{Apr}=83.917$、$F_{May}=87.25$、$F_{Jun}=91.333$、$F_{Jul}=95.0$。
5. **解讀結論：** July 預測 95；上升趨勢下平滑預測會落後最新值 98。

#### 計算題 5 <a id="exam-ch17-problem-5"></a>

##### 題目

> Actual sales for January through April are 18, 23, 20, 16. Use exponential smoothing with $\alpha=0.2$ and initial January forecast 18 to forecast May. Show all computations.

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 遞迴指數平滑。
2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $F_{Jan}=18$。
4. **代入計算／推理：** $F_{Feb}=18$、$F_{Mar}=19$、$F_{Apr}=19.2$、$F_{May}=18.56$。
5. **解讀結論：** May 預測 18.56；小 $\alpha$ 只修正最近下降的一小部分。

#### 計算題 6 <a id="exam-ch17-problem-6"></a>

##### 題目

> Actual sales for January through April are 18, 25, 30, 40. Use $\alpha=0.3$ and initial January forecast 18 to forecast May.

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數平滑。
2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** 水準持續上升，單一平滑可能落後。
4. **代入計算／推理：** $F_{Feb}=18$、$F_{Mar}=20.1$、$F_{Apr}=23.07$、$F_{May}=28.149$。
5. **解讀結論：** May 預測 28.149，明顯低於最新 40，顯示水平型方法追不上趨勢。

#### 計算題 7 <a id="exam-ch17-problem-7"></a>

##### 題目

> Sales in millions for January–April are 18, 25, 30, 40.<br>
> a. Use $\alpha=.3$, compute MSE and forecast May.<br>
> b. Repeat with $\alpha=.1$.<br>
> c. Which $\alpha$ is better by MSE?

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)、[MSE](./course2-slides-handout.html#formula-ch17-mse)


1. **辨認題型：** 比較平滑常數。
2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)與[MSE](./course2-slides-handout.html#formula-ch17-mse)。
3. **檢查假設：** MSE 比較共同有實際值的 February–April 三期。
4. **代入計算／推理：** $\alpha=.3$ 的預測為 18、20.1、23.07、28.149，$MSE=144.545$；$\alpha=.1$ 為 18、18.7、19.83、21.847，$MSE=194.506$。
5. **解讀結論：** 歷史 MSE 支持 $\alpha=.3$；上升資料需要較快更新，但兩者都未建模趨勢。

#### 計算題 8 <a id="exam-ch17-problem-8"></a>

##### 題目

> Actual demand for observations 1–6 is 35, 30, 26, 34, 28, 38; forecasts for 2–6 are 35, 30, 26, 34, 28. Calculate MAE and MSE.

##### 詳解

> **回看投影片講義：** [MAE](./course2-slides-handout.html#formula-ch17-mae)、[MSE](./course2-slides-handout.html#formula-ch17-mse)


1. **辨認題型：** 誤差指標。
2. **選方法：** 使用[MAE](./course2-slides-handout.html#formula-ch17-mae)與[MSE](./course2-slides-handout.html#formula-ch17-mse)。
3. **檢查假設：** 只有 5 個預測誤差。
4. **代入計算／推理：** 誤差 $-5,-4,8,-6,10$；$MAE=33/5=6.6$，$MSE=241/5=48.2$。
5. **解讀結論：** 一般一期約錯 6.6 單位；MSE 因 8、10 的大錯被放大。

#### 計算題 9 <a id="exam-ch17-problem-9"></a>

##### 題目

> Naive forecasts accompany actual demands 45, 48, 42, 44, 50, 60 for periods 1–6. Compute MAE and MSE.

##### 詳解

> **回看投影片講義：** [樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)


1. **辨認題型：** 樸素法回測。
2. **選方法：** 使用[樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)、MAE 與 MSE。
3. **檢查假設：** 第 2–6 期預測為 45、48、42、44、50。
4. **代入計算／推理：** 誤差 $3,-6,2,6,10$；$MAE=27/5=5.4$，$MSE=185/5=37$。
5. **解讀結論：** 樸素法一般錯 5.4，且最後一期的大錯對 MSE 影響最大。

#### 計算題 10 <a id="exam-ch17-problem-10"></a>

##### 題目

> Monthly values are 12, 14, 10, 16, 29, 22. Using the naive method, compute MAE, MSE, and the forecast for period 7.

##### 詳解

> **回看投影片講義：** [樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)


1. **辨認題型：** 樸素預測與準確度。
2. **選方法：** 使用[樸素法](./course2-slides-handout.html#formula-ch17-naive-forecast)。
3. **檢查假設：** 第 2–6 期誤差共 5 個。
4. **代入計算／推理：** 誤差 $2,-4,6,13,-7$；$MAE=6.4$，$MSE=54.8$，$F_7=22$。
5. **解讀結論：** 第 5 期跳升造成最大平方懲罰；下一期直接沿用 22。

#### 計算題 11 <a id="exam-ch17-problem-11"></a>

##### 題目

> Quarterly sales (millions) for 2007–2009 are Q1: 170,180,190; Q2: 111,96,120; Q3: 270,280,290; Q4: 250,220,223.<br>
> a. Compute four seasonal indexes.<br>
> b. Given $Trend=174+4t$, forecast Q1 2010.

##### 詳解

> **回看投影片講義：** [每季平均／總平均](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)


1. **辨認題型：** 簡化季節指數加趨勢。
2. **選方法：** 使用[每季平均／總平均](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)，再乘趨勢。
3. **檢查假設：** 題目未要求 CMA；總平均 200。
4. **代入計算／推理：** 季平均 180、109、280、231，指數 0.900、0.545、1.400、1.155；$T_{13}=226$，Q1 預測 $226(0.9)=203.4$。
5. **解讀結論：** Q1 通常低於總體水準 10%，故季調後預測 203.4 百萬。

#### 計算題 12 <a id="exam-ch17-problem-12"></a>

##### 題目

> Quarterly sales for 2007–2009 are Q1: 106,135,149; Q2: 256,280,292; Q3: 273,280,290; Q4: 190,180,209. Given $Trend=185.86+5.25t$, compute seasonal indexes, Q1 2010 trend-only forecast, and trend-plus-season forecast.

##### 詳解

> **回看投影片講義：** [簡化季節指數](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)


1. **辨認題型：** 簡化季節指數。
2. **選方法：** 使用[簡化季節指數](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)。
3. **檢查假設：** 總平均 220，Q1 2010 是 $t=13$。
4. **代入計算／推理：** 指數為 0.5909、1.2545、1.2773、0.8773；$T_{13}=254.11$；Q1 完整預測 $254.11(0.5909)=150.155$。
5. **解讀結論：** 趨勢基準 254.11，但 Q1 通常僅約 59.1% 基準，所以調整後約 150.16。

#### 計算題 13 <a id="exam-ch17-problem-13"></a>

##### 題目

> Quarterly sales for 2007–2009 are Q1: 14,28,30; Q2: 20,16,18; Q3: 36,40,38; Q4: 10,14,12. Given $Trend=20.82+.336t$, compute seasonal indexes, Q1 2010 trend-only forecast, and adjusted forecast.

##### 詳解

> **回看投影片講義：** [簡化季節指數](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)


1. **辨認題型：** 簡化季節指數。
2. **選方法：** 使用[簡化季節指數](./course2-slides-handout.html#formula-ch17-simple-seasonal-index)。
3. **檢查假設：** 總平均 23，$t=13$。
4. **代入計算／推理：** 指數 1.0435、0.7826、1.6522、0.5217；$T_{13}=25.188$；Q1 預測 $25.188(1.0435)=26.283$。
5. **解讀結論：** Q3 季節性最強，Q4 最弱；Q1 略高於趨勢基準。

#### 計算題 14 <a id="exam-ch17-problem-14"></a>

##### 題目

> Seven yearly sales values are 12, 16, 17, 19, 18, 21, 22 million. Develop a linear trend and forecast period 10.

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 線性趨勢。
2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 年距相同；外推三年。
4. **代入計算／推理：** $b_0=12,b_1=1.464286$，$T_t=12+1.464286t$；$T_{10}=26.6429$。
5. **解讀結論：** 預測約 26.64 百萬；平均每年增加約 1.46 百萬。

#### 計算題 15 <a id="exam-ch17-problem-15"></a>

##### 題目

> University enrollment (thousands) for years 1–6 is 6.30, 7.70, 8.00, 8.20, 8.80, 8.00. Develop a linear trend and forecast year 10.

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 線性趨勢。
2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 第 6 年回落使線性趨勢不完美。
4. **代入計算／推理：** $T_t=6.63333+0.342857t$；$T_{10}=10.0619$ 千人。
5. **解讀結論：** 預測約 10.06 千人；它平滑掉單年回落，不代表回落可忽略。

#### 計算題 16 <a id="exam-ch17-problem-16"></a>

##### 題目

> Weekly sales (in thousands of dollars) are 15,16,19,18,19,20,19,22,15,21.<br>
> a. Compute a 4-week moving average. b. Compute MSE. c. Use $\alpha=.3$ for exponential smoothing. d. Forecast week 11.

##### 詳解

> **回看投影片講義：** [移動平均](./course2-slides-handout.html#formula-ch17-moving-average)、[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 移動平均與指數平滑比較。
2. **選方法：** 使用[移動平均](./course2-slides-handout.html#formula-ch17-moving-average)、[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** MA 的誤差期為 5–10；指數平滑令 $F_1=Y_1$。
4. **代入計算／推理：** 四週 MA 對 5–11 期為 17,18,19,19,20,19,19.25，$MSE=46/6=7.667$。指數預測對 2–11 期為 15,15.3,16.41,16.887,17.5209,18.2646,18.4852,19.5397,18.1778,19.0244。
5. **解讀結論：** 指數平滑的 week 11 預測約 19.024；兩方法都將第 9 週低值平滑處理。

#### 計算題 17 <a id="exam-ch17-problem-17"></a>

##### 題目

> Monthly units sold (thousands) are 8,3,4,5,12,10.<br>
> a. Compute a 3-month moving average (centered). b. Compute MSE. c. Use $\alpha=.2$. d. Forecast month 7.

##### 詳解

> **回看投影片講義：** [一般 MA vs CMA](./course2-slides-handout.html#compare-ch17-ma-vs-cma)


1. **辨認題型：** 題目同時寫 forecast 與 centered，來源用語有歧義。
2. **選方法：** 依[一般 MA vs CMA](./course2-slides-handout.html#compare-ch17-ma-vs-cma)，預測與 MSE 採只用過去的三期 MA。
3. **檢查假設：** 若字面採 CMA，會用到未來值且不能預測第 7 月。
4. **代入計算／推理：** $F_4=5,F_5=4,F_6=7,F_7=9$，$MSE=(0^2+8^2+3^2)/3=24.333$。指數平滑 $F_7=7.8368$。
5. **解讀結論：** 三期 MA 預測 9；指數平滑預測 7.837。來源的 centered 應視為誤植。

#### 計算題 18 <a id="exam-ch17-problem-18"></a>

##### 題目

> CMM sales (millions) for years 1–8 are 2,3,5,4,6,8,9,9. Develop a linear trend and forecast period 9.

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 等距年度。 4. **代入計算／推理：** $T_t=0.928571+1.071429t$，$T_9=10.5714$。
5. **解讀結論：** 預測約 10.57 百萬，歷史平均每年增約 1.07 百萬。

#### 計算題 19 <a id="exam-ch17-problem-19"></a>

##### 題目

> Auto sales (thousands) for years 1–10 are 195,200,250,270,320,380,440,460,500,500. Develop a linear trend and forecast $t=11$.

##### 詳解

> **回看投影片講義：** [線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)。
3. **檢查假設：** 後兩期趨平，線性延伸需保留疑慮。 4. **代入計算／推理：** $T_t=136+39.181818t$；$T_{11}=567$。
5. **解讀結論：** 預測 567 千輛；近期平台化可能使線性模型高估。

#### 計算題 20 <a id="exam-ch17-problem-20"></a>

##### 題目

> Amazing Graphics quarterly sales for years 6–8 are: Y6 2.5,1.5,2.4,1.6; Y7 2.0,1.4,1.7,1.9; Y8 2.5,2.0,2.4,2.1.<br>
> a. Compute four-quarter moving averages. b. Compute seasonal factors. c. Use them to adjust the forecast for the effect of season for year 6.

##### 詳解

> **回看投影片講義：** [CMA 與季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)


1. **辨認題型：** 乘法分解；part c 的 “forecast ... year 6” 來源語意不完整。
2. **選方法：** 使用[CMA 與季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)。
3. **檢查假設：** 四期 MA 為 2.000,1.875,1.850,1.675,1.750,1.875,2.025,2.200,2.250。
4. **代入計算／推理：** 正規化季節因子 Q1–Q4 為 1.1527,0.8534,1.0823,0.9116。若 c 指去除 year 6 季節效果，則為 $2.5/1.1527=2.169$、$1.5/.8534=1.758$、$2.4/1.0823=2.218$、$1.6/.9116=1.755$。
5. **解讀結論：** Q1、Q3 偏旺，Q2、Q4 偏淡；因題目未給 year 6 的基準預測，以上採「調整 year 6 觀察值」解讀。

#### 計算題 21 <a id="exam-ch17-problem-21"></a>

##### 題目

> John's tips for days 1–7 are 18,22,17,18,28,20,12. Compute 3-day moving averages, MSE, MAD, and forecast day 7.

##### 詳解

> **回看投影片講義：** [移動平均](./course2-slides-handout.html#formula-ch17-moving-average)


1. **辨認題型：** 三日 MA 回測。 2. **選方法：** 使用[移動平均](./course2-slides-handout.html#formula-ch17-moving-average)。
3. **檢查假設：** 預測 days 4–7。 4. **代入計算／推理：** 預測 19,19,21,22；誤差 $-1,9,-1,-10$；$MSE=45.75$，$MAD=MAE=5.25$。
5. **解讀結論：** day 7 的事前預測是 22；實際 12 造成最大失準。

#### 計算題 22 <a id="exam-ch17-problem-22"></a>

##### 題目

> Greeting-card sales for weeks 1–6 are 105,90,95,110,105,100. Use exponential smoothing with $\alpha=.2$, compute MSE and week 7 forecast, then compare $\alpha=.2$ with .3.

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 選平滑常數。 2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)與 MSE。
3. **檢查假設：** 共同回測 weeks 2–6。 4. **代入計算／推理：** $\alpha=.2$ 預測至 week 7 為 105,102,100.6,102.48,102.984,102.387，$MSE=75.523$；$\alpha=.3$ 的 $MSE=79.332$。
5. **解讀結論：** 歷史上 .2 較佳；week 7 預測 102.387。

#### 計算題 23 <a id="exam-ch17-problem-23"></a>

##### 題目

> Annual people assisted (hundreds) for years 1–11 are 22,24,28,24,22,24,20,26,24,28,26. Compare 3-year moving-average forecasts for 4–11 with exponential smoothing $\alpha=.4$ for 2–11 using MSE.

##### 詳解


1. **辨認題型：** 不同平滑法回測。 2. **選方法：** 各自只用當期以前資料。
3. **檢查假設：** 兩法評估起點不同，直接比較時應留意。 4. **代入計算／推理：** 三年 MA 對 4–11 為 24.667,25.333,24.667,23.333,22,23.333,23.333,26，$MSE=7.667$；指數平滑 $MSE=8.406$。
5. **解讀結論：** 依各題指定期間，三年 MA 較小；嚴格模型比較最好改用共同 4–11 期間。

#### 計算題 24 <a id="exam-ch17-problem-24"></a>

##### 題目

> Chicago temperatures for days 1–7 are 82,80,84,83,80,79,82. Use $\alpha=.2$, compute MSE and day 8 forecast, then compare with $\alpha=.3$.

##### 詳解

> **回看投影片講義：** [指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)


1. **辨認題型：** 指數平滑比較。 2. **選方法：** 使用[指數平滑](./course2-slides-handout.html#formula-ch17-exponential-smoothing)。
3. **檢查假設：** $F_1=82$。 4. **代入計算／推理：** .2 的 $MSE=4.033$、$F_8=81.399$；.3 的 $MSE=4.306$、$F_8=81.222$。
5. **解讀結論：** 歷史 MSE 支持 .2，day 8 預測約 81.40 度。

#### 計算題 25 <a id="exam-ch17-problem-25"></a>

##### 題目

> Yearly values for years 1–10 are 120,132,148,152,160,175,182,190,195,205. Produce forecasts for years 11 and 12.

##### 詳解

> **回看投影片講義：** [線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)


1. **辨認題型：** 長期趨勢。 2. **選方法：** 使用[線性趨勢](./course2-slides-handout.html#formula-ch17-linear-trend)。
3. **檢查假設：** 圖形近似線性。 4. **代入計算／推理：** $T_t=115.2+9.218182t$；$T_{11}=216.6$、$T_{12}=225.818$。
5. **解讀結論：** 預測約 216.6 與 225.82，每年平均增加約 9.22。

#### 計算題 26 <a id="exam-ch17-problem-26"></a>

##### 題目

> Boat units by quarter for years 1–5 are: 300,240,240,290; 350,300,280,320; 410,400,390,410; 490,450,440,510; 540,530,520,540. Find four-quarter CMAs, plot, compute seasonal-irregular values and seasonal factors, deseasonalize, fit a linear trend, and forecast all quarters of year 6.

##### 詳解

> **回看投影片講義：** [CMA→季節指數→去季節→再季節化](./course2-slides-handout.html#section-ch17-decomposition)


1. **辨認題型：** 完整乘法分解。
2. **選方法：** 依[CMA→季節指數→去季節→再季節化](./course2-slides-handout.html#section-ch17-decomposition)。
3. **檢查假設：** 季節振幅以倍率表示，四季指數正規化總和 4。
4. **代入計算／推理：** CMA 為 273.75,287.50,300,308.75,320,340,366.25,391.25,412.50,428.75,441.25,460,478.75,495,515,528.75。季節因子為 1.1132,0.9954,0.9056,0.9858。去季節資料配適得 $T_t=216.3001+17.3575t$；year 6 預測為 646.56,595.40,557.43,623.90。
5. **解讀結論：** 長期趨勢向上；Q1 旺、Q3 淡。預測同時反映上升基準與季節倍率。

#### 計算題 27 <a id="exam-ch17-problem-27"></a>

##### 題目

> John's income (thousands) for years 1–7 is 15.0,16.2,17.1,18.1,18.8,19.2,20.5. Obtain a linear trend and forecast the next 5 years.

##### 詳解

> **回看投影片講義：** [趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)


1. **辨認題型：** 線性趨勢。 2. **選方法：** 使用[趨勢係數](./course2-slides-handout.html#formula-ch17-linear-trend-coefficients)。
3. **檢查假設：** 外推逐年不確定性增加。 4. **代入計算／推理：** $T_t=14.3857+0.864286t$；years 8–12 為 21.300,22.164,23.029,23.893,24.757。
5. **解讀結論：** 歷史平均年增約 0.864 千；第五年預測最依賴趨勢延續假設。

#### 計算題 28 <a id="exam-ch17-problem-28"></a>

##### 題目

> Ajax quarterly profits for years 1–4 are 150,120,160,150; 150,130,180,160; 170,140,200,180; 200,150,230,200. Find CMAs, seasonal-irregular values, seasonal factors, and the deseasonalized series.

##### 詳解

> **回看投影片講義：** [分解流程](./course2-slides-handout.html#section-ch17-decomposition)


1. **辨認題型：** 乘法分解至去季節化。 2. **選方法：** 使用[分解流程](./course2-slides-handout.html#section-ch17-decomposition)。
3. **檢查假設：** 四季因子總和正規化為 4。 4. **代入計算／推理：** CMA 為 145,146.25,150,153.75,157.5,161.25,165,170,176.25,181.25,186.25,192.5；季節因子 1.0395,0.8199,1.1323,1.0083。去季節值逐筆為 $Y_t/S_q$。
5. **解讀結論：** Q3 約高於趨勢 13.2%，Q2 約低 18.0%；除以因子後才能公平比較跨季長期水準。

#### 計算題 29 <a id="exam-ch17-problem-29"></a>

##### 題目

> Middletown crimes for years 1–4 are 10,20,25,5; 10,30,35,25; 20,40,35,15; 20,50,45,35. Seasonal factors are .589, 1.351, 1.335, .726. Deseasonalize, estimate linear trend, and forecast all quarters of year 5.

##### 詳解

> **回看投影片講義：** [去季節化](./course2-slides-handout.html#formula-ch17-deseasonalize)、[再季節化](./course2-slides-handout.html#formula-ch17-reseasonalize)


1. **辨認題型：** 已知季節因子的分解預測。 2. **選方法：** 使用[去季節化](./course2-slides-handout.html#formula-ch17-deseasonalize)與[再季節化](./course2-slides-handout.html#formula-ch17-reseasonalize)。
3. **檢查假設：** 因子由題目給定，直接使用。 4. **代入計算／推理：** 去季節資料依序約 16.978,14.804,18.727,6.887,16.978,22.206,26.217,34.435,33.956,29.608,26.217,20.661,33.956,37.010,33.708,48.209。趨勢 $T_t=11.1037+1.7860t$；year 5 預測 24.42,58.43,60.13,33.99。
5. **解讀結論：** 基準犯罪數呈上升；Q2、Q3 季節倍率較高。這是描述性預測，不是季節造成犯罪的證明。

#### 計算題 30 <a id="exam-ch17-problem-30"></a>

##### 題目

> Seasonal factors Q1–Q4 are 1.2, .9, .8, 1.1 and $T=126.23-1.6t$, based on five years of quarterly data. Forecast all quarters of year 6.

##### 詳解

> **回看投影片講義：** [再季節化](./course2-slides-handout.html#formula-ch17-reseasonalize)


1. **辨認題型：** 趨勢乘季節。 2. **選方法：** 使用[再季節化](./course2-slides-handout.html#formula-ch17-reseasonalize)。
3. **檢查假設：** year 6 是 $t=21,22,23,24$。 4. **代入計算／推理：** 趨勢 92.63,91.03,89.43,87.83；乘季節後為 111.156,81.927,71.544,96.613。
5. **解讀結論：** 趨勢逐季下降，但 Q1、Q4 旺季倍率使原始預測相對較高。

#### 計算題 31 <a id="exam-ch17-problem-31"></a>

##### 題目

> Auto quarterly sales for years 8–10 are 160,180,190,170; 200,210,260,230; 210,240,290,260. Compute four-quarter moving averages, seasonal factors, and use the factors to adjust the forecast for the effect of season for year 9.

##### 詳解

> **回看投影片講義：** [CMA 與季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)


1. **辨認題型：** 分解與來源語意中的 year 9 調整。
2. **選方法：** 使用[CMA 與季節指數](./course2-slides-handout.html#formula-ch17-seasonal-index)。
3. **檢查假設：** 四期 MA 為 175,185,192.5,210,225,227.5,235,242.5,250；CMA 為 180,188.75,201.25,217.5,226.25,231.25,238.75,246.25。
4. **代入計算／推理：** 季節因子 Q1–Q4 為 0.9469,0.9807,1.1144,0.9580。若 adjust year 9 指去季節化，200,210,260,230 分別變成 211.21,214.14,233.31,240.09。
5. **解讀結論：** Q3 是旺季；year 9 去季節化後可比較共同基準。來源未提供另一組 year 9 趨勢預測，因此不臆造。

<div class="page-break" style="page-break-after: always;"></div>

# 第 18 章：無母數方法｜考古題詳解

## 考古題詳解

本章收錄 81 題，每題只出現一次，並依序保留「題目」與「詳解」；共用 Exhibit 或題組資料放在所屬題組前，不另外建立一段重複的原題彙編。需要複習方法時，使用每題的「回看投影片講義」。

### 選擇題｜第 1–24 題：基本觀念與方法辨認

#### 選擇題 1 <a id="exam-ch18-mc-1"></a>

##### 題目

> A collection of statistical methods that generally requires very few, if any, assumptions about the population distribution is known as
>
> a. parametric methods<br>
> b. nonparametric methods<br>
> c. distribution-fixed methods<br>
> d. normal

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 無母數方法定義。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，關鍵字是對母體分布形式要求很少。
- **檢查假設：** 這是名詞題；「很少」不等於完全沒有隨機與獨立條件。
- **代入計算／推理：** distribution-free 是 nonparametric 的別稱。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 反而通常指定分布族；b 正確；c 不是本章術語；d 是一種分布，不是一組方法。

#### 選擇題 2 <a id="exam-ch18-mc-2"></a>

##### 題目

> The collection of statistical methods that require assumptions about the population is known as
>
> a. distribution free methods<br>
> b. nonparametric methods<br>
> c. small populations<br>
> d. parametric methods

##### 詳解

> **回看投影片講義：** [母數與無母數的分辨](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 母數方法定義。
- **選方法：** 回到[母數與無母數的分辨](./course2-slides-handout.html#compare-ch18-method-selection)。
- **檢查假設：** 題目問方法類別，不是母體大小。
- **代入計算／推理：** 以特定母體分布與參數為基礎的是 parametric methods。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 都是較少指定分布形式的方法；c 不是方法名稱；d 正確。

#### 選擇題 3 <a id="exam-ch18-mc-3"></a>

##### 題目

> Parametric methods are statistical methods that
>
> a. require some assumptions about the population<br>
> b. require no assumptions about the population<br>
> c. only deal with small samples<br>
> d. considers the sign of two matched samples

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 母數方法特徵。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)先看是否指定母體模型。
- **檢查假設：** 樣本大小不是母數／無母數的定義。
- **代入計算／推理：** 母數方法會對母體分布或參數結構作假設。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 把無母數也誇大成零假設；c 錯在只限小樣本；d 描述符號檢定。

#### 選擇題 4 <a id="exam-ch18-mc-4"></a>

##### 題目

> Which of the following tests would not be an example of a nonparametric method?
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. t-test

##### 詳解

> **回看投影片講義：** [跨方法比較](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 方法分類。
- **選方法：** 依[跨方法比較](./course2-slides-handout.html#compare-ch18-method-selection)，找出以平均數與 t 分布為核心的方法。
- **檢查假設：** `not` 表示要選不是無母數者。
- **代入計算／推理：** t-test 是母數方法；其餘三個都以符號或名次分析。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都是本章方法；d 正確，因 t 檢定直接推論平均數。

#### 選擇題 5 <a id="exam-ch18-mc-5"></a>

##### 題目

> A sign test is a
>
> a. parametric method for determining the differences between two populations based on two matched samples<br>
> b. nonparametric method for determining the differences between two populations based on two matched samples<br>
> c. nonparametric method for determining the differences between two or more populations based on two or more matched samples<br>
> d. parametric method for determining the differences between two or more populations based on two or more matched samples

##### 詳解

> **回看投影片講義：** [符號檢定的二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 符號檢定用途。
- **選方法：** 使用[符號檢定的二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)，配對結果只保留正負方向。
- **檢查假設：** 這個版本比較兩個配對條件，不是三群以上。
- **代入計算／推理：** 符號檢定是 nonparametric，且可處理兩個 matched samples。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、d 錯在 parametric；b 正確；c 把兩條件擴成兩個以上母體，應另選其他方法。

#### 選擇題 6 <a id="exam-ch18-mc-6"></a>

##### 題目

> The level of measurement that allows for the rank ordering of data items is
>
> a. nominal measurement<br>
> b. ratio measurement<br>
> c. interval measurement<br>
> d. ordinal measurement

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 測量尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，題幹只保證可以排序。
- **檢查假設：** 沒有說相鄰差距或倍數有意義。
- **代入計算／推理：** 可排序但距離未必等距是 ordinal。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 只有標籤；b、c 都比題幹提供更多數值資訊；d 正確。

#### 選擇題 7 <a id="exam-ch18-mc-7"></a>

##### 題目

> The level of measurement that is simply a label for the purpose of identifying an item is
>
> a. ordinal measurement<br>
> b. ratio measurement<br>
> c. nominal measurement<br>
> d. internal measurement

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 名目尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，只有辨識標籤、沒有順序。
- **檢查假設：** `internal` 不是標準測量尺度；原題如此拼寫，忠實保留。
- **代入計算／推理：** nominal scale 的功能就是分類與命名。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 還有次序；b 還能談倍數；c 正確；d 不是四種尺度之一。

#### 選擇題 8 <a id="exam-ch18-mc-8"></a>

##### 題目

> The labeling of parts as "defective" or "non-defective" is an example of
>
> a. ordinal data<br>
> b. ratio data<br>
> c. interval data<br>
> d. nominal data

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 二元類別的尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，兩標籤只區分類別。
- **檢查假設：** defective 與 non-defective 沒有可運算的距離。
- **代入計算／推理：** 這是 nominal data。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 需要有序等級；b、c 需要數值差距；d 正確。

#### 選擇題 9 <a id="exam-ch18-mc-9"></a>

##### 題目

> In a questionnaire, respondents are asked to mark their marital status. Marital status is an example of the
>
> a. ordinal scale<br>
> b. nominal scale<br>
> c. ratio scale<br>
> d. interval scale

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 類別尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，婚姻狀態只有互斥名稱。
- **檢查假設：** 類別沒有自然的高低順序。
- **代入計算／推理：** 因此是 nominal scale。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 會錯加順序；b 正確；c、d 需要有意義的數值差距。

#### 選擇題 10 <a id="exam-ch18-mc-10"></a>

##### 題目

> The scale of measurement that is used to rank order the observation for a variable is called the
>
> a. ratio scale<br>
> b. ordinal scale<br>
> c. nominal scale<br>
> d. interval scale

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 排名尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，題幹直接說 rank order。
- **檢查假設：** 沒有保證名次 1 與 2 的差等於 2 與 3 的差。
- **代入計算／推理：** 排序所需的最低尺度是 ordinal。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、d 提供更強的距離資訊；b 正確；c 不能排序。

#### 選擇題 11 <a id="exam-ch18-mc-11"></a>

##### 題目

> On a teacher evaluation form students are asked to rate their professor's performance as excellent, very good, good, and poor. This is an example of the
>
> a. ordinal scale<br>
> b. ratio scale<br>
> c. nominal scale<br>
> d. interval scale

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 有序評等。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，四個評語有自然順序。
- **檢查假設：** excellent 到 very good 的距離未必等於 good 到 poor。
- **代入計算／推理：** 有序但不保證等距，屬 ordinal。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 要求數值距離；c 忽略既有順序。

#### 選擇題 12 <a id="exam-ch18-mc-12"></a>

##### 題目

> Temperature is an example of a variable that uses
>
> a. the ratio scale<br>
> b. the interval scale<br>
> c. the ordinal scale<br>
> d. either the ratio or the ordinal scale

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 溫度的測量尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，一般教材中的攝氏或華氏溫度看差值。
- **檢查假設：** 0°C 不代表完全沒有溫度，故不能把 20°C 說成 10°C 的兩倍熱。
- **代入計算／推理：** 差值有意義、零點任意，是 interval scale。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 適合絕對零點尺度；b 正確；c 只保留順序；d 混入不適用的尺度。

#### 選擇題 13 <a id="exam-ch18-mc-13"></a>

##### 題目

> The speed of an automobile is an example of a variable that uses the
>
> a. ratio scale<br>
> b. interval scale<br>
> c. nominal scale<br>
> d. ordinal scale

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 速度的測量尺度。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，速度有真正的零點。
- **檢查假設：** 0 km/h 表示沒有移動，倍數比較有意義。
- **代入計算／推理：** 因此屬 ratio scale。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 零點可任意；c 只有標籤；d 只有順序。

#### 選擇題 14 <a id="exam-ch18-mc-14"></a>

##### 題目

> Statistical methods that generally require very few, if any, assumptions about the population distribution are known as
>
> a. parametric<br>
> b. nonparametric<br>
> c. free methods<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 無母數方法定義的重複確認。
- **選方法：** 回到[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)。
- **檢查假設：** 題目指的是不指定特定母體分布形式。
- **代入計算／推理：** 正式名稱是 nonparametric methods。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 通常有較明確分布假設；b 正確；c 不是完整術語；d 因 b 已正確而錯。

#### 選擇題 15 <a id="exam-ch18-mc-15"></a>

##### 題目

> Which of the following tests would not be an example of nonparametric method?
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. t test

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 方法分類的重複題。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)找出直接檢定平均數者。
- **檢查假設：** 題幹有 `not`。
- **代入計算／推理：** t test 是母數方法。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都使用符號或名次；d 正確。

#### 選擇題 16 <a id="exam-ch18-mc-16"></a>

##### 題目

> A nonparametric version of the Parametric analysis of variance test is the
>
> a. Kruskal-Wallis Test<br>
> b. Mann-Whitney-Wilcoxon Test<br>
> c. sign test<br>
> d. Wilcoxon Signed-rank test

##### 詳解

> **回看投影片講義：** [Kruskal-Wallis 公式](./course2-slides-handout.html#formula-ch18-kruskal-wallis)


- **辨認題型：** 三群以上方法對照。
- **選方法：** 依[Kruskal-Wallis 公式](./course2-slides-handout.html#formula-ch18-kruskal-wallis)，它比較 $k$ 個獨立樣本的名次。
- **檢查假設：** ANOVA 的典型問題是三群以上；不是兩群或配對。
- **代入計算／推理：** Kruskal-Wallis 是 one-way ANOVA 的無母數對照。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 只比兩個獨立群；c 只看正負；d 是兩個配對條件。

#### 選擇題 17 <a id="exam-ch18-mc-17"></a>

##### 題目

> A nonparametric method for determining the differences between two populations based on two matched samples where only preference data is required is the
>
> a. Mann-Whitney-Wilcoxon test<br>
> b. Wilcoxon signed-rank test<br>
> c. sign test<br>
> d. Kruskal-Wallis Test

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 配對偏好資料的方法選擇。
- **選方法：** 依[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)，只有偏好方向時轉成正負號。
- **檢查假設：** 沒有數值差距可供 signed-rank 排 $|d_i|$。
- **代入計算／推理：** matched samples 加 preference data 指向 sign test。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 是獨立樣本；b 需要配對數值；c 正確；d 是三群以上獨立樣本。

#### 選擇題 18 <a id="exam-ch18-mc-18"></a>

##### 題目

> When ranking combined data in a Wilcoxon signed rank test, the data that receives a rank of 1 is the
>
> a. lowest value<br>
> b. highest value<br>
> c. middle value<br>
> d. average of the highest and the lowest of values

##### 詳解

> **回看投影片講義：** [Wilcoxon signed-rank 步驟](./course2-slides-handout.html#formula-ch18-signed-rank)


- **辨認題型：** 名次配置規則。
- **選方法：** 依[Wilcoxon signed-rank 步驟](./course2-slides-handout.html#formula-ch18-signed-rank)，實際上是對非零 $|d_i|$ 由小到大排名。
- **檢查假設：** 若最低值同名次，應分配平均名次；題目未給 ties。
- **代入計算／推理：** 最小絕對差得到 rank 1。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 應得最大名次；c 沒有固定名次；d 不是排名規則。

#### 選擇題 19 <a id="exam-ch18-mc-19"></a>

##### 題目

> Statistical methods that require assumptions about the population are known as
>
> a. distribution free<br>
> b. nonparametric<br>
> c. either distribution free of nonparametric<br>
> d. parametric

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 母數方法定義。
- **選方法：** 回到[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)。
- **檢查假設：** 原題 c 的 `of` 疑為 `or`，不影響選項意義。
- **代入計算／推理：** 要求母體假設的是 parametric methods。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b、c 都指無母數；d 正確。

#### 選擇題 20 <a id="exam-ch18-mc-20"></a>

##### 題目

> The Spearman rank-correlation coefficient is
>
> a. a correlation measure based on the average of data items<br>
> b. a correlation measure based on rank-ordered data for two variables<br>
> c. a correlation measure based on the median of data items<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [Spearman 公式](./course2-slides-handout.html#formula-ch18-spearman)


- **辨認題型：** Spearman 定義。
- **選方法：** 使用[Spearman 公式](./course2-slides-handout.html#formula-ch18-spearman)。
- **檢查假設：** 兩套名次必須來自同一批對象。
- **代入計算／推理：** $r_s$ 以兩變數的 rank-ordered data 衡量單調關聯。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a、c 都不是公式依據；b 正確；d 因 b 已正確而錯。

#### 選擇題 21 <a id="exam-ch18-mc-21"></a>

##### 題目

> A nonparametric test for the equivalence of two populations would be used instead of a parametric test for the equivalence of the population parameters if
>
> a. the samples are very large<br>
> b. the samples are not independent<br>
> c. no information about the populations is available<br>
> d. The parametric test is always used in this situation.

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 何時選無母數方法。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，若無法合理指定母體分布，就考慮無母數方法。
- **檢查假設：** 無母數方法仍不能修復不獨立；b 不是使用理由。
- **代入計算／推理：** 缺乏母體分布資訊時，依名次或符號的方法較合適。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 大樣本本身不迫使改方法；b 違反兩類方法共同的重要條件；c 正確；d 過度絕對。

#### 選擇題 22 <a id="exam-ch18-mc-22"></a>

##### 題目

> A nonparametric test would be used if
>
> a. nominal data is available<br>
> b. interval data is available<br>
> c. it is known that the population is normally distributed<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)


- **辨認題型：** 資料尺度與方法。
- **選方法：** 依[方法選擇流程](./course2-slides-handout.html#compare-ch18-method-selection)，名目資料無法直接使用平均數型母數方法。
- **檢查假設：** 區間資料也能用無母數，但「有區間資料」本身不是必要理由；已知常態通常支持母數法。
- **代入計算／推理：** nominal data 常需要符號或類別方法。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 資訊較完整，仍需看目標與條件；c 反而支持母數法；d 因 a 正確而錯。

#### 選擇題 23 <a id="exam-ch18-mc-23"></a>

##### 題目

> If a null hypothesis that states that two populations are identical is rejected using a nonparametric test, then it is safe to assume that
>
> a. neither the means nor the variances are equal<br>
> b. the means of the populations are not the same<br>
> c. the variances of the populations are not the same<br>
> d. We cannot be sure of the way in which the populations differ from each other.

##### 詳解

> **回看投影片講義：** [MWW 的一般假設](./course2-slides-handout.html#formula-ch18-mww-w)


- **辨認題型：** 分布檢定的結論界線。
- **選方法：** 依[MWW 的一般假設](./course2-slides-handout.html#formula-ch18-mww-w)，拒絕的是兩個完整分布相同。
- **檢查假設：** 若未另假設兩群形狀相同，不能只歸因於平均、中位數或變異數。
- **代入計算／推理：** 顯著只說至少某種分布特徵不同。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 太強；b、c 都擅自指定差異來源；d 正確。

#### 選擇題 24 <a id="exam-ch18-mc-24"></a>

##### 題目

> The Spearman rank-correlation coefficient for 20 pairs of data when $\Sigma d_i^2=50$ is.
>
> a. 0.0063<br>
> b. 0.0376<br>
> c. 0.9624<br>
> d. 0.9937

##### 詳解

> **回看投影片講義：** [標準 Spearman 公式](./course2-slides-handout.html#formula-ch18-spearman)


- **辨認題型：** Spearman 係數計算。
- **選方法：** 使用[標準 Spearman 公式](./course2-slides-handout.html#formula-ch18-spearman)。
- **檢查假設：** 題目未提 ties，故可直接用 $d_i$ 公式。
- **代入計算／推理：** $r_s=1-6(50)/[20(20^2-1)]=1-300/7980=0.9624$。
- **解讀結論：** 答案是 **c** ；兩套排序高度同向。
- **選項檢討：** a、b 是把扣除量或分母處理錯；c 正確；d 對應過小的名次差。

### 選擇題｜第 25–53 題：共用 Exhibit 與計算

#### 題組 18-1：選擇題 25–28 共用資料

> Exhibit 18-1
>
> Fifteen people were given two types of cereal, Brand X and Brand Y. Two people preferred Brand X and thirteen people preferred Brand Y. We want to determine whether or not customers prefer one brand over the other.

#### 選擇題 25 <a id="exam-ch18-mc-25"></a>

##### 題目

> Refer to Exhibit 18-1. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

> **回看投影片講義：** [符號檢定二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 兩品牌偏好的符號檢定。
- **選方法：** 使用[符號檢定二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** 每人只表達一個偏好，且受試者彼此獨立。
- **代入計算／推理：** 無偏好差異表示偏好任一品牌的機率 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 把機率誤寫成平均數；c 把機率寫成不可能的 5；d 正確。

#### 選擇題 26 <a id="exam-ch18-mc-26"></a>

##### 題目

> Refer to Exhibit 18-1. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. Poisson<br>
> d. binomial

##### 詳解

> **回看投影片講義：** [精確二項分布](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 小樣本符號檢定參考分布。
- **選方法：** 使用[精確二項分布](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** $n=15\le20$，投影片規則用 exact binomial。
- **代入計算／推理：** 每人偏好 X／Y 是兩結果、$p=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a 是大樣本近似；b、c 不符合兩結果計數；d 正確。

#### 選擇題 27 <a id="exam-ch18-mc-27"></a>

##### 題目

> Refer to Exhibit 18-1. The p-value for this test is
>
> a. 0.0005<br>
> b. 0.001<br>
> c. 0.0037<br>
> d. 0.0074

##### 詳解

> **回看投影片講義：** [精確二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 雙尾精確符號檢定。
- **選方法：** 依[精確二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)，從較小的 2 人那一尾計算再乘 2。
- **檢查假設：** 有效樣本 $n=15$，觀察到 $X=2$。
- **代入計算／推理：** $p=2P(X\le2)=2(1+15+105)/2^{15}=0.007385\approx0.0074$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 漏加部分尾端或漏乘 2；c 是單尾值；d 正確。

#### 選擇題 28 <a id="exam-ch18-mc-28"></a>

##### 題目

> Refer to Exhibit 18-1. At 95% confidence, the null hypothesis should
>
> a. be rejected<br>
> b. not be rejected<br>
> c. be revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 以 p 值作決策。
- **選方法：** 沿用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** 95% confidence 對應 $\alpha=0.05$。
- **代入計算／推理：** $p=0.0074<0.05$。
- **解讀結論：** 答案是 **a** ；兩品牌偏好並非各半，樣本方向偏向 Brand Y。
- **選項檢討：** a 正確；b 與 p 值比較相反；c 不是標準決策；d 因 a 正確而錯。

#### 題組 18-2：選擇題 29–34 共用資料

> Exhibit 18-2
>
> Students in statistics classes were asked whether they preferred a 10-minute break or to get out of class 10 minutes early. In a sample of 150 students, 40 preferred a 10-minute break, 80 preferred to get out of class 10 minutes early, and 30 had no preference. We want to determine if there is a difference in students' preferences.

原題第 29–34 題誤寫為 `Exhibit 19-2`；實際上都指這份 Exhibit 18-2。刪除 30 位無偏好者後，有效樣本 $n=120$。

#### 選擇題 29 <a id="exam-ch18-mc-29"></a>

##### 題目

> Refer to Exhibit 19-2. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 兩種偏好的符號檢定。
- **選方法：** 使用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** 無偏好者不給正負號，已刪除。
- **代入計算／推理：** 無差異時，偏好提早下課的機率 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 的 $\mu$ 不是二項機率；c 超出機率範圍；d 正確。

#### 選擇題 30 <a id="exam-ch18-mc-30"></a>

##### 題目

> Refer to Exhibit 19-2. The mean and the standard deviation of the sampling distribution of the number of students who preferred to get out early are
>
> a. 50 and 30<br>
> b. 60 and 30<br>
> c. 50 and 5.478<br>
> d. 60 and 5.478

##### 詳解

> **回看投影片講義：** [符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 符號數的常態近似參數。
- **選方法：** 使用[符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 有效 $n=120$，不是原始 150。
- **代入計算／推理：** $\mu=0.5(120)=60$，$\sigma=\sqrt{0.25(120)}=\sqrt{30}=5.478$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、c 錯把有效人數算成 100；b 把變異數 30 當標準差；d 正確。

#### 選擇題 31 <a id="exam-ch18-mc-31"></a>

##### 題目

> Refer to Exhibit 19-2. To test the null hypothesis, the appropriate probability distribution to use is the
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 大樣本符號檢定的課堂計算法。
- **選方法：** 依[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)，$n=120>20$。
- **檢查假設：** 精確分布本質仍是 binomial，但投影片的大樣本計算選 normal approximation。
- **代入計算／推理：** $np=n(1-p)=60$，近似充足。
- **解讀結論：** 依題庫預期答案是 **a** 。
- **選項檢討：** a 正確；b、c 不處理二項正號數；d 是精確模型，但本題問大樣本採用的計算分布。

#### 選擇題 32 <a id="exam-ch18-mc-32"></a>

##### 題目

> Refer to Exhibit 19-2. The test statistic based on the number of students who preferred to get out early equals
>
> a. 1.825<br>
> b. 0.67<br>
> c. 0.82<br>
> d. 3.65

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 正號數的標準化。
- **選方法：** 使用[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 原題選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(80-60)/5.478=3.65$。若依投影片加修正，$z=(79.5-60)/5.478=3.56$，決策不變。
- **解讀結論：** 對應選項答案是 **d** 。
- **選項檢討：** a 是少除約一半；b、c 是錯誤分母；d 正確對應題庫算法。

#### 選擇題 33 <a id="exam-ch18-mc-33"></a>

##### 題目

> Refer to Exhibit 19-2. The p-value for testing the hypotheses is
>
> a. less than 0.002<br>
> b. between 0.002 and 0.05<br>
> c. between 0.05 and 0.10<br>
> d. greater than 0.10

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 雙尾 p 值區間。
- **選方法：** 由[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)取 $2P(Z\ge|z|)$。
- **檢查假設：** 不論用 $z=3.65$ 或連續性修正的 3.56，都是雙尾。
- **代入計算／推理：** 未修正 $p\approx0.00026$；修正後約 $0.00037$，都小於 0.002。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、c、d 都把極端的 $z$ 誤配成過大的 p 值。

#### 選擇題 34 <a id="exam-ch18-mc-34"></a>

##### 題目

> Refer to Exhibit 19-2. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** p 值決策。
- **選方法：** 沿用[符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 題目未另給 $\alpha$，依常見 0.05；前題 p 值遠小於 0.002。
- **代入計算／推理：** $p<0.05$，拒絕 $H_0$。
- **解讀結論：** 答案是 **a** ；偏好提早下課的人顯著較多。
- **選項檢討：** a 正確；b 與 p 值矛盾；c 不是檢定決策；d 因 a 正確而錯。

#### 題組 18-3：選擇題 35–39 共用資料

> Exhibit 18-3
>
> It is believed that the median yearly income in a suburb of Atlanta is \$70,000. A sample of 67 residents was taken. Thirty-eight had yearly incomes above \$70,000, 26 had yearly incomes below \$70,000, and 3 had yearly incomes equal to \$70,000. The null hypothesis to be tested is $H_0$: median = \$70,000.

刪除 3 位剛好等於 70,000 美元者後，有效樣本 $n=64$。

#### 選擇題 35 <a id="exam-ch18-mc-35"></a>

##### 題目

> Refer to Exhibit 18-3. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

> **回看投影片講義：** [符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 大樣本中位數符號檢定。
- **選方法：** 使用[符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 有效 $n=64>20$。
- **代入計算／推理：** 正號數的二項分布以常態分布近似。
- **解讀結論：** 題庫預期答案是 **a** 。
- **選項檢討：** a 正確；b、c 不符合正負計數；d 是精確母分布，但題庫依大樣本規則選 normal。

#### 選擇題 36 <a id="exam-ch18-mc-36"></a>

##### 題目

> Refer to Exhibit 18-3. The mean and the standard deviation (respectively) for this test about the median are
>
> a. 32 and 4<br>
> b. 32 and 16<br>
> c. 33.5 and 4<br>
> d. 33.5 and 16

##### 詳解

> **回看投影片講義：** [常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 常態近似參數。
- **選方法：** 使用[常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 平手已刪除，$n=64$。
- **代入計算／推理：** $\mu=32$，$\sigma=\sqrt{16}=4$。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 把變異數 16 當標準差；c、d 未刪除平手。

#### 選擇題 37 <a id="exam-ch18-mc-37"></a>

##### 題目

> Refer to Exhibit 18-3. The test statistic has a value of
>
> a. 1.00<br>
> b. 1.50<br>
> c. 2.00<br>
> d. 2.50

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 正號數標準化。
- **選方法：** 使用[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(38-32)/4=1.50$；修正後為 $(37.5-32)/4=1.375$。
- **解讀結論：** 對應選項答案是 **b** 。
- **選項檢討：** a、c、d 是錯誤中心或尺度；b 符合題庫算法。

#### 選擇題 38 <a id="exam-ch18-mc-38"></a>

##### 題目

> Refer to Exhibit 18-3. The p-value for this test is
>
> a. 0.4332<br>
> b. 0.8664<br>
> c. 0.0668<br>
> d. 0.1336

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 雙尾 p 值。
- **選方法：** 由[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)計算 $2P(Z\ge1.50)$。
- **檢查假設：** 題庫沿用未修正 $z$；若修正，p 值約 0.1691。
- **代入計算／推理：** $2(0.0668)=0.1336$。
- **解讀結論：** 對應答案是 **d** 。
- **選項檢討：** a、b 使用錯誤中央面積；c 是單尾；d 是題庫的雙尾值。

#### 選擇題 39 <a id="exam-ch18-mc-39"></a>

##### 題目

> Refer to Exhibit 18-3. The null hypothesis should be
>
> a. rejected<br>
> b. not rejected<br>
> c. revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 中位數檢定決策。
- **選方法：** 沿用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)。
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

#### 選擇題 40 <a id="exam-ch18-mc-40"></a>

##### 題目

> Refer to Exhibit 18-4. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. Normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. Binomial

##### 詳解

> **回看投影片講義：** [signed-rank 常態近似](./course2-slides-handout.html#formula-ch18-signed-rank-normal)


- **辨認題型：** 配對數值的 Wilcoxon signed-rank 檢定。
- **選方法：** 使用[signed-rank 常態近似](./course2-slides-handout.html#formula-ch18-signed-rank-normal)。
- **檢查假設：** 刪除 Person 5 的零差後 $n=11\ge10$，且差值需近似對稱。
- **代入計算／推理：** 投影片以 $T^+$ 的 normal approximation 作參考分布。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 不處理配對名次；c 是配對 t 的參考分布；d 是只看正負的符號檢定。

#### 選擇題 41 <a id="exam-ch18-mc-41"></a>

##### 題目

> Refer to Exhibit 18-4. The test statistic equals
>
> a. -0.81 or 0.81<br>
> b. -0.89 or 0.89<br>
> c. -10 or 10<br>
> d. -20 or 20

##### 詳解

> **回看投影片講義：** [signed-rank 公式](./course2-slides-handout.html#formula-ch18-signed-rank-normal)


- **辨認題型：** signed-rank 的常態標準化。
- **選方法：** 依[signed-rank 公式](./course2-slides-handout.html#formula-ch18-signed-rank-normal)計算 $T^+$。
- **檢查假設：** 以 `With - Without` 為差，零差刪除；同絕對差用平均名次。
- **代入計算／推理：** $T^+=23$，$\mu=33$，$\sigma=\sqrt{126.5}=11.247$，未修正 $z=(23-33)/11.247=-0.89$。
- **解讀結論：** 答案是 **b** ；正負號依差值方向而定，絕對值相同。
- **選項檢討：** a 來自錯誤名次和或尺度；b 正確；c、d 把未標準化差距當 z。

#### 選擇題 42 <a id="exam-ch18-mc-42"></a>

##### 題目

> Refer to Exhibit 18-4. The p-value for this test is
>
> a. 0.3133<br>
> b. 0.6266<br>
> c. 0.3734<br>
> d. 0.8167

##### 詳解

> **回看投影片講義：** [signed-rank 常態近似](./course2-slides-handout.html#formula-ch18-signed-rank-normal)


- **辨認題型：** 雙尾 signed-rank p 值。
- **選方法：** 由[signed-rank 常態近似](./course2-slides-handout.html#formula-ch18-signed-rank-normal)取 $2P(Z\le-0.89)$。
- **檢查假設：** 題庫使用未修正 z。
- **代入計算／推理：** $p\approx2(0.1867)=0.3734$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a、b、d 是單尾、倍數或中央面積的誤讀；c 正確。

#### 選擇題 43 <a id="exam-ch18-mc-43"></a>

##### 題目

> Refer to Exhibit 18-4. The null hypothesis should
>
> a. be rejected<br>
> b. not be rejected<br>
> c. be revised<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)


- **辨認題型：** 配對檢定決策。
- **選方法：** 沿用[Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)。
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

#### 選擇題 44 <a id="exam-ch18-mc-44"></a>

##### 題目

> Refer to Exhibit 18-5. To test the null hypothesis, the appropriate probability distribution to use is
>
> a. normal<br>
> b. chi-square<br>
> c. t distribution<br>
> d. binomial

##### 詳解

> **回看投影片講義：** [MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)


- **辨認題型：** 兩個獨立樣本的 MWW。
- **選方法：** 使用[MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)。
- **檢查假設：** $n_1=10,n_2=11$ 都至少 7，符合投影片門檻。
- **代入計算／推理：** $W$ 的抽樣分布以 normal approximation 處理。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b、d 不符合秩和；c 是比較平均數的 t 方法。

#### 選擇題 45 <a id="exam-ch18-mc-45"></a>

##### 題目

> Refer to Exhibit 18-5. The mean ($\mu_T$) is
>
> a. 10<br>
> b. 110<br>
> c. 66<br>
> d. 55

##### 詳解

> **回看投影片講義：** [MWW 平均公式](./course2-slides-handout.html#formula-ch18-mww-normal)


- **辨認題型：** 第一群名次和的期望值。
- **選方法：** 使用[MWW 平均公式](./course2-slides-handout.html#formula-ch18-mww-normal)。
- **檢查假設：** 第一群 women 有 $n_1=10$，第二群 $n_2=11$。
- **代入計算／推理：** $\mu_W=10(10+11+1)/2=110$。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 只是樣本數；b 正確；c、d 是錯誤乘除。

#### 選擇題 46 <a id="exam-ch18-mc-46"></a>

##### 題目

> Refer to Exhibit 18-5. The standard deviation ($\sigma_T$) is
>
> a. 10<br>
> b. 11.5<br>
> c. 14.2<br>
> d. 110

##### 詳解

> **回看投影片講義：** [MWW 標準差公式](./course2-slides-handout.html#formula-ch18-mww-normal)


- **辨認題型：** MWW 名次和標準差。
- **選方法：** 使用[MWW 標準差公式](./course2-slides-handout.html#formula-ch18-mww-normal)。
- **檢查假設：** 題庫公式未另做 ties correction。
- **代入計算／推理：** $\sigma_W=\sqrt{10(11)(22)/12}=14.20$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a、b 是錯誤根號或分母；c 正確；d 是平均數。

#### 題組 18-6：選擇題 47–53 共用資料

> Exhibit 18-6
>
> Forty-one individuals from a sample of 60 indicated they oppose legalized abortion. We are interested in determining whether or not there is a significant difference between the proportions of opponents and proponents of legalized abortion.

#### 選擇題 47 <a id="exam-ch18-mc-47"></a>

##### 題目

> Refer to Exhibit 18-6. The null hypothesis that is being tested is
>
> a. $H_0:\mu=5$<br>
> b. $H_0:\mu=0.5$<br>
> c. $H_0:P=5$<br>
> d. $H_0:P=0.5$

##### 詳解

> **回看投影片講義：** [符號檢定二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 兩種立場比例是否相同。
- **選方法：** 使用[符號檢定二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** 每人落入支持或反對其中一類，樣本共 60。
- **代入計算／推理：** 沒有比例差異即 $P=0.5$。
- **解讀結論：** 答案是 **d** 。
- **選項檢討：** a、b 把比例寫成平均數；c 機率不可能為 5；d 正確。

#### 選擇題 48 <a id="exam-ch18-mc-48"></a>

##### 題目

> Refer to Exhibit 18-6. $\mu$ in this situation is
>
> a. 60<br>
> b. 30<br>
> c. 41<br>
> d. 2

##### 詳解

> **回看投影片講義：** [常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 正號數的虛無平均。
- **選方法：** 使用[常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** $n=60,p=0.5$。
- **代入計算／推理：** $\mu=0.5(60)=30$。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 是總樣本；b 正確；c 是觀察到的反對數；d 是類別數。

#### 選擇題 49 <a id="exam-ch18-mc-49"></a>

##### 題目

> Refer to Exhibit 18-6. $\sigma$ in this problem is
>
> a. 15<br>
> b. 5.47<br>
> c. 3.87<br>
> d. 7.45

##### 詳解

> **回看投影片講義：** [常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 正號數標準差。
- **選方法：** 使用[常態近似公式](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** $n=60$。
- **代入計算／推理：** $\sigma=\sqrt{0.25(60)}=\sqrt{15}=3.873$。
- **解讀結論：** 答案是 **c** 。
- **選項檢討：** a 是變異數；b 對應 $n=120$；c 正確；d 無此計算來源。

#### 選擇題 50 <a id="exam-ch18-mc-50"></a>

##### 題目

> Refer to Exhibit 18-6. The test statistics is
>
> a. 3.87<br>
> b. 2.84<br>
> c. 60<br>
> d. 0.5

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 符號數 z 統計量。
- **選方法：** 使用[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
- **檢查假設：** 選項採未做連續性修正的版本。
- **代入計算／推理：** $z=(41-30)/3.873=2.84$；修正後為 $(40.5-30)/3.873=2.71$。
- **解讀結論：** 對應答案是 **b** 。
- **選項檢討：** a 是標準差；b 正確對應題庫；c 是樣本數；d 是虛無機率。

#### 選擇題 51 <a id="exam-ch18-mc-51"></a>

##### 題目

> Refer to Exhibit 18-6. p-value is
>
> a. 0.0023<br>
> b. 0.0046<br>
> c. 0.4954<br>
> d. 0.4977

##### 詳解

> **回看投影片講義：** [常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


- **辨認題型：** 雙尾常態 p 值。
- **選方法：** 由[常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)取 $2P(Z\ge2.84)$。
- **檢查假設：** 題庫採未修正 z；精確二項 p 值為 0.00622。
- **代入計算／推理：** $2(0.0023)=0.0046$。
- **解讀結論：** 題庫對應答案是 **b** 。
- **選項檢討：** a 是單尾；b 正確；c、d 把尾端與中央面積混淆。

#### 選擇題 52 <a id="exam-ch18-mc-52"></a>

##### 題目

> Refer to Exhibit 18-6. The null hypothesis should be
>
> a. Rejected<br>
> b. not rejected<br>
> c. Not enough information is given to answer this question.<br>
> d. None of these alternatives.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 符號檢定決策。
- **選方法：** 沿用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)。
- **檢查假設：** 以 $\alpha=0.05$；題庫近似與精確 p 值都小於 0.05。
- **代入計算／推理：** $p\approx0.0046$，拒絕 $H_0$。
- **解讀結論：** 答案是 **a** 。
- **選項檢討：** a 正確；b 與 p 值矛盾；c 的資料已足夠；d 因 a 正確而錯。

#### 選擇題 53 <a id="exam-ch18-mc-53"></a>

##### 題目

> Refer to Exhibit 18-6. The conclusion is that there
>
> a. is no significant difference between the proportions<br>
> b. is a significant difference between the proportions<br>
> c. could be a difference in proportions, depending on the sample size<br>
> d. None of these alternatives is correct.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


- **辨認題型：** 把檢定決策翻成情境語言。
- **選方法：** 依[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)解讀比例是否各半。
- **檢查假設：** 結論只談比例差異，不談立場形成的因果。
- **代入計算／推理：** 已拒絕 $P=0.5$，且 41 對 19 顯示反對者較多。
- **解讀結論：** 答案是 **b** 。
- **選項檢討：** a 與拒絕結果相反；b 正確；c 忽略已完成的檢定；d 因 b 正確而錯。

### 計算題｜第 1–28 題：完整推論與獨立驗算

#### 計算題 1 <a id="exam-ch18-problem-1"></a>

##### 題目

> In a sample of 400 people, 250 indicated that they prefer domestic wines, while 140 said they prefer European wines, and 10 indicated no preference. We want to use the sign test to determine if there is evidence of a significant difference in the preferences for the two types of wine.
>
> a. Provide the hypotheses to be tested.<br>
> b. Compute the mean.<br>
> c. Compute the standard deviation.<br>
> d. At 95% confidence, test to determine if there is evidence of a significant difference in the preferences for the two types of wine.

##### 詳解

> **回看投影片講義：** [大樣本符號檢定](./course2-slides-handout.html#formula-ch18-sign-normal)


1. **辨認題型：** 兩種偏好的符號檢定；無偏好者不提供方向。
2. **選方法：** 使用[大樣本符號檢定](./course2-slides-handout.html#formula-ch18-sign-normal)，檢定 $H_0:p=0.5$ 對 $H_a:p\ne0.5$。
3. **檢查假設：** 刪除 10 位無偏好者後 $n=390$；每人的偏好應彼此獨立，且 $np=n(1-p)=195$ 足夠大。
4. **代入計算／推理：** $\mu=195$，$\sigma=\sqrt{97.5}=9.874$。以 domestic 為正號，連續性修正後 $z=(249.5-195)/9.874=5.519$，雙尾 $p=3.40\times10^{-8}$；精確二項驗算 $p=2.77\times10^{-8}$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；國產酒偏好顯著較多。這不表示每位消費者都偏好國產酒，也不量化偏好強度。

#### 計算題 2 <a id="exam-ch18-problem-2"></a>

##### 題目

> In a sample of 200 racquetball players, 120 indicated they prefer Penn racquetballs, 75 favored Ektelon, and 5 were indifferent. We want to use the sign test to determine if there is evidence of a significant difference in the preferences for the two types of racquetballs.
>
> a. Provide the hypotheses to be tested.<br>
> b. Compute the mean.<br>
> c. Compute the standard deviation.<br>
> d. At 95% confidence, test to determine if there is evidence of a significant difference in the preferences for the two types of racquetballs.

##### 詳解

> **回看投影片講義：** [符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


1. **辨認題型：** Penn 與 Ektelon 的二選一偏好。
2. **選方法：** 使用[符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 刪除 5 位 indifferent，$n=195$；兩個期望次數都是 97.5。
4. **代入計算／推理：** $\mu=97.5$，$\sigma=\sqrt{48.75}=6.982$；修正後 $z=(119.5-97.5)/6.982=3.151$，雙尾 $p=0.00163$；精確二項 $p=0.00156$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；樣本方向顯示 Penn 較受偏好。

#### 計算題 3 <a id="exam-ch18-problem-3"></a>

##### 題目

> The monthly sales records of two branches of a department store (Branch A and Branch B) over the last year (12 months) were gathered. It was decided to use the Mann-Whitney-Wilcoxon test to determine if there has been a significant difference between the sales of the two branches.
>
> a. Provide the hypotheses for this test.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute the standard deviation $\sigma_T$.<br>
> d. The sum of the ranks for branch A was determined to be 184.5. Compute the test statistic Z.<br>
> e. Use $\alpha=0.05$ and test to determine if there is a significant difference in the populations of the sales of the two branches.

##### 詳解

> **回看投影片講義：** [MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)


1. **辨認題型：** 題目指定兩群 MWW，$H_0$ 為兩分店銷售分布相同，$H_a$ 為不同。
2. **選方法：** 使用[MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)。
3. **檢查假設：** 題目把兩分店當獨立樣本，且 $n_1=n_2=12\ge7$。若同月份有共同景氣衝擊，實務上應考慮配對方法；此處依原題指定作答。
4. **代入計算／推理：** $\mu_W=12(25)/2=150$，$\sigma_W=\sqrt{12(12)(25)/12}=\sqrt{300}=17.321$。上尾的連續性修正 $z=(184.5-0.5-150)/17.321=1.963$，雙尾 $p\approx0.0496$。
5. **解讀結論：** 在 0.05 水準勉強拒絕 $H_0$；A 的名次和偏高，顯示 A 銷售傾向較高。結論對連續性修正與獨立性設定敏感，不能忽略月份配對疑慮。

#### 計算題 4 <a id="exam-ch18-problem-4"></a>

##### 題目

> Independent random samples of the scores of 10 daily quizzes from day students and 15 quizzes from evening students were gathered. It was decided to use the Mann-Whitney-Wilcoxon test to determine if there is a significant difference between the scores of the two groups of students.
>
> a. Provide the hypotheses for this test.<br>
> b. Compute the mean $\mu_T$.<br>
> c. Compute the standard deviation $\sigma_T$.<br>
> d. The sum of the ranks for the day students was determined to be 184.5. Compute the test statistic Z.<br>
> e. Use $\alpha=0.05$ and test to determine if there is a significant difference in the populations of the scores of the two groups.

##### 詳解

> **回看投影片講義：** [MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)


1. **辨認題型：** 日間與夜間兩個獨立群的 MWW。
2. **選方法：** 使用[MWW 常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)，$H_0$ 為兩分布相同。
3. **檢查假設：** $n_1=10,n_2=15$ 都至少 7；兩群樣本需獨立。
4. **代入計算／推理：** $\mu_W=10(26)/2=130$，$\sigma_W=\sqrt{10(15)(26)/12}=18.028$；修正後 $z=(184.5-0.5-130)/18.028=2.995$，雙尾 $p\approx0.00274$。
5. **解讀結論：** $p<0.05$，拒絕兩群分布相同；日間生名次和偏高，分數傾向較高，但不直接等同平均分數差。

#### 計算題 5 <a id="exam-ch18-problem-5"></a>

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

> **回看投影片講義：** [MWW 名次和與常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)


1. **辨認題型：** 題目指定兩群獨立樣本 MWW。
2. **選方法：** 合併 24 筆資料，使用[MWW 名次和與常態近似](./course2-slides-handout.html#formula-ch18-mww-normal)。
3. **檢查假設：** 兩群各 12 筆；250 同值使用平均名次。月份可能形成天然配對，但依原題指定 MWW。
4. **代入計算／推理：** Branch A 的名次和 $W=148.5$，$\mu_W=150$，$\sigma_W=17.321$；修正後 $|z|=(|148.5-150|-0.5)/17.321=0.058$，雙尾 $p=0.9540$。tie-aware 軟體驗算 $p=0.95395$。
5. **解讀結論：** 不拒絕 $H_0$；兩分店名次高度混合，沒有足夠證據認為銷售分布不同。

#### 計算題 6 <a id="exam-ch18-problem-6"></a>

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

> **回看投影片講義：** [MWW](./course2-slides-handout.html#formula-ch18-mww-normal)


1. **辨認題型：** 日間與夜間學生是兩個獨立樣本。
2. **選方法：** 使用[MWW](./course2-slides-handout.html#formula-ch18-mww-normal)，檢查兩群年齡分布是否相同。
3. **檢查假設：** 兩群各 10 人且獨立；30 歲同值給平均名次。
4. **代入計算／推理：** 日間組 $W=74.5$，$\mu_W=105$，$\sigma_W=13.229$；連續性修正後 $z=-2.268$，雙尾 $p=0.02334$，tie-aware 驗算 $p=0.02329$。
5. **解讀結論：** $p<0.05$，拒絕兩群年齡分布相同；日間生名次和偏低，年齡傾向較小。

#### 計算題 7 <a id="exam-ch18-problem-7"></a>

##### 題目

> From the courthouse records, it is found that in 60 divorce cases, the filing for divorce was initiated by the wife 41 times. Using the sign test, test for a difference in filing between husband and wives. Let $\alpha=0.05$.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 60 件案件中由妻／夫提出的二元比例是否各半。
2. **選方法：** 使用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 各案件應可合理視為獨立，沒有平手；$n=60$ 可常態近似。
4. **代入計算／推理：** $\mu=30$，$\sigma=3.873$；修正後 $z=(40.5-30)/3.873=2.711$，雙尾近似 $p=0.00671$，精確二項 $p=0.00622$。
5. **解讀結論：** $p<0.05$，拒絕各半；妻子提出的比例顯著較高。法院紀錄是觀察資料，不能由此推論造成離婚的原因。

#### 計算題 8 <a id="exam-ch18-problem-8"></a>

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

> **回看投影片講義：** [Spearman 等級相關](./course2-slides-handout.html#formula-ch18-spearman)


1. **辨認題型：** 同五位候選人的兩套完整排名。
2. **選方法：** 使用[Spearman 等級相關](./course2-slides-handout.html#formula-ch18-spearman)，$H_0:\rho_s=0$。
3. **檢查假設：** 沒有同名次；但 $n=5<10$，不能套投影片的大樣本常態近似作正式決策。
4. **代入計算／推理：** $\sum d_i^2=10$，$r_s=1-6(10)/[5(25-1)]=0.500$。窮舉 $5!=120$ 種排列，雙尾精確 $p=0.450$。
5. **解讀結論：** 不拒絕 $H_0$；樣本呈中度正向排序，但五人太少，沒有足夠證據認定母體排序相關。

#### 計算題 9 <a id="exam-ch18-problem-9"></a>

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

> **回看投影片講義：** [Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)


1. **辨認題型：** 同一人課前／課後，是配對數值；有效表示課後較高。
2. **選方法：** 使用[Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)，令 $d=After-Before$，$H_a$ 為位置差大於 0。
3. **檢查假設：** D 的零差刪除，剩 $n=5$；需假設非零差近似對稱。小樣本使用精確／排列概念。
4. **代入計算／推理：** 差值為 2、16、-2、0、4、-2；平均名次後 $T^+=11,T^-=4$。枚舉五個非零名次的 $2^5=32$ 種正負配置，一尾精確 $p=0.250$。
5. **解讀結論：** $p>0.05$，沒有足夠證據認為研習使分數整體提高；少數大幅進步不足以壓過小樣本不確定性。

#### 計算題 10 <a id="exam-ch18-problem-10"></a>

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

> **回看投影片講義：** [精確二項符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 15 個二元偏好的小樣本符號檢定。
2. **選方法：** 使用[精確二項符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)，$H_0:p=0.5$。
3. **檢查假設：** 12 個正號、3 個負號，沒有平手；每人應獨立。
4. **代入計算／推理：** 雙尾 $p=2P(X\ge12)=2P(X\le3)=0.035156$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；正號較多，樣本支持進口車較受偏好。

#### 計算題 11 <a id="exam-ch18-problem-11"></a>

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

> **回看投影片講義：** [精確二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 20 人兩候選人偏好的符號檢定。
2. **選方法：** 使用[精確二項模型](./course2-slides-handout.html#formula-ch18-sign-binomial)，$H_0:p=0.5$。
3. **檢查假設：** 14 個正號、6 個負號；投影片在 $n\le20$ 使用 exact binomial。
4. **代入計算／推理：** 雙尾 $p=2P(X\ge14)=0.115318$。
5. **解讀結論：** $p>0.05$，不能拒絕各半；雖民主黨候選人在樣本中較多，證據尚不足以推廣到母體。

#### 計算題 12 <a id="exam-ch18-problem-12"></a>

##### 題目

> In a sample of 120 people, 50 indicated that they prefer domestic automobiles, 60 said they prefer foreign-made cars, and 10 indicated no difference in their preference. At a 0.05 level of significance, determine if there is evidence of a significant difference in the preferences for the two makes of automobiles.

##### 詳解

> **回看投影片講義：** [符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)


1. **辨認題型：** 兩車種偏好的大樣本符號檢定。
2. **選方法：** 使用[符號檢定常態近似](./course2-slides-handout.html#formula-ch18-sign-normal)。
3. **檢查假設：** 刪除 10 位無差異者，$n=110$；正負期望各 55。
4. **代入計算／推理：** $\sigma=\sqrt{27.5}=5.244$；修正後 $|z|=(|60-55|-0.5)/5.244=0.858$，雙尾 $p=0.3908$；精確 p $=0.3909$。
5. **解讀結論：** 不拒絕 $H_0$；沒有足夠證據認為國產與進口車偏好比例不同。

#### 計算題 13 <a id="exam-ch18-problem-13"></a>

##### 題目

> In a sample of 300 shoppers, 160 indicated they prefer fluoride toothpaste, 120 favored nonfluoride, and 20 were indifferent. At a 0.05 level of significance, test for a difference in the preference for the two kinds of toothpaste.

##### 詳解

> **回看投影片講義：** [大樣本符號檢定](./course2-slides-handout.html#formula-ch18-sign-normal)


1. **辨認題型：** 含平手的兩種牙膏偏好。
2. **選方法：** 使用[大樣本符號檢定](./course2-slides-handout.html#formula-ch18-sign-normal)。
3. **檢查假設：** 刪除 20 位 indifferent，$n=280$，$\mu=140$。
4. **代入計算／推理：** $\sigma=\sqrt{70}=8.367$；修正後 $z=(159.5-140)/8.367=2.331$，雙尾 $p=0.01977$；精確 p $=0.01961$。
5. **解讀結論：** $p<0.05$，拒絕偏好各半；含氟牙膏在樣本中較受偏好。

#### 計算題 14 <a id="exam-ch18-problem-14"></a>

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

> **回看投影片講義：** [Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)


1. **辨認題型：** 同十人的前後分數，問訓練是否使分數提高。
2. **選方法：** 使用[Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)，令 $d=After-Before$，作右尾檢定。
3. **檢查假設：** 第 3 人零差刪除後 $n=9$；非零差需近似對稱。樣本小，使用精確／排列處理。
4. **代入計算／推理：** $T^+=36.5,T^-=8.5$；枚舉九個非零名次的 $2^9=512$ 種正負配置，一尾精確 $p=0.05469$。
5. **解讀結論：** $p$ 略高於 0.05，不能拒絕 $H_0$；樣本有進步方向，但證據剛好未達門檻。若改用某些 ties 的大樣本近似可能跨過 0.05，因此應優先報告本題小樣本精確結果與個人差值。

#### 計算題 15 <a id="exam-ch18-problem-15"></a>

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

> **回看投影片講義：** [Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)


1. **辨認題型：** 同十位駕駛測兩車，是配對數值比較。
2. **選方法：** 使用[Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)，令 $d=A-B$，作雙尾比較。
3. **檢查假設：** 十個差值都非零且全為正；需假設配對差近似對稱。
4. **代入計算／推理：** $T^+=55,T^-=0$；精確雙尾 $p=2/2^{10}=0.001953$。
5. **解讀結論：** $p<0.05$，兩車表現有差；所有駕駛下 A 都跑得更遠，方向支持 Model A 的每加侖里程較高。

#### 計算題 16 <a id="exam-ch18-problem-16"></a>

##### 題目

> A PTA group wishes to determine whether a barrage of letters sent to the local station has reduced the amount of violence broadcast between the hours of 4 P.M. and 9 P.M. The results of a survey of viewers are given here.

| Response | Number of Respondents |
|---|---:|
| More Violence | 4 |
| Less Violence | 11 |
| No Change | 6 |

> Carry out a sign test to determine whether or not the letters were effective in reducing the amount of violence during the 4 to 9 p.m. period. Use a .05 level of significance. Be sure to state the null and alternative hypotheses.

##### 詳解

> **回看投影片講義：** [精確符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 觀眾認為暴力增加／減少的方向資料，問是否減少，是單尾符號檢定。
2. **選方法：** 使用[精確符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)。令正號為 Less Violence，$H_0:p\le0.5$、$H_a:p>0.5$。
3. **檢查假設：** 6 位 No Change 刪除，有效 $n=15$；受訪者意見需近似獨立。
4. **代入計算／推理：** 觀察正號 11 個，一尾 $p=P(X\ge11)=0.05923$。
5. **解讀結論：** $p>0.05$，不能拒絕 $H_0$；樣本多數認為暴力減少，但證據尚未達 5% 門檻，不能宣稱信件有效。

#### 計算題 17 <a id="exam-ch18-problem-17"></a>

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

> **回看投影片講義：** [Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)


1. **辨認題型：** 同一批工人的新舊機器產量，問新機器是否提高，是配對右尾檢定。
2. **選方法：** 使用[Wilcoxon signed-rank](./course2-slides-handout.html#formula-ch18-signed-rank)，令 $d=New-Old$。
3. **檢查假設：** Workers 7、15 零差刪除，$n=13$；差值分布需近似對稱。
4. **代入計算／推理：** 平均同名次後 $T^+=53.5,T^-=37.5$；枚舉 $2^{13}=8,192$ 種正負配置，一尾精確 $p=0.29993$。
5. **解讀結論：** $p>0.05$，沒有足夠證據認為新機器提升產量；正負差與大名次沒有一致朝增加方向集中。

#### 計算題 18 <a id="exam-ch18-problem-18"></a>

##### 題目

> The president of a company wants to see if the new anti-smoking campaign is having any influence on his employees. A sample of 100 employees who smoked prior to the campaign is taken. Thirty-six employees said they smoked less, 15 employees said they smoked more, and 49 employees said there was no change.
>
> a. State the null and alternative hypotheses.<br>
> b. Test the null hypothesis at the 1% level of significance.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 抽菸變少／變多的方向是否失衡；`any influence` 表示雙尾。
2. **選方法：** 使用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)，令正號為 smoked less，$H_0:p=0.5$、$H_a:p\ne0.5$。
3. **檢查假設：** 刪除 49 位 no change，$n=51$；各員工回應應近似獨立。
4. **代入計算／推理：** $\mu=25.5$，$\sigma=3.571$；修正後 $z=(35.5-25.5)/3.571=2.801$，雙尾近似 $p=0.00510$，精確 p $=0.00460$。
5. **解讀結論：** $p<0.01$，拒絕無影響；方向顯示回報抽得較少者較多。這是自陳的前後變化，不能單靠檢定排除其他同期因素。

#### 計算題 19 <a id="exam-ch18-problem-19"></a>

##### 題目

> It is believed that the median age of college students is 21 years. A sample of 80 college students is taken. Thirty of the students were under 21, 45 of the students were over 21, and 10 were 21 years old.
>
> a. State the null and alternative hypotheses.<br>
> b. Test the null hypothesis at the 1% level of significance.

##### 詳解

> **回看投影片講義：** [符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)


1. **辨認題型：** 母體中位數 21 歲的雙尾符號檢定。
2. **選方法：** 使用[符號檢定](./course2-slides-handout.html#formula-ch18-sign-binomial)，$H_0:\text{Median}=21$、$H_a:\text{Median}\ne21$。
3. **檢查假設：** 原題有來源疑義：30 + 45 + 10 = 85，與宣稱的樣本 80 不一致。題幹無法同時全部成立，因此不能無條件給唯一答案。
4. **代入計算／推理：** 若忠實採三個分類次數，刪除 10 位平手後 $n=75$，正號 45、負號 30；精確雙尾 $p=0.10534$，連續性修正近似 $p=0.10597$。
5. **解讀結論：** 在上述可驗算處理下 $p>0.01$，不拒絕中位數 21 歲；但正式作答應先向出題者確認總樣本或其中一個分類數，不能把不一致資料悄悄修掉。

#### 計算題 20 <a id="exam-ch18-problem-20"></a>

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

> **回看投影片講義：** [MWW](./course2-slides-handout.html#formula-ch18-mww-normal)


1. **辨認題型：** 日班與夜班是兩個獨立群，問生產力分布是否不同。
2. **選方法：** 使用[MWW](./course2-slides-handout.html#formula-ch18-mww-normal)，$H_0$ 為兩母體分布相同，$H_a$ 為不同。
3. **檢查假設：** $n_1=10,n_2=11$ 都至少 7；兩班工人彼此獨立；31、39 同值用平均名次。
4. **代入計算／推理：** 日班名次和 $W=111$，$\mu_W=110$，$\sigma_W=14.201$；修正後 $|z|=0.035$，雙尾 $p=0.9719$，tie-aware 驗算一致。
5. **解讀結論：** 不拒絕 $H_0$；兩班高低名次幾乎完全混合，沒有分布差異證據。

#### 計算題 21 <a id="exam-ch18-problem-21"></a>

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

> **回看投影片講義：** [Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)


1. **辨認題型：** 三個獨立年齡群的銷售分布比較。
2. **選方法：** 使用[Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同，$H_a$ 為至少一群不同。
3. **檢查假設：** 樣本數為 6、7、7，均至少 5；各業務員獨立；同值採平均名次並做 ties correction。
4. **代入計算／推理：** 名次和為 40、69、101；未修正 $H=5.688$，ties-corrected $H=5.697$，$df=2$，$p=0.05793$。
5. **解讀結論：** $p>0.05$，不能拒絕三群分布相同。45 歲以上名次偏高是樣本線索，但尚未達顯著，更不能推論年齡造成銷售差異。

#### 計算題 22 <a id="exam-ch18-problem-22"></a>

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

> **回看投影片講義：** [Spearman 係數與常態檢定](./course2-slides-handout.html#formula-ch18-spearman-test)


1. **辨認題型：** 同 12 人的兩套完整排名。
2. **選方法：** 使用[Spearman 係數與常態檢定](./course2-slides-handout.html#formula-ch18-spearman-test)，$H_0:\rho_s=0$、$H_a:\rho_s\ne0$。
3. **檢查假設：** 無 ties，$n=12\ge10$，符合投影片近似門檻。
4. **代入計算／推理：** $\sum d_i^2=38$，$r_s=1-6(38)/[12(12^2-1)]=0.8671$；$z=r_s\sqrt{11}=2.876$，雙尾 $p=0.00403$。
5. **解讀結論：** $p<0.02$，拒絕零等級相關；兩位教授的排序高度同向，但並非完全一致。

#### 計算題 23 <a id="exam-ch18-problem-23"></a>

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

> **回看投影片講義：** [Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)


1. **辨認題型：** 三個獨立主修群的考試分數比較。
2. **選方法：** 使用[Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同。
3. **檢查假設：** 群大小 5、6、5，符合投影片每群至少 5；學生獨立；60、70、80 等 ties 要平均名次並修正。
4. **代入計算／推理：** 名次和 38、56、42；未修正 $H=0.3647$，ties-corrected $H=0.3680$，$df=2$，$p=0.8320$。
5. **解讀結論：** 不拒絕 $H_0$；三群名次高度混合，沒有足夠證據認為表現分布不同。

#### 計算題 24 <a id="exam-ch18-problem-24"></a>

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

> **回看投影片講義：** [Spearman 等級相關檢定](./course2-slides-handout.html#formula-ch18-spearman-test)


1. **辨認題型：** 同 12 位教授的兩套排名是否一致。
2. **選方法：** 使用[Spearman 等級相關檢定](./course2-slides-handout.html#formula-ch18-spearman-test)。
3. **檢查假設：** 兩欄都是 1–12 的完整排名，無 ties；$n=12\ge10$。
4. **代入計算／推理：** $\sum d_i^2=294$，$r_s=-0.02797$；$z=-0.0928$，雙尾 $p=0.9261$。
5. **解讀結論：** 不拒絕 $\rho_s=0$；兩組學生的排序幾乎沒有單調一致性。這不是證明兩組對每位教授都持相反看法。

#### 計算題 25 <a id="exam-ch18-problem-25"></a>

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

> **回看投影片講義：** [Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)


1. **辨認題型：** 八輛車的兩套完整排名。
2. **選方法：** 使用[Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)，檢查 $H_0:\rho_s=0$。
3. **檢查假設：** 無 ties；$n=8<10$，正式決策用精確排列，不用投影片的大樣本 z。
4. **代入計算／推理：** $\sum d_i^2=78$，$r_s=1-6(78)/[8(8^2-1)]=0.07143$；窮舉 $8!=40,320$ 種排列得雙尾精確 $p=0.8820$。
5. **解讀結論：** 不拒絕零相關；兩人的排序幾乎沒有同向單調關聯。

#### 計算題 26 <a id="exam-ch18-problem-26"></a>

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

> **回看投影片講義：** [Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)


1. **辨認題型：** 八項活動在住宿生與非住宿生中的兩套排名。
2. **選方法：** 使用[Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)。
3. **檢查假設：** 無 ties；$n=8<10$，以精確排列 p 值作決策。
4. **代入計算／推理：** $\sum d_i^2=30$，$r_s=0.64286$；精確雙尾 $p=0.09618$。若誤用常態近似會得約 0.089，決策仍相同。
5. **解讀結論：** $p>0.05$，不能認定母體排序相關；樣本有中度正向一致，但八項活動的證據不足。

#### 計算題 27 <a id="exam-ch18-problem-27"></a>

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

> **回看投影片講義：** [Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)


1. **辨認題型：** 五位候選人的兩套排名。
2. **選方法：** 使用[Spearman 係數](./course2-slides-handout.html#formula-ch18-spearman)。
3. **檢查假設：** 無 ties；$n=5<10$，使用精確排列。
4. **代入計算／推理：** $\sum d_i^2=24$，$r_s=-0.200$；$5!=120$ 種排列的雙尾精確 $p=0.7833$。
5. **解讀結論：** 不拒絕零相關；觀察到的輕微反向排序很可能只是小樣本波動。

#### 計算題 28 <a id="exam-ch18-problem-28"></a>

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

> **回看投影片講義：** [Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)


1. **辨認題型：** 三所大學的獨立分數樣本；原題雖寫 average scores，但指定 Kruskal-Wallis，檢定的是分布／名次位置。
2. **選方法：** 使用[Kruskal-Wallis](./course2-slides-handout.html#formula-ch18-kruskal-wallis)，$H_0$ 為三群分布相同。
3. **檢查假設：** 樣本獨立且隨機；群大小為 5、4、6。Central 只有 4 人，未達投影片每群 $n_i\ge5$ 的卡方近似門檻，因此另做精確隨機化驗算。
4. **代入計算／推理：** 名次和為 37.5、37、45.5；未修正 $H=0.4271$，ties-corrected $H=0.4278$。卡方近似 $p=0.8074$；枚舉所有保持 5／4／6 群大小的標籤分配，精確右尾 $p=0.8234$。
5. **解讀結論：** 兩種算法都遠大於 0.01，不拒絕 $H_0$；沒有足夠證據認為三校分數分布不同。這不是證明三校平均數完全相等。
