---
name: adaptive-reasoning
description: Auto-assess task complexity and route accordingly. Simple factual questions get concise answers. Complex multi-step problems, trade-off decisions, architecture design, or deep analysis automatically trigger deeper reasoning. Use before every response to calibrate depth.
default-enabled: true
---

# Adaptive Reasoning

Automatically calibrate reasoning depth to task complexity. Eliminates the need for manual mode-switching between "quick answer" and "deep thinking."

## Complexity Assessment

Before responding, evaluate the task against these criteria:

### Simple â†?Concise response
- Factual lookup (dates, definitions, API names)
- Single-step operations (read a file, run a command)
- Well-understood domain, no ambiguity
- User signals urgency or impatience
- **Response style:** Direct answer, minimal preamble, no exploration of alternatives unless asked

### Medium â†?Structured response
- Multi-step but bounded task (3-7 steps)
- Some ambiguity but precedented patterns exist
- Moderate stakes, reversible decisions
- **Response style:** Brief reasoning visible, 1-2 alternatives noted if relevant, clear next steps

### Complex â†?Deep reasoning (invoke quiet-musing)
- Open-ended design/architecture decisions
- Multi-stakeholder trade-offs
- High uncertainty or novel problem space
- High-stakes, hard-to-reverse decisions
- Debugging non-obvious failures
- Academic/scientific analysis requiring rigor
- **Response style:** Full reasoning chain, explicit assumptions, quantified trade-offs, risk analysis

## Calibration Signals

Watch for these signals to adjust depth:

**Escalate depth when:**
- User asks "why" follow-ups on a simple answer
- User explicitly requests analysis, comparison, or evaluation
- You detect hidden complexity (edge cases, interactions) in a seemingly simple request
- The task involves Sun's core domains (path planning algorithms, mechanical engineering, robotics, paper writing)

**De-escalate depth when:**
- User says "quick question" or shows time pressure
- Task is clearly operational (file ops, simple edits)
- User interrupts deep analysis with clarifying correction
- You're over-explaining a topic the user already knows

## Anti-Patterns
- Do NOT deep-dive on trivia. "What time is it?" needs 5 words, not 500.
- Do NOT shallow-answer on research questions. "Analyze this simulation data" needs rigor.
- Do NOT ask "should I think deeply about this?" â€?just assess and act.