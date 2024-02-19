<script lang="ts">
	import { listCategories } from '@api/category';
	import { onMount } from 'svelte';
	import Button from '@components/Button.svelte';
	import SelectInput from './SelectInput.svelte';
	import TextInput from './TextInput.svelte';

	export let period_categories: any[];
	export let budget_id: number;
	let categories: { value: string; label: string }[] | undefined = undefined;

	let selectedCategory: string | undefined = undefined;

	let addingCategory = false;
	let showCreateCategoryModal = false;

	onMount(() => {
		listCategories(budget_id).then((data) => {
			categories = data.filter((value: any) => {
				!period_categories
					.filter((val) => {
						val.category.id;
					})
					.map((value) => {
						return { value: value.id, label: value.label };
					});
			});
		});
	});
</script>

{#if addingCategory && categories}
	{#if categories.length}
		<SelectInput label="Budget Categories" options={categories} bind:value={selectedCategory} />
	{:else}
		<p>Add Budget Category</p>
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
