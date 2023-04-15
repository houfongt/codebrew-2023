<template>
    <div class="flex flex-col justify-center items-center font-Poppins">
        <p class="m-9 font-bold text-4xl">{{ title }}</p>
        <img :src="getImageUrl()" alt="Intro Pictures" class="m-16 block" />
        <p class="text-xl px-8 text-center w-auto">{{ context }}</p>
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