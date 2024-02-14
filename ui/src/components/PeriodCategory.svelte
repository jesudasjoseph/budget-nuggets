<script lang="ts">
	import Button from '@components/Button.svelte';
	import { createEventDispatcher } from 'svelte';
	export let id: number;
	export let value: string;
	export let label: string;

	const dispatch = createEventDispatcher();
</script>

<div class="container">
	<p>{label}</p>

	<div class="right">
		<p>{value}</p>
		<Button
			variant="close"
			label="D"
			on:click={() => {
				dispatch('delete', { id });
			}}
		/>
	</div>
</div>

<style>
	.container {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		padding: 0.5rem;
		width: 20rem;
		background-color: var(--gray-7);
		border-radius: 5px;
	}
	.right {
		display: flex;
		flex-direction: row;
		justify-content: space-evenly;
		align-items: center;
		column-gap: 1rem;
	}

	p {
		font-size: var(--font-size-medium);
	}
</style>
