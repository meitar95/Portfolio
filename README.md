# meitarmechoresh.com

Personal portfolio. Built with [Astro](https://astro.build) (plain, fast HTML pages),
hosted on Vercel. Every change pushed to GitHub republishes the site automatically.

## Where things live

| What | File |
|---|---|
| Colors, fonts, spacing (design tokens) | `src/styles/global.css` |
| Page shell: head, nav, footer | `src/layouts/Base.astro`, `src/components/Nav.astro`, `Footer.astro` |
| Homepage | `src/pages/index.astro` |
| Hero blue glow (pure CSS) | `src/components/HeroGlow.astro` |
| Homepage project card | `src/components/ProjectCard.astro` |
| **Case-study template** (one layout for all studies) | `src/pages/work/[slug].astro` |
| Template rules (required fields) | `src/content.config.ts` |
| Case-study content (one file each; `.mdx` can embed visuals) | `src/content/work/*.md(x)` |
| Filtering interactive prototype (before/after) | `src/components/filtering/FilterBeforeAfter.astro` |
| Filtering evidence visuals | `src/components/filtering/*.astro` |
| Sentrycs slider + visuals | `src/components/sentrycs/*.astro`, images in `public/images/sentrycs/` |
| Farmers before/after + visuals | `src/components/farmers/*.astro`, images in `public/images/farmers/` |
| YouTube link cards | `src/components/VideoLinks.astro` |
| Before/after drag slider (any case study) | `src/components/BeforeAfterSlider.astro` |
| Screens behind tabs (any case study) | `src/components/ScreenTabs.astro` |
| Cybersixgill / Herd visuals | `src/components/cybersixgill/*.astro`, `src/components/herd/*.astro` |
| Final flow with clickable screens (every Result) | `src/components/FlowScreens.astro` — usage at the top of the file |
| Flow chart (any case study) | `src/components/Flow.astro` — usage example at the top of the file |
| Icons (Untitled UI style) | `src/components/icons.ts`, `Icon.astro` |
| Reference image with caption | `src/components/RefImage.astro` |
| Images | `public/images/` |

## The case-study template

Every study renders in the same order:

1. Title + one-line payoff
2. Role · Team · Timeline · Platform
3. Outcomes (max 3 numbers)
4. Why it mattered
5. The solution (visual + 2–4 key points)
6. What we learned
7. *How we got there* → The problem, The evidence
8. Next case study

The build fails if a required field is missing, so the structure can't drift.

## Adding or editing a case study

1. Copy `src/content/work/filtering.md`, rename it (the file name becomes the URL: `/work/<name>/`).
2. Fill in the fields at the top, then write *The problem* and *The evidence* below.
3. Keep `draft: true` until it's finished: drafts show in preview, never on the live site.

## Voice (how the copy should sound)

Picked together on 2026-10-14: warm and personal, light hooks, I + we.

- **I** for my own calls and work ("I decided where it lives"). **We** for team work and results.
- Talk like a designer explaining the project to a friend in the field: plain words,
  short sentences, UX terms only where they're the precise word (cognitive load, power users, design QA).
- Personal is good: what surprised me, what I loved, what I'd do differently. Only real moments.
- Titles get a light hook plus the fact ("From paper binders to 15,000 farms").
- Avoid the usual AI tells: "X, not Y" slogans, "It wasn't X, it was Y", a colon before a
  big reveal, three-adjective lists, neat one-liner morals, and words like seamless,
  leverage, elevate, robust.

## Design rules

- Two type families only: Lustria (headings), Satoshi (body).
- No text smaller than 14px. Body text passes WCAG AA contrast.
- One max-width (1080px) and one side gutter for every section.
- Motion: fade in once, never hide content; everything respects "reduce motion".
- Meta label is always "Timeline", lowercase units ("6 months").

## Running it locally (optional)

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # production build into dist/
```
