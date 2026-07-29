# 14 — Workflow & Execution Protocol

> **Module:** 14 of N · **Status:** stable
> **Read when:** starting a design task and you want the full process, or when a task is large enough that the six-step version in `SKILL.md` is not enough.

`SKILL.md` carries the short protocol. This is the expanded one, plus the routing table for which module to load when, and the handling for the cases the short version does not cover.

---

## Phase 0 — Establish the brief

**Never start from a blank aesthetic.** An unconstrained prompt produces unconstrained output, which is the mechanism that produces slop in the first place.

Five things must be known before any pixel is decided:

| # | Question | If the user did not say |
|---|---|---|
| 1 | What is the product, in one sentence? | Infer from the codebase and state the inference |
| 2 | Who is the primary user? | Pick the most likely and say which |
| 3 | What is the emotional register, in three words? | Propose three and say you are proposing them |
| 4 | What must it *not* look like? | Name the category default it should avoid |
| 5 | What is the single most important action? | Infer from the product and state it |

State the inferences in one line, then design against them. Do not stop and ask unless a wrong guess would waste substantial work — proceeding on a stated assumption beats blocking.

If a design system, brand guide, or existing product already exists, **that is the brief.** Read it first. Matching an existing system correctly beats inventing a better one.

---

## Phase 1 — Commit to a direction

Write the visual thesis as one sentence before writing any code.

> "Editorial serif headlines, near-monochrome, generous negative space, one red accent reserved for severity."

This is the single most important step. A named direction is what stops sampling from falling back to the statistical mode. Without it, every subsequent decision defaults.

**A good thesis** names the typographic character, the color strategy, the density, and what carries the personality. **A bad thesis** is "clean and modern" — that constrains nothing.

**Set the six axes first** — density, warmth, formality, energy, ornament, contrast — from [`15-product-types.md`](15-product-types.md). Those positions *are* the thesis, and they translate directly into tokens in phase 2. It also carries the starting position for each product category, which is what stops a design being technically clean and still in the wrong register.

Sanity checks:

- Could this thesis describe a competitor? Sharpen it.
- Does it commit to something a reasonable person might dislike? If not, it is not a direction.
- Can every later decision be checked against it? That is what it is for.

---

## Phase 2 — Derive the system

Decide once, apply everywhere. Ad-hoc per-component values are a slop tell in themselves.

Before building any screen, fix:

- **Type** — families, scale with ratio, weights, line heights, tracking at display sizes
- **Space** — one scale on a 4px base
- **Color** — semantic tokens, not literals; ramps in OKLCH; light and dark defined together
- **Radius** — a scale with assigned meaning per element class
- **Elevation** — shadow steps for light, lightness steps for dark
- **Motion** — duration and easing tokens, entrance and exit differing
- **Z-index** — a named, enumerated scale

Consult [`03`](03-color-patterns.md) for color, [`04`](04-typography-patterns.md) for type, [`07`](07-animation-patterns.md) for motion.

---

## Phase 3 — Build

Work outward from the most important element on the page, not top to bottom. The hero exists to serve the primary action; build the primary action first and let the rest support it.

While building, every element passes the Hierarchy of Needs ([`01`](01-philosophy.md#4-the-anti-slop-hierarchy-of-needs)):

1. Does this serve the user?
2. Does it communicate hierarchy?
3. Does it reflect the brand?
4. Is this the best way to achieve the goal?
5. Would a human designer make this choice?

Design all eight states as you build each component, not afterwards. Retrofitting states is how they get skipped.

**Then run [`11-craft-list.md`](11-craft-list.md) before you consider the build done.** Phases 0–3 are mostly about not doing the wrong thing; module 11 is what puts something there. Skipping it is the single most likely way to produce a page that passes every check and still reads as nothing.

---

## Phase 4 — Self-critique

Run [`13-pre-emit-checklist.md`](13-pre-emit-checklist.md) in full. Gate 1 first — instant fails are cheapest to catch before deeper review.

**Fix what you find before emitting.** Do not ship and apologize. "I've added a purple gradient, let me know if you'd like something else" is a failure of this step, not a courtesy.

---

## Phase 5 — Report the decisions

Close with 3–6 lines naming the deliberate choices and why — the format at the end of [`13`](13-pre-emit-checklist.md#reporting).

Then say plainly what you did not do: checks you could not run, sections you left out, assumptions you shipped under. An unreported gap costs more than a known one.

---

## Module routing

Load on demand. Do not read everything upfront — that is what progressive disclosure is for.

| Working on | Load |
|---|---|
| Justifying any decision, or explaining why something is slop | [`01`](01-philosophy.md) |
| Backgrounds, surfaces, shadows, borders, badges, decoration | [`02`](02-visual-patterns.md) |
| Palettes, tokens, ramps, dark mode, contrast | [`03`](03-color-patterns.md) |
| Typefaces, scale, measure, line height, tracking | [`04`](04-typography-patterns.md) |
| Page structure, heroes, grids, information architecture | [`05`](05-layout-patterns.md) |
| Cards, pricing, forms, feedback, loading, empty, error | [`06`](06-component-patterns.md) |
| Transitions, entrances, hover, scroll, page transitions | [`07`](07-animation-patterns.md) |
| Any user-facing words | [`08`](08-copywriting-patterns.md) |
| Markup, tokens, performance, accessibility wiring | [`09`](09-code-patterns.md) |
| Photography, illustration, icons, screenshots, video | [`10`](10-image-media-patterns.md) |
| Knowing what to *add* once the slop is gone | [`11`](11-craft-list.md) |
| Choosing the direction, or a design that is clean and still feels wrong | [`15`](15-product-types.md) |
| Any mobile app, native or cross-platform | [`16`](16-mobile-app-patterns.md) |
| A specific app screen: onboarding, feed, settings, paywall | [`17`](17-app-screen-rules.md) |
| Choosing what proof to show, or a page that will not convert | [`18`](18-trust-signals.md) |
| Any chart, dashboard or metric tile | [`19`](19-data-visualisation.md) |
| Unsure what the protocol looks like in practice | [`20`](20-worked-example.md) |
| Concrete rules for a specific page region | [`12`](12-section-rules.md) |
| About to emit anything | [`13`](13-pre-emit-checklist.md) |

---

## Mode: reviewing existing work

When asked to critique rather than build, the protocol inverts.

1. **Inventory before judging.** Read the whole thing first. A critique that fires on the first pattern it sees misses the structural problems.
2. **Run Gate 1** from [`13`](13-pre-emit-checklist.md) and list every hit with its location.
3. **Sort by severity**, not by reading order. CRITICAL first.
4. **For each finding: the pattern, why it is slop, and the specific replacement.** A finding with no replacement is a complaint.
5. **Say what is working.** If the type scale is good, say so — otherwise the author cannot tell what to preserve.
6. **Separate the structural from the cosmetic.** "The layout is the SaaS conveyor belt" matters more than "the radius is inconsistent," and fixing the first may moot the second.
7. **Do not rewrite unless asked.** A review is a review.

---

## Mode: working inside an existing product

**The existing system wins.** Consistency beats individual improvement almost every time — a "better" button that matches nothing is a worse button.

- Match the established type, spacing, color, and radius even where you would have chosen differently
- If the existing system contains slop, say so once, then follow it unless asked to change it
- Propose systemic fixes as a separate piece of work, not as a surprise inside an unrelated task
- Never introduce a second design system inside a product that has one
- New components must look like they were always there

The exception is accessibility. Never propagate an accessibility defect for consistency's sake — fix it in what you touch and flag the pattern.

---

## Mode: the user asks for something on the banned list

Sometimes the request is explicit: "give me a purple gradient hero."

1. **Say the concern once, in a sentence or two.** Name the specific cost — that this exact treatment reads as AI-generated to most visitors in 2026.
2. **Offer the nearest strong alternative**, concretely.
3. **If they confirm, build it, fully and well.** Do not sandbag it, do not add a disclaimer, do not re-litigate.

A reaffirmed request is a decision. Their product, their call. Build the best possible version of what they asked for.

The same applies to house style: if a project's brand genuinely is a purple gradient, it is not slop — it is the brand. Slop is the *unexamined* default, not the color.

---

## Mode: constrained scope

For a small change — one component, one section, a copy edit — run the short version:

1. Match the existing system (Phase 0 collapses to "read the surrounding code")
2. Build
3. Run the one-minute checklist at the end of [`13`](13-pre-emit-checklist.md)
4. One line on what you decided

Do not impose a full design process on a two-line change. Proportionality is itself good judgment.

---

## What "done" means

Done is not "the code runs" or "it looks nice." Done is:

- Every Gate-1 item clear
- Accessibility gate passed, and actually run rather than assumed
- All eight states designed for anything interactive
- Real copy in every visible string, including empty, loading, and error
- The decisions stated, and the gaps named

Anything less is unfinished, and reporting it as finished is the one failure this skill cannot help with.
