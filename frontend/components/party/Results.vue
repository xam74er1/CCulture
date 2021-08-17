<template>
  <div>
    <p>{{ finalsResults }}</p>
    <ResultsDiagram />
  </div>
</template>

<script>
import ResultsDiagram from '@/components/party/ResultsDiagram'

export default {
  name: 'Results',
  components: { ResultsDiagram },
  computed: {
    finalsResults () {
      return this.$store.state.party.finalsResults ?? ''
    }
  }
}
</script>

<style scoped>

</style>
