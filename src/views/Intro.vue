<template>
    <div v-for="page in pages" :key="page.num">
        <IntroCards :title="page.title" :context="page.content" :imgsrc="page.imgsrc" />
    </div>
</template>

<script>
import IntroCards from '../components/IntroCards.vue'

export default {
    name: 'Intro',
    components: {
        IntroCards
    },
    data() {
        return {
            pages: [{ num: 1, imgsrc: "intro-1.png", title: 'Waste No More!', content: "Ever needed to throw away perfectly good food because you don’t know what to do with it? Well.... not anymore. "}]
        }
    }
}
</script>

<style>

</style>