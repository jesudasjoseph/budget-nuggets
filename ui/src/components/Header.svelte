<script lang="ts">
	import { goto } from '$app/navigation';
	import { isLoggedIn, APIToken, APITokenExpiry } from '@/stores/auth';
	import { logoutallAPICall } from '@api/auth';
	import Button from '@components/Button.svelte';

	export let title = 'Budget Nuggets';
	let open = false;

	function logOut(e: Event) {
		e.preventDefault();

		logoutallAPICall().then((data) => {
			goto('/app/login');
			$APIToken = '';
			$APITokenExpiry = '';
		});
	}

	function onKeyDown(event: KeyboardEvent) {
		if (event.key == 'Escape') {
			open = false;
		}
	}
</script>

<svelte:window on:keydown={onKeyDown} />

{#if $isLoggedIn}
	<header>
		<h1>{title}</h1>
		<Button
			label="Open Navigation"
			icon={open ? 'x' : 'menu'}
			iconOnly
			variant="secondary"
			on:click={() => {
				open = !open;
			}}
		/>

		{#if open}
			<nav on:click={() => (open = false)}>
				<Button label="Dashboard" href="/app/dashboard" />
				<Button label="Budgets" href="/app/budgets" />
				<Button label="Logout" variant="secondary" on:click={logOut} />
			</nav>
		{/if}
	</header>
{/if}

<style>
	header {
		position: relative;
		padding: 1rem;
		background-color: rgba(0, 0, 0, 0.1);
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
	h1 {
		font-size: var(--font-size-lg);
		margin: 0;
	}
	nav {
		position: absolute;
		top: calc(100% + 1rem);
		right: 1rem;
		z-index: 999;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		row-gap: 1rem;
		border-radius: 8px;
		padding: 1rem;
		background-color: var(--gray-7);
	}
</style>
