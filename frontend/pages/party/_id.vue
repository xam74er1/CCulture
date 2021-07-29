<template>
  <div>
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ id }}
    </h2>
    <h3 class="mt-6 text-center text-1xl font-bold text-gray-900">
      Game status: {{ gameStatus }}
    </h3>
    <div v-if="question!=null && gameStatus === 'started'" class="p-1.5">
      <p>{{ question }}</p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 m-1">
        <div class="mt-1 relative rounded-md shadow-sm">
          <input
            v-model="response"
            type="text"
            name="response"
            placeholder="Entrez la réponse"
            class="focus:ring-indigo-500 focus:border-indigo-500 block w-full w-full px-3 py-2 pl-7 pr-12 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none sm:text-sm"
            pattern=""
            @keypress.enter="sendResponse"
          >
          <div class="absolute inset-y-0 right-0 flex items-center">
            <button
              class="hover:ring-indigo-500 hover:border-indigo-500 h-full py-0 pl-2 pr-7 border border-r-0 border-gray-300 bg-transparent text-indigo-600 hover:text-indigo-700 font-medium sm:text-sm rounded-md"
              @click="sendResponse"
            >
              Envoyer
            </button>
          </div>
        </div>
      </div>
    </div>

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
      response: null
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
    })

    this.socket.on('Evt_party_game_terminated', (evt) => {
      console.log(evt)
      this.gameStatus = status.FINISHED
    })
  },
  methods: {
    startGame () {
      this.socket.emit('Evt_party_start_game', {})
    },

    sendResponse () {
      this.socket.emit('Evt_party_game_send_response', this.response)
      this.response = null
    }
  }
}
</script>

<style scoped>

</style>
