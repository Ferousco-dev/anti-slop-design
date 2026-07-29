# 11 — The Craft List

> **Module:** 11 of N · **Status:** stable
> **Read when:** you have avoided the slop and need to know what to *add*. Read alongside [`13-pre-emit-checklist.md`](13-pre-emit-checklist.md).

Modules 02–10 are prohibitions. This one is the positive specification: the things premium interfaces do that generated ones almost never do.

Avoiding slop gets you to *inoffensive*. These get you to *good*. The distinction matters, because a page can pass every ban in this skill and still feel like nothing.

> **This module is not optional polish.** Modules 02–10 are subtractive: run them alone and you get austerity, which is its own failure ([`01` §9](01-philosophy.md#9-anti-anti-slop--the-failure-mode-on-the-other-side)). A design needs a positive idea, and prohibitions cannot supply one. If you have cleared every ban and the result feels flat, you are not finished — you are half finished.

---

## 1. All eight states, every time

Generated components ship the default state. Craft ships all eight.

| State | Owed to the user |
|---|---|
| **Default** | The resting appearance |
| **Hover** | "This is interactive" — pointer only |
| **Focus** | "You are here" — keyboard, and never removed |
| **Active** | "Your press registered" — immediate, ~100 ms |
| **Disabled** | "Not now" — *and why not* |
| **Loading** | "Working" — and genuinely blocking re-submission |
| **Empty** | "Nothing here yet" — and how to change that |
| **Error** | "This failed" — what failed, and what to do |

The last four are where craft lives. Anyone can style a hover.

**Two rules that get missed:** a disabled control must communicate *why* it is disabled, or it reads as a bug. And a loading state must actually prevent a second submission, not merely appear busy.

---

## 2. Optical alignment over mathematical alignment

Mathematically centered is often visually wrong. Real designers correct by eye.

- A play triangle centered in a circle needs shifting right; its visual mass sits left of its bounding box
- Round shapes need slight overshoot against flat ones to appear the same size
- Text next to an icon aligns on x-height, not bounding boxes
- Quotation marks and bullets hang into the margin so the text edge stays straight
- Capital letters against lowercase need optical, not metric, baseline treatment

If it measures correct and looks wrong, it *is* wrong. Trust the eye.

---

## 3. One spacing scale, applied with intent

Not "consistent spacing" — *meaningful* spacing. Space encodes relationship.

Build on a 4px base: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`.

Then use proximity to express grouping. A label sits 4px from its input, the field group sits 24px from the next, the section sits 96px from the next. A reader should be able to infer the structure from spacing alone, with all text blurred out.

**The test:** blur the page until text is unreadable. The grouping should still be obvious. If everything is evenly spaced, nothing is grouped.

---

## 4. Real content, at real lengths, at the extremes

Design with the content you will actually have — then break it.

- The longest realistic name, title, and description, not the convenient one
- The shortest: one item, one character, one word
- Zero: the empty state, designed rather than defaulted
- Enormous: 10,000 rows, 200-character labels, a 40-item nav
- Numbers at every magnitude: 0, 7, 1,284, 4,000,000
- Names with diacritics, non-Latin scripts, and right-to-left text
- Text 30% longer, which is roughly what German translation costs you

Lorem ipsum hides every one of these failures until production.

---

## 5. Keyboard operability as a first-class path

Every action reachable by mouse must be reachable by keyboard, in an order that matches the visual layout.

- A logical tab order — DOM order matching visual order
- A skip link as the first focusable element
- Escape closes every overlay
- Enter submits every form
- Arrow keys within composite widgets — tabs, menus, listboxes
- Focus trapped inside modals while open, restored to the trigger on close
- Focus moved to new content on route change
- Shortcuts for genuinely frequent actions, and a way to discover them

Keyboard support is not an accessibility feature bolted on afterwards. It is what power users experience as *speed*, which is the premium tier's most consistent signature.

---

## 6. Responsive type and space, not just responsive layout

Most responsive work stops at column count. Craft scales the whole system.

```css
h1 { font-size: clamp(2rem, 5vw + 1rem, 4.5rem); }
```

- Type scales fluidly; a 72px hero on desktop is not 72px on a phone
- Spacing scales with viewport — 96px section padding becomes 48px
- Measure stays 45–75 characters at every width
- Touch targets are at least 44×44px on touch devices
- Hover-dependent affordances have a tap equivalent
- Test the awkward middle: 768–1024px, where most layouts break

---

## 7. Dark mode as a designed system

Not an inversion. A second system with its own decisions. See [`03-color-patterns.md` §3.6](03-color-patterns.md#36-dark-mode-as-inversion).

- Near-black surfaces (`#0a0a0a`), never pure black
- Elevation inverts — raised surfaces get *lighter*, since shadows barely read
- Chroma reduces, or saturated colors bloom
- Images and screenshots get dark variants
- Borders soften; a border that reads correctly on white is harsh on near-black
- Every component checked independently in both modes

---

## 8. Micro-copy written with the same care as headlines

The small words are most of the words, and nobody writes them.

- Button labels naming the action: "Analyze APK", not "Submit"
- Empty states that teach
- Error messages that say what to do next
- Loading text describing the actual work: "Scanning libraries…"
- Confirmations that state what happened: "Report saved to your workspace"
- Tooltips adding information rather than repeating the label
- Placeholder text showing format, never replacing a label
- Destructive confirmations naming what will be destroyed

See [`08-copywriting-patterns.md`](08-copywriting-patterns.md) for voice.

---

## 9. Performance treated as a design constraint

Speed *is* the aesthetic. The premium tier's most consistent shared property is that nothing lags.

Budgets worth holding, at the 75th percentile of real users:

| Metric | Target |
|---|---|
| LCP | < 2.5 s |
| INP | < 200 ms |
| CLS | < 0.1 |
| JS on first load | < 200 KB compressed |
| Web fonts | ≤ 2 families, subset, preloaded |

- Every image sized, so nothing shifts
- The LCP image prioritized, never lazy-loaded
- No blocking third-party scripts above the fold
- Interactions responding within 100 ms, even if the result takes longer

A beautiful page that takes four seconds is not a beautiful page.

---

## 10. Motion with a point of view

Not "add animations." A defined motion system. See [`07-animation-patterns.md`](07-animation-patterns.md).

- Named duration tokens — instant 100 ms, fast 150 ms, base 200 ms, slow 300 ms
- Named easing tokens, with entrance and exit curves that differ
- Exits roughly two-thirds the duration of entrances
- Motion that explains — where a panel came from, where a deleted row went
- `prefers-reduced-motion` respected everywhere, with instant state changes replacing movement

---

## 11. Details that signal a human was here

The accumulation of small correctness that nobody notices individually and everybody feels collectively.

- Selection color set to match the brand instead of default blue
- Scrollbars styled where the design warrants, still visible and operable
- `::marker`, `::placeholder`, and `:invalid` styled rather than left default
- A real 404 and a real 500 page
- A favicon at every required size, plus a dark-mode variant
- Correct Open Graph and Twitter card images, tested in a real preview
- A `theme-color` meta tag so mobile browser chrome matches
- Print styles, if anyone would ever print it
- Correct `lang`, and a `<title>` that changes per route
- Real curly quotes and apostrophes, not `"` and `'`
- Non-breaking spaces preventing awkward line breaks in names and numbers
- Consistent capitalization in labels — pick sentence case or title case and hold it

None of these individually matters. Together they are the entire difference.

---

## 12. Systems that are documented and enforced

A design system that lives only in one person's head is not a system.

- Tokens defined once and consumed everywhere — no literal hex values in components
- Components with a single canonical implementation, not four near-duplicates
- Naming conventions written down
- Linting that catches drift automatically
- Accessibility tests in CI, not in someone's intention
- A changelog for the design system itself

The test: can a new contributor build a new page that looks like it belongs, without asking anyone?

---

## The craft test

Six questions. Any "no" is unfinished work.

1. Did I design all eight states, or only the default?
2. Does the page still make sense with the longest realistic content — and with none?
3. Can I complete every task with the keyboard alone?
4. Does it hold together in dark mode, at 200% zoom, and at 375px wide?
5. Does it hit the performance budget on a mid-range phone, not my laptop?
6. Is there one detail here a careful person would notice and appreciate?

Question six is the real one. Slop has no such detail. Craft always has several.

---

## Sources & further reading

- [Button States: Communicate Interaction — Nielsen Norman Group](https://www.nngroup.com/articles/button-states-communicate-interaction/)
- [Button States Explained: The Complete Design Guide for 2026 — UXPin](https://www.uxpin.com/studio/blog/button-states/)
- [Spectrum Design Data — interaction states registry](https://opensource.adobe.com/spectrum-design-data/registry/states)
- [Core Web Vitals 2026: LCP, INP & CLS](https://www.corewebvitals.io/core-web-vitals)
- [Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel)
- [How Stripe, Linear, and Vercel Ship Premium UI](https://mantlr.com/blog/stripe-linear-vercel-premium-ui)
