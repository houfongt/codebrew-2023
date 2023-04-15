<template>
    <div class="flex flex-row justify-between items-center w-full p-12 font-Poppins">
            <p class="text-3xl font-bold">{{ title }}</p>
            <button class="hidden">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                </svg>
            </button>
    </div>
</template>

<script>
    export default {
        name: 'Title',
        props: ['title']
    }
</script>

<style>

</style>