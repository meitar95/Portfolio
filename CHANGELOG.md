# Changelog

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
