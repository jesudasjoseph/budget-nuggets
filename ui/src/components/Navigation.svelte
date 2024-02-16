<script lang="ts">
	import Button from '@components/Button.svelte';

	let open = false;
</script>

<div>
	<Button
		label="Open Navigation"
		icon={open ? 'x' : 'menu'}
		iconOnly
		variant="secondary"
		on:click={() => {
			open = !open;
		}}
	/>

	{#if open}
		<nav>
			<slot />
		</nav>
	{/if}
</div>

<style>
	div {
		position: relative;
	}
	nav {
		position: absolute;
		top: 4rem;
		right: 0;
		z-index: 999;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		row-gap: 1rem;
		border-radius: 8px;
		padding: 1rem;
		background-color: var(--gray-7);
	}
</style>
