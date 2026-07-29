# 12 — Section-by-Section Rules

> **Module:** 12 of N · **Status:** stable
> **Read when:** building a specific page region and you want the concrete rules for it.

Modules 02–10 say what to avoid. Module 11 says what to add. This one is the working reference: per section, what to ban, what to do, and how to know it worked.

---

## Navigation

**Ban** — five-plus top-level links · a mega menu for a small product · hover-only dropdowns · the logo not linking home · a search icon that expands into nothing · a header taller than ~10% of a mobile viewport · a sticky header that hides content on scroll-up.

**Do** — three to five destinations maximum. One primary action, visually distinct. The logo links home. Dropdowns open on click as well as hover, close on Escape, and are arrow-key navigable. Current location is indicated by something other than color alone. On mobile, a real menu with focus trapping — not a `<details>` element pretending to be one.

**On sticky:** a header that is sticky on desktop does not have to be sticky on a phone. There it costs ~10% of the viewport permanently, and at the bottom of the page it sits across the footer — which reads as a broken overlay when the two have different backgrounds. If the footer carries the full navigation, a static header on mobile loses nothing and gives the content back its space.

**Done when** — a first-time visitor can name what the product does from the nav alone, and every item is reachable by keyboard in visual order.

---

## Hero

**Ban** — the centered badge → headline → subheadline → two-button stack · a headline over 10 words · two competing primary buttons · decorative visuals in place of real ones · everything crammed above the fold · a carousel.

**Do** — one message, one action, one real visual anchor. State what the product does in plain language. Put the CTA immediately after the claim it supports. Use a screenshot, terminal output, or real data as the anchor — or no image at all with strong typography. If a secondary action exists, make it a text link, not a second button.

Six structural alternatives are in [`05-layout-patterns.md` §5.2](05-layout-patterns.md#52-the-centered-badge--headline--subheadline--two-buttons-hero).

**Done when** — someone who reads only the headline and looks only at the anchor knows what this is and who it is for.

---

## Social proof

**Ban** — faded grayscale logo grids · "Trusted by 10,000+" with no basis · logos of companies that are not customers · avatar stacks with a "+12" · auto-scrolling marquees · fabricated testimonials · stock-photo faces.

**Do** — real logos at full opacity, with permission, linked to case studies where they exist. Or one specific, attributed testimonial that names an outcome. Or a metric you can defend and source. Include a mild reservation in testimonials where you have one — qualified praise reads as real, unqualified praise reads as written.

Place proof adjacent to the decision it supports: near the CTA, near pricing, near the feature it validates. Proof stranded at the bottom of the hero influences nothing.

**Done when** — every claim on screen could survive someone checking it.

**Which proof, for which audience:** see [`18-trust-signals.md`](18-trust-signals.md). A developer wants a code sample, a patient wants a licence number, a shopper wants the returns policy — and proof the audience does not accept is worse than none, because it occupies the slot where their answer should have been.

---

## Features

**Ban** — three identical icon cards · a 6–9 icon grid with equal weight · generic icons (shield, bolt, globe) · one-line descriptions that could describe anything · every feature given the same visual weight · "Learn more →" repeated identically.

**Do** — rank the features honestly. Give the one people buy for a large treatment with real evidence — a screenshot, a snippet, a number. Give supporting features less room. Write descriptions that name the specific thing: not "Secure", but "Flags permissions an app requests and never uses."

Interleave: feature, then proof of that feature. Vary the layout between features rather than repeating a grid cell.

**Done when** — a reader can tell which feature matters most without being told, and no description would fit a competitor unchanged.

---

## Pricing

**Ban** — "Most Popular" ribbons · three tiers by reflex · decoy tiers existing only to flatter another · hidden overage terms · "Contact sales" when the product is self-serve · fake scarcity or countdowns · annual pricing displayed as monthly without saying so.

**Do** — state the price in the largest text on the section. Say exactly what happens at the limits: what occurs when a plan is exceeded, how billing changes, how to cancel. If one plan genuinely suits most people, say so in words and only if true. Show annual and monthly clearly, with the real annual total. A comparison table beats tier cards once there are more than about six differentiating features.

Consider fewer tiers. One honest price converts better than three confusing ones.

**Done when** — a visitor can determine their exact monthly cost without contacting anyone, and knows what happens if they outgrow it.

---

## Testimonials & case studies

**Ban** — carousels · anonymous quotes · quotes with no company or role · uniformly ecstatic praise · quotes containing your own marketing vocabulary · fabricated metrics · case studies with invented companies.

**Do** — one to three testimonials, all visible at once, with real name, role, company, photo, and link. Specific claims with numbers. For case studies: the problem, what they tried before, what changed, and measured results with a real timeline and a named contact.

**Done when** — a skeptical reader could verify at least one claim in under a minute.

---

## FAQ

**Ban** — questions the page should already answer · more than 8 items · restating existing content · generated Q&A pairs · questions nobody asks · vague answers ("Yes, it's secure").

**Do** — three to five genuine objections and edge cases, answered specifically. "Your file is analyzed in memory and never written to disk. Transfers use TLS 1.3." Answer the hard questions honestly, including the ones with unfavorable answers — a candid "no, not yet" builds more trust than an evasion. Move anything longer into documentation.

**Done when** — every item answers a question a real prospect actually asked.

---

## Call to action

**Ban** — "Get Started" as the only label · "Contact us to learn more" · "Learn more" as the primary action · two equal-weight buttons · a CTA with no supporting context · the same CTA repeated verbatim in every section.

**Do** — name the action: "Analyze your first APK." One primary action per section, matched to where the reader is in the page. Remove friction and say so — "No signup required" or "Free for open source" does more than any button styling. Repeat the CTA down a long page, but vary the framing to match the preceding content.

**Done when** — the label alone tells the user what will happen when they click.

---

## Footer

**Ban** — the three-column Product/Company/Resources default · dumping every page · a newsletter form with no value proposition · dead social icons · a copyright year that has to be updated manually · legal links that are the only content.

**Do** — include only links that earn their place. Make the newsletter concrete about content and frequency, or remove it. Treat the footer as a last brand touchpoint: a terminal-styled footer for a developer tool, a live status indicator for infrastructure, recent writing for a content-led product. Generate the year. Link the status page, security policy, and changelog where they exist — those signal maturity more than any tagline.

**Done when** — the footer would look wrong on a competitor's site.

---

## Forms

**Ban** — placeholder-as-label · optional fields with no reason to exist · validation firing on every keystroke · error messages saying only "Invalid" · clearing input on failure · no `autocomplete` · CAPTCHAs on low-risk forms · a "Reset" button next to "Submit".

**Do** — a visible label on every field, correct `type` and `autocomplete`, and validation on blur and submit. Mark *optional* fields rather than required ones when most are required. Error text that says how to fix it, tied to its field, announced to assistive technology. Preserve everything the user typed. Show what happens next after submission.

Ask for the minimum. Every field costs completions.

**Done when** — the form is completable by keyboard alone, with autofill, and a failed submission loses nothing.

---

## Dashboards & data

**Ban** — every metric given equal weight · charts with no axis labels · rainbow categorical palettes · data with no time frame · percentages without denominators · exportless tables · no empty state for a new account · loading spinners that block the whole view.

**Do** — establish hierarchy: the one number that matters largest, supporting metrics smaller. Label axes, state the time range, and show the denominator. Encode meaning with position and length before color, and never with color alone. Use tabular numerals so values do not jitter as they update. Design the first-run empty state as an onboarding surface. Let sections load independently rather than blocking on the slowest query.

**Done when** — a user can answer "is this good or bad?" without asking anyone.

Chart-level rules — axes, palettes, dual axes, accessibility — are in [`19-data-visualisation.md`](19-data-visualisation.md).

---

## Empty, loading, and error states

**Ban** — "No data available" · a sad-face illustration · "Something went wrong" · infinite spinners · full-page blocking loads · errors with no recovery path · raw exception text.

**Do** — distinguish *nothing yet* (teach and offer the first action) from *nothing matched* (explain and offer to clear filters). Loading: skeletons matching the real layout for content, inline spinners for actions, nothing under 200 ms, and a delayed indicator for operations that are usually fast. Errors: what failed, why, what to do, a support code, and never lose the user's work.

**Done when** — every one of these states has copy someone actually wrote.

---

## Documentation

**Ban** — a wall of prose with no navigation · code samples that do not run · no copy button · undated content · "coming soon" pages · search that returns nothing useful · examples using placeholder credentials that look real.

**Do** — a task-oriented structure with working, copyable, tested examples. Show the smallest thing that works before the exhaustive reference. Date pages and state the version. Make search good — it is the primary navigation for docs. Include the failure cases, not only the happy path.

**Done when** — a new user can complete a first real task using only the docs.

---

## 404 and error pages

**Ban** — the default server page · "Page not found" alone · a joke with no way forward · a dead end with no navigation.

**Do** — say what happened, offer a search box, link the most likely destinations, and keep the site navigation present. Log 404s and fix the ones that recur — they usually indicate a broken link you own.

**Done when** — a user who lands here has an obvious next step.

---

## Sources & further reading

- [Auto-Forwarding Carousels and Accordions Annoy Users — Nielsen Norman Group](https://www.nngroup.com/articles/auto-forwarding/)
- [How Stripe, Linear, and Vercel Ship Premium UI](https://mantlr.com/blog/stripe-linear-vercel-premium-ui)
- [Designing Bento Grids That Actually Work: A 2026 Practical Guide](https://www.saasframe.io/blog/designing-bento-grids-that-actually-work-a-2026-practical-guide)
- [Core Web Vitals 2026: LCP, INP & CLS](https://www.corewebvitals.io/core-web-vitals)
