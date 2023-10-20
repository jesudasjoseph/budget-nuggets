<script lang="ts">
	import { isLoggedIn, APIToken, APITokenExpiry } from '../stores';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { authenticatedAPICall } from '../api/util';
	import Button from '../components/Button.svelte';
	import { onMount } from 'svelte';

	function logOut(e: Event) {
		e.preventDefault();
		authenticatedAPICall('POST', 'auth/logoutall/').then(() => {
			$APIToken = '';
			$APITokenExpiry = '';
			goto('/');
		});
	}

	$: if (!$isLoggedIn && !['/login'].includes($page.url.pathname)) {
		goto('/login');
	}
</script>

{#if $isLoggedIn}
	<nav><Button label="Logout" variant="secondary" on:click={logOut} /></nav>
{/if}

<main>
	<slot />
</main>

<style lang="scss">
	@import '../scss/variables';
	@import '../scss/reset';

	main {
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
