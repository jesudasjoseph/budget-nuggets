<script lang="ts">
	export let value: string | undefined = undefined;
	export let label: string;
	export let placeholder = '';
	export let hideLabel = false;
	export let required = false;
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	<input type="text" {placeholder} {required} bind:value />
</label>
