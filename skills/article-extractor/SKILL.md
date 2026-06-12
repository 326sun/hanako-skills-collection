---
name: article-extractor
description: Extract clean article content from URLs, removing navigation/ads/clutter. Triggers: download article, extract content, save blog post.
default-enabled: true
---

# Article Extractor

Extract main content from web articles. Save as clean `.txt` with article title as filename.

## Rules

### Priority Order
1. `reader` (Mozilla Readability CLI) — best for most articles
2. `trafilatura` (Python) — best for non-English or unusual layouts
3. Fallback `curl` + HTML parser — no dependencies, least reliable

### Install Check
- `reader`: `npm install -g @mozilla/readability-cli`
- `trafilatura`: `pip3 install trafilatura`

### Extraction
```bash
# reader
reader "URL" > article.txt

# trafilatura
trafilatura --URL "URL" --output-format txt > article.txt

# fallback: curl + python HTMLParser stripping script/style/nav/header/footer/aside
```

### Title + Filename
```bash
# reader
TITLE=$(reader "URL" | head -n 1 | sed 's/^# //')

# trafilatura
TITLE=$(trafilatura --URL "URL" --json | python3 -c "import json,sys; print(json.load(sys.stdin)['title'])")

# Clean: strip / : ? " < > |, trim to 100 chars, append .txt
```

## Constraints

- Always verify extracted content for completeness, especially paywalled/JS-heavy sites.
- Never auto-install missing dependencies; report what's needed.
- Check tool availability before extraction; fall back in order.
