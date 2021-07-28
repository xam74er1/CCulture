<template>
  <div>
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ id }}
    </h2>
    <h3 class="mt-6 text-center text-1xl font-bold text-gray-900">
      Game status: {{ gameStatus }}
    </h3>
    <p v-if="question!=null && gameStatus === 'started'">
      {{ question }}
      <!--Champ temporaire a inclure dans un modele -->
       <input
              id="reponce"
              v-model="reponce"
              type="text"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Reponce"
            >
    </p>
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
export const status = { PENDING: 'pending', STARTED: 'started', FINISHED: 'finished' }
export default {
  data () {
    return {
      id: this.$route.params.id,
      players: [],
      gameStatus: status.PENDING,
      question: null,
      reponce:null
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

    this.socket.on('Evt_party_game_started', (evt) => {
      console.log(evt)
      this.gameStatus = status.STARTED
    })

    this.socket.on('Evt_party_game_new_question', (evt) => {
      console.log(evt)
      this.question = evt
      //Envois la reponce
      this.socket.emit('Evt_party_game_reponce', this.reponce)
      this.reponce = "";
    })

    this.socket.on('Evt_party_game_terminated', (evt) => {
      console.log(evt)
      this.gameStatus = status.FINISHED
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
