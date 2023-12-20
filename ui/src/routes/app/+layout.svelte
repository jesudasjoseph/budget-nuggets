<script lang="ts">
	import { isLoggedIn, APIToken, APITokenExpiry } from '@/stores/auth';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { authenticatedAPICall } from '@api/util';
	import Button from '@components/Button.svelte';

	function logOut(e: Event) {
		e.preventDefault();
		authenticatedAPICall('POST', 'auth/logoutall/').then(() => {
			$APIToken = '';
			$APITokenExpiry = '';
			goto('/');
		});
	}

	/* $: if (!$isLoggedIn && !['/login'].includes($page.url.pathname)) {
		goto('/login');
	} */
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

	@media screen and (min-width: 1280px) {
		main {
			padding-left: 25%;
			padding-right: 25%;
		}
	}

	main div {
		position: relative;

		background-color: var(--secondary-background);
		display: flex;
		flex-direction: column;

		align-items: center;
		justify-content: stretch;

		width: 100%;
		height: 100%;
	}

	nav {
		padding: 1rem;
		background-color: rgba(0, 0, 0, 0.1);
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
</style>
