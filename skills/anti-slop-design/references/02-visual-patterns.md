# 02 — Slop Taxonomy: Visual Patterns

> **Module:** 2 of N · **Status:** stable
> **Read when:** generating or reviewing any visual treatment — backgrounds, surfaces, shadows, borders, badges, decorative elements.

This module catalogs visual slop. **Presence of a CRITICAL pattern in output is an automatic fail — regenerate the affected section.** HIGH and MEDIUM require an explicit, written, product-specific justification to survive. LOW are context-dependent defaults worth questioning.

**Severity legend**

| Level | Meaning |
|---|---|
| **CRITICAL** | Automatic fail. Regenerate immediately. No justification accepted. |
| **HIGH** | Regenerate on detection unless you can defend it in one specific sentence. |
| **MEDIUM** | Strong smell. Justify or replace. |
| **LOW** | Situationally fine. Question the default. |

---

## 2.1.1 The purple / indigo / blue gradient syndrome

**CRITICAL**

The single most recognizable AI slop signature on the internet. It is not ugly. It is omnipresent to the point of meaninglessness — the visual equivalent of elevator music.

**Banned specifics**

- Purple, indigo, or blue-to-purple gradients in any hero, background, or CTA
- `bg-gradient-to-r from-indigo-500 to-purple-600` or any Tailwind equivalent
- `linear-gradient(135deg, #667eea, #764ba2)` or any CSS equivalent
- Gradient text (`background-clip: text`) with purple/blue/indigo stops
- Aurora/mesh gradients blending cyan, magenta, yellow, blue, green
- Multi-stop rainbow gradients used decoratively
- Northern-lights / aurora borealis background effects
- Holographic shimmer, prismatic effects, iridescent overlays
- `conic-gradient` or mesh gradients with multi-color blends
- Any gradient whose dominant hues are purple, indigo, violet, or blue-purple
- Any gradient used as a hero background that is not a subtle, brand-specific monochromatic ramp

**Why this exists**

Tailwind CSS shipped `bg-indigo-500` as the prominent default across its documentation and Tailwind UI examples. Adam Wathan has publicly acknowledged the consequence. Thousands of developers copied those examples; thousands of tutorials used those defaults; component libraries adopted similar palettes. When models trained on GitHub, Stack Overflow, and documentation sites, they learned an implicit rule: *modern web design = purple buttons.*

It goes deeper than one framework. Purple sits at the intersection of "creative" and "technical" in color psychology. It is the safest choice for a product that wants to feel innovative without committing to a real brand. It is the design equivalent of saying "synergy."

Users now subconsciously associate purple gradients with low-effort AI sites, scam landing pages, cookie-cutter templates, and products that have not found their identity.

**Instead**

- Use one primary brand color as a solid fill. Commit to it.
- Build ramps in OKLCH — perceptually uniform, no purple bias (see [`03-color-patterns.md`](03-color-patterns.md))
- If a gradient is genuinely required, use a subtle monochromatic ramp in a non-purple hue
- Build semantic tokens: `--color-action-primary`, `--color-surface-elevated`
- Study real brands: Stripe commits to one blue. Linear is near-monochrome. Vercel is black and white with a rare accent.

```css
/* BANNED */
.hero { background: linear-gradient(135deg, #667eea, #764ba2); }
.btn-primary { background: linear-gradient(to right, #8b5cf6, #6366f1); }
.headline {
  background: linear-gradient(90deg, #a855f7, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-aurora {
  background: conic-gradient(from 90deg at 50% 50%, #e0c3fc 0%, #8ec5fc 50%, #e0c3fc 100%);
}
```

---

## 2.1.2 Glassmorphism & frosted glass

**CRITICAL**

Frosted glass, backdrop-blur overlays, and floating translucent cards have become the default decorative effect for generated interfaces. It adds visual noise without functional value, reduces readability, and signals "I could not think of what to put here, so I made it blurry." It is reverb on every instrument in the mix.

**Banned specifics**

- `backdrop-filter: blur()` for decorative panels, cards, or sections
- Frosted-glass navigation bars, unless the nav genuinely floats over content *and* the blur serves a purpose
- Translucent floating cards (`bg-white/10` + `backdrop-blur-lg`)
- Glassmorphism as a section background treatment
- Floating translucent modals with no solid scrim behind them
- Cards that look like glass sitting on a gradient

**Why this is slop**

Apple popularized the effect in macOS Big Sur (2020). It was fresh then. By 2023 every generated landing page had a frosted card; by 2025 it was a cliché. The problem is not the technique — it is the unthinking, default application of it.

It also carries real costs: reduced readability over blurred backgrounds, compositing-layer and GPU overhead from `backdrop-filter`, unpredictable contrast ratios, and measurable mobile performance degradation.

**The only acceptable use**

`backdrop-blur` survives only when **all five** hold:

1. The element is a true modal, dialog, or overlay that must sit above content
2. A solid scrim (`bg-black/50` or similar) sits beneath it
3. The blur serves a function — focus shift or depth indication
4. Content inside meets 4.5:1 contrast against the blurred backdrop at its worst case
5. It is not a decorative background treatment

**Instead**

- Solid backgrounds with subtle elevation (neutral shadow, hairline border)
- Opacity for hierarchy, not blur
- Whitespace and typography for depth
- For navigation: solid background, subtle bottom border

---

## 2.1.3 Floating blobs, orbs & abstract 3D shapes

**CRITICAL**

The Lorem Ipsum of visual design. They communicate nothing about the product, the brand, or the user. They exist because "add visual interest" resolves to the statistically safest decoration available.

**Banned specifics**

- Floating gradient orbs (blurred, low-opacity circles)
- Abstract 3D shapes in CSS or Three.js for decoration
- Morphing, drifting mesh-gradient blobs
- Decorative geometric patterns with no structural purpose
- "Atmospheric" background elements that are colorful noise
- Any element whose sole purpose is making the background less empty
- Spheres with `filter: blur(100px)` at low opacity
- Icosahedrons, torus knots, and friends floating in the background
- Particle systems that exist purely for decoration

**Why this is slop**

Blobs are the ultimate "I have nothing to say, so I will add decoration" pattern. Real design uses whitespace intentionally. Empty space is not a problem to be solved with blobs — it creates focus, breathing room, and hierarchy.

**Instead**

- Let the background be empty. Whitespace is the element.
- Add **one** meaningful visual anchor: a product screenshot, a custom illustration, a bold typographic treatment, a code snippet, a real data visualization
- Subtle grain or texture if the surface feels too flat — sparingly
- Layer information, not decoration
- For visual interest, reach for asymmetric layout and bold type before decoration

```css
/* BANNED */
.blob {
  position: absolute;
  width: 600px; height: 600px;
  background: linear-gradient(180deg, #a855f7, #3b82f6);
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.3;
  animation: float 6s ease-in-out infinite;
}
```

---

## 2.1.4 Neon glows, colored drop shadows & aura effects

**CRITICAL**

The hallmark of an interface trying too hard to look modern. Visual noise, accessibility damage, and poor aging. The design equivalent of underglow lighting on a car.

**Banned specifics**

- `box-shadow: 0 0 20px rgba(139, 92, 246, 0.5)` — the purple card glow
- `drop-shadow` with colored tints, especially purple, blue, pink
- `text-shadow` in any non-neutral color
- Hover states that add a colored glow to buttons or cards
- Any colored shadow that is not a subtle neutral elevation shadow
- "Aura" effects around interactive elements
- Neon borders with glow
- Glowing underlines or dividers
- Colored shadows standing in for focus states

**Why this is slop**

A glow is a cheap substitute for hierarchy. It says: *I could not make this element stand out through typography, spacing, or position, so I lit it up.* It also creates real accessibility problems — colored shadows interfere with focus indicators and blur the boundary between interactive and static elements.

**Instead**

- Neutral elevation shadows for depth: `0 1px 3px rgba(0,0,0,0.1)`
- Border-color change on hover
- Background-color shift for interactive feedback
- Subtle scale transform (`scale(1.02)`) for emphasis
- Weight or color change for hierarchy
- If an element must stand out, make it bigger, bolder, or better placed — do not glow it

**Focus states are the exception you must not remove.** A visible focus indicator is required. Use a neutral or brand-colored `outline` with `outline-offset`, never `outline: none` without a replacement.

---

## 2.1.5 Uniform border radius everywhere

**HIGH**

When every button, card, input, and image carries the same `rounded-2xl`, the page reads flat and undifferentiated. Speaking in monotone.

**Banned specifics**

- `rounded-2xl` on every card, button, and image
- `rounded-full` on every avatar and badge
- Zero radius variation across an entire page
- A global `border-radius: 16px` default
- Images sharing radius with cards and buttons

**Why this is slop**

Radius communicates purpose. Sharp corners read precise, technical, authoritative. Round corners read friendly, approachable, soft. Uniform radius throws away that vocabulary, and signals a global style applied without thought.

**Instead — a radius scale with assigned meaning**

```css
/* Varied radius by purpose */
.nav        { border-radius: 0; }      /* Sharp, authoritative */
.input      { border-radius: 4px; }    /* Subtle, precise */
.card       { border-radius: 8px; }    /* Friendly but contained */
.hero-image { border-radius: 16px; }   /* Prominent, featured */
.avatar     { border-radius: 9999px; } /* Pills reserved for avatars */
```

- Sharp (`0–2px`): data tables, navigation, code blocks, structural and technical surfaces
- Small (`4px`): inputs, compact buttons, tags, badges
- Medium (`8px`): cards, panels, modals, standard buttons
- Large (`16px+`): sparingly — hero images, featured content, promotional banners

**Nested-radius rule:** an inner radius should equal the outer radius minus the padding between them. Equal inner and outer radii read visually wrong at corners.

---

## 2.1.6 Box shadows on every container

**HIGH**

The card-ification of everything. When everything is elevated, nothing is elevated.

**Banned specifics**

- Every section wrapped in a `shadow-lg` card
- Cards around simple text that needs no containment
- Nested cards — the card-inception anti-pattern
- Shadow as the primary separator between sections
- `shadow-md` / `shadow-lg` as a default on every container

**Why this is slop**

Cards are a containment pattern: they group related information, indicate interactivity, or draw a boundary. Wrapping every paragraph in one is not using cards — it is using them as a crutch in place of whitespace, borders, and typographic hierarchy.

Linear, Notion, and Stripe use cards sparingly, reserving them for content that genuinely needs containment: forms, complex data, interactive panels, dashboard widgets.

**Instead**

- Generous spacing to separate sections
- Hairline borders (`border-t`, `border-b`) for separation
- Type hierarchy (size, weight, color) to group information
- Reserve cards for forms, data tables, interactive panels, complex widgets
- If you use cards, vary elevation — some flat, some slightly raised, none heavy

```html
<!-- GOOD — whitespace does the work -->
<section class="py-24">
  <h2 class="text-3xl font-semibold">Features</h2>
  <p class="mt-4 text-lg text-neutral-600">…</p>
</section>

<!-- GOOD — card for actual containment -->
<div class="border rounded-lg p-6">
  <form>…</form>
</div>
```

---

## 2.1.7 The "BETA" / "NEW" generic pill badge

**HIGH**

The small pill above the headline. It signals uncertainty and adds no information.

**Banned specifics**

- Centered hero with a pill badge above the headline
- "BETA" badges styled as generic pills (`rounded-full bg-indigo-100 text-indigo-700`)
- "NEW" badges used purely as decoration
- Status badges that do not communicate actual status
- "Coming Soon" badges that sit in the hero for months
- Generic "v2.0" or "Just Launched" badges

**Why this is slop**

The pattern came from early-stage startups signaling fast iteration. It has since been adopted as a way to fill an otherwise empty hero. It communicates the wrong thing: uncertainty, unfinished work, low confidence.

**Instead**

- If the product really is in beta, say so honestly in copy: "In early access. Here is what that means for you."
- Use status indicators only where they carry information — a changelog, not a hero
- Draw attention with type hierarchy
- To signal newness, be specific and time-bound: "Shipped July 2026" beats "NEW"

---

## 2.1.8 Decorative gradients behind text

**HIGH**

**Banned specifics**

- Gradient backgrounds behind hero text
- `background-clip: text` with multi-color gradients on body copy
- Text that needs a gradient to "pop" because hierarchy is missing
- Gradient overlays on images that damage text legibility
- Any gradient treatment on paragraphs or descriptions

**Why this is slop**

Gradient text was novel in 2019. It is now a substitute for good typography. If a headline needs a gradient to stand out, the type scale is wrong. If body text has a gradient, readability has already failed.

**Instead** — size, weight, color, and whitespace create hierarchy. Reserve color for function: links, CTAs, status.

---

## 2.1.9 Full-width gradient buttons with white text

**HIGH**

Two slop patterns compounded: the gradient, and the make-it-pop mentality.

**Banned specifics**

- Buttons combining `bg-gradient-to-r` and `text-white`
- Gradients as a button's primary visual treatment
- `from-indigo-500 to-purple-600` on any button
- Gradient + `rounded-full` — the gradient pill button is peak slop

**Instead**

```css
/* GOOD — solid, confident */
.btn-primary {
  background: #0a0a0a;
  color: white;
  border-radius: 6px;
  padding: 12px 24px;
  font-weight: 500;
}
.btn-primary:hover { background: #1a1a1a; }
```

Establish button hierarchy through size, weight, placement, and solid color. Primary solid, secondary outline or ghost, tertiary as a text link.

---

## 2.1.10 Floating icon pills with soft shadows

**MEDIUM**

Small circular or pill containers holding an icon, floating with a soft shadow, used as decorative anchors in feature sections.

**Banned specifics**

- `w-12 h-12 rounded-full bg-indigo-100 flex items-center justify-center` as a decorative anchor
- Icon pills that do not correspond to a clickable action
- Icon pills in colors outside the brand system
- Rows of icon pills in different pastel backgrounds

**Why this is slop**

Borrowed from mobile design — app launchers, Material filter chips — where the pill is functional. On a landing page it is decorative noise carrying no information.

**Instead** — icons inline with text if at all; screenshots, code, and data visualizations where meaning is needed.

---

## 2.1.11 The "Trusted by" logo grid at faded opacity

**MEDIUM**

**Banned specifics**

- Grayscale logos at 30–50% opacity in a grid
- "Trusted by" / "Used by" headings with no real social proof behind them
- Logos of companies that do not use the product
- Auto-scrolling logo marquees
- Obvious stock or placeholder logos

**Why this is slop**

Fake social proof is worse than none. Low-opacity grayscale logos register as decoration, not evidence — and if a user recognizes a logo that does not belong, trust collapses entirely.

**Instead** — real logos with permission, at full opacity, well spaced. Or one strong testimonial with a real name, role, and company. Or a specific metric you can defend.

---

## 2.1.12 The tilted dashboard mockup in the hero

**HIGH**

**Banned specifics**

- Dashboard screenshots in tilted browser frames (`rotate(-3deg)`)
- Fake mockups with placeholder data
- Perfectly symmetrical fake charts
- Stacks of overlapping browser frames
- Screenshots with fake avatars and invented names

**Why this is slop**

The tilted browser frame was fresh in 2018. It now signals "I could not show you the real product, so I built a plausible one." Real products show real screens with real data.

**Instead** — a real screenshot, flat and unframed; terminal output or a code snippet for developer tools; a short screen recording of an actual workflow; or a bold typographic treatment with no screenshot at all.

---

## 2.1.13 The left-border accent card

**MEDIUM**

**Banned specifics**

- `border-l-4 border-indigo-500` on feature cards
- Rounded cards with left-border accents used as feature lists
- Alternating left-border colors outside genuine alert contexts

**Why this is slop**

The pattern is strongly associated with AI chat interfaces and has been copied outward onto marketing pages. It now reads as an AI-interface tell rather than a design decision.

**Instead** — top borders, bottom borders, or none; background shifts instead of border accents; spacing and type for hierarchy. Keep left-border accents for real alert and callout semantics, and pair them with an icon and text so color is never the sole signal.

---

## 2.1.14 The "As seen on" media badge row

**MEDIUM**

**Banned specifics**

- "As seen on" / "Featured in" rows without actual coverage
- Outdated or unlicensed media logos
- Low opacity or grayscale used to hide poor logo quality

**Instead** — show media logos only with real, verifiable coverage, and link to the articles. One prominent, real, attributed quote outperforms a row of logos. With no coverage, do not fake it.

---

## 2.1.15 The stats bar with rounded numbers

**MEDIUM**

"10K+ Users · 99.9% Uptime · 24/7 Support."

**Banned specifics**

- "10K+ Users" with no verification
- "99.9% Uptime" with no public status page or monitoring
- "24/7 Support" when support is async email
- "5-Star Rating" with no link to reviews
- Numbers obviously rounded to the nearest thousand

**Instead** — specific honest figures: "2,437 developers," not "2K+." Link to sources. If the numbers are small, own them: "Used by 47 teams" is more persuasive than "Used by thousands," because it is believable.

---

## 2.1.16 The before/after slider

**LOW**

Effective for genuinely visual products — photo editing, design tools, restoration. Slop when applied to abstract concepts ("before: chaos, after: order") or when a side-by-side would be clearer.

**Instead** — side-by-side comparison for clarity; specific metrics to show improvement; reserve the slider for cases where dragging genuinely reveals something.

---

## 2.1.17 The floating action button on desktop

**LOW**

A Material Design mobile pattern with no place on a desktop web page.

**Banned specifics** — FAB on desktop layouts; FAB as the primary landing-page CTA; FAB obscuring content.

**Instead** — inline CTAs; a persistent header CTA; reserve the FAB for mobile contexts where screen space is genuinely constrained.

---

## 2.1.18 The sticky announcement bar

**LOW**

**Banned specifics** — generic unstyled bars; bars that shift layout on every load; fake urgency that never expires; bars that reappear after dismissal.

**Instead** — style it to the brand, use it only for genuinely important news, persist dismissal, and reserve the space in the layout so it does not cause layout shift.

---

## 2.1.19 The scroll progress bar

**LOW**

**Banned specifics** — progress bars on single-screen landing pages; bright bars competing with the brand; progress indication on pages that barely scroll.

**Instead** — a table of contents for long articles; step indicators for multi-step flows; if you keep it, make it subtle and neutral.

---

## 2.1.20 The back-to-top floating button

**LOW**

**Banned specifics** — on short pages; obscuring content; appearing abruptly with no transition.

**Instead** — only on genuinely long pages (3000px+), subtle and unobtrusive; a fixed header usually serves better.

---

## Quick audit

Scan output for these strings. Each hit needs justification or removal.

```text
gradient-to-   from-indigo   from-purple   from-violet   to-purple
backdrop-blur  backdrop-filter
blur(1          blur(8        blur(100
box-shadow: 0 0     drop-shadow(0 0
background-clip: text
rounded-2xl    rounded-full
shadow-lg      shadow-xl
border-l-4
rotate(-3deg)  rotate(3deg)
Trusted by     As seen on     Featured in
BETA           Coming Soon
```

---

## Sources & further reading

- [Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500)](https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p)
- [AI Slop Fonts and Gradients: The Tells That Give Away AI Design](https://www.925studios.co/blog/ai-slop-design-tells)
- [AI Design Slop: Why AI-Generated UI Looks Generic — SmoothUI](https://smoothui.dev/blog/ai-design-slop)
- [How Stripe, Linear, and Vercel Ship Premium UI](https://mantlr.com/blog/stripe-linear-vercel-premium-ui)
- [Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel)
