<script lang="ts">
	import Button from '@components/Button.svelte';
	import ConfirmationModal from '@components/Modals/ConfirmationModal.svelte';

	import { createEventDispatcher } from 'svelte';
	export let id: number;
	export let value: string;
	export let label: string;

	const dispatch = createEventDispatcher();

	let showConfirmationModal = false;
</script>

<li>
	<p>{label}</p>

	<div>
		<p>${value}</p>
		<Button
			variant="delete"
			icon="x"
			iconOnly
			label="Delete"
			on:click={() => dispatch('delete', { id })}
		/>
	</div>
</li>

<style>
	li {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		padding: 0.5rem;
		width: 100%;
		background-color: var(--gray-7);
		border-radius: 5px;
	}
	div {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
		align-items: center;
		column-gap: 1rem;
	}

	p {
		font-size: var(--font-size);
	}
</style>
