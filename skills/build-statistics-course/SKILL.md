---
name: build-statistics-course
description: Build and iteratively improve a Traditional Chinese introductory-statistics course from chapter Markdown notes through worked practice, cross-chapter method selection, and an interactive learning website. Use for the Stanford/Coursera Introduction to Statistics curriculum, creating or revising chapter notes, adding diagnostic exercises and step-by-step solutions, comparing similar formulas or tests, generating statistical figures with Python and uv, or implementing the chapter-based interactive course site.
---

# Build Statistics Course

Build a student-first statistics course in four gated phases. Teach intuition before notation, preserve mathematical precision, and make every method choice explainable.

## Start or Resume Work

1. Read `references/curriculum.md` to identify the canonical 12-module scope.
2. Read `references/authoring-standard.md` before changing educational content or the website.
3. Inspect the repository and preserve existing work. Treat completed earlier-phase content as the source for later phases.
4. If the course directories do not exist, run `python skills/build-statistics-course/scripts/scaffold_course.py --root .`.
5. Read `course/進度.md` as the single source of truth. Work on the requested phase and chapter; if neither is specified, continue the earliest incomplete phase and module.
6. Update `course/進度.md` only after the relevant quality gate passes. Keep one row per chapter and record review evidence below the table.

Do not reproduce Coursera quizzes, transcripts, or paywalled course material. Use the public module outline only as the scope, then write original explanations, examples, figures, and exercises.

## Phase 1: Write Core Notes

Create one file per module under `course/chapters/`. For every lesson topic:

1. State what the learner will be able to decide or compute.
2. Open with a concrete question or visual intuition.
3. Define essential terms in Traditional Chinese and include the English term on first use.
4. Derive or motivate formulas; define every symbol, assumptions, units, and valid use conditions.
5. Explain interpretation, common confusion, and at least one non-example.
6. Close with a short self-check and a compact formula/term recap.

Use stable anchors such as `<a id="formula-standard-error-mean"></a>` immediately before important formulas. Keep anchors unique across the course so Phase 3 and Phase 4 can link to them.

Generate figures only when they materially improve understanding. Prefer reproducible Python scripts under `course/figures/scripts/`, run them with `uv run`, and store outputs under `course/figures/generated/`. Give every figure alt text and explain what the learner should notice.

### Phase 1 gate

Confirm curriculum coverage, mathematical correctness, defined notation, explicit assumptions, useful intuition, accessible figures, and no unexplained prerequisite jumps.

## Phase 2: Add Diagnostic Practice

Extend the Phase 1 sections without replacing their explanations. Add practice close to the concept it tests.

- Include conceptual, method-selection, interpretation, and calculation questions.
- For each multiple-choice distractor, record the specific misconception that makes it tempting and give corrective feedback without revealing unrelated answers.
- For calculations, give numbered steps: identify givens, choose a method, check assumptions, substitute with units, calculate, interpret, and sanity-check.
- Link every solution to the exact formula anchor it uses.
- Vary surface contexts and numbers; do not create copies solved by blind substitution.

Store reusable structured question data in `course/questions/<chapter>.yaml` when Phase 4 will render it interactively. Keep the Markdown version readable without JavaScript.

### Phase 2 gate

Verify every answer independently, ensure distractors map to distinct plausible misconceptions, and ensure solutions teach the decision process rather than only arithmetic.

## Phase 3: Connect Chapters and Select Methods

Add cross-links at the point of confusion, not only in an appendix. Maintain `course/concept-map.md` and `course/method-selector.md`.

- Compare similar quantities and methods in tables: parameter vs statistic, SD vs SE, normal vs t, independent vs paired samples, confidence intervals vs tests, chi-square variants, ANOVA vs repeated pairwise tests, bootstrap vs parametric inference.
- For each method, specify data type, target quantity, number/dependence of groups, assumptions, statistic, uncertainty measure, and interpretation.
- Include finance-oriented transfer examples such as returns, volatility, event comparisons, proportions, regression, and multiple testing, while clearly warning that statistical evidence is not investment advice.
- Add “why not the neighboring formula?” explanations wherever two methods are easily confused.

### Phase 3 gate

Test the selector using mixed, unlabeled scenarios. A learner should be able to choose a method and justify why nearby alternatives do not apply.

## Phase 4: Build the Interactive Course

Do not begin Phase 4 until every one of the 12 chapters is marked `完成` for Phase 1, Phase 2, and Phase 3 in `course/進度.md`. Scaffolding a web app, selecting a framework, or implementing shared site components also counts as beginning Phase 4 and must wait. When the gate opens, develop Phase 4 as one coordinated course-wide project rather than chapter by chapter.

Create a responsive chapter-based site that progressively reveals one learning unit at a time while preserving direct links and browser navigation.

- Make each chapter a route and each concept/formula a stable deep link.
- Render math accessibly and keep a no-JavaScript-readable content source where practical.
- For multiple choice, give option-specific misconception feedback after submission and allow retry.
- For calculations, reveal one scaffolded step at a time; never require the learner to expose the full solution immediately.
- Link each solution step to the formula and prerequisite concept it uses.
- Add interactive simulations only when manipulation clarifies a relationship, such as sampling distributions, CLT, confidence-interval coverage, regression leverage, bootstrap, or multiple testing.
- Preserve progress locally and provide reset/export controls without collecting personal data by default.
- Test keyboard use, focus order, color contrast, reduced motion, mobile layout, formula links, incorrect-answer paths, and correct-answer paths.

Choose the site's framework from existing repository conventions. Do not replace an established stack without an explicit request.

### Phase 4 gate

Run the repository's type checks, tests, and production build. Manually verify at least one full chapter, every interaction type, narrow and wide viewports, and all formula deep links touched by the change.

## Maintain Integrity

- Use authoritative references to verify formulas when uncertain; record sources in `course/references.md`.
- Distinguish definitions, approximations, conventions, and theorems.
- Never claim that a small p-value proves an alternative, that correlation proves causation, or that a confidence interval assigns probability to a fixed realized parameter under the standard frequentist interpretation.
- Prefer small reviewable chapter increments. Do not mark an entire phase complete from scaffolding alone.
- Use only `未開始`, `進行中`, `待驗收`, and `完成` for chapter Phase 1–3 statuses. Do not start a later phase for a chapter until its preceding phase is `完成`. Keep Phase 4 `鎖定` until all 36 chapter-phase cells through Phase 3 are `完成`.

## Resources

- `references/curriculum.md`: canonical public module and lesson scope.
- `references/authoring-standard.md`: required chapter, exercise, feedback, and QA schemas.
- `scripts/scaffold_course.py`: idempotently create the course workspace and progress manifest.
