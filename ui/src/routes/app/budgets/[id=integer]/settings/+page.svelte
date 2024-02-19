<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { deleteBudget } from '@api/budget';
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import Widget from '@components/Layouts/Widget.svelte';
	import { onMount } from 'svelte';
	import { listCategories } from '@api/category';
	import CategoryCard from '@components/Category/CategoryCard.svelte';
	import Modal from '@components/Modal.svelte';
	import TextInput from '@components/TextInput.svelte';

	let confirmationDialogOpen = false;
	let categories: any[];

	function onDeleteBudget() {
		deleteBudget(parseInt($page.params.id)).then(() => {
			goto('/app/budgets');
		});
	}

	onMount(() => {
		listCategories(parseInt($page.params.id)).then((data) => {
			categories = data;
		});
	});
</script>

<Widget title="Budget Categories">
	{#if categories}
		<div class="category-widget">
			<Button label="Add Category" variant="primary" />
			<ul>
				{#each categories as category}
					<li>
						<CategoryCard id={category.id} label={category.label} color={category.color} />
					</li>
				{/each}
			</ul>
		</div>
	{/if}
</Widget>

<Modal>
	<h2 slot="header">Add Category</h2>
	<form />
</Modal>

<Widget title="Delete Budget">
	<Button label="Delete Budget" variant="delete" on:click={() => (confirmationDialogOpen = true)} />
</Widget>

<ConfirmationModal
	bind:visible={confirmationDialogOpen}
	label="Delete Budget"
	on:ok={onDeleteBudget}
>
	<p>
		Are you sure you want to delete this budget and all items related to it? This includes all
		transactions.
	</p>
</ConfirmationModal>

<style>
	.category-widget {
		display: flex;
		flex-direction: column;
		row-gap: var(--space);
	}
</style>
