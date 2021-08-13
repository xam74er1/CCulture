<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <error v-if="message!==null" :message="message" />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Rejoindre une partie
        </h2>
      </div>
      <form class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="pseudoId" class="sr-only">Pseudo</label>
            <input
              id="pseudoId"
              v-model="pseudoId"
              type="text"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Pseudo"
            >
          </div>

          <div>
            <label for="gameId" class="sr-only">Id de la partie</label>
            <input
              id="gameId"
              v-model="gameId"
              type="text"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Id de la partie"
            >
          </div>

          <input id="sid" v-model="sid" type="hidden" name="sid">
        </div>

        <div>
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 cursor-pointer"
            @click="join"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
            Rejoindre
          </a>
        </div>
      </form>
    </div>
  </div>
</template>
<script>

import socket from '@/plugins/socket.io'
import { createCookie } from '@/components/uttils/GenerateCookie'
import { dayInMs } from '@/components/uttils/Constante'

export default {
  name: 'Join',
  data () {
    return {
      gameId: '',
      pseudoId: null,
      sid: null,
      socket,
      message: null
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({ name: 'main', persist: 'mainSocket' })

    this.socket.on('Evt_redirect_game_id', (evt) => {
      console.log('Receive Evt_redirect_game_id')
      console.log(evt)

      if ('party_id' in evt && 'player_id' in evt) {
        createCookie('userID', evt.player_id, 100 * dayInMs)
        this.$router.push({ path: `party/${evt.party_id}` })
      }

      // sessionStorage.uuid = evt.playerID
      // createCookie('userID', evt.playerID, 100 * dayInMs)
      // window.location.href = 'http://' + document.domain + ':' + location.port + evt.url
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      this.message = evt.toString()
    })
  },
  methods: {
    join () {
      this.socket.emit('Evt_join_game', {
        gameId: this.gameId,
        sid: this.socket.io.engine.id,
        pseudoId: this.pseudoId
      })
    }
  }
}

</script>

<style scoped>

</style>
