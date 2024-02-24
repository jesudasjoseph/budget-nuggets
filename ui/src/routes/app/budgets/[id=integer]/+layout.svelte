<script lang="ts">
	import { setContext, onMount } from 'svelte';
	import { writable, type Writable } from 'svelte/store';
	import { page } from '$app/stores';
	import { getBudget } from '@api/budget';
	import type { Budget } from '@models/budget';

	let budget: Writable<Budget | undefined> = writable();
	setContext('budget', budget);

	onMount(() => {
		getBudget(parseInt($page.params.id)).then((data) => {
			$budget = data;
		});
	});
</script>

{#if $budget}
	<slot />
{/if}
