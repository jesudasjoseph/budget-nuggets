<script lang="ts">
	import { APIToken, APITokenExpiry, isAuthenticated } from '../stores';

	let username: string;
	let password: string;

	function loginOnClick(e: Event) {
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
			});
	}
</script>

<form>
	<header>
		<h1>Login</h1>
	</header>
	<label>
		Username
		<input type="text" name="username" bind:value={username} />
	</label>
	<label>
		Password
		<input type="password" name="password" bind:value={password} />
	</label>
	<button on:click={loginOnClick}>Login</button>
	<button
		on:click={(e) => {
			e.preventDefault();
			console.log($APIToken);
		}}
	/>
</form>
