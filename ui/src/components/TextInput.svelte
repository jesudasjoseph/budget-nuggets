<script lang="ts">
	export let value: string | undefined = undefined;
	export let label: string;
	export let placeholder = '';
	export let hideLabel = false;
	export let required = false;
	export let pattern: string | undefined = undefined;
	export let variant: 'default' | 'currency' = 'default';
	export let type: 'text' | 'password' | 'date' = 'text';

	const onKeypress = (event: KeyboardEvent) => {
		if (
			event.key === '0' ||
			event.key === '1' ||
			event.key === '2' ||
			event.key === '3' ||
			event.key === '4' ||
			event.key === '5' ||
			event.key === '6' ||
			event.key === '7' ||
			event.key === '8' ||
			event.key === '9' ||
			event.key === 'Backspace' ||
			event.key === 'Delete' ||
			event.key === 'ArrowLeft' ||
			event.key === 'ArrowRight' ||
			event.key === 'Tab'
		)
			return true;
		else event.preventDefault();
	};

	const onInput = (event: Event) => {
		if (value) {
			value = value.replace('.', '');
			if (value.length < 2) value = '.' + value;
			else {
				value = value.slice(0, -2) + '.' + value.slice(-2);
			}

			if (value === '.') value = '';
		}
	};
</script>

<label>
	<span class={hideLabel ? 'sr-only' : ''}>{label}</span>
	{#if type === 'text'}
		{#if variant === 'currency'}
			<span class="overlay">
				<input
					type="text"
					{pattern}
					{placeholder}
					{required}
					bind:value
					on:keydown={onKeypress}
					on:input={onInput}
				/>
				<span>$</span>
			</span>
		{:else}
			<input type="text" {pattern} {placeholder} {required} bind:value />
		{/if}
	{:else if type === 'password'}
		<input type="password" {pattern} {placeholder} {required} bind:value />
	{:else if type === 'date'}
		<input type="date" {pattern} {required} bind:value />
	{/if}
</label>

<style>
	label {
		display: flex;
		flex-direction: column;
		row-gap: var(--space-xxs);
		color: var(--blue-0);
	}
	input {
		border-radius: var(--input-border-radius);
		padding: var(--input-padding);
		width: 100%;
		background-color: var(--gray-8);
		border: 3px solid var(--gray-5);
		color: var(--blue-0);
		font-size: var(--font-size-md);
	}
	.overlay {
		position: relative;
		display: block;
	}
	.overlay span {
		position: absolute;
		left: var(--space-xs);
		width: var(--space);
		color: var(--blue-0);
		top: 0;
		bottom: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: var(--font-size-md);
	}
	.overlay input {
		padding-left: calc(var(--space) + var(--space-xxs));
		vertical-align: middle;
		text-align: right;
	}
</style>
