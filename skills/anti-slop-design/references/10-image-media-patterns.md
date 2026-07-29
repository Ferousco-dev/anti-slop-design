# 10 — Slop Taxonomy: Image & Media Patterns

> **Module:** 10 of N · **Status:** stable
> **Read when:** choosing or generating photography, illustration, icons, screenshots, video, or any visual asset.

Imagery is where slop is most immediately legible to a visitor. A single stock photo of diverse colleagues laughing at a laptop undoes an otherwise careful page in under a second — because the reader has seen that exact photo on four other sites.

Technical delivery (formats, sizing, lazy loading, CLS) lives in [`09-code-patterns.md` §9.6](09-code-patterns.md#96-images-that-break-performance). This module is about *what the image is*.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 10.1 Generic stock photography

**CRITICAL**

**Banned specifics**

- Diverse colleagues laughing around a laptop
- The handshake
- A person pointing at a whiteboard covered in meaningless diagrams
- Someone gazing thoughtfully out of a floor-to-ceiling window
- Hands typing on a backlit keyboard, shot from above
- A headset-wearing "support agent" smiling at nothing
- Aerial city timelapses used as generic "scale"
- Anonymous hoodie-and-code imagery for anything security-related
- Any photo whose caption could be "business"

**Why this is slop**

Stock photography communicates one thing reliably: *we had a space to fill.* It says nothing about the product, and readers have learned to skip it entirely. Worse, the same images recur across unrelated brands — a visitor may literally have seen your hero photo on a competitor's site.

**Instead**

- **Show the product.** A real screenshot outperforms any photograph of a person near a computer.
- **Show real output** — a terminal session, a generated report, an actual chart with actual numbers.
- **Show the real team**, if people matter to the story. Imperfect real photos beat polished fake ones.
- **Show real customers** doing the real work, with permission.
- **Show nothing.** Whitespace and strong typography beat a filler image every time. An empty area is not a problem to solve.

---

## 10.2 Obvious AI-generated imagery

**CRITICAL**

**Banned specifics**

- Generated "photographs" of people used as customers, team members, or testimonial faces
- Generated hero illustrations with the smooth, over-lit, plastic look
- Generated product images where reflections and lighting do not agree
- Any generated image with visible artifacts: extra or missing fingers, smeared text or logos, melted jewelry, inconsistent shadows
- Generated screenshots of a UI that does not exist
- The same generated "person" reused across pages with different names

**Why this is slop — and why it's getting more expensive**

Consumer awareness of AI imagery has risen sharply, and the reaction is not neutral. Survey work puts consumer concern about AI image use around 95%, with deception (~71%) and inauthenticity (~65%) as the leading objections. Brands using obvious AI lifestyle imagery see measurable conversion drops on product pages.

The tells are consistent: generated images lack the physical imperfections of real capture — luminance-dependent sensor noise, natural compression artifacts, real lens characteristics, coherent metadata. People cannot always name what is wrong, but they register it.

There is also a disclosure dimension. Several platforms now require AI content to be labeled, and presenting a generated person as a real customer is a straightforward misrepresentation.

**Instead**

- **Never** generate a human being and present them as real. Not a customer, not a team member, not a testimonial face. This is the hard line.
- Use generated imagery, if at all, for **openly abstract or illustrative** work where nothing is claimed to be real — and hold it to the same taste standard as everything else.
- Prefer real photography, real screenshots, or commissioned illustration.
- If you use AI assets, disclose where the platform or the context requires it.

---

## 10.3 Generic vector illustration ("Corporate Memphis" and successors)

**HIGH**

**Banned specifics**

- Flat people with disproportionate limbs and no faces, in a two-tone brand palette
- Isometric scenes of abstract "workflow" that depict nothing
- Floating UI fragments arranged around a smiling figure
- Illustration packs used unmodified, so your site shares art with hundreds of others
- Illustration whose subject is "technology" in the abstract
- Mixed illustration styles on the same page

**Why this is slop**

The flat-illustration style became the default because it was cheap, scalable, and inoffensive — the same forces that produced the purple gradient. An unmodified illustration pack is a stock photo with more steps.

**Instead** — commission illustration with a specific point of view if illustration suits the brand; use diagrams that actually explain the system; or show the product instead. If you must use a pack, restyle it into your palette and use it consistently, never mixed with other styles.

---

## 10.4 Icons that carry no information

**HIGH**

**Banned specifics**

- A shield for "security", a lightning bolt for "speed", a globe for "global", a gear for "settings" as the entire visual vocabulary
- Icons from multiple sets on one page — mismatched stroke widths, corner radii, and grids
- Emoji used as interface iconography
- Icons at inconsistent optical sizes
- Icon-only controls with no accessible name
- Decorative icons announced to screen readers

**Why this is slop**

A shield could belong to any product on earth. Generic icons occupy the position where information should be and deliver none — they are visual filler that looks like communication.

Mixing icon sets is subtler but reads as carelessness: a 1.5px-stroke Lucide icon next to a filled Font Awesome glyph looks wrong even to people who cannot say why.

**Instead**

- **One icon set**, consistently, at a consistent optical size and stroke weight
- Icons that identify a specific thing (a file type, a platform, a state), not an abstract quality
- **Labels beside icons** wherever space allows — icon-only navigation is guesswork
- Icon-only controls get an accessible name: `aria-label` or visually-hidden text
- Decorative icons get `aria-hidden="true"` so they are not announced
- Never emoji as iconography — they render differently on every platform and are announced verbosely by screen readers

---

## 10.4b Brand marks set as Unicode characters

**HIGH**

**Banned specifics**

- A logo, monogram or wordmark rendered as a text character rather than an asset
- Non-Latin script (Arabic, Devanagari, CJK, Cyrillic) typed into a Latin-only font stack
- Currency symbols, arrows, mathematical operators or dingbats assumed to exist in the loaded face
- Assuming a glyph is safe because it renders on the machine you built it on

**Why this is slop**

A character is only as reliable as the font that has to draw it. Set `ن` in a `Helvetica Neue, Arial` stack and iOS has no Arabic glyph at that weight, so it renders as **tofu** — an empty box where the brand mark should be. On the developer's machine, with a fuller font library, it looks perfect.

The failure is invisible in review and visible to exactly the audience the mark matters to. And it is worst where it hurts most: a mark set large as a background flourish becomes a large empty box.

**Instead**

- **Logos and marks ship as assets** — SVG for line art, PNG with alpha for raster. They are brand, not text.
- If a non-Latin glyph genuinely belongs in running text, load a font that covers the script and declare `lang` so the right face and shaping are used
- Use a subsetted webfont with an explicit `unicode-range` rather than trusting the system stack
- Test on the actual platforms, not just the build machine — glyph coverage varies most between macOS, iOS, Windows and Android

**The check:** view the page on a device that is not yours. A missing glyph is a box, a question mark, or a blank — never a fallback that "looks fine".

---

## 10.5 Screenshots that undermine the product

**HIGH**

**Banned specifics**

- Screenshots with placeholder or obviously fake data
- Blurry screenshots captured at 1× and displayed at 2×
- Screenshots showing an outdated version of the UI
- Cropped so tightly the context is lost, or so wide nothing is legible
- Browser chrome, bookmarks bar, and desktop clutter left in
- Personal data left visible
- Screenshots with text too small to read at the displayed size
- Light-mode screenshots on a dark page, or the reverse

**Why this matters**

The screenshot is usually the most persuasive asset on the page — it is the only element that shows the product actually existing. A bad one is worse than none, because it demonstrates carelessness in the artifact meant to demonstrate care.

**Instead**

- Capture at **2× device pixel ratio**, display at 1×, so it is sharp on every modern screen
- **Realistic data** — real-looking names, plausible numbers, genuine states. Not "Lorem", not "Test User", not `$1,234.56`.
- Crop to the thing you are illustrating; if detail matters, zoom into the region rather than shrinking the whole window
- Remove browser chrome unless the browser is the point
- Scrub personal and customer data
- Provide light and dark variants and swap with the theme
- Re-capture when the UI changes — a stale screenshot is a broken promise
- Real `alt` text describing what the screenshot shows, not "screenshot"

---

## 10.6 Video and audio failures

**HIGH**

**Banned specifics**

- Autoplay with sound
- Video that cannot be paused
- No captions
- No transcript for anything with meaningful narration
- Video that carries information available nowhere else
- Uncompressed video shipped as a background
- No poster frame, so the space is empty until it loads
- Video that keeps playing off-screen, burning battery
- Full-viewport motion with no reduced-motion alternative

**Why this is slop**

Autoplay with sound is the most reliably hated pattern on the web. Missing captions exclude deaf and hard-of-hearing users and everyone watching without sound — which, on mobile, is most people. Full-viewport motion is a leading vestibular trigger.

**Instead**

- Never autoplay with sound. If it autoplays, it is muted, brief, and clearly pausable.
- **Captions on everything.** Not auto-generated and left uncorrected — reviewed.
- **A transcript** for anything longer than a few seconds. It is also indexable, which auto-captions are not.
- Poster frame always; pause when out of viewport; compress hard
- Never make video the sole carrier of information
- Under `prefers-reduced-motion`, serve the poster image instead

---

## 10.7 Images of text

**HIGH** — and an accessibility failure

**Banned specifics**

- Headlines rendered as images
- Pricing tables, feature comparisons, or quotes as images
- Text baked into a hero graphic
- Code samples as screenshots when the code could be text
- Infographics carrying information available nowhere else

**Why this is slop**

Text in an image cannot be selected, copied, searched, translated, resized by the user, restyled for dark mode, or read aloud. It blurs on zoom, and it is invisible to search engines.

**Instead** — real text, positioned over the image with CSS. Real `<pre><code>` for code, so it can be copied. For a genuine infographic, provide the same content as structured text nearby — that is also the version search engines can read. Logos are the reasonable exception, and they still need `alt`.

---

## 10.8 Decorative overlays that destroy contrast

**MEDIUM**

**Banned specifics**

- White text over a photo with no scrim, legible only where the photo happens to be dark
- Gradient overlays tuned to one crop that fail at other viewport sizes
- Text over a busy region of an image
- Contrast that passes on the designer's monitor and fails outdoors
- Overlay opacity chosen by eye rather than measured

**Instead** — a measured scrim (a solid colour at defined opacity, or a directional gradient) sized to the text block rather than the whole image, verified at the worst-case crop across every breakpoint. Or move the text off the image entirely — beside it, above it, below it. Text on photography is a choice; legibility is not optional.

---

## 10.9 Inconsistent visual language across assets

**MEDIUM**

**Banned specifics**

- Photography on one section, flat illustration on the next, 3D renders on a third
- Different colour grading between photographs
- Screenshots at inconsistent crops, corner radii, and shadow treatments
- Some images with borders, some without, no rule
- Aspect ratios varying arbitrarily within one grid

**Why this is slop**

Individually acceptable assets that do not agree with each other read as assembled rather than designed. Consistency across assets is one of the clearest signals that a real team was involved.

**Instead** — pick one visual language and hold it. Grade photography to a consistent temperature and contrast. Define one screenshot treatment — radius, border, shadow, background — and apply it everywhere. Fix aspect ratios per context. Write the rules down; unwritten rules drift.

---

## 10.10 Media with missing or useless alt text

**CRITICAL**

**Banned specifics**

- No `alt` attribute at all
- `alt="image"`, `alt="photo"`, `alt="screenshot"`, `alt="graphic"`
- Filenames as alt text (`alt="IMG_4821.jpg"`)
- Keyword-stuffed alt text written for search engines
- Decorative images with descriptive alt, adding noise
- Long descriptions crammed into `alt`
- Alt text duplicating an adjacent visible caption

**The rule**

Alt text answers: **what would a sighted user learn from this image that they cannot learn from the surrounding text?**

- **Informative image** → describe the information: `alt="Permission report showing 23 requested permissions, 3 flagged as dangerous"`
- **Decorative image** → `alt=""` (empty, not missing) so it is skipped
- **Functional image** (a linked logo) → describe the destination: `alt="Home"`
- **Complex image** (a chart) → a short `alt` plus the full data nearby as text
- **Image of text** → do not; if unavoidable, the alt is the exact text

Empty `alt=""` and a missing `alt` are different: the first says "skip this", the second makes the screen reader guess, often by reading the filename aloud.

---

## Quick audit

```text
unsplash   pexels   shutterstock   istockphoto   gettyimages
alt="image"   alt="photo"   alt="screenshot"   alt=""   (on informative images)
<img                (with no alt attribute at all)
autoplay            (with no muted)
<video              (with no <track kind="captions">)
emoji in JSX/HTML   (used as an icon)
non-Latin characters in markup   (brand marks set as text rather than shipped as assets)
lucide + heroicons + react-icons   (more than one icon set imported)
Lorem   "Test User"   "John Doe"   (visible inside a screenshot)
```

Then look at the page with fresh eyes: could any image here appear on a competitor's site unchanged? Every "yes" is slop.

---

## Sources & further reading

- [The Ultimate Guide to Detecting AI-Generated Images Online in 2026](https://facia.ai/blog/the-ultimate-guide-to-detecting-ai-generated-images-online-in-2026/)
- [AI Lifestyle Photos Hurting Your Brand in 2026](https://www.rewarx.com/blogs/ai-lifestyle-photos-hurting-brand)
- [Stock Photos vs AI: Which Option Wins for Your Brand?](https://www.photoaistudio.com/blog/stock-photos-vs-ai-which-option-wins-for-your-brand)
- [Should Brands Use AI Product Images?](https://www.squareshot.com/post/should-brands-use-ai-product-images)
- [Top Photography Trends for 2026: AI, authentic & cinematic](https://www.visualsclipping.com/blog/top-photograhy-trends-2026/)
- [Image Optimization in 2026: WebP/AVIF, DPR, and Lazy-Loading](https://tworowstudio.com/image-optimization-2026/)
