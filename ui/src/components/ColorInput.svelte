<script lang="ts">
	export let value: string | undefined;
	export let label: string;
	export let hideLabel = false;
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	<input type="color" bind:value />
</label>

<style>
	input {
		padding: 0;
		height: var(--space-lg);
		width: var(--space-xl);
	}
</style>
