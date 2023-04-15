<template>
    <div v-for="page in pages" :key="page.num">
        <IntroCards :title="page.title" :context="page.content" :imgsrc="page.imgsrc" v-if="currentPage === page.num" />
    </div>
    <div class="flex flex-col justify-center items-center">
    <button @click="next()" class="bg-gradient-to-t from-green-700 to-green-400 flex justify-center items-center p-4 rounded-3xl my-[37px]">
        <p class="text-white">Next</p>
    </button>
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
            pages: [{ num: 1, imgsrc: "intro-1.png", title: 'Waste No More!', content: "Ever needed to throw away perfectly good food because you don’t know what to do with it? Well.... not anymore. "},
            { num: 2, imgsrc: "intro-2.png", title: 'Save your planet... ', content: "Reduce waste by letting our app turn your fridge into a sustainable place!"},
            { num: 3, imgsrc: "intro-3.png", title: 'Let\'s get started!', content: ""}],
            currentPage: 1
        }
    },
    mounted() {
        console.log(this.$store.state.introPageShown);
        if (this.$store.state.introPageShown != true) {
            this.$router.push('/Welcome')
         } else {
            this.$router.push('/')
         }
    },
    methods: {
        next() {
            if (this.currentPage !== 3) {
                this.currentPage += 1
            } else {
                this.$store.commit('setIntroPageStatus', true)
                this.$router.push('/')
            }
        }
    }
}
</script>

<style>

</style>