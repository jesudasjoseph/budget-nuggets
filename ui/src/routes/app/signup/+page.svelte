<script lang="ts">
	import { goto } from '$app/navigation';
	import { createUser } from '@api/user';
	import Button from '@components/Button.svelte';

	interface FormFeedback {
		email?: [string];
		first_name?: [string];
		last_name?: [string];
		password?: [string];
		password_confirmation?: [string];
	}

	let email = '';
	let firstName = '';
	let lastName = '';
	let password = '';
	let passwordConfirmation = '';

	let formFeedback: FormFeedback = {};

	function createUserSubmit() {
		createUser(email, firstName, lastName, password, passwordConfirmation)
			.then((data) => {
				goto('/app/login');
			})
			.catch((error) => {
				console.log(error.status);
				error.response.json().then((errors: FormFeedback) => {
					formFeedback = errors;
				});
			});
	}
</script>

<div class="main">
	<form class="form-layout">
		<h2>Sign Up</h2>
		<label>
			<span>Email</span>
			<p aria-live="polite">
				{formFeedback.email ? formFeedback.email[0] : ''}
			</p>
			<input type="email" placeholder="Email" required bind:value={email} />
		</label>
		<label>
			<span>First Name</span>
			<p aria-live="polite">
				{formFeedback.first_name ? formFeedback.first_name[0] : ''}
			</p>
			<input type="text" placeholder="Firt Name" required bind:value={firstName} />
		</label>
		<label>
			<span>Last Name</span>
			<p aria-live="polite">
				{formFeedback.last_name ? formFeedback.last_name[0] : ''}
			</p>
			<input type="text" placeholder="Last Name" required bind:value={lastName} />
		</label>
		<label>
			<span>Password</span>
			<p aria-live="polite">
				{formFeedback.password ? formFeedback.password[0] : ''}
			</p>
			<input type="password" placeholder="Password" required bind:value={password} />
		</label>
		<label>
			<span>Confirm Password</span>
			<p aria-live="polite">
				{formFeedback.password_confirmation ? formFeedback.password_confirmation[0] : ''}
			</p>
			<input
				type="password"
				placeholder="Confirm Password"
				required
				bind:value={passwordConfirmation}
			/>
		</label>
		<div class="button-layout">
			<Button variant="primary" label="Sign Up" type="submit" on:click={createUserSubmit} />
		</div>
	</form>
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
	label {
		display: flex;
		flex-direction: column;
		row-gap: 0.2rem;
	}
	p {
		color: var(--red-4);
	}
</style>
