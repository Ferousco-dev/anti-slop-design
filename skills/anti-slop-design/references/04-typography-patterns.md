# 04 — Slop Taxonomy: Typography

> **Module:** 4 of N · **Status:** stable
> **Read when:** choosing typefaces, building a type scale, setting measure and rhythm, or reviewing any type-setting decision.
> **Not here:** everything about *words* — buzzwords, headlines, voice, testimonials — lives in [`08-copywriting-patterns.md`](08-copywriting-patterns.md).

Typography is where slop is most insidious. Bad typography does not scream like a purple gradient — it whispers. It creates a sense of wrongness users feel but cannot name. Generated typography is consistently mediocre: safe, symmetrical, forgettable.

It is also the **single fastest lever for escaping slop.** Changing one typeface transforms a generic page into a recognizable one more cheaply than any other change you can make.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 4.1 Inter as the only font

**CRITICAL**

Inter is a genuinely excellent typeface — designed for screens, superbly hinted, enormous character set, strong at small sizes. It is also the default in nearly every AI design tool, component library, and site builder. Inter plus a system fallback and no other typographic decision is a strong signal the design was never intentionally styled.

Estimates in 2026 put Inter in the overwhelming majority of new UI work. The ubiquity is the problem, not the design.

**Banned specifics**

- Inter as the only family on the site
- Inter for both headings and body with no differentiation
- `font-family: 'Inter', sans-serif` as an unexamined global default
- No display/text distinction at all
- Loading Inter without ever considering an alternative
- "It's the default" or "it looks clean" offered as the reason

**Why this is slop**

Inter shipped in 2017 and became the design community's favorite: free, well made, screen-optimized. Tailwind adopted it. Vercel, Linear, and Notion used it. Every tutorial, template, and starter kit included it. Models trained on that corpus learned *Inter = modern web design*, and reach for it whenever the prompt leaves the choice open.

**Instead — a deliberate pairing**

One distinctive display face plus one highly readable text face, matched to the brand's personality.

| Direction | Pairing | Reads as |
|---|---|---|
| Developer / technical | Geist + Geist Mono | Precise, native, modern |
| Developer / technical | Commit Mono + DM Sans | Open-source, clean |
| Developer / technical | Berkeley Mono + a neutral sans | Terminal, engineered |
| Editorial | Playfair Display + a clean sans | Classic, high contrast |
| Editorial | Source Serif + Source Sans | Academic, trustworthy |
| Editorial | Merriweather + Lato | Warm, readable |
| Modern / startup | Bricolage Grotesque + DM Sans | Playful, warm |
| Modern / startup | Space Grotesk + a neutral sans | Geometric, distinctive |
| Modern / startup | Clash Display + Satoshi | Bold, fashion-forward |
| Minimal / premium | Söhne, Graphik, or Helvetica Now alone | Swiss, timeless |

Strong single-family alternatives when a pairing is overkill: **Geist**, **Satoshi**, **Switzer**, **Work Sans**, **IBM Plex Sans**, **Public Sans**. Each carries more personality than Inter at comparable quality.

**How to choose**

1. Name the brand personality in exactly three words
2. Find a display face that embodies them
3. Find a text face that complements without competing
4. Test at every size you will actually ship — headline, body, caption, smallest label
5. Verify character set, numeral styles, and available weights before committing

```css
:root {
  --font-display: 'Geist', system-ui, sans-serif;
  --font-body:    'Geist', system-ui, sans-serif;
  --font-mono:    'Geist Mono', ui-monospace, monospace;
}
h1, h2, h3 { font-family: var(--font-display); letter-spacing: -0.02em; }
body       { font-family: var(--font-body); }
code, pre  { font-family: var(--font-mono); }
```

**Two families is usually the ceiling.** Three is rarely justified; four is a tell of its own. A single family used across several weights and optical sizes often reads more expensive than any pairing.

---

## 4.2 System font stacks as the default

**HIGH**

`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` with no deliberate selection is the ultimate "I did not care about typography" signal: *I couldn't be bothered to choose, so the operating system decided.*

**Banned specifics**

- A system stack with no custom font anywhere
- Arial, Roboto, or Helvetica as primary with no justification
- "System fonts are faster" invoked without weighing the brand cost
- Stacks that render differently per platform, so the design is never the design you approved

**Legitimate exceptions**

- Internal admin tools where load time genuinely dominates
- Documentation where readability is the only goal
- Utility apps with no brand surface
- When the system font *is* the brand

**Instead** — load at least one custom face for display. Self-host it for performance and privacy, subset it to the characters you use, and set `font-display: swap` with a `<link rel="preload">` for the face that appears above the fold.

**Match the fallback metrics.** Use `size-adjust`, `ascent-override`, and `descent-override` on an `@font-face` fallback so the swap doesn't shift layout. Unmatched fallbacks are a major source of cumulative layout shift — a performance failure that reads as cheapness.

---

## 4.3 Centered body text

**HIGH**

Center-aligning paragraphs longer than two lines creates a ragged left edge that measurably slows reading. The eye anchors on the left margin; when that anchor moves every line, tracking costs effort.

**Banned specifics**

- Any centered paragraph longer than 2 lines
- Centered body copy in feature sections and cards
- Centered blog content or FAQ answers
- Any centered text block longer than ~40 characters

**Instead**

- Left-align all body text. Always.
- Center only: short headlines (1–2 lines), CTAs, nav items, single-line labels
- Constrain measure — target **45–75 characters per line**
- `text-wrap: balance` on headlines to prevent orphans; `text-wrap: pretty` on body

```html
<div class="text-center mb-8">
  <h2 class="text-3xl font-semibold text-balance">Analyze any APK in seconds</h2>
</div>
<div class="max-w-prose mx-auto">
  <p>Decompiles, inspects, and reports on every layer of a mobile application —
  from manifest permissions to native libraries.</p>
</div>
```

---

## 4.4 A type scale that isn't a scale

**HIGH**

Ad-hoc sizes chosen per component — 15px here, 17px there, 22px because it looked right — produce an interface with no rhythm. The opposite failure is equally common: a scale so tight (`text-sm`, `text-base`, `text-lg`) that nothing has real hierarchy and every page reads flat.

**Banned specifics**

- Font sizes that appear once and never again
- Only two or three effective sizes across an entire product
- A hero headline that is merely "bigger" rather than decisively bigger
- Sizes chosen per component rather than drawn from a defined scale
- Weight used as the only hierarchy signal, with size held constant

**Instead — define the scale once, use only its steps**

Build on a ratio (1.2 for dense UI, 1.25–1.333 for marketing) and stop inventing values:

```css
:root {
  --text-xs:   0.75rem;   /* 12px — labels, metadata */
  --text-sm:   0.875rem;  /* 14px — secondary, captions */
  --text-base: 1rem;      /* 16px — body, never smaller */
  --text-lg:   1.125rem;  /* 18px — lead paragraphs */
  --text-xl:   1.5rem;    /* 24px — section headings */
  --text-2xl:  2rem;      /* 32px — page headings */
  --text-3xl:  3rem;      /* 48px — hero */
  --text-4xl:  4.5rem;    /* 72px — display, used rarely */
}
```

**Commit to the jumps.** Timid hierarchy is a slop signal in its own right — the gap between body and hero should be obvious at a glance, not measured. Premium interfaces tend to use *fewer* sizes with *larger* gaps between them.

**16px is the floor for body text.** Below that, mobile browsers zoom on input focus and readability drops for a large share of users. Small type is not sophistication.

---

## 4.5 Default line height, tracking, and measure

**MEDIUM**

Setting one `line-height` globally and never touching letter-spacing is the typographic equivalent of a single border radius everywhere.

**Banned specifics**

- One `leading-relaxed` applied to headlines and body alike
- Zero letter-spacing adjustment at display sizes
- Unbounded line length — full-width paragraphs on a wide screen
- Default numerals in tables, prices, and any value that updates
- Headlines left to wrap into a single orphaned word

**Instead — these are the details that separate real typography from defaults**

**Line height scales inversely with size.** Large type needs less; small type needs more.

| Size | Line height |
|---|---|
| Display (48px+) | 1.0–1.1 |
| Headings | 1.2–1.3 |
| Body | 1.5–1.6 |
| Captions | 1.4 |

**Tracking scales inversely too.** Display type needs negative letter-spacing (`-0.02em` to `-0.04em`) because gaps grow with size; small caps and tiny labels often need slightly positive tracking.

**Tabular numerals wherever numbers align or change:**

```css
.price, .metric, table td { font-variant-numeric: tabular-nums; }
```

Without this, a live counter visibly jitters as digits change width — a small detail that reads as unfinished.

**Measure belongs on the container, not the viewport.** 45–75 characters. On wide screens an unconstrained paragraph becomes unreadable regardless of how good the typeface is.

---

## 4.6 Overly perfect, symmetrical alignment

**MEDIUM**

Every headline centered. Every card title centered. Every section symmetrically balanced. A monotonous rhythm that reads robotic, because it is.

**Banned specifics** — every text element centered · perfect symmetry across all sections · zero alignment variation · predictable alternating patterns · every card centered.

**Instead** — vary alignment with intent. Left for editorial and long-form. Centered for CTAs, short headlines, and navigation. Right for pull quotes, captions, and metadata. Align to a grid rather than a centerline.

**Never justify text on the web.** Without hyphenation control, `text-align: justify` produces rivers of whitespace that are worse than a ragged edge.

---

## 4.7 Type that ignores the reader

**HIGH** — and an accessibility failure

**Banned specifics**

- Body text below 16px
- Light weights (300 or below) used for body copy
- All-caps for anything longer than a short label
- Text baked into images, so it cannot be selected, translated, or read aloud
- Sizes fixed in `px` in ways that ignore the user's browser settings
- Low-contrast gray body text — see [`03-color-patterns.md` §3.7](03-color-patterns.md#37-color-without-a-contrast-check)
- Headings chosen for size rather than semantics — an `<h3>` used because `<h2>` "looked too big"

**Why this matters**

Typography is the layer most users interact with, and the one where small failures compound. All-caps removes word-shape cues and slows reading. Thin weights at body size fail contrast on many screens. Text in images is invisible to search, translation, and screen readers.

**Instead**

- 16px minimum body, in relative units so browser zoom and user preferences work
- 400 or higher for body copy; reserve light weights for large display sizes
- All-caps only for short labels, with positive tracking added
- Real text, always — if it must sit on an image, it is still text
- Heading levels chosen by document structure, then styled to whatever size the design needs

---

## Quick audit

```text
Inter          -apple-system      BlinkMacSystemFont
text-center    (on any block longer than 2 lines)
leading-relaxed  (applied globally)
text-xs  text-[13px]  text-[15px]   (ad-hoc sizes off the scale)
font-light  font-thin              (on body copy)
uppercase                          (on anything longer than a label)
text-justify
letter-spacing                     (absent at display sizes)
tabular-nums                       (absent in tables and metrics)
max-w-                             (absent on paragraph containers)
```

Then ask: how many distinct font sizes does this page use, and did every one come from the scale? Is the jump from body to hero obvious without measuring?

---

## Sources & further reading

- [Stop Using Inter Font: 7 Clean Alternatives for UI Design](https://superfiles.in/7-clean-alternatives-to-inter-font.php)
- [Best Inter alternative typefaces & similar fonts — Zetafonts](https://www.zetafonts.com/collections/similar-to/inter)
- [24 Best Fonts for Websites — Figma resource library](https://www.figma.com/resource-library/best-fonts-for-websites/)
- [Inter Font: License, Pairings & Why It's the #1 UI Typeface of 2026](https://madegooddesigns.com/inter-font/)
- [AI Slop Fonts and Gradients: The Tells That Give Away AI Design](https://www.925studios.co/blog/ai-slop-design-tells)
