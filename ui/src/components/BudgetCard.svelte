<script lang="ts">
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

<article>
	<a href={`app/budget/${id}`}>
		<h2>{name}</h2>
		<p>{BUDGET_TYPE_MAP[type]}</p>
	</a>
</article>

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
		padding: 0.2rem;
		padding-right: 0.5rem;
	}
	p {
		font-size: var(--font-size-small);
		color: var(--gray-2);
	}
</style>
