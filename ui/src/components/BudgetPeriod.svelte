<script lang="ts">
	import { onMount } from 'svelte';

	export let budget_id: number;
	export let period_id: number;
	export let label: string;

	onMount(() => {});
</script>

<h3>{label}</h3>
