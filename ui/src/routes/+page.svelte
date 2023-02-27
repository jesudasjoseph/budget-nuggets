<script lang="ts">
	import Button from '../components/Button.svelte';
</script>

<main>
	<h1>Budget Nuggets.</h1>
	<p>A simple budgeting app</p>
	<nav>
		<Button variant="primary" label="Login" />
		<Button variant="secondary" label="Create Account" />
	</nav>
</main>

<style lang="scss">
	@import '../scss/colors';
</style>
