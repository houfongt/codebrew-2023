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
    <div class="w-full h-full bg-white flex flex-row flex-wrap justify-center sm:justify-evenly content-start md:space-between p-4 overflow-auto outline-0" id="appDrawer">
        'Hello world'
    </div>
  </div>
</template>

<script>
export default {
    name: 'IngredientsCard',
    data() {
        return {
            isOpen: false,
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
  }
}
</script>

<style>

</style>