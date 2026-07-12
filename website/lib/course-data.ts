import { load } from "js-yaml";

import chapter01 from "../content/chapters/01-descriptive-statistics.md?raw";
import chapter02 from "../content/chapters/02-sampling-and-experiments.md?raw";
import chapter03 from "../content/chapters/03-probability.md?raw";
import chapter04 from "../content/chapters/04-normal-and-binomial.md?raw";
import chapter05 from "../content/chapters/05-sampling-distributions-clt.md?raw";
import chapter06 from "../content/chapters/06-regression.md?raw";
import chapter07 from "../content/chapters/07-confidence-intervals.md?raw";
import chapter08 from "../content/chapters/08-significance-tests.md?raw";
import chapter09 from "../content/chapters/09-resampling.md?raw";
import chapter10 from "../content/chapters/10-categorical-data.md?raw";
import chapter11 from "../content/chapters/11-one-way-anova.md?raw";
import chapter12 from "../content/chapters/12-multiple-comparisons.md?raw";

import questions01 from "../content/questions/01-descriptive-statistics.yaml?raw";
import questions02 from "../content/questions/02-sampling-and-experiments.yaml?raw";
import questions03 from "../content/questions/03-probability.yaml?raw";
import questions04 from "../content/questions/04-normal-and-binomial.yaml?raw";
import questions05 from "../content/questions/05-sampling-distributions-clt.yaml?raw";
import questions06 from "../content/questions/06-regression.yaml?raw";
import questions07 from "../content/questions/07-confidence-intervals.yaml?raw";
import questions08 from "../content/questions/08-significance-tests.yaml?raw";
import questions09 from "../content/questions/09-resampling.yaml?raw";
import questions10 from "../content/questions/10-categorical-data.yaml?raw";
import questions11 from "../content/questions/11-one-way-anova.yaml?raw";
import questions12 from "../content/questions/12-multiple-comparisons.yaml?raw";

export type QuestionOption = {
  id: string;
  text: string;
  correct: boolean;
  feedback: string;
  misconception?: string;
};

export type QuestionStep = {
  title: string;
  explanation: string;
  formula_ref?: string;
};

export type Question = {
  id: string;
  type: "multiple-choice" | "calculation" | string;
  difficulty: string;
  prompt: string;
  answer: string;
  solution?: string;
  options?: QuestionOption[];
  steps?: QuestionStep[];
  checks?: string[];
};

export type Chapter = {
  number: number;
  slug: string;
  title: string;
  eyebrow: string;
  description: string;
  accent: string;
  content: string;
  questions: Question[];
  figureCount: number;
};

const rawChapters = [chapter01, chapter02, chapter03, chapter04, chapter05, chapter06, chapter07, chapter08, chapter09, chapter10, chapter11, chapter12];
const rawQuestions = [questions01, questions02, questions03, questions04, questions05, questions06, questions07, questions08, questions09, questions10, questions11, questions12];

const metadata = [
  ["descriptive-statistics", "描述統計與資料探索", "先看懂資料的樣子", "從變數型態、圖表到平均數與標準差，建立閱讀資料的第一雙眼睛。", "#f06a4f", 2],
  ["sampling-and-experiments", "抽樣與實驗設計", "資料怎麼來，決定你能說多遠", "辨認偏誤、混淆與隨機化，分清描述、推廣與因果。", "#e8903a", 1],
  ["probability", "機率", "替不確定性建立語言", "從互補、條件機率走到貝氏更新，學會拆解隨機事件。", "#d5a82f", 1],
  ["normal-and-binomial", "常態近似與二項分配", "把機率分布變成可計算的模型", "理解常態曲線、z 分數、二項條件與連續性修正。", "#58a76b", 2],
  ["sampling-distributions-clt", "抽樣分配與中央極限定理", "樣本為什麼能代表母體", "看懂標準誤、平方根律、大數法則與中央極限定理。", "#2b9c8f", 2],
  ["regression", "迴歸", "用直線描述關係，也尊重例外", "從相關與預測到殘差、離群點與迴歸謬誤。", "#3693b6", 3],
  ["confidence-intervals", "信賴區間", "不只給答案，也說明不確定性", "用涵蓋率、誤差界限與 bootstrap 正確解讀區間估計。", "#5477c8", 2],
  ["significance-tests", "顯著性檢定", "證據有多不尋常？", "建立假設、檢定統計量與 p 值的完整推理鏈。", "#8066c7", 2],
  ["resampling", "重抽樣", "讓電腦重做抽樣，觀察答案怎麼變", "用 Monte Carlo 與 bootstrap 處理難以解析計算的不確定性。", "#a460b5", 2],
  ["categorical-data", "類別資料分析", "比較比例與列聯表", "用卡方方法回答適合度、同質性與獨立性問題。", "#c05c91", 2],
  ["one-way-anova", "單因子變異數分析", "一次比較三組以上的平均數", "把總變異拆成組間與組內，理解 F 統計量的意義。", "#d45772", 2],
  ["multiple-comparisons", "多重比較", "問得越多，誤報越容易發生", "辨認資料窺探，使用 Bonferroni、FDR 與資料切分控制錯誤。", "#dc675d", 2],
] as const;

function cleanMarkdown(raw: string) {
  return raw
    .replace(/^---\n[\s\S]*?\n---\n/, "")
    .replaceAll("../figures/generated/", "/figures/");
}

export const chapters: Chapter[] = metadata.map((item, index) => ({
  number: index + 1,
  slug: item[0],
  title: item[1],
  eyebrow: item[2],
  description: item[3],
  accent: item[4],
  figureCount: item[5],
  content: cleanMarkdown(rawChapters[index]),
  questions: (load(rawQuestions[index]) ?? []) as Question[],
}));

export function getChapter(slug: string) {
  return chapters.find((chapter) => chapter.slug === slug);
}
