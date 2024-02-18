<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { deleteBudget } from '@api/budget';
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';

	let confirmationDialogOpen = false;

	function onDeleteBudget() {
		deleteBudget(parseInt($page.params.id)).then(() => {
			goto('/app/budgets');
		});
	}
</script>

<Button label="Delete Budget" on:click={() => (confirmationDialogOpen = true)} />

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
