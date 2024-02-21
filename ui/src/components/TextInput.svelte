<script lang="ts">
	export let value: string | undefined = undefined;
	export let label: string;
	export let placeholder = '';
	export let hideLabel = false;
	export let required = false;
	export let pattern: string | undefined = undefined;
	export let type: 'text' | 'password' = 'text';
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	{#if type === 'text'}
		<input type="text" {pattern} {placeholder} {required} bind:value />
	{:else}
		<input type="password" {pattern} {placeholder} {required} bind:value />
	{/if}
</label>

<style>
	label {
		display: flex;
		flex-direction: column;
		row-gap: var(--space-xxs);
	}
	input {
		border-radius: var(--input-border-radius);
		padding: var(--input-padding);
		width: 100%;
	}
</style>
