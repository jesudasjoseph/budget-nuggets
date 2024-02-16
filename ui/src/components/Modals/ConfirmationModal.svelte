<script lang="ts">
	import Modal from '@components/Modal.svelte';
	import Button from '@components/Button.svelte';
	import { createEventDispatcher } from 'svelte';

	export let visible = false;
	export let label: string;

	const dispatch = createEventDispatcher();
</script>

<Modal bind:visible on:cancel>
	<h2 slot="header">{label}</h2>
	<slot />
	<div class="modal-footer" slot="footer">
		<Button
			label="Yes"
			variant="primary"
			on:click={() => {
				visible = false;
				dispatch('ok');
			}}
		/>
		<Button
			label="No"
			variant="secondary"
			on:click={() => {
				visible = false;
				dispatch('cancel');
			}}
		/>
	</div>
</Modal>

<style>
	div {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}

	.modal-footer :global(.button) {
		width: 6rem;
		min-width: 0;
	}
</style>
