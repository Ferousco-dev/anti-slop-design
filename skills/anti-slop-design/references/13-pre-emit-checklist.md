# 13 — Pre-Emit Self-Critique Checklist

> **Module:** 13 of N · **Status:** stable
> **Read when:** you have produced output and are about to hand it over. Run this **before** emitting, not after.

This is the gate. Everything above is instruction; this is enforcement.

**How to use it:** work top to bottom. Gate 1 is a hard stop — any hit means regenerate that section before continuing. Gates 2–5 are graded. Do not report the work as finished until Gate 6 passes.

Do not skip this because the output "looks fine." Slop always looks fine. That is the entire problem.

---

## Gate 1 — Instant fails

Any single hit: **stop and regenerate that section.** No justification is accepted.

- [ ] A purple, indigo, or violet gradient appears anywhere
- [ ] `backdrop-filter: blur()` used decoratively
- [ ] Floating blobs, orbs, or abstract 3D shapes
- [ ] Colored glow or neon shadow on any element
- [ ] Inter (or a bare system stack) as the only typeface, unexamined
- [ ] Three identical feature cards in a row
- [ ] Centered hero: badge → headline → subheadline → two buttons
- [ ] Fade-in animation applied to everything on scroll
- [ ] Lorem ipsum, placeholder copy, or fake names anywhere visible
- [ ] A banned buzzword in a headline ("unlock", "elevate", "seamless", "cutting-edge", "empower")
- [ ] `outline: none` with no `:focus-visible` replacement
- [ ] A `<div>` with `onClick` where a `<button>` belongs
- [ ] An AI-generated human presented as a real person
- [ ] An em-dash in a headline, tagline, or CTA

**Mobile apps only, additionally:**

- [ ] `:hover` carrying meaning anywhere
- [ ] One identical design shipped to iOS and Android
- [ ] Content under the notch, status bar, or home indicator
- [ ] A tap target under 44pt
- [ ] A permission prompt before the user has seen any value
- [ ] Type that ignores the OS text-size setting

**Charts and dashboards only, additionally:**

- [ ] A bar chart whose y-axis does not start at zero
- [ ] Two series on two y-axes in one plot
- [ ] A rainbow or red-green palette
- [ ] Values available only on hover, with no table or text alternative
- [ ] A metric with no comparison and no time window

**Count of hits: ___. Anything above zero means the work is not ready.**

---

## Gate 2 — Intention

Every one must have an answer. "It looked good" is not one.

- [ ] I can state the visual thesis in a single sentence
- [ ] I can name why *this* typeface, for *this* product
- [ ] I can name why *this* primary color, and it is not a framework default
- [ ] Every color present serves brand, hierarchy, state, feedback, or navigation
- [ ] Border radii vary by element purpose, not one value everywhere
- [ ] Section spacing varies with content density
- [ ] The layout is not the standard SaaS conveyor belt
- [ ] Nothing here is a library default I accepted without deciding
- [ ] I removed something. Name it: ______________

**The test:** strip the logo. Could this be a competitor's page? If yes, return to Gate 2 and decide something.

---

## Gate 3 — Copy

- [ ] The headline explains what the product does in ≤10 words
- [ ] No banned buzzwords or forbidden phrases survive ([`08`](08-copywriting-patterns.md))
- [ ] No hedging — "designed to", "may help", "allows you to"
- [ ] Active voice in at least 80% of sentences
- [ ] Every claim contains a number, a name, or something checkable
- [ ] Every proof element reduces the audience's *actual* anxiety ([`18`](18-trust-signals.md))
- [ ] At least one thing on the page is checkable by a sceptic in under a minute
- [ ] **Sentence length varies visibly** — not all in the 18–24 word band
- [ ] **Paragraph length varies visibly** — not all 3–5 sentences
- [ ] Contractions appear where natural
- [ ] No section repeats the same structural template as the one before it
- [ ] Button labels name the action, not "Submit" or "Get Started"
- [ ] Empty, loading, error, and success states all have written copy
- [ ] I read it aloud and did not stumble

The cadence checks are the highest-value items on this list. Word-level bans are easy to satisfy while still sounding synthetic; rhythm is not.

---

## Gate 4 — Accessibility

Non-negotiable. Failures here are defects, not preferences.

- [ ] Every text/background pair meets 4.5:1 — 3:1 for large text and UI components
- [ ] Contrast verified in **both** light and dark mode
- [ ] Color is never the only carrier of meaning
- [ ] `:focus-visible` is defined and visible everywhere
- [ ] Full keyboard operation, mouse unplugged, no traps
- [ ] Tab order matches visual order
- [ ] Skip link present as the first focusable element
- [ ] One `<h1>`; heading levels descend without gaps
- [ ] Landmarks used — `<nav>`, `<main>`, `<header>`, `<footer>`
- [ ] Every image has meaningful `alt`, or `alt=""` if decorative
- [ ] Every input has a real associated `<label>` — placeholders are not labels
- [ ] Errors are announced, tied to their field, and say how to fix
- [ ] `prefers-reduced-motion` respected
- [ ] Modals trap focus, close on Escape, and restore focus on close
- [ ] Usable at 200% zoom with no horizontal scroll
- [ ] axe-core run, zero critical or serious violations

---

## Gate 5 — Craft

- [ ] All eight states designed: default, hover, focus, active, disabled, loading, empty, error
- [ ] Disabled controls communicate *why*
- [ ] Loading states actually block re-submission
- [ ] Every value comes from a token or scale — no arbitrary one-offs
- [ ] Tested with the longest realistic content, and with none
- [ ] Tested at 375px, 768px, 1024px, and 1440px
- [ ] Dark mode designed, not inverted — elevation lightens, chroma reduces
- [ ] Micro-interactions land under 300 ms; exits faster than entrances
- [ ] Custom easing tokens, not bare `ease`
- [ ] Every image has dimensions; the LCP image is not lazy-loaded
- [ ] Tabular numerals wherever numbers align or update
- [ ] Measure held to 45–75 characters
- [ ] At least one detail a careful person would notice and appreciate. Name it: ______________

---

## Gate 6 — The final six

Answer honestly. These override everything above. Question 4 is the one that catches austerity, which every earlier gate will happily pass.

**1. Would Stripe, Linear, or Vercel ship this?**
Not "is it as good as" — would they *ship* it? If not, name the specific thing they would cut.

**2. Does anything here exist only because it looked empty?**
Decoration added to fill space is slop by definition. Delete it and check whether the page got worse. Usually it improves.

**3. Could I defend every choice to a designer who disagreed?**
Pick the three most arguable decisions. If you cannot argue them, they were not decisions.

**4. Is there a visual idea here, or only an absence of bad ones?**
Name the idea in one sentence, and make it something you could *see* rather than something you avoided. "No gradients, neutral palette, clean type" is not an idea — that is a list of removals. "The interface is built out of the product's own furniture" is an idea. If the honest answer is that the page is simply inoffensive, go to [`11-craft-list.md`](11-craft-list.md); you are half finished.

**5. Is this in the right register for the category?**
Describe the design aloud without naming the product — "quiet, precise, monochrome, generous space" — and ask what it sells. If the honest answer is a different category, the register is wrong, and no amount of craft rescues it. See [`15-product-types.md`](15-product-types.md).

**6. Will this look dated in two years?**
Separate what is durable — hierarchy, type, spacing, restraint — from what is trend. If the trend elements were removed, is anything left?

---

## Reporting

When the work is done, close with 3–6 lines naming the deliberate decisions and why. Not a feature list — the *choices*:

> Chose Geist over Inter for the mono-adjacent numerals, since this interface is mostly figures. Near-monochrome with a single red accent reserved for severity, so color always means one thing. Radius varies: 0 on the data table, 8 on panels. Hero is a real terminal capture rather than a mockup, because the output is the product. Dropped the testimonial section — there is no real testimonial yet, and a fake one would cost more than the empty space.

If you cannot write those lines, you did not make decisions — you accepted defaults, which is where this started.

**And state what you did not do.** If you skipped a check, could not verify contrast, or shipped a section under an assumption, say so plainly. An unreported gap is worse than a known one.

---

## The one-minute version

When there is genuinely no time for the full pass:

1. **Grep for the instant fails** — gradient, backdrop-blur, Inter, Lorem, `outline: none`, three-card grid
2. **Tab through it once** with no mouse
3. **Read the copy aloud** and listen for the metronome
4. **Strip the logo** and ask whether it could be anyone
5. **Name the visual idea** in one sentence, as something visible rather than something avoided

Five checks. If any fails, the full list is not optional after all.
