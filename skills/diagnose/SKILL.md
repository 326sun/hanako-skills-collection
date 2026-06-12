---
name: diagnose
description: "High-discipline debugging: build feedback loop first, then reproduce, generate 3-5 falsifiable hypotheses, instrument, fix with regression test. Triggers: debug, troubleshoot, fix bug, error, performance regression, intermittent issue, broken, failing. MANDATORY: never fix without a feedback loop."
---

# Diagnose

## Phase 1 — Build a Feedback Loop

This is the skill. Everything else is mechanical. A fast, deterministic, agent-runnable pass/fail signal makes the bug solvable. No signal = guessing.

Spend disproportionate effort here. Be aggressive. Be creative. Refuse to give up.

### 10 Ways to Build a Loop (try in order)

1. **Failing test** at any seam that reaches the bug
2. **Curl/HTTP script** against a running dev server
3. **CLI invocation** with fixture input, diff stdout against known-good
4. **Headless browser script** (Playwright/Puppeteer) — drive UI, assert DOM/console/network
5. **Replay captured trace** — save real request/event log to disk, replay in isolation
6. **Throwaway harness** — minimal subset of system (one service + mocked deps), single function call
7. **Property/fuzz loop** — run 1000 random inputs, find failure mode
8. **Bisection harness** — automate "boot at state X, check" for `git bisect run`
9. **Differential loop** — same input, old vs new version, diff outputs
10. **HITL bash script** — last resort, drive human clicks with structured script

### Iterate on the Loop

Make it faster (cache setup, skip unrelated init), sharper (assert specific symptom, not "didn't crash"), more deterministic (pin time, seed RNG, isolate filesystem).

A 2-second deterministic loop is a debugging superpower. A 30-second flaky loop is barely useful.

### Non-Deterministic Bugs

Goal: raise reproduction rate, not perfect repro. Loop trigger 100x, parallelize, add stress, inject sleeps. 50% flaky is debuggable; 1% is not.

### When No Loop is Possible

Stop. State what you tried. Ask user for: (a) environment access, (b) captured artifact (HAR, log dump, core dump, screen recording), or (c) permission for temporary production instrumentation.

## Phase 2 — Reproduce

Run the loop. Confirm the failure matches the user's described symptom. Verify reproducibility.

## Phase 3 — Generate Hypotheses

Generate 3-5 ranked, falsifiable hypotheses before testing any. Single-hypothesis generation anchors on the first plausible idea.

Format: "If X is the cause, then changing Y will make the bug disappear / changing Z will make it worse."

Show the ranked list to the user before testing — cheap checkpoint, big time saver.

## Phase 4 — Instrument

Each probe maps to a specific Phase 3 prediction. Change one variable at a time.

Tool priority: debugger/REPL > targeted logs > never "log everything and grep."

Tag every debug log with unique prefix like `[DEBUG-a4f2]`. Cleanup is one grep.

For performance regressions: establish baseline measurement first, then bisect. Measure before fixing.

## Phase 5 — Fix + Regression Test

Write the regression test BEFORE the fix — but only if a correct seam exists. A correct seam exercises the real bug pattern. If no correct seam exists, note it — that's an architectural finding, not a testing failure.

Fix: one change at a time. No refactoring. No bundling.

## 3+ Failed Fixes = Architecture Problem

Stop. Signals: each fix reveals new coupling elsewhere, fixes need massive refactoring, each fix creates new symptoms. Discuss architecture with user.

## Red Flags — Return to Phase 1

- "Quick fix, investigate later"
- "Try changing X and see"
- "Multiple changes at once"
- "Skip the test, I'll manually verify"
- "Probably X, let me fix it"
- "One more fix attempt" (after 2 failures)

## Constraints

- Never fix without a feedback loop
- Never test a single hypothesis — generate 3-5
- Never change multiple variables at once
- Never force a regression test without a correct seam
- Never attempt fix #4 — escalate to architecture discussion
- Never refactor while RED
