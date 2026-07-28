# 07 — Slop Taxonomy: Animation & Motion Patterns

> **Module:** 7 of N · **Status:** stable
> **Read when:** adding any transition, entrance, hover effect, loading state, scroll behavior, or page transition.

Animation is where slop is most subtle and most damaging. Bad motion does not scream like a purple gradient — it whispers. It produces a sense of sluggishness and artificiality that users feel and cannot name. Generated motion is consistently mediocre: slow, generic, purposeless.

**The governing principle: motion is communication, not decoration.** Every animation must answer "what does this tell the user?" If the answer is "that an animation exists," delete it.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## The accessibility floor — read this before anything else

Motion is the one design category that can make people physically ill. Vestibular disorders — vertigo, Ménière's disease, and related conditions — are triggered by parallax, large page transitions, full-viewport autoplay video, and camera-pan effects. Counting vestibular conditions alongside migraine and attention disorders, the affected population is a large minority of adults, not an edge case.

**Every animation you ship must respect `prefers-reduced-motion`.** This is not a nicety; WCAG 2.3.3 requires that motion triggered by interaction can be disabled.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Two things this snippet gets right that the common version does not: it uses a near-zero duration rather than `none`, so animations still *complete* and any JS listening for `animationend` or `transitionend` still fires; and it caps infinite loops at one iteration.

For motion driven by JavaScript, CSS alone is not enough — query the preference and branch:

```js
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
```

Reduced motion does not mean *no feedback*. Replace movement with an instant state change — an opacity or color shift — so the interface still confirms the action.

---

## 7.1 Generic fade-in on every element

**CRITICAL**

**Banned specifics**

- `opacity: 0 → 1` on every section, card, and text block
- Identical timing (`0.6s ease-out`) everywhere
- Fade-in on content already visible above the fold
- Fade-in on text that should be immediately readable
- Fade-in on navigation or footer
- Staggered fade-in on every list item with a 0.1s cascade

**Why this is slop**

It serves no function. It does not guide attention, communicate state, or improve anything. It exists because "add scroll animations" resolves to the statistically safest animation available.

The costs are real: content feels slow even when it has already rendered; users must wait before they can read; scanning becomes impossible when content is hidden until it scrolls into view; and for users with vestibular conditions, gratuitous motion causes nausea. If the JavaScript that reveals it fails, the content never appears at all — a fade-in cascade is a single point of failure for your entire page.

**Instead**

1. **Animate only what benefits from an entrance** — one key headline per section, the primary CTA, the hero visual anchor
2. **Vary the type** — slide-up for content entering from below, scale for images growing into view, line-by-line reveal for editorial text, and *nothing* for most content
3. **Vary timing** — 200–300 ms for fast entrances; 500–800 ms only for hero-scale moments; custom easing, never bare `ease`
4. **Default to static.** Most content should simply be there.

---

## 7.2 `transition: all`

**HIGH**

**Banned** — `transition: all 0.3s ease` · Tailwind's `transition-all` used without thought · any `transition: all` in production.

**Why this is slop**

It animates every property, including layout-triggering ones — `width`, `height`, `top`, `left`, `margin`, `border-width` — forcing reflow and repaint on every frame. It is the choice of someone who did not decide what they were animating.

It also produces bugs you will not predict: a property you never intended to animate changes, and now it eases.

**Instead**

Animate **`transform` and `opacity`** wherever possible. They are composited on the GPU and do not trigger layout, which is why they hold 60fps when other properties do not.

```css
.button {
  transition:
    transform        0.15s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    box-shadow       0.15s cubic-bezier(0.4, 0, 0.2, 1);
}
```

- `transform: scale()` instead of animating `width`/`height`
- `transform: translate()` instead of `top`/`left`
- `will-change` only on elements actively animating, removed afterwards — it allocates a compositing layer, and leaving it on static elements costs memory for nothing

---

## 7.3 Micro-interactions slower than 300 ms

**MEDIUM**

**Banned** — button hover over 300 ms · toggles taking 500 ms+ · input focus over 200 ms · card hover at 400 ms+ · modal open/close over 300 ms · dropdown over 200 ms.

**Why this is slop**

Micro-interactions are feedback, not entertainment. A button should feel like a physical button: immediate and tactile. A slow button feels like a broken one.

Rough perceptual thresholds:

| Duration | Feels |
|---|---|
| 0–100 ms | Instantaneous |
| 100–300 ms | Responsive |
| 300–1000 ms | Sluggish |
| 1000 ms+ | Broken |

**Instead**

| Interaction | Duration |
|---|---|
| Button press | ~100 ms |
| Button hover | 150–200 ms |
| Input focus | ~150 ms |
| Toggle | 150–200 ms |
| Dropdown open | 150–200 ms |
| Card hover | 200–250 ms |

Use `ease-out` for entrances — it starts fast, so the interface feels responsive. Reserve 500–800 ms for page-scale transitions, hero reveals, and deliberate brand moments.

**Exits should be faster than entrances.** Roughly two-thirds the duration. Users have already decided; do not make them wait to leave.

---

## 7.4 Parallax as decoration

**HIGH**

**Banned** — backgrounds moving at differing speeds for "depth" · decorative parallax with no narrative role · multiple stacked layers · parallax on text · parallax on mobile · anything that interferes with scroll.

**Why this is slop**

Parallax was novel in 2012 and was originally a storytelling device. As a default decoration it causes nausea in users with vestibular disorders, produces janky scrolling from multi-layer compositing, breaks predictable scroll position for keyboard and screen-reader users, and makes touch scrolling unpredictable.

**Instead**

Use it only when it serves narrative — a product reveal that unfolds with scroll, a timeline that progresses, a story that builds. Then keep it to 1–2 layers with subtle speed differences, never on text or interactive elements, disabled on touch, and gated behind `prefers-reduced-motion`. Verify 60fps on a mid-range device, not your laptop. If it drops, remove it.

---

## 7.5 Hover effects that communicate nothing

**MEDIUM**

**Banned** — cards lifting 2px with no other change · buttons shifting color imperceptibly · images scaling 1.02× · links changing color with no other indicator · icons rotating 15° · hover effects on non-interactive elements.

**Why this is slop**

A hover state should answer "what happens if I click this?" A 2px lift answers "I noticed you." That is not information.

**Instead** — make the hover state say something specific: *this is clickable* (cursor plus a clear state change), *this expands* (a rotating chevron, a preview), *this reveals more* (the detail actually appearing), *this is selected* (border or background shift).

**Three rules that are not optional:**

- **Never rely on color alone for links.** Add an underline or another non-color indicator, or the link is invisible to color-blind users.
- **Every hover state needs a focus equivalent.** Keyboard users get no hover. `:focus-visible` should produce a comparably clear state.
- **Hover does not exist on touch.** Anything reachable only by hovering is unreachable for most mobile users. Never hide essential content behind hover.

---

## 7.6 Scroll-triggered animation on every element

**HIGH**

**Banned** — every heading, paragraph, and card animating in · staggered cascades on every list · nothing static · animations firing every 100px · simultaneous animations · animation that blocks scrolling.

**Why this is slop**

It does not guide attention — it demands it, continuously. Users end up processing motion instead of content. It destroys scannability, causes jank when many animations fire at once, and triggers vestibular symptoms.

**Instead** — reserve scroll animation for genuine moments: a hero entrance, a major section transition, a chart drawing itself as it becomes relevant. Body text, feature descriptions, navigation, and footer stay static. Always guard with `prefers-reduced-motion`.

If you use `IntersectionObserver`, make the *visible* state the default in CSS and let JS remove a hidden class — so a JS failure leaves content readable rather than permanently invisible.

---

## 7.7 No animation at all

**MEDIUM** — the failure on the other side

**Banned** — zero hover states · zero focus states · zero transitions · zero loading feedback · buttons that do not respond to press · forms that give no sign of submitting · modals and dropdowns that appear instantly with no transition.

**Why this is slop**

Animation is communication. It says *this is clickable*, *this is submitting*, *this succeeded*, *this is focused*, *this is loading*. An interface with none of it feels like a static image, and users do not trust interfaces that do not respond.

**Instead**

- Button press: `scale(0.98)`, ~100 ms
- Button hover: background shift, ~150 ms
- Input focus: border color plus a subtle ring, ~150 ms
- State toggle: ~200 ms
- Async content: a skeleton matching the final layout
- Outcomes: a checkmark for success, a short shake for error — both brief, both guarded by reduced-motion

The absence of a visible **focus state** is the most serious version of this failure. It makes the product unusable by keyboard. `outline: none` without a replacement is never acceptable.

---

## 7.8 Default easing curves

**MEDIUM**

**Banned** — `ease` everywhere · `ease-in-out` for everything · one curve for all motion.

**Why this is slop**

Easing is the personality of motion. Snappy reads precise and technical. Smooth reads calm and expensive. Bouncy reads playful. One generic curve for everything is monotone.

Worse, the default `ease` is subtly wrong for entrances: it starts slowly, so the interface feels laggy at exactly the moment responsiveness matters.

**Instead — tokenize your curves**

```css
:root {
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);   /* general purpose */
  --ease-entrance: cubic-bezier(0, 0, 0.2, 1);     /* fast in, settle out */
  --ease-exit:     cubic-bezier(0.4, 0, 1, 1);     /* accelerate away */
  --ease-bouncy:   cubic-bezier(0.34, 1.56, 0.64, 1); /* overshoot, settle */
}
```

Match the curve to the brand: snappy and fast for precision tools; smooth and slower for luxury; bouncy for playful products; minimal for technical ones. Then use entrance easing for entrances and exit easing for exits — not one curve in both directions.

---

## 7.9 Loading animation as decoration

**MEDIUM**

**Banned** — spinners for sub-200 ms content · skeletons that flash for under 100 ms · progress bars for instant actions · animations that add artificial delay · "Please wait…" for sub-second work.

**Why this is slop**

A loading state on an instant operation manufactures the perception of slowness. You make your own product feel slower than it is.

**Instead** — nothing under 200 ms; a skeleton matching the real layout for content-heavy surfaces; a small inline spinner for simple actions, never a full-page block; a real progress indicator for genuinely long work.

If an operation is *usually* fast but occasionally slow, delay the loading indicator by ~200–300 ms. Fast cases show no spinner at all; slow cases still get feedback.

---

## 7.10 Infinite animation loops

**MEDIUM**

**Banned** — pulsing dots · bouncing arrows · rotating icons · elements bobbing · blinking cursors outside terminal UI · marquee text · anything looping forever without user interaction.

**Why this is slop**

Infinite motion says "look at me" permanently. It is peripherally distracting even when ignored, it prevents the eye from settling, and it keeps a compositing layer active — a measurable battery cost on mobile.

Acceptable only for: temporary loading indicators, live-status indicators where "live" is the actual message, and notifications that can be dismissed.

**Instead** — one-shot animations for entrances and state changes; subtle states for hover, focus, and active. Anything genuinely infinite must stop under `prefers-reduced-motion`.

---

## 7.11 Spring physics overuse

**LOW**

Spring physics are salt. A little sharpens; too much ruins the dish.

**Banned** — springs on every button press, card hover, modal, navigation transition, and form input.

Appropriate for playful brands, celebratory moments, and mobile gestures where the physics match a real drag. Wrong for professional tools, enterprise software, and developer tooling — anywhere precision and speed are the point. An overshoot on a save button implies imprecision.

**Instead** — standard easing for the overwhelming majority of interactions; springs reserved for the one or two moments that deserve personality.

---

## 7.12 3D transforms on 2D content

**LOW**

**Banned** — 3D card flips for standard content · 3D rotation in navigation · perspective on text · 3D hover on ordinary cards · any 3D effect that harms readability.

3D transforms suit product showcases, genuine flip interactions like flashcards, and interactive viewers. On standard content they add cost and gimmickry without value — and rotated or perspective-transformed text renders poorly and reads worse.

**Instead** — 2D `translate`, `scale`, and subtle `rotate` for icons. Keep any 3D subtle and never apply it to body copy.

---

## 7.13 Page-load animation that blocks interaction

**HIGH**

**Banned** — splash screens blocking content for over a second · intro animations before content is reachable · loading screens for static content · full-page overlays animating in ahead of content · anything preventing interaction.

**Why this is slop**

Users came for content, not for your intro. A splash screen says your brand matters more than their time. It also delays every Core Web Vital that matters, hurts indexing of content behind it, and leaves screen-reader users waiting on an animation they cannot perceive.

**Instead** — render content immediately. Let subtle animation run *around* readable, interactive content rather than in front of it. Reserve loading states for genuinely async work, and keep them non-blocking so the rest of the page stays usable.

---

## 7.14 Custom cursors and cursor trails

**LOW**

**Banned** — custom cursor shapes on standard sites · particle trails · cursor effects that lag behind the real pointer · anything that obscures content.

Custom cursors break a universal expectation and reduce pointing precision. They belong in games, creative tools, and interactive art — not SaaS, marketing, or documentation.

**Instead** — the default cursor set, used correctly: `pointer` for interactive elements, `text` for text, `not-allowed` for disabled. If you ship a custom cursor, keep the standard hit-target semantics and make sure it never lags.

---

## 7.15 Scroll-hijacking libraries

**HIGH**

**Banned** — smooth-scroll libraries that replace native scrolling · custom implementations that alter scroll speed · forced section snapping · anything overriding `window.scroll`.

**Why this is slop**

It asserts that you know better than the browser how a user should move through a page. It breaks scroll momentum, keyboard navigation (Page Down, Home, End), screen-reader virtual cursors, find-in-page positioning, and touch gestures. Users with motion sensitivity have no escape from it.

**Instead** — native scrolling; `scroll-behavior: smooth` for anchors (guarded by reduced-motion); `scroll-snap-type` only for carousels and galleries, and prefer `proximity` over `mandatory`. For scroll-linked effects, `IntersectionObserver` and CSS `animation-timeline: scroll()` achieve the effect without seizing control.

---

## 7.16 Video backgrounds in the hero

**MEDIUM**

**Banned** — generic stock footage with no purpose · autoplay with sound · video that delays load · unoptimized on mobile · a generic looping animation · no fallback image.

**Why this is slop**

Video backgrounds are expensive in bandwidth, CPU, and battery, and they usually communicate nothing specific. Full-viewport moving footage is also one of the most reliable vestibular triggers on the web.

**Instead** — a static image or solid color in most cases. Where video genuinely serves the brand, compress hard, ship a poster fallback, never autoplay with sound, pause when out of viewport, and swap to the still image under `prefers-reduced-motion`. Anything longer than a few seconds should have a visible pause control.

---

## 7.17 Typewriter effects on headlines

**LOW**

**Banned** — typewriter on hero headlines or CTAs · on any text that should be readable immediately · unskippable · replaying on every visit.

It slows reading to the speed of an animation, and it is frequently used to signal "we're technical" while signaling "we're stuck in 2010." It also breaks text selection and confuses screen readers as content mutates mid-announcement.

**Instead** — render text immediately. Reserve the effect for genuine terminal interfaces and deliberate storytelling; if used, make it skippable, once per session, short, and fast.

---

## 7.18 Confetti for every action

**LOW**

**Banned** — confetti on every form submit · celebration on every click · unavoidable celebration animations.

Celebration loses meaning through repetition. If everything is a celebration, nothing is.

**Instead** — reserve it for genuine milestones: first successful setup, course completion, a real goal reached. Standard actions get subtle feedback. Always allow it to be disabled, and always respect reduced-motion.

---

## 7.19 Morphing SVG as decoration

**LOW**

**Banned** — morphing shapes as background decoration · morphing logos and icons · morphs with no functional purpose · morphs that cause jank.

Path interpolation is computationally expensive and drops frames on low-end devices — for decoration, that is cost with no return.

**Instead** — static SVG for decoration; CSS `transform`/`opacity` for simple effects; morphing reserved for loading states, meaningful transitions between two related shapes, and interactive demos.

---

## 7.20 Page transition animations

**LOW**

**Banned** — a transition on every link click · transitions that add perceptible delay · unskippable transitions · transitions that break the back button or accessibility.

A 500 ms transition adds 500 ms to every navigation. Across a session that is real friction, and it frequently breaks browser history, focus management, and deep linking.

**Instead** — instant navigation by default. Subtle transitions where they genuinely help: same-page section changes, modal open/close, panel slide-in. If you use the View Transitions API, keep transitions under ~300 ms, guard with reduced-motion, and **move focus to the new content on navigation** — otherwise keyboard and screen-reader users are stranded on the old page's focus position.

---

## Quick audit

```text
transition: all        transition-all
opacity-0              animate-fade-in        data-aos
initial={{ opacity: 0, y: 20 }}
duration-500  duration-700  duration-1000     (on hover or micro-interactions)
animate-pulse  animate-bounce  animate-spin   (outside a loading state)
infinite               animation-iteration-count: infinite
parallax    locomotive    lenis    scroll-snap-type: y mandatory
autoplay               <video ... autoplay
cursor: none           custom-cursor
outline: none          (with no :focus-visible replacement)
```

Then check the floor: **does `prefers-reduced-motion` appear anywhere in this codebase?** If you shipped animation and it does not, the work is not finished.

---

## Sources & further reading

- [WCAG 2.3.3: Animation from Interactions (Level AAA)](https://dequeuniversity.com/resources/wcag2.1/2.3.3-animations-from-interactions)
- [Design accessible animation and movement, with code examples — Pope Tech](https://blog.pope.tech/2025/12/08/design-accessible-animation-and-movement/)
- [How to Create Engaging and Accessible WCAG-Compliant Animations — The A11Y Collective](https://www.a11y-collective.com/blog/wcag-animation/)
- [Reduced motion — accessibility glossary](https://www.disabilityworld.org/toolkit/glossary/reduced-motion/)
- [Animated content and timing — Yale Usability](https://usability.yale.edu/digital-accessibility/accessibility-resources/accessibility-articles/animated-content-and-timing)
- [Auto-Forwarding Carousels and Accordions Annoy Users — Nielsen Norman Group](https://www.nngroup.com/articles/auto-forwarding/)
