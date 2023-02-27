<script lang="ts">
	export let label: string;
	export let variant: 'primary' | 'secondary';
	export let href: string = '';
</script>

{#if href}
	<a {href}>{label}</a>
{:else}
	<button on:click class={`${variant}-button`}>{label}</button>
{/if}

<style lang="scss">
	@import '../scss/colors';

	button {
		color: $primary-font-color;
		box-shadow: 1px 2px 1px 0 $boxshadow-color;
		cursor: pointer;

		&:active {
			box-shadow: inset 1px 1px 1px 0 rgba(0, 0, 0, 80%);
		}
	}

	.primary-button {
		border: none;
		border-radius: 5px;
		background-color: $primary-accent;
		padding: 10px;

		&:hover {
			background-color: lighten($primary-accent, 5%);
		}
	}

	.secondary-button {
		border: none;
		border-radius: 5px;
		background-color: $secondary-accent;
		padding: 10px;

		&:hover {
			background-color: lighten($secondary-accent, 5%);
		}
	}
</style>
