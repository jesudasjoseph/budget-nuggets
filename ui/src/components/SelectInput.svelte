<script lang="ts">
	import type { Options } from '@models/general';

	export let value: string | undefined = undefined;
	export let label: string;
	export let hideLabel = false;
	export let required = false;
	export let options: Options[];
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
	}
</style>
