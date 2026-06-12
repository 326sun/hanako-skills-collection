---
name: data-analysis
description: Scientific data analysis with pandas/numpy/scipy. Triggers: data analysis, statistics, data processing.
default-enabled: true
---

# Data Analysis

Use pandas, numpy, scipy for scientific data analysis.

## Workflow

1. **Inspect**: Check shape, dtypes, missing values, duplicates. Use `.info()`, `.describe()`, `.isna().sum()`.
2. **Clean**: Handle missing values, remove duplicates, fix dtypes, filter outliers.
3. **Explore**: Distributions, correlations, group-by aggregations. Visualize with matplotlib/seaborn.
4. **Test**: Check normality (Shapiro-Wilk, Kolmogorov-Smirnov) before choosing parametric/non-parametric tests.
5. **Export**: Save cleaned data and results. Document all transformations.

## Constraints

- Always report effect sizes alongside p-values.
- Always check normality before selecting statistical tests.
- Never apply parametric tests to non-normal data without transformation or non-parametric fallback.
- Document every transformation step.
