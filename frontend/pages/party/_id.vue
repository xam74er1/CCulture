<template>
  <div>
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ id }}
    </h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 m-1">
      <div>
        <PlayersList :players="players" />
        <div class="mt-1">
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click="startGame"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
            Démarrer la partie
          </a>
        </div>
      </div>
    </div>
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
  },
  methods: {
    startGame () {
      this.socket.emit('Evt_party_start_game', {})
    }
  }
}
</script>

<style scoped>

</style>
