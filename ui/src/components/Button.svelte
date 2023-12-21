<script lang="ts">
	export let label: string;
	export let variant: 'primary' | 'secondary' | 'close';
	export let classes: string = '';
	export let href: string = '';
	export let type: 'button' | 'submit' | 'reset' = 'button';
</script>

{#if href}
	<a {href} class={classes}>{label}</a>
{:else}
	<button {type} on:click class={`${variant}-button ${classes}`}>
		{#if variant == 'close'}
			<span class="sr-only">{label}</span>
			<svg
				fill="white"
				transform="rotate(45)"
				viewBox="0 0 100 100"
				xmlns="http://www.w3.org/2000/svg"
			>
				<rect x="40" y="0" width="20" height="100" />
				<rect x="0" y="40" width="100" height="20" />
				Close
			</svg>
		{:else}
			{label}
		{/if}
	</button>
{/if}

<style>
	button {
		color: var(--primary-font-color);
		box-shadow: 1px 2px 1px 0 var(--boxshadow-color);
		cursor: pointer;
		border: none;
		border-radius: 5px;
		padding: 0.6rem;
	}
	button:active {
		box-shadow: inset 1px 1px 1px 0 rgba(0, 0, 0, 80%);
	}

	.primary-button {
		background-color: var(--primary-accent-6);
		min-width: 15rem;
	}
	.primary-button:hover {
		background-color: var(--primary-accent-5);
	}

	.secondary-button {
		background-color: var(--secondary-accent-6);
		min-width: 15rem;
	}
	.secondary-button:hover {
		background-color: var(--secondary-accent-5);
	}

	.close-button {
		background-color: var(--red-5);
		position: relative;
	}
	.close-button:hover {
		background-color: var(--red-4);
	}
	.close-button svg {
		position: relative;
		vertical-align: middle;
		height: 1em;
		width: 1em;
	}
</style>
