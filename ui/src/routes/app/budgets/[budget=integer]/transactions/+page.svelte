<script lang="ts">
	import { onMount, getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { listTransactions } from '@api/transactions';
	import type { Budget } from '@models/budget';
	import type { Transaction } from '@models/transactions';
	import Button from '@components/Button.svelte';

	import TransactionCard from './TransactionCard.svelte';

	const budget: Writable<Budget> = getContext('budget');
	let transactions: Transaction[] = [];

	onMount(async () => {
		transactions = await listTransactions($budget.id);
	});
</script>

<h2>All Transactions</h2>

<section>
	{#each transactions as transaction}
		<TransactionCard
			id={transaction.id}
			value={transaction.value}
			merchant={transaction.merchant}
			date={transaction.date}
			categories={transaction.period_categories}
		/>
	{/each}
</section>

<Button label="Add transaction" />

<style lang="scss">
	section {
		display: flex;
		flex-direction: column;
		row-gap: var(--space);
	}
</style>
