<script lang="ts">
	import type { FeatherIconNames } from 'feather-icons';
	import Icon from './Icon.svelte';

	export let label: string;
	export let variant: 'primary' | 'secondary' | 'close' | 'default' = 'default';
	export let classes: string = '';
	export let href: string = '';
	export let type: 'button' | 'submit' | 'reset' = 'button';
	export let full = false;
	export let icon: FeatherIconNames | undefined = undefined;
	export let iconOnly = false;
</script>

{#if href}
	<a {href} class:full class={`${variant}-button button ${iconOnly ? 'icon-only' : ''} ${classes}`}>
		<span class={iconOnly ? 'sr-only' : ''}>
			{label}
		</span>
		{#if icon}
			<Icon {icon} />
		{/if}
	</a>
{:else}
	<button
		{type}
		on:click
		class:full
		class={`${variant}-button button ${iconOnly ? 'icon-only' : ''} ${classes}`}
	>
		{#if variant == 'close'}
			<span class="sr-only">{label}</span>
			<Icon icon="x" />
		{:else}
			<span class={iconOnly ? 'sr-only' : ''}>
				{label}
			</span>
		{/if}
		{#if icon}
			<Icon {icon} />
		{/if}
	</button>
{/if}

<style>
	button,
	a {
		display: flex;
		align-items: center;
		justify-content: center;
		color: var(--primary-font-color);
		box-shadow: 1px 2px 1px 0 var(--boxshadow-color);
		cursor: pointer;
		border: none;
		border-radius: 5px;
		padding: 0.6rem;
		text-align: center;
		font-size: var(--font-size-normal);
	}

	.full {
		width: 100%;
	}

	.icon-only {
		padding: 0.4rem;
	}

	a {
		text-decoration: none;
	}

	button:active {
		box-shadow: inset 1px 1px 1px 0 rgba(0, 0, 0, 80%);
	}

	.default-button {
		background-color: var(--primary-accent-6);
	}
	.default-button:hover {
		background-color: var(--primary-accent-5);
	}

	.primary-button {
		background-color: var(--primary-accent-6);
	}
	.primary-button:hover {
		background-color: var(--primary-accent-5);
	}

	.secondary-button {
		background-color: var(--secondary-accent-6);
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
