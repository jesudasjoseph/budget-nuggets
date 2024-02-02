<script lang="ts">
	import { page } from '$app/stores';
	import { getBudget } from '@api/budget';
	import { getPeriodByDate, createPeriod } from '@api/period';
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

{name}
{type}
{id}
{users}
{owner}

{#if period}
	{period.label}
{/if}
