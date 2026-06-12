---
name: apple-minimal-ui
description: Apple-style minimal UI design for web, components, dashboards. Triggers: clean UI, minimal design, apple style. Never for scientific figures or data charts.
default-enabled: false
---

# Apple Minimal UI

Convey maximum hierarchy with minimum visual elements. Every pixel must justify its existence.

## Rules

### Color
- Base: Zinc or Stone. Single accent only, saturation ≤70%. No gradients for decoration.
- Dark mode: bg `zinc-950`, cards `zinc-900`, hover `zinc-800`. Text contrast ≥4.5:1.
- Accent pool: `#007AFF`, `#34C759`, `#FF6B35`, `#8B5CF6` (50% sat), or pure B&W.

### Typography
- Priority: Satoshi+JetBrains Mono, Geist+Geist Mono, Cabinet Grotesk, SF Pro.
- One family for hierarchy via weight variants. Never mix two families.
- Headings: `font-semibold/bold`, `tracking-tighter`. Body: `leading-relaxed` 1.6–1.75, `max-w-[65ch]`.

### Spacing
- Card padding min 24px, normal 32px, large 48px. Gaps: `gap-6`/`gap-8`, never `gap-4`.
- CSS Grid. Default: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`.
- Container: `max-w-7xl`. Hero: `min-h-[85dvh]`.

### Motion
- Serve only: direct attention, explain spatial relationships, confirm action results.
- Duration 150–300ms, never over 400ms. Easing: `cubic-bezier(0.25,0.1,0.25,1.0)`.
- Page entrance: `opacity 0→1` + `translateY(8px→0)`, stagger 50–80ms.

### Components
- Buttons: solid accent, `rounded-xl`, `px-6 py-3`. Never glow.
- Cards: bg one step lighter than page, border-over-shadow (`border-zinc-200/60`). Hover: `translateY(-2px)`.
- Inputs: `rounded-xl`, border `zinc-300`, focus ring accent.
- Icons: Phosphor or Heroicons, stroke-width 1.5. Never Lucide.

### Borders/Shadows
- Radius: page `rounded-3xl` → card `rounded-2xl` → button `rounded-xl` → badge `rounded-lg`.
- Shadows: `shadow-sm` max. Never `shadow-lg`/`shadow-2xl`. Replace heavy shadows with borders.

## Constraints

**Forbidden**: gradient glows, centered large titles on dark grids, three equal feature cards, glassmorphism, Inter default, infinite-loop animations, gradient text, >1 accent, serif defaults, Lucide icons, motion >500ms, `scale` >1.05.

**Quality checklist**: 1 accent? No gradient glows? Not Inter? Light shadows? Motion ≤400ms? Card padding ≥24px? No infinite loops? Dark bg = zinc-950? Consistent radii? No Lucide?
