<script lang="ts">
	import { onMount, getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { listTransactions } from '@api/transactions';
	import type { Budget } from '@models/budget';
	import type { Transaction } from '@models/transactions';
	import Button from '@components/Button.svelte';

	const budget: Writable<Budget> = getContext('budget');
	let transactions: Transaction[] = [];

	onMount(async () => {
		transactions = await listTransactions($budget.id);
	});
</script>

<h2>All Transactions</h2>

{#each transactions as transaction}
	{transaction.id}
	{transaction.date}
{/each}

<Button label="Add transaction" />
