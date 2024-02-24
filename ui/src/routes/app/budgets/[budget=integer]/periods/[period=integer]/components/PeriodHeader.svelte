<script lang="ts">
	import Button from '@components/Button.svelte';
	import type { Period } from '@models/periods';

	export let periods: Period[];
	export let period: Period;
	export let budgetId: number;

	const getPeriodIndex = () => {
		return periods.findIndex((p) => p.id == period.id);
	};

	let periodIndex: number;
	let nextPeriodId: number | undefined = undefined;
	let previousPeriodId: number | undefined = undefined;

	$: if (period) {
		periodIndex = getPeriodIndex();
		try {
			nextPeriodId = periods[periodIndex + 1].id;
		} catch {
			nextPeriodId = undefined;
		}

		try {
			previousPeriodId = periods[periodIndex - 1].id;
		} catch {
			previousPeriodId = undefined;
		}
	}
</script>

<div class="header">
	<h3>{period.label}</h3>
	<div class="period-actions">
		{#if previousPeriodId}
			<Button
				label="Previous Budget Period"
				icon="arrow-left"
				iconOnly
				href={`/app/budgets/${budgetId}/periods/${previousPeriodId}`}
			/>
		{/if}
		{#if nextPeriodId}
			<Button
				label="Next Budget Period"
				icon="arrow-right"
				iconOnly
				href={`/app/budgets/${budgetId}/periods/${nextPeriodId}`}
			/>
		{:else}
			<Button
				label="Create The Next Budget"
				icon="arrow-right"
				href={`/app/budgets/${budgetId}/periods/create?currentPeriod=${period.id}`}
			/>
		{/if}
	</div>
</div>

<style>
	.header {
		width: 100%;
		display: flex;
		justify-content: space-between;
	}
	.period-actions {
		display: flex;
		column-gap: var(--space);
	}
</style>
