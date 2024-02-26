<script lang="ts">
	import { page, navigating } from '$app/stores';
	import { getPeriodCategoryAPI } from '@api/period';
	import BackButton from '@components/BackButton.svelte';
	import type { Period, PeriodCategory } from '@models/periods';
	import { getContext } from 'svelte';
	import type { Writable } from 'svelte/store';
	import { fade } from 'svelte/transition';

	const period: Writable<Period> = getContext('period');

	let category: PeriodCategory;

	$: if ($page.params.category) {
		getPeriodCategoryAPI($period.id, parseInt($page.params.category)).then(
			(response: PeriodCategory) => {
				category = response;
			}
		);
	}

	$: console.log($navigating);
	$: console.log($page);
</script>

<div>
	<h3>
		{$period.label}
		{#if category}
			<span transition:fade> - {category.category.label}</span>
		{/if}
	</h3>
	<BackButton pageTitle="budget" />
</div>

{#if category}
	<p transition:fade>
		{category.category.color}
		{category.value}
	</p>
{/if}
Transactions

<style>
	div {
		display: flex;
		width: 100%;
		justify-content: space-between;
		align-items: center;
	}
</style>
