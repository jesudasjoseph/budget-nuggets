<script lang="ts">
	export let label: string;
	export let variant: 'primary' | 'secondary' | 'close';
	export let href: string = '';
	export let type: 'button' | 'submit' | 'reset' = 'button';
</script>

{#if href}
	<a {href}>{label}</a>
{:else}
	<button {type} on:click class={`${variant}-button`}>
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

<style lang="scss">
	@import '../scss/variables';
	@import '../scss/common';

	button {
		color: $primary-font-color;
		box-shadow: 1px 2px 1px 0 $boxshadow-color;
		cursor: pointer;
		border: none;
		border-radius: 5px;
		padding: 1rem;

		&:active {
			box-shadow: inset 1px 1px 1px 0 rgba(0, 0, 0, 80%);
		}
	}

	.primary-button {
		background-color: $primary-accent;
		min-width: 15rem;

		&:hover {
			background-color: lighten($primary-accent, 5%);
		}
	}

	.secondary-button {
		background-color: $secondary-accent;
		min-width: 15rem;

		&:hover {
			background-color: lighten($secondary-accent, 5%);
		}
	}

	.close-button {
		background-color: $red;
		position: relative;

		svg {
			position: relative;
			vertical-align: middle;
			height: 1em;
			width: 1em;
		}

		&:hover {
			background-color: lighten($red, 5%);
		}
	}
</style>
