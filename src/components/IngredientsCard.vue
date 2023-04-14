<template>
    <div class="fixed shadow-lg bottom-0 left-0 right-0 w-full h-5/6 flex flex-col justify-start items-center transition-all ease-in-out duration-300 z-50" id="safeArea" :class="isOpen ? '' : 'translate-y-[30vh]'">
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
    <div class="w-full h-full bg-white flex flex-col flex-wrap content-start md:space-between  outline-0 px-8 py-4" id="appDrawer">
        <div class="flex flex-row justify-between items-center w-full">
            <p class="text-3xl font-bold">Ingredients</p>
            <button>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                </svg>
            </button>
        </div>
        <div class="p-8">
            <ul>
                <li v-for="item in items" :key="item.id" class="flex flex-row justify-between items-center my-3">
                    <div class="flex flex-row justify-start items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mr-4">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        {{ item.title }}
                    </div>
                    <button @click="removeItem(item)">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                        </svg>
                    </button>
                </li>
            </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'IngredientsCard',
    data() {
        return {
            isOpen: false,
            items: [
                { id: 1, title: 'Egg' },
                { id: 2, title: 'Honey' },
                { id: 3, title: 'Apple' },
                { id: 4, title: 'Cheese' },
                { id: 5, title: 'Smoked Salmon' },
                { id: 6, title: 'Bread' },
                { id: 7, title: 'Ham' },
                { id: 8, title: 'Watermelon' },
                { id: 9, title: 'Carrot' },
                { id: 10, title: 'Carrot' },
                
            ]
        }
    },
    watch: {
        isOpen: function() {
            if (this.isOpen) {
                document.getElementById('safeArea').style.bottom = '0';
            } else {
                document.getElementById('safeArea').style.bottom = 'env(safe-area-inset-bottom)';
            }
        }
    },
    methods: {
        removeItem(item) {
            const index = this.items.indexOf(item)
            if (index > -1) {
                this.items.splice(index, 1)
            }
        }
    }
}
</script>

<style>

</style>