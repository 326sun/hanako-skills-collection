---
name: thesis-docx
description: "Format thesis/dissertation Word docs: normalize styles, captions, page numbers, section levels, Mermaid figures, LaTeX listings. Triggers: Word formatting, thesis formatting, Word, docx formatting."
---

## Rules

- Prefer Microsoft Word desktop automation over WPS. WPS degrades layout fidelity for thesis formatting.
- **Audit first, edit second.** Never make broad formatting changes before understanding the document's internal state.
- **Styles are the single source of truth.** Reduce direct formatting; bring the document under style control.
- Edit content only from user-provided facts. Never invent experimental data, system structure, or results.
- Write in normal thesis voice, not AI-workflow voice. Forbidden: "based on existing code", "per the provided outline", "according to your requirements", or any wording that sounds like prompt notes.
- **Verify page-level output** before claiming completion. Export to PDF and review every page.

## Workflow

1. **Check Word availability**: Run `powershell -ExecutionPolicy Bypass -File scripts/check_word_com.ps1 -Json`. If Word/COM/DOM is unavailable, stop and tell the user to install desktop Microsoft Word.
2. **Collect constraints**: Thesis template, school formatting guide, screenshots, existing document, sample pages, explicit chapter rules. Classify into:
   - `must enforce`: school guide, template, user-confirmed rules
   - `preserve current state`: anything the guide does not define
3. **Audit OOXML**: Run `scripts/audit_docx_ooxml.py` before bulk edits. Detect hidden indentation, section drift, stale REF display text, style-ID mismatches.
4. **Standardize via styles**: Reuse and repair existing styles. Create missing styles only when no match exists. Logical style buckets: `Body Text`, `Heading 1/2/3`, `Figure Caption`, `Table Caption`, `References`, `Abstract`, `Keywords`, `Appendix Title`. Before changing any style globally, inspect for direct paragraph formatting overrides.
5. **Generate figures**: Use Mermaid for architecture, E-R, flow, and state diagrams. Every node/field/relation must trace to user-provided material (code, schema, docs). If materials are insufficient, refuse and ask.
6. **Typeset code**: Use LaTeX conventions. Keep only code relevant to the argument. Preserve real identifiers. No synthetic filler code.
7. **Final audit**: Structure audit (styles, captions, references, page numbers, cross-references, hidden paragraph overrides). Export to PDF. Review page by page. Only then claim completion.

## High-Risk Pitfalls

- Style names that look correct but map to wrong style IDs
- Paragraph-level direct formatting that overrides intended style
- `firstLineChars` or numbering indentation creating invisible extra indents
- TOC/cross-reference fields showing stale display text
- Section-level first-page settings silently removing headers or page numbers
- Word vs. WPS differences in table row height, vertical alignment, code box clipping
- Punctuation normalization accidentally rewriting DOIs, URLs, code, or English references

## Quality Gates

Before claiming completion:
- [ ] Document is style-driven after all edits
- [ ] Captions, numbering, page breaks, TOC are coherent
- [ ] Cross-references display correct target labels, not stale field text
- [ ] Section settings don't silently remove page headers/numbers
- [ ] References match school rules; DOI/English references undamaged
- [ ] Every diagram and code block is grounded in user material
- [ ] PDF exported and inspected page by page
- [ ] If Word automation or PDF verification was unavailable, explicitly warn about unverified layout fidelity
