<script lang="ts">
	import Button from './Button.svelte';

	export let pageTitle: string;
	export let urlOverride: string | undefined = undefined;
</script>

{#if urlOverride}
	<Button label={`Go back to ${pageTitle}`} icon="arrow-right" href={urlOverride} />
{:else}
	<Button
		label={`Back to ${pageTitle}`}
		icon="arrow-right"
		on:click={() => {
			history.back();
		}}
	/>
{/if}
