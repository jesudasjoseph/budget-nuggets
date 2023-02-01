import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			pages: '../server/static/ui',
			assets: '../server/static/ui',
			compress: true
		})
	}
};

export default config;
