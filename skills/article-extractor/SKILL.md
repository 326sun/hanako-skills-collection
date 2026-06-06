---
name: article-extractor
description: Extract clean article content from URLs (blog posts, articles, tutorials) and save as readable text. Use when user wants to download, extract, or save an article/blog post from a URL without ads, navigation, or clutter.
default-enabled: true
---

# Article Extractor

This skill extracts the main content from web articles and blog posts, removing navigation, ads, newsletter signups, and other clutter. Saves clean, readable text.

## When to Use This Skill

Activate when the user:
- Provides an article/blog URL and wants the text content
- Asks to "download this article"
- Wants to "extract the content from [URL]"
- Asks to "save this blog post as text"
- Needs clean article text without distractions

## How It Works

### Priority Order:
1. Check if tools are installed (reader or trafilatura)
2. Download and extract article using best available tool
3. Clean up the content (remove extra whitespace, format properly)
4. Save to file with article title as filename
5. Confirm location and show preview

## Installation Check

Check for article extraction tools in this order:

### Option 1: reader (Recommended - Mozilla's Readability)

```bash
command -v reader
```

If not installed:
```bash
npm install -g @mozilla/readability-cli
```

### Option 2: trafilatura (Python-based, very good)

```bash
command -v trafilatura
```

If not installed:
```bash
pip3 install trafilatura
```

### Option 3: Fallback (curl + simple parsing)

If no tools available, use basic curl + text extraction (less reliable but works)

## Extraction Methods

### Method 1: Using reader (Best for most articles)

```bash
reader "URL" > article.txt
```

Based on Mozilla's Readability algorithm. Excellent at removing clutter while preserving article structure.

### Method 2: Using trafilatura (Best for blogs/news)

```bash
# Extract article
trafilatura --URL "URL" --output-format txt > article.txt

# Or with more options
trafilatura --URL "URL" --output-format txt --no-comments --no-tables > article.txt
```

Options:
- `--no-comments`: Skip comment sections
- `--no-tables`: Skip data tables
- `--precision`: Favor precision over recall
- `--recall`: Extract more content (may include some noise)

### Method 3: Fallback (curl + basic parsing)

```bash
# Download and extract basic content
curl -s "URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            if tag in {'p', 'article', 'main', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                self.in_content = True
        self.current_tag = tag

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > article.txt
```

## Getting Article Title

Extract title for filename:

### Using reader:
```bash
TITLE=$(reader "URL" | head -n 1 | sed 's/^# //')
```

### Using trafilatura:
```bash
TITLE=$(trafilatura --URL "URL" --json | python3 -c "import json, sys; print(json.load(sys.stdin)['title'])")
```

### Using curl (fallback):
```bash
TITLE=$(curl -s "URL" | grep -oP '<title>\K[^<]+' | sed 's/ - .*//' | sed 's/ | .*//')
```

## Filename Creation

Clean title for filesystem:
```bash
TITLE="Article Title from Website"
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '-' | cut -c 1-100 | sed 's/ *$//')
FILENAME="${FILENAME}.txt"
```

## Complete Workflow

```bash
ARTICLE_URL="https://example.com/article"

# Check for tools
if command -v reader &> /dev/null; then
    TOOL="reader"
elif command -v trafilatura &> /dev/null; then
    TOOL="trafilatura"
else
    TOOL="fallback"
fi

# Extract article
case $TOOL in
    reader)
        reader "$ARTICLE_URL" > temp_article.txt
        TITLE=$(head -n 1 temp_article.txt | sed 's/^# //')
        ;;
    trafilatura)
        TITLE=$(trafilatura --URL "$ARTICLE_URL" --json | python3 -c "import json,sys; print(json.load(sys.stdin)['title'])")
        trafilatura --URL "$ARTICLE_URL" --output-format txt > temp_article.txt
        ;;
    fallback)
        TITLE=$(curl -s "$ARTICLE_URL" | grep -oP '<title>\K[^<]+' | sed 's/ - .*//; s/ | .*//')
        curl -s "$ARTICLE_URL" | python3 -c "
from html.parser import HTMLParser
import sys
class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags and tag in {'p', 'article', 'main', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
            self.in_content = True
    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())
    def get_content(self):
        return '\n\n'.join(self.content)
parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > temp_article.txt
        ;;
esac

# Clean filename
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '-' | cut -c 1-100 | sed 's/ *$//')
FILENAME="${FILENAME}.txt"

# Save final file
mv temp_article.txt "$FILENAME"
echo "Article saved to: $FILENAME"
```

## Notes
- reader (Mozilla Readability) produces the cleanest output for most articles
- trafilatura handles edge cases better (non-English content, unusual layouts)
- The fallback method works without any dependencies but is less reliable
- Always check extracted content for completeness, especially with paywalled or JS-heavy sites