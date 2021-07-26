<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>

        <div id="errorBox" class="bg-red-100 border-l-8 border border-red-400 text-red-700 px-4 py-3 rounded relative " role="alert" v-if="hasError">
          <div class="flex">
            <div class="py-1"><svg class="fill-current h-5 w-5 text-teal-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
            <div>
              <p class="font-bold"><span v-html="message"></span></p>

            </div>

          </div>

        </div>



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
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Pseudo"
            >
          </div>

          <div>
            <label for="gameId" class="sr-only">Id de la partie</label>
            <input
              id="gameId"
              v-model="gameId"
              type="text"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Id de la partie"
            >
          </div>

          <input id="sid" v-model="sid" type="hidden" name="sid">
        </div>

        <div>
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
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

import socket from '~/plugins/socket.io'
import Vue from 'vue'

export default {
  name: 'Join',
  data () {
    return {
      gameId: '',
      pseudoId: null,
      sid: null,
      socket,
      hasError : false,
      message: "<p>Message 42 </p>",


    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({ channel: '' })

    this.socket.on('Evt_redirect_game_id', (evt) => {
      console.log('Receive Evt_redirect_game_id')
      console.log(evt)

      // sessionStorage.uuid = evt.playerID
      // createCookie('userID', evt.playerID, 100 * dayInMs)
      // window.location.href = 'http://' + document.domain + ':' + location.port + evt.url
    })

    this.socket.on('Evt_error', (evt) => {
      console.log('Evt_error')
      console.log(evt)
      this.error = evt;
      this.hasError = true
      this.message = "<div> </div><strong class=\"font-bold\">"+evt+"</strong>"

    })


    //Pour changer en cas derreur



  },
//

  methods: {
    join () {
      console.log('Send Evt_join_game')

      this.socket.emit('Evt_join_game', {
        gameId: this.gameId,
        sid: this.socket.io.engine.id,
        pseudoId: this.pseudoId
      })
    }
  },

}



</script>

<style scoped>

</style>
