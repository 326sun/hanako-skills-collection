---
name: mermaid-diagrams
description: Generate Mermaid diagrams from natural language, export to PNG/SVG/PDF. Triggers: draw diagram, architecture diagram, flowchart, sequence diagram, diagram, sequence, class diagram, ER, state machine, architecture, git graph. Proactive for 3+ component systems, API flows, auth sequences, class hierarchies, DB schemas, state machines.
---

# Mermaid Diagrams

Generate `.mmd` files and export via `mmdc` CLI or Kroki API.

## Rules

- Prerequisites: local `npm install -g @mermaid-js/mermaid-cli && npx puppeteer browsers install chrome-headless-shell` or Kroki (just `curl`).
- CJK fonts: `mmdc` uses headless Chromium. Tofu fix: `mermaid-config.json` with `"fontFamily": "Microsoft YaHei, SimHei, Noto Sans SC, sans-serif"`. Kroki: add `?fontFamily=Noto+Sans+SC`. Verify Windows fonts: `[System.Drawing.Text.InstalledFontCollection]::new().Families | ? { $_.Name -match 'YaHei|SimHei|SimSun' }`.
- Always validate before final export.

## Workflow

1. Check deps: `mmdc --version` or fall back to Kroki
2. Pick diagram type from table
3. CJK text? Prepare font config
4. Generate `.mmd` file
5. Validate: `mmdc -i diagram.mmd -o /tmp/test.png 2>&1` (or POST to `https://kroki.io/mermaid/svg`)
6. Export, show, iterate

## Diagram Types

| Type | Keyword | Use for |
|------|---------|---------|
| Flowchart | `flowchart TD/LR` | processes, pipelines |
| Sequence | `sequenceDiagram` | API calls, messaging |
| Class | `classDiagram` | OOP models |
| ER | `erDiagram` | DB schemas |
| State | `stateDiagram-v2` | state machines |
| Gantt | `gantt` | timelines |
| Pie | `pie` | proportions |
| Git Graph | `gitGraph` | branch strategies |
| Mind Map | `mindmap` | topic breakdowns |
| User Journey | `journey` | UX flows |

## Examples

```
sequenceDiagram
  participant C as Client
  participant S as Server
  participant D as Database
  C->>S: POST /login {email, password}
  S->>D: SELECT user
  D-->>S: user record
  S-->>C: JWT token
```

```
flowchart LR
  A[User] --> B[API Gateway]
  B --> C[Auth Service]
  B --> D[Business Logic]
  D --> E[(Database)]
  D --> F[(Cache)]
```

## Export

```bash
mmdc -i diagram.mmd -o diagram.png -w 1200 -c mermaid-config.json  # local + CJK
mmdc -i diagram.mmd -o diagram.png -w 1200                          # local, no CJK
curl -s -X POST "https://kroki.io/mermaid/png" --data-binary @diagram.mmd -o diagram.png
curl -s -X POST "https://kroki.io/mermaid/svg" --data-binary @diagram.mmd -o diagram.svg
```

## Constraints

- Labels with special chars need quotes: `A["Label with spaces"]`
- Wrong arrows: sequence uses `->>`, flowchart uses `-->`
- Undeclared sequence participants: declare all first
- CJK tofu: add `fontFamily` in config
