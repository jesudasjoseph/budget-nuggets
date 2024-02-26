<script lang="ts">
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { getPeriodCategoryAPI, deletePeriodCategoryAPI } from '@api/period';
	import BackButton from '@components/BackButton.svelte';
	import Button from '@components/Button.svelte';
	import type { Period, PeriodCategory } from '@models/periods';
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { fade, fly } from 'svelte/transition';

	const period: Writable<Period> = getContext('period');

	let category: PeriodCategory;

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
<Button label="Delete Category" variant="delete" on:click={deleteCategory} />
{#if category}
	<p transition:fade>
		{category.category.color}
		{category.value}
	</p>
{/if}
Transactions

<style>
	.heading {
		display: flex;
		width: 100%;
		justify-content: space-between;
		align-items: center;
	}
</style>
