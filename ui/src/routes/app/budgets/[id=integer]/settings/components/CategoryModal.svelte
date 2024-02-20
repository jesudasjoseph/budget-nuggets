<script lang="ts">
	import Modal from '@components/Modal.svelte';
	import TextInput from '@components/TextInput.svelte';
	import ColorInput from '@components/ColorInput.svelte';
	import Button from '@components/Button.svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let visible = false;
	export let title: string;
	export let label: string | undefined;
	export let color: string | undefined;
</script>

<Modal bind:visible on:cancel>
	<form on:submit>
		<h2>{title}</h2>
		<div class="input-section">
			<TextInput label="Label" bind:value={label} />
			<ColorInput label="Color" hideLabel bind:value={color} />
		</div>
		<div class="button-group">
			<Button
				label="Cancel"
				variant="secondary"
				on:click={() => {
					visible = false;
					dispatch('cancel');
				}}
			/>
			<Button label="Save" variant="primary" type="submit" />
		</div>
	</form>
</Modal>

<style>
	.input-section {
		display: flex;
		column-gap: var(--space-xs);
		align-items: end;
	}
	.button-group {
		display: flex;
		justify-content: space-between;
	}
	form {
		display: flex;
		flex-direction: column;
		row-gap: var(--space);
	}
</style>
