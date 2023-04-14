<template>
    <div class="fixed shadow-lg bottom-0 left-0 right-0 w-full h-full flex flex-col justify-start items-center transition-all ease-in-out duration-300 z-30" id="safeArea" :class="isOpen ? '' : 'translate-y-[45vh]'">
        <button class="bg-white outline-0 shadow-2xl border-t-2 h-20 border-l-2 border-r-2 border-gray-300 flex justify-center items-center w-full rounded-t-full" v-on:click="isOpen ? isOpen = false : isOpen = true" >
            <div :class="isOpen ? 'hidden' : ''"> 
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" />
                </svg>
            </div>
            <div :class="isOpen ? '' : 'hidden'">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
            </div>
        </button>
    <div class="w-full h-full bg-white flex flex-col content-start md:space-between overflow-y-scroll overflow-x-clip outline-0 px-8 py-4" id="appDrawer">
        <div class="flex flex-row justify-between items-center w-full">
            <p class="text-3xl font-bold">Ingredients</p>
            <button>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                </svg>
            </button>
        </div>
        <div v-if="!store.fetchingData">
            <ul>
                <li v-for="item in store.items" :key="item.id" class="flex flex-row justify-between items-center my-[8px] shadow-xl rounded-lg px-4 bg-white">
                    <div class="flex flex-row justify-start items-center py-4">
                        {{ item.title }}
                    </div>
                    <button @click="removeItem(item)">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                        </svg>
                    </button>
                </li>
            </ul>
            <div class="flex justify-between py-4">
                <input type="text" placeholder="Enter missing items..." class="shadow-xl rounded-lg w-full p-4 mr-4" v-model="newItem" />
                <button class="flex justify-center items-center border-solid border-green-500 border-2 rounded-xl px-2 py-1" @click="addTodo()">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m6-6H6" />
                    </svg>
                    <p class="mr-2">Add</p>
                </button>
            </div>
            <div class="flex justify-center items-center my-[37px]">
                <button class="bg-gradient-to-t from-green-700 to-green-400 flex justify-center items-center p-4 rounded-3xl">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" class="w-6 h-6 mr-2">
                    <path fill-rule="evenodd" d="M9 4.5a.75.75 0 01.721.544l.813 2.846a3.75 3.75 0 002.576 2.576l2.846.813a.75.75 0 010 1.442l-2.846.813a3.75 3.75 0 00-2.576 2.576l-.813 2.846a.75.75 0 01-1.442 0l-.813-2.846a3.75 3.75 0 00-2.576-2.576l-2.846-.813a.75.75 0 010-1.442l2.846-.813A3.75 3.75 0 007.466 7.89l.813-2.846A.75.75 0 019 4.5zM18 1.5a.75.75 0 01.728.568l.258 1.036c.236.94.97 1.674 1.91 1.91l1.036.258a.75.75 0 010 1.456l-1.036.258c-.94.236-1.674.97-1.91 1.91l-.258 1.036a.75.75 0 01-1.456 0l-.258-1.036a2.625 2.625 0 00-1.91-1.91l-1.036-.258a.75.75 0 010-1.456l1.036-.258a2.625 2.625 0 001.91-1.91l.258-1.036A.75.75 0 0118 1.5zM16.5 15a.75.75 0 01.712.513l.394 1.183c.15.447.5.799.948.948l1.183.395a.75.75 0 010 1.422l-1.183.395c-.447.15-.799.5-.948.948l-.395 1.183a.75.75 0 01-1.422 0l-.395-1.183a1.5 1.5 0 00-.948-.948l-1.183-.395a.75.75 0 010-1.422l1.183-.395c.447-.15.799-.5.948-.948l.395-1.183A.75.75 0 0116.5 15z" clip-rule="evenodd" />
                    </svg>
                    <p class="text-white">Create Recipe</p> 
                </button>
            </div>
        </div>
        <div v-else class="flex justify-center items-center">
            <svg class="animate-spin mt-16 h-12 w-12 text-black" fill="none" viewBox="0 0 24 24" >
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>
    </div>
     
    </div>
    <!--
    <div class="fixed shadow-lg bottom-0 left-0 right-0 w-full h-auto flex flex-col justify-start items-center transition-all ease-in-out duration-300 z-50" :class="addBoxOpen ? '' : 'translate-y-[45px]'">
        Hello
     </div>
     --->
</template>

<script>
import { store } from '../store'

export default {
    name: 'IngredientsCard',
    
    data() {
        return {
            isOpen: false,
            addBoxOpen: false,
            newItem: '',
            store
        }
    },
    mounted() {
        console.log(this.items);
    },
    watch: {
        isOpen: function() {
            if (this.isOpen) {
                document.getElementById('safeArea').style.bottom = '0';
                document.getElementById('safeArea').style.top = '0';
            } else {
                document.getElementById('safeArea').style.bottom = 'env(safe-area-inset-bottom)';
                document.getElementById('safeArea').style.top = 'calc(env(safe-area-inset-top) + 32px)';
            }
        },
        
    },
    methods: {
        removeItem(item) {
            const index = this.store.items.indexOf(item)
            if (index > -1) {
                this.store.items.splice(index, 1)
            }
        },
        addTodo() {
            if (this.newItem.trim()) {
            const newId = this.store.items.length > 0 ? this.store.items[this.items.length - 1].id + 1 : 1
            this.store.items.push({ id: newId, title: this.newItem.trim() })
            this.newItem = ''
        }
    },
    }
}
</script>

<style>

</style>