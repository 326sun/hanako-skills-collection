---
name: mcp-builder
description: Build MCP servers for LLM-tool integration. Triggers: MCP server, build MCP, FastMCP, MCP tool, MCP protocol.
---

# MCP Server Development

Create MCP servers enabling LLMs to interact with external services. Quality metric: how well LLMs accomplish real-world tasks.

## Rules

- Prioritize comprehensive API coverage over specialized workflow tools. Agents compose better with full coverage.
- Use consistent tool prefixes: `github_create_issue`, `github_list_repos`. Action-oriented names.
- Tool descriptions must be concise. Support filtering/pagination. Return focused data.
- Error messages must guide agents toward solutions with specific next steps.
- **Recommended**: TypeScript (strong SDK, broad compatibility, good AI codegen). Python (FastMCP) as alternative.
- Transport: Streamable HTTP (stateless JSON) for remote; stdio for local.
- Input schemas: Zod (TS) or Pydantic (Python) with constraints, descriptions, examples.
- Output: define `outputSchema` where possible, use `structuredContent` in TS SDK.
- Annotations: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

## Workflow

### Phase 1: Research

1. Study MCP spec: fetch `https://modelcontextprotocol.io/sitemap.xml`, then key pages with `.md` suffix (specification, transport, tool definitions).
2. Load framework docs:
   - TS SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
   - Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
   - Best practices: `reference/mcp_best_practices.md`
3. Study target API: endpoints, auth, data models. Use web search + WebFetch.
4. Plan: list endpoints, prioritize most common operations.

### Phase 2: Implementation

1. Set up project structure per language guide (`reference/node_mcp_server.md` or `reference/python_mcp_server.md`).
2. Build shared infrastructure: API client with auth, error handling, response formatting (JSON/Markdown), pagination.
3. Implement tools one by one: input schema → output schema → description → async implementation → annotations.

### Phase 3: Review & Test

- Code quality: DRY, consistent errors, full types, clear descriptions.
- Build: `npm run build` (TS) or `python -m py_compile server.py` (Python).
- Test: `npx @modelcontextprotocol/inspector` for both stacks.

### Phase 4: Evaluations

Create 10 complex, realistic, read-only questions requiring multiple tool calls. Each must be independent, verifiable by string comparison, with stable answers.

1. List tools → understand capabilities
2. Explore data with read-only operations
3. Generate 10 questions + verify answers yourself
4. Output XML: `<evaluation><qa_pair><question>...</question><answer>...</answer></qa_pair>...</evaluation>`

See `reference/evaluation.md` for full guide.

## Constraints

- Questions must not depend on other questions
- Only non-destructive operations
- Single clear answer per question
- See language-specific guides for quality checklists

## References

- `reference/mcp_best_practices.md` — Naming, response formats, pagination, transport, security
- `reference/node_mcp_server.md` — TypeScript project structure, Zod patterns, tool registration, examples
- `reference/python_mcp_server.md` — Python/FastMCP patterns, Pydantic, `@mcp.tool`, examples
- `reference/evaluation.md` — Question creation, answer verification, XML format, eval scripts
