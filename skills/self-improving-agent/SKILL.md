---
name: self-improving-agent
description: Captures learnings, errors, and corrections to enable continuous improvement across sessions. Use when a command fails, you correct me, I discover outdated knowledge, or a better approach is found. Reviews learnings before major tasks.
default-enabled: true
---

# Self-Improvement Skill

Log learnings and errors for continuous improvement. When I make mistakes, you correct me, or I discover better approaches, record them so future sessions benefit.

## When to Log

| Situation | Action |
|-----------|--------|
| Command/operation fails | Log error with context and fix |
| You correct me | Log as `correction` learning |
| Knowledge was outdated | Log as `knowledge_gap` |
| Found better approach | Log as `best_practice` |
| You request missing feature | Log feature request |
| Recurring pattern detected | Log with pattern-key for tracking |

## Logging Format

Use `record_experience` tool for quick one-line learnings. For detailed issues, use structured format:

### Learning Entry
```
## [LRN-YYYYMMDD-XXX] category
**Priority**: low | medium | high | critical
**Summary**: One-line description
**Details**: What happened, what was correct
**Suggested Action**: Specific fix
**Tags**: tag1, tag2
```

### Error Entry
```
## [ERR-YYYYMMDD-XXX] component
**Priority**: high
**Summary**: What failed
**Error**: Actual error message
**Context**: What was attempted
**Suggested Fix**: If identifiable
```

## Self-Check Before Major Tasks

Before starting complex work (multi-file edits, new features, architecture decisions), quickly scan recent learnings for relevant corrections or best practices. Apply proactively.