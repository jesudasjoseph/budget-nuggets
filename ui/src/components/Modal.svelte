<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	export let visible = false;
	export let variant: 'default' | 'form' = 'default';

	const dispatch = createEventDispatcher();

	function onKeyDown(event: KeyboardEvent) {
		if (event.key == 'Escape') {
			visible = false;
			dispatch('cancel');
		}
	}
</script>

<svelte:window on:keydown={onKeyDown} />

{#if visible}
	<div
		role="presentation"
		on:click|self={() => {
			visible = false;
			dispatch('cancel');
		}}
	/>
	<section role="dialog">
		<header><slot name="header" /></header>
		{#if variant === 'form'}
			<form on:submit>
				<slot />
			</form>
		{:else}
			<slot />
			<footer><slot name="footer" /></footer>
		{/if}
	</section>
{/if}

<style>
	div {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: rgba(100, 100, 100, 0.5);
	}
	section {
		position: absolute;
		background-color: var(--secondary-background);
		border-radius: 8px;
		left: 50%;
		top: 2rem;

		transform: translateX(-50%);
		padding: 1rem;
	}
	header {
		padding-bottom: 1rem;
	}
	footer {
		padding-top: 1rem;
	}
	form {
		display: flex;
		flex-direction: column;
		row-gap: var(--space);
	}
</style>
