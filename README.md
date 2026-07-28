<div align="center">

# Anti-Slop Design

**A Claude Agent Skill that stops your AI from shipping the same purple-gradient website as everyone else.**

[![Validate](https://github.com/Ferousco-dev/anti-slop-design/actions/workflows/validate.yml/badge.svg)](https://github.com/Ferousco-dev/anti-slop-design/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Agent%20Skill-d97757)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

</div>

---

## The problem

Ask any AI to "build a modern landing page" and you get the same site every time:

> Purple→indigo gradient hero · Inter headline · centered badge → heading → gray subheading → two buttons · three identical feature cards with icons · 1px gray borders on everything · glassmorphic nav · fade-in-on-scroll on every section.

That is not a style. It is **regression to the mean** — the model emitting the statistically most common interface in its training data. The web has a name for it now: **AI slop**.

It costs real things. Users form a first impression in ~50ms and mostly from visual design. Generic design reads as automated, and automated increasingly reads as untrustworthy. Slop erodes credibility, dilutes brand, suppresses conversion, and reliably fails accessibility.

## What this skill does

`anti-slop-design` installs as a [Claude Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Once installed, Claude loads it automatically whenever you generate, review, or refactor UI — and it changes how the model decides.

It gives the agent:

- **A hard rejection list** of the specific patterns that mark output as AI-generated
- **An operating protocol** that forces a named visual direction *before* any code, so sampling never falls back to the mode
- **A design-decision framework** — the Hierarchy of Needs, the "Would Stripe do this?" test, the self-interrogation script
- **A mechanism-level explanation** of *why* slop happens (the Tailwind `indigo-500` cascade, inherited library defaults, prompt underspecification), so the agent can generalize to patterns not on the list
- **Non-negotiable floors** for accessibility, performance, and durability

It does not make your AI weird. Over-correction — brutalism on a medical dashboard, scroll-jacking on a pricing page — is its own failure mode, and the skill guards against that too. The target is **intentionality**, not deviation.

## Install

### Claude Code (project-level)

```bash
git clone https://github.com/Ferousco-dev/anti-slop-design.git /tmp/anti-slop-design && cp -r /tmp/anti-slop-design/skills/anti-slop-design .claude/skills/
```

### Claude Code (all your projects)

```bash
git clone https://github.com/Ferousco-dev/anti-slop-design.git /tmp/anti-slop-design && mkdir -p ~/.claude/skills && cp -r /tmp/anti-slop-design/skills/anti-slop-design ~/.claude/skills/
```

### One-liner installer

```bash
curl -fsSL https://raw.githubusercontent.com/Ferousco-dev/anti-slop-design/main/install.sh | bash
```

Pass `--project` to install into `./.claude/skills` instead of your home directory.

### Claude.ai / Claude Desktop

Download the `.zip` from the [latest release](https://github.com/Ferousco-dev/anti-slop-design/releases/latest) and upload it under **Settings → Capabilities → Skills**.

Verify with `/skills` in Claude Code — you should see `anti-slop-design` listed.

## Usage

There is nothing to invoke. The skill triggers on its own when you say things like:

- *"Build the landing page for this."*
- *"This dashboard looks AI-generated — fix it."*
- *"Review this component for design quality."*
- *"Make this feel premium."*
- *"Give this some personality."*

To force it in Claude Code:

```text
/anti-slop-design
```

### What changes

Without it:

> Centered hero, `bg-gradient-to-r from-indigo-500 to-purple-600`, Inter 700, three `<Card>` components in a grid, `motion.div` with `initial={{opacity:0,y:20}}`.

With it: Claude names a visual thesis first, derives a type/space/color system, designs all eight interaction states, and closes by telling you which decisions it made and why — so you can argue with them.

## Repo structure

```text
anti-slop-design/
├── skills/
│   └── anti-slop-design/
│       ├── SKILL.md              # entry point — loaded on trigger
│       └── references/          # loaded on demand
│           ├── 01-philosophy.md
│           ├── 02-visual-patterns.md
│           ├── 03-color-patterns.md
│           ├── 04-typography-patterns.md
│           └── 05-layout-patterns.md
├── scripts/validate_skill.py     # CI validator
├── .github/workflows/            # validate + release automation
└── install.sh
```

The skill uses **progressive disclosure**: `SKILL.md` stays small so it costs almost nothing in context, and the deeper reference modules load only when the agent actually needs them.

## Modules

| # | Module | Covers | Status |
|---|---|---|---|
| 01 | Core Philosophy | Why slop happens, the three laws, cost analysis, self-interrogation | ✅ Stable |
| 02 | Visual Patterns | 20 banned treatments: gradients, glassmorphism, blobs, glows, radius, shadows, badges | ✅ Stable |
| 03 | Color Patterns | The purple monoculture, OKLCH ramps, 60-30-10, neutrals, dark mode, contrast | ✅ Stable |
| 04 | Typography, Voice & Copy | Inter, pairings, alignment, the buzzword database, headlines, cadence uniformity | ✅ Stable |
| 05 | Layout Patterns | The SaaS conveyor belt, hero alternatives, bento, spacing rhythm, scroll hijacking | ✅ Stable |
| 06 | Component & Element Patterns | — | 🚧 Planned |
| 07 | Animation & Motion Patterns | — | 🚧 Planned |
| 08 | Code-Level & Technical Patterns | — | 🚧 Planned |
| 09 | Image & Media Patterns | — | 🚧 Planned |
| 10 | The Craft List | — | 🚧 Planned |
| 11 | Section-by-Section Rules | — | 🚧 Planned |
| 12 | Pre-Emit Self-Critique Checklist | — | 🚧 Planned |

## Contributing

New banned patterns are the most valuable contribution. If you can screenshot a tell that marks output as AI-generated, open a PR against the relevant reference module. See [CONTRIBUTING.md](CONTRIBUTING.md).

Every PR is gated by CI: frontmatter validation, size budgets, link checking, and markdown lint.

## License

[MIT](LICENSE) — use it, fork it, ship it commercially. Attribution appreciated, not required.

---

<div align="center">
<sub>Built by <a href="https://github.com/Ferousco-dev">Feranmi</a> · AppMD</sub>
</div>
