# 08 — Slop Taxonomy: Copywriting & Content

> **Module:** 8 of N · **Status:** stable
> **Read when:** writing any user-facing words — headlines, body copy, CTAs, testimonials, case studies, blog posts, release notes, error messages, empty states.

Copy is where slop is most invisible and most damaging. Bad copy does not announce itself like a purple gradient — it whispers. Generated copy is consistently vague, hedging, and forgettable: technically language, actually noise.

This module owns **all word-level guidance**. Typeface and type-setting decisions live in [`04-typography-patterns.md`](04-typography-patterns.md).

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## The single test

Read the draft aloud. Then ask three questions:

1. **Could a competitor put their logo on this sentence unchanged?** If yes, it says nothing.
2. **Does it contain a number, a name, or a checkable claim?** If not, it is decoration.
3. **Would the founder actually say this out loud to a customer?** If not, rewrite it.

Almost every pattern below is a specific way of failing one of those three.

---

## 8.1 The "In today's world" opening

**CRITICAL**

**Banned openings** — "In today's rapidly evolving landscape…" · "In today's world…" · "In recent years…" · "As we navigate…" · "In the ever-changing world of…" · "In an era of digital transformation…" · "In the modern age…" · "In this day and age…" · "As technology continues to advance…" · "With the rise of AI…" · "In the age of [X]…" · "In a world where…" · "Now more than ever…"

**Why this is slop**

Pure filler. It adds no information and creates no engagement — it just signals that something generic is coming. It is the statistically safest opening, which is exactly why it offends no one and reaches no one.

**Instead — open on something that could only be about this product**

| Opening type | Example |
|---|---|
| Surprising stat | "73% of mobile apps request permissions they don't need." |
| Bold claim | "Most mobile apps are over-permissioned." |
| The user's pain | "Reviewing a third-party APK by hand takes hours." |
| A specific scenario | "You just installed an app. It asked for 12 permissions. Do you know what any of them do?" |
| A question with a real answer | "How many permissions does the average APK request? Twelve. How many does it need? Three." |

---

## 8.2 The "It's not just about X, it's about Y" formula

**CRITICAL**

**Banned** — "It's not just about the technology; it's about the people." · "…not just features; it's about outcomes." · "…not just speed; it's about precision." · "…not just data; it's about insights." · "…not just security; it's about trust." · "…not just the destination; it's about the journey." · every other permutation.

**Why this is slop**

A rhetorical device that manufactures depth by inventing a false dichotomy, implying the writer has transcended the obvious. It appears in a large share of generated business copy because it is learned wholesale from business blogs and self-help writing.

**Instead** — make the point directly. "The best software is useless if your team can't operate it." Or replace the philosophy with a specific: "It doesn't just list permissions. It tells you which ones are dangerous and why."

---

## 8.3 Lists of three

**MEDIUM**

**Banned** — "Faster, smarter, and more secure." · "Build, deploy, and scale." · "Simple, fast, and reliable." · "Powerful, flexible, and easy to use." · any tricolon of adjectives used as emphasis.

**Why this is slop**

The tricolon is a real rhetorical device that creates rhythm — which is why it is effective sparingly and deadening constantly. Generated copy reaches for it by default, and the result reads like a motivational poster.

**Instead** — two items for punch ("Fast and accurate"). Four or more for genuine coverage ("Permissions, libraries, assets, and code structure"). Vary the length deliberately. Best of all, replace adjectives with measurements: "30-second analysis. 99.7% accuracy. Full OWASP Top 10 coverage."

---

## 8.4 Uniform paragraph length — the cadence tell

**MEDIUM** by severity, **highest-value** by diagnostic power

**Banned** — every paragraph 4–5 sentences · every paragraph 3–4 lines · no variation in density · every paragraph following topic-sentence → explanation → example → conclusion.

**Why this matters more than any single word**

This is the tell that actually identifies generated prose. Not em-dashes, not any individual word — **rhythm**. Sentence after sentence landing in the same 18–24 word band, paragraph after paragraph running the same length, section after section built to the same shape.

Word-level bans are easy to satisfy while still sounding synthetic. Cadence is not. If you fix only one thing in a draft, fix this.

**Instead**

Vary aggressively. One sentence, then seven, then two.

Use a single-sentence paragraph as a landing point:

```text
Most mobile apps request permissions they don't need.

We find them in 30 seconds.
```

Then let a long paragraph do real explanatory work when the content earns it — decompiling the binary, parsing the manifest, extracting DEX files, mapping every permission and library, cross-referencing a vulnerability database, all inside half a minute. Long is fine when there is something to say.

And fragments land hard. Use them.

---

## 8.5 Perfect grammar with zero voice

**MEDIUM**

**Banned** — zero contractions · zero fragments · never starting a sentence with "And" or "But" · no informal register anywhere · grammar so clean it feels sterile · no humor, no opinions, no edge.

**Why this is slop**

Sterility reads as machine-authored because it usually is. Humans use contractions. Humans start sentences with conjunctions. Humans write fragments. Humans have opinions.

**A caution:** this does not mean introduce typos or errors. "Write badly to seem human" is a bad trade — errors cost credibility. The goal is *voice*, not *noise*.

**Instead**

- Use contractions naturally — "don't", "can't", "it's"
- Start with "And" or "But" when it improves flow: "We analyze your APK in 30 seconds. And we find things you didn't know were there."
- Use fragments for emphasis: "Fast. Accurate. Auditable."
- Write as if explaining to a smart friend: "Here's the thing — most apps ask for far more than they need."
- Take a stance: "Manual APK review is a waste of an afternoon."

---

## 8.6 Vague claims without numbers

**HIGH**

**Banned** — "Trusted by thousands of companies" · "Used by developers worldwide" · "Industry-leading" · "World-class" · "Best-in-class" · "Top-rated" · "Award-winning" · "The go-to solution for…" · "The #1 choice for…" · and every "The most [adjective]" construction — most powerful, most secure, most comprehensive, most advanced, most reliable, most user-friendly.

**Why this is slop**

Unverifiable and unmemorable. "Trusted by thousands" means nothing. "Trusted by 2,437 developers" means something — it is checkable, which is precisely what makes it persuasive.

There is also legal exposure. Unsubstantiated superiority claims ("the most secure", "#1") are actionable as false advertising in many jurisdictions, and competitors do file.

**Instead**

- Specific and verifiable: "2,437 developers"
- Measured: "Analyzes APKs in 30 seconds"
- Named, with permission: "Used by security teams at [real company]"
- Sourced: "99.97% uptime over the last 12 months" — linked to a public status page
- Honest when small: "47 teams, and growing" beats an invented thousand

---

## 8.7 The "Imagine if" opening

**MEDIUM**

**Banned** — "Imagine if you could…" · "What if you could…" · "Picture this:" · "Envision a world where…" · "Think about a future where…" · "Close your eyes and imagine…" · "Picture yourself…" · "Visualize a scenario where…"

Asking the reader to do imaginative work before you have given them a reason is an infomercial move. It also concedes that the real thing isn't compelling enough to state plainly.

**Instead** — a fact, a problem, or the solution stated directly. See [§8.1](#81-the-in-todays-world-opening) for the openings that work.

---

## 8.8 The "We believe" statement

**MEDIUM**

**Banned** — "We believe that…" · "Our philosophy is that…" · "We are committed to…" · "We are dedicated to…" · "We are passionate about…" · "We are driven / guided / inspired / motivated by…"

Framing a claim as belief weakens it and puts distance between the reader and the fact.

**Instead**

- State it: "Mobile security should be accessible to everyone."
- Better, demonstrate it: "Free for open-source projects."
- Best, make it concrete and personal: "We built this because we were tired of losing afternoons to manual APK review."

---

## 8.9 The "We are" opening

**LOW**

**Banned** — "We are a team of…" · "We are building…" · "We are a company that…" · "We are a platform that…" · "We are the leading / best / only…"

Users do not care what you are. They care what changes for them.

**Instead** — start with the user, the problem, or the outcome. "You need to know what's inside your APK" beats "We are a mobile analysis platform."

---

## 8.10 The "Our Mission" section

**LOW**

**Banned** — "Our Mission" / "Our Story" / "Our Values" / "Our Vision" sections on a product page · origin stories unrelated to the product · a "Why We Built This" longer than the feature descriptions.

**Instead** — thread the mission through the product narrative, prove it through actions ("free for open source", "here is our full methodology"), and if you must state it, keep it to one sentence. An About page is the right home for the rest.

---

## 8.11 The FAQ as crutch

**MEDIUM**

**Banned** — FAQs answering things the page should already answer ("What is this?") · questions nobody asks · more than 8 items on a landing page · answers that restate the main content · generated Q&A pairs.

**Instead**

- Answer the obvious questions where they arise — what it is in the hero, cost in pricing, how it works in features
- Reserve the FAQ for genuine objections and edge cases: "Does it support iOS?" · "Can I export reports?" · "Is my data stored?"
- 3–5 items maximum on a landing page
- Answer specifically: not "Yes, it's secure," but "Your APK is analyzed in memory and never written to disk. Transfers use TLS 1.3."
- Move anything larger into documentation

---

## 8.12 "Contact us" as a generic CTA

**LOW**

**Banned** — "Contact us to learn more" · "Get in touch" · "Reach out" · "Let's talk" · "Schedule a demo" on a self-serve product · "Talk to sales" when there is no sales team · "Request a quote" when pricing is public.

**Instead** — name the next action: "Analyze your first APK." Match the CTA to where the reader is: after features, "See it running"; after pricing, "Start free"; after proof, "Join them." If the product is self-serve, never route people through a human.

---

## 8.13 Newsletter signup as the default footer CTA

**LOW**

**Banned** — "Subscribe to our newsletter" with no value proposition · "Stay updated" · no stated frequency or content · newsletter as the primary CTA on a landing page.

**Instead** — be concrete about what arrives and how often: "A weekly digest of new Android vulnerabilities. Every Tuesday." Add proof if you have it. If the newsletter isn't worth someone's inbox, delete the form and give the space to the primary action.

---

## 8.14 Lorem Ipsum & placeholder copy

**CRITICAL**

**Banned** — "Lorem ipsum dolor sit amet" · "Your text here" · "Description goes here" · "Coming soon" · "TBD" · "Sample text" · fake names (John Doe, Jane Smith, Test User) · fake companies (Acme Corp, Example Inc) · fake emails and phone numbers in shipped UI · fake metrics · fake testimonials · fake ratings.

**Instead** — real copy for every element, including the ones nobody remembers: button labels, error messages, empty states, loading states, confirmation screens, email subject lines. If a section isn't ready, ship the page without it.

Fabricated metrics and reviews are not just slop. Invented testimonials and star ratings are consumer-protection violations in most jurisdictions, and platforms de-list for it.

---

## 8.15 Generic testimonials

**HIGH**

**Banned** — "This changed my life!" — John D. · "Amazing tool, highly recommended!" — Jane S. · anonymous praise · stock-photo faces · no company, no title, no specifics · testimonials that read like your own marketing copy · testimonials containing banned buzzwords · uniformly ecstatic quotes.

**Why this is slop**

A generic testimonial is worse than none. It reads as fabricated, and once a reader suspects one element is fake they discount everything around it.

**Instead**

- Real people, with permission — name, role, company, and a link
- **Specific**: "It found three unnecessary permissions in our production APK that we'd missed for months. That was a security incident we didn't have."
- With a number where possible: "Cut our review time from four hours to under a minute."
- **Believable, which means imperfect.** A quote containing a mild reservation ("the CLI took some getting used to") is far more persuasive than unqualified praise. Real people qualify things.
- If you have none yet, say nothing and lead with the product.

---

## 8.16 Case studies with no real data

**HIGH**

**Banned** — invented company names · no metrics · no timeline · no attributed quotes · before/after numbers that don't reconcile · no named contact · no link to the customer.

**Instead** — a real company (with written permission), real before-and-after numbers, a real timeline, and a quote from a named person. Tell the whole arc: the problem, what they tried, what changed, what it measured out to.

- BAD: "Company X increased efficiency by 50%."
- GOOD: "[Company]'s security team ran 200+ third-party APKs through it over six weeks. They found 47 issues and cut review time by 90%."

No case studies yet? Use testimonials. No testimonials? Use the product.

---

## 8.17 Blog posts as SEO filler

**MEDIUM**

**Banned** — "What is [keyword]?" posts that only define the keyword · "Top 10 [keyword] tools" with no real evaluation · "How to [keyword]" with no depth · "The future of [keyword]" with no original research · biased "[X] vs [Y]" comparisons · summaries of other people's posts · posts bylined "Team" with no human author · anything written to target a term rather than to say something.

**Why this matters now**

Search engines have gotten explicitly better at demoting mass-produced, low-value content, and volume-first content strategies increasingly carry ranking risk rather than ranking benefit. The economics that justified filler have largely inverted.

**Instead**

- Original research: "We analyzed 1,000 APKs. 73% request permissions they never use."
- Genuine insight: "Why most analysis tools miss runtime-requested permissions"
- Real problems solved end to end: "Audit your app's permissions in five minutes"
- Real stories: "How we found a credential leak in a banking app"
- A named human author with a real byline
- Nothing worth saying? Publish nothing. Quality beats cadence.

---

## 8.18 Press-release tone

**MEDIUM**

**Banned** — "We are thrilled to announce…" · "We are excited to unveil…" · "We are proud to introduce…" · "Today marks a significant milestone…" · "It is with great pleasure that we…" · "This groundbreaking innovation…" · "This revolutionary platform…"

Nobody is thrilled. Everybody knows nobody is thrilled.

**Instead** — announce like a person:

```text
BAD:  "We are thrilled to announce the launch of version 2.0."
GOOD: "Version 2.0 is out. Here's what changed."

BAD:  "We are proud to introduce our new feature."
GOOD: "You can now analyze iOS apps."
```

Lead with what the reader can now do, not with how the company feels about it.

---

## 8.19 Corporate speak

**HIGH**

Jargon that obscures rather than conveys — a fog machine for meaning.

**The curated blacklist.** These are genuinely empty phrases:

*Meeting and process theatre:* moving the needle · circle back · touch base · take this offline · double-click on that · drill down · level-set · socialize the idea · get alignment · sync up · loop in · action item · low-hanging fruit · quick win · boil the ocean · move the goalposts · peel the onion · open the kimono · run it up the flagpole · bandwidth (meaning time) · capacity (meaning time).

*Empty strategy language:* leverage our core competencies · optimize our value proposition · drive engagement · unlock synergies · align our vision · execute our mission · deliver value · create impact · foster growth · exceed expectations · push boundaries · think outside the box · best-in-class · world-class · industry-leading · turnkey solution · one-stop shop · end-to-end solution · 360-degree view · single pane of glass · holistic approach · paradigm shift · digital transformation (used vaguely) · disrupt the industry.

*Hollow verbs applied to people:* empower · enable · upskill · incentivize · operationalize · socialize · ideate · productize · solutionize · right-size (meaning lay off) · restructure (meaning lay off).

> **A correction to the source material.** An earlier draft of this list ran to roughly 800 entries and swept in ordinary technical vocabulary — Kubernetes, Docker, TLS, encryption at rest, logging, caching, CI/CD — alongside a long tail of generated filler ("randomness by design", "buttressing by design"). Those are not corporate speak. **Precise technical terms are the opposite of jargon**: they carry exact meaning to the audience that needs them. Writing "Kubernetes" to a platform engineer is clarity; writing "cloud-native orchestration paradigm" is fog. Ban the fog, keep the vocabulary.

**The real test**, better than any list: *could you say this sentence to a customer's face without embarrassment?* If not, it is corporate speak, whether or not it appears above.

**Instead** — plain words, specific nouns, active voice, short sentences, concrete examples.

```text
BAD:  "We leverage cutting-edge technology to deliver transformative security insights."
GOOD: "We found 12 permissions a banking app requests and never uses."
```

---

## 8.20 The overall generated tone

**CRITICAL**

The gestalt: formal, evenly structured, hedging, vague, and voiceless. Human-shaped and lifeless.

**Diagnostic checklist** — count how many apply to your draft:

- [ ] Every paragraph is roughly the same length
- [ ] Sentences cluster in the 18–24 word range
- [ ] Lists of three appear more than once
- [ ] Hedges throughout ("may", "can help", "designed to")
- [ ] Formal transitions ("Furthermore", "Moreover", "Additionally")
- [ ] Vague superlatives with no measurement behind them
- [ ] Passive voice in more than ~20% of sentences
- [ ] Zero contractions
- [ ] Zero fragments
- [ ] No opinion, no humor, no edge
- [ ] No specific numbers
- [ ] No named people or companies
- [ ] No stories or concrete examples
- [ ] Every section follows the same structure

**Three or more: rewrite. Six or more: start over.** Editing generated prose usually preserves its rhythm; rewriting from the specifics does not.

**The rewrite procedure**

1. **Extract the facts.** List every number, name, and checkable claim you actually have. If the list is short, the problem is research, not writing.
2. **Write the single most specific sentence you can** from that list. That is your lede.
3. **Build outward from it**, varying sentence length on purpose.
4. **Read it aloud.** Anywhere you stumble, or hear a metronome, rewrite.
5. **Cut 20%.** Whatever survives is stronger.

Then the three questions from the top of this module: could a competitor claim this sentence? Is there a checkable fact in it? Would the founder say it out loud?

---

## 8.21 Em-dashes in marketing copy

**CRITICAL for marketing copy** — with an important caveat

**Banned** — em-dashes in headlines, hero text, taglines, and slogans · in CTAs and button labels · manufacturing dramatic pauses · more than one per paragraph · anywhere a colon, period, or comma would do · in email subject lines and social posts.

**Why the ban**

Models insert em-dashes at a far higher rate than most writers, having learned the mark signals sophisticated flow. The result reads like a Victorian novel: "Our platform—built for developers—delivers insights—powerful, actionable insights—that transform your workflow." That is not sophistication. It is the written equivalent of pausing constantly to sound thoughtful.

**The caveat — this is a style rule, not a detector**

The claim that em-dashes *prove* AI authorship does not hold up, and acting on it has caused real harm: students and professional writers have been falsely accused, and detection tools disagree wildly on the same text. Essayists and heavy fiction readers use the mark constantly; AP-trained journalists avoid it. "More frequent than average" is not "reliable signal."

So ban it in marketing copy as **discipline**, because a period is usually the stronger choice in a headline — never as a **diagnosis** of who wrote something. The tell that actually works is cadence: see [§8.4](#84-uniform-paragraph-length--the-cadence-tell).

**Instead**

- Periods for breaks. Colons to introduce. Semicolons to join related clauses.
- En-dashes for ranges (`2024–2026`); hyphens for compounds.
- Restructure the sentence rather than reaching for the dash.
- In long-form, if you truly need one: at most one per 500 words, and never in marketing copy.

```text
BANNED: "Acme—your mobile analysis platform—delivers insights in seconds."
BANNED: "Analyze—decompile—inspect—any APK with one click."

GOOD:   "Acme delivers insights in seconds."
GOOD:   "Analyze, decompile, and inspect any APK with one click."
```

---

## Quick audit

```text
—             (em dash, in any marketing string)
"In today's"  "In recent years"  "In a world where"  "Now more than ever"
"It's not just"  "not just about"
"Imagine if"  "What if you could"  "Picture this"
"We believe"  "We are committed"  "We are passionate"  "We are a team"
"Our Mission"  "Our Story"  "Our Values"
"thrilled to announce"  "excited to unveil"  "proud to introduce"
"Trusted by thousands"  "world-class"  "industry-leading"  "best-in-class"
"the most secure"  "the most powerful"  "#1"
"Contact us to learn more"  "Get in touch"  "Subscribe to our newsletter"
"moving the needle"  "circle back"  "low-hanging fruit"  "empower"
Lorem ipsum  "John Doe"  "Acme"  "Coming soon"  "TBD"
```

Then run the cadence check, which no grep can do for you: paste the draft into a counter and look at the distribution of sentence lengths. A flat distribution is the tell.

---

## Sources & further reading

- [The Em-Dash Myth: What Actually Gives Away AI Writing](https://www.duey.ai/post/em-dash-ai-writing)
- [The Obvious Signs Someone Is Writing With AI Have Nothing to Do With Em-Dashes](https://medium.com/@allahverdiyev.tural/the-obvious-signs-someone-is-secretly-writing-with-ai-have-nothing-to-do-with-em-dashes-a89f3d99c577)
- [Em Dashes, Hyphens and Spotting AI Writing — Plagiarism Today](https://www.plagiarismtoday.com/2025/06/26/em-dashes-hyphens-and-spotting-ai-writing/)
- [AI Slop: The Definitive 2026 Guide (with Real Data)](https://www.sailop.com/blog/ai-slop-definitive-guide-2026)
- [AI Slop in 2026: The State of the AI-Generated Web](https://www.sailop.com/blog/ai-slop-2026-state-of-the-ai-generated-web)
