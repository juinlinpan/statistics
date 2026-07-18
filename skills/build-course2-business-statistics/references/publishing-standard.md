# Publishing Standard（course_2 合併講義與 PDF 發布標準）

## 目錄

- [正典與產物](#正典與產物)
- [章節納入規則](#章節納入規則)
- [雙向考古題索引](#雙向考古題索引)
- [印刷拆冊](#印刷拆冊)
- [列印版面](#列印版面)
- [重建流程](#重建流程)
- [發布驗收](#發布驗收)

## 正典與產物

`course_2/chapters/*.md` 是唯一正典。以下都是可重建產物，不得直接手改：

- `course_2/merged_chapters.md`：合併 Markdown。
- `course_2/merged_chapters.html`：自包含 KaTeX 與列印樣式的 HTML。
- `output/pdf/course2-business-statistics-handout.pdf`：A4 講義。
- `course_2/course2-slides-handout.md`、`.html` 與 `output/pdf/course2-slides-handout.pdf`：投影片講義版。
- `course_2/course2-exam-solutions.md`、`.html` 與 `output/pdf/course2-exam-solutions.pdf`：每題只出現一次的題目＋詳解版。

程式正典放在本 skill 的 `scripts/handout_manifest.mjs`、`scripts/merge_chapters.mjs`、`scripts/split_print_editions.mjs`、`scripts/build_handout.mjs`、`scripts/export_handout_pdf.mjs`、`scripts/export_print_editions.mjs`；`course_2/scripts/` 只保留方便執行的薄入口。修正輸出問題時改正典章節或 skill 腳本，再完整重建。

## 章節納入規則

- 以 `scripts/handout_manifest.mjs` 作唯一 manifest，依教學順序明列完整講義與考古題章節；不可用 glob 自動吞入所有 Markdown。
- 只納入 learner-facing 內容與適用 phase 都已完成的章節。骨架、等待投影片或含內部 phase 標記的檔案一律排除。
- 新章先通過 authoring gate，且 Phase 1–7 完成後才可加入 manifest。
- 合併時移除 frontmatter、把章間連結轉成文件內錨點、重設圖片與 course1 相對路徑，並拒絕重複錨點、不完整章節或不符 H1 的章名。
- 不在程式或規格硬寫總頁數、章界、題數或圖數；每次從最新產物量測，並把當次數據記入 `course_2/進度.md`。

## 雙向考古題索引

合併器依正典詳解中的連結產生衍生導覽：

- 每題取得唯一 `exam-chN-mc-K` 或 `exam-chN-problem-K` 錨點；錨點嵌在單題 H4 內，不能插成標題前的獨立空元素，否則會破壞防孤立分頁。
- 每題「詳解」後產生「回看講義」，跳到核心公式或方法。
- 正文教學節產生「對應考古題」，完整標示 `ChN 選擇題／計算題` 與可點擊題號。
- 配對優先採「選方法」第一個分句的具體公式，再採「代入計算／推理」中的具體公式；沒有專屬公式的辨識題才回到方法判斷準則。
- 次要診斷不能蓋過核心方法。跨章題要回到真正教授方法的章節，反向索引也列在該章。
- 索引只存在於合併產物，不寫回正典章節。

## 印刷拆冊

印刷拆冊必須從 `course_2/chapters/*.md` 重新解析，不得把完整 PDF 當來源裁切、抽頁或轉回文字：

- **投影片講義版**：納入所有已完成章節的正文，從每章 `## 考古題與詳解` 前截斷；保留教學公式、圖表與定性意義，不含題庫題號、題目或詳解。
- **考古題詳解版**：只納入已有考古題的完成章節。每個單題依序保留唯一一份 `##### 題目` 與 `##### 詳解`，題幹、選項、完整解題計算都保留；`#### 題組`、Exhibit 與共用資料只在所屬題組前出現一次。不得另加一段只有原題的重複題本，也不得改寫正典答案或臆造題幹。
- 詳解版的「回看投影片講義」連到投影片講義 HTML 的核心公式或方法錨點。純辨識題沒有可靠核心錨點時可以不硬塞連結。
- 兩冊各自經過 Markdown → HTML → PDF；HTML 與 PDF 不得由另一冊或完整 PDF 逆向產生。
- 拆冊器必須驗證：投影片版沒有 `## 考古題與詳解`；詳解版的單題數、`##### 題目` 數與 `##### 詳解` 數完全相等，每題順序是題目在前、詳解在後，共用題組數與正典一致。

## 列印版面

- 使用 A4 named pages；每章包成獨立 `<section class="chapter">`，章首強制從新頁開始。
- 封面不顯示頁首或頁碼；目錄右上顯示「目錄」；正文右上顯示當前完整章名；右下顯示連續實體頁碼。
- 章名與 `@page` 由 H1 清單自動生成，不手寫章節頁碼範圍。
- H1–H6 設定 `break-inside: avoid-page` 與 `break-after: avoid-page`；題目錨點留在 H4 內，避免題型範圍或單題標題孤立在頁尾。
- 表格列、公式、圖片與緊湊索引框盡量不跨頁；題目或詳解太長時允許自然分頁，但不得裁切、重疊或混淆題解邊界。

## 重建流程

從 repository root 執行：

```bash
node course_2/scripts/export_handout_pdf.mjs
```

這會依序執行合併、HTML 與 Chrome／Chromium PDF 輸出。除錯時可分段執行：

```bash
node course_2/scripts/merge_chapters.mjs
node course_2/scripts/build_handout.mjs
```

另外產生投影片講義版與不重複題目的考古題詳解版時，執行：

```bash
node course_2/scripts/export_print_editions.mjs
```

這個指令先從正典章節拆出兩份 Markdown，再各自建立 HTML，最後分別呼叫 Chrome／Chromium 建立兩份 PDF。只除錯單一 PDF 時，可設定 `COURSE2_PRINT_EDITION=slides` 或 `COURSE2_PRINT_EDITION=solutions`；正常發布仍應不帶環境變數一次重建兩冊。

HTML 使用 `website/node_modules` 的 React Markdown、GFM、remark-math、rehype-raw 與 KaTeX。PDF 需要 Chrome／Chromium；找不到時用 `CHROME_PATH` 指定執行檔。

## 發布驗收

每次章節、題庫、索引或樣式變更後都完成以下檢查：

1. **合併**：每章恰有一個 H1；無骨架／phase 控制文字；顯式錨點跨檔唯一；本地圖片、相對連結與公式錨點存在。
2. **題解結構**：單題數等於「題目」數與「詳解」數；每題順序正確；題庫清冊、選項分析與進度證據一致。
3. **雙向索引**：每題唯一錨點且恰有一個「回看講義」；正文索引含章號、題型與題號；HTML 所有 `#fragment` 都有目標；用 pypdf 確認 PDF 含內部 GoTo link annotations。
4. **HTML**：章數、題數與圖片數符合最新進度；`class="katex-error"` 為 0；沒有失效圖片、控制文字或生成標記外洩。
5. **PDF metadata**：用 `pdfinfo` 確認檔案可讀、A4、頁數合理；用 `pdftotext -layout` 確認每頁有內容、右上章名在章界精準切換、右下頁碼連續。
6. **孤立標題掃描**：掃描全 PDF，任何 H1–H5 或題型範圍標題都不能成為頁面最後一個正文項目。
7. **視覺 QA**：用 Poppler 渲染封面、目錄、每章首頁、章界前後頁、公式、寬表、所有圖所在頁、長題號索引、單題回看框、題目／詳解跨頁處與最後一頁；最新版 PNG 必須零裁切、零重疊、零錯誤字形。
8. **帳本**：把實際頁數、章界、題數、圖數、錨點／連結數、抽查頁與已知未納入章節記入 `course_2/進度.md`；不要把過期頁碼留成最新版描述。
9. **拆冊專項**：分別檢查兩冊 Markdown、HTML 與 PDF。投影片版不得出現考古題區；詳解版的題號、題目與詳解必須逐題一一配對，題組／Exhibit 只能出現一次，不得另外附一段重複原題。兩冊都要檢查 KaTeX error、fragment 連結、A4 metadata、異常空白頁、孤立標題、章首、章界與末頁。
