<script lang="ts">
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	import { getDate } from '@/utils';
	import type { Period } from '@models/periods';

	const periods: Writable<Period[]> = getContext('periods');

	const selectedPeriod = $periods.find(
		(period) => period.start_date <= getDate() && period.end_date >= getDate()
	);
	if (selectedPeriod) goto(`${$page.url}/${selectedPeriod.id}`);
	else goto(`${$page.url}/create`);
</script>
