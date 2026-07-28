# 06 — Slop Taxonomy: Component & UI Element Patterns

> **Module:** 6 of N · **Status:** stable
> **Read when:** building or reviewing any component — cards, pricing, forms, social proof, feedback, loading, empty and error states.

Components are the building blocks. When the components are generic, the whole interface is generic regardless of how good the page structure is.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md): **CRITICAL** = automatic fail · **HIGH** = regenerate unless defensible · **MEDIUM** = justify or replace · **LOW** = question the default.

---

## 6.1 The SaaS triad — three identical feature cards

**CRITICAL**

```text
+---------+  +---------+  +---------+
|  icon   |  |  icon   |  |  icon   |
| Secure  |  |  Fast   |  | Global  |
| desc…   |  | desc…   |  | desc…   |
| Learn → |  | Learn → |  | Learn → |
+---------+  +---------+  +---------+
```

**Why this is slop**

Users have developed card blindness for it. The brain registers "template" and skips the content entirely — so the features never get read, however good they are.

It also fails structurally: equal visual weight for unequal features, generic icons that communicate nothing, identical sizes that prevent emphasis, predictable hover (a 2px lift and a shadow), and "Learn more" links that rarely lead anywhere worth going.

**Instead**

1. **Break the count.** Two cards, or four, or an editorial run. Three-in-a-row is the tell.
2. **Vary size to encode importance.** One large card for the feature people actually buy for; smaller cards for the rest.
3. **Replace icons with evidence.** A screenshot for one, a code snippet for the next, a real chart for the third.
4. **Interleave with full-width content** — card, then a testimonial that validates it, then a card.
5. **Write specific descriptions.**
   - BAD: "Secure — Your data is safe with us."
   - GOOD: "Permission mapping — every permission an APK requests, including the dangerous ones it doesn't disclose."
6. **Consider removing cards entirely.** A heading, a paragraph, and a rule between sections often reads better than three boxes.

---

## 6.2 Cookie-cutter card layouts

**HIGH**

Every card following `icon → heading → description → link`, centered, identical.

**Why this is slop**

The template treats all content as the same shape. It is not. Some content needs an image, some needs a number, some needs a quote, some needs to be interactive. Forcing one template throws away the ability to communicate difference.

**Instead**

- **Vary what's inside** — images, data, quotes, interactive elements
- **Vary size within one section** — one large, two medium, three small
- **Drop cards for grouping by spacing, rules, and type hierarchy**
- **Add real interactivity** where it earns its place — expand in place, hover reveal, progressive detail
- **Use real visuals** — screenshots instead of icons, charts instead of adjectives, user quotes instead of generic copy

Whatever you build, design all its states — default, hover, focus, active, disabled, loading, empty, error. Shipping only the default state is the single most common component failure.

---

## 6.3 Pricing cards with a "Most Popular" ribbon

**HIGH**

Three tiers, middle one highlighted with a colored border and a badge.

**Why this is slop**

The ribbon is a nudge dressed as information. It pushes users toward the middle tier regardless of fit, and it is transparent enough that users discount it — so it manipulates without even working. Regulators in several jurisdictions now treat manufactured urgency and false-popularity signals as deceptive design.

The three-tier model is itself a template. Not every product needs three. Some need one.

**Instead**

1. **A comparison table** for genuinely complex pricing — feature by feature, no badge, let people decide.
2. **Signal a recommendation through design, not a sticker** — slightly larger, a subtle background shift. If it truly is the most common plan, say so factually and only if true.
3. **Consider one tier.** One price, all features. Simple and honest converts.
4. **Editorial pricing** — a headline, a checklist, one CTA, no grid at all.
5. **Usage-based pricing** where it fits: "$0.01 per analysis. First 100 free."
6. **If you use tiers, give each a distinct audience** — individuals, teams, organizations — and make the boundary obvious. A tier that exists only to make another look reasonable is a dark pattern.

Always show what happens at the limits: what occurs when a plan is exceeded, how billing changes, and how to cancel. Hiding that is a slop pattern with legal consequences.

---

## 6.4 Avatar stacks with a "+12" overflow circle

**MEDIUM**

```text
[👤][👤][👤][👤][+12]
Trusted by 10,000+ developers
```

**Why this is slop**

Borrowed from Slack and Discord, where the stack is functional — it shows who is actually present. On a landing page it is decoration. The overflow count is usually invented, the avatars are usually stock, and the headline number is usually rounded past the point of meaning.

**Instead**

- **One real testimonial** with a real photo, name, role, and company, saying something specific: "It found three unnecessary permissions in our production APK that we'd missed for months."
- **Actual metrics**, only if true and checkable
- **A real logo grid** with permission, at full opacity, linked to case studies
- **A screenshot of a genuinely active community** — more convincing than any avatar row
- **If you have no social proof yet, don't fake it.** Lead with the value proposition and build proof first.

---

## 6.5 Newsletter inputs with an arrow button inside

**MEDIUM**

```text
[Enter your email        →]
```

**Why this is slop**

Copied from mobile search UI, where the constraint justifies it. On desktop the circular arrow is ambiguous — users cannot tell whether it is a button or an ornament — and it gives the action no name.

**Instead**

- A labeled button beside the field: `[Enter your email] [Subscribe]`
- A value proposition above it: "Weekly APK security reports"
- Clear inline feedback on success and failure, not a toast that vanishes
- A real `<label>`, not placeholder-as-label — placeholders disappear on focus and are invisible to some assistive tech
- If the newsletter is not worth subscribing to, remove it and give the space to the primary CTA

---

## 6.6 Generic cookie consent banners

**LOW** — but a legal surface, so get it right

```text
[We use cookies to enhance your experience.]   [Decline] [Accept]
```

**Why this is slop**

Designed for compliance rather than people: vague language ("enhance your experience"), a binary with no explanation, and content blocked behind it. Where consent is legally required, a design that makes rejection harder than acceptance is not merely slop — it is non-compliant in several jurisdictions.

**Instead**

- Brand it: your colors, your type, your voice
- Say what the cookies actually do: "We use analytics cookies to see which features get used."
- **Make reject as easy as accept** — same prominence, same click count
- Do not block content; do not use a scrim that traps keyboard focus
- Offer a preference centre that is reachable again later, and honour the choice

---

## 6.7 The chat bubble in the bottom-right corner

**LOW**

Appropriate for e-commerce and staffed support. Slop when it appears on every page, auto-opens over content, is unbranded, is unstaffed, or competes with the primary CTA.

**Instead** — a branded, clearly labeled help affordance; a link to docs or a support address where that is the honest answer; opt-in rather than auto-open; presence only on pages where support is the likely need. If you cannot staff it, remove it — an unanswered chat widget damages trust more than no widget.

Whatever you ship must be dismissible and must never cover a control or the footer.

---

## 6.8 Testimonial carousels & auto-scrolling logo marquees

**HIGH**

**Why this is slop**

This one is not a matter of taste — it is one of the best-evidenced findings in usability research. Nielsen Norman Group has documented banner blindness across three decades and found that auto-forwarding carousels annoy users and *reduce* the visibility of the content inside them. Interaction rates are close to zero: roughly 1% of visitors engage with the first slide, and well under half a percent reach any slide after it.

Auto-rotation also actively harms: content disappears mid-read, breaking reading flow and causing missed information. And an auto-advancing carousel violates the user's motion preferences unless explicitly guarded.

**Instead**

1. **Show one or two testimonials prominently**, with real photo, name, role, and company
2. **A static logo grid** — everything visible at once, full opacity, properly spaced
3. **A grid of testimonials** if you have many — 2×2 or 3×2, all visible
4. **A dedicated testimonials or case-study page** with long-form quotes and real metrics, linked from the landing page

If you keep a carousel: never auto-advance, expose real controls, make it keyboard-operable, and pause on hover and focus.

---

## 6.9 Fake dashboard mockups in the hero

**HIGH**

Fully covered in [`02-visual-patterns.md` §2.1.12](02-visual-patterns.md#2112-the-tilted-dashboard-mockup-in-the-hero). Summary: no tilted browser frames, no invented data, no perfect symmetrical charts.

The component-level addition worth stating: **fake dashboards are dishonest, not just tired.** They show idealized data the real product will not produce, setting an expectation the first session immediately breaks. Show the real screen, or show terminal output, or show nothing and let typography carry the hero.

```text
$ appmd analyze app.apk
✓ Manifest parsed
✓ 23 permissions found
✓ 12 libraries detected
✓ 3 vulnerabilities identified
Analysis complete in 28.4s
```

Real output beats a rendered mockup, and it costs less to build.

---

## 6.10 Left-border accent cards

**MEDIUM**

Fully covered in [`02-visual-patterns.md` §2.1.13](02-visual-patterns.md#2113-the-left-border-accent-card). Use top borders, bottom borders, background shifts, or spacing instead. Keep the left-border accent for genuine alert semantics — and pair it with an icon and text so color is never the only signal.

---

## 6.11 Toggle switches for non-binary choices

**LOW**

A toggle means *on or off, applied immediately*. It is the wrong control for mode selection.

**Banned** — toggles for monthly/annual pricing, light/dark mode, category filters, show-more/less.

**Instead** — tabs or a segmented control for mode selection; radio buttons for mutually exclusive options; a button group for two peers. Reserve toggles for true settings, and make sure the label states what "on" means — a toggle labeled only "Notifications" tells the user nothing about its current state.

---

## 6.12 Skeleton screens as the default loading state

**LOW**

**Banned** — skeletons for a button click or form submit; skeletons whose shape does not match the content that replaces them; skeletons that flash for under ~200 ms.

**Instead** — skeletons for content-heavy surfaces with a known layout (dashboards, feeds, lists); an inline spinner for simple actions; a progress indicator for multi-step work; **nothing at all under 200 ms** — adding a loading state to an instant operation makes it feel slower.

A skeleton whose layout does not match the final content causes a visible jump. That is worse than no skeleton.

---

## 6.13 A loading spinner for everything

**LOW**

**Banned** — a generic spinner for operations over ~3 seconds; a spinner with no explanation; a spinner blocking the whole page; a spinner where real progress is knowable.

**Instead** — progress bars where progress is measurable; skeletons for content; text that says what is happening ("Scanning libraries…"); percentages for multi-step work. Announce state changes to assistive technology with a polite live region, or a screen reader user learns nothing happened.

---

## 6.14 A toast for every action

**LOW**

**Banned** — toasts on every click or field completion; toasts on navigation; stacks of simultaneous toasts; auto-dismiss so fast the message cannot be read.

**Instead** — toasts for outcomes that matter and are not otherwise visible; inline feedback for form validation, next to the field; one toast at a time. Give at least ~5 seconds, pause the timer on hover and focus, and make anything actionable persist until dismissed. A toast carrying an error the user must act on should not disappear on a timer at all.

---

## 6.15 A tooltip for everything

**LOW**

**Banned** — tooltips on every icon; tooltip text that repeats a visible label; hover-only tooltips on touch devices; tooltips that cover the thing they describe; paragraphs inside a tooltip.

**Instead** — tooltips for icon-only controls and genuinely non-obvious features; visible labels wherever space allows; 1–2 sentences maximum. Tooltips must be reachable by keyboard, dismissible with Escape, and stay visible long enough to move the pointer into them. Never put essential information *only* in a tooltip.

---

## 6.16 A badge for everything

**LOW**

**Banned** — badges on every feature and nav item; multiple badges on one element; "NEW" badges that never expire.

**Instead** — one or two per page at most; a defined expiry (30 days for "NEW"); badges only for genuine status changes. A changelog does this job better and permanently. And a badge that encodes meaning by color alone fails for color-blind users — include the word.

---

## 6.17 Progress bars for non-linear processes

**LOW**

**Banned** — fake progress during an "Analyzing…" step; bars that jump backwards; bars that stall at 99%; determinate bars for unknown durations.

**Instead** — an indeterminate indicator when duration is genuinely unknown; step indicators for discrete stages; honest status text that changes as work moves ("Parsing manifest…" → "Scanning libraries…"). Be honest about uncertainty — a stalled 99% costs more trust than an indeterminate spinner ever does.

---

## 6.18 Step indicators for simple processes

**LOW**

**Banned** — step indicators for two steps or a single action; indicators that do not update; more than ~5 steps in one flow.

**Instead** — step indicators for genuine multi-step forms (3+); a simple label for two-step flows; inline guidance for single actions. Show which step is current, which are complete, and let users move backwards without losing input.

---

## 6.19 Empty states with a generic illustration

**LOW** — and a large missed opportunity

**Banned** — "Nothing here yet" with a sad face; "No data available" with no guidance; a generic empty-box illustration; an empty state with no action.

**Why this matters more than its severity suggests**

The empty state is often a user's *first* screen. It is the highest-leverage teaching moment in the product, and the default treats it as an error message.

**Instead**

- Say what belongs here and how to create it: "You haven't analyzed any APKs yet. Upload one to get started."
- Distinguish the two kinds: **nothing yet** (onboard them) versus **nothing matched** (help them recover — "No results for that filter. Clear filters.")
- Include one clear action
- Consider seeding a demo or sample so the interface can be understood before the user has data

---

## 6.20 Error states with a generic message

**LOW** — and a trust-critical touchpoint

**Banned** — "Something went wrong" · "An error occurred" · "Oops!" · a bare "Error 500" · any error with no recovery path or explanation.

**Why this matters**

Errors are where users decide whether to trust you. A vague error says you either did not know what failed or did not think they deserved to be told. Both are worse than the failure.

**Instead**

- **Be specific:** "We couldn't analyze this APK. The file may be corrupted or password-protected."
- **Offer a recovery action:** "Try a different file" or a link to support
- **Give context** where it helps: "This usually happens when the APK is signed with a v1-only signature."
- **Use human language** without being cute — nobody wants a joke when they are blocked
- **Include a support code** ("APK-001") so a report is actionable
- **Never blame the user,** and never lose their input on failure

Errors must be announced to assistive technology, associated with the field that caused them, and never conveyed by red border alone.

---

## Quick audit

```text
grid-cols-3           (three identical cards)
"Most Popular"        "Recommended"     "Best Value"
"Learn more →"        (repeated identically across cards)
+12   avatar-stack    "Trusted by 10,000+"
carousel   swiper   slick   marquee   autoplay
animate-pulse         (skeleton for a sub-200ms action)
toast(                (fired on a trivial action)
"Something went wrong"   "An error occurred"   "Oops"
"Nothing here yet"       "No data available"
placeholder=            (used in place of a <label>)
```

Then check the state coverage: for each interactive component, did you design hover, focus, active, disabled, loading, empty, and error — or only the default?

---

## Sources & further reading

- [Auto-Forwarding Carousels and Accordions Annoy Users and Reduce Visibility — Nielsen Norman Group](https://www.nngroup.com/articles/auto-forwarding/)
- [Banner blindness — overview and research history](https://en.wikipedia.org/wiki/Banner_blindness)
- [Why Website Carousels Harm UX, Conversions, and Accessibility](https://bhirst.media/why-website-carousels-harm-ux/)
- [WCAG Compliance & Rethinking the Carousel Trend](https://www.mandr-group.com/internet-rethinking-carousel-trend/)
- [How to Use Image Carousels the Right Way — VWO](https://vwo.com/blog/image-slider-alternatives/)
