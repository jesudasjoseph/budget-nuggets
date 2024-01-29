<script lang="ts">
	import Button from '@components/Button.svelte';
	import Modal from '@components/Modal.svelte';
	import BudgetCard from '@components/BudgetCard.svelte';
	import { createBudget, listBudgets } from '@api/budget';
	import type { Types } from '@models/budget';
	import { onMount } from 'svelte';

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

<Button label="Add Budget" variant="primary" on:click={() => (showAddBudgetModal = true)} />

<ul>
	{#each budgets as budget}
		<li>
			<BudgetCard id={budget.id} name={budget.name} type={budget.type} />
		</li>
	{/each}
</ul>

<Modal bind:visible={showAddBudgetModal}>
	<form class="form-layout" on:submit={onAdd}>
		<h2>Add Budget</h2>
		<label>
			<span class="sr-only">Name</span>
			<input type="text" placeholder="annual budget" required bind:value={name} />
		</label>
		<label>
			<span class="sr-only">Type</span>
			<select bind:value={type}>
				<option value="AN">Annual</option>
				<option value="MN">Monthly</option>
				<option value="BW">Biweekly</option>
				<option value="W">Weekly</option>
				<option value="EV">Event (Single)</option>
			</select>
		</label>
		<div class="button-layout">
			<Button variant="close" label="Close" on:click={() => (showAddBudgetModal = false)} />
			<Button variant="primary" label="Login" type="submit" />
		</div>
	</form>
</Modal>

<style>
	ul {
		display: flex;
		flex-direction: column;
		row-gap: 1rem;
		width: 100%;
		padding: 1rem;
	}
</style>
