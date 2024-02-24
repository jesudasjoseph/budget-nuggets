<script lang="ts">
	import { onMount, getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	import { createPeriod, listPeriods, createNextPeriodAPI } from '@api/period';
	import { getDate } from '@/utils';
	import type { Budget } from '@models/budget';
	import type { Period } from '@models/periods';
	import Button from '@components/Button.svelte';

	import BudgetPeriod from './components/BudgetPeriod.svelte';

	const budget: Writable<Budget> = getContext('budget');

	let periods: [Period];

	let currentPeriod: number;

	function createThisBudgetPeriod() {
		createPeriod(getDate(), $budget.id).then((data: Period) => {
			periods.push(data);
			periods = periods;
			currentPeriod = periods.findIndex(
				(period) => period.start_date <= getDate() && period.end_date >= getDate()
			);
		});
	}

	function createNextPeriod() {
		createNextPeriodAPI(periods[currentPeriod].id, $budget.id).then((period: Period) => {
			periods.push(period);
			periods = periods;
			currentPeriod++;
		});
	}

	onMount(() => {
		listPeriods($budget.id).then((data: [Period]) => {
			if (data.length) {
				periods = data;
				currentPeriod = periods.findIndex(
					(period) => period.start_date <= getDate() && period.end_date >= getDate()
				);
			} else {
				createThisBudgetPeriod();
			}
		});
	});
</script>

<div class="header">
	<h2>{$budget.name}</h2>
	<Button
		label="budget settings"
		href={`/app/budgets/${$budget.id}/settings`}
		icon="settings"
		iconOnly
		variant="secondary"
	/>
</div>

{#if periods}
	<div class="period-actions">
		<Button
			label="Previous Budget Period"
			icon="arrow-left"
			iconOnly
			disabled={currentPeriod === 0}
			on:click={() => currentPeriod--}
		/>
		<h3>{periods[currentPeriod].label}</h3>
		<Button
			label="Next Budget Period"
			icon="arrow-right"
			iconOnly
			on:click={() => {
				if (currentPeriod !== periods.length - 1) {
					currentPeriod++;
				} else {
					createNextPeriod();
				}
			}}
		/>
	</div>
	<BudgetPeriod period_id={periods[currentPeriod].id} />
{/if}

<style>
	.header {
		display: flex;
		justify-content: space-between;
		width: 100%;
	}
	.period-actions {
		width: 100%;
		display: flex;
		justify-content: space-between;
	}
</style>
