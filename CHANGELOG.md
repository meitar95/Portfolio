# Changelog

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
