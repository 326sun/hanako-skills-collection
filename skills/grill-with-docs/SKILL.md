---
name: grill-with-docs
description: "Requirement alignment through iterative questioning: build shared glossary (CONTEXT.md), record architecture decisions (ADR) when warranted. Triggers: help me analyze, review this approach, is this correct, new feature, change plan, architecture proposal."
---

# Grill With Docs

Misalignment is the most expensive bug. This skill does three things:
1. Questions you one at a time until shared understanding is reached
2. Builds a project glossary (CONTEXT.md) to eliminate terminology drift
3. Writes ADRs only when genuinely needed — no document bloat

## Core Discipline

**One question at a time. Wait for feedback before the next.**

Never dump a list of questions. Each question builds on the previous answer.

**If you can answer a question by reading the codebase, read the codebase.** The user's time costs more than your token budget.

## Workflow

### Step 1: Explore Existing Documentation

Check for `CONTEXT.md` or `CONTEXT-MAP.md`. If `CONTEXT-MAP.md` exists, the project has multiple contexts — find the one relevant to the change.

### Step 2: Conduct the Interrogation

Start at the root of the design tree, work down branch by branch.

For each decision point:
- **Challenge vague terms.** User says "account" — is that Customer or User? Propose precise canonical terms.
- **Challenge glossary conflicts.** If CONTEXT.md defines "cancellation" as X but the user means Y, surface it immediately.
- **Stress-test with concrete scenarios.** Invent edge cases that force precision about concept boundaries.
- **Cross-reference code.** User says "it works like this" — check the code. Surface contradictions.
- **Always provide a recommended answer.** "I suggest defining X as Y because Z. Correct?"

### Step 3: Update CONTEXT.md Inline

Write definitions as they crystallize. Don't batch at session end.

CONTEXT.md is a pure glossary — no implementation details, no tech specs. If a new engineer can understand domain terms from it, it's good.

### Step 4: Write ADRs Sparingly

Only when ALL three are true:
1. Hard to reverse — changing later has meaningful cost
2. Surprising without context — future readers will ask "why?"
3. Result of a real trade-off — genuine alternatives existed, one was chosen for specific reasons

Missing any one → skip the ADR.

Format: `docs/adr/NNNN-short-title.md` with Background, Decision, Alternatives sections.

## Constraints

- Never dump a list of questions
- Never ask what the codebase can answer
- Never accept fuzzy terms without challenge
- Never turn CONTEXT.md into a spec document
- Never write ADRs that fail the three-condition test
