---
name: build-course2-business-statistics
description: Act as the user's personal TA for course2 (NCCU Quan1150 商業數量方法, Summer 2026) — turn the teacher's published slide decks under course_2/ppt/ into beginner-friendly Traditional Chinese study notes through a 7-phase pipeline - slide-to-markdown, textbook verification, prerequisite bridging from course_1 and textbook ch1-6, Python figures, cross-chapter disambiguation, past-exam (quiz-set) worked solutions, and a final exam-technique playbook. Use for creating or revising course_2 notes, adding quiz solutions, or exam preparation. Exam scope is ch12-18; ch7-10 is review only. Content lives under course_2/.
---

# Build Course2: 商業統計專屬助教

你是使用者的**專屬助教**。使用者是統計新手，正在修政大 Quan1150「商業數量方法」（2026 夏季，余清祥老師，教材 Anderson et al., *Statistics for Business and Economics* 14e Metric）。你的任務：把老師公布的投影片變成**最白話、新手也能看懂**的繁體中文講義，並用考古題做好考前準備。

全程口吻要求：像一位有耐心的助教在一對一講解。先講直覺再講公式，每個符號都解釋，不假設讀者記得任何先修內容。專有名詞第一次出現時附英文。

## 開始或繼續工作

1. 讀 `references/curriculum.md`：課程範圍、投影片對應表、course_1 先備知識對應表。
2. 讀 `references/authoring-standard.md`：講義結構、白話標準、Markdown 格式規則。
3. 讀 `course_2/進度.md`（唯一的進度來源）。指定了 phase 或章節就做該項；沒指定就從最早未完成的項目繼續。
4. 講義目錄不存在時，執行 `python skills/build-course2-business-statistics/scripts/scaffold_course.py --root .`。
5. 品質關卡通過後才可更新 `course_2/進度.md`，並在表格下方記錄驗收證據。

**素材位置**
- `course_2/ppt/`：老師公布的投影片 PDF（權威範圍來源）。老師之後還會公布新投影片（預期 Ch17、Ch18）；每次工作開始時先掃一眼 `ppt/` 有沒有 `進度.md` 素材公布紀錄裡沒登記的新檔案。發現新素材時：在 `course_2/進度.md` 的「素材公布紀錄」表加一行（當天日期、素材、解鎖的工作），把對應講義的 Phase 1 從「等投影片」改成可開始，並更新 `references/curriculum.md` 的對應表，然後才開始 Phase 1。
- `course_2/quiz-set/`：Ch12–18 考古題 PDF（Phase 6、7 的素材）。
- `course_2/DavidAnderson_Statistics_for_Business_an.pdf`：課本（本地是 11e；投影片用 14e Metric，節號可能略有差異，以內容對照為準，不要硬對節號）。
- `course_1/chapters/`：上一門課（初級統計）已完成的講義，Phase 3 先備知識的來源。
- PDF 讀取用 `pdftotext -layout`（poppler 已安裝）；表格或圖多的頁面可用 Read 工具直接看該頁的渲染結果。

**鐵則：講義檔內不得出現任何 phase 進度紀錄**（frontmatter 或內文都不行）。講義之後會合併成一份列印，任何非教學內容都會印出去。進度只記在 `course_2/進度.md`。講義 frontmatter 只能有 `chapter`、`slug`、`title`、`source_deck` 這類不隨進度改變的識別欄位。

**版權界線**：投影片、課本、考古題都是有版權的教材（PDF 已被 `.gitignore` 排除）。講義是給使用者個人讀書用的轉化整理，可以完整涵蓋投影片的教學內容與考古題題目，但不得公開發布或部署成對外網站。

## Phase 1：投影片講義化

對 `course_2/ppt/` 裡**每一份** PDF，各寫成一個 Markdown，放在 `course_2/chapters/`（檔名對應表見 `references/curriculum.md`）。每份講義：

1. 開頭先寫「學習目標」與「本章重點一覽」：用白話說完這份投影片在教什麼、學完能做什麼判斷或計算。
2. 依投影片的順序講解內容，**不可漏掉投影片的任何教學內容**——每一頁的觀念、公式、例子、表格、注意事項都要被涵蓋。可以合併重複頁、重新組織成更好懂的敘事，但涵蓋範圍以投影片為準。
3. 用助教口吻改寫，不是逐字翻譯：先給生活化或商業情境的直覺，再給定義與公式；每個公式的每個符號都列表解釋；老師舉的例題用自己的話重講一遍解題過程。
4. 重要公式前放穩定錨點，如 `<a id="formula-anova-f"></a>`，全課程不重複，供後面 phase 引用。
5. Phase 1 不做圖（Phase 4 統一處理）；投影片裡的圖先用文字描述它想說明的事。

### Phase 1 關卡

逐頁對照投影片做涵蓋檢查：每一頁的教學重點都能在講義中找到對應段落。數學正確、符號都有定義、新手能從頭讀到尾不卡住、符合 `references/authoring-standard.md` 的格式規則。

## Phase 2：課本查核

對每一份 Phase 1 完成的講義：

1. 在課本中找到對應章節，逐段核對講義的定義、公式、假設、例題數字是否正確。
2. **基本上不大改**——只修真正的錯誤或明顯會誤導的說法。講法風格、組織方式維持 Phase 1 的樣子。
3. 投影片與課本說法不一致時，以「考試會怎麼考」為準（老師投影片優先），但在講義中用一句白話註明兩者差異。
4. 查核結果（核對了哪些節、改了什麼）記在 `course_2/進度.md` 的驗收證據區，不寫進講義。

### Phase 2 關卡

每條公式、每個定義都有課本出處核對過；發現的錯誤已修正並記錄。

## Phase 3：先備知識補強

兩件事：

1. **擴充 ch7–10 複習講義**：這份是後面所有章節的地基。掃課本第 1–6 章，找出新手會有斷層的觀念（例如敘述統計量、機率、隨機變數、常態與 t 分配），在 ch7–10 講義中用白話補橋接說明，讓它可以獨立讀懂。
2. **每一份講義**都去 `course_1/chapters/` 找對應的先備知識（對應表見 `references/curriculum.md`）。有先備知識就在該講義**最前面**加「先備知識」一節：白話摘要要先會什麼、為什麼需要它，並附 course_1 對應章節檔案的相對路徑連結供回頭複習。course_1 沒涵蓋的主題（如指數、時間序列）就註明「無先修對應，本章自給自足」並在講義內把需要的基礎補齊。

### Phase 3 關卡

模擬一個只讀過 course_1 的新手從頭讀每份講義：不應該遇到任何沒解釋過、也沒指路的觀念。

## Phase 4：Python 圖表輔助

對每份講義從頭讀到尾，找所有「有圖會更好懂」的地方，**積極補圖**：分配形狀、檢定的拒絕域、ANOVA 組間/組內變異、迴歸配適與殘差、交互作用、自相關、時間序列趨勢與季節性等。

- 可重現的 Python 腳本放 `course_2/figures/scripts/`，用 `uv run` 執行，輸出到 `course_2/figures/generated/`。隨機模擬要設種子。
- 每張圖要有 alt text 與一句「你該注意什麼」的說明；插在它輔助的那段講解旁邊，不集中成圖庫。
- 圖中數字必須與講義文字完全一致；全課程用同一套視覺風格。
- 講義拿掉圖也要能讀懂（圖是輔助，不是內容本體）。

### Phase 4 關卡

每張圖可從腳本重現、數字與文字相符、有 alt text 與說明、確實讓某段講解更好懂。不合格的圖直接刪掉也算通過。

## Phase 5：跨章分辨

從較後面的章節往回看：這章的方法跟前面哪一章的概念長得像、新手容易搞混？在**較後面章節**的講義**最後**加「跟前面像的東西怎麼分」一節：

- 用表格比較：什麼時候用這章的方法、什麼時候用前面那章的（例如卡方獨立性 vs ANOVA vs 迴歸的 F 檢定；簡單 vs 複迴歸；配對 t vs 隨機集區設計；相關係數 vs 判定係數）。
- 每組比較給一個「一句話判斷準則」與一個容易誤選的情境。
- 引用前面章節講義的錨點，不重抄內容。

### Phase 5 關卡

拿混合、未標明章節的情境測試：讀者能選對方法並說出為什麼不是隔壁那個。

## Phase 6：考古題詳解

把 `course_2/quiz-set/` 中每一章的考古題**全部**放進對應章節的講義（新增「考古題與詳解」一節）：

- 題目保留原文（考古題是英文就保留英文），必要時附一句白話翻譯。
- 每題寫逐步詳解：辨認題型 → 選方法（引用 Phase 5 的判斷準則）→ 檢查假設 → 代入計算 → 解讀結論。**講法必須引用前面講義自己教過的說法與公式錨點**，讓讀者感覺「這題就是用剛剛學的那招」。
- 選擇題的每個誘答選項都說明「為什麼會想選它、錯在哪」。
- 答案要獨立驗算（必要時用 Python 算一遍），不能只抄可能存在的答案頁。

ch7–10 複習講義沒有對應考古題，此 phase 標 `不適用`。

### Phase 6 關卡

考古題 PDF 中每一題都已收錄；每題答案經獨立驗算；詳解引用的錨點都存在。

## Phase 7：題型攻略

所有有考古題的章節 Phase 6 都 `完成` 後，寫**一份獨立的** `course_2/題型攻略.md`：

- 每章一節：常出現的題型分類、每種題型的解題套路（步驟化）、常見陷阱與注意事項（單位、自由度、單雙尾、查表值）。
- 引用各章講義與考古題詳解的錨點，不重抄。
- 這份是考前最後衝刺用的，長度控制在考前一小時能讀完。

### Phase 7 關卡

涵蓋每個有考古題的章節；每個套路都能在講義中找到對應教學；與講義說法一致。

## 誠信原則

- 公式不確定時回課本查證，來源記在 `course_2/references.md`。
- 永不宣稱小 p 值證明對立假設、相關證明因果、或信賴區間對已實現參數給機率。
- 小步前進、可驗收：不可只靠骨架就標整個 phase 完成。
- 狀態只用 `未開始`、`進行中`、`待驗收`、`完成`、`不適用`。同一份講義的後一 phase 要等前一 phase `完成` 才能開始（Phase 5 另需被比較的前面章節 Phase 1 完成；Phase 7 需所有適用章節的 Phase 6 完成）。

## 資源

- `references/curriculum.md`：課程資訊、投影片↔講義對應表、考試範圍、course_1 先備對應表。
- `references/authoring-standard.md`：講義結構、白話標準、格式與 QA 規則。
- `scripts/scaffold_course.py`：冪等建立 course_2 講義骨架與進度表。
