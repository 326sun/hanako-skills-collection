---
name: quiet-musing
description: "Deep reasoning framework for complex tasks: multi-step problems, high uncertainty, trade-off decisions. Triggers: deep thinking, complex problem, analyze complex problem, make decision, weigh options, debug hard bug, architecture design, strategy planning, think it through. Do NOT activate for simple Q&A, casual chat, or single-step tasks."
---

# Deep Reasoning Protocol

Structured reasoning framework for complex problems. Complementary to MOOD: MOOD captures intuition and emotion; this protocol handles structured reasoning.

## Activation Criteria

Activate when any of:
- Multiple reasonable solutions exist, requiring trade-offs
- Requirements are vague or implicit
- Decision involves architecture, strategy, or design
- Debugging requires systematic investigation
- Task affects multiple modules or has cascading effects
- User explicitly requests deep analysis

**Do NOT activate**: fixing a typo, answering a factual question, single-step operations. When uncertain, skip — complex protocols waste time on simple problems.

## Phase 1: Understand

- **Restate the problem in your own words**. If you can't, you haven't understood it.
- **Separate known from unknown**: what is confirmed? What are you guessing? What needs investigation?
- **Find the real problem**: what the user asks for and what they need are often different. "Add a button" may mean "this workflow is too long."
- **Mark uncertainty**: explicitly state what you're unsure about. Don't pretend to know everything.

If the problem itself is unclear at this stage, ask the user. Don't proceed with fuzzy understanding.

## Phase 2: Decompose

- **Identify sub-problems**: large problems typically break into 2–5 independent sub-problems.
- **Map dependencies**: what can be parallelized? What must be sequential?
- **Build a todo list**: each item should be completable in one sitting and independently verifiable.
  - ✓ Good: "Fix null guard in engine.js", "Add toast for archive failure"
  - ✗ Too fine: "Open engine.js", "Find line 1302", "Write if statement"
  - ✗ Too coarse: "Refactor entire frontend"

## Phase 3: Multi-Path Thinking

- **Generate at least two approaches**. Even when the first path looks right, spend 30 seconds considering alternatives.
- **Write trade-offs explicitly**: benefits, costs, risks for each path. One to two lines each.
- **Justify your choice**: "Choose A because XYZ; B also works but XYZ."
- **Stay reversible**: if execution reveals you chose wrong, switch paths. No sunk cost fallacy.

If all paths converge to the same answer, don't force a second. Multi-path thinking prevents blind spots, not performance art.

## Phase 4: Execute

- **Single-threaded**: do one thing at a time. Mark complete, then move to the next.
- **Dynamic adjustment**: add new problems to the todo as they emerge; remove items that become irrelevant. The list is alive.
- **Verify each step**: confirm correctness (run it, check it, test it) before proceeding.
- **Don't ram walls**: if a path is blocked, stop and analyze why. Don't keep hitting the same wall from different angles.

## Phase 5: Verify

- [ ] Does the actual result match the Phase 1 restatement?
- [ ] Are there missed edge cases?
- [ ] Did the changes introduce new problems?
- [ ] Was the user's real need satisfied?

## Reasoning Posture

**Think like a detective, not a judge.** Detectives follow evidence and allow their minds to change. Judges decide upfront. You are a detective until Phase 3 concludes.

**Errors are clues.** When you realize you were wrong, state it explicitly: "I assumed X, but the code shows otherwise, so I'm changing direction." Errors often expose more than correct reasoning.

**Depth matches complexity.** Shallow problems get shallow thought; complex problems get deep thought. Not every problem needs all 5 Phases. Changing a CSS color doesn't need multi-path thinking. Be adaptive, not dogmatic.

**Sync with the user.** Phase 1 and Phase 3 are natural alignment points. Uncertain? Ask. Multiple paths? Let the user choose. Don't finish in silence only to discover you went the wrong way.
