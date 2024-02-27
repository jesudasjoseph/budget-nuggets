<script lang="ts">
	import { onMount } from 'svelte';
	import { createCategoryAPI, listCategories } from '@api/category';
	import Button from '@components/Button.svelte';
	import Widget from '@components/Layouts/Widget.svelte';
	import CategoryCard from './CategoryCard.svelte';
	import CategoryModal from './CategoryModal.svelte';

	export let budgetId: number;

	let categories: any[];

	let openAddCategory = false;
	let label: string;
	let color: string;

	function onCreate() {
		createCategoryAPI(budgetId, label, color).then((data) => {
			categories.push(data);
			categories = categories;
		});
		openAddCategory = false;
	}

	onMount(() => {
		listCategories(budgetId).then((data) => {
			categories = data;
		});
	});
</script>

{#if categories}
	<Widget title="Budget Categories">
		<div class="category-widget">
			<ul>
				{#each categories as category}
					<li>
						<CategoryCard id={category.id} label={category.label} color={category.color} />
					</li>
				{/each}
			</ul>
			<Button label="Add Category" variant="primary" on:click={() => (openAddCategory = true)} />
		</div>
	</Widget>
{/if}

<CategoryModal
	title="Add Category"
	bind:label
	bind:color
	bind:visible={openAddCategory}
	on:submit={onCreate}
	on:cancel={() => {
		label = '';
		color = '';
	}}
/>

<style>
	.category-widget {
		display: flex;
		flex-direction: column;
		row-gap: var(--space);
	}
	ul {
		display: flex;
		flex-direction: column;
		row-gap: var(--space-xs);
	}
</style>
