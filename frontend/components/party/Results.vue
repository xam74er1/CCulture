<template>
  <p>{{ finalsResults }}</p>
</template>

<script>
export default {
  name: 'Results',
  computed: {
    finalsResults () {
      return this.$store.state.party.finalsResults ?? ''
    }
  }
}
</script>

<style scoped>

</style>
