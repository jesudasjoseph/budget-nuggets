import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter(),
		alias: {
			'@api': 'src/api',
			'@stores': 'src/stores',
			'@components': 'src/components',
			'@models': 'src/models',
			'@': 'src',
		},
	}
};

export default config;
