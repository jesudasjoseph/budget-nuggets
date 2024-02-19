<script lang="ts">
	import { onMount } from 'svelte';
	import { createCategoryAPI, listCategories } from '@api/category';
	import type { Options } from '@models/general';
	import Button from '@components/Button.svelte';
	import SelectInput from './SelectInput.svelte';
	import TextInput from './TextInput.svelte';
	import { createPeriodCategoryAPI } from '@api/period';

	export let period_categories: any[];
	export let budget_id: number;
	export let period_id: number;
	let categories: Options[] | undefined = undefined;

	let selectedCategory: string | undefined = undefined;

	let addingCategory = false;
	let showCreateCategoryModal = false;

	let categoryName = '';
	let categoryValue = '0';

	function createCategory() {
		addingCategory = false;
		createCategoryAPI(budget_id, categoryName).then((data) => {
			createPeriodCategoryAPI(period_id, data.id, categoryValue);
		});
	}

	function createPeriodCategory() {
		addingCategory = false;
		createPeriodCategoryAPI(period_id, parseInt(selectedCategory), categoryValue);
	}

	onMount(() => {
		listCategories(budget_id).then((data) => {
			let rawCategories = data;
			if (period_categories) {
				rawCategories = data.filter((value: any) => {
					!period_categories.filter((val) => {
						val.category.id;
					});
				});
			}
			categories = rawCategories.map((value: any) => {
				return { value: value.id, label: value.label };
			});
		});
	});
</script>

{#if addingCategory && categories}
	{#if categories.length}
		<form on:submit={createPeriodCategory} on:reset={() => (addingCategory = false)}>
			<SelectInput label="Budget Categories" options={categories} bind:value={selectedCategory} />
			<TextInput
				label="Value"
				hideLabel
				required
				placeholder="$40.00"
				pattern="^[0-9]+(\.{1}[0-9]{1 - 2})?$"
				bind:value={categoryValue}
			/>
			<Button label="Create Category" icon="plus" iconOnly type="submit" />
			<Button label="Cancel Create Category" variant="delete" icon="x" iconOnly type="reset" />
		</form>
	{:else}
		<form on:submit={createCategory} on:reset={() => (addingCategory = false)}>
			<TextInput
				label="Category name"
				hideLabel
				required
				placeholder="category name"
				bind:value={categoryName}
			/>
			<TextInput
				label="Value"
				hideLabel
				required
				placeholder="$40.00"
				pattern="^[0-9]+(\.{1}[0-9]{1 - 2})?$"
				bind:value={categoryValue}
			/>
			<Button label="Create Category" icon="plus" iconOnly type="submit" />
			<Button label="Cancel Create Category" variant="delete" icon="x" iconOnly type="reset" />
		</form>
	{/if}
{:else}
	<Button
		label="Add Category"
		full
		on:click={() => {
			addingCategory = true;
		}}
	/>
{/if}
