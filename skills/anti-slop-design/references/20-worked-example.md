# 20 — Worked Example

> **Module:** 20 of N · **Status:** stable
> **Read when:** you want to see the protocol run end to end, or you are unsure what "state your decisions" actually looks like in practice.

Every other module describes a process. This one runs it, on a real brief, with the wrong turns left in — because the wrong turns are where the process actually earns its keep.

**The build:** a marketing site for a YouTube strategy agency. Six pages. Next.js and Tailwind. Live, so every claim here is checkable.

---

## Phase 0 — The brief

Five questions from [`14-workflow.md`](14-workflow.md) phase 0, answered from the client's own brand document rather than inferred:

| | |
|---|---|
| **Product** | YouTube strategy that gets B2B and B2C businesses booking sales calls. Research and scripting, not an editing shop. |
| **Primary user** | Coaches, SaaS founders and agency owners already making money, with a validated offer and a sales system that closes. Bottlenecked on attention, not on product or closing. |
| **Register, three words** | Direct. Proven. Unpretentious. |
| **Must not look like** | A guru site. No manifestation language, no lifestyle imagery, no fabricated proof. The client's own words: *"I don't larp."* |
| **Primary action** | Book a call. Secondary, lower risk: a $597 test video. |

**Given constraints** — not chosen, inherited: brand colours `#ffffff` `#000000` `#8f56ff` `#ff69c5`, and Helvetica Bold with Playfair Display Italic.

**The immediate problem:** the brand's primary is purple, which [`03-color-patterns.md`](03-color-patterns.md) bans as a CRITICAL. [`14-workflow.md`](14-workflow.md) resolves it — a *specified* brand colour is not the unexamined default the ban targets. So it stays, with a discipline attached: solid only, never a gradient, roughly 10% of the surface, no `indigo-500` anywhere near it.

---

## Phase 1 — The six axes

From [`15-product-types.md`](15-product-types.md). Category: **agencies and studios**, whose starting position is sparse · varies · low formality · medium energy · varies · high contrast.

| Axis | Chosen | Why |
|---|---|---|
| Density | Sparse | One argument per screen. The buyer is time-poor and skeptical. |
| Warmth | Cool | The brand's whole position is *no hype*. Warmth would read as selling. |
| Formality | Low | Direct operator voice, contractions throughout. |
| Energy | Medium | The medium is YouTube. Still would misread the industry. |
| Ornament | Very low | Decoration is what a guru site does. |
| Contrast | High | Skeptical readers scan before they read. |

**Named thesis:** *Swiss editorial, set loud. Helvetica Bold at display scale with tight negative tracking, black on white, sharp corners, hairline rules as the only ornament. Playfair italic as the single human voice. Purple used solid and rarely — reserved for where money or commitment changes hands.*

**Dominant anxiety:** *credibility*. That single word decided the whole site — see phase 5.

---

## Phase 2 — The system, derived from the axes

Not chosen per component. Derived once from the six positions above.

| From | To |
|---|---|
| Cool + low ornament | Cool neutral ramp, `oklch(… 0.008 285)` — a constant small chroma at a fixed hue, which is what a "cool grey" is |
| High contrast | Type ratio ~1.333, jumps large enough to read at a glance |
| Low ornament | Radius sharp by default: `0` on nav and tables, `2px` on inputs, `4px` on panels. No uniform value. |
| Medium energy | Motion 100–200ms, exits ~⅔ of entrances, custom easing tokens rather than bare `ease` |
| Sparse | Section padding varies by content density rather than one global `py-24` |
| Cool + credibility | Tabular numerals everywhere a number appears |

**A contrast failure surfaced here, before any component existed.** The brand purple `#8f56ff` measures **4.25:1** against white — under the 4.5:1 AA floor for text. Not a judgement call; a measurement.

Resolution: keep the exact hex for *graphical* roles, where the floor is 3:1 and it passes — borders, focus ring, rules. Add a darker step at the same hue for anything carrying white text, which measures 5.52:1. Brand fidelity where it reads as brand, legibility where it has to be read.

---

## Phase 3 — Build, and the first wrong turn

The bans were applied thoroughly. No gradient, no glassmorphism, no three-card grid, no stock photo, no fabricated proof. Every instant-reject in [`13-pre-emit-checklist.md`](13-pre-emit-checklist.md) Gate 1 was clear.

**The client's reaction: "I feel this design looks ugly."**

They were right, and the diagnosis is [`01-philosophy.md`](01-philosophy.md) §9 — **austerity**. Modules 02–10 are subtractive. Run them alone and you get a page with nothing wrong and nothing in it. Specifically:

- The brand had four colours; two were in use. Purple appeared on one button. Pink appeared nowhere.
- The hero's visual anchor was a grey box with a 1px grey border — which is §2.1.6 card-ification, banned in a module that had been read and then quietly violated because a box was the fastest way to fill a column.
- Register mismatch: a Swiss legal textbook for a YouTube agency. Technically consistent with "direct, unpretentious", and wrong for the medium.

**The fix was additive, and it came from the brand's own material rather than from taste.** The logo turned out to be the Arabic letter *nūn* — the letter the company is named for — wrapped in corner brackets. Those brackets are a **viewfinder**. The brand mark already contained the frame idea, so:

- Corner brackets became a component, used on the one element carrying the argument
- 16:9 frames with duration chips became layout units — the medium's own furniture, not decoration
- Purple went from one button to carrying whole sections at a deeper step that supports two text levels
- Pink was dropped entirely rather than half-used

---

## Phase 4 — Self-critique found six real defects

Running Gate 1 as a grep, then the accessibility gate as an automated suite. Each of these shipped before the gate caught it:

1. **Em-dashes in the page title and throughout body copy.** §8.21 bans them in marketing copy. Removed from every user-facing string.
2. **Contrast, six failures.** `neutral-400` numerals at ~2.5:1. `neutral-300` stage numbers at ~1.9:1, under even the 3:1 large-text floor. Footer headings too dark on ink. A placeholder below AA.
3. **`.eyebrow` hardcoded a colour** that silently overrode callers on dark surfaces, so a label rendered dark-on-purple and was nearly invisible. Caught by looking, not by grep.
4. **Horizontal scroll at 375px on every page.** Grid children default to `min-width: auto`, so a child that cannot shrink widens the track past the viewport — the hero track was 460px inside a 375px screen.
5. **The hamburger showed at every breakpoint.** Not a breakpoint bug: custom CSS appended *outside* any `@layer` beats everything inside one, so `display: inline-flex` overrode Tailwind's `md:hidden` and the media query never got a say. Now [`09`](09-code-patterns.md) §9.4b.
6. **A tofu box in the footer.** The watermark was set as the Unicode character `ن`, and the Helvetica/Arial system stack has no Arabic glyph on iOS. It rendered as an empty square. Perfect on the build machine. Now [`10`](10-image-media-patterns.md) §10.4b.

**Then a seventh, in production only.** Three of four hero proof thumbnails rendered blank on a cold load: only the first was marked priority, so the rest lazy-loaded. All four sit above the fold, and that panel is the one thing on the page that must be there immediately.

**None of these were visible in a screenshot.** That is the argument for the gate.

---

## Phase 5 — Where trust signals decided the design

[`18-trust-signals.md`](18-trust-signals.md), applied. Dominant anxiety: *credibility*. Available evidence, sorted by the proof ladder:

| Tier | Asset | Used |
|---|---|---|
| 1 | Four YouTube searches where client videos hold top 3 | **Hero.** The strongest asset on the site. |
| 1 | Six public client channels | Linked, watchable |
| 2 | A case-study video on the client's own channel | Work page |
| 2 | Live search-result screenshots | Work page |
| 3 | Revenue figures — real, from the brand document | **Withheld.** Not cleared in writing. |

**The decision that shaped everything:** the tier-1 asset is a *challenge*, not a claim. The hero says **"Don't take our word for it — search these four on YouTube"**, with each query paired to the thumbnail of the video that ranks for it and a link to the real channel. A visitor can falsify the entire page in about ten seconds.

That is why the revenue figures stayed off. A site whose central argument is *go and check* cannot quietly publish unverified numbers — and it says so on the page rather than leaving a silent gap. The content file gates them behind a `cleared` flag, and the Work page renders an honest explanation instead.

**A permission classifier blocked one commit** that would have rendered named clients' revenue. It was right to. The gate had been written two steps earlier and walked past.

---

## Phase 6 — Stating the decisions

The protocol's step 6, as actually delivered:

> Chose to keep the brand purple but only as a solid, never a gradient, at ~10% of surface — the ban targets the unexamined default, not a specified brand colour, and the discipline is what stops it drifting into the generic. Added a darker step for anything carrying white text because the brand hex measures 4.25:1, under AA.
>
> Radius varies by purpose rather than one value: 0 on nav and tables, 2px on inputs, 4px on panels. Sharp reads precise, which is the register.
>
> The hero anchor is the ranking challenge rather than a mockup, because the buyer's dominant anxiety is credibility and a checkable claim beats an unfalsifiable one.
>
> Corner brackets and 16:9 frames are lifted from the client's own logo lockup, which is a viewfinder. Not decoration — the brand already contained the idea.
>
> Dropped pink entirely rather than using it weakly, and left the revenue figures off pending written client clearance. A page that tells people to verify everything cannot publish unverified numbers.

**And what was not done**, stated plainly: no keyboard pass at the time of first delivery, no screen-reader pass, the Helvetica webfont licence undecided, and no photograph of the founder because the source document contained none usable.

---

## What this example is actually for

Four things worth taking from it:

1. **The bans are the easy half.** Every Gate 1 item was clear and the result was still wrong. Austerity passes every subtractive check.
2. **The brand usually contains the answer.** The viewfinder was sitting in the logo the entire time. Read the source material properly before inventing a direction.
3. **The defects that matter are invisible in a screenshot.** Six of seven were contrast, cascade, layout or glyph failures. Only automation and real devices find those.
4. **Constraints improve the work.** Not being allowed to publish revenue figures forced the ranking challenge into the hero, and that is the best thing on the site.

**Six findings from this build went back into the skill:** austerity as a named failure mode, the em-dash correction, the craft gate in Gate 6, the cascade-layer pattern (§9.4b), the Unicode-glyph pattern (§10.4b), and mobile sticky headers. A skill that never gets used never gets corrected.
