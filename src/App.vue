<script>
   export default {
      name: 'App',
      mounted() {
         if (this.$store.state.introPageShown != true) {
            //this.$router.push('/Welcome')
         } else {
            //this.$router.push('/')
         }
      }
   }
</script>

<template>
   <router-view/>
</template>


