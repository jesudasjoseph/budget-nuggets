<script lang="ts">
	import { updateCategory } from '@api/category';
	import Button from '@components/Button.svelte';
	import Modal from '@components/Modal.svelte';
	import TextInput from '@components/TextInput.svelte';

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

	$: console.log(color);
</script>

<div class="category-card" style:--color={color ? color : undefined}>
	<p>{label}</p>
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

<Modal bind:visible={openEditModal}>
	<form on:submit={onEdit}>
		<TextInput label="Label" bind:value={updateLabel} />
		<label>
			<p>Color</p>
			<input type="color" bind:value={updateColor} />
		</label>
		<Button label="Save" variant="primary" type="submit" />
	</form>
</Modal>

<style>
	.category-card {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		border-radius: 5px;
		padding: var(--space-xs);
		padding-left: var(--space-sm);
		border: 2px solid var(--color, var(--gray-8));
		background-color: var(--gray-8);
	}
	p {
		font-size: var(--font-size-md);
	}
</style>
