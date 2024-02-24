<script lang="ts">
	import { setContext, onMount } from 'svelte';
	import { writable, type Writable } from 'svelte/store';
	import { afterNavigate } from '$app/navigation';
	import { page } from '$app/stores';

	import { getBudgetAPI } from '@api/budget';
	import type { Budget } from '@models/budget';

	const budget: Writable<Budget | undefined> = writable();
	setContext('budget', budget);

	const getBudget = () => {
		getBudgetAPI(parseInt($page.params.budget)).then((data) => {
			$budget = data;
		});
	};

	onMount(() => {
		getBudget();
	});

	afterNavigate(() => {
		if (parseInt($page.params.budget) != $budget?.id) {
			getBudget();
		}
	});
</script>

{#if $budget}
	<slot />
{/if}
