<script lang="ts">
	import Button from '@components/Button.svelte';
	import Modal from '@components/Modal.svelte';
</script>

<div class="main">
	<div>
		<h1>Budget Nuggets.</h1>
		<p>A simple budgeting app</p>
	</div>
	<div class="options">
		<Button variant="primary" href="/app/login" label="Go to app" />
	</div>
</div>

<style>
	.main {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: stretch;
		padding: 10rem 2rem 2rem;
		height: 100%;
	}

	.options {
		display: flex;
		row-gap: 1rem;
		flex-direction: column;
		justify-content: stretch;
	}

	/* tablet */
	@media (min-width: 768px) {
		.main {
			padding: 0;
			align-items: center;
			flex-direction: row;
			justify-content: center;
			column-gap: 10rem;
		}
	}
</style>
