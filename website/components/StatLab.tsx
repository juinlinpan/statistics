"use client";

import { Check, Play, RefreshCw, Sparkles } from "lucide-react";
import { type ReactNode, useMemo, useState } from "react";

type CycleProps = {
  title: string;
  mission: string;
  question: string;
  options: string[];
  correct: number;
  feedback: string[];
  children: ReactNode;
};

function LearnCycle({ title, mission, question, options, correct, feedback, children }: CycleProps) {
  const [answer, setAnswer] = useState<number>();
  const [checked, setChecked] = useState(false);

  return (
    <section className="stat-lab">
      <header className="lab-heading">
        <span className="section-kicker">互動實驗</span>
        <h2>{title}</h2>
        <p>{mission}</p>
      </header>
      <div className="lab-cycle">
        <section className="lab-predict" aria-labelledby="prediction-title">
          <div className="lab-step-label"><span>1</span>先預測</div>
          <h3 id="prediction-title">{question}</h3>
          <div className="prediction-options">
            {options.map((option, index) => (
              <button
                key={option}
                className={answer === index ? "selected" : ""}
                aria-pressed={answer === index}
                onClick={() => { setAnswer(index); setChecked(false); }}
              >
                <span>{String.fromCharCode(65 + index)}</span>{option}
              </button>
            ))}
          </div>
          {!checked ? (
            <button className="lab-action" disabled={answer === undefined} onClick={() => setChecked(true)}>鎖定預測</button>
          ) : (
            <div className={answer === correct ? "prediction-feedback correct" : "prediction-feedback incorrect"}>
              {answer === correct ? <Check size={18} /> : <Sparkles size={18} />}
              <p><strong>{answer === correct ? "判斷正確。" : "這正是常見的直覺陷阱。"}</strong>{feedback[answer ?? 0]}</p>
            </div>
          )}
        </section>
        {checked && (
          <section className="lab-experiment">
            <div className="lab-step-label"><span>2</span>動手驗證</div>
            {children}
          </section>
        )}
      </div>
    </section>
  );
}

function seeded(seed: number) {
  const x = Math.sin(seed * 999.91) * 43758.5453;
  return x - Math.floor(x);
}

function mean(values: number[]) { return values.reduce((sum, value) => sum + value, 0) / values.length; }
function median(values: number[]) {
  const sorted = [...values].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
}

function DescriptiveLab() {
  const original = [8, 10, 12, 12, 15, 18, 20, 22, 25, 58];
  const [includeOutlier, setIncludeOutlier] = useState(true);
  const values = includeOutlier ? original : original.slice(0, -1);
  return (
    <LearnCycle
      title="一個極端值，會把誰拉得更遠？"
      mission="不要只讀『平均數怕離群值』。先猜，再親手拿掉 58 分鐘，直接比較兩個摘要量移動多少。"
      question="拿掉 58 分鐘後，哪個摘要量的變化會比較大？"
      options={["平均數", "中位數", "兩者一樣"]}
      correct={0}
      feedback={["平均數使用每一個數值，58 的距離會完整進入計算。", "中位數只看排序後的中央位置，對單一極端值較不敏感。", "兩者都可能改變，但移動幅度不會一樣。"]}
    >
      <div className="experiment-controls">
        <button className={includeOutlier ? "active" : ""} onClick={() => setIncludeOutlier(true)}>放回 58</button>
        <button className={!includeOutlier ? "active" : ""} onClick={() => setIncludeOutlier(false)}>拿掉 58</button>
      </div>
      <div className="number-strip" aria-label={`目前資料：${values.join("、")}`}>
        {original.map((value) => <span key={value} className={!includeOutlier && value === 58 ? "removed" : value === 58 ? "extreme" : ""}>{value}</span>)}
      </div>
      <div className="compare-measures">
        <div><span>平均數</span><strong>{mean(values).toFixed(1)}</strong><i style={{ width: `${mean(values) * 1.45}%` }} /></div>
        <div><span>中位數</span><strong>{median(values).toFixed(1)}</strong><i style={{ width: `${median(values) * 1.45}%` }} /></div>
      </div>
      <p className="experiment-takeaway"><strong>看移動量：</strong>平均數由 20.0 變成 15.8，移動 4.2；中位數只由 16.5 變成 15.0，移動 1.5。這就是「抗拒性」的具體意思。</p>
    </LearnCycle>
  );
}

function SamplingLab() {
  const [method, setMethod] = useState<"convenience" | "stratified">("convenience");
  const [round, setRound] = useState(0);
  const nightWorkers = 10;
  const sampleNight = method === "convenience" ? (round % 3) : 5;
  const sampleSize = method === "convenience" ? 20 : 20;
  const estimate = sampleNight / sampleSize;
  return (
    <LearnCycle
      title="樣本變大，不代表偏誤會消失"
      mission="母體有 40 人，其中 10 位是夜班。比較只在白天攔人，與按班別分層抽樣的結果。"
      question="哪個方法比較可能估到真正的夜班比例 25%？"
      options={["白天方便抽 20 人", "按班別分層抽 20 人", "只要樣本一樣大就沒差"]}
      correct={1}
      feedback={["白天攔人會系統性漏掉夜班，這是偏誤，不是運氣差。", "分層讓夜班與日班都按母體比例進入樣本。", "樣本數控制機會誤差；抽樣規則決定是否有系統性偏誤。"]}
    >
      <div className="population-grid" aria-label="40 人母體，10 位夜班">
        {Array.from({ length: 40 }, (_, index) => <span key={index} className={index >= 30 ? "night" : "day"}>{index >= 30 ? "夜" : "日"}</span>)}
      </div>
      <div className="experiment-controls">
        <button className={method === "convenience" ? "active" : ""} onClick={() => setMethod("convenience")}>白天方便抽樣</button>
        <button className={method === "stratified" ? "active" : ""} onClick={() => setMethod("stratified")}>按班別分層</button>
        <button onClick={() => setRound((value) => value + 1)}><RefreshCw size={15} />再抽一次</button>
      </div>
      <div className="sample-result">
        <div><span>母體真值</span><strong>25%</strong></div><div><span>這次樣本</span><strong>{(estimate * 100).toFixed(0)}%</strong></div><div><span>誤差</span><strong>{Math.abs(estimate - .25) === 0 ? "0" : `${(Math.abs(estimate - .25) * 100).toFixed(0)}%`}</strong></div>
      </div>
      <p className="experiment-takeaway">{method === "convenience" ? "方便抽樣每次都幾乎看不到夜班；重抽很多次也只是穩定地得到錯答案。" : "分層抽樣先確保兩個班別都被代表，再依母體比例合併，估計才有機會對準母體。"}</p>
    </LearnCycle>
  );
}

function ProbabilityLab() {
  const [round, setRound] = useState(1);
  const [groupsWithSuccess, setGroupsWithSuccess] = useState(0);
  const outcomes = Array.from({ length: 10 }, (_, index) => seeded(round * 31 + index) < .1);
  const hasSuccess = outcomes.some(Boolean);
  const run = () => { setGroupsWithSuccess((count) => count + (hasSuccess ? 1 : 0)); setRound((value) => value + 1); };
  return (
    <LearnCycle
      title="『至少一次』為什麼不能直接乘 10？"
      mission="每次中獎機率 10%，連續參加 10 次。先猜至少中一次的機率，再用互補事件和模擬核對。"
      question="至少中一次的機率最接近哪一個？"
      options={["10%", "65%", "100%"]}
      correct={1}
      feedback={["10% 只是一回合的機率；10 次會累積多個中獎機會。", "先算 10 次都沒中：0.9¹⁰，再用 1 減掉，約 65.1%。", "10 × 10% 不是合法的『至少一次』算法，事件可能重疊，也不保證一定發生。"]}
    >
      <div className="trial-row" aria-label="十次模擬結果">
        {outcomes.map((success, index) => <span key={index} className={success ? "success" : "miss"}>{success ? "中" : "—"}</span>)}
      </div>
      <button className="lab-action" onClick={run}><Play size={15} />再跑一組 10 次</button>
      <div className="formula-story"><span>10 次都沒中</span><strong>0.9¹⁰ = 34.9%</strong><i>→</i><span>至少中一次</span><strong>1 − 0.9¹⁰ = 65.1%</strong></div>
      <p className="experiment-takeaway">你已跑 {round} 組，其中 {groupsWithSuccess + (hasSuccess ? 1 : 0)} 組至少中一次。模擬比例會抖動；互補公式給的是長期理論機率。</p>
    </LearnCycle>
  );
}

function BinomialLab() {
  const [round, setRound] = useState(2);
  const outcomes = Array.from({ length: 20 }, (_, index) => seeded(round * 47 + index) < .3);
  const successes = outcomes.filter(Boolean).length;
  return (
    <LearnCycle
      title="先判斷能不能用二項分配，再開始算"
      mission="二項分配不是看到『次數』就能用；四個條件缺一個，公式就失去對應的隨機機制。"
      question="哪個情境符合二項設定？"
      options={["記錄 20 位顧客各自的消費金額", "同一機器獨立檢查 20 件產品是否瑕疵，瑕疵率固定 30%", "一直投球直到命中 5 次"]}
      correct={1}
      feedback={["結果不是成功／失敗兩類，而是多種金額。", "固定 20 次、兩種結果、近似獨立、成功率固定，四個條件都有。", "試驗次數不是事先固定；停止規則取決於成功次數。"]}
    >
      <div className="condition-list"><span><Check />固定 20 次</span><span><Check />瑕疵／正常</span><span><Check />近似獨立</span><span><Check />p = 0.30 固定</span></div>
      <div className="trial-row compact" aria-label={`20 件中 ${successes} 件瑕疵`}>
        {outcomes.map((success, index) => <span key={index} className={success ? "success" : "miss"}>{success ? "瑕" : "正"}</span>)}
      </div>
      <div className="experiment-controls"><button onClick={() => setRound((value) => value + 1)}><RefreshCw size={15} />再檢查 20 件</button></div>
      <p className="experiment-takeaway">這次有 <strong>{successes} 件瑕疵</strong>。$X$ 不是單件是否瑕疵，而是固定 20 件裡的瑕疵總數；多次重做後，中心會靠近 $np=6$。</p>
    </LearnCycle>
  );
}

function CLTLab() {
  const [n, setN] = useState(2);
  const [round, setRound] = useState(1);
  const means = useMemo(() => Array.from({ length: 120 }, (_, sampleIndex) => {
    const sample = Array.from({ length: n }, (_, j) => -Math.log(Math.max(.001, seeded(round * 10000 + sampleIndex * 101 + j))));
    return mean(sample);
  }), [n, round]);
  const bins = Array.from({ length: 12 }, (_, bin) => means.filter((value) => value >= bin * .2 && value < (bin + 1) * .2).length);
  const max = Math.max(...bins);
  return (
    <LearnCycle
      title="CLT 說的是『樣本平均數』的形狀"
      mission="母體故意做成強烈右偏。每次重複抽樣 120 次，比較 n=2、10、30 時樣本平均數的分布。"
      question="樣本數增大時，樣本平均數的分布會怎樣？"
      options={["更右偏、更分散", "形狀與寬度都不變", "更接近鐘形，而且更集中"]}
      correct={2}
      feedback={["個別資料仍右偏，但平均數會把極端值攤薄，標準誤也按 √n 縮小。", "抽樣分配會隨 n 改變；這正是 CLT 與平方根律描述的事情。", "形狀逐漸接近常態，寬度則由 σ/√n 控制。"]}
    >
      <div className="experiment-controls"><button className={n === 2 ? "active" : ""} onClick={() => setN(2)}>n = 2</button><button className={n === 10 ? "active" : ""} onClick={() => setN(10)}>n = 10</button><button className={n === 30 ? "active" : ""} onClick={() => setN(30)}>n = 30</button><button onClick={() => setRound((value) => value + 1)}><RefreshCw size={15} />重抽 120 次</button></div>
      <div className="histogram" role="img" aria-label={`樣本數 ${n} 的 120 個樣本平均數直方圖`}>
        {bins.map((count, index) => <div key={index}><i style={{ height: `${(count / max) * 100}%` }} /><span>{index % 2 === 0 ? (index * .2).toFixed(1) : ""}</span></div>)}
      </div>
      <p className="experiment-takeaway"><strong>現在 n={n}：</strong>120 個平均數的標準差約 {Math.sqrt(means.reduce((sum, value) => sum + (value - mean(means)) ** 2, 0) / 119).toFixed(2)}。切換 n 時，不只看鐘形，也要看整個分布是否往中心收窄。</p>
    </LearnCycle>
  );
}

function regression(values: { x: number; y: number }[]) {
  const mx = mean(values.map((point) => point.x)); const my = mean(values.map((point) => point.y));
  const slope = values.reduce((sum, point) => sum + (point.x - mx) * (point.y - my), 0) / values.reduce((sum, point) => sum + (point.x - mx) ** 2, 0);
  return { slope, intercept: my - slope * mx };
}

function RegressionLab() {
  const base = [{x:1,y:2},{x:2,y:3},{x:3,y:3.5},{x:4,y:5},{x:5,y:5.5},{x:6,y:7}];
  const presets = [{ label: "中央離群點", point: {x:3.5,y:9} }, { label: "高槓桿、在線上", point: {x:9,y:10} }, { label: "高槓桿＋大殘差", point: {x:9,y:2} }];
  const [preset, setPreset] = useState(0);
  const points = [...base, presets[preset].point];
  const line = regression(points);
  const y0 = line.intercept; const y10 = line.intercept + line.slope * 10;
  const angle = Math.atan2(-(y10 - y0) * 24, 520) * 180 / Math.PI;
  const length = Math.sqrt(520 ** 2 + ((y10 - y0) * 24) ** 2);
  return (
    <LearnCycle
      title="離群、槓桿、影響力不是同一件事"
      mission="把三種特殊點放進同一組資料。觀察哪一種最能改變最小平方法的斜率。"
      question="哪一個點最可能大幅拉動迴歸線？"
      options={["只在 y 方向離群，但 x 靠近中心", "x 很遠，但剛好落在線上", "x 很遠，而且也偏離原趨勢"]}
      correct={2}
      feedback={["它殘差大，但 x 靠近中心，對斜率的槓桿有限。", "它槓桿高，卻支持原本趨勢，未必大幅改變斜率。", "它同時有高槓桿與大殘差，刪除前後的迴歸線最可能明顯不同。"]}
    >
      <div className="experiment-controls">{presets.map((item, index) => <button key={item.label} className={preset === index ? "active" : ""} onClick={() => setPreset(index)}>{item.label}</button>)}</div>
      <div className="scatter-plot" role="img" aria-label={`${presets[preset].label}，迴歸斜率 ${line.slope.toFixed(2)}`}>
        <i className="fit-line" style={{ width: length, transform: `rotate(${angle}deg)`, left: 22, bottom: 22 + y0 * 24 }} />
        {points.map((point, index) => <span key={index} className={index === points.length - 1 ? "special" : ""} style={{ left: `${point.x * 9 + 3}%`, bottom: `${point.y * 8 + 5}%` }}>{index === points.length - 1 ? "特殊點" : ""}</span>)}
      </div>
      <p className="experiment-takeaway">目前斜率 = <strong>{line.slope.toFixed(2)}</strong>。判斷影響力的關鍵不是只看點「遠不遠」，而是看它的位置是否讓整條 fitted line 明顯改變。</p>
    </LearnCycle>
  );
}

function ConfidenceLab() {
  const [level, setLevel] = useState(95);
  const [round, setRound] = useState(1);
  const z = level === 80 ? 1.282 : level === 95 ? 1.96 : 2.576;
  const intervals = Array.from({ length: 20 }, (_, index) => {
    const estimate = Array.from({length: 6}, (_, j) => seeded(round * 500 + index * 17 + j)).reduce((a,b)=>a+b,0) - 3;
    return { estimate, low: estimate - z, high: estimate + z };
  });
  const covers = intervals.filter((item) => item.low <= 0 && item.high >= 0).length;
  return (
    <LearnCycle
      title="信賴區間的 95% 是一套程序的涵蓋率"
      mission="母體平均數固定在 0。一次產生 20 個獨立樣本的區間，數一數哪些區間真的蓋住 0。"
      question="同一批樣本改用更高信心水準，區間通常會怎樣？"
      options={["變窄，涵蓋更多", "變寬，涵蓋更多", "寬度不變"]}
      correct={1}
      feedback={["想提高涵蓋率，必須把網撒得更寬，不是更窄。", "臨界值變大，所以每條區間更寬，長期涵蓋率也更高。", "標準誤相同時，臨界值仍會隨信心水準改變。"]}
    >
      <div className="experiment-controls"><button className={level === 80 ? "active" : ""} onClick={() => setLevel(80)}>80%</button><button className={level === 95 ? "active" : ""} onClick={() => setLevel(95)}>95%</button><button className={level === 99 ? "active" : ""} onClick={() => setLevel(99)}>99%</button><button onClick={() => setRound((value) => value + 1)}><RefreshCw size={15} />換 20 個樣本</button></div>
      <div className="interval-plot" role="img" aria-label={`${level}% 信賴區間，20 條中 ${covers} 條涵蓋真值`}>
        <i className="truth-line" />
        {intervals.map((item, index) => <span key={index} className={item.low <= 0 && item.high >= 0 ? "covers" : "misses"} style={{ left: `${((item.low + 5) / 10) * 100}%`, width: `${((item.high - item.low) / 10) * 100}%`, top: `${index * 5}%` }} />)}
      </div>
      <p className="experiment-takeaway">這一批涵蓋 <strong>{covers}/20</strong>。單一批次不必剛好等於 {level}%；信心水準描述的是這套程序在無限次重複抽樣下的長期表現。</p>
    </LearnCycle>
  );
}

const combinations = [1,8,28,56,70,56,28,8,1];
function SignificanceLab() {
  const [observed, setObserved] = useState(7);
  const tail = combinations.slice(observed).reduce((a,b)=>a+b,0) / 256;
  return (
    <LearnCycle
      title="p 值是在 H₀ 世界裡量『這麼極端有多罕見』"
      mission="假設每次都只是公平硬幣，做 8 次。把觀察結果從 5 次正面推到 8 次正面，看右尾面積如何縮小。"
      question="p 值最正確的意思是哪一個？"
      options={["H₀ 為真的機率", "若 H₀ 為真，得到目前或更極端資料的機率", "研究結果重要的程度"]}
      correct={1}
      feedback={["頻率論 p 值不把機率直接指派給固定的 H₀。", "p 值從 H₀ 出發，量資料在這個世界裡有多不尋常。", "統計顯著與效果大小、實務重要性是不同問題。"]}
    >
      <div className="experiment-controls">{[5,7,8].map((value) => <button key={value} className={observed === value ? "active" : ""} onClick={() => setObserved(value)}>觀察到 {value}/8</button>)}</div>
      <div className="tail-bars" role="img" aria-label={`8 次公平硬幣的二項分配，${observed} 次以上的右尾機率 ${tail.toFixed(4)}`}>
        {combinations.map((count, k) => <div key={k} className={k >= observed ? "tail" : ""}><i style={{ height: `${count}%` }} /><span>{k}</span></div>)}
      </div>
      <p className="experiment-takeaway">公平硬幣的 256 種等可能序列中，有 <strong>{combinations.slice(observed).reduce((a,b)=>a+b,0)} 種</strong>得到 {observed} 次以上正面，所以單尾 p = {tail.toFixed(4)}。小 p 代表資料與 H₀ 不相容，不代表 H₀「被證明為假」。</p>
    </LearnCycle>
  );
}

function BootstrapLab() {
  const source = [3,4,4,5,12];
  const [round, setRound] = useState(1);
  const [replicates, setReplicates] = useState<number[]>([]);
  const drawSample = (seed: number) => Array.from({length: 5}, (_, index) => source[Math.floor(seeded(seed * 73 + index) * source.length)]);
  const current = drawSample(round);
  const draw = (count: number) => {
    const next = Array.from({length: count}, (_, index) => median(drawSample(round + index)));
    setReplicates((items) => [...items, ...next].slice(-200)); setRound((value) => value + count);
  };
  const counts = [3,4,5,12].map((value) => replicates.filter((item) => item === value).length);
  const max = Math.max(1, ...counts);
  return (
    <LearnCycle
      title="Bootstrap 是從原樣本『有放回』地重抽"
      mission="原樣本只有 3、4、4、5、12。先看一個 bootstrap 樣本怎麼出現重複值，再累積中位數的重抽分配。"
      question="為什麼 bootstrap 樣本裡可以重複出現同一筆值？"
      options={["因為抽完會放回，下一次仍可能抽到它", "因為要把樣本排序", "因為重複值要自動刪掉"]}
      correct={0}
      feedback={["有放回抽樣讓每一抽都從同一個經驗分布出發。", "排序只改變順序，不會創造 bootstrap 的隨機性。", "重複是重抽機制的必要結果，不能刪掉。"]}
    >
      <div className="bootstrap-source"><span>原樣本</span>{source.map((value,index)=><i key={index}>{value}</i>)}<b>→</b><span>這次重抽</span>{current.map((value,index)=><i key={index}>{value}</i>)}</div>
      <div className="experiment-controls"><button onClick={() => draw(1)}>加入這 1 次</button><button onClick={() => draw(50)}><Play size={15} />累積 50 次</button><button onClick={() => setReplicates([])}>清空</button></div>
      <div className="bootstrap-bars" role="img" aria-label={`${replicates.length} 次 bootstrap 中位數分布`}>
        {[3,4,5,12].map((value,index)=><div key={value}><i style={{height:`${(counts[index]/max)*100}%`}}/><strong>{counts[index]}</strong><span>中位數 {value}</span></div>)}
      </div>
      <p className="experiment-takeaway">每次先產生一個與原樣本同樣大小的重抽樣本，再計算一次中位數。累積的不是原始觀察值，而是<strong>統計量的重抽分配</strong>。</p>
    </LearnCycle>
  );
}

function CategoricalLab() {
  const rows = [{name:"手機續訂",o:42,e:30},{name:"手機未續",o:18,e:20},{name:"桌機續訂",o:25,e:30},{name:"桌機未續",o:15,e:20}];
  const [selected, setSelected] = useState(0);
  const contributions = rows.map((row)=>(row.o-row.e)**2/row.e);
  return (
    <LearnCycle
      title="χ² 不是只看差幾人，而是看『相對期望值差多遠』"
      mission="逐格比較觀察次數 O 與期望次數 E，找出哪一格對整體 χ² 的貢獻最大。"
      question="哪一格對 χ² 的貢獻最大？"
      options={["手機續訂：42 vs 30", "手機未續：18 vs 20", "桌機未續：15 vs 20"]}
      correct={0}
      feedback={["差 12 人，而且相對期望 30 很大；貢獻為 12²/30=4.8。", "只差 2 人，平方後再除以 20，貢獻只有 0.2。", "差 5 人的貢獻是 25/20=1.25，仍小於第一格。"]}
    >
      <div className="chi-table"><div className="table-head"><span>格子</span><span>觀察 O</span><span>期望 E</span><span>貢獻</span></div>{rows.map((row,index)=><button key={row.name} className={selected===index?"active":""} onClick={()=>setSelected(index)}><span>{row.name}</span><span>{row.o}</span><span>{row.e}</span><strong>{contributions[index].toFixed(2)}</strong></button>)}</div>
      <div className="contribution-bar"><i style={{width:`${contributions[selected]/5*100}%`}}/><span>(O−E)²/E = {contributions[selected].toFixed(2)}</span></div>
      <p className="experiment-takeaway">點不同格比較。χ² = Σ(O−E)²/E = <strong>{contributions.reduce((a,b)=>a+b,0).toFixed(2)}</strong>；最大的格子最值得後續檢查，但整體檢定仍是把所有格子的證據加總。</p>
    </LearnCycle>
  );
}

function anovaF(groups:number[][]){
  const all=groups.flat(); const grand=mean(all); const ssb=groups.reduce((s,g)=>s+g.length*(mean(g)-grand)**2,0); const ssw=groups.reduce((s,g)=>s+g.reduce((q,v)=>q+(v-mean(g))**2,0),0);
  return (ssb/(groups.length-1))/(ssw/(all.length-groups.length));
}
function AnovaLab() {
  const scenarios=[{label:"A：平均數分開、組內很集中",groups:[[3,4,4,5],[8,9,9,10],[13,14,14,15]]},{label:"B：平均數相近、組內很分散",groups:[[2,7,10,13],[4,6,10,12],[3,8,9,12]]}];
  const [scenario,setScenario]=useState(0); const groups=scenarios[scenario].groups; const f=anovaF(groups);
  return (
    <LearnCycle title="ANOVA 的 F 是組間訊號除以組內雜訊" mission="兩個情境都有三組資料。不要只看總範圍；同時比較組平均之間的距離與每組內部的散亂程度。" question="哪個情境會有較大的 F？" options={["平均數分開，而且每組很集中","平均數接近，而且每組很分散","只看總樣本數，兩者一樣"]} correct={0} feedback={["組間差異大、組內差異小，F 的分子大而分母小。","組平均接近讓組間訊號小，組內分散又讓分母大。","樣本數影響自由度與穩定度，但這裡兩者樣本數相同，變異結構才是關鍵。"]}>
      <div className="experiment-controls">{scenarios.map((item,index)=><button key={item.label} className={scenario===index?"active":""} onClick={()=>setScenario(index)}>{item.label}</button>)}</div>
      <div className="group-dotplot" role="img" aria-label={`${scenarios[scenario].label}，F=${f.toFixed(1)}`}>{groups.map((group,index)=><div key={index}><span>第 {index+1} 組</span><i className="axis"/>{group.map((value,j)=><b key={j} style={{left:`${value/16*100}%`}}/>)}<em style={{left:`${mean(group)/16*100}%`}}>平均 {mean(group).toFixed(1)}</em></div>)}</div>
      <p className="experiment-takeaway">目前 F = <strong>{f.toFixed(1)}</strong>。F 很大時，只能先說「至少一組平均數不同」；還不能直接指出是哪兩組，也不能跳過多重比較問題。</p>
    </LearnCycle>
  );
}

function MultipleLab() {
  const [round,setRound]=useState(1); const [method,setMethod]=useState<"raw"|"bonferroni">("raw");
  const ps=Array.from({length:20},(_,index)=>seeded(round*83+index)); const threshold=method==="raw"?.05:.0025; const flagged=ps.filter(p=>p<threshold).length;
  return (
    <LearnCycle title="20 個都是真的 H₀，也很容易冒出一個『顯著』" mission="這裡的 20 個 p 值全部來自虛無假設。每跑一個研究家族，就看未修正門檻與 Bonferroni 門檻各自會誤報幾個。" question="每項都用 α=.05，獨立做 20 次時，至少一次誤報的機率約多少？" options={["5%","36%","64%"]} correct={2} feedback={["5% 是單一檢定的型一錯誤率，不是整個檢定家族。","36% 接近一次都不誤報的機率 0.95²⁰。","1−0.95²⁰≈64.2%，所以『每項都守 5%』仍不足以保護整個家族。"]}>
      <div className="experiment-controls"><button className={method==="raw"?"active":""} onClick={()=>setMethod("raw")}>每項 α=.05</button><button className={method==="bonferroni"?"active":""} onClick={()=>setMethod("bonferroni")}>Bonferroni .05/20</button><button onClick={()=>setRound(v=>v+1)}><RefreshCw size={15}/>再跑 20 個 H₀</button></div>
      <div className="p-grid" role="img" aria-label={`20 個虛無檢定，門檻 ${threshold}，誤報 ${flagged} 個`}>{ps.map((p,index)=><span key={index} className={p<threshold?"flagged":""}><i>{index+1}</i><strong>{p.toFixed(3)}</strong></span>)}</div>
      <p className="experiment-takeaway">這一輪在門檻 {threshold} 下誤報 <strong>{flagged} 個</strong>。Bonferroni 把整體 α 分給 20 個問題，代價是更難發現真實效果；它控制的是 FWER，不是讓每個研究都更「正確」。</p>
    </LearnCycle>
  );
}

const labs = [DescriptiveLab, SamplingLab, ProbabilityLab, BinomialLab, CLTLab, RegressionLab, ConfidenceLab, SignificanceLab, BootstrapLab, CategoricalLab, AnovaLab, MultipleLab];

export function StatLab({ chapterNumber, accent }: { chapterNumber: number; accent: string }) {
  const Lab = labs[chapterNumber - 1] ?? DescriptiveLab;
  return <div style={{ "--chapter-accent": accent } as React.CSSProperties}><Lab /></div>;
}
