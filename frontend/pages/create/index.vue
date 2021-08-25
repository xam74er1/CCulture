<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <error v-if="error!==null" :message="error" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Créer une partie
        </h2>
      </div>
      <form class="mt-8 space-y-6">
        <input name="remember" type="hidden" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label class="sr-only" for="pseudoId">Pseudo</label>
            <input
              id="pseudoId"
              v-model="pseudoId"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Pseudo"
              type="text"
            >
          </div>

          <div class="pt-4 ">
            <a
              class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 cursor-pointer"
              @click="create"
            >
              <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
              Créer une partie
            </a>
          </div>

          <input id="sid" v-model="sid" name="sid" type="hidden">
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import socket from '~/plugins/socket.io'
import { createCookie } from '~/components/uttils/GenerateCookie'
import { dayInMs } from '~/components/uttils/Constante'

export default {
  name: 'Create',
  data () {
    return {
      socket,
      gameId: '',
      pseudoId: null,
      sid: null,
      error: null
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({
      name: 'main',
      persist: 'mainSocket'
    })

    this.socket.on('Evt_redirect_game_id', (evt) => {
      console.log('Receive Evt_redirect_game_id')
      console.log(evt)

      if ('party_id' in evt && 'player_id' in evt) {
        createCookie('userID', evt.player_id, 100 * dayInMs)
        this.$router.replace({ path: `party/${evt.party_id}` })
      }
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      this.error = evt.toString()
    })
  },
  methods: {
    create () {
      this.socket.emit('Evt_join_game', {
        gameId: '',
        sid: this.socket.io.engine.id,
        pseudoId: this.pseudoId
      })
    }
  }
}
</script>

<style scoped>

</style>
