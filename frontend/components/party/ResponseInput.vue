<template>
  <div class="mt-1 relative rounded-md shadow-sm">
    <input
      v-model="response"
      type="text"
      placeholder="Entrez la réponse"
      class="focus:ring-indigo-500 focus:border-indigo-500 block w-full w-full px-3 py-2 pl-7 pr-12 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none sm:text-sm"
    >
  </div>
</template>
<script>
export default {
  name: 'ResponseInput',
  computed: {
    response: {
      get () {
        return this.$store.state.party.playerResponse
      },
      set (value) {
        this.$store.commit('party/setPlayerResponse', value)
      }
    }
  }
}
</script>
