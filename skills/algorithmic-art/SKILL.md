---
name: algorithmic-art
description: p5.js generative art via algorithmic philosophies. Flow fields, particle systems, seeded randomness. Triggers: generative art, algorithmic art, creative coding.
license: Complete terms in LICENSE.txt
---

# Algorithmic Art

Produce generative art in two steps: algorithmic philosophy → p5.js implementation.

## Step 1: Algorithmic Philosophy (`.md`)

- Name a 1–2 word movement (e.g. "Organic Turbulence").
- Write 4–6 paragraphs describing computational expression: noise functions, particle behaviors, field dynamics, temporal evolution, parametric variation.
- Emphasize craftsmanship: "meticulously crafted," "master-level implementation."
- Leave creative space for the implementation phase.

## Step 2: p5.js Implementation

- **Read `templates/viewer.html` first.** Use it as the literal starting point.
- Keep fixed sections: header, sidebar structure, Anthropic branding, seed controls, action buttons.
- Replace variable sections: p5.js algorithm, parameter definitions, UI controls.
- Output a single self-contained `.html` file with inline p5.js from CDN.

### Technical Requirements

- Always use `randomSeed(seed)` and `noiseSeed(seed)` for reproducibility.
- Define a `params` object with seed and tunable properties.
- Parameters: quantities, scales, probabilities, ratios, angles, thresholds.
- Build sidebar controls: parameter sliders, seed navigation (prev/next/random/jump), regenerate/reset/download buttons.

## Constraints

- Never create HTML from scratch — always start from `templates/viewer.html`.
- Never copy flow-field examples verbatim; build what the philosophy demands.
- Never skip seeding; same seed must produce identical output.
- One self-contained HTML artifact per piece. No external files except p5.js CDN.
