<script lang="ts">
	import { page } from '$app/stores';
	import { getBudget } from '@api/budget';
	import { getPeriodByDate, createPeriod } from '@api/period';
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

	function createThisBudgetPeriod() {
		createPeriod(today, id).then((data: Period) => {
			period = data;
		});
	}

	onMount(() => {
		getBudget(id).then((data) => {
			name = data.name;
			type = data.type;
			users = data.users;
			owner = data.owner;
		});

		getPeriodByDate(today, id).then((data: [Period]) => {
			if (data.length) period = data[0];
			else createThisBudgetPeriod();
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

{#if period}
	<BudgetPeriod budget_id={parseInt($page.params.id)} period_id={period.id} label={period.label} />
{/if}

<style>
	.header {
		display: flex;
		justify-content: space-between;
		width: 100%;
	}
</style>
