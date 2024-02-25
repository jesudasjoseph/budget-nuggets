<script lang="ts">
	import { getContext, onMount } from 'svelte';
	import type { Writable } from 'svelte/store';

	import { listPeriodCategoriesAPI } from '@api/period';
	import type { Period, PeriodCategory } from '@models/periods';
	import type { Budget } from '@models/budget';

	import PeriodHeader from './components/PeriodHeader.svelte';
	import PeriodCategoryCard from './components/PeriodCategoryCard.svelte';
	import PeriodCategory from '@components/PeriodCategory.svelte';

	const budget: Writable<Budget> = getContext('budget');
	const period: Writable<Period> = getContext('period');
	const periods: Writable<Period[]> = getContext('periods');

	let periodCategories: PeriodCategory[] = [];

	$: if ($period) {
		listPeriodCategoriesAPI($period.id).then((response: PeriodCategory[]) => {
			periodCategories = response;
		});
	}
</script>

<PeriodHeader period={$period} periods={$periods} budgetId={$budget.id} />
<div>
	{#each periodCategories as periodCategory}
		<PeriodCategoryCard
			id={periodCategory.id}
			value={periodCategory.value}
			label={periodCategory.category.label}
			color={periodCategory.category.color}
		/>
	{/each}
</div>

<style>
	div {
		display: flex;
		flex-direction: column;
		width: 100%;
		row-gap: var(--space-sm);
	}
</style>
