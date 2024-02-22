<script lang="ts">
	import { page } from '$app/stores';
	import { getBudget } from '@api/budget';
	import { getPeriodByDate, createPeriod, listPeriods } from '@api/period';
	import BudgetPeriod from '@components/BudgetPeriod.svelte';
	import Button from '@components/Button.svelte';
	import { onMount } from 'svelte';

	interface Period {
		id: number;
		start_date: Date;
		end_date: Date;
		label: string;
		budget: number;
	}

	let name = '';
	let type = '';
	let id = parseInt($page.params.id);
	let users: number[] = [];
	let owner: number | undefined = undefined;

	let today = new Date(Date.now());

	let period: Period;
	let currentPeriod: number;

	function createThisBudgetPeriod() {
		createPeriod(today, id).then((data: Period) => {
			periods.push(data);
			currentPeriod = periods.length - 1;
		});
	}

	let periods: [Period];

	onMount(() => {
		getBudget(id).then((data) => {
			name = data.name;
			type = data.type;
			users = data.users;
			owner = data.owner;
		});

		listPeriods(id).then((data: [Period]) => {
			if (data.length) {
				periods = data;
				currentPeriod = periods.length - 1;
				console.log(periods);
			} else {
				createThisBudgetPeriod();
			}
		});
	});
</script>

<div class="header">
	<h2>{name}</h2>
	<Button
		label="budget settings"
		href={`/app/budgets/${id}/settings`}
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
			on:click={() => currentPeriod++}
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
