# Changelog

## 2026-10-18 · Consistency pass

- Before/after slider: drag from the handle only; Before/After tags glide to that side.
- Zoom icon stays light everywhere (benchmark row had inherited grey).
- Case-study roles in one format ("Product Designer via UI Human Factors"), Farmers platform
  now B2B mobile, its "50+" label matches the number, Cybersixgill tagline uses digits.
- Experience: UIHF title matches the CV (Product Designer & Design Project Manager), "Present".

## 2026-10-18 · Card glow, calmer AI chips, case-study stepper

- Homepage cards: every visual gets a small soft glow (white 4px ring plus a faint blue
  halo), echoing the AI box focus ring. Slightly stronger on hover.
- Filtering card: chips now land 0.6s apart (was 0.35s). Space opens first, the chip fades up,
  and a brief soft-blue "AI added this" glow settles to grey. Rows, count and toast wait for
  the last chip.
- Case-study template: a quiet "← Previous · 2 / 5 · Next →" line above the title, small grey
  text, accent on hover, wraps around at the ends. Counter hidden under 360px.

## 2026-10-18 · Photo and a personal touch in the hero

- `HeroAvatar.astro`: Meitar's photo beside the name (140px desktop, 104px phone) in a thin
  white rim shaped like the blobs in her Lottie illustrations, with three small sparkles in
  her illustration colors. Quiet motion (14s rim drift, 5.5s twinkle), off for reduced motion.
- Footer: two small sparkles beside "Thanks for stopping by." (soft blue and mint, tuned
  for the dark band), twinkling out of step. A site-wide sparkle system was previewed and
  turned down in favor of keeping it to the hero and this closing touch.
- A personal line under the intro was tried and removed.
- Chosen from four previewed options (photo beside, small avatar, photo with illustrations,
  and this combination). Checked at 1440, 1024, 768, 390 and 320px with no overflow.

## 2026-10-15 · Off Framer completely, learnings at the end

- Motion reel: the last three animations (email, call, CV) are now in `/public/lottie/`, so
  nothing loads from Framer any more. Picked the full 15s CALL loop over CALL2 (a cut 5s
  version that jumps at the loop point); duplicates were identical files.
- Case study template: "What we learned" moved from the opening summary to the end, after
  the result, so the story reads problem → evidence → result → lessons.
- Huskeys bullet: "First product designer. Built the design function and helped grow the
  team to five."

## 2026-10-14 · One enlarge behaviour everywhere, real pinch zoom

- `Zoom.astro` rewritten: the screen opens fitted to the phone, with real pinch-to-zoom,
  drag to pan, double-tap to zoom in/out, scroll-wheel on desktop, and − / Fit / + buttons.
  Before/after pairs open with a Before / After switch.
- Same trigger on every screenshot: a small round expand icon in the corner, and tapping
  the screen opens it. Applied to flow screens, screen tabs, reference images, the
  benchmark snapshots (their old small dialog is gone) and the before/after sliders
  (icon only there, since dragging moves the slider).
- Flow chart steps: the arrows no longer scroll the whole page to the active step; only the
  step row slides, and only when the step is out of view.
- Vocabulary map on phones: old names, arrow down, new name, left aligned.
- "~10–14" now reads "10 to 14".

## 2026-10-14 · Mobile review fixes

- New shared full-screen viewer (`Zoom.astro`): every desktop flow screen and every
  before/after slider gets an **Enlarge** button. On phones the screen opens at a readable
  width and can be swiped and pinched; sliders open Before and After stacked.
- Case study header on phones: Role / Team / Timeline / Platform are one row each (label
  left, value right) instead of two narrow, ragged columns.
- Outcome numbers never wrap ("10 → 10K" stayed on two lines before).
- "What we learned" quote is a size smaller on phones.
- Filtering pattern matrix: on phones it becomes a list (module → pattern used), since the
  4-column grid was cut off.
- "Next case study" link keeps its last word and arrow together.

## 2026-10-14 · Filtering: mock table instead of grey placeholders

- Prototype: the grey bars are now a faded findings table (finding, severity, status, cloud)
  built from the same demo data the filters run on, so every filter visibly changes the rows.
  The four grey widgets became summary cards (total, critical, open, crown jewels). Phones
  show finding + severity only. Seeded counts unchanged (104 of 257).
- Homepage card: the bars are faded finding rows; after the AI adds filters, the two critical
  AWS rows stay highlighted and the rest fade out.
- Result flow: all six prototype captures retaken with the table.

## 2026-10-14 · Filtering before/after on phones

- Under 640px the drag slider is replaced by a Before / After switch. Each side gets the full
  width: the four old filter bars stacked, or the live new filter bar (still fully tappable:
  Ask AI, Quick Start, is → is not, Save View). Desktop and tablet keep the slider.

## 2026-10-14 · Launch prep, facts check and full review

**Facts**
- Hero: dropped "Senior" from the role line and meta description.
- Experience realigned to the CV summary from the Framer site.
- Roles: Cybersixgill, Sentrycs and Herd all say "via UI Human Factors". Herd is "Lead
  designer" with no promotion story; its third outcome is now "4 core areas on one shared set
  of components".
- Farmers: growth chart credits the check with Afimilk's analysts; usage findings no longer
  claim exact dates.

**Launch**
- `public/og.png` (1200×630) for link previews, plus a `404` page.
- Motion reel: three originals now served from `/public/lottie/`. Three are still on Framer's
  CDN, and a tile that fails to load now removes itself instead of leaving a gap.
- Satoshi still loads from Fontshare (the download is blocked from the build container).

**Review at 1440, 1280, 1024, 834, 768, 600, 390, 360, 320**
- No horizontal scroll or overlapping text on any page.
- Type scale tightened: off-scale sizes (12, 13, 16, 18, 20px) in diagrams moved to 14, 17, 21 or
  24px. Text under 14px is only left inside product mocks shown at true scale, and in the
  Sentrycs "before" sample that shows the old 11 to 12px text on purpose.
- Copy: removed repeated lines (Filtering "why" vs. tagline and problem; Sentrycs "tested with
  ~20 users" said three times; Herd "same components" said three times), a couple of tidy
  one-line morals, and the em dashes in page titles. Hero lead no longer repeats "AI-native".

## 2026-10-14 — Filtering: Quick Start step fixed

- The "Or a Quick Start" screen in the final flow was captured on top of the AI result, so
  the panel showed the wrong chips highlighted. Recaptured from a clean state: Critical only
  selected, its two filters (Severity is Critical + Status is Open, In progress) in the bar.
- Prototype bug: picking a Quick Start grew the bar but not the frame, so the open panel
  spilled out. The frame now re-measures after every change.

## 2026-10-14 — Filtering card: responsive AI moment

- The Ask AI box now takes the full row while typing (saved views slide out of the way).
- Sized by the card's own width (container queries): one row of chips at every size, with
  3 chips → 2 + "+1" → 1 + "+2" as space shrinks; count moves into the toast on small cards.
  Checked at 1440, 1100, 900, 820, 600, 390 and 320px.
- Nav: tighter spacing under 360px so the Contact button no longer overflows on 320px phones.

## 2026-10-14 — Filtering card: slow AI moment

- Replaced the fast 4→1 fold with `filtering/FilterAICard.astro`: the Ask AI box opens, slowly
  types "Critical AWS findings this week", thinks, then three filters arrive one by one, the
  table narrows to 7 matches and a toast confirms. It lingers ~4s, then eases back to the start
  and loops (~14s). Only runs while on screen; static end state for reduced motion.

## 2026-10-14 — New Filtering card visual

- `filtering/FilterFold.astro` replaces the cropped mini panel: the four old filter bars
  (Findings, Log analysis, Achievements, Inventory) fold into the one new bar with chips and
  a results table. Plays once when the card scrolls into view, replays on hover/focus.
  Static "after" for reduced motion; 4:3 on phones.

## 2026-10-14 — Card buttons go light

- Black buttons are now only for "Contact me". "Read case study" uses the light button
  (white, steel-blue dot that grows into an arrow) with a soft shadow so it holds on tinted cards.

## 2026-10-14 — Hero intro

- Repositioned around security and complex B2B: "Founding designer at Huskeys, building WAF and API
  security from zero. Almost 5 years turning complex B2B systems into tools people trust..."
  Role line and meta description updated to match.

## 2026-10-14 — Filtering references from the FigJam board

- `filtering/Benchmarks.astro` now shows real snapshots from the "filtering-ux" FigJam
  reference board: Notion, Linear, monday.com and Kibana featured (with the pattern each
  belongs to and what I took from it), plus Datadog, Jira, Cycode, Rapid7, Tenable,
  Microsoft Foundry and SentinelOne in a swipeable row. Tap any snapshot to enlarge.

## 2026-10-14 — Result sections with the final flow

- Fixed: the Filtering process cards had titles overlapping their text. The template's
  heading spacing rule was reaching into visuals; it now only applies to the page's own headings.
- New `components/FlowScreens.astro`: the final flow as a flow chart where every step is
  clickable and shows its real screen (spotlighting the right part when steps share a screen).
  Arrows, prev/next, keyboard arrows; swipeable steps on phones.
- Every case study now ends with a "The result" section: the outcome, then the final flow.
  - Filtering: 6 steps captured from the working prototype (view → ask AI → chips →
    Quick Start → is / is not → save view).
  - Sentrycs: the operator loop on the shipped screen (map → Sky Status → details → analytics).
  - Cybersixgill: the inventory flow (moved here from the evidence section).
  - Farmers: today's tasks → task → group → confirm → multi-select (phone frames).
  - Herd: dashboard → tasks → one cow → settings (replaces the separate screen tabs).

## 2026-10-14 — Copy rewrite in Meitar's voice

- Picked together: warm and personal, light-hook titles, "I" for my calls and "we" for team work.
  The rules are written down in README → Voice.
- Rewrote every case study (titles, taglines, card text, why, solution, learned, body),
  the homepage hero and experience bullets, the footer, and the captions inside visuals.
- Removed the usual AI tells: "X, not Y" slogans, "it wasn't X, it was Y", colon reveals,
  three-adjective lists and tidy one-line morals.
- New titles: Filtering → "From four filter bars to one"; Sentrycs → "A counter-drone
  system that finally looks the part"; Herd → "When everyone says 'it doesn't look good'".

## 2026-10-14 — Floating laptop, Filtering slider, new Herd screens

- Cybersixgill: the laptop mockup is cut out (transparent background) and floats with
  a soft shadow. `RefImage` has a new `bare` option for cut-out mockups.
- Filtering: the Before/After switch is now the same drag-to-compare slider as Sentrycs
  and Herd, drawn over the live prototype. Only the handle takes clicks, so the new
  filter bar stays usable; tap "After" to slide fully open, "Before" to slide back.
  Arrow keys move the handle. The headline still changes, following the bigger side.
- Herd: Dashboard, Herd view and Settings replaced with the latest screens.

## 2026-10-14 — Flow chart, Cybersixgill and Herd

**Template**
- New `components/Flow.astro`: a flow chart any case study can use in MDX. One or more
  lanes (e.g. Before / After), steps with an optional detail, a red "drop-off" tag
  where people left, faded steps after it, and a highlighted end step. Horizontal on
  desktop, vertical on phones. Used in Farmers, Cybersixgill and Herd.
- The drag-to-compare slider is now shared (`components/BeforeAfterSlider.astro`);
  Sentrycs and Herd both use it. New shared `components/ScreenTabs.astro`.

**Cybersixgill** (published) — from the C6G Figma page
- Hero: Dashboard / Asset inventory / Monitoring policies (browser bar cropped out).
- Same widget at 10 and 10k alerts; the 3×3 widget grid drawn as a diagram; the
  inventory flow as a flow chart; the shipped dashboard from Cybersixgill's site.

**Herd** (published) — from the "Presenting" slides and the 2023 concept file
- Hero: Daily Tasks before/after slider. Problem → brief as a flow chart.
- Calendar and task list zoomed before/after; dashboard, herd view and settings tabs.
- Links to the Farmers study (the field app it led to).

## 2026-10-14 — Screen anatomy fits one screen

- "One screen, broken into parts": the screenshot's width is now capped by the window
  height, so the screen and all 8 parts fit together on laptops (checked 1024×700 up to
  1920×1080). Hovering a part never hides the screen under the nav.
- Tapping a part when the screen is partly off-view scrolls the whole figure into view.
- Tablets and phones: the parts become one swipeable row directly under the screen.

## 2026-10-14 — Farmers case study (published)

- Built from the Afi-App Figma board (analytics, field sessions, new design, wireframes).
- Hero visual: old app next to the redesign, phone by phone (Daily tasks, Cow card).
- "What the data said": 1,000 farms never logged vs 400 that did; logging in bursts;
  574 farms tagging in bulk; tasks logged ~50/50 from cow card vs Add event.
- Field notes: 3 real screens from remote sessions, cropped to the app only (no faces
  or names), with the original critiques translated from Hebrew.
- Tag assignment in 3 steps (type or scan with the wand → confirm → next cow).
- Growth chart: task events 0.03M → 0.15M → 0.29M. Farmers is no longer a draft.

## 2026-10-14 — Sentrycs: team voice + videos

- The concept-deck brief now reads "we" (the deck was a team effort).
- New `components/VideoLinks.astro`: YouTube thumbnail cards that open in a new tab
  (no embedded player, so nothing heavy loads). Sentrycs links its two public videos
  that feature the redesign.

## 2026-10-14 — Sentrycs case study

- Built from the Sentrycs Figma file (Presentation + Style guide pages).
- Hero visual: drag-to-compare slider with 3 real before/after pairs (Real time,
  Analytics, Settings); legacy screens cropped from browser captures, same frame size.
- "One screen, broken into parts": hover a part to spotlight it on the shipped screen.
- Readability shown at real size (11–12px vs 16px / 14px floor).
- The brief from the concept deck: keep the UX, upgrade the UI + look-and-feel pillars.
- Style guide: drone states, zone states, 4 terrain backgrounds, tablet sizing, index.
- Template: "What we learned" (team voice); h3 subheadings in the fold get the same
  heading-to-paragraph rhythm.

## 2026-10-14 — Filtering story: usage ≠ success

- Rewrote the Filtering story around the real discovery: the most-used feature was where
  power users struggled most. Recordings (analyzed with Amplitude's AI agent) showed
  repeated clicks and mid-search exits at 3 clients; Customer Success confirmed it, and
  users blamed themselves.
- New visuals: "dashboard vs. recordings" + a reconstructed session track
  (`SessionPattern.astro`), and what Customer Success heard (`VoiceOfCustomer.astro`).
- Process steps now start from questioning the assumption. Outcome "3 at-risk clients"
  replaces "1 cycle". New "What I learned".
- Font check: Geist vs Plus Jakarta Sans inside the mock; kept Plus Jakarta Sans to match
  the shipped product and the Figma reference image.

## 2026-10-14 — Template rhythm, rebuilt prototype, visual evidence

**Template**
- Outcome numbers in Satoshi (no serif). "All work" link removed.
- One spacing system: 96px between sections (64px on phones), 12px from a heading to
  its paragraph, 32px from text to a visual. Applied above and below the fold.

**Filtering prototype** (`components/filtering/FilterBeforeAfter.astro`), rebuilt from the Figma file
- Figma tokens and the product font (Plus Jakarta Sans, only inside the mock).
- Chips match the Figma anatomy: field | is | values | is not | values | ×, with color dots.
- Works on a 257-row generic dataset, so "Matching" is always true; "My Special View"
  shows 104 of 257, as in the Figma frame.
- New interactions: click "is" to flip to "is not"; And/Or toggle; Simple panel with
  grouped families → value list with Is/Is not per value; Advanced panel with
  field → operator → value rows, add/remove; Quick Starts that add several filters
  at once (e.g. Critical only = Severity: Critical + Status: Open, In progress);
  Ask AI with suggested queries and free text; Save view (adds a tab), Reset, toasts.
- Made-up numbered markers removed. Before/After is now a simple sliding switch,
  with a headline below that changes slowly (fade + slight blur).
- Phones: chips scroll sideways in one row; panel goes full width.

**Evidence visuals** (from the research board, no invented data)
- Pattern matrix (6 modules × 4 patterns), vocabulary map, process strip with icons,
  benchmark cards, 28 → 8 families → ~10–14 fields, and the final Figma panel as a
  reference image. Filtering is now MDX so visuals sit between paragraphs.

## 2026-10-13 — Feedback round 1

- **Signature button restored** (`components/Button.astro`): peach dot grows into a circle
  with an arrow on hover/focus, background shifts to a grey-to-black gradient. Used for
  every button on the site, including the card buttons (they react when the card is hovered).
- **Hero glow**: no box around it anymore, so no hard edges; it visibly wanders (13–19s
  loops) and is much softer. Clipped sideways only, so phones never scroll horizontally.
- **Nav**: transparent at the top so it doesn't slice the glow; frosted background appears
  after scrolling. Button reads "Contact" on phones so the nav isn't cramped.
- **Motion reel**: white boxes removed; animations sit on the page, centered, unclipped.
- "Selected work" heading hidden (kept for screen readers). Huskeys link removed.
- Reveal: anything already on screen shows instantly; fade shortened to 0.45s; the
  interactive before/after never fades.

## 2026-10-13 — Images, motion reel, content fixes

**Added**
- Card images for Sentrycs, Cybersixgill, Farmers and Herd (WebP, 800px + 1600px, ~12–60 KB each), with real alt text.
- "More capabilities — Motion & illustration" section: the 6 Lottie animations from the
  Framer site. The player loads only when the section is near, pauses off-screen, and
  shows a still frame for reduced-motion visitors.

**Changed**
- Filtering → Ask AI: now credits the request to Product and shows Meitar's call on
  placement and behavior (in the filter bar, changing the table, not a side chat).
- Experience: Bank Leumi restored as a client name (text only, no screens).
- Card images are 16:9 so logos are never cropped.

**Pending**
- Lottie files still load from Framer's CDN; swap in the originals before cancelling Framer.

## 2026-10-13 — Foundation + Filtering pilot

**Added**
- Design tokens taken from the Framer site: warm off-white background, the five-step
  baby-blue card scale, steel-blue skill chips, Lustria + Satoshi.
- Homepage: hero, CSS-only blue glow, Selected work, What I bring, Experience, footer.
- Case-study template enforced by a schema (every study, same structure).
- Filtering case study rewritten outcome-first.
- Interactive before/after for Filtering, rebuilt from the Figma prototype in HTML
  (replaces the hard-to-read screenshots and the MP4s).
- README explaining where everything lives.

**Fixed vs. the Framer site**
- Cards no longer stack and cover each other's text; they fade in once and stay.
- Mobile keeps the same copy and the card images (Framer had separate, drifting
  copies per breakpoint).
- Third font (Hanken Grotesk) and unused template fonts removed.
- "Premium UX Template for Framer" alt text removed.
- Body grey darkened from 50% black to pass WCAG AA contrast.
- Logo shows the full name (or "MM" on small phones) instead of "Meit".
- Hero glow's near-black blob replaced with a low-opacity deep slate.
- Hamburger menu removed: three links fit on every screen.
- Experience: Sentrycs line no longer says "Led"; Bank Leumi name removed (confidential).

**Pending**
- Card images for the other four studies.
- Migrate Sentrycs, Cybersixgill, Farmers, Herd into the template.
- Self-host Satoshi font files.
