# Changelog

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
