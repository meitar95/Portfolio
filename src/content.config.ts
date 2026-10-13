// The case-study schema = the canonical template, enforced by code.
// A case study cannot build unless every required field is filled in,
// so every page has the same structure, in the same order.
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const work = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/work' }),
  schema: z.object({
    // Card + hero
    title: z.string(),
    tagline: z.string().max(140),            // one line, the payoff
    card: z.string().max(220),               // homepage card blurb
    order: z.number(),
    draft: z.boolean().default(false),       // drafts never reach production
    cover: z.string().optional(),            // /images/... for the homepage card
    coverAlt: z.string().optional(),
    visual: z.enum(['filtering-before-after']).optional(), // interactive hero visual

    // 1. Why it mattered (business angle)
    why: z.string(),
    // 2. Team & my role
    role: z.string(),
    team: z.string(),
    timeline: z.string(),                    // always "Timeline", lowercase units
    platform: z.string(),
    confidential: z.boolean().default(false),
    // Outcome, stated up front (BLUF)
    outcomes: z.array(z.object({ value: z.string(), label: z.string() })).min(1).max(3),
    // 3. The solution
    solution: z.object({
      summary: z.string(),
      points: z.array(z.object({ title: z.string(), text: z.string() })).min(2).max(4),
    }),
    // 4. What I learned
    learned: z.string(),
    // 5 + 6 (The problem, The evidence) live in the Markdown body below the fold.
  }),
});

export const collections = { work };
