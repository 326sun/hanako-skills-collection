---
name: journal-figures
description: "Publication-quality scientific figure design guide for journal submissions. Covers graphical abstracts, mechanism diagrams, device schematics, TOC figures, and journal-style illustrations. Trigger when user asks for 机制图, 图形摘要, 期刊配图, 示意图, graphical abstract, mechanism diagram, journal figure, scientific illustration, or Nature-style figure."
default-enabled: true
---

# Journal-Quality Scientific Figures

Design philosophy and prompt engineering for publication-ready scientific figures. This skill provides the aesthetic and structural framework for generating journal-style images through AI image generation tools (e.g., HanaAgent image-gen). It does NOT handle exact data plotting — that is the domain of data-visualization.

## When To Use This Skill

- Graphical abstracts and TOC figures
- Mechanism diagrams (device工作原理, 反应路径, 物理过程)
- Device architecture and system schematics
- Processing workflow illustrations
- Journal-style conceptual figures
- Scientific illustrations requiring consistent visual language

Do NOT use this for exact data charts (scatter, trend, bar, heatmap) — those belong to data-visualization.

## Core Design Philosophy

### Minimalist, High-Contrast, Publication-Oriented

- White or near-white background by default
- Clean panel structure, no decorative collage
- Frameless legends and uncluttered axes
- Short professional labels, not marketing copy
- Readable at single-column scale (typical journal column width)

### Typography

- Sans-serif typography (Helvetica or Arial-like)
- Clear label hierarchy:
  - **Panel labels and titles**: strongest emphasis, bold
  - **Axis or legend text**: medium emphasis
  - **Secondary notes**: smallest emphasis
- Avoid ornate fonts, handwritten fonts, and heavy 3D text effects
- All labels in clean, readable size

### Semantic Color Palette

Use color to convey meaning, not decoration. Keep the same meaning for the same color across all panels.

| Color | Hex | Semantic Role |
|-------|-----|---------------|
| Deep Blue | `#0F4D92` | Primary method, central mechanism, key pathway |
| Medium Blue | `#3775BA` | Supporting mechanism, secondary pathway |
| Light Green | `#8BCF8B` | Improvement, favorable variant, beneficial state |
| Pale Green | `#AADCA9` | Background improvement region |
| Deep Red | `#B64342` | Baseline, contrast, competing route, adverse state |
| Pale Pink | `#F6CFCB` | Background adverse region |
| Light Gray | `#CFCECE` | Substrate, background categories, non-focal scaffolds |
| Dark Gray | `#4D4D4D` | Structural elements, borders, annotations |

**Nature-style alternative palette** (higher contrast, suitable for multi-panel figures):

| Color | Hex | Role |
|-------|-----|------|
| Cobalt Blue | `#1F618D` | Main mechanism |
| Teal | `#148F77` | Beneficial pathway |
| Warm Orange | `#E67E22` | Contrast condition |
| Deep Crimson | `#922B21` | Adverse/competing |
| Slate Gray | `#7F8C8D` | Structural |

### Layout Logic

- Prefer balanced multi-panel compositions over single crowded canvas
- For comparison-heavy figures, use left-to-right narrative flow:
  1. Condition or processing state
  2. Structure or intermediate state
  3. Mechanism
  4. Property or performance outcome
- Keep legends outside the densest data region
- Use consistent alignment and spacing across panels for systematic feel

### Simplification Rules

- Remove unnecessary perspective, glossy rendering, and decorative textures
- Keep arrows clear and causal (straight or gently curved, not ornate)
- Keep iconography modular and editable-looking
- Use moderate color saturation; reserve bright accents for focal points
- No cinematic lighting, dramatic shadows, or photorealistic backgrounds
- No poster-style gradients unless explicitly requested

## Prompt Construction

When writing prompts for AI image generation (image-gen tool), include these directives:

### Must-Include Instructions

```
- White or off-white background
- Nature-style or journal-style composition
- Consistent semantic color mapping (blue=mechanism, green=improvement, red=baseline)
- Concise professional labels
- Balanced panel structure
- Vector-friendly modular shapes
- Minimal visual clutter
- Sans-serif typography
```

### Must-Avoid Instructions

```
- No cinematic lighting
- No dramatic shadows
- No photorealistic backgrounds
- No poster-style gradients
- No ornate decorative elements
- No 3D perspective effects
- No handwritten fonts
- No glossy rendering
```

### Figure-Type Prompt Templates

#### Graphical Abstract / TOC Figure

```
A journal-style graphical abstract showing [core finding].
Single-panel composition with clean schematic.
White background, Nature journal visual style.
Key elements: [element 1], [element 2], [element 3].
Semantic colors: blue for [mechanism], green for [benefit].
Concise labels in sans-serif font. Minimal visual noise.
16:9 or 4:3 aspect ratio.
```

#### Mechanism Diagram

```
A journal-style mechanism diagram illustrating [process name].
Left-to-right flow: [input] → [intermediate] → [output].
Clean arrows showing causal direction.
Semantic colors: blue for primary pathway, red for competing pathway.
Each component labeled with short professional text.
White background, no decorative elements.
4:3 or 3:2 aspect ratio.
```

#### Device Architecture / System Schematic

```
A journal-style device architecture diagram.
Multi-component layout showing [component A], [component B], [component C].
Layered or hierarchical arrangement with clear boundaries.
Dark gray structural outlines, blue fill for active components.
Concise component labels. Legend positioned outside main diagram area.
White background, Nature journal style.
16:9 or 4:3 aspect ratio.
```

#### Multi-Panel Research Figure

```
A balanced multi-panel journal figure with [N] panels arranged [layout].
Panel 1: [content], Panel 2: [content], Panel 3: [content].
Consistent color semantics across all panels.
Uniform label positioning and panel margins.
Sans-serif labels: bold for panel titles (a), (b), (c).
White background, clean separation between panels.
16:9 aspect ratio for horizontal layout.
```

## Chart Pattern Reference

When the figure includes chart-like elements, specify these patterns:

### Grouped Comparison Bars
- Grouped vertical bars with strong dark edges
- Compact legend (positioned outside data region)
- Short metric labels on axes
- Y-axis limits tightened to reveal differences
- Optional value labels above bars when the figure is stylized

### Trend Panels
- 2–4 primary curves per panel
- Consistent line widths across curves
- Optional shaded uncertainty bands
- Minimal grid or no grid
- Dedicated legend zone if plot is dense

### Heatmaps and Result Matrices
- Clean cell grid without excessive beveling
- Restrained colormap with readable contrast
- Legible row and column labels
- Simple colorbar if needed
- No glossy effects

### Print-Safe Separation
When multiple groups have similar fills:
- Use dark outlines
- Use different hatching or texture cues
- Do not rely solely on red-vs-green distinctions (colorblind safety)

## Integration with HanaAgent

When generating a journal figure:

1. **Determine figure type**: graphical abstract, mechanism diagram, device schematic, or multi-panel research figure
2. **Define the scientific narrative**: what is the core message this figure communicates?
3. **Build the prompt** using the templates above, customized to the specific content
4. **Call image-gen tool** with the constructed prompt, specifying appropriate aspect ratio and resolution
5. **Review output**: check color semantics, label readability, panel balance
6. **Iterate if needed**: adjust prompt to fix specific issues (e.g., "make the blue component more prominent", "reduce label font size")

For exact data plots (scatter, trend lines, bar charts with precise values), use data-visualization instead. This skill complements data-visualization by covering the conceptual/schematic figures that matplotlib cannot produce.

## Quality Checklist

Before finalizing a journal figure, verify:

- [ ] White background, no decorative elements
- [ ] Semantic colors used consistently (blue=mechanism, green=benefit, red=baseline)
- [ ] All labels in sans-serif font, readable at single-column width
- [ ] Arrows are clear and causal
- [ ] Panel layout is balanced with consistent margins
- [ ] No cinematic effects, glossy rendering, or 3D perspective
- [ ] Legend is outside the densest data region
- [ ] Figure communicates a single clear scientific narrative
