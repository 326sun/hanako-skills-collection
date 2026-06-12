---
name: skill-creator
description: Create, improve, and benchmark skills. Trigger evaluation and description optimization loops. Triggers: create skill, improve skill, skill eval, benchmark skill, optimize description, 创建技能, 改进技能, 评估技能.
---

# Skill Creator

Core loop: draft → test → evaluate → improve → repeat.

## Rules

- Match communication to user's technical level. "JSON" and "assertion" need cues.
- Skill anatomy: `SKILL.md` (YAML: name + description) + optional `scripts/`, `references/`, `assets/`.
- Progressive disclosure: metadata always in context (~100 words), body on trigger (<500 lines ideal), resources as needed.
- Description is the primary trigger. Make it pushy — include contexts where skill SHOULD fire. Claude undertriggers; combat this.
- Explain why, not heavy-handed ALWAYS/NEVER. No malware or exploits.
- Preflight (Python 3.10+): `node skills2set/skill-creator/scripts/check_env.mjs --capability <name>`. Capabilities: `quick-validate`, `package-skill`, `aggregate-benchmark`, `eval-viewer`, `run-eval`, `description-optimize`, `run-loop`. If `ok: false`, stop.

## Workflow

### Creating a Skill

1. Capture intent: what, when, output format, test cases?
2. Interview: edge cases, I/O, examples, success criteria. Research via MCPs/subagents.
3. Write SKILL.md. Draft 2-3 test prompts → `evals/evals.json` (schema: `references/schemas.md`).

### Running Evaluations

Results in `<skill-name>-workspace/iteration-N/eval-ID/`. Don't pause mid-sequence.

**Step 1**: Spawn all subagents at once (with-skill + baseline). Write `eval_metadata.json`: `{"eval_id":0,"eval_name":"...","prompt":"...","assertions":[]}`.

**Step 2**: While runs progress, draft assertions. Objective outputs only. Subjective skills: skip.

**Step 3**: Save subagent `total_tokens` + `duration_ms` to `timing.json` as they complete.

**Step 4**: Grade (subagent reads `agents/grader.md` → `grading.json` with `text`,`passed`,`evidence`). Aggregate: `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`. Launch viewer: `nohup python <skill-creator>/eval-viewer/generate_review.py <workspace>/iteration-N --skill-name "name" --benchmark <path>/benchmark.json &`. Iteration 2+: add `--previous-workspace`.

**Step 5**: Read `feedback.json` when user done. Kill viewer. Empty feedback = fine.

### Improving

1. Generalize from feedback — don't overfit.
2. Keep prompt lean; cut unproductive parts from transcripts.
3. Explain the why behind instructions.
4. Repeated helper scripts across cases → bundle in `scripts/`.

Loop: improve → `iteration-N+1/` → viewer with `--previous-workspace` → review → repeat. Stop when user happy or no progress.

### Description Optimization

1. 20 eval queries (10 should-trigger, 10 should-not-trigger): realistic, detailed, tricky near-misses. Save `[{query, should_trigger}]`.
2. Review via `assets/eval_review.html`. Replace placeholders, write temp HTML, open. User exports `eval_set.json`.
3. Run: `python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <current-model> --max-iterations 5 --verbose`. 60/40 split, 3 runs/query, selects `best_description` by test score.
4. Apply to SKILL.md. Show before/after + scores.

Requires `claude` CLI. Queries must be substantive enough for skill consultation.

## Constraints

- No subagents: no parallel runs, skip baselines/benchmarks. Inline results. Skip description optimization.
- Blind comparison: optional, see `agents/comparator.md`.
- Package: `python -m scripts.package_skill <path>` (only if `stage_files`).

## References

- `agents/grader.md` — Assertion evaluation
- `agents/comparator.md` — Blind A/B comparison
- `agents/analyzer.md` — Benchmark patterns
- `references/schemas.md` — JSON schemas
