<script lang="ts">
	import { listPeriodCategoriesAPI } from '@api/period';
	import Button from '@components/Button.svelte';
	import SelectInput from '@components/SelectInput.svelte';
	import type { Option } from '@models/general';
	import type { PeriodCategory } from '@models/periods';
	import { onMount } from 'svelte';

	export let periodId: number;
	export let value: string;

	let categories: PeriodCategory[] = [];
	let categoryOptions: Option[] = [];

	onMount(async () => {
		categories = await listPeriodCategoriesAPI(periodId);
		categoryOptions = categories.map((category: PeriodCategory) => {
			return { value: category.id.toString(), label: category.category.label };
		});
	});
</script>

<SelectInput label="Category" options={categoryOptions} bind:value />

<Button label="Add Category" />
