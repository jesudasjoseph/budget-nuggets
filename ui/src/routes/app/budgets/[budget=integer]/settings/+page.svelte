<script lang="ts">
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { fade } from 'svelte/transition';
	import { goto } from '$app/navigation';

	import { deleteBudget } from '@api/budget';
	import type { Budget } from '@models/budget';

	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import Widget from '@components/Layouts/Widget.svelte';
	import Button from '@components/Button.svelte';

	import CategoriesSection from './components/CategoriesSection.svelte';

	let confirmationDialogOpen = false;
	const budget: Writable<Budget> = getContext('budget');

	function onDeleteBudget() {
		deleteBudget($budget.id).then(() => {
			goto('/app/budgets');
		});
	}
</script>

<div class="page-header">
	<h2>{$budget.name} - Settings</h2>
	<Button label="Go to Budget" href={`/app/budgets/${$budget.id}/periods`} icon="arrow-right" />
</div>

<CategoriesSection budgetId={$budget.id} />

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
	.page-header {
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
</style>
