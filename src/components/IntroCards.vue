<template>
    <div class="flex flex-col justify-center items-center font-Poppins">
        <p class="m-9 font-bold text-4xl">{{ title }}</p>
        <img :src="getImageUrl()" alt="Intro Pictures" class="m-16" />
        
        <div class="flex flex-col justify-center items-center">
            <p class="text-xl m-4">{{ context }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'IntroCards',
    props: ['title', 'imgsrc', 'context',],
    data() {
        return {

        }
    },
    methods: {
        getImageUrl() {
            return new URL(`/src/assets/${this.$props.imgsrc}`, import.meta.url)
        }
    }
}
</script>

<style>

</style>