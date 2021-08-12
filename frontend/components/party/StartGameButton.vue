<template>
  <div class="mt-1">
    <a
      class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      @click="startGame"
    >
      <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
      Démarrer la partie
    </a>
  </div>
</template>
<script>
export default {
  name: 'StartGameButton',
  data () {
    return {
      socket: null
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({ name: 'main', persist: 'mainSocket' })
  },
  methods: {
    startGame () {
      this.socket.emit('Evt_party_start_game', {})
    }
  }
}
</script>
