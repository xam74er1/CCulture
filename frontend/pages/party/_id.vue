<template>
  <div>
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ id }}
    </h2>
    <PlayersList :players="players" />
  </div>
</template>

<script>
export default {
  data () {
    return {
      id: this.$route.params.id,
      players: []
    }
  },

  mounted () {
    this.socket = this.$nuxtSocket({ name: 'main', persist: 'mainSocket' })
    this.socket.emit('Evt_party_join', { message: 'I\'m joining' })
    this.socket.on('Evt_party_new_player_as_join', (evt) => {
      console.log(evt)
      if ('players' in evt && Array.isArray(evt.players)) {
        this.players = evt.players
      }
    })
  }
}
</script>

<style scoped>

</style>
