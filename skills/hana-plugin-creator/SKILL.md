---
name: hana-plugin-creator
description: Scaffold, develop, and publish Hana plugins. Triggers: create plugin, plugin scaffold, plugin dev, plugin SDK, 创建插件, 插件开发.
---

# Hana Plugin Creator

For Hana application plugins (not Codex `.codex-plugin` bundles).

## Rules

- Beginner mode: guided, plain language. Developer mode: concise, SDK-focused. Ask when uncertain.
- After delivery: state concrete value. Don't inflate praise.
- Read `.docs/PLUGIN-DEVELOPMENT.md`, `PLUGIN_SDK.md`, relevant `PLUGINS.md` before coding. For React: `packages/plugin-sdk/README.md`, `packages/plugin-components/README.md`.
- Dev authority from dev install slot (`${HANA_HOME}/plugins-dev/`), not manifest. User must enable "Allow Agent plugin dev tools".
- Declare needs in manifest `capabilities`. High-risk needs in `sensitiveCapabilities`.
- Static `tools/*.js`: export `name`, `description`, `parameters`, `execute`.
- Full-access: `"trust": "full-access"`. Extension runners rebind on next safe rebuild for idle sessions; in-flight replies won't pick up fresh code.
- EventBus handlers: return `HANA_BUS_SKIP` for irrelevant payloads.

## Capability Map

- Agent tools, slash commands, skills, agents, knowledge
- Iframe pages, widgets, cards (Hana theme)
- Lifecycle/EventBus (full-access)
- Session control: `createSession`, `listSessions`, `sendSessionMessage`, `subscribeSessionEvents`
- Agent control: `createAgent`, `updateAgent`
- Context injection: `sendSessionMessage(..., { context })` — no JSONL mutation
- Utility model: `sampleText()` for summarization/classification/routing
- Media: `listMediaProviders()`, `generateImage()`, `generateVideo()`, `transcribeAudio()`
- Provider contributions: `providers/*.js`
- Pi SDK extensions: `extensions/*.js`
- `SessionFile` outputs via `toolCtx.stageFile()`

Constraints: prefer runtime helpers over raw bus calls. Plugin-only sessions use `visibility: "plugin_private"`. Media-only providers set `chat.projection = "none"`. CLI providers use `runtime.kind = "local-cli"|"browser-cli"` with structured bindings.

## Workflow

1. Find Hana repo root (`PLUGIN_SDK.md`, `PLUGINS.md`, `packages/plugin-runtime`).
2. Preflight: `node skills2set/hana-plugin-creator/scripts/check_env.mjs --capability scaffold`. If `ok: false`, stop and show guidance. Don't auto-install.
3. Pick template: `direct` (no build), `guided-react`, `professional-react`.
4. Pick kind: `tool`, `ui`, `full`, `provider`.
5. Pick location: `plugins/<id>`, `examples/plugins/<id>`, or user plugins dir.
6. Scaffold: `python3 skills2set/hana-plugin-creator/scripts/create_hana_plugin.py "Name" --path examples/plugins --audience beginner --template direct --kind tool`. Options: `--sdk-mode workspace|bundled`, `--dev-scenario`, `--force` (only for explicit overwrite).
7. Dev loop: `plugin.dev.install` → edit → `plugin.dev.reload` → `plugin.dev.invokeTool` (smoke test) → `plugin.dev.diagnostics` → `plugin.dev.listSurfaces`.
8. UI debug: element-first (role/label/text), screenshots for visual polish.

## Constraints

- Iframe UI: self-contained, no `desktop/src/react` imports.
- React UI: `HanaThemeProvider mode="inherit"`.
- Marketplace: metadata in `OH-Plugins` repo. Privacy-push + user confirmation before any remote push.
