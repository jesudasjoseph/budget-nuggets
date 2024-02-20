<script lang="ts">
	import CategoryModal from '@/routes/app/budgets/[id=integer]/settings/components/CategoryModal.svelte';
	import { updateCategory } from '@api/category';
	import Button from '@components/Button.svelte';

	export let id: number;
	export let label: string;
	export let color: string | undefined = undefined;

	let updateLabel = label;
	let updateColor = color;

	let openEditModal = false;

	function onEdit() {
		openEditModal = false;
		updateCategory(id, updateLabel, updateColor).then((response) => {
			label = updateLabel;
			color = updateColor;
		});
	}
</script>

<div class="category-card" style:--color={color ? color : undefined}>
	<p class="card-label">{label}</p>
	<Button
		label={`edit ${label} category`}
		variant="secondary"
		icon="edit-2"
		iconOnly
		on:click={() => {
			openEditModal = true;
		}}
	/>
</div>

<CategoryModal
	title="Edit Category"
	bind:label={updateLabel}
	bind:color={updateColor}
	bind:visible={openEditModal}
	on:submit={onEdit}
	on:cancel={() => {
		updateLabel = label;
		updateColor = color;
	}}
/>

<style>
	.category-card {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		border-radius: 5px;
		padding: var(--space-xs);
		padding-left: var(--space-sm);
		border-left: 4px solid var(--color, var(--gray-8));
		background-color: var(--gray-8);
	}
	.card-label {
		font-size: var(--font-size-md);
	}
</style>
