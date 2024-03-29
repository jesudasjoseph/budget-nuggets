<script lang="ts">
	import { getDateString } from '@/utils';
	import TextInput from '@components/TextInput.svelte';
	import Button from '@components/Button.svelte';
	import CategorySelector from './CategorySelector.svelte';
	import { getContext } from 'svelte';
	import type { Period } from '@models/periods';
	import type { Budget } from '@models/budget';
	import type { Writable } from 'svelte/store';
	import { createTransaction } from '@api/transactions';

	let category: string;
	let date: string = getDateString(new Date());
	let notes: string;
	let merchant: string;
	let value: string;

	const period: Writable<Period> = getContext('period');
	const budget: Writable<Budget> = getContext('budget');

	const onSave = async () => {
		const transaction = await createTransaction(
			$budget.id,
			$period.id,
			value,
			merchant,
			notes,
			date,
			[{ period_category: category, value }]
		);
	};

	$: console.log(date);
</script>

<form>
	<TextInput label="Amount" variant="currency" bind:value />
	<TextInput label="Merchant" bind:value={merchant} />
	<TextInput label="Notes" bind:value={notes} />
	<TextInput label="Date" type="date" bind:value={date} />
	<CategorySelector periodId={$period.id} bind:value={category} />
	<Button type="submit" label="Save" on:click={onSave} />
</form>

<style>
	form {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: stretch;
		row-gap: var(--space);
	}
</style>
