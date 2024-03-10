<script lang="ts">
	import PeriodCategory from '@components/PeriodCategory.svelte';

	export let id: number;
	export let value: string;
	export let merchant: string;
	export let date: string;
	export let categories: PeriodCategory[] = [];
</script>

<div>
	${value}
	{merchant}
	{date}
	{#if categories.length}
		{#each categories as category}
			{category.category.label}
		{/each}
	{:else}
		Uncategorized
	{/if}
</div>
