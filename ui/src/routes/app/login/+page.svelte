<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import Button from '@components/Button.svelte';
	import { isLoggedIn } from '@stores/auth';
	import { loginAPICall } from '@api/auth';
	import TextInput from '@components/TextInput.svelte';

	const REF = $page.url.searchParams.get('ref') || '/app/dashboard';

	let email = '';
	let password = '';

	let loginForm: HTMLFormElement;
	function onLoginSubmit(event: SubmitEvent) {
		loginAPICall(email, password).then(() => {
			goto(REF);
		});
		event.preventDefault();
	}
	onMount(() => {
		if ($isLoggedIn) {
			goto(REF);
		}
	});
</script>

<div class="main">
	{#if $page.url.searchParams.get('ref')}
		<p>You are not logged in yet! Please log in to continue.</p>
	{/if}
	<form class="form-layout" on:submit={onLoginSubmit} bind:this={loginForm}>
		<h2>Login</h2>
		<TextInput label="Email" hideLabel placeholder="jane@example.com" required bind:value={email} />
		<TextInput
			label="Password"
			hideLabel
			placeholder="password"
			type="password"
			required
			bind:value={password}
		/>
		<div class="button-layout">
			<Button variant="primary" label="Login" type="submit" />
		</div>
		<p>Don't have an account yet? <a href="/app/signup">Signup here</a></p>
	</form>
	<Button variant="secondary" label="Back to homepage!" href="/" />
</div>

<style>
	.main {
		display: flex;
		flex-direction: column;
		row-gap: 3rem;
		width: 100%;
		padding: 2rem;
		height: 100%;
		justify-content: space-between;
		max-width: 30rem;
	}
	.form-layout {
		display: flex;
		flex-direction: column;
		row-gap: 1rem;
		width: 100%;
	}
	.form-layout input {
		width: 100%;
	}

	.button-layout {
		display: flex;
		flex-direction: column;
		row-gap: 1rem;
		width: 100%;
		justify-content: space-between;
	}
</style>
