import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// MDX lets a case study embed visual components (charts, diagrams) between paragraphs.
export default defineConfig({ site: 'https://meitarmechoresh.com', integrations: [mdx()] });
