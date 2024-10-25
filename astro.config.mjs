import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';

import sentry from '@sentry/astro';

const DEV_PORT = 2121;

// https://astro.build/config
export default defineConfig({
    site: process.env.CI
        ? 'https://themesberg.github.io'
        : `http://localhost:${DEV_PORT}`,
    base: process.env.CI ? '/flowbite-astro-admin-dashboard' : undefined,

    // output: 'server',

    /* Like Vercel, Netlify,… Mimicking for dev. server */
    // trailingSlash: 'always',

    server: {
        /* Dev. server only */
        port: DEV_PORT,
    },

    integrations: [//
    sitemap(), tailwind(),  sentry({
      dsn: "https://09be0cfb8a92991101c32820aab98851@o4508183539941376.ingest.de.sentry.io/4508183542366288",
      sourceMapsUploadOptions: {
        project: "javascript-astro",
        authToken: process.env.PUBLIC_SENTRY_AUTH_TOKEN,
      },
    })
		],
});
