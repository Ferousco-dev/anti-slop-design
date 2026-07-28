# Changelog

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [1.1.0] — 2026-07-29

### Added

- `references/02-visual-patterns.md` — 20 visual slop patterns with severity levels, from the purple gradient and glassmorphism through floating blobs, neon glows, uniform radius, card-ification, badges, faded logo grids, and tilted dashboard mockups. Includes a nested-radius rule and a grep-able quick audit.
- `references/03-color-patterns.md` — the purple monoculture and its five converging causes; OKLCH ramp construction with a worked example; the 60-30-10 rule; custom neutral temperature; dark mode as a first-class system (elevation inverts, chroma reduces); WCAG contrast floors; the five-purpose color test.
- `references/04-typography-patterns.md` — Inter and 10 deliberate pairings plus single-family alternatives; optical sizing, tabular numerals, line-height scaling; the full buzzword and forbidden-phrase database; headline rules with real-world comparisons; hedging, passive voice, and academic transitions; placeholder copy including forgotten states.
- `references/05-layout-patterns.md` — the SaaS conveyor belt and six hero alternatives; footer, feature-grid, and spacing rhythm; bento grids with the contexts where they win and lose; scroll hijacking as an accessibility failure; container, sidebar, modal, tab, and accordion misuse.
- Severity taxonomy (CRITICAL / HIGH / MEDIUM / LOW) applied consistently across all taxonomy modules.
- Per-module "Quick audit" grep blocks for pre-emit self-checking.

### Changed

- `SKILL.md` reference table now routes to all five modules and states the severity scale.
- Em-dash guidance now separates the *discipline* (avoid in marketing copy) from the *myth* (em-dashes do not prove AI authorship — the reliable tell is cadence uniformity).

## [1.0.0] — 2026-07-29

### Added

- Initial skill: `anti-slop-design`
- `SKILL.md` entry point — one rule, six-step operating protocol, instant-reject list, non-negotiables
- `references/01-philosophy.md` — core philosophy module, covering:
  - The mechanism of slop: regression to the mean, the Tailwind `indigo-500` cascade, inherited library defaults, prompt underspecification
  - The Three Laws of Anti-Slop Design
  - The Anti-Slop Hierarchy of Needs
  - The "Would Stripe do this?" test, and the five decisions premium teams actually share
  - The measurable cost of slop: trust, brand, conversion, technical debt, accessibility
  - A ten-question self-interrogation script
  - Anti-anti-slop — guarding against over-correction
- MIT license, contributing guide, one-line installer
- CI: frontmatter validation, size budgets, link checking, markdown lint
- CD: automatic tagged release and `.zip` bundle on version bump

[1.1.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.1.0
[1.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.0.0
