<template>
  <div>
    <error v-if="message!==null" :message="message" />
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ id }}
    </h2>
    <h3 class="mt-6 text-center text-1xl font-bold text-gray-900">
      Game status: {{ gameStatus }}
    </h3>
    <div v-if="question!=null && gameStatus === 'started'" class="p-1.5">
      <Question :question="question" :response="response" />
    </div>

    <div v-if="gameStatus === 'answer'">
      <AnswerList
        :question="question"
        :all-response="allResponse"
        :display-validation="displayValidation"
      />
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

        <!--Provistoire pour teste -->

        <div class="mt-1">
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click="testFillAuto"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
            Pour teste : Remplissage auto
          </a>
        </div>

        <div class="mt-1">
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click="testEnvoisAutoCaseCocher"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
            Pour teste : Enovis auto des case cocher
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Question from '../../components/Question'
import AnswerList from '../../components/AnswerList'

export const status = { PENDING: 'pending', STARTED: 'started', FINISHED: 'finished', ANSWER: 'answer' }
export default {
  components: { AnswerList, Question },
  data () {
    return {
      id: this.$route.params.id,
      players: [],
      gameStatus: status.PENDING,
      question: null,
      response: null,
      message: null,
      allResponse: null,
      socket: null,
      displayValidation: true
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({ name: 'main', persist: 'mainSocket' })

    this.socket.emit('Evt_party_join', this.id)

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
      this.sendResponse()
    })

    this.socket.on('Evt_party_game_terminated', (evt) => {
      console.log(evt)
      this.sendResponse()
      this.gameStatus = status.FINISHED
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      this.message = evt.toString()
    })

    this.socket.on('Evt_party_send_new_answers', (evt) => {
      console.log('Evt_new_answer')
      console.log(evt)

      this.gameStatus = status.ANSWER
      if ('question' in evt && 'allResponse' in evt) {
        this.question = evt.question
        this.allResponse = evt.allResponse
      }
      this.displayValidation = true
    })
  },
  methods: {
    startGame () {
      this.socket.emit('Evt_party_start_game', {})
    },

    sendResponse () {
      this.socket.emit('Evt_party_game_send_response', this.response)
      this.response = null
    },
    getNextAnswer () {
      this.socket.emit('Evt_party_get_current_answer', '')
    },

    testFillAuto () {
      console.log('Demende de remplissage auto')
      this.socket.emit('Evt_Test_fill_answer', '')
    },
    testEnvoisAutoCaseCocher () {
      console.log(this.allResponse)
    }

  }
}
</script>

<style scoped>

</style>
