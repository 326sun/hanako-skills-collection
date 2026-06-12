---
name: office-documents
description: Read and edit PDF, DOCX, XLSX, XLSM, PPTX files via deterministic scripts. Triggers: open, edit, convert Office/PDF files.
default-enabled: true
---

# Office Documents

Read and modify document files using bundled Python worker scripts. No OfficeCLI or GUI viewer required.

## Core Workflow

1. Identify file type. Run `scripts/check_env.mjs --capability <cap>` for preflight.
2. Read: `python3 scripts/read_document.py input.file --format markdown`.
3. Edit: write JSON ops, run matching edit script. Save to new file unless overwrite explicit.
4. Verify: re-read output with `read_document.py`.

## Edit Operations

```json
// DOCX: replace_text, append_paragraph, add_table
[{"op":"replace_text","find":"old","replace":"new"}]

// XLSX: set_cell, set_formula, append_row, add_sheet, rename_sheet, set_style
[{"op":"set_cell","sheet":"Sheet1","cell":"B2","value":"Approved"}]

// PPTX: replace_text, set_shape_text, add_textbox
[{"op":"replace_text","find":"Q1","replace":"Q2"}]

// PDF: rotate_pages, extract_pages, delete_pages, merge, set_metadata
[{"op":"rotate_pages","pages":"1,3-4","degrees":90}]
```

## Format Support

| Format | Read | Edit Capability |
|--------|------|----------------|
| PDF `.pdf` | pdfplumber→pypdf | Rotate, extract, delete pages, merge, metadata |
| Word `.docx` | MarkItDown or OOXML | Text replace, append paragraph, add table |
| Excel `.xlsx/.xlsm` | MarkItDown or OOXML | Cell/formula, row, sheet, style ops |
| PPTX `.pptx` | MarkItDown or OOXML | Text replace, shape text, add textbox |

## Constraints

- Always run `check_env.mjs` first. Stop if `ok: false`; show `installGuidance`.
- Never auto-install dependencies.
- Unsupported: PDF text replacement, scanned OCR, macros/VBA, encrypted files, pivot tables, track-changes.
- XLSX formulas preserved but not calculated locally; state this.
- Large docs: read structure first, then narrow by sheet/slide/page.
