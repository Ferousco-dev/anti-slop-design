---
name: anti-slop-design
description: Eliminates generic AI-generated design ("AI slop") from any front-end you build or review — web or mobile. Use whenever generating, reviewing, refactoring, or critiquing a website, landing page, dashboard, web app, iOS or Android app, React Native or Flutter screen, component, design system, or micro-interaction — and whenever the user says a design "looks AI-generated", "looks generic", "looks like a template", "needs personality", or asks to make an interface premium, handcrafted, or distinctive. Also use before emitting any frontend code that involves color, typography, layout, spacing, motion, or copy decisions.
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
2. **Commit to a direction.** Pick one visual thesis and name it (e.g. "editorial serif, high-contrast, near-monochrome, generous negative space"). A named direction is what prevents regression to the mean. Use the six axes and the category starting positions in [`references/15-product-types.md`](references/15-product-types.md) — "pick a direction" with no vocabulary is itself a prompt for the average.
3. **Derive the system, not the screen.** Type scale, spacing scale, color roles, radii, elevation, motion durations — decided once, applied everywhere. Ad-hoc per-component values are a slop tell.
4. **Build.** Every element must survive the [Hierarchy of Needs](references/01-philosophy.md#the-anti-slop-hierarchy-of-needs).
5. **Self-critique before emitting.** Run [`references/13-pre-emit-checklist.md`](references/13-pre-emit-checklist.md). Fix what you find. Do not ship and apologize.
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
- One identical design shipped to both iOS and Android
- `:hover` carrying meaning in a mobile app
- A bar chart whose y-axis does not start at zero
- Chart values available only in a hover tooltip
- Copy like "Elevate your workflow" / "Unlock the power of" / "Seamlessly"

The full banned-pattern database lives in the reference files below.

## References

Load these on demand — do not read them all upfront.

| File | Read it when |
|---|---|
| [`references/01-philosophy.md`](references/01-philosophy.md) | Starting any design task; justifying a decision; explaining why something is slop |
| [`references/02-visual-patterns.md`](references/02-visual-patterns.md) | Backgrounds, surfaces, shadows, borders, badges, decorative elements |
| [`references/03-color-patterns.md`](references/03-color-patterns.md) | Choosing a palette, defining tokens, building ramps, dark mode, contrast |
| [`references/04-typography-patterns.md`](references/04-typography-patterns.md) | Choosing typefaces, type scales, measure, line height, tracking |
| [`references/05-layout-patterns.md`](references/05-layout-patterns.md) | Page structure, hero design, grids, information architecture |
| [`references/06-component-patterns.md`](references/06-component-patterns.md) | Cards, pricing, forms, social proof, loading, empty and error states |
| [`references/07-animation-patterns.md`](references/07-animation-patterns.md) | Any transition, entrance, hover, scroll behavior, or page transition |
| [`references/08-copywriting-patterns.md`](references/08-copywriting-patterns.md) | Any user-facing words: headlines, body, CTAs, testimonials, errors, release notes |
| [`references/09-code-patterns.md`](references/09-code-patterns.md) | Markup, tokens, styling architecture, performance, accessibility wiring |
| [`references/10-image-media-patterns.md`](references/10-image-media-patterns.md) | Photography, illustration, icons, screenshots, video, alt text |
| [`references/11-craft-list.md`](references/11-craft-list.md) | Knowing what to **add** once the slop is gone |
| [`references/12-section-rules.md`](references/12-section-rules.md) | Concrete rules for a specific page region — nav, hero, pricing, footer, forms |
| [`references/13-pre-emit-checklist.md`](references/13-pre-emit-checklist.md) | **Always, before emitting.** The gate. |
| [`references/14-workflow.md`](references/14-workflow.md) | Full protocol, module routing, and the review / existing-product / constrained-scope modes |
| [`references/15-product-types.md`](references/15-product-types.md) | Choosing the direction: personality axes and the register each product category needs |
| [`references/16-mobile-app-patterns.md`](references/16-mobile-app-patterns.md) | Any native or cross-platform mobile app: iOS, Android, React Native, Flutter, SwiftUI, Compose |
| [`references/17-app-screen-rules.md`](references/17-app-screen-rules.md) | A specific app screen — onboarding, feed, profile, settings, paywall, checkout |
| [`references/18-trust-signals.md`](references/18-trust-signals.md) | Deciding what proof to show, or a page that is clean and still not converting |
| [`references/19-data-visualisation.md`](references/19-data-visualisation.md) | Any chart, dashboard, metric tile or table |
| [`references/20-worked-example.md`](references/20-worked-example.md) | Seeing the whole protocol run end to end on a real brief, wrong turns included |

To pin your own product's brief, palette, and voice so they stop being re-decided every session, copy [`assets/project-context.template.md`](assets/project-context.template.md) to `references/00-project-context.md`, fill it in, and add it to this table as "read first, always."

**When the product's category is not in module 15, research it rather than guessing.** Falling back to B2B SaaS is what produces the generic page. Module 15 §4 has the search protocol.

**On the examples.** This skill was written while building **AppMD**, a mobile app analysis tool, so APK/permission/security examples appear throughout. They are illustrations of the *principle*, never requirements. Substitute the user's actual product and domain — an example that mentions APKs applies identically to invoices, patient records, or freight manifests.

Each taxonomy module ends with a **Quick audit** block — a list of strings to grep your own output for. Run it before emitting.

Severity: **CRITICAL** = automatic fail, regenerate · **HIGH** = regenerate unless defensible in one specific sentence · **MEDIUM** = justify or replace · **LOW** = question the default.

## Non-negotiables

Regardless of aesthetic direction, output must be:

- **Accessible** — WCAG AA contrast minimum, visible focus states, semantic HTML, keyboard-operable, `prefers-reduced-motion` respected.
- **Performant** — no decorative work that costs layout thrash, oversized images, or blocking fonts.
- **Durable** — defensible in two years, not tied to a 2024–2026 trend cycle.
- **Specific** — communicating something true about *this* product.

Craft is not decoration. If in doubt, remove.
