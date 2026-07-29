# Changelog

All notable changes to this skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [3.3.0] — 2026-07-29

### Added

- `10-image-media-patterns.md` §10.4b — **brand marks set as Unicode characters.** Found on a real build: an Arabic ن used as a corner watermark rendered as tofu on iOS, because the Helvetica/Arial system stack has no glyph for it at that weight. It looked perfect on the build machine. Marks ship as assets; non-Latin text needs a font that actually covers the script plus a `lang` declaration.
- `12-section-rules.md` navigation — guidance that a sticky desktop header need not be sticky on mobile, where it costs ~10% of viewport permanently and sits across the footer at the bottom of the page.

## [3.2.0] — 2026-07-29

### Added

- `09-code-patterns.md` §9.4b — **unlayered CSS silently beating your utilities.** Found on a real build: a hamburger stayed visible at every breakpoint because custom component CSS was appended outside any `@layer`, and unlayered CSS beats everything inside one regardless of specificity or source order. Tailwind's utilities live in `@layer utilities`, so a plain `.class { display: inline-flex }` overrode `md:hidden` and the media query never got a say. The failure presents as a breakpoint bug, so the debugging goes to the media query, the viewport and the build — never to layering. Includes the fix and the check: assert `display: none` at each breakpoint rather than reading the class list, because the class can be present and losing.

## [3.1.0] — 2026-07-29

Findings from the first real build using the skill.

### Changed

- **Named the austerity failure mode.** Modules 02–10 are subtractive. Run them alone and you produce something with nothing wrong and nothing in it. Added to `01-philosophy.md` §9 as the most common over-correction, and the hardest to see, because every other gate passes.
- `11-craft-list.md` now states up front that it is not optional polish. Prohibitions cannot supply a positive idea.
- `13-pre-emit-checklist.md` Gate 6 gains a question that bites: **"Is there a visual idea here, or only an absence of bad ones?"** The idea must be nameable as something visible rather than something avoided. The previous Gate 5 item ("name one detail a careful person would notice") was too soft to catch a flat page.
- `14-workflow.md` phase 3 now requires a craft pass before the build is considered done, rather than leaving module 11 to be picked up optionally.

## [3.0.0] — 2026-07-29

The skill is now complete. All planned modules are stable.

### Added

- `references/09-code-patterns.md` — div soup and why models produce it (no representation of the accessibility tree); ARIA as a substitute for semantics; focus management and `:focus-visible`; `!important`, magic numbers and z-index scales; arbitrary values versus tokens; image performance against the 2026 Core Web Vitals thresholds (LCP <2.5s, INP <200ms, CLS <0.1; images are the LCP element on ~73% of mobile pages); the eight interaction states; form semantics; i18n readiness; error and loading handling; and a five-step accessibility gate.
- `references/10-image-media-patterns.md` — generic stock photography; AI-generated imagery with the hard line against synthetic humans presented as real, and the consumer-trust data behind it; generic vector illustration; icons that carry no information; screenshot craft; video and captions; images of text; overlay contrast; cross-asset consistency; and a full alt-text decision tree.
- `references/11-craft-list.md` — the positive specification: eight states, optical over mathematical alignment, spacing as grouping, real content at the extremes, keyboard as a first-class path, responsive type and space, dark mode as a designed system, micro-copy, performance budgets, motion with a point of view, the details that signal a human, and documented systems.
- `references/12-section-rules.md` — ban / do / done-when for nav, hero, social proof, features, pricing, testimonials, FAQ, CTA, footer, forms, dashboards, empty-loading-error, documentation, and 404.
- `references/13-pre-emit-checklist.md` — six gates: instant fails, intention, copy, accessibility, craft, and four final questions. Plus a reporting format and a one-minute version.
- `references/14-workflow.md` — the expanded protocol, a module routing table, and four modes the short version does not cover: reviewing existing work, working inside an existing product, handling a user who explicitly requests a banned pattern, and constrained scope.
- `assets/project-context.template.md` — a template users copy to `references/00-project-context.md` to pin their own brief, design system, voice, defensible claims, standing decisions, and known debt. Kept separate so upstream updates never conflict with local context.

### Changed

- `SKILL.md` step 5 now routes explicitly to the pre-emit checklist rather than describing self-critique generically.

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

[3.3.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v3.3.0
[3.2.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v3.2.0
[3.1.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v3.1.0
[3.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v3.0.0
[2.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v2.0.0
[1.2.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.2.0
[1.1.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.1.0
[1.0.0]: https://github.com/Ferousco-dev/anti-slop-design/releases/tag/v1.0.0
