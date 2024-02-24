<script lang="ts">
	import { setContext, onMount, getContext } from 'svelte';
	import { writable, type Writable } from 'svelte/store';
	import { page } from '$app/stores';

	import type { Period } from '@models/periods';
	import { afterNavigate } from '$app/navigation';

	const period: Writable<Period | undefined> = writable();
	setContext('period', period);

	const periods: Writable<Period[]> = getContext('periods');

	const updatePeriod = () => {
		$period = $periods.find((p) => p.id === parseInt($page.params.period));
	};

	onMount(() => {
		updatePeriod();
	});

	afterNavigate(() => {
		if (parseInt($page.params.period) !== $period?.id) updatePeriod();
	});
</script>

{#if $period}
	<slot />
{/if}
