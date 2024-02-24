<script lang="ts">
	import { setContext, onMount, getContext } from 'svelte';
	import { writable, type Writable } from 'svelte/store';

	import Button from '@components/Button.svelte';
	import { listPeriods } from '@api/period';
	import type { Period } from '@models/periods';
	import type { Budget } from '@models/budget';

	const periods: Writable<Period[] | undefined> = writable();
	setContext('periods', periods);

	const budget: Writable<Budget> = getContext('budget');

	onMount(() => {
		listPeriods($budget.id).then((response: Period[]) => {
			$periods = response;
		});
	});
</script>

{#if $periods}
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
	<slot />
{/if}

<style>
	.header {
		display: flex;
		justify-content: space-between;
		width: 100%;
	}
</style>
