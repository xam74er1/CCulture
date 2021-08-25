<template>
  <div>
    <error v-if="error!==null" :message="error" />
    <Title :game-status="gameStatus" :party-id="id" />

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 m-1.5">
      <div class="md:col-span-2 p-1.5">
        <Question v-if="currentQuestion!==null && gameStatus === 'started'" />
        <AnswerList v-if="gameStatus === 'answer'" :all-response="allResponse" />
        <Results v-if="gameStatus==='results'" />
      </div>
      <div>
        <PlayersList :players="players" />
        <StartGameButton />

        <!--Provistoire pour teste -->

        <div v-if="gameStatus === 'started'" class="mt-1">
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
import { status } from '@/components/uttils/utils'
import Error from '@/components/common/Error'
import StartGameButton from '@/components/party/StartGameButton'
import Title from '@/components/party/Title'
import PlayersList from '@/components/PlayersList'
import Results from '@/components/party/Results'
import Question from '@/components/party/Question'
import AnswerList from '@/components/party/AnswerList'

export default {
  components: {
    StartGameButton,
    Title,
    AnswerList,
    Question,
    PlayersList,
    Results,
    Error
  },
  data () {
    return {
      id: this.$route.params.id,
      allResponse: null,
      socket: null
    }
  },
  computed: {
    error () {
      return this.$store.state.party.error
    },
    players () {
      return this.$store.state.party.players ?? []
    },
    gameStatus () {
      return this.$store.state.party.gameStatus ?? status.PENDING
    },
    currentQuestion () {
      return this.$store.state.party.currentQuestion
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({
      name: 'main',
      persist: 'mainSocket'
    })

    this.socket.emit('Evt_party_join', this.id)

    this.socket.on('Evt_party_new_player_as_join', (evt) => {
      console.log(evt)
      if ('players' in evt && Array.isArray(evt.players)) {
        this.$store.commit('party/setPlayers', evt.players)
      }
    })

    this.socket.on('Evt_party_player_disconnected', (evt) => {
      console.log(evt)
      if ('leader' in evt && 'players' in evt && Array.isArray(evt.players)) {
        this.$store.commit('party/setPlayers', evt.players)
      }
    })

    this.socket.on('Evt_party_game_started', (evt) => {
      console.log(evt)
      this.$store.commit('party/setGameStatus', status.STARTED)
    })

    this.socket.on('Evt_party_game_new_question', (evt) => {
      console.log(evt)
      this.$store.commit('party/setCurrentQuestion', evt)
      this.sendResponse()
    })

    this.socket.on('Evt_party_game_terminated', (evt) => {
      console.log(evt)
      this.sendResponse()
      this.$store.commit('party/setGameStatus', status.FINISHED)
      this.$store.commit('party/setCurrentQuestion', null)
      this.socket.emit('Evt_party_get_current_answer', {})
    })

    this.socket.on('Evt_party_final_results', (evt) => {
      console.log('Evt_party_final_results')
      console.log(evt)
      this.$store.commit('party/setGameStatus', status.RESULTS)
      this.$store.commit('party/setFinalsResults', evt)
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      this.$store.commit('party/setError', evt.toString())
    })

    this.socket.on('Evt_party_send_new_answers', (evt) => {
      console.log('Evt_new_answer')
      console.log(evt)

      this.$store.commit('party/setGameStatus', status.ANSWER)

      if ('question' in evt && 'allResponse' in evt) {
        this.$store.commit('party/setCurrentQuestion', evt.question)
        this.allResponse = evt.allResponse
      }
    })
  },
  methods: {
    sendResponse () {
      this.socket.emit('Evt_party_game_send_response', this.$store.state.party.playerResponse)
      this.$store.commit('party/setPlayerResponse', '')
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
