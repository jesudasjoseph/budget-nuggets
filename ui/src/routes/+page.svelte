<script lang="ts">
	import { APIToken, APITokenExpiry, isLoggedIn } from '@/stores/auth';
	import { goto } from '$app/navigation';
	import Button from '@components/Button.svelte';
	import Modal from '@components/Modal.svelte';
	import { onMount } from 'svelte';
	import { loginAPICall } from '@api/util';
	let showLoginModal = false;
	let showCreateAccountModal = false;
	let username = '';
	let password = '';

	let create_username = '';
	let create_email = '';
	let create_firstname = '';
	let create_lastname = '';
	let create_password = '';

	function resetLoginModal() {
		username = '';
		password = '';
	}

	function resetCreateAccountModal() {}

	function createAccount() {}

	let loginForm: HTMLFormElement;
	function onLoginSubmit(event: SubmitEvent) {
		loginAPICall(username, password).then(() => {
			goto('/app/dashboard');
		});
		event.preventDefault();
	}

	onMount(() => {
		if ($isLoggedIn) {
			goto('/app/dashboard');
		}
	});
</script>

<div class="main">
	<h1>Budget Nuggets.</h1>
	<p>A simple budgeting app</p>
	<div id="options">
		<Button
			variant="primary"
			type="submit"
			label="Login"
			on:click={() => (showLoginModal = true)}
		/>
		<Button
			variant="secondary"
			label="Create Account"
			on:click={() => (showCreateAccountModal = true)}
		/>
	</div>
</div>
<Modal bind:visible={showLoginModal} on:reset={resetLoginModal}>
	<form class="form-layout" on:submit={onLoginSubmit} bind:this={loginForm}>
		<h2>Login</h2>
		<label>
			<span class="sr-only">Username</span>
			<input type="text" placeholder="Username" required bind:value={username} />
		</label>
		<label>
			<span class="sr-only">Password</span>
			<input type="password" placeholder="Password" required bind:value={password} />
		</label>
		<div class="button-layout">
			<Button variant="close" label="Close" on:click={() => (showLoginModal = false)} />
			<Button variant="primary" label="Login" type="submit" />
		</div>
	</form>
</Modal>
<Modal bind:visible={showCreateAccountModal} on:reset={resetCreateAccountModal}>
	<form class="form-layout">
		<h2>Create User</h2>
		<label>
			<span class="sr-only">Username</span>
			<input type="text" placeholder="Username" bind:value={create_username} />
		</label>
		<label>
			<span class="sr-only">First Name</span>
			<input type="text" placeholder="Firt Name" bind:value={create_firstname} />
		</label>
		<label>
			<span class="sr-only">Last Name</span>
			<input type="text" placeholder="Last Name" bind:value={create_lastname} />
		</label>
		<label>
			<span class="sr-only">Email</span>
			<input type="email" placeholder="Email" bind:value={create_email} />
		</label>
		<label>
			<span class="sr-only">Password</span>
			<input type="password" placeholder="Password" bind:value={create_password} />
		</label>
		<div class="button-layout">
			<Button variant="close" label="Close" on:click={() => (showCreateAccountModal = false)} />
			<Button variant="primary" label="Login" type="submit" on:click={createAccount} />
		</div>
	</form>
</Modal>

<style>
	.main {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
		padding: 10rem 2rem 2rem;
		height: 100%;
		width: 100%;
	}

	#options {
		display: flex;
		row-gap: 1rem;
		flex-direction: column;
		width: 100%;
	}

	.form-layout {
		display: flex;
		flex-direction: column;
		row-gap: 1rem;
		width: 100%;
		padding: 2rem;
	}
	.form-layout input {
		width: 100%;
	}

	.button-layout {
		display: flex;
		column-gap: 1rem;
		width: 100%;
		justify-content: space-between;
	}
</style>
