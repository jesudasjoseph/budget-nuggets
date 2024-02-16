<script lang="ts">
	import { isLoggedIn, APIToken, APITokenExpiry } from '@/stores/auth';
	import { logoutallAPICall } from '@api/auth';
	import { fatalNavigationError } from '@stores/error';
	import { goto, beforeNavigate } from '$app/navigation';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	import Button from '@components/Button.svelte';
	import Navigation from '@components/Navigation.svelte';

	let loggingOut = false;

	function logOut(e: Event) {
		e.preventDefault();

		logoutallAPICall().then((data) => {
			loggingOut = true;
			goto('/');
			$APIToken = '';
			$APITokenExpiry = '';
		});
	}

	function redirectToLogin() {
		if (!['/', '/app/login', '/app/signup'].includes($page.url.pathname) && !loggingOut) {
			goto(`/app/login?ref=${$page.url.pathname}`);
		}
	}

	onMount(() => {
		if (!$isLoggedIn) {
			redirectToLogin();
		}
	});

	beforeNavigate(() => {
		$fatalNavigationError = false;
	});

	$: if (!$isLoggedIn) redirectToLogin();
</script>

{#if $isLoggedIn}
	<header>
		<h1>Budget Nuggets</h1>
		<Navigation>
			<a href="/app/dashboard">Dashboard</a>
			<a href="/app/budgets">Budgets</a>
			<Button label="Logout" variant="secondary" on:click={logOut} />
		</Navigation>
	</header>
{/if}
{#if !$fatalNavigationError}
	<main>
		<div>
			<slot />
		</div>
	</main>
{:else}
	<main class="error">
		<h2>404 Not Found!</h2>
	</main>
{/if}

<style>
	main {
		position: relative;
		height: 100%;

		padding-left: 1rem;
		padding-right: 1rem;
	}

	main.error {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 4rem;
	}

	main div {
		display: flex;
		flex-direction: column;

		align-items: center;
		justify-content: stretch;

		width: 100%;
		height: 100%;

		/* TODO: Remove */
		border: 1px solid purple;
	}

	header {
		padding: 1rem;
		background-color: rgba(0, 0, 0, 0.1);
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}

	h1 {
		font-size: var(--font-size-large);
		margin: 0;
	}

	/* desktop */
	@media screen and (min-width: 1280px) {
		main {
			padding-left: 20%;
			padding-right: 20%;
		}
	}
</style>
