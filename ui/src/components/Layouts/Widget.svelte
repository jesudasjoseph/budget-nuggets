<script lang="ts">
	export let title: string;
	export let headingLevel: 'h2' | 'h3' | 'h4' | 'h5' = 'h2';
</script>

<section>
	<header>
		{#if headingLevel === 'h2'}
			<h2>{title}</h2>
		{:else if headingLevel === 'h3'}
			<h3>{title}</h3>
		{:else if headingLevel === 'h4'}
			<h4>{title}</h4>
		{:else if headingLevel === 'h5'}
			<h5>{title}</h5>
		{/if}
	</header>
	<slot />
</section>

<style>
	header {
		padding-bottom: var(--space);
	}
	section {
		width: 100%;
		padding: var(--space);
		background-color: var(--gray-6);
		border-radius: 8px;
	}
</style>
