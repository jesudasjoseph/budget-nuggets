<script lang="ts">
	import feather from 'feather-icons';
	import type { FeatherIconNames } from 'feather-icons';

	export let icon: FeatherIconNames;
	export let size: 'xxs' | 'xs' | 'sm' | 'default' | 'md' | 'lg' | 'xl' = 'default';

	const attrs = feather.icons[icon].attrs;
	attrs.class += ` ${size}`;
</script>

<svg {...attrs} aria-hidden="true">
	{@html feather.icons[icon].contents}
</svg>

<style>
	.xxs {
		width: 0.4rem;
		height: 0.4rem;
	}
	.xs {
		width: 0.8rem;
		height: 0.8rem;
	}
	.sm {
		width: 1rem;
		height: 1rem;
	}
	.default {
		width: 1.4rem;
		height: 1.4rem;
	}
	.md {
		width: 1.8rem;
		height: 1.8rem;
	}
	.lg {
		width: 2.4rem;
		height: 2.4rem;
	}
	.xl {
		width: 3rem;
		height: 3rem;
	}
</style>
