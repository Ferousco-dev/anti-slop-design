# 03 — Slop Taxonomy: Color & Gradient Patterns

> **Module:** 3 of N · **Status:** stable
> **Read when:** choosing a palette, defining color tokens, building ramps, implementing dark mode, or reviewing any color decision.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md): **CRITICAL** = automatic fail · **HIGH** = regenerate unless defensible · **MEDIUM** = justify or replace · **LOW** = question the default.

---

## 3.1 The AI purple problem — color monoculture

**CRITICAL**

Generated interfaces converge on the same palette: purple, indigo, blue, and their gradients. This is not a design choice. It is a statistical artifact of training data.

**Banned specifics**

- Indigo (`#6366f1`) as primary brand color without explicit written justification
- Purple (`#8b5cf6`) as primary without explicit written justification
- Violet (`#7c3aed`) as primary without explicit written justification
- Blue-purple gradients as the default "modern" look
- Tailwind `indigo-500`, `purple-600`, `violet-500` used as brand colors
- Material Design's default indigo/purple used uncustomized
- Any scheme where purple/indigo/blue-purple dominates without justification
- "It looks techy" or "it looks modern" offered as justification — these are not justifications

**Why this exists — converging causes**

1. **Tailwind UI defaults (2019–2020).** `bg-indigo-500` shipped as the default button color across the examples millions of developers copied.
2. **Material Design (2014).** Google's primary was indigo `#3F51B5`. Android apps, Google products, and Material-based web apps inherited it; it came to read as "official."
3. **Bootstrap (2011).** Primary was blue-purple `#337ab7`. A generation learned web design through it, internalizing blue-purple as the correct primary.
4. **Color-psychology misapplication.** Purple sits between "creative" and "technical" — the safest choice for a product unwilling to commit to an identity.
5. **Training-data bias.** Models trained on GitHub code, Tailwind/Material docs, and Dribbble learn *modern = purple*, then reproduce it whenever the prompt leaves the choice open.

**The real cost**

Purple does not merely make you generic. It makes you *invisible*. When every product in a category uses it, users cannot tell them apart — you may as well have no brand color.

**Instead**

**1 — Choose from product personality and audience**

| Domain | Direction that carries meaning |
|---|---|
| Fintech / finance | Deep greens, petrol blues, charcoal, restrained gold |
| Healthcare | Soft teals, sage greens, warm whites |
| Developer tools | Neutral grays with a single accent, or high-contrast black/white |
| Creative / design | Bold, unexpected, owned |
| Enterprise | Navy, charcoal, one warm or cool accent |
| Security | Dark surfaces with a red or green signal accent |

**2 — Build ramps in OKLCH, not HSL**

OKLCH (Oklab lightness, chroma, hue) is perceptually uniform: `oklch(0.7 …)` genuinely looks 70% bright at every hue angle. HSL does not — `hsl(60 100% 50%)` yellow and `hsl(240 100% 50%)` blue share an L of 50% while the yellow looks dramatically lighter. That failure is why HSL-built ramps have uneven steps and why designers reach for a color picker's defaults instead of computing a scale.

OKLCH has been natively supported in CSS since 2023 and works across all evergreen browsers (Chrome/Edge 111+, Safari 15.4+, Firefox 113+). Tailwind v4 uses it internally for its default palette.

**Method:** fix hue and chroma, vary lightness in equal steps. The result is perceptually even.

```css
:root {
  /* One hue, one chroma, even lightness steps */
  --brand-50:  oklch(97% 0.02 250);
  --brand-100: oklch(93% 0.04 250);
  --brand-200: oklch(86% 0.07 250);
  --brand-300: oklch(78% 0.10 250);
  --brand-400: oklch(68% 0.13 250);
  --brand-500: oklch(58% 0.16 250);
  --brand-600: oklch(48% 0.15 250);
  --brand-700: oklch(39% 0.12 250);
  --brand-800: oklch(30% 0.09 250);
  --brand-900: oklch(22% 0.06 250);
}
```

Taper chroma at the extremes — full chroma at very high or very low lightness falls outside sRGB and clips unpredictably.

**3 — Generate from a single seed.** Start with one color that means something, then derive. Material 3's HCT pipeline and OKLCH both work; the point is that the palette descends from one decision.

**4 — Study brands that do not lean on purple.** Stripe commits to one blue. Linear is near-monochrome with subtle accents. Vercel is black and white with a rare accent. Notion is warm off-white and black. Figma owns purple — the exception that proves the rule, because they committed to it first and completely.

**5 — Commit.** 60% dominant, 30% secondary, 10% accent. Do not dilute with decorative colors.

```css
/* GOOD — intentional, semantic, defensible */
:root {
  --color-surface:        #fafafa;
  --color-surface-raised: #ffffff;
  --color-border:         #e5e5e5;
  --color-text-primary:   #171717;
  --color-text-secondary: #737373;
  --color-action-primary: #0a0a0a;
  --color-accent:         #dc2626; /* one signal color, used for one purpose */
}
```

---

## 3.2 Decorative gradients with no semantic purpose

**HIGH**

The broader category above purple: gradients used because they look nice, serving no hierarchy, state, or brand function.

**Banned specifics**

- Gradients as section backgrounds with no functional purpose
- Gradients used to spice up an otherwise flat design
- Rainbow / multi-color linear gradients
- Mesh gradients with no functional role
- Gradients that do not map to a semantic token
- Gradients on buttons, cards, or text purely for visual interest
- 3+ stop gradients outside data visualization

**Why this is slop**

Gradients age badly — they are trend-dependent in a way solid color is not. Mesh gradients and aurora backgrounds are the worst offenders: complex, multi-color fills whose only job is occupying space.

**The only acceptable uses**

1. **Data visualization** — heatmaps, ranges, progress where the gradient encodes a value
2. **Brand identity that genuinely is a gradient** — and is owned, custom, and consistent
3. **Very subtle depth** on a control, where solid is usually still better
4. **Softening a dark-mode section transition**
5. **Monochromatic ramps** from brand color toward black or white, used sparingly

Anything else needs a documented, defensible reason in the design system.

---

## 3.3 Timid, evenly-distributed palettes

**MEDIUM**

Every color given equal weight, producing a washed-out, indecisive result.

**Banned specifics**

- 5+ colors of equal prominence
- No clear primary — everything reads equally important
- Accents so sparing they have no effect
- Background, text, and accent competing for attention
- Palettes that look randomly generated

**Why this is slop**

Color hierarchy matters as much as typographic hierarchy. With equal weight everywhere, the eye has no anchor. It is a meeting where everyone speaks at the same volume.

**Instead — the 60-30-10 rule**

- **60% dominant** — backgrounds, large surfaces, primary text
- **30% secondary** — subheadings, secondary controls, borders
- **10% accent** — CTAs, links, critical states

Stripe: ~60% white, 30% near-black text, 10% brand blue for actions. Linear: neutral field, dark text, a subtle accent for active states. Vercel: white, black, minimal accent.

A bold palette of 3 colors beats a timid palette of 8.

---

## 3.4 Default Tailwind gray scale

**MEDIUM**

**Banned specifics**

- `bg-gray-50` / `text-gray-600` / `text-gray-900` as the entire neutral system
- Tailwind's default gray for all neutrals with no customization
- No warm or cool tint anywhere in the neutral ramp
- `slate` / `zinc` / `neutral` / `stone` picked without intent
- "It's the default" as the reason

**Why this is slop**

Tailwind's default gray is fine — and used by millions of sites. Adopting it uncustomized inherits the Tailwind look: a subtle sameness users register without naming.

Gray temperature carries meaning. Warm grays (`#fafaf9` → `#1c1917`) read organic, editorial, human. Cool grays (`#f8fafc` → `#0f172a`) read technical, clinical, precise. Your neutrals should match your brand's personality, not your framework's.

**Instead**

```css
/* Warm — approachable, editorial */
:root {
  --gray-50:#fafaf9; --gray-100:#f5f5f4; --gray-200:#e7e5e4; --gray-300:#d6d3d1;
  --gray-400:#a8a29e; --gray-500:#78716c; --gray-600:#57534e; --gray-700:#44403c;
  --gray-800:#292524; --gray-900:#1c1917;
}

/* Cool — technical, precise */
:root {
  --gray-50:#f8fafc; --gray-100:#f1f5f9; --gray-200:#e2e8f0; --gray-300:#cbd5e1;
  --gray-400:#94a3b8; --gray-500:#64748b; --gray-600:#475569; --gray-700:#334155;
  --gray-800:#1e293b; --gray-900:#0f172a;
}
```

Then name them semantically, so components never reference a number:

```css
:root {
  --color-surface:        var(--gray-50);
  --color-surface-raised: #ffffff;
  --color-border:         var(--gray-200);
  --color-text-primary:   var(--gray-900);
  --color-text-secondary: var(--gray-500);
  --color-text-tertiary:  var(--gray-400);
}
```

Better still: build the neutral ramp in OKLCH with a small, constant chroma at a fixed hue. That is what a "warm gray" is — a neutral with a deliberate, consistent hue bias.

---

## 3.5 The rainbow accent pattern

**MEDIUM**

Feature 1 blue, Feature 2 green, Feature 3 orange, Feature 4 pink.

**Banned specifics**

- A different colored icon or background per feature card
- A different accent per section
- Status indicators in arbitrary bright colors with no system
- Data visualizations using every hue available

**Why this is slop**

Rainbow accents say "I could not decide on a brand color, so I used all of them." They prevent users from ever associating a color with a meaning — the thing color is uniquely good at.

**Instead** — one accent for all highlights, actions, and important states. Use shades of the primary for variation. For genuine categories, use restrained tints of the brand hues. For charts, use a controlled, tested 3–5 color sequence and never rely on hue alone to encode meaning.

---

## 3.6 Dark mode as inversion

**MEDIUM**

**Banned specifics**

- Dark mode implemented as `filter: invert(1)` or equivalent
- Every color the mechanical inverse of its light counterpart
- Pure black (`#000000`) surfaces
- Pure white (`#ffffff`) text on pure black
- No saturation or brightness adjustment for dark
- Shadows silently becoming glows

**Why this is slop**

Dark mode is a distinct system, not a flipped one. Pure black causes halation and eye strain; pure white on pure black is harsh at high contrast. Colors that read well on white often go neon on dark.

**Instead**

1. **Near-black, not black.** `#0a0a0a` or `#111111` — it lets you show elevation through subtle brightness steps, which pure black cannot.
2. **Reduce chroma in dark mode.** Bright saturated colors bloom against dark surfaces. OKLCH makes this a controlled adjustment rather than guesswork.
3. **Elevation inverts.** In light mode, higher surfaces cast shadows. In dark mode, higher surfaces get *lighter*. Shadows barely read on dark; a lightness step does the work.
4. **Design it as a first-class system** with its own tokens, and test every component in it.

```css
:root {
  --color-surface:      oklch(98% 0.002 250);
  --color-surface-1:    oklch(100% 0 0);
  --color-text-primary: oklch(20% 0.01 250);
}
:root[data-theme="dark"] {
  --color-surface:      oklch(16% 0.005 250);
  --color-surface-1:    oklch(21% 0.006 250); /* raised = lighter, not shadowed */
  --color-text-primary: oklch(93% 0.008 250);
}
```

---

## 3.7 Color without a contrast check

**HIGH** — and an accessibility failure, not merely a taste failure.

**Banned specifics**

- Text below 4.5:1 contrast (WCAG AA, normal text)
- Large text (≥18pt, or ≥14pt bold) below 3:1
- UI components and graphical objects below 3:1
- Colored text on colored backgrounds with no verification
- `text-gray-400` used for body copy
- Placeholder text too light to read — and placeholder text used *as* a label

**Minimum requirements**

| Content | Minimum |
|---|---|
| Normal text (<18pt, or <14pt bold) | **4.5:1** |
| Large text (≥18pt, or ≥14pt bold) | **3:1** |
| UI components, focus indicators, graphical objects | **3:1** |

**Instead**

- Verify every pair with a contrast checker before shipping
- Encode contrast into tokens so a compliant pairing is the easy path
- Test with color-blindness simulation — roughly 1 in 12 men has a color vision deficiency
- **Never use color as the sole carrier of meaning.** Pair it with an icon, text label, shape, or pattern. This applies to charts, status dots, form validation, and diff views.
- Check dark mode independently; a pairing that passes in light mode frequently fails inverted

---

## 3.8 The random accent color

**MEDIUM**

An accent chosen because it "adds pop" rather than because it means something.

**Banned specifics**

- Accents pulled from a trendy palette with no brand rationale
- Accents that clash with the primary
- Multiple accents with no system
- Accents contradicting convention — red for a save action, green for a destructive one

**Instead** — choose an accent tied to the product's function (security: red for alert or green for verified; finance: green for growth; developer tools: blue for information, amber for build warnings), then use it consistently and document what it means. An accent color is a promise about meaning; keep it.

---

## 3.9 The pastel-everything palette

**MEDIUM**

**Banned specifics**

- Pastel backgrounds on every section (`bg-pink-50`, `bg-blue-50`, `bg-green-50`)
- Pastel card backgrounds with no functional purpose
- Pastels as primary UI colors
- A different pastel per section

**Why this is slop**

Pastels are the safe choice: they do not offend, and they do not communicate. A pastel palette says "I wanted color but feared commitment." Pastels also make WCAG contrast harder, since low chroma at high lightness leaves little room against white.

**Instead** — white or off-white surfaces, subtle gray tints to differentiate sections, pastels reserved for tags and subtle highlights where the low contrast is not carrying meaning. If you want color, use it boldly and rarely.

---

## 3.10 Color as decoration

**HIGH**

**Banned specifics**

- Colored borders with no purpose
- Alternating section backgrounds for "visual interest"
- Icons in arbitrary colors with no semantic mapping
- Colored underlines, dividers, or accents with no functional role

**The rule.** Every color must serve exactly one of these:

1. **Brand identity** — reinforces who you are
2. **Hierarchy** — shows what matters most
3. **State** — hover, active, selected, disabled
4. **Feedback** — success, error, warning, info
5. **Navigation** — shows where the user is

If a color serves none of the five, remove it.

---

## Quick audit

```text
#6366f1  #8b5cf6  #7c3aed  #667eea  #764ba2  #a855f7
indigo-  violet-  purple-  fuchsia-
bg-gray-50  text-gray-400  text-gray-600
gradient-to-  conic-gradient  radial-gradient
#000000  #ffffff  invert(
bg-pink-50  bg-blue-50  bg-green-50
```

For each hit: is there a written justification? Does it pass contrast? Does it serve one of the five purposes?

---

## Sources & further reading

- [OKLCH Color Space — Atmos design glossary](https://atmos.style/glossary/oklch-color-space)
- [OKLCH Color in CSS: The Complete Guide for 2026](https://66colorful.com/blog/oklch-color/)
- [On oklch — Karl Koch](https://karlkoch.me/writing/on-oklch)
- [Color experiments with OKLCH — Chris Henrick](https://clhenrick.io/blog/color-experiments-with-oklch/)
- [Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500)](https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p)
- [Design Systems for AI Coding: Stop Getting Purple Gradients](https://www.braingrid.ai/blog/design-system-optimized-for-ai-coding)
