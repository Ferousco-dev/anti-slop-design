# 04 — Slop Taxonomy: Typography, Voice & Copy

> **Module:** 4 of N · **Status:** stable
> **Read when:** choosing typefaces, setting a type scale, or writing any user-facing text — headlines, body, CTAs, empty states, error messages.

Typography is where slop is most insidious. Bad typography does not scream like a purple gradient — it whispers. It creates a sense of wrongness users feel but cannot name. Generated typography is consistently mediocre: safe, symmetrical, forgettable.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 4.1 Inter as the only font

**CRITICAL**

Inter is a genuinely good typeface — designed for screens, excellently hinted, huge character set, superb at small sizes. It is also the default in nearly every AI design tool, component library, and site builder. Inter plus a system fallback and no other typographic decision is a strong signal the design was never intentionally styled. Vanilla ice cream: pleasant, inoffensive, unmemorable.

Estimates in 2026 put Inter in the overwhelming majority of new UI work. That ubiquity, not the design, is the problem.

**Banned specifics**

- Inter as the only family on the site
- Inter for both headings and body with no differentiation
- `font-family: 'Inter', sans-serif` as an unexamined global default
- No pairing at all — no display/body distinction
- System stacks with no deliberate selection
- Loading Inter from Google Fonts without ever considering an alternative
- "It's the default" or "it looks clean" as the reason

**Why this is slop**

Inter shipped in 2017 and became the design community's favorite: free, well made, screen-optimized. Tailwind adopted it. Vercel, Linear, and Notion used it. Every tutorial, template, and starter kit included it. Models trained on that corpus learned *Inter = modern web design*, and now reach for it whenever the prompt leaves the choice open.

**Typography is the single fastest lever for escaping slop.** Changing one typeface transforms a generic page into a recognizable one more cheaply than any other single change.

**Instead — a deliberate pairing**

One distinctive display face plus one highly readable text face, chosen to match the brand's personality.

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
| Minimal / premium | Söhne, Graphik, or Helvetica Now as a single family | Swiss, timeless |

Strong single-family Inter alternatives when a pairing is overkill: **Geist**, **Satoshi**, **Switzer**, **Work Sans**, **IBM Plex Sans**, **Public Sans**. Each carries more personality than Inter at comparable quality.

**How to choose**

1. Name the brand personality in exactly three words
2. Find a display face that embodies them
3. Find a text face that complements without competing
4. Test at every size you will actually ship — headline, body, caption, and the smallest label
5. Verify the character set, numerals (tabular for data), and available weights

```css
/* GOOD — a deliberate system */
:root {
  --font-display: 'Geist', system-ui, sans-serif;
  --font-body:    'Geist', system-ui, sans-serif;
  --font-mono:    'Geist Mono', ui-monospace, monospace;
}
h1, h2, h3 { font-family: var(--font-display); letter-spacing: -0.02em; }
body       { font-family: var(--font-body); }
code, pre  { font-family: var(--font-mono); }
```

**Craft details that separate real typography from defaults**

- **Optical sizing.** Tighten tracking as size increases: display type needs negative letter-spacing (`-0.02em` to `-0.04em`), small text often needs slightly positive.
- **Tabular numerals** (`font-variant-numeric: tabular-nums`) anywhere numbers align or update — tables, prices, timers, dashboards.
- **Line height scales inversely with size.** ~1.1 for display, ~1.5–1.6 for body, ~1.4 for captions. A single global `leading-relaxed` is a tell.
- **Load `font-display: swap`** and self-host or preload the display face. A flash of invisible text is a performance *and* craft failure.

---

## 4.2 System font stacks as the default

**HIGH**

`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` with no deliberate selection is the ultimate "I did not care about typography" signal: *I could not be bothered to choose, so the operating system decided.*

**Banned specifics**

- A system stack with no custom font anywhere
- Arial, Roboto, or Helvetica as primary with no justification
- No web font loaded from any source
- "System fonts are faster" invoked without weighing the brand cost
- Stacks that render differently per platform, breaking visual consistency for everyone

**Legitimate exceptions**

- Internal admin dashboards where load time genuinely dominates
- Documentation where readability is the only goal
- Utility apps with no brand surface
- When the system font *is* the brand

**Instead** — load at least one custom face for display. Self-host for performance and privacy. Subset it. Use `font-display: swap` and `<link rel="preload">` for the face that appears above the fold.

---

## 4.3 Centered body text

**HIGH**

Center-aligning paragraphs longer than two lines creates a ragged left edge that measurably slows reading. The eye anchors on the left margin; when that anchor moves every line, tracking from line to line costs effort.

**Banned specifics**

- Any centered paragraph longer than 2 lines
- Centered body copy in feature sections and cards
- Centered blog content or FAQ answers
- Any centered text block longer than ~40 characters

**Instead**

- Left-align all body text. Always.
- Center only: short headlines (1–2 lines), CTAs, nav items, single-line labels
- Constrain measure with `max-w-prose` / `max-w-2xl` — target **45–75 characters per line**
- Use `text-wrap: balance` on headlines to prevent orphans, `text-wrap: pretty` on body

```html
<!-- GOOD — centered headline, left-aligned body -->
<div class="text-center mb-8">
  <h2 class="text-3xl font-semibold text-balance">Analyze any APK in seconds</h2>
</div>
<div class="max-w-prose mx-auto">
  <p>Decompiles, inspects, and reports on every layer of a mobile application —
  from manifest permissions to native libraries.</p>
</div>
```

---

## 4.4 Em-dashes in marketing copy

**CRITICAL for marketing copy** — with an important caveat below.

**Banned specifics**

- Em-dashes in headlines, hero text, taglines, or slogans
- Em-dashes in CTAs or button labels
- Em-dashes manufacturing dramatic pauses in marketing copy
- Multiple em-dashes in a single paragraph
- Em-dashes where a colon, period, or comma would do
- Em-dashes in email subject lines and social posts

**Why the ban**

Models insert em-dashes at a far higher rate than most writers because they have learned the mark signals sophisticated flow. The result reads like a Victorian novel: "Our platform—built for developers—delivers insights—powerful, actionable insights—that transform your workflow." That is not sophisticated. It is the written equivalent of pausing constantly to sound thoughtful.

**The caveat — do not treat the em-dash as a detector**

The popular claim that em-dashes *prove* AI authorship does not hold up, and it has caused real harm: students and professional writers have been falsely accused, and detection tools disagree wildly on the same text. Plenty of human writers — essayists, fiction readers, Substack natives — use the mark constantly, while AP-trained journalists avoid it. "More frequent than average" is not "reliable signal."

**So: ban it in marketing copy as a discipline, not as a diagnostic.** The reason to avoid it in a headline is that it is usually a weaker choice than a period, not that its presence convicts anyone.

**The tell that actually matters: cadence uniformity.** The strongest signature of generated prose is rhythm — sentence after sentence landing in the same 18–24 word range, paragraph after paragraph running the same length, every section built to the same template. Vary sentence length aggressively. A three-word sentence after a long one does more to sound human than any punctuation rule. See [§4.9](#49-perfectly-structured-lists--subheadings).

**Instead**

- Periods for breaks. Colons to introduce. Semicolons to join related clauses.
- En-dashes for ranges (`2024–2026`); hyphens for compounds.
- Restructure the sentence rather than reaching for the dash.
- If you truly need one in long-form: at most one per 500 words, never in marketing copy.

```text
BANNED: "Acme—your mobile analysis platform—delivers insights in seconds."
BANNED: "Analyze—decompile—inspect—any APK with one click."

GOOD:   "Acme delivers insights in seconds."
GOOD:   "Analyze, decompile, and inspect any APK with one click."
```

---

## 4.5 Overly perfect, symmetrical alignment

**MEDIUM**

Every headline centered. Every card title centered. Every section symmetrically balanced. A monotonous rhythm that reads robotic, because it is.

**Banned specifics** — every text element centered; perfect symmetry across all sections; zero alignment variation; predictable alternating patterns; every card centered.

**Instead** — vary alignment with intent. Left for editorial and long-form. Centered for CTAs, short headlines, and nav. Right for pull quotes, captions, and metadata. Align to a grid rather than a centerline. Never justify text on the web — without hyphenation control, it produces rivers of whitespace.

---

## 4.6 Generic superlatives & buzzwords

**CRITICAL**

Vague superlatives that say nothing specific. Hallucinations of sophistication — purple prose that distances the reader from the product. The verbal equivalent of a purple gradient.

**Forbidden words**

*Verbs of empty motion:* delve, leverage, unlock, enhance, elevate, unleash, utilize, facilitate, optimize, streamline, empower, envision, embark, navigate, cultivate, foster, champion, propel, catalyze, augment, fortify, spearhead, galvanize, revolutionize, reimagine, supercharge, turbocharge, amplify, maximize, harness, transform.

*Adjectives of empty praise:* robust, seamless, multifaceted, comprehensive, pivotal, unwavering, holistic, nuanced, cutting-edge, transformative, revolutionary, next-gen, state-of-the-art, world-class, industry-leading, best-in-breed, turnkey, disruptive, innovative, groundbreaking, pioneering, trailblazing, visionary, dynamic, proactive, synergistic, impactful, actionable, bulletproof, rock-solid, future-proof, battle-tested, mission-critical, enterprise-grade.

*Nouns of empty scale:* tapestry, synergy, paradigm shift, testament, myriad, plethora, landscape, beacon, journey, roadmap, symphony, game-changer.

*Qualified only by context:* scalable, agile, strategic, data-driven, cloud-native, production-ready, AI-powered, machine-learning-driven, customer-centric, results-oriented, forward-thinking — banned when used vaguely; fine when attached to a specific, checkable claim.

**Forbidden phrases**

- "It's not just about X, it's about Y"
- "In today's rapidly evolving landscape" / "In today's world" / "In recent years"
- "Unlock / harness the power of…"
- "Elevate your [workflow/team/strategy]"
- "Take your X to the next level" / "Supercharge your X"
- "The ultimate / complete / all-in-one X"
- "Your X, reimagined" / "Reinventing X" / "Redefining X"
- "The new standard in X" / "Setting the standard for X" / "Raising the bar"
- "Pushing the boundaries" / "Breaking new ground" / "At the forefront of"
- "Shaping / building the future of X" / "Welcome to the future of X"
- "Where X meets Y" / "The intersection of X and Y" / "Bridging the gap"
- "The best of both worlds" / "The perfect blend of X and Y"
- "Powerful yet simple" and every permutation
- "Form meets function" / "Style meets substance" / "Beauty meets brains"
- "End-to-end solution" / "One-stop shop" / "Single source of truth" / "360-degree view"
- "At your fingertips" / "The possibilities are endless" / "The sky's the limit"

**Why these are slop**

This is consensus language — the average of every business website ever written. Generated copy reaches for the words that appear most often in business contexts, producing prose that sounds like a committee of consultants: technically correct, emotionally empty, entirely forgettable.

Real copy has edges. It takes a stance. "We analyze APKs in 30 seconds" beats "We leverage cutting-edge technology to deliver transformative insights." The first tells you something.

**Instead**

1. **Write as a specific human with opinions.**
   - BAD: "Leverages AI-powered technology to deliver comprehensive insights."
   - GOOD: "Shows you exactly what's inside any APK — permissions, libraries, assets, code structure — in under 30 seconds."
2. **Concrete nouns, active verbs.**
   - BAD: "Enhances your mobile security posture."
   - GOOD: "Finds vulnerabilities in your APK before attackers do."
3. **Replace abstractions with observable facts.**
   - BAD: "Unlock the power of mobile analysis."
   - GOOD: "See every permission, library, and asset in your APK."
4. **Specific numbers.**
   - BAD: "Trusted by thousands of developers."
   - GOOD: "Used by 2,437 developers on 12,000+ APKs."
5. **Take a stance.**
   - BAD: "May help you improve your mobile security."
   - GOOD: "Most mobile apps request permissions they don't need. We find them."

---

## 4.7 Vague aspirational headlines

**CRITICAL**

Headlines generated by averaging every headline ever seen say nothing about the product.

**Banned headlines** — "Build the future" · "Your all-in-one platform" · "Scale without limits" · "The future of [industry]" · "Empowering teams to [vague verb]" · "Redefining [category]" · "Next-generation [product]" · "The ultimate [tool]" · "Experience the difference" · "Discover the power of X" · "Welcome to [product]" · "Transform / revolutionize / supercharge your X" · "The smart way to X" · "A better way to X" · "The only X you'll ever need" · "Everything you need for X" · "Your X, simplified."

**What good looks like**

| Company | Headline | Why it works |
|---|---|---|
| Stripe | "Financial infrastructure for the internet" | Specific category, clear audience, zero buzzwords |
| Linear | "Plan and build products" | Two verbs, four words, no fluff |
| Notion | "Your wiki, docs, and projects. Together." | Three concrete nouns, one clear claim |
| Vercel | "Develop. Preview. Ship." | Three actions describing the actual workflow |
| Raycast | "Blazingly fast, totally extendable launcher" | Concrete category, human word choice |

**Rule:** explain what the product does in 10 words or fewer, with specific nouns and verbs. No buzzwords, superlatives, or aspirations.

```text
BAD:  "The future of mobile analysis"
BAD:  "Unlock the power of APK insights"
GOOD: "See inside any APK in 30 seconds"
GOOD: "Decompile, inspect, and understand any Android app"
```

---

## 4.8 Hedging language

**HIGH**

Hedging protects the writer from being wrong — and protects the reader from being convinced.

**Banned** — "may help you," "can potentially," "designed to," "aims to," "seeks to," "is intended to," "is meant to," "can be used to," "has the potential to," "could potentially," "might be able to," "is expected to," "is projected to."

Also restructure rather than using: "allows you to," "enables you to," "provides the ability to," "offers the opportunity to," "makes it possible to." Usually "lets you" works, and often the whole clause can go.

```text
BAD:  "Acme is designed to help you analyze APKs."
GOOD: "Acme analyzes APKs in 30 seconds."

BAD:  "This tool allows you to decompile mobile applications."
GOOD: "Decompile any APK with one click."
```

---

## 4.9 Perfectly structured lists & subheadings

**MEDIUM**

**Banned patterns**

- Every section following heading → subheading → bullets
- Bullets that all start with a verb in the same tense
- Lists of three everywhere ("faster, simpler, safer")
- Repeated "Whether X or Y" constructions
- Point-Example-Explain-Restate in every paragraph
- Every paragraph exactly 3–5 sentences
- Every section with the same number of bullets

**Why this is slop**

This is the **cadence uniformity** tell, and it is the most reliable signature of generated prose — far more so than any individual word or punctuation mark. Real writing has rhythm. Some paragraphs are one sentence. Some are ten. Some sections use lists; some flow continuously. That variation is what humanity sounds like.

Generated writing has no rhythm because it has no ear. It is structurally perfect and emotionally flat — a metronome, technically correct and musically dead.

**Instead**

- Vary paragraph length dramatically: one sentence, then seven, then two
- Let some sections carry no subheading and no bullets at all
- Mix prose with lists rather than defaulting to lists
- Break your own structural patterns on purpose
- Some sections should be a single paragraph that lands

---

## 4.10 Passive voice dominance

**MEDIUM**

**Banned** — "The platform was designed to…" · "Insights can be gained by…" · "Your workflow will be streamlined…" · "Results are provided to you…" · passive in more than ~20% of sentences · any passive in a headline or CTA.

Passive voice earns its place in scientific and legal writing, where the actor is unknown or irrelevant. In product copy it is a crutch that distances the product from the action and turns promises into observations.

```text
BAD:  "Your APK is analyzed by Acme in 30 seconds."
GOOD: "Acme analyzes your APK in 30 seconds."

BAD:  "Permissions are extracted from the manifest file."
GOOD: "Acme extracts every permission from the manifest."
```

---

## 4.11 Formal academic transitions

**HIGH**

Transitions that read like a graded essay rather than a product page: *Furthermore · Moreover · Additionally · In conclusion · It is important to note · As previously mentioned · In summary · In essence · At its core · Fundamentally · Ultimately · Consequently · Therefore · Thus · Hence · Accordingly · Subsequently · Notwithstanding · Nevertheless · Nonetheless · Conversely · In contrast · Similarly · Likewise · In the same vein · By the same token · In light of this · As a result · As such · In this regard · With respect to · In terms of · With regard to · Pertaining to · Regarding · Concerning.*

**Instead** — conversational bridges ("But here's the thing," "The problem is," "Here's why that matters:"), or no transition at all. Often the strongest move is to start the next thought and trust the logic to connect.

---

## 4.12 The "Whether X or Y" construction

**MEDIUM**

"Whether you're a developer or a security researcher…" tries to include everyone and reaches no one — the copywriting equivalent of a campaign speech.

**Also banned** — "No matter your role" · "Regardless of your experience level" · "From beginners to experts" · "For teams of all sizes."

**Instead** — pick a primary audience and write to them. Separate pages or sections for genuinely separate audiences. Specific scenarios instead of broad categories.

```text
BAD:  "Whether you're a developer or a security researcher, Acme helps you analyze mobile apps."
GOOD: "Security teams use Acme to find vulnerabilities before attackers do."
```

---

## 4.13 The "Imagine if" opening

**MEDIUM**

"Imagine if you could…" · "What if you could…" · "Picture this:" · "Envision a world where…" · "Think about a future where…"

**Instead** — open with a fact ("Most APKs request permissions they don't need"), a problem ("Reviewing a third-party APK by hand takes hours"), or the solution stated plainly.

---

## 4.14 The "We believe" statement

**MEDIUM**

"We believe that…" frames a claim as the company's opinion rather than a fact, and creates distance. Same for "Our philosophy is that…" and "We are committed to…"

**Instead** — state it directly ("Mobile security should be accessible to everyone"), or better, demonstrate it ("Free for open-source projects").

---

## 4.15 The "We are" opening

**LOW**

"We are a team of…" · "We are building…" · "We are passionate about…" · "We are dedicated to…"

Users do not care what you are. They care what you do for them.

**Instead** — start with the user, the problem, or the solution.

---

## 4.16 The "Our Mission" section

**LOW**

Mission statements matter internally and rarely belong on a product page — especially when longer than the feature descriptions.

**Instead** — express mission through the product narrative and through actions. If you must state it, one sentence.

---

## 4.17 The FAQ as crutch

**MEDIUM**

An FAQ used as a dumping ground for information that should have been in the main content.

**Banned** — FAQs answering basic questions the page should already answer ("What is [product]?"); FAQ items that belong in feature descriptions; more than 8 items; obviously generated question/answer pairs; FAQ substituting for information architecture.

**Instead** — answer the important things in the main content. Reserve the FAQ for genuine objections and edge cases, 3–5 items on a landing page. Move anything larger to documentation.

---

## 4.18 "Contact us" as a generic CTA

**LOW**

"Contact us to learn more" · "Get in touch" · "Reach out" · "Let's talk" · "Schedule a demo" on a self-serve product.

**Instead** — a specific next action: "Analyze your first APK." Guide the user to the next real step. If the product is self-serve, do not make people talk to you.

---

## 4.19 Newsletter signup as the default footer CTA

**LOW**

**Instead** — offer something specific and defensible ("Weekly APK security reports"), state the value ("Join 2,400 developers reading it"), and if the newsletter is not worth subscribing to, do not ask.

---

## 4.20 Lorem Ipsum & placeholder copy

**CRITICAL**

The ultimate slop signal.

**Banned** — "Lorem ipsum dolor sit amet" · "Your text here" · "Description goes here" · "Coming soon" · "TBD" · "Placeholder" · fake names (John Doe, Jane Smith) · fake companies (Acme Corp, Example Inc) in *shipped* UI · `test@example.com` in a live interface.

**Instead** — write real copy for every element. If a section is not ready, do not ship the section. Use realistic data in screenshots and demos. Use real names and companies only with permission.

This applies with special force to the states everyone forgets: **empty states, loading states, error messages, and success confirmations.** "Something went wrong" is placeholder copy wearing a costume. Say what went wrong and what to do next.

---

## Quick audit

```text
Inter   -apple-system   BlinkMacSystemFont
text-center  (on any block > 2 lines)
—  (em dash, in any marketing string)
leverage  unlock  seamless  robust  elevate  empower  streamline
cutting-edge  next-gen  world-class  game-changer  revolutionary
"Build the future"  "all-in-one"  "The future of"  "Take your"
"designed to"  "allows you to"  "may help"  "aims to"
"Furthermore"  "Moreover"  "Additionally"  "Ultimately"
"Whether you're"  "Imagine if"  "We believe"  "We are a team"
Lorem ipsum  John Doe  example.com  "Coming soon"  "Something went wrong"
```

Then read the draft aloud and measure the rhythm. If every sentence lands at the same length, rewrite for variation before anything else.

---

## Sources & further reading

- [The Em-Dash Myth: What Actually Gives Away AI Writing](https://www.duey.ai/post/em-dash-ai-writing)
- [The em dash is not an AI red flag](https://www.thinklikeapublisher.com/the-em-dash-is-not-a-red-flag-its-a-beat-that-a-comma-cant-land/)
- [Em Dashes, Hyphens and Spotting AI Writing — Plagiarism Today](https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/)
- [Stop Using Inter Font: 7 Clean Alternatives for UI Design](https://superfiles.in/7-clean-alternatives-to-inter-font.php)
- [Best Inter alternative typefaces & similar fonts — Zetafonts](https://www.zetafonts.com/collections/similar-to/inter)
- [24 Best Fonts for Websites — Figma resource library](https://www.figma.com/resource-library/best-fonts-for-websites/)
- [AI Slop Fonts and Gradients: The Tells That Give Away AI Design](https://www.925studios.co/blog/ai-slop-design-tells)
