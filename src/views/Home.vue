<template>
    <div class="flex flex-col justify-center items-center mt-28">
        <router-link style="-webkit-touch-callout: none"  :to="{ name: 'Capture'}">
            <button>Click me to shoot</button>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'Home',
    
}
</script>

<style>

</style>