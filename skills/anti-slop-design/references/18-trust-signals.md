# 18 — Trust Signals by Category

> **Module:** 18 of N · **Status:** stable
> **Read when:** deciding what proof to put on a page, or when a design is clean, well-written, and still not converting.

Modules 06 and 12 treat social proof as one thing — logos, testimonials, numbers. It is not one thing. **Different audiences accept different evidence, and evidence the audience doesn't accept is worse than none**, because it occupies the position where proof should be and delivers nothing.

A developer wants a code sample. A patient wants a licence number. A shopper wants the returns policy. Give the developer a testimonial and you have said nothing to them.

---

## 1. Why the wrong proof is worse than no proof

Three reasons, and the third is the one people miss:

1. **It doesn't answer the question being asked.** The visitor has one dominant anxiety ([`15-product-types.md`](15-product-types.md) §5). Proof that addresses a different anxiety is noise.
2. **It occupies the slot.** A logo wall where a code sample belongs means the developer scrolls past the place their answer should have been.
3. **It signals you don't know your buyer.** A logo wall on a developer tool says *marketing people made this*, which is itself evidence — against you.

**The test:** name the visitor's dominant anxiety in one word, then ask whether each piece of proof on the page reduces *that* anxiety. Anything that doesn't, cut.

---

## 2. The proof ladder

Not all evidence is equal, regardless of category. Ranked by how hard it is to fake, which is the same as how much it is worth:

| Tier | Kind | Why it works |
|---|---|---|
| **1** | **Something the visitor can check right now** | Zero trust required. A live demo, a public URL, a search they can run, a repo they can read. |
| **2** | **A third party asserting it** | Independent. A named customer, an audit, a certification, a public status page, a review on a platform you don't control. |
| **3** | **A specific claim you make** | Checkable in principle. "2,437 users", "99.97% over 12 months", linked to a source. |
| **4** | **A vague claim you make** | Worthless. "Trusted by thousands", "industry-leading", "world-class". |
| **5** | **A fabricated claim** | Negative. Invented numbers, stock-photo testimonials, unlicensed logos. Costs more than silence and, for reviews and testimonials, is unlawful in most jurisdictions. |

**Spend your effort moving up, not adding more of the same tier.** One tier-1 asset beats ten tier-3 claims. If you only have tier 4, ship less and say so plainly — a stated absence reads as honesty; a vague claim reads as nothing.

---

## 3. What each audience actually accepts

### Developers and technical buyers

**Anxiety:** will this break, and will I be stuck?
**Accepts:** a working code sample on the landing page · a public repo with real commit activity · documentation that loads fast and is complete · a changelog · a public status page with real incident history · open GitHub issues answered by maintainers · self-hostable or exportable · a real free tier, not a trial.
**Rejects:** logo walls · testimonials · "enterprise-grade" · award badges · anything with a stock photo.
**Strongest single asset:** a snippet they can copy and run in under a minute.

### Enterprise and procurement

**Anxiety:** will this pass security review and survive an audit?
**Accepts:** SOC 2 / ISO 27001, named and dated · a DPA and sub-processor list · uptime SLA with the actual number · named reference customers in their industry and size band · a security page that answers questions rather than asserting "bank-grade" · data residency stated · a real support escalation path.
**Rejects:** consumer-style social proof · G2 badges alone · founder-led testimonials.
**Strongest single asset:** a security and compliance page that a security reviewer can complete their checklist from without emailing you.

### Consumers buying a physical product

**Anxiety:** what does it actually look like, and can I return it?
**Accepts:** many real photographs including unflattering angles · scale references · a returns policy stated in the buying flow, not the footer · reviews with photos, including the mediocre ones · real delivery estimates · stock status.
**Rejects:** studio-only imagery · uniformly five-star reviews · "as seen in" rows.
**Strongest single asset:** a returns policy so clear it removes the decision's risk.

### Patients and health consumers

**Anxiety:** is this safe and legitimate?
**Accepts:** named clinicians with verifiable registration numbers · the regulator and licence, stated · citations to actual literature · clear scope — what this is *not* for · privacy handling of health data in plain words · who to contact in an emergency.
**Rejects:** before-and-after imagery · testimonials as efficacy evidence · urgency of any kind · "doctor-approved" with no named doctor.
**Strongest single asset:** a named, checkable professional registration.
**Note:** health claims are regulated advertising in most jurisdictions. Check before writing, not after.

### People trusting you with money

**Anxiety:** can this disappear?
**Accepts:** the regulator and licence number · how client funds are held and whether they are segregated · deposit-protection scheme and limit · the full fee schedule, including the ones people forget · the legal entity name and address · security specifics rather than adjectives.
**Rejects:** growth numbers as safety evidence · "bank-grade security" · testimonials · anything that reads like marketing near a balance.
**Strongest single asset:** the licence number and what happens to your money if the company fails.

### Small-business buyers of services

**Anxiety:** will this person actually deliver, and can I afford to find out?
**Accepts:** case studies with before/after numbers and a named client · a low-risk entry offer · a specific niche stated plainly · the actual work, visible · clear pricing · honesty about who they are *not* for.
**Rejects:** broad positioning · "trusted by 500+ businesses" · stock team photos · long "our values" sections.
**Strongest single asset:** one case study with a real number and a real name.

### Students and course buyers

**Anxiety:** will I finish it, and will it change anything?
**Accepts:** a full syllabus visible before purchase · a free first module · honest time commitment · completion rates if you dare publish them · outcomes with methodology · a refund window with actual terms.
**Rejects:** income screenshots · countdown timers · "students get results" with no cohort data · lifestyle imagery.
**Strongest single asset:** the real curriculum, unlocked, before payment.

### Job seekers and candidates

**Anxiety:** what is it actually like to work here?
**Accepts:** salary range in the posting · the interview process written out with stages and timelines · real team members talking about real work · honest statements about what is hard · public engineering writing.
**Rejects:** office ping-pong photography · "we're like a family" · perks lists in place of substance.
**Strongest single asset:** the salary band, published.

### Donors and supporters

**Anxiety:** does the money reach the thing?
**Accepts:** a financial breakdown including overhead · specific outcomes per amount · independent charity registration · photography of actual work with consent · published annual reports.
**Rejects:** guilt mechanics · stock imagery of the people you claim to serve · vague impact language.
**Strongest single asset:** an honest overhead percentage, stated before anyone asks.

---

## 4. Placement: proof goes next to the doubt

Proof stranded in a dedicated section does nothing. The doubt happens at a specific moment, and that is where the evidence belongs.

| Doubt | Where the proof goes |
|---|---|
| "Does this even work?" | Beside the claim, in the hero |
| "Will it work for *me*?" | Beside the feature that matters to their case |
| "Is this worth the price?" | Inside the pricing section, not above it |
| "What if I hate it?" | Adjacent to the buy button — returns, trial, cancellation |
| "Are these people real?" | Beside the form, before submission |
| "What happens after I pay?" | On the confirm step, before confirming |

A testimonial section between the features and the footer is the default and the least useful arrangement. Break it up and move each piece next to what it answers.

---

## 5. When you have no proof yet

The honest options, in order:

1. **Sell the thinking.** A method explained well is evidence of competence. It is the only proof asset available on day one, and it is genuinely persuasive.
2. **Make the risk small.** A low-price entry offer, a real free tier, a trial with no card. Removing risk substitutes for proof.
3. **Show the work rather than results.** Your own artefacts — a repo, a design file, a live thing you built — prove capability without needing a customer.
4. **Publish an absence.** "No case studies yet, and here is why" reads as confidence. It also inoculates you: the visitor stops looking for what isn't there.
5. **Never invent.** Fabricated testimonials and reviews are unlawful in most markets, platforms de-list for it, and a single recognised fake discredits every true thing on the page.

---

## Quick audit

For every proof element on the page:

- [ ] Which anxiety does this reduce? Name it.
- [ ] Which tier is it? (Tier 4 → cut or upgrade. Tier 5 → remove immediately.)
- [ ] Is it adjacent to the doubt it answers, or parked in a section?
- [ ] Would this audience actually accept this *kind* of evidence?
- [ ] Could a sceptic verify at least one thing on this page in under a minute?

The last one is the whole module. If nothing on the page is checkable, you have written claims, not proof.

---

## Sources & further reading

- [Website Design and Credibility — Behavioral Design Academy](https://www.behavioraldesign.academy/resources/practices/website-design-and-credibility/)
- [The Impact of Website Design on Users' Trust Perceptions](https://link.springer.com/chapter/10.1007/978-3-030-51626-0_34)
- [Auto-Forwarding Carousels and Accordions Annoy Users — Nielsen Norman Group](https://www.nngroup.com/articles/auto-forwarding/)
