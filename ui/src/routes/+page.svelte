<script lang="ts">
	import { APIToken, APITokenExpiry, isAuthenticated } from '../stores';
	import { goto } from '$app/navigation';
	import Button from '../components/Button.svelte';
	import Modal from '../components/Modal.svelte';
	let showLoginModal = false;
	let username = '';
	let password = '';

	function resetLoginModal(){
		username = '';
		password = '';
	}

	function getAPIKey(e: Event) {
		e.preventDefault();
		fetch('http://127.0.0.1:8000/auth/login/', {
			method: 'POST',
			mode: 'cors',
			body: JSON.stringify({ username: username, password: password }),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((response) => response.json())
			.then((data) => {
				$APIToken = data.token;
				$APITokenExpiry = data.token;
				goto("/dashboard");
			});
	}

</script>

<main>
	<div>
		<h1>Budget Nuggets.</h1>
		<p>A simple budgeting app</p>
	</div>
	<div id="options">
		<Button variant="primary" type='submit' label="Login" on:click={() => showLoginModal=true}/>
		<Button variant="secondary" label="Create Account"/>
	</div>
	<Modal bind:visible={showLoginModal} on:reset={resetLoginModal}>
		<form class="form-layout">
			<h2>Login</h2>
			<label>
				<span class="sr-only">Username</span>
				<input type="text" placeholder="Username" bind:value={username}/>
			</label>
			<label>
				<span class="sr-only">Password</span>
				<input type="password" placeholder="Password" bind:value={password}/>
			</label>
			<div class="button-layout">
				<Button variant="close" label="Close" on:click={() => showLoginModal=false} />
				<Button variant="primary" label="Login" on:click={getAPIKey}/>
			</div>
		</form>
	</Modal>
</main>

<style lang="scss">
	@import '../scss/variables';
	@import '../scss/breakpoints';
	@import '../scss/common';

	main {
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

		input {
			width: 100%;
		}
	}

	.button-layout {
		display: flex;
		column-gap: 1rem;
		width: 100%;
		justify-content: space-between;
	}

	@include breakpoint(tablet){
		main {
			padding: 10rem 2rem;
		}

		#options {
			width: 200px;
		}
	}

</style>
