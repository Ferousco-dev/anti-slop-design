# 15 — Product Types & Design Personality

> **Module:** 15 of N · **Status:** stable
> **Read when:** choosing a direction, at [`14-workflow.md`](14-workflow.md) phase 1, before any pixel. Also when a design is technically clean and still feels wrong.

Module 14 says *commit to a direction*. This is the module that tells you which directions exist and which ones fit what you are building.

That gap matters, because "pick a direction" with no vocabulary is exactly the prompt that produces the mean. A model asked to be distinctive with no frame reaches for whatever "distinctive" looks like on average — which is how you get brutalism on a pension dashboard.

---

## 1. The failure this prevents: register mismatch

A page can pass every ban in modules 02–10, hold together as a system, meet every contrast floor, and still be wrong — because the *register* does not match the product.

Register is the tone a design speaks in. Getting it wrong is not a taste failure, it is a **comprehension** failure: the visitor reads the wrong thing about what the product is, before they read a word.

| Product | Wrong register | What the visitor concludes |
|---|---|---|
| A YouTube agency | Swiss legal textbook | "These people are not in this industry" |
| A children's learning app | Enterprise data density | "This is for my school district, not my kid" |
| A pension provider | Playful, bouncy, illustrated | "I would not put my retirement here" |
| A developer CLI | Soft gradients and rounded illustration | "This is a landing page, not a tool" |
| A luxury resort | Dense feature comparison table | "This is a booking aggregator" |
| A hospital system | Startup marketing energy | "Is this a real clinic?" |

**The test:** describe the design out loud without naming the product — "quiet, precise, monochrome, generous space" — and ask someone what it sells. If their guess is a different category, the register is off.

Restraint is not universally correct. It is correct *for categories where restraint signals competence*. In a category where warmth signals competence, restraint reads as coldness, and the same design that looks premium on a fintech site looks unwelcoming on a preschool's.

---

## 2. Personality as axes, not adjectives

Adjectives are unusable. "Modern", "clean", "professional" constrain nothing and are why briefs fail. Axes are decidable: each one is a position you can name, defend, and translate into a token.

Set six positions before designing. Together they *are* the direction.

| Axis | One end | Other end | Mostly decided by |
|---|---|---|---|
| **Density** | Sparse, one idea per screen | Dense, many values visible at once | How often the user is here, and whether they compare things |
| **Warmth** | Cool, neutral, machined | Warm, human, tactile | Whether the user is anxious or comfortable |
| **Formality** | Institutional, composed | Casual, conversational | The size of the commitment being asked |
| **Energy** | Still, calm, slow | Kinetic, immediate, loud | Whether the medium itself is energetic |
| **Ornament** | Structural only, no decoration | Expressive, illustrative, textured | Whether the product's value is legible without help |
| **Contrast** | Even, quiet hierarchy | Extreme scale jumps, loud emphasis | Whether the user scans or reads |

**How the axes become a system**

- **Density** → spacing scale base, type scale ratio, line height, how much sits above the fold
- **Warmth** → neutral temperature (warm greys vs cool), radius, typeface (humanist vs grotesque vs geometric)
- **Formality** → copy voice, contractions, whether the CTA says "Get started" or "Open an account"
- **Energy** → motion durations and easing, colour saturation, image treatment
- **Ornament** → whether illustration exists at all, texture, background treatment
- **Contrast** → type scale jumps, weight range, colour ratio

Two products in the same category can sit at different points on every axis. That is not a bug — that is where brand actually lives. **The axes are the vocabulary; the category is the starting position, not the answer.**

---

## 3. Types

Each entry gives: what the visitor is actually deciding, the starting position on the axes, what "premium" means here, and the specific way this category goes wrong.

### Developer tools, APIs, infrastructure

**They are deciding:** whether this will still work at 3am when it breaks, and whether the docs will answer them.
**Start:** dense · cool · low-formality · low-energy · no ornament · high contrast.
**Premium means:** speed, keyboard operability, real terminal output, docs that load instantly.
**Goes wrong by:** marketing at engineers. Soft gradients, illustrated mascots and "empower your team" copy read as *someone who does not build things made this*. Show the code in the first screen.
**Non-obvious:** a monospace face carries more trust here than any testimonial.

### B2B SaaS

**They are deciding:** whether this survives procurement and whether their team will actually adopt it.
**Start:** medium density · cool-neutral · medium formality · low energy · minimal ornament · medium contrast.
**Premium means:** the product visible early, real screenshots, pricing on the page, security and compliance reachable in one click.
**Goes wrong by:** being the exact page module 05 §5.1 describes. This is the category that invented the conveyor belt, and it is the hardest place to be distinctive — which is precisely why it pays most.
**Non-obvious:** an honest limitations section outperforms another feature grid.

### Fintech and financial services

**They are deciding:** whether their money is safe here.
**Start:** medium density · cool · high formality · low energy · minimal ornament · medium contrast.
**Premium means:** precision. Tabular numerals, exact figures, clear fees, no ambiguity about what happens to a balance.
**Goes wrong by:** two opposite ways. Too playful and it reads unserious with money. Too cold and it reads like the bank the user left. The successful modern versions run warm-but-composed, and buy the warmth with *copy and support*, not with bouncy animation.
**Non-obvious:** typography that draws attention to itself undermines trust here. A face nobody notices is the correct choice.

### Healthcare and anything clinical

**They are deciding:** whether they are safe and whether they understood correctly.
**Start:** sparse · warm · medium formality · still · minimal ornament · medium contrast.
**Premium means:** calm and unambiguous. Larger type than you think, plain language, one action per screen, no dark patterns anywhere near consent.
**Goes wrong by:** startup energy. Urgency mechanics, growth-marketing copy and playful motion are actively harmful when the reader may be frightened or unwell.
**Non-obvious:** accessibility is not a floor here, it is the product. Assume impaired vision, tremor, low literacy, and stress.

### E-commerce and retail

**They are deciding:** what this actually looks like, and whether returning it will be a fight.
**Start:** dense · warm · low formality · medium energy · medium ornament · high contrast.
**Premium means:** photography quality, and friction removed from the boring parts — sizes, shipping, returns, stock.
**Goes wrong by:** fake urgency. Countdown timers, "only 2 left" and manufactured scarcity are the category's default and are now regulated as deceptive design in several jurisdictions. They also stop working the moment a shopper recognises them.
**Non-obvious:** the product image is the entire design. Everything else is arranging it.

### Marketplaces

**They are deciding:** whether there is enough supply, and whether they will be scammed.
**Start:** dense · neutral · low formality · medium energy · low ornament · medium contrast.
**Premium means:** real inventory visible immediately, honest ratings including bad ones, and an obvious dispute path.
**Goes wrong by:** designing for the buyer and forgetting the seller, who needs a completely different and usually denser interface.

### Agencies, studios, freelancers

**They are deciding:** whether you can do for them what you did for the work on the page.
**Start:** sparse · varies · low formality · medium energy · varies · high contrast.
**Premium means:** the work, large, first, with real outcomes. The site is itself the portfolio piece and is judged as one.
**Goes wrong by:** hiding the work behind a philosophy statement. Also by over-designing: an agency site that is more interesting than the work makes an argument against itself.
**Non-obvious:** a specific niche stated plainly out-converts a broad one, because the buyer is looking for someone who has done *their* problem.

### Personal brands and creators

**They are deciding:** whether they like and trust this person.
**Start:** sparse · warm · low formality · medium energy · medium ornament · high contrast.
**Premium means:** a real face, real voice, and the work reachable in one click.
**Goes wrong by:** performing an agency. A single person pretending to be a "we" is transparent and costs the exact intimacy that makes this format work.

### Editorial, publishing, blogs

**They are deciding:** whether this is worth their time.
**Start:** sparse · warm · medium formality · still · low ornament · high contrast.
**Premium means:** reading experience. Measure, line height, a real type pairing, and no interruption between the reader and the sentence.
**Goes wrong by:** monetisation. Interstitials, autoplay, newsletter modals over the second paragraph. Each one is a small argument that the reader is inventory.
**Non-obvious:** this is the category where a serif is usually correct and where a display face earns its licence fee.

### Dashboards and internal tools

**They are deciding:** nothing. They already work here. They want to finish the task.
**Start:** very dense · cool · low formality · still · no ornament · medium contrast.
**Premium means:** speed, keyboard shortcuts, information density done well, and states that never lie about loading.
**Goes wrong by:** marketing-site instincts. Hero sections, generous whitespace and decorative charts waste the screen of someone who is here eight hours a day. Density is a *feature* here and nowhere else.
**Non-obvious:** the empty state and the 10,000-row state matter more than the demo state.

### Education and courses

**They are deciding:** whether they will actually finish it, and whether it will change anything.
**Start:** medium density · warm · low formality · medium energy · medium ornament · medium contrast.
**Premium means:** visible progress, a scoped curriculum, and honesty about time required.
**Goes wrong by:** transformation theatre. Income claims, before-and-after screenshots and countdowns are the category's slop, and the audience is now inoculated against them.

### Non-profit and public sector

**They are deciding:** whether the money reaches the thing.
**Start:** sparse · warm · medium formality · still · low ornament · medium contrast.
**Premium means:** clarity about where funds go, real photography of real work, and a donation flow with no dark patterns.
**Goes wrong by:** either guilt mechanics or corporate polish. Too slick reads as overhead.
**Non-obvious:** government and public services carry statutory accessibility requirements. This is legal compliance, not craft.

### Local service businesses

**They are deciding:** whether these people are real, close, and available.
**Start:** sparse · warm · low formality · still · low ornament · medium contrast.
**Premium means:** phone number, area covered, hours, real photos of real staff and real jobs — above the fold, on a phone.
**Goes wrong by:** aspiring to look like a SaaS company. The buyer wants a plumber, not a platform.

### Luxury and hospitality

**They are deciding:** how it will feel to be there.
**Start:** very sparse · warm · high formality · still · medium ornament · high contrast.
**Premium means:** photography, restraint, and slowness used deliberately — the one category where slower motion genuinely reads as expensive.
**Goes wrong by:** feature lists and comparison tables, which turn an experience into a commodity.
**Careful:** slow still has a ceiling. A 4-second hero video is atmosphere; a 4-second load is a bounce.

### Games and entertainment

**They are deciding:** whether this looks fun.
**Start:** dense · warm · low formality · kinetic · high ornament · extreme contrast.
**Premium means:** the work itself — footage, art, motion. This is the one category where maximalism is the correct answer and restraint is the mistake.
**Goes wrong by:** applying SaaS conventions to entertainment. A neutral, tasteful, well-spaced games site has failed.

---

## 4. Choosing when the category is mixed

Most real products sit across two. A fintech tool sold to developers, a healthcare SaaS, an education marketplace.

**Resolve it by the audience's dominant anxiety, not the industry label.** The anxiety decides the register:

- Money at risk → precision wins
- Health at risk → calm wins
- Reputation at risk → credibility wins
- Time at risk → speed wins
- Boredom at risk → energy wins

A fintech tool for developers is a *developer tool* — because the buyer's dominant anxiety is "will this break", not "is my money safe". A healthcare SaaS sold to hospital administrators is closer to B2B SaaS than to clinical, because the user is not the patient.

---

## 5. Where the category is the *wrong* answer

The starting positions above are conventions, and module 01 is clear that convention adopted unexamined is exactly the failure this skill exists to prevent.

Depart from the category when:

- **The brand genuinely is the exception.** A deliberately warm, illustrated bank is a real strategy — if it is a strategy, funded and consistent, rather than a mood.
- **The category default is the reason it is boring.** If every competitor is cool-neutral-restrained, warmth is a differentiator with a business case behind it.
- **The audience is not the industry's stereotype.** A pension product for 25-year-olds is not the same design problem as one for 60-year-olds.

Departing is fine. Departing *without noticing you departed* is not. Name it: **"This category usually runs formal and cool. We are running warm because ______."** If the blank cannot be filled, go back to the convention.

---

## Quick audit

Before building, these six are answered in writing:

- [ ] Density: ______
- [ ] Warmth: ______
- [ ] Formality: ______
- [ ] Energy: ______
- [ ] Ornament: ______
- [ ] Contrast: ______

Then:

- [ ] Category named, and its starting position stated
- [ ] Any departure from it named, with the reason
- [ ] The audience's **dominant anxiety** named in one word
- [ ] Described aloud without naming the product, someone would guess the right category

**The last one is the real test.** Everything else can be right while that is wrong, and when it is wrong nothing else rescues it.

---

## Sources & further reading

- [Fintech Brand Design: 16 case studies from Monzo to Robinhood](https://www.feelystudio.com/journal/the-evolution-of-fintech-design)
- [Fintech Branding Guide: build trust in financial tech](https://www.metabrand.digital/guides/startup-branding-guide/fintech-branding)
- [Material 3: personal, adaptive and expressive](https://zoewave.medium.com/material-3-design-system-e91a15d303a0)
- [Designing Personality — UXmatters](https://www.uxmatters.com/mt/archives/2013/12/designing-personality.php)
- [Basic Elements and Principles of Design — UXPin](https://www.uxpin.com/studio/blog/basic-elements-design/)
