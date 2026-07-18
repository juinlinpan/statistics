// Keep the single publishing manifest in teaching order. Every full or split
// handout edition imports this list; never discover chapters with a glob.
export const chapterFiles = [
  "07-10-review-estimation-and-testing.md",
  "12-chi-square-tests.md",
  "13-anova.md",
  "14-simple-linear-regression.md",
  "15-multiple-regression.md",
  "16-regression-model-building.md",
  "17-time-series-and-forecasting.md",
  "18-nonparametric-methods.md",
];

export const examChapterFiles = chapterFiles.filter((filename) => !filename.startsWith("07-10-"));
