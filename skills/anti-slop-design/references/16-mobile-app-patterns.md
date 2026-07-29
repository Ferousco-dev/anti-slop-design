# 16 — Slop Taxonomy: Mobile App Patterns

> **Module:** 16 of N · **Status:** stable
> **Read when:** building or reviewing a native or cross-platform mobile app — iOS, Android, React Native, Flutter, Expo, SwiftUI, Compose.
> **Not here:** responsive web on a phone. That is a website, and modules 02–12 cover it. This module is about *apps*.

Everything in modules 02–12 still applies. What changes is that a phone app is not a small website: it has platform conventions users have already learned, a hand holding it, a battery, and an operating system with opinions.

Generated mobile UI fails in a specific way. Models have far more web training data than native, so they produce **a website wearing an app's clothes**: hover states on a touch device, a web navbar instead of a tab bar, a hamburger where a tab bar belongs, and desktop-sized touch targets. That is the through-line of this module.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 16.1 The same design on both platforms

**CRITICAL**

**Banned specifics**

- One identical interface shipped to iOS and Android with nothing changed
- Material's floating action button on iOS
- iOS-style back-chevron-and-title headers on Android, with no system back handling
- A navigation drawer on iOS where a tab bar belongs
- Android's overflow "kebab" menu on iOS, or iOS's action sheet idiom on Android
- Ignoring the Android hardware or gesture back
- One shared icon set drawn in the other platform's style

**Why this is slop**

Navigation is the single largest divergence between the two platforms, and it is the thing users have most deeply learned. iOS puts primary navigation in a bottom tab bar; Android historically favoured drawers and top tabs, and treats the FAB as the screen's primary action. Ship one to the other and the app feels subtly broken in a way users cannot name but do abandon.

Shipping identically to both is the single most common mistake in cross-platform work, and cross-platform tooling makes it easier, not harder.

**Instead**

- Share the *product*, diverge on the *idioms*: navigation, typography defaults, back behaviour, sheets, pickers, haptics, share sheets
- On iOS: SF Pro / SF Symbols, bottom tabs, swipe-back from the left edge, native action sheets
- On Android: system font / Material Symbols, respect the back gesture and predictive back, use Material sheets and dialogs
- If you genuinely want one custom design language everywhere, **make that a decision, funded and consistent** — a strong brand app (games, media, some fintech) can override conventions. Drifting into it because a component library only had one option is not the same thing.

---

## 16.2 Hover states on a touch device

**HIGH**

**Banned specifics**

- `:hover` carrying meaning anywhere in an app
- Tooltips that only appear on hover
- Content that reveals on hover
- No `:active` / pressed state, so a tap gives no feedback
- Web-sized tap targets under 44pt

**Why this is slop**

Hover does not exist on a phone. A design whose affordances live in hover has no affordances. Worse, the *pressed* state — the one that does matter — is usually the one missing, so taps feel dead.

**Instead**

- **Pressed state on everything tappable.** Immediate, under 100ms, visible: opacity, scale, or a background shift.
- **44×44pt minimum** on iOS; 48dp on Android. Measured on the *hit area*, not the glyph — a 20pt icon needs padding to reach it.
- Anything hover would have revealed becomes visible, or a tap, or a long-press with a discoverable hint.
- Haptics for consequential actions on iOS, used sparingly. Vibration for everything is worse than none.

---

## 16.3 Ignoring safe areas and the physical device

**CRITICAL**

**Banned specifics**

- Content under the notch, Dynamic Island, or status bar
- Buttons behind the home indicator or the gesture bar
- Interactive elements in the bottom ~34pt with no inset
- Hardcoded status-bar heights
- Ignoring the keyboard, so it covers the field being typed into
- No landscape handling on a form that people will rotate
- Assuming one screen size

**Why this is slop**

This is the most visible "made on a laptop" tell there is. A primary button sitting under the home indicator is unusable, and it takes one look on a real device to see.

**Instead** — safe-area insets on every screen edge, keyboard-avoiding scroll on any screen with an input, and test on the smallest supported device *and* the largest. A simulator at one size is not a test.

---

## 16.4 Reach: putting the primary action where the thumb isn't

**HIGH**

**Banned specifics**

- The primary action top-right, on a 6.7-inch phone
- Destructive and primary actions adjacent
- Critical controls in the top corners
- A bottom sheet whose confirm button is at the top

**Why this is slop**

Phones got tall. The top third of a large phone is a stretch or a two-handed operation, and the top-right corner is the worst spot on the device for a right-handed one-handed user. Web layouts put actions top-right because desktop pointers have no reach cost. Phones do.

**Instead** — primary actions in the bottom half, near where the thumb already is. Bottom sheets and bottom bars are not a trend; they are the reachable zone. Keep destructive actions physically distant from confirmations.

---

## 16.5 Navigation that fights the platform

**HIGH**

**Banned specifics**

- A hamburger drawer as the *primary* navigation on iOS
- More than five tabs in a tab bar
- Tabs that change between screens
- Losing scroll position and state when returning to a tab
- Deep links that dump the user at a root with no back path
- Modals stacked on modals
- A custom back button that does not match the system gesture

**Why this is slop**

A hamburger hides the app's structure behind a tap, which is why tab bars beat drawers for discoverability on phones. The drawer became a default because it scales to any number of items — which is a symptom of not having decided what matters.

**Instead** — three to five tabs, fixed for the life of the session, each preserving its own navigation stack and scroll position. Everything else lives inside a tab or in a settings screen. Support the system back gesture rather than reimplementing it.

---

## 16.6 First-run experience that asks before it gives

**HIGH**

**Banned specifics**

- A permission prompt before the user has seen anything
- Push-notification permission on launch
- Forced signup before any value is visible
- A five-screen carousel walkthrough nobody reads
- A paywall on screen one
- Asking for location, contacts or camera with no context

**Why this is slop**

An OS permission prompt is a one-shot resource: refused once, you usually cannot ask again, and asking cold is how you burn it. The tutorial carousel is the app-world equivalent of a splash screen — your onboarding is more important than their curiosity, which is never true.

**Instead**

- Let people use the app first. Ask for permission **at the moment it is needed**, with a sentence explaining the benefit, immediately before the system prompt.
- Teach in place with a first-run empty state rather than a carousel.
- If signup is genuinely required, say why in one line.

---

## 16.7 Motion that ignores the platform's physics

**MEDIUM**

**Banned specifics**

- Web easing curves and durations transplanted into an app
- Screen transitions that do not match the platform (a fade where iOS pushes)
- Animations that block interaction
- No transition at all between screens, so context is lost
- Ignoring the OS reduce-motion setting

Everything in [`07-animation-patterns.md`](07-animation-patterns.md) applies, plus: both platforms have a *documented* motion language, and users have internalised it. iOS pushes and dismisses with particular curves; Material has its own easing and duration tokens. Matching them makes an app feel native at no cost.

**Instead** — use the platform's native transitions unless you have a reason not to, keep interaction available during animation, and honour Reduce Motion / Remove Animations at the OS level, not just in-app.

---

## 16.8 Lists that fall over with real data

**HIGH**

**Banned specifics**

- Rendering a long list without virtualisation
- No skeleton or placeholder for the initial load
- No empty state
- No error state for a failed fetch
- Pull-to-refresh missing where users will reach for it
- Images loaded at full resolution into a list
- Nothing handling a slow or absent connection

**Why this is slop**

Mobile lists are the app. They are also where generated code is weakest: it renders ten mock items beautifully and stutters at a thousand. And a phone is the device most likely to be on a bad connection, so offline is a normal state, not an edge case.

**Instead** — virtualise anything unbounded, size and cache list images, and design the four states every list has: loading, populated, empty, failed. Add pull-to-refresh where the content is time-sensitive. Assume the network will drop mid-request.

---

## 16.9 Ignoring the system's own settings

**HIGH** — and an accessibility failure

**Banned specifics**

- Type that does not respond to Dynamic Type / font-size settings
- Layouts that break at the largest accessibility text sizes
- Hardcoded `px`/`pt` for all type
- Ignoring the OS dark-mode setting
- No VoiceOver / TalkBack labels on icon-only controls
- Custom controls with no accessibility traits
- Ignoring bold-text, increase-contrast and reduce-transparency settings

**Why this matters more on mobile**

Phones are where accessibility settings are actually used, heavily — larger text especially. An app that ignores the system text size is unusable for a large group of people who have already told the OS what they need.

**Instead** — scale with the platform's text APIs, test at the largest accessibility size and fix what breaks rather than clamping it, label every icon-only control, and follow the OS appearance setting rather than an in-app toggle alone.

---

## 16.10 Battery, data and heat

**MEDIUM**

**Banned specifics**

- Polling on a timer when a push or a socket would do
- Location updates at high accuracy continuously
- Animations looping forever on screen
- Full-resolution image downloads over cellular
- Background work with no batching
- Autoplaying video on a metered connection

Phones are thermally constrained and battery-limited, and the user can see which app drained them. Nothing here is visible in a screenshot and all of it is visible in Settings → Battery.

**Instead** — event-driven rather than polled, resolution matched to display size, work batched, infinite animation stopped when off-screen, and heavy transfers deferred to unmetered connections where the content allows.

---

## 16.11 App-store surfaces treated as an afterthought

**MEDIUM**

**Banned specifics**

- Screenshots that are raw simulator captures with no framing or context
- The same screenshot set for phone and tablet
- An icon with text in it, unreadable at 60px
- An icon that is a photograph, or a shrunken logo with a wordmark
- No dark-mode icon variant where the platform supports one
- A description written for the store algorithm rather than a person

**Why this is slop**

The icon and the first two screenshots are the entire conversion surface, and they are seen more often than any screen inside the app. An icon with a wordmark in it is illegible at the size it is actually rendered.

**Instead** — one simple, high-contrast mark that survives 60px; screenshots that show real content with a one-line caption each; per-device sets; and a first line of description that says what the app does.

---

## Quick audit

```text
:hover                    (in any app stylesheet)
onMouseEnter  onMouseOver
Dimensions.get('window')  (as a substitute for safe-area insets)
SafeAreaView              (absent from screens with edge content)
FlatList / LazyColumn     (absent where a list is unbounded)
ScrollView                (wrapping a long list instead of virtualising)
position: 'absolute', bottom: 0   (with no inset)
allowFontScaling={false}  (or any hard opt-out of Dynamic Type)
accessibilityLabel        (absent on icon-only controls)
setInterval               (polling where an event would do)
```

Then the checks no grep performs: run it on the smallest supported device, turn the system text size to maximum, turn on VoiceOver or TalkBack, and use it one-handed.

---

## Sources & further reading

- [iOS vs Android UI Design: 9 Key Differences (2026) — UXPin](https://www.uxpin.com/studio/blog/ios-vs-andoid-ui-design-for-mobile/)
- [Apple Human Interface Guidelines explained (2026)](https://www.nadcab.com/blog/apple-human-interface-guidelines-explained)
- [Material Design vs iOS Human Interface: complete comparison](https://freecardsort.com/comparisons/material-design-vs-ios-human-interface-complete-comparison)
- [iOS vs Android design guidelines: key differences](https://www.aaronmallen.com/2026/04/08/ios-vs-android-design-guidelines-key-differences-every-app-designer-should-know/)
- [iOS vs Android app UI design: the differences explained](https://arounda.agency/blog/ios-vs-android-app-ui-design-the-differences-explained)
