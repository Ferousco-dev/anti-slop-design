# 17 — App Screen Rules

> **Module:** 17 of N · **Status:** stable
> **Read when:** building a specific screen inside an app — onboarding, feed, detail, profile, settings, search, paywall, checkout, empty and error states.
> **Companion to** [`16-mobile-app-patterns.md`](16-mobile-app-patterns.md), which covers the platform-level failures. This is the per-screen working reference, the same shape as [`12-section-rules.md`](12-section-rules.md) is for web pages.

Format per screen: what to **ban**, what to **do**, and how you know it's **done**. Applies to native apps and to web apps that behave like apps — anything with sessions, state, and a signed-in user.

---

## Onboarding / first run

**Ban** — a five-screen value-proposition carousel · permission prompts before any value is shown · forced account creation before anything works · a paywall on screen one · progress dots with no way to skip · asking for a name you never use · a tour with tooltip overlays pointing at an empty interface.

**Do** — get the user to one real moment of value as fast as possible, then ask for things. Teach in place: a first-run empty state that shows what belongs there beats any walkthrough. If signup is genuinely required, say why in one line. Let people skip anything skippable, and remember that they did.

**Done when** — a new user reaches something useful without creating an account or granting a permission, and every prompt they *do* see arrives with a reason attached.

---

## Feed / list / home

**Ban** — no empty state · no error state · no loading state · unvirtualised long lists · pull-to-refresh missing where content is time-sensitive · infinite scroll with no way to reach anything below it · losing scroll position on return · full-resolution images in rows · ranking that hides the thing the user came for.

**Do** — design all four states before the populated one: **loading, populated, empty, failed**. Virtualise anything unbounded. Cache and size row images. Preserve scroll position and state per tab. Make the refresh gesture available where freshness matters, and make it honest — if nothing changed, say so rather than animating for a second.

**Done when** — it holds up at zero items, one item, and ten thousand, on a bad connection, and returning to it feels like returning rather than reloading.

---

## Detail screen

**Ban** — the primary action above the fold on a long screen and nowhere else · back navigation that loses the list position · no handling for content that has been deleted since the list loaded · truncation with no way to expand · a share sheet that shares the wrong URL · images that cannot be zoomed where detail matters.

**Do** — one clear primary action, reachable in the thumb zone, repeated at the end of long content. Preserve the parent's scroll position on back. Handle the deleted case explicitly. Make the share target a real deep link that opens this screen.

**Done when** — a deep link into this screen from cold start puts the user somewhere sensible with a working way back.

---

## Search

**Ban** — a search field that does nothing until submit, with no indication · no recent or suggested queries on focus · no empty-result state · no way to clear the field · results that reflow as you type so you tap the wrong one · filters that reset on back · no handling for a typo.

**Do** — show recent and popular queries on focus so an empty search field is still useful. Debounce, don't thrash. Keep result rows stable while typing. Write a real no-results state that suggests what to try, and offer a way to clear filters. Handle near-misses.

**Done when** — the field is useful before a single character is typed, and a misspelling still finds the thing.

---

## Profile / account

**Ban** — an avatar upload with no crop and no size limit · a display name field with no length constraint that then breaks every layout · no way to see what other people see · destructive account actions adjacent to routine ones · "delete account" that only opens a support email.

**Do** — treat the longest realistic name as the design case, not the shortest. Give people a view of their own public profile. Put account deletion in the app, reachable, with a clear explanation of what is removed and what is kept — this is a legal requirement in several jurisdictions and both app stores have rules about it.

**Done when** — a user can find, understand, and complete account deletion without contacting anyone.

---

## Settings

**Ban** — a flat list of thirty toggles · toggle labels that do not say what "on" means · settings that apply on next launch with no indication · no search in a long settings screen · burying notification controls · a theme toggle that ignores the OS setting entirely.

**Do** — group by what the user is trying to change, not by which team built it. Label toggles so the state is unambiguous — "Email notifications" tells you nothing; "Email me about replies" tells you everything. Apply immediately or say when it applies. Follow the OS appearance and text-size settings by default, with an override rather than a replacement.

**Done when** — someone can find the setting they came for in under ten seconds without reading every row.

---

## Notifications & permissions

**Ban** — asking on launch · asking with no context · a custom pre-prompt that is more aggressive than the system one · treating a refusal as a state to nag about · notifications that all use the same channel · no in-app way to change what was granted.

**Do** — ask at the moment of need, with one sentence on the benefit, immediately before the system prompt. Accept a refusal and keep working. Use separate categories so a user can mute one thing without muting everything. Link to the OS settings for anything you cannot change in-app.

**Done when** — a user who refuses every permission can still use the core of the app.

---

## Paywall / upgrade

**Ban** — a paywall before any value · fake countdown timers · a hidden or greyed-out close button · "cancel anytime" without saying how · the annual price shown as a monthly number without labelling it · pre-selecting the most expensive plan without saying it is selected · no restore-purchases option · obscuring the total charged today.

**Do** — state the exact amount charged today, the renewal amount, and the renewal date. Make the close affordance obvious and immediately tappable. Say plainly what free keeps. Offer restore purchases where the platform requires it. If there is a trial, say what happens when it ends before the user commits.

**Done when** — the user can state, unprompted, what they will be charged and when. Anything less is a dark pattern, and both stores reject for it.

---

## Checkout / payment

**Ban** — surprise fees at the last step · a total that changes after address entry with no warning · no order summary before confirm · a single-field card input with no formatting or validation · losing the cart on session expiry · no confirmation screen or receipt · a confirm button that can be double-tapped into two charges.

**Do** — show the true total as early as it is knowable, and flag anything still to be added. Summarise before confirming. Use the platform's payment sheet where available — it is faster, safer, and better tested than your form. Make the confirm action idempotent. Send a receipt and show one.

**Done when** — nothing about the amount charged is a surprise, and a double tap cannot double-charge.

---

## Forms inside an app

**Ban** — placeholder as label · wrong keyboard type per field · no `autocomplete`/`textContentType` · validating on every keystroke · errors that clear the field · a submit button that doesn't disable while in flight · a form longer than the screen with no progress indication · no way to save and return.

**Do** — visible labels, correct keyboards, platform autofill wired up. Validate on blur and submit. Keep what was typed on failure, always. Disable and mark the submit as busy. For anything long, break it into steps with visible progress and save partial state.

**Done when** — the form survives an interruption — a phone call, a backgrounded app — without losing input.

---

## Empty states

**Ban** — "No data" · a sad-face illustration · an empty state that does not distinguish *nothing yet* from *nothing matched* · no action · a blank screen while the real emptiness is a failed request.

**Do** — treat first-run empty as the primary onboarding surface, because it usually is. Say what belongs here and give the one action that creates it. For filtered-empty, name the filter and offer to clear it. Never confuse empty with broken.

**Done when** — a brand-new user understands what the screen is for without a tutorial.

---

## Error & offline

**Ban** — "Something went wrong" · a raw status code · an alert with only "OK" · a permanent spinner on failure · silent failure · treating offline as an error rather than a state · losing user input on a failed request.

**Do** — say what failed, why if you know, and what to do next. Offer retry. Distinguish *no connection* from *server error* from *this item is gone* — they need different words and different actions. Queue what you can and reconcile when connectivity returns. Never discard input.

**Done when** — a user in a lift with no signal can tell the difference between your app being broken and their connection being gone.

---

## Quick audit

```text
requestPermission        (called at launch or on mount)
AsyncStorage / SharedPreferences   (with no migration path)
onChangeText + validate  (validating on every keystroke)
"Something went wrong"   "No data"   "Error"
paywall / subscribe      (rendered before any value screen)
placeholder=             (in place of a label)
keyboardType             (absent on email, phone or numeric fields)
ScrollView               (wrapping an unbounded list)
```

Then the checks no grep performs: complete the core task with every permission refused, put the device in airplane mode mid-request, and try to delete your own account.

---

## Sources & further reading

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design 3](https://m3.material.io/)
- [Auto-Forwarding Carousels and Accordions Annoy Users — Nielsen Norman Group](https://www.nngroup.com/articles/auto-forwarding/)
- [iOS vs Android UI Design: 9 Key Differences — UXPin](https://www.uxpin.com/studio/blog/ios-vs-andoid-ui-design-for-mobile/)
