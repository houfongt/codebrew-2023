<script>
   export default {
      name: 'App',
      mounted() {
         if (this.$store.state.introPageShown != true) {
            this.$router.push('/Welcome')
         } else {
            this.$router.push('/')
         }
      }
   }
</script>

<template>
   <div class="select-none cont02">
      <router-view/>
   </div>
</template>


