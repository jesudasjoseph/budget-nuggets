<script lang="ts">
	import { loginAPICall } from '../../api/util';
	let username: string;
	let password: string;
	let result = '';
	let error = '';

	export async function API(url: string, type: string, message: object) {
		const response = await fetch(`http://127.0.0.1:8000${url}`, {
			method: type,
			mode: 'cors',
			body: JSON.stringify(message),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then((response) => {
				if (!response.ok) {
					throw new Error(`Network Error: ${response.status} - ${response.statusText}`);
				}
				return response.json();
			})
			.then((data) => {
				result = data;
			})
			.catch((localError) => {
				error = localError;
			});
	}
</script>

<section>
	<h1>API Test Page</h1>

	<section>
		<h2>Login API</h2>
		<input type="text" bind:value={username} />
		<input type="password" bind:value={password} />
		<button on:click={() => API('/auth/login/', 'POST', { username, password })}>Login</button>
	</section>
	<section>
		<h2>Account API</h2>
		<section>
			<h3>Create Account</h3>
		</section>
	</section>
</section>

<div>
	<p class="results">{result}</p>
	<p class="error">{error}</p>
</div>

<style lang="scss">
	section {
		padding: 1rem;
	}
	div {
		position: fixed;
		bottom: 0;
		left: 0;
		right: 0;
		padding: 1rem;
		.error {
			color: red;
		}
	}
</style>
