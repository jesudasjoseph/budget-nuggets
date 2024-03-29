<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { getPeriodCategoryAPI, deletePeriodCategoryAPI } from '@api/period';
	import BackButton from '@components/BackButton.svelte';
	import Button from '@components/Button.svelte';
	import type { Period, PeriodCategory } from '@models/periods';
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { fade } from 'svelte/transition';
	import { listTransactions } from '@api/transactions';
	import type { Transaction } from '@models/transactions';
	import TransactionCard from '../../../../transactions/TransactionCard.svelte';

	const period: Writable<Period> = getContext('period');

	let category: PeriodCategory;
	let transactions: Transaction[] = [];

	const getBackURL = () => {
		return `/app/budgets/${$page.params.budget}/periods/${$page.params.period}`;
	};

	const deleteCategory = () => {
		deletePeriodCategoryAPI($period.id, category.id).then(() => {
			goto(getBackURL());
		});
	};

	$: if ($page.params.category) {
		getPeriodCategoryAPI($period.id, parseInt($page.params.category)).then(
			(response: PeriodCategory) => {
				category = response;
			}
		);
	}

	$: if (category) {
		listTransactions($period.budget, undefined, undefined, undefined, category.id).then(
			(response: Transaction[]) => {
				transactions = response;
			}
		);
	}
</script>

<div class="heading">
	<h3>
		{$period.label}
		{#if category}
			<span transition:fade> - {category.category.label}</span>
		{/if}
	</h3>
	<BackButton pageTitle="budget" urlOverride={getBackURL()} />
</div>
{#if category}
	<div class="widget" style:--bg={category.category.color} transition:fade>
		<div class="category-value">
			<p>
				$55.00 / ${category.value}
			</p>
		</div>
		<div class="category-transactions">
			{#each transactions as transaction}
				<TransactionCard
					id={transaction.id}
					date={transaction.date}
					value={transaction.value}
					merchant={transaction.merchant}
					categories={transaction.period_categories}
				/>
			{/each}
		</div>
		<Button label="Delete Category" variant="delete" on:click={deleteCategory} />
	</div>
{/if}

<style>
	.heading {
		display: flex;
		width: 100%;
		justify-content: space-between;
		align-items: center;
	}
	.widget {
		display: flex;
		flex-direction: column;
		row-gap: var(--space-sm);
		width: 100%;
		background-color: var(--gray-7);
		padding: var(--space);
		border-radius: 12px;
		border-top: 4px solid var(--bg);
	}
	.category-value {
		width: 100%;
		display: flex;
		justify-content: end;
	}
	.category-value p {
		font-size: var(--font-size-md);
	}
</style>
