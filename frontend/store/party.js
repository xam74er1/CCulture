import { status } from '~/components/uttils/utils'

export const state = () => ({
  error: null,
  players: [],
  gameStatus: status.PENDING,
  currentQuestion: null,
  playerResponse: null
})

export const mutations = {
  setError (state, error) {
    state.error = error
  },
  setPlayers (state, players) {
    state.players = players
  },
  addPlayer (state, player) {
    state.players.push(player)
  },
  setGameStatus (state, status) {
    state.gameStatus = status
  },
  setCurrentQuestion (state, question) {
    state.currentQuestion = question
  },
  setPlayerResponse (state, response) {
    state.playerResponse = response
  }
}