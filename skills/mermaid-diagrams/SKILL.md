---
name: mermaid-diagrams
description: Generate Mermaid diagrams from natural language and export to PNG/SVG/PDF. Use when user asks for diagram, flowchart, sequence diagram, class diagram, ER diagram, state machine, architecture visualization, git graph, ç”»å›¾, æž¶æž„å›? æµç¨‹å›? æ—¶åºå›? Proactively use when explaining systems with 3+ components, API flows, authentication sequences, class hierarchies, database schemas, or state machines.
default-enabled: true
---

# Mermaid Diagrams

Generate `.mmd` text files and export to PNG/SVG/PDF using `mmdc` CLI or Kroki API.

**Key advantage:** Text-based syntax with fully automatic layout â€?no x/y coordinates needed.

## Prerequisites

**Option A: Local (mmdc)**
```bash
npm install -g @mermaid-js/mermaid-cli
npx puppeteer browsers install chrome-headless-shell
mmdc --version
```

**Option B: Kroki API (no install)**
```bash
curl --version  # Just need curl
```

## Workflow

1. Check deps â€?`mmdc --version` or fall back to Kroki
2. Pick diagram type from table below
3. Generate `.mmd` file
4. Validate syntax before export
5. Export to PNG/SVG/PDF
6. Show to user, iterate

## Validation (Required)
```bash
# With mmdc
mmdc -i diagram.mmd -o /tmp/test.png 2>&1

# With Kroki (if mmdc unavailable)
curl -s -X POST -H "Content-Type: text/plain" --data-binary @diagram.mmd https://kroki.io/mermaid/svg -o /tmp/test.svg && echo "Valid" || echo "Invalid"
```

## Diagram Types

| Type | Keyword | Use for |
|------|---------|---------|
| Flowchart | `flowchart TD/LR` | processes, pipelines, decisions |
| Sequence | `sequenceDiagram` | API calls, message passing |
| Class | `classDiagram` | OOP models, data structures |
| ER | `erDiagram` | database schemas |
| State | `stateDiagram-v2` | state machines, lifecycle |
| Gantt | `gantt` | project timelines |
| Pie | `pie` | proportions |
| Git Graph | `gitGraph` | branch strategies |
| Mind Map | `mindmap` | topic breakdowns |
| User Journey | `journey` | user-experience flows |

## Quick Examples

### Sequence Diagram (API Flow)
```mermaid
sequenceDiagram
  participant C as Client
  participant S as Server
  participant D as Database
  C->>S: POST /login {email, password}
  S->>D: SELECT user
  D-->>S: user record
  S-->>C: JWT token
```

### Flowchart (Architecture)
```mermaid
flowchart LR
  A[User] --> B[API Gateway]
  B --> C[Auth Service]
  B --> D[Business Logic]
  D --> E[(Database)]
  D --> F[(Cache)]
```

### State Diagram
```mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Processing: start
  Processing --> Success: ok
  Processing --> Error: fail
  Error --> Idle: retry
  Success --> [*]
```

## Export
```bash
# Local
mmdc -i diagram.mmd -o diagram.png -w 1200

# Kroki (PNG)
curl -s -X POST -H "Content-Type: text/plain" --data-binary @diagram.mmd https://kroki.io/mermaid/png -o diagram.png

# Kroki (SVG)
curl -s -X POST -H "Content-Type: text/plain" --data-binary @diagram.mmd https://kroki.io/mermaid/svg -o diagram.svg
```

## Common Errors
- Missing quotes around labels with special characters â†?use `A["Label with spaces"]`
- Wrong arrow syntax â†?sequence uses `->>`, flowchart uses `-->`
- Undeclared participants in sequence diagrams â†?declare all participants first