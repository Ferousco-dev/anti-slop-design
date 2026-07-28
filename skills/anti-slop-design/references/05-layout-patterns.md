# 05 — Slop Taxonomy: Layout & Structural Patterns

> **Module:** 5 of N · **Status:** stable
> **Read when:** structuring a page, designing a hero, choosing a grid, or reviewing information architecture.

Layout is the skeleton. When the skeleton is generic, everything built on it feels generic. Generated layouts follow predictable structures because models learn from the most common ones on the web.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 5.1 The SaaS conveyor belt

**CRITICAL**

The most recognizable slop layout on the internet:

```text
Hero (centered badge + headline + subheadline + 2 buttons + social proof)
Features (3 identical icon cards)
How It Works (3 numbered steps)
Testimonials (3 quote cards)
Pricing (3 tiers, middle highlighted)
FAQ (accordion)
CTA (big headline + button)
Footer (3 link columns + newsletter)
```

**Why this is slop**

It is the statistical average of every SaaS landing page built between roughly 2018 and 2025 — the structure that satisfies the most cases, converts best *on average*, and requires the least thought. "Safest" means "most generic," which means "indistinguishable," which means "forgettable."

Real products design for their specific user journey. A security tool should not share a skeleton with a project management tool.

**Instead**

1. **Start from the user's journey, not a template.** What must they know first? What problem brought them? What proof do they need? What single action should they take? The page order falls out of those answers.
2. **Vary the opening by product type.**
   - Developer tool → a code snippet or terminal output
   - Security tool → a real threat or finding
   - Creative tool → the work itself
   - Enterprise → proof and case studies first
3. **Combine sections.** Interleave features with the testimonials that validate them. Fuse pricing with the comparison table. Put a CTA at the top *and* bottom.
4. **Use editorial structure for content-heavy pages** — asymmetric grids, full-bleed mixed with contained, pull quotes, inline figures.
5. **Consider opening with the problem.** "Most mobile apps request permissions they don't need." Then show the fix.

**Distinctive openings that work**

Linear leads with a large product screenshot and lets it speak. Stripe leads with a bold headline beside a code snippet — developer-first from the first pixel. Notion shows a demo. Vercel opens on a terminal command. Raycast: one screenshot, one headline, nothing else.

---

## 5.2 The centered badge → headline → subheadline → two buttons hero

**CRITICAL**

```text
                    [BETA]
              [Build the Future]
        [Your all-in-one platform for...]
        [Get Started]    [Learn More]
        [Trusted by 10,000+ companies]
```

**Why this is slop**

Users have developed banner blindness for it. The brain registers "template" and disengages before reading a word. It also has structural problems: the badge competes with the headline, the subheadline is usually too long to survive, two equal buttons create decision paralysis, and social proof sits too far from the CTA to influence it.

**Instead — six alternatives**

1. **Left text, right visual anchor** — headline and CTA left; real screenshot or terminal output right
2. **Full-bleed editorial image** with minimal overlaid text, 3–5 words
3. **Asymmetric split** — 35/65 or 40/60, not 50/50
4. **Text-only with massive typography** — headline, one line of context, one CTA
5. **Side-by-side with real output** — the claim beside the evidence
6. **Problem-first** — state the problem in one line, the fix in the next, then a single CTA

**Hero principles**

- The headline explains what the product does in ≤10 words
- The visual anchor is *real* — screenshot, code, data — never decorative
- **One** primary action. A secondary can exist as a text link, not a competing button.
- Social proof sits adjacent to the CTA or inside the headline, not stranded below

---

## 5.3 The three-column footer

**HIGH**

```text
[Logo + Tagline]   [Product]   [Company]   [Resources]
                   Features    About       Blog
                   Pricing     Careers     Docs
                   API         Contact     Help
```

Inherited from 2000s corporate sites and perpetuated by Bootstrap templates, WordPress themes, and generated output. It is not bad. It is invisible — and when a user does look, it confirms their suspicion that the site is a template.

**Instead**

- **Dense and generous** — a full-width band, 5+ columns, real content, lots of whitespace, legal and locale where they belong
- **Minimal** — logo, one-line statement, three social links, copyright. Nothing else.
- **Brand-expressive** — a terminal-styled footer for a developer tool; a live status indicator for an infrastructure or security product; recent work for a creative tool
- **Footer as content** — a newsletter with a real value proposition, latest writing, a hiring callout, a community link

Include only links that earn their place. The footer is a final brand touchpoint, not a sitemap dump.

---

## 5.4 Icon-grid feature sections with no hierarchy

**HIGH**

```text
[icon]   [icon]   [icon]
Secure   Fast     Global
Desc     Desc     Desc
```

**Why this is slop**

It treats all features as equal. They are not. Some are why people buy; some are table stakes. Equal visual weight communicates that none of them matter.

The generic icon compounds it. A shield for "security" and a lightning bolt for "speed" carry no information — they could belong to any product in any category.

**Instead**

1. **Give the killer feature a large card** with a real screenshot and its own CTA; supporting features get smaller cards
2. **Vary card size to encode importance** — one large, two medium, three small
3. **Interleave features with evidence** — feature, then the screenshot proving it; feature, then the code
4. **Use real visuals instead of icons** — screenshots, terminal output, data visualizations, workflow diagrams
5. **Write specific descriptions**
   - BAD: "Secure — Your data is safe with us."
   - GOOD: "Permission mapping — every permission an APK requests, including the dangerous ones it doesn't disclose."

---

## 5.5 Uniform vertical padding

**MEDIUM**

`py-24` on every section produces a metronomic rhythm: technically correct, musically dead. It signals a global style applied without reading the content.

**Instead**

- **Let density drive spacing.** Content-heavy sections tighten; sparse and emotional sections open up.
- **Suggested rhythm** — hero `py-32`–`py-40`, feature grid `py-20`, testimonial `py-32`, CTA `py-24`, footer `py-16`
- **Use asymmetric padding** — `pt-32 pb-16` leading into a dense section; `pt-16 pb-32` coming out of one
- **Mix full-bleed (`py-0`) with contained sections** so the page has texture

---

## 5.6 Symmetrical layouts everywhere

**MEDIUM**

Text left / image right, then image left / text right, forever. Perfect 50/50 splits in every section.

**Instead**

- **Asymmetric splits** — 40/60, 35/65, 30/70, 25/75
- **Break the grid on purpose** — overlap text and image, let a pull quote extend past the column, full-bleed with overlaid text, sticky elements that interrupt the scroll
- **Vary section weight** — some text-heavy, some image-heavy, some balanced; the variation *is* the rhythm
- **Editorial structures** — magazine grids, asymmetric image placement, sidebars and marginalia

---

## 5.7 Bento grids as the default

**MEDIUM**

Bento grids exploded in popularity and are now the new three-column feature grid: trendy, overused, frequently misapplied. Most teams either force them where they do not belong or treat them as glorified card grids, ignoring the one thing they are genuinely good at — encoding hierarchy in the structure itself.

**When bento genuinely works** — multiple related but distinct items the user needs to compare or access in any order. Feature showcases, dashboard widgets, tool collections, data overviews. Measured well on scroll depth versus a conventional 12-column grid, because size differences give the eye a path.

**When it fails** — sequential content (a process, a story), strongly hierarchical content, dense content crammed into small cards, or any case where "it looks modern" is the reason.

**Context matters more than the pattern.** A bento that wins on a SaaS homepage can suppress conversion on an e-commerce category page; the modular look that makes a portfolio feel curated makes a blog feel disorganized.

**Worth knowing:** as bento saturated, a counter-trend emerged — deliberately broken layouts, raw HTML aesthetics, brutalist type, monospace everything. That is *also* becoming a default. Do not swap one costume for another; choose from the content.

**Instead**

1. Use bento only when the content is genuinely modular
2. Vary card sizes to encode real importance — one large, two medium, four small
3. Alternate bento sections with full-width editorial sections
4. Never force content into the grid. A list wants a list. A table wants a table. A story wants prose.

---

## 5.8 The default sticky header

**LOW**

```text
[Logo]   [Home] [Features] [Pricing] [About]   [Get Started]
```

Not bad — the default. When every site has the same header, headers stop being seen.

**Instead** — fewer links and more whitespace; a search-first header for docs-heavy products; a product switcher for multi-product companies; a transparent header that solidifies on scroll; no header at all for immersive experiences; or a header that expresses the brand (a command prompt for a developer tool, a live status indicator for infrastructure).

Whatever you choose: keep it keyboard-navigable, give it a visible focus state, and do not let it eat more than ~10% of viewport height on mobile.

---

## 5.9 Mobile-first as mobile-only

**MEDIUM**

Designing mobile-first (good), then shipping a stretched mobile layout to desktop (bad). Full-width text, full-width image, repeat.

Mobile-first means starting simple and *adding* as space allows. Desktop users have different context and expectations, and a desktop layout should spend the space it has.

**Instead** — genuine multi-column layouts; larger display type and more generous whitespace; desktop-specific affordances (hover states, keyboard shortcuts, multi-pane views, drag and drop); use of the full viewport where it serves the content.

The inverse failure is equally real: a desktop-designed page crushed into one column with no thought. Design both ends deliberately.

---

## 5.10 The container-only layout

**LOW**

Every section inside the same `max-w-7xl mx-auto`. Safe, contained, and monotonous — nothing ever breaks out.

**Instead**

```html
<section class="max-w-7xl mx-auto">…</section>
<section class="w-full bg-neutral-900 text-white py-32">
  <div class="max-w-7xl mx-auto">…</div>
</section>
<section class="max-w-7xl mx-auto">…</section>
```

Full-bleed for emotional impact — hero imagery, a testimonial, a brand statement, the closing CTA. Contained for information density — feature grids, pricing, docs, forms. Break the container deliberately: a pull quote extending past the text column, an image bleeding to one edge.

---

## 5.11 Equal-width columns

**LOW**

50/50, 33/33/33, 25/25/25/25 for everything. Equal widths declare all content equally important, which is almost never true.

**Instead** — golden-ratio-ish proportions (62/38); asymmetric grids chosen per section (70/30 heroes, 60/40 features, 40/60 for image-led); let content drive width. Use CSS Grid with named areas so the intent is legible in the code:

```css
.layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-areas: "main sidebar";
}
```

---

## 5.12 A sidebar on every page

**LOW**

Sidebars serve documentation, dashboards, and content-heavy sites. On a landing page a sidebar is a distraction that competes with the primary message.

**Instead** — full-width for landing pages, sidebars only where navigation genuinely needs persistence, off-canvas on mobile rather than a crushed permanent rail, and sticky sidebars only on genuinely long content.

---

## 5.13 The "above the fold" obsession

**LOW**

Cramming the headline, subheadline, three buttons, social proof, feature preview, trust badges, and a newsletter signup into the first 100vh because "users don't scroll."

Users scroll. They expect to. Overloading the first screen creates information overload and reads as desperation.

**Instead** — one message in the hero: headline, one line of context, one CTA, one visual anchor. Let the page unfold as a narrative. Trust whitespace to create focus.

---

## 5.14 Scroll hijacking

**HIGH**

Overriding native scroll with custom animation, forced snap points, or parallax that fights the user.

**Banned** — `scroll-snap-type: y mandatory` on a whole page; scroll libraries that replace native scrolling; animations that block interaction until they finish; full-screen sections that snap.

**Why this is slop**

It takes control from the user and says the page knows better than the browser. It breaks keyboard navigation, screen readers, find-in-page, and every assistive workflow that depends on predictable scroll position. It is an accessibility failure, not just an annoyance.

**Instead** — let the browser scroll. Use `scroll-snap` only for carousels and galleries, and prefer `proximity` over `mandatory`. Scroll-triggered animation is fine when it never blocks interaction and respects `prefers-reduced-motion`.

---

## 5.15 Infinite scroll where pagination belongs

**LOW**

Appropriate for social feeds and open-ended discovery. Slop for search results, documentation, and filtered product listings — where users need to track position, return to a result, or reach the footer.

**Instead** — pagination for results and listings; an explicit "Load more" for feeds; infinite scroll only for genuine discovery surfaces. Always keep the footer reachable.

---

## 5.16 A modal for everything

**LOW**

**Banned** — sign-up and contact forms in modals; settings in modals; content that deserves a URL; nested modals.

**Instead** — dedicated pages for complex workflows (they get a URL, back-button support, and can be linked); modals only for confirmations and short focused tasks; side panels for settings and filters; inline forms for simple input.

---

## 5.17 Tabs for everything

**LOW**

**Banned** — tabs as primary navigation; tabs hiding long-form content; tabs across content users need to compare side by side; more than 5 in a group; nested tabs.

**Instead** — separate pages for distinct content, accordions for FAQ-shaped content, one scrollable page for related content. Reserve tabs for closely related, equal-priority views — and make them real tabs with proper ARIA roles and arrow-key navigation.

---

## 5.18 Accordions for everything

**LOW**

**Banned** — accordions hiding feature descriptions or pricing details; accordions over primary content; accordions across items users must compare; more than ~10 items in one group.

Hidden content is not scannable and is frequently missed entirely. Anything a user needs to compare must be visible simultaneously.

**Instead** — keep primary information visible; accordions for FAQs and secondary detail only.

---

## 5.19 Fixed elements on all four sides

**LOW**

```text
[Sticky header 60px]
[Sidebar 250px]  [Content — what's left]
[Sticky footer 40px]
[Chat widget 60px]
```

Everything within reach; nothing with room to breathe. Worst on laptops and landscape mobile, where vertical space is already scarce.

**Instead** — sticky headers sparingly, no sticky footer, sidebars only when earned, and a content viewport of at least ~70% of the screen. Chat widgets should be dismissible and must never cover a control.

---

## 5.20 Mega menus for simple navigation

**LOW**

Appropriate for e-commerce and large content sites. Slop on a product with a dozen pages.

**Banned** — mega menus for fewer than ~10 destinations; images and descriptions attached to plain links; menus obscuring the page; menus with no internal hierarchy.

**Instead** — simple dropdowns for 3–5 links, separate pages for distinct sections, a sidebar for documentation. If you keep a mega menu, make it keyboard-operable and escapable.

---

## Quick audit

```text
py-24  (repeated on every section)
max-w-7xl  (with zero full-bleed sections anywhere)
grid-cols-3  (on features, testimonials, pricing, and footer)
scroll-snap-type: y mandatory
grid-cols-2  (with a perfect 50/50 in every section)
"Get Started"  +  "Learn More"   (two competing hero buttons)
```

Then ask the structural questions: Could this page order be swapped onto a completely different product unchanged? Is the hero doing one job or five? Which section is visually largest, and is it actually the most important?

---

## Sources & further reading

- [Designing Bento Grids That Actually Work: A 2026 Practical Guide](https://www.saasframe.io/blog/designing-bento-grids-that-actually-work-a-2026-practical-guide)
- [Bento Grid by Website Category — The 2026 Breakdown](https://landdding.com/blog/bento-grid-design-by-website-category-where-the-pattern-wins)
- [Web Design Trends 2026: What Actually Held Up After Six Months](https://studiomeyer.io/en/blog/webdesign-trends-2026-reality-check)
- [How Stripe, Linear, and Vercel Ship Premium UI](https://mantlr.com/blog/stripe-linear-vercel-premium-ui)
- [Teaching agents product design at Vercel](https://vercel.com/blog/teaching-agents-product-design-at-vercel)
