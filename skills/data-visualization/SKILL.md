---
name: data-visualization
description: "Scientific charts with matplotlib/seaborn: 600dpi, vector export, colorblind-friendly. Triggers: data visualization, 数据可视化, chart, plot, scientific figure, graph, histogram, boxplot, heatmap. NOT for schematics/conceptual figures (use journal-figures)."
---

## Rules

- Use matplotlib + seaborn. Set 600 DPI minimum. Export vector (PDF/EPS/SVG) for LaTeX publications.
- Serif fonts (Times New Roman or STIX). Chinese fonts: SimHei or Microsoft YaHei.
- Colorblind-friendly palettes: Set2, viridis, or cividis. Avoid red-green-only distinctions.

## Chart Selection

| Purpose | Chart |
|---------|-------|
| Distribution | Histogram, KDE, violin plot |
| Group comparison | Boxplot, bar chart with error bars, violin plot |
| Relationship/correlation | Scatter + regplot, line plot, hexbin |
| Matrix/correlation | Heatmap, clustermap |
| Composition | Stacked bar, pie/donut (≤5 categories) |
| Trend over time | Line plot with error bands |

## Workflow

1. Load and validate data. Check for NaN, outliers, column types.
2. Select chart type based on purpose.
3. Build figure: descriptive title, labeled axes with units, legend outside data region.
4. Apply colorblind-friendly palette. Ensure readable font sizes.
5. Export both PDF (for papers) and PNG (for quick preview).
6. Note any caveats: bin width choice, outlier handling, normalization method.
