<script lang="ts">
	import { slide, fade } from 'svelte/transition';
	export let open = false;
</script>

<svelte:window
	on:keydown={(event) => {
		if (event.key === 'Escape') open = false;
	}}
/>

{#if open}
	<div class="backdrop" transition:fade role="presentation" on:click={() => (open = false)} />
	<div class="drawer" transition:slide={{ axis: 'y' }}>
		<slot />
	</div>
{/if}

<style>
	.backdrop {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: rgba(100, 100, 100, 0.5);
	}
	.drawer {
		position: fixed;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: var(--gray-8);
		padding: var(--space-md);
	}
</style>
