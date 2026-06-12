---
name: subagent-driven-development
description: Dispatch per-plan-task subagents with mandatory two-stage review (spec compliance then code quality). Triggers: execute plan, implement tasks, subagent dev, 按计划执行, 子agent开发, 分发任务. Requires approved plan.
---

# Subagent-Driven Development

Execute each plan task via a clean subagent. Mandatory two-stage review after every task: spec compliance first, then code quality. Only mark complete when both pass.

## Rules

**When to use** (all three required):
- Approved implementation plan exists (tasks decomposed, independent)
- Tasks are loosely coupled
- No session/environment switch needed

Not for: tightly coupled tasks, unclear plans, decisions between every task.

**Model selection:**
- Mechanical (single file, clear spec) → fast/cheap model
- Integration (multi-file, cross-module) → standard model
- Architecture/Review (design judgment) → strongest model

**Implementer status handling:**
- DONE → proceed to spec review
- DONE_WITH_CONCERNS → address correctness issues first, record observations, proceed
- NEEDS_CONTEXT → supply context, re-dispatch
- BLOCKED → supply context, upgrade model, decompose, or escalate. Never retry unchanged.

## Workflow

```
Phase 0: Extract all task text → create TodoWrite
Phase 1-N (per task):
  Dispatch implementer (see implementer-prompt.md)
    → NEEDS_CONTEXT: supply context, re-dispatch
    → BLOCKED: supplement/upgrade/decompose/escalate
    → DONE_WITH_CONCERNS: address correctness issues, record observations, proceed
    → DONE:
      Stage 1: Spec compliance review (spec-reviewer-prompt.md)
        → Issues: same implementer fixes, same reviewer re-reviews → repeat
      Stage 2: Code quality review (code-quality-reviewer-prompt.md)
        → Issues: same loop until approved → mark complete
After all tasks: final overall review
```

Don't pause between tasks. Execute continuously. Stop only for genuine BLOCKED without self-resolution.

## Constraints

- Never skip a review stage
- Never accept "close enough" on spec compliance
- Never run code quality review before spec compliance
- Never dispatch parallel implementers (will conflict)
- Never make subagents read the plan file (provide full text)
- Never retry unchanged on BLOCKED
- Never move to next task with open review issues
- Review loops: same implementer fixes, same reviewer re-reviews

## References

- `implementer-prompt.md` — dispatch template, self-review checklist, report format
- `spec-reviewer-prompt.md` — compliance checklist (missing/extra/misunderstanding, file:line)
- `code-quality-reviewer-prompt.md` — quality dimensions (responsibility, structure, bloat, naming)
