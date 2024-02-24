<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import type { Writable } from 'svelte/store';

	import type { Period } from '@models/periods';
	import type { Budget } from '@models/budget';

	import PeriodHeader from './components/PeriodHeader.svelte';

	const budget: Writable<Budget> = getContext('budget');
	const period: Writable<Period> = getContext('period');
	const periods: Writable<Period[]> = getContext('periods');
</script>

<PeriodHeader period={$period} periods={$periods} budgetId={$budget.id} />
