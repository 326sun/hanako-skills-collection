---
name: journal-figures
description: "Journal-quality scientific figures: graphical abstracts, mechanism diagrams, TOC figures. Triggers: mechanism diagram, graphical abstract, journal figure, Nature-style figure, schematic, device architecture. NOT for data charts (use data-visualization)."
---

## Rules

- **Design philosophy**: Minimalist, high-contrast, publication-oriented. White/off-white background. Clean panel structure without decorative collage. Frameless legends, uncluttered axes. Sans-serif typography (Helvetica/Arial-like). Readable at single-column journal width.
- **Color semantics**: Use color to convey meaning, not decoration. Same color = same meaning across panels.

### Semantic Color Palette

| Color | Hex | Role |
|-------|-----|------|
| Deep Blue | `#0F4D92` | Primary method, central mechanism, key pathway |
| Medium Blue | `#3775BA` | Supporting mechanism, secondary pathway |
| Light Green | `#8BCF8B` | Improvement, favorable variant, beneficial state |
| Pale Green | `#AADCA9` | Background improvement region |
| Deep Red | `#B64342` | Baseline, contrast, competing route, adverse state |
| Pale Pink | `#F6CFCB` | Background adverse region |
| Light Gray | `#CFCECE` | Substrate, background categories, non-focal scaffolds |
| Dark Gray | `#4D4D4D` | Structural elements, borders, annotations |

### Nature-Style Alternative Palette

| Color | Hex | Role |
|-------|-----|------|
| Cobalt Blue | `#1F618D` | Main mechanism |
| Teal | `#148F77` | Beneficial pathway |
| Warm Orange | `#E67E22` | Contrast condition |
| Deep Crimson | `#922B21` | Adverse/competing |
| Slate Gray | `#7F8C8D` | Structural |

- **Layout**: Balanced multi-panel over single crowded canvas. Left-to-right narrative flow for comparisons. Consistent alignment and spacing across panels. Legends outside densest data region.
- **Simplification**: No perspective, glossy rendering, cinematic lighting, dramatic shadows, poster gradients, 3D effects, handwritten fonts, ornate arrows. Moderate saturation; bright accents only for focal points.

## Prompt Construction

When building prompts for image generation, embed these directives:

- White/off-white background, journal-style composition
- Consistent semantic color mapping (blue=mechanism, green=improvement, red=baseline)
- Concise professional labels in sans-serif
- Balanced panel structure, vector-friendly modular shapes
- No cinematic lighting, dramatic shadows, photorealistic backgrounds, poster gradients, ornate elements, 3D perspective, handwritten fonts, glossy rendering

### Figure-Type Short Templates

**Graphical Abstract / TOC**: Single-panel, clean schematic. White background. Key elements listed. Semantic colors. 16:9 or 4:3.

**Mechanism Diagram**: Left-to-right flow (input → intermediate → output). Clean causal arrows. Blue primary pathway, red competing pathway. Short component labels. 4:3 or 3:2.

**Device Architecture**: Multi-component layout, hierarchical/layered with clear boundaries. Dark gray structural outlines, blue fill for active components. Legend outside main diagram. 16:9 or 4:3.

**Multi-Panel Research Figure**: N panels in specified layout. Each panel described separately. Consistent color semantics, uniform label positioning, bold panel titles (a), (b), (c). 16:9 for horizontal.

## Chart Hints (for figure-internal chart elements)

- **Grouped bars**: Strong dark edges, compact legend outside data region, tight Y-axis limits, optional value labels above bars
- **Trend panels**: 2–4 curves, consistent line widths, optional shaded uncertainty bands, minimal grid
- **Heatmaps**: Clean cell grid, restrained colormap, legible row/column labels, no glossy effects
- **Print-safe**: Dark outlines + hatching/texture cues for similar fills; don't rely on red-vs-green alone

## Anti-Patterns

- Cinematic lighting, glossy 3D rendering, photorealistic backgrounds
- Ornate decorative arrows, poster gradients, handwritten fonts
- Inconsistent color semantics across panels
- Labels too small for single-column readability
- Legends overlapping dense data regions
- Decorative collage layout instead of structured panels
