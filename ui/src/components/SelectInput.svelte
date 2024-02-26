<script lang="ts">
	import type { Option } from '@models/general';

	export let value: string | undefined = undefined;
	export let label: string;
	export let hideLabel = false;
	export let required = false;
	export let options: Option[];
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	<select {required} bind:value>
		{#each options as option}
			<option value={option.value}>{option.label}</option>
		{/each}
	</select>
</label>

<style>
	select {
		border-radius: var(--input-border-radius);
		padding: var(--input-padding);
		color: var(--blue-0);
		background-color: var(--gray-7);
		border: 3px solid var(--gray-5);
	}
</style>
