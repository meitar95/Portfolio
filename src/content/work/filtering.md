---
title: Unifying filtering across a security platform
tagline: Four filtering patterns became one AI-assisted system — learned once, used everywhere.
card: Four inconsistent filtering patterns across six modules, unified into one AI-assisted system that users learn once and use everywhere.
order: 1
visual: filtering-before-after

why: >-
  Filtering sits on the critical path to the platform's value: finding a security
  issue and fixing it. As the product grew module by module, filtering grew with it —
  six modules, four patterns, four vocabularies. Users found issues, then stalled
  before resolving them, and less technical users stalled first.
role: Sole Product Designer
team: Product lead, PM, engineering
timeline: 1 month · 2026
platform: WAF & API security, B2B SaaS
confidential: true

outcomes:
  - value: "4 → 1"
    label: filtering patterns, unified across 6 modules
  - value: "~10"
    label: users validated the flow before engineering started
  - value: "1 cycle"
    label: from discovery to a tested, shipped design

solution:
  summary: >-
    One filtering system with one shared vocabulary, built for everyone from a
    first-time viewer to a daily power user.
  points:
    - title: Ask AI
      text: Describe what you want to see in plain language. Per-client suggestions get non-technical users started without learning any syntax.
    - title: Simple / Advanced
      text: The essentials up front, full query depth one click away.
    - title: Grouped filters
      text: Related filters sit in collapsible groups, so complex queries stay readable.
    - title: Save View
      text: Save a filter set and come back to it — no repeated setup for recurring investigations.

learned: >-
  In a security product, the hard part isn't adding capability — it's making complexity
  legible to people who aren't all security experts. One system tuned for a range of
  fluency, plus AI to shorten the loop from idea to tested prototype, is how one
  designer moved a product this complex in a month.
---

## The problem

Six modules, four filtering patterns, four vocabularies. A user who learned to filter
in one module had to relearn it in the next — different entry points, different
labels, different ways to clear or save what they'd built.

Because filtering sits directly on the path to remediation, that friction quietly
throttled adoption, especially for users who aren't security specialists.

## The evidence

**Amplitude** showed where people got stuck: the same filters clicked over and over
without reaching a finding, and dead ends on the path to fixing an issue.

**Power-user interviews** covered what they were trying to achieve, how they filter
today, and how they filter in tools they already trust.

**Market benchmarking** compared filter conventions in tools like Linear, Notion and
Jira, then turned them into a short list of behavior options.

**Testing:** simplified A/B comparisons with power users picked a direction; an
interactive prototype built with Claude and Dia was validated with about ten users —
all inside one work cycle, before engineering wrote a line.

**Result:** strong early client feedback, and the work contributed to closing new
deals. It's now rolling out to all clients, instrumented with session recordings
against defined flows to measure the lift. Filtering became the first proof point for
consolidating all six modules into one coherent product.
