# 09 — Slop Taxonomy: Code-Level & Technical Patterns

> **Module:** 9 of N · **Status:** stable
> **Read when:** writing or reviewing frontend implementation — markup, styling architecture, tokens, state, performance, accessibility wiring.

Visual slop is visible. Code slop is not — until an audit, a screen reader, or a Lighthouse run finds it. This module covers the failures that survive a good-looking screenshot.

**The governing fact:** models have no representation of the accessibility tree. They learn what code *looks like*, not what it *means* to assistive technology. Left unconstrained, generated markup converges on div soup — which is why accessibility is the single most reliable place to find AI-authored code.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 9.1 Div soup — non-semantic markup

**CRITICAL**

**Banned specifics**

- `<div>` and `<span>` carrying the entire document structure
- `<div onClick>` where a `<button>` belongs
- `<div className="nav">` instead of `<nav>`
- No `<main>`, `<header>`, `<footer>`, `<article>`, `<section>`, `<aside>`
- Heading levels chosen by size rather than structure — an `<h4>` because `<h2>` looked too big
- Skipped heading levels (`h1` → `h3`)
- Multiple `<h1>`s on one page
- Lists built from divs
- Tabular data built from divs

**Why this is slop**

`<div onClick>` is not a button. It is not focusable, does not respond to Enter or Space, is not announced as a control, and does not appear in a screen reader's list of controls. It looks identical and is functionally broken for a substantial minority of users.

Semantics are also how search engines and every automated reader understand a page. Div soup ranks worse with identical content.

**Instead**

```html
<!-- BANNED -->
<div class="btn" onclick="submit()">Analyze</div>

<!-- GOOD — free focus, keyboard, and announcement -->
<button type="button" onclick="submit()">Analyze</button>
```

- One `<h1>` per page; heading levels descend without gaps; style them to whatever size the design needs
- `<nav>`, `<main>`, `<header>`, `<footer>`, `<aside>` for landmarks
- `<button>` for actions, `<a href>` for navigation — the distinction is not cosmetic. A link opens in a new tab, is bookmarkable, and appears in link lists. A button does not.
- Real `<ul>`/`<ol>` for lists, real `<table>` for tabular data with `<th scope>`
- `<form>` with a real submit — Enter should work

**The check:** disconnect the mouse and operate the page. Anything unreachable is broken.

---

## 9.2 ARIA used as a substitute for semantics

**HIGH**

**Banned specifics**

- `role="button"` on a div instead of using `<button>`
- `aria-label` on elements that already have visible text, silently overriding it
- ARIA roles on elements that natively have them (`<nav role="navigation">`)
- `aria-hidden="true"` on focusable elements — creating a control a screen reader cannot see but a keyboard can reach
- Custom widgets with roles but no keyboard implementation
- `tabindex` values above 0
- `aria-live` on everything, or on nothing that changes

**Why this is slop**

The first rule of ARIA is not to use ARIA. Native elements come with behavior; ARIA only changes announcement. `role="button"` on a div tells a screen reader it is a button while giving it none of a button's behavior — a promise the element cannot keep. That is worse than the unlabeled div, because now the user expects it to work.

**Instead** — native elements first. Reach for ARIA only for patterns HTML lacks (tabs, comboboxes, live regions), and when you do, implement the full keyboard contract the role implies. Better still, use an accessible primitive library and inherit the contract.

`tabindex="0"` to make something focusable and `tabindex="-1"` for programmatic focus are fine. Positive values reorder the entire document tab sequence and are essentially always a bug.

---

## 9.3 Missing focus management

**CRITICAL**

**Banned specifics**

- `outline: none` with no replacement
- `*:focus { outline: none }` anywhere
- Focus rings removed "because they look bad on click"
- Modals that do not move focus in, trap it, or return it on close
- Route changes that leave focus on the old page
- No skip-to-content link
- Focus indicators below 3:1 contrast against their background

**Why this is slop**

Removing focus indicators makes a product unusable by keyboard while looking completely fine in a screenshot. It is the most common serious accessibility defect in generated code and the easiest to fix.

**Instead**

```css
/* Visible for keyboard users, invisible on mouse click */
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
  border-radius: 2px;
}
```

`:focus-visible` is exactly the fix for the complaint that motivates `outline: none` — the ring appears for keyboard navigation and not for pointer clicks. There is no remaining reason to remove it.

**Modals must:** move focus in on open, trap it while open, restore it to the trigger on close, and close on Escape.
**Route changes must:** move focus to the new page's heading, or screen-reader users are stranded.
**Every page needs a skip link** as the first focusable element.

---

## 9.4 `!important`, magic numbers, and z-index chaos

**HIGH**

**Banned specifics**

- `!important` used to win a specificity fight
- Arbitrary values scattered inline: `top: 37px`, `margin-left: -13px`, `width: 847px`
- `z-index: 9999`, `z-index: 99999`, and the escalation war that follows
- Hardcoded hex values in components when tokens exist
- Spacing values off the scale
- Deeply nested selectors compensating for weak structure

**Why this is slop**

Every one of these is a symptom of the same disease: no system. `!important` and `z-index: 9999` are what you write when you do not know what else is on the page — which is exactly the position a model is in when generating a component in isolation.

**Instead**

```css
:root {
  --z-base: 0;
  --z-dropdown: 10;
  --z-sticky: 20;
  --z-overlay: 30;
  --z-modal: 40;
  --z-toast: 50;
}
```

A named, enumerated z-index scale. Spacing drawn from a defined scale (4px base is standard). Colors from tokens, never literals. And if you need `!important`, the real problem is upstream — fix the specificity instead.

---

## 9.4b Unlayered CSS silently beating your utilities

**HIGH**

**Banned specifics**

- Custom rules appended to a stylesheet outside any `@layer`, in a project whose framework uses layers
- A component class setting `display`, `position` or `width` and quietly winning over `md:hidden`, `lg:flex`, `hidden`
- Reaching for `!important` when a responsive utility "doesn't work"
- Assuming a later rule loses because its selector is less specific

**Why this is slop**

Unlayered CSS beats **everything** inside `@layer`, regardless of specificity or source order. Tailwind v4 puts its utilities in `@layer utilities`, so a single plain `.my-button { display: inline-flex }` at the bottom of your stylesheet overrides `md:hidden` on every breakpoint — and the media query never gets a say.

The failure is quiet and looks like a breakpoint bug, so people debug the media query, the viewport, and the build. The devtools even show the utility as applied-then-overridden without making the reason obvious.

**Instead**

```css
/* Component styles belong below utilities, so utilities can still win. */
@layer components {
  .nd-burger { display: inline-flex; }
}
```

- Put custom component CSS in `@layer components`; put resets in `@layer base`
- Never leave rules unlayered in a layered project unless you specifically intend them to beat everything
- If a responsive utility "isn't working", check layering **before** specificity — it is the more likely cause and the one nobody looks at

**The check:** resize to each breakpoint and assert the thing that should disappear actually has `display: none`. Reading the class list is not enough; the class can be present and losing.

---

## 9.5 Arbitrary values instead of tokens

**HIGH**

**Banned specifics**

- `class="mt-[13px] text-[15px] bg-[#f3f1ee]"` scattered through components
- The same color written as a literal in a dozen files
- Values that appear once and never again
- Bypassing the theme config rather than extending it
- Design decisions living in component files rather than in one system

**Why this is slop**

Arbitrary values are decisions with no memory. Nothing records *why* 13px, so nobody can change it safely, and the next component invents a different number for the same purpose. A theme change becomes a search-and-replace across the codebase.

**Instead** — extend the theme, then consume tokens. If a value is genuinely one-off, that is a signal the scale is wrong; fix the scale. The test: can you change the brand color in one place and have the whole product follow?

---

## 9.6 Images that break performance

**HIGH**

**Banned specifics**

- `<img>` with no `width` and `height` (or `aspect-ratio`) — guaranteed layout shift
- `loading="lazy"` on the LCP image
- Full-resolution images scaled down in CSS
- No `srcset`/`sizes` for responsive delivery
- PNG or JPEG where AVIF/WebP would serve
- No `alt` attribute at all

**Why this matters, concretely**

Images are the LCP element on roughly **73% of mobile pages** — so image handling is usually *the* performance story, not a detail of it. And lazy-loading the hero image is a specific, common own-goal: it delays the exact element the metric measures.

**The 2026 Core Web Vitals thresholds**, each at the 75th percentile of real users:

| Metric | Good | Note |
|---|---|---|
| **LCP** | < 2.5 s | Usually an image |
| **INP** | < 200 ms | The most-failed vital — roughly 43% of sites miss it |
| **CLS** | < 0.1 | Almost always unsized media or injected banners |

**Instead**

```html
<picture>
  <source srcset="hero.avif" type="image/avif">
  <source srcset="hero.webp" type="image/webp">
  <img src="hero.jpg" width="1200" height="630"
       alt="Permission report showing 23 requested permissions"
       fetchpriority="high" decoding="async">
</picture>
```

- **Always** set dimensions or `aspect-ratio`
- `fetchpriority="high"` and **no** `loading="lazy"` on the LCP image
- `loading="lazy"` on everything below the fold
- AVIF first (~50% smaller than JPEG, past 90% browser support), WebP second, JPEG fallback
- `srcset`/`sizes` so phones do not download desktop assets

---

## 9.7 Interaction states that were never implemented

**HIGH**

**Banned specifics**

- Only the default state styled
- Hover with no `:focus-visible` equivalent
- Disabled controls that look identical to enabled ones
- Disabled controls conveyed by opacity alone, failing contrast
- No loading state on an async action, so buttons can be double-submitted
- No empty state, no error state

**The eight states.** Every interactive component owes: **default, hover, focus, active, disabled, loading, empty, error.** Shipping the first and none of the rest is the most common component failure in generated code.

**Instead**

```css
.btn                { background: var(--action); }
.btn:hover          { background: var(--action-hover); }
.btn:focus-visible  { outline: 2px solid var(--focus); outline-offset: 2px; }
.btn:active         { transform: scale(0.98); }
.btn:disabled       { background: var(--surface-muted); color: var(--text-muted);
                      cursor: not-allowed; }
.btn[data-loading]  { pointer-events: none; }
```

A loading state must actually **prevent re-submission**, not just look busy. And a disabled control should say why it is disabled — a tooltip or adjacent text — or it reads as a bug.

---

## 9.8 Forms built without form semantics

**HIGH**

**Banned specifics**

- Placeholder text used instead of a `<label>`
- Labels not associated via `for`/`id`
- No `type` on inputs — `type="text"` for email, phone, and numbers
- No `autocomplete` attributes
- Validation errors conveyed by red border alone
- Errors not associated with their field
- Errors announced only visually
- Input wiped on failed submission
- No `<form>` element, so Enter does nothing

**Why this is slop**

Placeholder-as-label is the signature version: it vanishes the moment the user types, so anyone who loses their place has no way to recover the question. It also fails contrast on nearly every implementation.

Missing `type` and `autocomplete` are quieter but expensive — they cost mobile users the right keyboard and cost everyone browser autofill.

**Instead**

```html
<form>
  <label for="email">Work email</label>
  <input id="email" name="email" type="email"
         autocomplete="email" required
         aria-describedby="email-error" aria-invalid="true">
  <p id="email-error" role="alert">Enter an email address that includes an @.</p>
</form>
```

- A real, visible, associated label on every input
- Correct `type` and `autocomplete`
- Errors linked with `aria-describedby`, marked with `aria-invalid`, announced via `role="alert"`
- Error text that says how to fix it, not that something is wrong
- **Never** clear the form on failure
- Validate on blur and on submit, not on every keystroke

---

## 9.9 Hardcoded content and no internationalization path

**MEDIUM**

**Banned specifics**

- Strings hardcoded throughout components
- Dates, numbers, and currency formatted by hand
- Layouts that break when text runs 30% longer
- Fixed-width containers around translatable text
- Concatenated sentence fragments
- No `lang` attribute on `<html>`

**Why this is slop**

Even for an English-only product, hardcoded formatting is wrong: `Intl` respects the user's locale for dates, numbers, and currency, and hand-rolled formatting does not. And German or Finnish translations routinely run 30% longer than English — fixed-width containers guarantee overflow later.

**Instead** — `Intl.DateTimeFormat` and `Intl.NumberFormat` rather than manual formatting. Complete sentences as single strings, never assembled from fragments. Containers that grow. `lang` set correctly so screen readers use the right pronunciation.

---

## 9.10 Components with no error or loading handling

**HIGH**

**Banned specifics**

- `fetch` with no `.catch`
- Data components that render only the success path
- No error boundary anywhere in the tree
- Errors logged to console and nowhere else
- Optimistic updates with no rollback
- Infinite spinners when a request fails
- Raw exception messages shown to users

**Why this is slop**

Generated components model the happy path because the happy path is what the training examples show. Every network call has at least four outcomes — loading, success, empty, error — and shipping one of four means three-quarters of the states are undefined.

**Instead** — handle all four explicitly. Wrap route-level trees in error boundaries so one failure does not blank the page. Show users a human message and a retry; log the technical detail somewhere you can actually read it. Roll optimistic updates back visibly when they fail.

---

## 9.11 Shipping without an accessibility check

**CRITICAL**

Everything above is testable, and most of it is testable automatically. Generated UI is inaccessible by default; the fix is to make the check part of the pipeline rather than an intention.

**The minimum gate**

1. **Automated:** run axe-core (or the WAVE extension) on every page. It catches missing labels, contrast failures, and broken landmark structure in seconds.
2. **Keyboard:** unplug the mouse. Tab the whole page. Every control reachable, focus always visible, no traps, Escape closes overlays.
3. **Zoom:** 200% browser zoom with no horizontal scroll and no clipped content.
4. **Screen reader:** one pass with VoiceOver or NVDA over the primary flow.
5. **Reduced motion:** verify with the OS setting enabled.

Automated tooling catches roughly a third of real issues. It is the floor, not the ceiling — but the floor is where most generated code fails, so start there.

---

## Quick audit

```text
<div onClick        <div onclick        role="button"
outline: none       outline:none
!important
z-index: 9           z-index: 99         z-index: 999
(custom CSS appended outside @layer in a layered project)
tabindex="1"        tabindex="2"
placeholder=        (with no matching <label for>)
aria-hidden="true"  (on anything focusable)
loading="lazy"      (on the hero or LCP image)
<img                (with no width/height and no alt)
text-[             bg-[#              mt-[
fetch(              (with no .catch and no error state)
transition: all
```

Then run the three checks no grep performs: axe-core on the page, the whole flow by keyboard only, and 200% zoom.

---

## Sources & further reading

- [AI-Generated UI Is Inaccessible by Default — Frontend Masters](https://frontendmasters.com/blog/ai-generated-ui-is-inaccessible-by-default/)
- [The Hidden Cost of AI-Generated Frontend Code — DZone](https://dzone.com/articles/ai-generated-frontend-code-cost)
- [AI website optimization: the value of semantics and accessibility in 2026](https://kodem.dev/ai-website-optimization-semantic-and-accessibility-value/)
- [Core Web Vitals 2026: INP, LCP & CLS thresholds](https://www.corewebvitals.io/core-web-vitals)
- [Core Web Vitals 2026: INP, LCP & CLS Optimization](https://www.digitalapplied.com/blog/core-web-vitals-2026-inp-lcp-cls-optimization-guide)
- [Image Optimization in 2026: WebP/AVIF, DPR, and Lazy-Loading](https://tworowstudio.com/image-optimization-2026/)
- [Responsive Images with srcset and sizes: 2026 Guide](https://smolpix.co/blog/responsive-images-with-srcset-and-sizes-2026-guide)
