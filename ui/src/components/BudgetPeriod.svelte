<script lang="ts">
	import { onMount } from 'svelte';
	import { deletePeriodCategories, listPeriodCategories } from '@api/period';
	import PeriodCategory from '@components/PeriodCategory.svelte';
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import Modal from '@components/Modal.svelte';
	import TextInput from '@components/TextInput.svelte';
	import SelectInput from './SelectInput.svelte';
	import { listCategories } from '@api/category';
	import AddPeriodCategoryButton from './AddPeriodCategoryButton.svelte';

	export let budget_id: number;
	export let period_id: number;
	export let label: string;

	let selectedPeriodCategory: number;
	let selectedCategory: string;

	let showCreateCategoryModal = false;
	let showConfirmationModal = false;
	let addingCategory = false;

	let categories: any[];
	let budgetCategories: any[];

	function onDeleteCategory(id: number) {
		deletePeriodCategories(period_id, id)
			.then((response) => {
				categories = categories.filter((periodCategory) => periodCategory.id !== id);
			})
			.catch();
	}

	function onCreatePeriodCategory() {}

	onMount(() => {
		listPeriodCategories(period_id).then((data) => {
			categories = data;
		});
		listCategories(budget_id).then((data) => {
			budgetCategories = data;
		});
	});
</script>

<h3>{label}</h3>

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
<AddPeriodCategoryButton period_categories={categories} {period_id} {budget_id} />

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
