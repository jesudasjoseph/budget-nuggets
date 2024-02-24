<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { deletePeriodCategories, listPeriodCategories } from '@api/period';
	import PeriodCategory from '@components/PeriodCategory.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import { listCategories } from '@api/category';
	import AddPeriodCategoryButton from './AddPeriodCategoryButton.svelte';

	export let period_id: number;

	const budget_id: number = parseInt($page.params.id);

	let selectedPeriodCategory: number;

	let showConfirmationModal = false;

	let categories: any[];
	let budgetCategories: any[];

	function onDeleteCategory(id: number) {
		deletePeriodCategories(period_id, id)
			.then(() => {
				categories = categories.filter((periodCategory) => periodCategory.id !== id);
			})
			.catch();
	}

	function getCategories(periodId: number) {
		listPeriodCategories(periodId).then((responseData: PeriodCategory[]) => {
			categories = responseData;
		});
	}

	onMount(() => {
		listCategories(budget_id).then((data) => {
			budgetCategories = data;
		});
	});

	$: getCategories(period_id);
</script>

<ul>
	{#if categories}
		{#each categories as category}
			<PeriodCategory
				label={category.category.label}
				value={category.value}
				id={category.id}
				on:delete={(event) => {
					selectedPeriodCategory = event.detail.id;
					showConfirmationModal = true;
				}}
			/>
		{/each}
	{/if}
</ul>
<AddPeriodCategoryButton
	on:add={(event) => {
		categories.push(event.detail);
	}}
	period_categories={categories}
	{period_id}
	{budget_id}
/>

<ConfirmationModal
	label="Confirm"
	bind:visible={showConfirmationModal}
	on:ok={() => {
		onDeleteCategory(selectedPeriodCategory);
	}}
>
	Are you sure you want to remove this category?
</ConfirmationModal>

<style>
	ul {
		display: flex;
		flex-direction: column;
		justify-content: stretch;
		align-items: stretch;
		row-gap: 0.5rem;
		width: 100%;
	}
</style>
