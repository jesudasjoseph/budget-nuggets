<script lang="ts">
	import { isLoggedIn, APIToken, APITokenExpiry } from '../stores';
	import { goto } from '$app/navigation';

	function logOut(e: Event) {
		e.preventDefault();
		fetch('http://127.0.0.1:8000/auth/logoutall/', {
			method: 'POST',
			mode: 'cors',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Token ${$APIToken}`
			}
		}).then((response) => {
			if (response.status == 204) {
				console.log(response);
				APIToken.set('');
				APITokenExpiry.set('');
				goto('/');
			}
		});
	}
</script>

{#if $isLoggedIn}
	<nav><button on:click={logOut}>Logout</button></nav>
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
</style>
