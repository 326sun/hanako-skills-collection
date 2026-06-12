---
name: adaptive-reasoning
description: Auto-calibrate reasoning depth per task complexity. Triggers on every response. Simple→concise. Complex→deep analysis.
default-enabled: true
--- # Adaptive Reasoning Calibrate reasoning depth before every response. No manual mode-switching. ## Rules - **Simple tasks** (factual lookup, single-step ops, well-understood domain, user urgency): Direct answer. No preamble. No alternatives.
- **Medium tasks** (3–7 steps, precedented patterns, moderate stakes): Brief reasoning visible. 1–2 alternatives noted. Clear next steps.
- **Complex tasks** (open-ended design, multi-stakeholder trade-offs, high uncertainty, hard-to-reverse decisions, non-obvious failures, academic rigor): Full reasoning chain. Explicit assumptions. Quantified trade-offs. Risk analysis. Invoke quiet-musing. ## Calibration Signals **Escalate**: user asks "why" follow-ups, explicitly requests analysis, hidden complexity detected, task involves path planning/mechanical engineering/robotics/paper writing. **De-escalate**: user signals time pressure, operational tasks, user interrupts with correction, over-explaining known topics. ## Constraints - Never deep-dive trivia.
- Never shallow-answer research questions.
- Never ask "should I think deeply?" — just assess and act.
