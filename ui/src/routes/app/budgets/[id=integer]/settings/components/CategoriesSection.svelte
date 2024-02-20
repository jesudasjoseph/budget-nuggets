<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { createCategoryAPI, listCategories } from '@api/category';
	import Button from '@components/Button.svelte';
	import Widget from '@components/Layouts/Widget.svelte';
	import CategoryCard from '@components/Category/CategoryCard.svelte';
	import CategoryModal from './CategoryModal.svelte';

	let categories: any[];

	let openAddCategory = false;
	let label: string;
	let color: string;

	function onCreate() {
		createCategoryAPI(parseInt($page.params.id), label, color).then((data) => {
			categories.push(data);
			categories = categories;
		});
		openAddCategory = false;
	}

	onMount(() => {
		listCategories(parseInt($page.params.id)).then((data) => {
			categories = data;
		});
	});
</script>

<Widget title="Budget Categories">
	{#if categories}
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
	{/if}
</Widget>

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
