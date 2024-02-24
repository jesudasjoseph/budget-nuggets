<script lang="ts">
	import { isLoggedIn } from '@/stores/auth';
	import { fatalNavigationError } from '@stores/error';
	import { goto, beforeNavigate } from '$app/navigation';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	import Header from '@components/Header.svelte';

	function redirectToLogin() {
		if (!['/', '/app/login', '/app/signup'].includes($page.url.pathname)) {
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
</script>

<div>
	<Header />
	{#if $fatalNavigationError}
		<main class="error">
			<h2>404</h2>
			<p>The page does not exist!</p>
		</main>
	{:else}
		<main>
			<slot />
		</main>
	{/if}
</div>

<style>
	div {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		overflow: auto;
	}
	main {
		position: relative;
		padding: var(--space);
		padding-top: var(--space-lg);
		display: flex;
		flex-direction: column;
		align-items: center;
		row-gap: var(--space-lg);
	}

	main.error {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding-top: 4rem;
	}

	/* desktop */
	@media screen and (min-width: 1280px) {
		main {
			padding-left: 20%;
			padding-right: 20%;
		}
	}
</style>
