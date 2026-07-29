# Changelog

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [2.0.0] — 2026-07-29

### Added

- `references/08-copywriting-patterns.md` — the copywriting module. Temporal filler openings; the "it's not just X, it's Y" formula; lists of three; cadence uniformity as the primary diagnostic; voice without sacrificing correctness; vague claims and their legal exposure; "Imagine if", "We believe", "We are", "Our Mission"; the FAQ crutch; generic CTAs; placeholder copy; fake testimonials and case studies; SEO filler; press-release tone; a curated corporate-speak list; and a 14-point generated-tone checklist with a rewrite procedure.
- A note in `SKILL.md` and the README explaining that APK, permission, and mobile-security examples throughout the modules come from AppMD, the project the skill was authored for, and are illustrations rather than requirements.

### Changed

- **BREAKING (organizational):** module 04 is now **Typography only**. All word-level guidance moved to module 08. Module 04 previously held both, duplicating §2.7 of the source material.
- Module 04 gained real typographic depth in place of the moved copy sections: type-scale construction with a worked ratio scale, line height and tracking that scale inversely with size, measure, tabular numerals, fallback metric matching to prevent layout shift, and an accessibility floor (16px body minimum, no light weights for body, no text baked into images, heading levels chosen semantically).
- Em-dash guidance moved to §8.21, keeping the discipline and the correction that it is not a detector.

### Removed

- The source material's ~820-term corporate-speak list, which degenerated into generated filler ("randomness by design", "buttressing by design") and swept in legitimate technical vocabulary (Kubernetes, Docker, TLS, encryption at rest, caching, logging). Replaced with a curated list of genuine corporate speak plus a general test, and an explicit note that precise technical terms are the opposite of jargon.

## [1.2.0] — 2026-07-29

### Added

- `references/06-component-patterns.md` — the SaaS triad and cookie-cutter cards; pricing dark patterns ("Most Popular" ribbons, decoy tiers, hidden overage terms); avatar stacks and fake social proof; cookie banners where reject must be as easy as accept; carousels backed by Nielsen Norman research (~1% engage the first slide, well under 0.5% reach the second); toggles, skeletons, spinners, toasts, tooltips, badges, progress and step indicators; empty states as the highest-leverage onboarding moment; error states as a trust-critical touchpoint.
- `references/07-animation-patterns.md` — opens with a mandatory accessibility floor covering `prefers-reduced-motion`, WCAG 2.3.3, and vestibular impact, with a reduced-motion reset that preserves `animationend`/`transitionend` events. Then fade-in-everything, `transition: all` and compositing, perceptual timing thresholds, parallax, meaningless hover, scroll-triggered cascades, static deadness as the opposite failure, easing tokens, loading theatre, infinite loops, springs, 3D, splash screens, custom cursors, scroll-hijacking libraries, video backgrounds, typewriter effects, confetti, SVG morphing, and page transitions.

### Changed

- Deduplicated two patterns that appeared twice in the source material: the tilted dashboard mockup (§2.1.12 / §6.9) and the left-border accent card (§2.1.13 / §6.10) now cross-reference module 02 instead of repeating it.
- `SKILL.md` and README route to all seven modules.

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

[2.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v2.0.0
[1.2.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.2.0
[1.1.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.1.0
[1.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.0.0
