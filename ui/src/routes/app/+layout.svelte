<script lang="ts">
	import { isLoggedIn, APIToken, APITokenExpiry } from '@/stores/auth';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { authenticatedAPICall } from '@api/util';
	import Button from '@components/Button.svelte';
	import { onMount } from 'svelte';

	let loggingOut = false;

	function logOut(e: Event) {
		e.preventDefault();

		authenticatedAPICall('POST', 'auth/logoutall/').then(() => {
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

	$: if (!$isLoggedIn) redirectToLogin();
</script>

{#if $isLoggedIn}
	<nav><Button label="Logout" variant="secondary" on:click={logOut} /></nav>
{/if}
<main>
	<div>
		<slot />
	</div>
</main>

<style>
	main {
		height: 100%;

		padding-left: 1rem;
		padding-right: 1rem;
	}

	/* desktop */
	@media screen and (min-width: 1280px) {
		main {
			padding-left: 20%;
			padding-right: 20%;
		}
	}

	main div {
		position: relative;
		display: flex;
		flex-direction: column;

		align-items: center;
		justify-content: stretch;

		width: 100%;
		height: 100%;

		/* TODO: Remove */
		border: 1px solid purple;
	}

	nav {
		padding: 1rem;
		background-color: rgba(0, 0, 0, 0.1);
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
</style>
