<script lang="ts">
	export let value: string | undefined = undefined;
	export let label: string;
	export let placeholder = '';
	export let hideLabel = false;
	export let required = false;
	export let pattern: string | undefined = undefined;
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	<input type="text" {pattern} {placeholder} {required} bind:value />
</label>
