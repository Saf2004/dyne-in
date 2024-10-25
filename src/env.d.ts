/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />


// https://docs.astro.build/en/guides/environment-variables/#intellisense-for-typescript
interface ImportMetaEnv {
	readonly SITE: string;
	readonly BASE_URL: string;
	readonly SENTRY_AUTH_TOKEN: string;
}

interface ImportMeta {
	readonly env: ImportMetaEnv;
}
