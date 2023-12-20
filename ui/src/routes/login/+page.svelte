<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import Button from '../../components/Button.svelte';
	import { isLoggedIn } from '../../stores';
	import { loginAPICall } from '../../api/util';
	let username = '';
	let password = '';
	let showLoginModal = false;

	function login(e: Event) {
		e.preventDefault();
		loginAPICall(username, password).then(() => {
			goto('/dashboard');
		});
	}
	onMount(() => {
		if ($isLoggedIn) {
			goto('/dashboard');
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
		<Button variant="primary" label="Login" on:click={login} />
	</div>
</form>

<style lang="scss">
	@import '../../scss/global';

	form {
		display: flex;
		flex-direction: column;
	}
</style>
