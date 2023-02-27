<script lang="ts">
	import { afterUpdate } from "svelte";
    import { slide, fade } from "svelte/transition";
    import { createEventDispatcher } from 'svelte';
    export let visible: Boolean = false;

    const dispatch = createEventDispatcher();

    function onKeyDown(event: KeyboardEvent){
        if(event.key == 'Escape')
            visible=false;
    }

    afterUpdate(() => {
        if (!visible) {
            dispatch('reset');
        }
    });
</script>

<svelte:window on:keydown={onKeyDown}/>

{#if visible}
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div transition:fade on:click={() => visible=false}>
    </div>
    <section transition:slide>
        <slot/>
    </section>
{/if}

<style lang="scss">
    @import '../scss/variables';
    div {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        opacity: 20%;
        background-color: $white;
    }
    section {
        position: absolute;
        border-radius: 15px 15px 0 0;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        flex-direction: column;
        row-gap: 1rem;
        background-color: $secondary-background;
    }
</style>