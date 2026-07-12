# Authoring and QA Standard

## Chapter Contract

`course/chapters/<chapter>.md` is the single canonical learner-facing document for a chapter. Phase 1 creates it; Phase 2, Phase 3, and Phase 4 revise and extend that same file. Never fork a chapter into `phase2/`, `phase3/`, `*-practice.md`, or another competing Markdown source.

Use this order unless pedagogy clearly requires another:

1. Chapter title and status metadata
2. Why this chapter matters
3. Prerequisite check
4. Learning objectives stated as observable actions
5. Concept sections, each containing intuition, definition, notation/formula, assumptions, example or visual, pitfalls, and self-check
6. Chapter synthesis
7. Formula and terminology recap
8. Cumulative check
9. Links to prerequisites and next chapter

When adding later phases, retain this structure and insert content at the relevant concept. A useful cumulative pattern is `觀念 → 公式與判斷 → 類題與詳解 → 常見誤選 → 跨章比較 → 自我檢核`.

Write in natural Traditional Chinese for a learner who found the original lecture too compressed. Include English terminology on first mention. Use short sentences around dense formulas, but do not dilute precise distinctions.

## VSCode Markdown Compatibility

Write all learner-facing chapter Markdown so the VSCode Markdown renderer can parse it reliably:

1. Use dollar-delimited math only. Use `$E = mc^2$` for inline formulas and `$$ \\bar{x} = \\frac{1}{n}\\sum x_i $$` for display formulas. Do not use `\\( ... \\)` or `\\[ ... \\]`, which fail in some VSCode renderers.
2. Use ASCII parentheses `( )` everywhere, including Chinese-English terminology. Write `**平均數(mean)**` rather than `**平均數（mean）**`; full-width parentheses can interfere with Markdown parser boundary matching.
3. Put one literal ASCII space immediately after every closing `**` before the next text or symbol. Write `**平均數(mean)** 是...`, not `**平均數(mean)**是...`. Chinese characters, English letters, punctuation, and `$` do not count as that separator; insert the space manually.

Before marking a chapter phase complete, search the changed Markdown for `\\(`, `\\[`, `（`, `）`, and bold closings followed immediately by a non-space character. Review any intentional exceptions manually.

## Formula Contract

For each important formula include:

- globally unique anchor ID
- formula name and purpose
- expression
- symbol table with meaning and units
- assumptions and domain restrictions
- decision cue: when to use it
- contrast cue: when not to use it and the neighboring formula to consider
- interpretation in context
- one dimensional or magnitude sanity check where applicable

## Question Schema

Each question needs a stable ID, chapter and concept IDs, difficulty, prompt, answer, and solution. Multiple-choice questions additionally need option IDs and a misconception-specific response for every incorrect option. Calculation questions need structured steps and formula anchor links.

Recommended YAML shape:

```yaml
- id: m05-se-mean-01
  type: calculation
  concepts: [sampling-distribution, standard-error]
  difficulty: foundational
  prompt: "..."
  answer: "..."
  steps:
    - title: "辨認目標量"
      explanation: "..."
      formula_ref: "formula-standard-error-mean"
  checks:
    - "單位是否與平均數相同？"
```

Never encode only `correct: false` for a distractor. Store the inferred misconception and a targeted correction.

Question YAML is optional structured data for rendering. It must not be the only place where a learner can read a question or its explanation; keep the complete learner-facing content in the chapter Markdown.

## Figure Contract

- Store source code separately from generated files.
- Seed randomized figures and simulations.
- Label axes and units; do not rely on color alone.
- Use alt text that conveys the statistical takeaway, not merely the objects shown.
- State whether a figure is observed data, simulated data, or a schematic.
- Record the command needed to regenerate it.

## Completion Evidence

Before changing a phase status to `完成`, record in `course/進度.md`:

- files reviewed
- validation performed
- remaining limitations, if any
- completion date

Scaffolds and TODO placeholders count as `未開始`, never `完成`.

## Progress Ledger Contract

Maintain `course/進度.md` as the only authoritative progress ledger. Keep a table with all 12 chapters and separate Phase 1, Phase 2, Phase 3, and Phase 4 columns. Use `未開始`, `進行中`, `待驗收`, or `完成` exactly.

Below the table, maintain dated evidence entries containing the chapter, phase, files reviewed, checks performed, and known limitations. Never infer completion merely from file existence.

Keep Phase 5 status as `鎖定` unless all 48 cells in the table are `完成`. After that condition is met, change it to `未開始`; only then may website implementation begin.
