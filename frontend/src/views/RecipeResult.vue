<template>
   
    <div v-if="dataReady">
        <Title title="Here is a suggested recipe: " />
        <div v-html="data" class="w-full px-8 font-Poppins"></div>
        <div class="flex flex-row justify-center items-center">
        <router-link style="-webkit-touch-callout: none"  :to="{ name: 'Home'}">
            <button class="bg-gradient-to-t from-green-700 to-green-400 flex justify-center items-center p-4 rounded-3xl my-[37px]" @click="save(); store.items = []">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6 mr-2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p class="text-white">Done</p> 
            </button>
        </router-link>
        </div>
    </div>
    <div v-else class="flex flex-col justify-center items-center">
        <Title title="Hold on..." />
        <svg class="animate-spin mt-16 h-12 w-12 text-black" fill="none" viewBox="0 0 24 24" >
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
    </div>
</template>

<script>
import Title from '../components/Title.vue'
import { store } from '../store'
export default {
    name: 'RecipeResult',
    components: {
        Title
    },
    data() {
        return {
            dataReady: false,
            data: '',
            store
        }
    },
    mounted() {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ food_items: this.store.items})
        };
        fetch("https://codebrew.cgps.ch/upload2", requestOptions).then(response => response.json()).then(data => {
            console.log(JSON.parse(data));
            data = this.JSON_parse(data, true)
            this.data = data
            this.dataReady = true
        });
    },
    methods: {
        save() {
            //this.data = this.data
            const regex = /\b<strong>\b <\/strong>*/;
            console.log(this.data.match(regex));
        },
        JSON_parse(s, emit_unicode) {
            let json = JSON.parse(s).recipe;
            return emit_unicode ? json : json.replace(/[\u007f-\uffff]/g,
            function(c) { 
                return '\\u'+('0000'+c.charCodeAt(0).toString(16)).slice(-4);
            }
            );
        }
    }
}
</script>

<style>

</style>
