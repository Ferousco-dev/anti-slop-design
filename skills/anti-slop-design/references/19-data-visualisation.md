# 19 — Data Visualisation

> **Module:** 19 of N · **Status:** stable
> **Read when:** building any chart, dashboard, metric tile, sparkline or table — analytics, fintech, logistics, health, admin.
> **Note:** if a dedicated `dataviz` skill is available in the session, load that too. This module covers the *slop* dimension — the ways generated charts mislead or fail — and is deliberately complementary rather than a replacement for a full charting system.

Charts are the highest-stakes thing in this whole skill, because a bad chart doesn't look bad. It looks authoritative and says something false. Every other module is about a design failing to impress; this one is about a design failing to be *true*.

Severity legend as in [`02-visual-patterns.md`](02-visual-patterns.md).

---

## 19.1 Truncated axes on bar charts

**CRITICAL**

**Banned specifics**

- A bar chart whose y-axis starts anywhere other than zero
- A "zoomed" bar chart to make a small difference look large
- No axis break marker where truncation is unavoidable
- Truncation applied silently by a charting library default

**Why this is slop**

A bar encodes value by *length*. Truncate the axis and the length no longer maps to the value, so a 2% difference can be drawn as a 5× one. This is the oldest way to lie with a chart and it is usually not deliberate — it is a library default nobody checked.

**Instead** — bar and column axes start at zero, always. Line charts have more latitude because they encode *change* by slope rather than value by length, but if you truncate a line axis, mark the break and label it. If the real story is a small difference, use a chart that can show a small difference honestly: a dot plot, or a chart of the delta itself.

---

## 19.2 Dual axes

**HIGH**

**Banned specifics**

- Two series on two different y-axes in one chart
- Axis ranges chosen so the lines cross where you want them to
- A revenue line and a percentage line sharing a plot
- Any dual axis without both scales clearly labelled

**Why this is slop**

With two independent scales, the *visual* relationship between the lines is an artefact of the ranges you picked. Shift one axis and you can make the same data show correlation, inverse correlation, or a crossover — none of which is in the numbers. The reader sees a relationship you invented.

**Instead** — two charts stacked with a shared x-axis. Or index both series to a common baseline (both start at 100) so a single axis is honest. Or chart the ratio directly if the relationship is the point.

---

## 19.3 The rainbow palette

**HIGH**

**Banned specifics**

- Full-spectrum ROYGBIV for a sequential scale
- A different hue per series with no meaning attached
- Red-to-green as a diverging scale
- More than about six categorical colours in one chart
- Colour assigned by library default order

**Why this is slop**

Rainbow has no natural order, so the eye cannot rank it — and it is perceptually non-uniform, meaning equal steps in the data produce unequal steps in appearance, which creates false boundaries that look like findings.

Red-green is separately disqualified: it is the most common colour-vision deficiency, affecting roughly 8% of men.

**Instead**

- **Sequential data** → a single hue varying in lightness, or a perceptually uniform scale (viridis and similar)
- **Diverging data** → two hues with a neutral midpoint. **Blue–orange** is the safe default; never red–green
- **Categorical data** → six colours maximum, and if you need more, the chart is wrong: group, facet, or highlight one series against grey
- Never let colour be the *only* encoding. Pair with position, label, shape or pattern

---

## 19.4 Pie and donut charts

**MEDIUM**

**Banned specifics**

- More than five or six slices
- A pie for anything that is not parts of one whole
- Two pies compared side by side
- 3D or exploded pies
- A donut with an unrelated number in the hole
- Percentages that don't total 100

**Why this is slop**

People compare angles badly and lengths well. A pie asks for the harder judgement, and past a handful of slices it becomes unreadable — which is why the legend ends up doing the work the chart was supposed to do.

**Instead** — a sorted horizontal bar chart for parts of a whole. Keep pies for the genuine case: two or three slices where "roughly half" is the entire message.

---

## 19.5 Charts that don't say what they are

**HIGH**

**Banned specifics**

- No axis labels
- No units
- No time range stated
- A percentage with no denominator
- "Users" with no definition of active
- No source or last-updated timestamp on a live figure
- A legend where a direct label would do
- A title that names the chart type instead of the finding

**Why this is slop**

An unlabelled chart is decoration wearing the costume of evidence. "Up 40%" with no baseline, no window, and no denominator is not information.

**Instead** — label the axes with units. State the window explicitly ("last 30 days", not "recently"). Give percentages a denominator. Define your metric where it is shown, not in a docs page. Label series directly on the line rather than making the eye round-trip to a legend. Title the *finding*: "Signups doubled after the pricing change" beats "Signups over time".

---

## 19.6 Metric tiles that mislead

**HIGH**

**Banned specifics**

- A big number with no comparison
- A green up-arrow on a metric where up is bad
- Percentage change on a tiny base — "+300%" from 1 to 4
- No time window on the tile
- A sparkline with no scale
- Colour as the only indicator of good/bad
- Numbers that jitter as they update because the font isn't tabular

**Why this is slop**

A number alone is unreadable. 4,200 signups is good or catastrophic depending on last week, and the tile is the place people look first — so it is the place a wrong impression is cheapest to create.

**Instead** — every metric gets a comparison and a window. Say what "good" means for *this* metric, since up is bad for churn, latency, error rate and cost. Suppress percentage change on small bases or show the absolute alongside it. `font-variant-numeric: tabular-nums` on anything that updates, or the digits shift and the tile twitches.

---

## 19.7 Charts nobody can use without a mouse

**HIGH** — and an accessibility failure

**Banned specifics**

- Data available only in a hover tooltip
- Canvas or WebGL charts with no accessible alternative
- No keyboard access to data points
- No table fallback
- No text summary of the finding
- `aria-hidden` on the whole chart with nothing offered instead
- Motion-heavy chart entrances with no reduced-motion path

**Why this matters**

Hover doesn't exist on touch and doesn't exist for keyboard users. If the values live only in a tooltip, the chart has no data for a large share of the audience — and generated chart code puts them there by default, because that is what every tutorial does.

**Instead**

- **Always ship the numbers as text somewhere** — a `<table>` beneath, a details/summary, or a download. This one change fixes most of it.
- Give the chart an accessible name and a one-sentence text summary of the finding: `role="img"` with a real `aria-label`, or a caption
- Make points keyboard-reachable where interaction matters
- Prefer SVG over canvas so elements can carry semantics
- Honour `prefers-reduced-motion` on entrances

---

## 19.8 Chart junk and 3D

**MEDIUM**

**Banned specifics**

- 3D bars, pies or areas
- Gradient fills under lines with no meaning
- Drop shadows on data marks
- Heavy gridlines competing with the data
- Background images behind plots
- Animated entrances that replay on every render
- Decorative axes and frames
- Every gridline labelled

**Why this is slop**

3D adds a dimension carrying no data and makes lengths and angles genuinely harder to judge — perspective distorts the values. Everything else here is ink spent on something other than the numbers.

**Instead** — remove until only data and the minimum scaffolding remain. Gridlines light or absent, no frame, direct labels, no shadows, no gradients unless the gradient *is* a scale. Then check whether the chart got worse. It usually got better.

---

## 19.9 The wrong chart for the question

**MEDIUM**

The most common failure is not an ugly chart, it is a chart answering a different question. Pick by the question, not by what looks impressive:

| The question | The chart |
|---|---|
| How has this changed over time? | Line |
| How do these compare? | Sorted horizontal bar |
| How is this distributed? | Histogram or box plot |
| Are these two related? | Scatter |
| What is this made of? | Stacked bar, or a sorted bar of the parts |
| Where is it? | Map, only if location is the finding |
| How does it flow between states? | Sankey, sparingly |
| Is it above target? | Bullet chart or a bar with a target line |
| One number, in context? | A metric tile with comparison |

**Special cases worth knowing:** stacked areas make individual series impossible to read except the bottom one — use small multiples instead. Radar charts are near-unreadable past three axes. Word clouds encode nothing usefully. Gauges spend enormous space on one number a tile would carry.

---

## 19.10 Dashboards with no hierarchy

**HIGH**

**Banned specifics**

- Twelve tiles of identical size and weight
- No stated time range for the board
- Charts arranged by which team asked for them
- No empty state for a new account
- No indication of staleness on cached data
- A full-page spinner blocking everything on the slowest query
- Filters that reset on navigation
- No export

**Why this is slop**

A dashboard with no hierarchy makes the user do the prioritising every single visit. If everything is equally prominent, nothing is — and this is a screen people open daily, so the cost compounds.

**Instead** — one primary metric, largest and first, answering "is this okay?". Supporting metrics smaller. Diagnostics below or behind a click. One global time range, stated. Load sections independently so a slow query doesn't block a fast one, and show per-section skeletons. Design the first-run empty state, because every new customer sees it. Timestamp cached data. Persist filters. Offer the raw numbers.

**Done when** — a user can answer "is this good or bad?" in under five seconds without asking anyone.

---

## Quick audit

```text
beginAtZero: false          (on a bar chart)
yAxisID / y2 / secondary    (dual axes)
rainbow  jet  hsl(          (spectrum palettes)
PieChart  DoughnutChart     (with more than ~6 slices)
tooltip                     (as the only place values appear)
<canvas>                    (with no table or text alternative)
aria-hidden="true"          (on a chart, with no alternative offered)
3d  bevel  shadow  gradient (on data marks)
tabular-nums                (absent on updating numbers)
```

Then three checks no grep performs: read every axis and ask whether a stranger could state the units and the window; unplug the mouse and try to get the values; and ask what the chart claims versus what the numbers say.

---

## Sources & further reading

- [10 Chart Mistakes to Avoid](https://5of10.com/articles/10-chart-mistakes-to-avoid/)
- [10 Accessibility Mistakes That Make Your Charts Useless](https://5of10.com/articles/10-accessability-errors/)
- [Vibe Coding Charts? 10 Accessibility Mistakes Your AI Is Making](https://5of10.com/articles/vibe-coding-chart-mistakes/)
- [Dueling with axis: the problems with dual axis charts — ONS](https://digitalblog.ons.gov.uk/2019/07/03/dueling-with-axis-the-problems-with-dual-axis-charts)
- [Colour-blind friendly chart palettes (2026)](https://rgblind.com/blog/color-blindness-friendly-chart-colors)
- [Three ways to make your charts more accessible — Flourish](https://flourish.studio/blog/accessible-chart-design/)
