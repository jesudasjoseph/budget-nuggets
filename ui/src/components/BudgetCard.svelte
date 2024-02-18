<script lang="ts">
	import { fade } from 'svelte/transition';
	import Button from '@components/Button.svelte';

	export let id: number;
	export let name = 'No Name';
	export let type: string;

	const BUDGET_TYPE_MAP: Record<string, string> = {
		AN: 'Annual',
		MN: 'Monthly',
		BW: 'Biweekly',
		W: 'Weekly',
		EV: 'Event'
	};
</script>

<div transition:fade>
	<article>
		<a href={`/app/budgets/${id}`}>
			<h2>{name}</h2>
			<p>{BUDGET_TYPE_MAP[type]}</p>
		</a>
	</article>
	<Button icon="settings" iconOnly label={`${name} settings`} href={`budgets/${id}/settings`} />
</div>

<style>
	article {
		display: flex;
		background-color: var(--gray-6);
		box-shadow: 1px 2px 1px 0 var(--boxshadow-color);
		border-radius: 5px;
		width: 100%;
	}
	article:hover {
		background-color: var(--gray-7);
	}
	a {
		display: flex;
		flex-direction: row;
		align-items: baseline;
		justify-content: space-between;
		color: var(--primary-font-color);
		text-decoration: none;
		width: 100%;
		padding: var(--space-xs) var(--space-sm);
	}
	p {
		font-size: var(--font-size-sm);
		color: var(--gray-2);
	}
	h2 {
		font-size: var(--font-size-md);
	}
	div {
		display: flex;
		flex-direction: row;
		column-gap: var(--space-xs);
	}
</style>
