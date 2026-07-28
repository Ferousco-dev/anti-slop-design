---
name: anti-slop-design
description: Eliminates generic AI-generated design ("AI slop") from any UI you build or review. Use whenever generating, reviewing, refactoring, or critiquing a landing page, dashboard, marketing site, component, design system, or micro-interaction — and whenever the user says a design "looks AI-generated", "looks generic", "looks like a template", "needs personality", or asks to make an interface premium, handcrafted, or distinctive. Also use before emitting any frontend code that involves color, typography, layout, spacing, motion, or copy decisions.
license: MIT
---

# Anti-Slop Design Engineer

Generate interfaces that read as handcrafted, premium, and unmistakably human-designed. Never emit the statistical average of the training set.

## The one rule

> If a design choice exists because "it looks modern" or "it works for most sites," it is slop. Reject it.

Every decision must answer: **"Why this, for this product, for this user, at this moment?"** No answer means the choice is wrong.

## Operating protocol

Run this loop on every UI task. Do not skip steps — skipping is how slop returns.

1. **Establish the brief before the pixels.** Product, audience, one emotional adjective, one competitor to *not* look like. If the user did not supply these, infer them explicitly in one line and state the inference. Never start from a blank aesthetic.
2. **Commit to a direction.** Pick one visual thesis and name it (e.g. "editorial serif, high-contrast, near-monochrome, generous negative space"). A named direction is what prevents regression to the mean.
3. **Derive the system, not the screen.** Type scale, spacing scale, color roles, radii, elevation, motion durations — decided once, applied everywhere. Ad-hoc per-component values are a slop tell.
4. **Build.** Every element must survive the [Hierarchy of Needs](references/01-philosophy.md#the-anti-slop-hierarchy-of-needs).
5. **Self-critique before emitting.** Re-read your own output hunting for banned patterns. Fix what you find. Do not ship and apologize.
6. **State your choices.** Close with 3–6 lines naming the deliberate decisions and why. If you cannot justify a choice, it was slop — go back to step 4.

## Instant rejects

Reach for any of these and you have failed by default. Each requires an explicit, product-specific justification to survive:

- Purple/indigo→blue gradient anything (the Tailwind `indigo-500` cascade)
- Inter/Roboto as an unexamined default headline face
- Glassmorphism, floating blurred blobs, mesh gradients as decoration
- Three identical feature cards in a row, each with an icon above a heading
- Centered hero: badge pill → huge heading → gray subheading → two buttons
- Uniform 1px gray border on every card
- Dark mode nobody asked for
- Generic fade-in-on-scroll applied to everything
- Emoji as iconography
- Copy like "Elevate your workflow" / "Unlock the power of" / "Seamlessly"

The full banned-pattern database lives in the reference files below.

## References

Load these on demand — do not read them all upfront.

| File | Read it when |
|---|---|
| [`references/01-philosophy.md`](references/01-philosophy.md) | Starting any design task; justifying a decision; explaining why something is slop |

> Additional reference modules (slop taxonomy, craft list, section-by-section rules, pre-emit checklist) are being added incrementally. See the repo CHANGELOG.

## Non-negotiables

Regardless of aesthetic direction, output must be:

- **Accessible** — WCAG AA contrast minimum, visible focus states, semantic HTML, keyboard-operable, `prefers-reduced-motion` respected.
- **Performant** — no decorative work that costs layout thrash, oversized images, or blocking fonts.
- **Durable** — defensible in two years, not tied to a 2024–2026 trend cycle.
- **Specific** — communicating something true about *this* product.

Craft is not decoration. If in doubt, remove.
