<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { deleteBudget } from '@api/budget';
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';
	import Widget from '@components/Layouts/Widget.svelte';
	import CategoriesSection from './components/CategoriesSection.svelte';

	let confirmationDialogOpen = false;
	let categories: any[];

	function onDeleteBudget() {
		deleteBudget(parseInt($page.params.id)).then(() => {
			goto('/app/budgets');
		});
	}
</script>

<div class="quick-actions">
	<Button label="Go to Budget" href={`/app/budgets/${$page.params.id}`} icon="arrow-right" />
</div>

<CategoriesSection />

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
	.quick-actions {
		width: 100%;
		display: flex;
		justify-content: end;
	}
</style>
