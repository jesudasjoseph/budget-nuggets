<script lang="ts">
	import { listPeriodCategories } from '@api/period';
	import { onMount } from 'svelte';

	export let budget_id: number;
	export let period_id: number;
	export let label: string;

	let categories: [any];
	console.log(period_id);

	onMount(() => {
		listPeriodCategories(period_id).then((data) => {
			categories = data;
		});
	});
</script>

<h3>{label}</h3>

{#if categories}
	{#each categories as category}
		{category.category.label}
		{category.value}
	{/each}
{/if}
