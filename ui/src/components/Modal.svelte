<script lang="ts">
	import { afterUpdate } from 'svelte';
	import { slide, fade } from 'svelte/transition';
	import { createEventDispatcher } from 'svelte';
	export let visible = false;

	const dispatch = createEventDispatcher();

	function onKeyDown(event: KeyboardEvent) {
		if (event.key == 'Escape') {
			visible = false;
			dispatch('cancel');
		}
	}

	afterUpdate(() => {
		if (!visible) {
			dispatch('reset');
		}
	});
</script>

<svelte:window on:keydown={onKeyDown} />

{#if visible}
	<div role="presentation" in:fade={{ delay: 100 }} on:click|self={() => (visible = false)} />
	<section role="dialog" in:fade={{ delay: 100 }}>
		<header><slot name="header" /></header>
		<slot />
		<footer><slot name="footer" /></footer>
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
		border-radius: 1rem;
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
</style>
