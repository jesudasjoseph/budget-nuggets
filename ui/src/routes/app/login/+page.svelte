<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import Button from '@components/Button.svelte';
	import { isLoggedIn } from '@/stores/auth';
	import { loginAPICall } from '@api/util';
	let username = '';
	let password = '';
	let showLoginModal = false;

	function login(e: Event) {
		e.preventDefault();
		loginAPICall(username, password).then(() => {
			goto('/app/dashboard');
		});
	}
	onMount(() => {
		if ($isLoggedIn) {
			goto('/app/dashboard');
		}
	});
</script>

<form>
	<h2>Login</h2>
	<label>
		<span class="sr-only">Username</span>
		<input type="text" placeholder="Username" bind:value={username} />
	</label>
	<label>
		<span class="sr-only">Password</span>
		<input type="password" placeholder="Password" bind:value={password} />
	</label>
	<div class="button-layout">
		<Button variant="close" label="Close" on:click={() => (showLoginModal = false)} />
		<Button classes="login-button" variant="primary" label="Login" on:click={login} />
	</div>
</form>

<style>
	form {
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: stretch;
		justify-content: end;
		row-gap: 0.5rem;
		padding-bottom: 1rem;
	}

	form .button-layout {
		display: flex;
		align-items: stretch;

		column-gap: 0.5rem;
	}

	:global(form .button-layout .login-button) {
		flex-grow: 2;
	}
</style>
