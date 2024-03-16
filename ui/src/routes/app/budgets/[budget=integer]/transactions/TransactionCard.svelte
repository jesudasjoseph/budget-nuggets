<script lang="ts">
	import type { PeriodCategory } from '@models/periods';
	import type { Budget } from '@models/budget';
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';

	export let id: number;
	export let value: string;
	export let merchant: string;
	export let date: string;
	export let categories: PeriodCategory[] = [];

	const budget: Writable<Budget> = getContext('budget');
</script>

<a href={`/app/budgets/${$budget.id}/transactions/${id}`}>
	<div class="left-section">
		<p class="value">${value}</p>
		<div>
			<p>{merchant}</p>
			<p>{date}</p>
		</div>
	</div>

	{#if categories.length}
		{#each categories as category}
			{category.category.label}
		{/each}
	{:else}
		Uncategorized
	{/if}
</a>

<style lang="scss">
	a {
		display: flex;
		justify-content: space-between;
		text-decoration: none;
		border-radius: 8px;
		background-color: var(--gray-7);
		padding: var(--space-sm);
		align-items: center;
		column-gap: var(--space-xs);
	}

	.left-section {
		display: flex;
		align-items: center;
		column-gap: var(--space-xs);
	}

	.value {
		font-size: var(--font-size-lg);
		color: var(--blue-1);
	}
</style>
