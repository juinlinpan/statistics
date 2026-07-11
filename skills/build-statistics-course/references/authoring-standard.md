# Authoring and QA Standard

## Chapter Contract

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

Write in natural Traditional Chinese for a learner who found the original lecture too compressed. Include English terminology on first mention. Use short sentences around dense formulas, but do not dilute precise distinctions.

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

Maintain `course/進度.md` as the only authoritative progress ledger. Keep a table with all 12 chapters and separate Phase 1, Phase 2, and Phase 3 columns. Use `未開始`, `進行中`, `待驗收`, or `完成` exactly.

Below the table, maintain dated evidence entries containing the chapter, phase, files reviewed, checks performed, and known limitations. Never infer completion merely from file existence.

Keep Phase 4 status as `鎖定` unless all 36 cells in the table are `完成`. After that condition is met, change it to `未開始`; only then may website implementation begin.
