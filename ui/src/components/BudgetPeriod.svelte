<script lang="ts">
	import { onMount } from 'svelte';
	import { deletePeriodCategories, listPeriodCategories } from '@api/period';
	import PeriodCategory from '@components/PeriodCategory.svelte';
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import Modal from '@components/Modal.svelte';
	import TextInput from '@components/TextInput.svelte';

	export let period_id: number;
	export let label: string;

	let selectedPeriodCategory: number;

	let showCreateCategoryModal = false;
	let showConfirmationModal = false;

	let categories: any[];

	function onDeleteCategory(id: number) {
		console.log(id);
		deletePeriodCategories(period_id, id)
			.then((response) => {
				if (response.ok)
					categories = categories.filter((periodCategory) => periodCategory.category.id != id);
			})
			.catch();
	}

	function onCreatePeriodCategory() {}

	onMount(() => {
		listPeriodCategories(period_id).then((data) => {
			categories = data;
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
<Button
	label="Add Category"
	full
	on:click={() => {
		showCreateCategoryModal = true;
	}}
/>

<!-- <Modal bind:visible={showCreateCategoryModal}>
	<form on:submit={onCreatePeriodCategory}>
		<h2>Add Budget</h2>
		<TextInput hideLabel label="Name" placeholder="Budget Name" required bind:value={name} />
		<SelectInput
			hideLabel
			label="Type"
			required
			bind:value={type}
			options={[
				{ value: 'AN', label: 'Annual' },
				{ value: 'MN', label: 'Monthly' },
				{ value: 'BW', label: 'Biweekly' },
				{ value: 'W', label: 'Weekly' },
				{ value: 'EV', label: 'Event (Single)' }
			]}
		/>
		<div class="button-layout">
			<Button variant="close" label="Close" on:click={() => (showAddBudgetModal = false)} />
			<Button variant="primary" label="Create" type="submit" />
		</div>
	</form>
</Modal> -->

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
