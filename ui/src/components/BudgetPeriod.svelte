<script lang="ts">
	import { onMount } from 'svelte';
	import { deletePeriodCategories, listPeriodCategories } from '@api/period';
	import PeriodCategory from '@components/PeriodCategory.svelte';

	export let budget_id: number;
	export let period_id: number;
	export let label: string;

	let categories: any[];
	console.log(period_id);

	function onDeleteCategory(id: number) {
		console.log(id);
		deletePeriodCategories(period_id, id)
			.then((response) => {
				if (response.ok)
					categories = categories.filter((periodCategory) => periodCategory.category.id != id);
			})
			.catch();
	}

	onMount(() => {
		listPeriodCategories(period_id).then((data) => {
			categories = data;
		});
	});
</script>

<h3>{label}</h3>

<div>
	{#if categories}
		{#each categories as category}
			<PeriodCategory
				label={category.category.label}
				value={category.value}
				id={category.id}
				on:delete={(event) => onDeleteCategory(event.detail.id)}
			/>
		{/each}
	{/if}
</div>

<style>
	div {
		display: flex;
		flex-direction: column;
		row-gap: 0.5rem;
		padding: 1rem;
	}
</style>
