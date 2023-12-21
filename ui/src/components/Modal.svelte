<script lang="ts">
	import { afterUpdate } from 'svelte';
	import { slide, fade } from 'svelte/transition';
	import { createEventDispatcher } from 'svelte';
	export let visible: Boolean = false;

	const dispatch = createEventDispatcher();

	function onKeyDown(event: KeyboardEvent) {
		if (event.key == 'Escape') visible = false;
	}

	afterUpdate(() => {
		if (!visible) {
			dispatch('reset');
		}
	});
</script>

<svelte:window on:keydown={onKeyDown} />

{#if visible}
	<div role="presentation" in:fade={{ delay: 100 }} on:click|self={() => (visible = false)}>
		<section role="dialog" in:fade={{ delay: 100 }}>
			<slot />
		</section>
	</div>
{/if}

<style>
	div {
		position: absolute;
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
		top: 50%;

		transform: translateY(-50%) translateX(-50%);
	}
</style>
