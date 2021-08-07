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
      <Question :question="this.question" :reponce="this.response"></Question>
    </div>

    <div v-if="gameStatus === 'answer'">
      <AnswerList :question="this.question" :all-reponce="this.allReponce" :socket="this.socket" :dispaly-valider="this.dispalyValider"></AnswerList>
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
import Question from "../../components/Question";
import AnswerList from "../../components/AnswerList";
export const status = { PENDING: 'pending', STARTED: 'started', FINISHED: 'finished',ANSWER :'answer' }
export default {
  components: {AnswerList, Question},
  data () {
    return {
      id: this.$route.params.id,
      players: [],
      gameStatus: status.PENDING,
      question: null,
      response: null,
      message: null,
      allReponce : null,
      socket : null,
      dispalyValider : true
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
      this.sendResponse ();
    })

    this.socket.on('Evt_party_game_terminated', (evt) => {
      console.log(evt)
      this.sendResponse ();
      this.gameStatus = status.FINISHED
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      this.message = evt.toString()
    })

    this.socket.on('Evt_party_send_new_aswers', (evt) => {
      console.log('Evt_new_answer')
      this.gameStatus = status.ANSWER

      this.question = evt.question;
      this.allReponce = evt.allReponce;
      this.dispalyValider = true;
      console.log(evt)
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
    getNextAnswer(){
      this.socket.emit('Evt_party_get_curent_answer', "")

    },

    testFillAuto(){
      console.log("Demende de remplissage auto")
      this.socket.emit('Evt_Test_fill_asnwer', "")
    },
    testEnvoisAutoCaseCocher(){
      console.log(this.allReponce)
    }

  }
}
</script>

<style scoped>

</style>
