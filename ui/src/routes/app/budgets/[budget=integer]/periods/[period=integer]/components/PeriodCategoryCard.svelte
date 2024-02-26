<script lang="ts">
	import Drawer from '@components/Drawer.svelte';

	export let id: number;
	export let value: string;
	export let label: string;
	export let color: string;
	export let referer: string;

	let openDialog = false;
</script>

<a style:--color={color} href={`${referer}/categories/${id}`}>
	<span class="label">
		{label}
	</span>
	<span class="value">
		${value}
	</span>
</a>

<Drawer bind:open={openDialog}>{value}{id}{label}{color}</Drawer>

<style>
	a {
		appearance: none;
		text-decoration: none;
		border-left: 4px solid var(--color);
		border-radius: 8px;
		background-color: var(--gray-6);
		color: var(--gray-0);
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: var(--space-xs);
	}

	a:hover {
		background-color: var(--gray-5);
	}

	.label {
		font-size: var(--font-size-lg);
	}
	.value {
		font-size: var(--font-size-md);
	}
</style>
