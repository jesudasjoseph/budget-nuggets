<script lang="ts">
	import { getContext } from 'svelte';
	import { fade } from 'svelte/transition';
	import type { Writable } from 'svelte/store';
	import { page } from '$app/stores';

	import { listPeriodCategoriesAPI, createPeriodCategoryAPI } from '@api/period';
	import { listCategories } from '@api/category';
	import type { Period, PeriodCategory } from '@models/periods';
	import type { Budget } from '@models/budget';
	import type { Category } from '@models/categories';
	import type { Option } from '@models/general';

	import PeriodHeader from './components/PeriodHeader.svelte';
	import PeriodCategoryCard from './components/PeriodCategoryCard.svelte';
	import Button from '@components/Button.svelte';
	import SelectInput from '@components/SelectInput.svelte';
	import TextInput from '@components/TextInput.svelte';

	const budget: Writable<Budget> = getContext('budget');
	const period: Writable<Period> = getContext('period');
	const periods: Writable<Period[]> = getContext('periods');

	let periodCategories: PeriodCategory[] = [];
	let categories: Category[] = [];
	let availableCategories: Option[] = [];

	let newValue = '';
	let newCategory = '';

	const addCategory = () => {
		console.log('hello');
		createPeriodCategoryAPI($period.id, parseInt(newCategory), newValue).then(
			(response: PeriodCategory) => {
				periodCategories = [...periodCategories, response];
			}
		);
	};

	$: if ($period) {
		listPeriodCategoriesAPI($period.id).then((response: PeriodCategory[]) => {
			periodCategories = response;
		});
		listCategories($budget.id).then((response: Category[]) => {
			categories = response;
		});
	}

	const updateAvaialableCategories = () => {
		availableCategories = categories
			.filter((category: Category) => {
				const list = periodCategories.filter((periodCategory: PeriodCategory) => {
					if (category.id == periodCategory.category.id) return true;
				});
				return !list.length;
			})
			.map((category: Category) => {
				return { value: category.id.toString(), label: category.label } as Option;
			});
		if (availableCategories.length) newCategory = availableCategories[0].value;
		newValue = '';
	};

	$: if (periodCategories && categories.length) {
		updateAvaialableCategories();
	}
</script>

<PeriodHeader period={$period} periods={$periods} budgetId={$budget.id} />

{#if periodCategories.length}
	<div class="category-list" transition:fade>
		{#each periodCategories as periodCategory}
			<PeriodCategoryCard
				id={periodCategory.id}
				value={periodCategory.value}
				label={periodCategory.category.label}
				color={periodCategory.category.color}
				referer={`${$page.url}`}
			/>
		{/each}
	</div>
{/if}
{#if availableCategories.length}
	<div class="actions" transition:fade>
		<SelectInput
			label="New Category"
			hideLabel
			options={availableCategories}
			bind:value={newCategory}
		/>
		<TextInput label="Category Value" placeholder="00.00" hideLabel bind:value={newValue} />
		<Button label="Add category" variant="secondary" on:click={addCategory} />
	</div>
{/if}

<style>
	.category-list {
		display: flex;
		flex-direction: column;
		width: 100%;
		row-gap: var(--space-sm);
	}
	.actions {
		display: flex;
		width: 100%;
		column-gap: var(--space);
	}
</style>
