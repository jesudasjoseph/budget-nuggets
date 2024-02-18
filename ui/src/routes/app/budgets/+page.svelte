<script lang="ts">
	import Button from '@components/Button.svelte';
	import Modal from '@components/Modal.svelte';
	import BudgetCard from '@components/BudgetCard.svelte';
	import { createBudget, listBudgets } from '@api/budget';
	import type { Types } from '@models/budget';
	import { onMount } from 'svelte';
	import TextInput from '@components/TextInput.svelte';
	import SelectInput from '@components/SelectInput.svelte';

	let showAddBudgetModal = false;
	let name = '';
	let type: Types = 'MN';

	let budgets: any[] = [];

	function onAdd() {
		createBudget(name, type).then((budget) => {
			if (budget) {
				getBudgets();
			}
		});
		showAddBudgetModal = false;
	}

	function getBudgets() {
		listBudgets().then((data) => {
			if (data) {
				budgets = data;
			}
		});
	}

	onMount(() => {
		getBudgets();
	});
</script>

<ul>
	{#each budgets as budget}
		<li>
			<BudgetCard id={budget.id} name={budget.name} type={budget.type} />
		</li>
	{/each}
</ul>

<Button
	classes="add-budget"
	label="Add Budget"
	variant="primary"
	on:click={() => (showAddBudgetModal = true)}
/>

<Modal bind:visible={showAddBudgetModal}>
	<form on:submit={onAdd}>
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
</Modal>

<style>
	ul {
		display: flex;
		flex-direction: column;
		row-gap: 1rem;
		width: 100%;
	}
	:global(.add-budget) {
		position: fixed;
		bottom: var(--space-sm);
		right: var(--space-sm);
	}
	form {
		display: flex;
		flex-direction: column;
		row-gap: var(--space-sm);
	}
	.button-layout {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
</style>
