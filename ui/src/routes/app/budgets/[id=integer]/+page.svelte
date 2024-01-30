<script lang="ts">
	import { page } from '$app/stores';
	import { getBudget } from '@api/budget';
	import { onMount } from 'svelte';

	let name = '';
	let type = '';
	let id = parseInt($page.params.id);
	let users: number[] = [];
	let owner: number | undefined = undefined;

	onMount(() => {
		getBudget(id).then((data) => {
			name = data.name;
			type = data.type;
			users = data.users;
			owner = data.owner;
		});
	});
</script>

{name}
{type}
{id}
{users}
{owner}
