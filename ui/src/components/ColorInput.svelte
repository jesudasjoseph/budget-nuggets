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
		height: calc(var(--space-sm) + var(--space-sm) + var(--font-size-md));
		width: var(--space-xl);
		border: 3px solid var(--gray-5);
		border-radius: var(--input-border-radius);
	}
</style>
