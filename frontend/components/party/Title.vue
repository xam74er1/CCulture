<template>
  <div>
    <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
      Partie: #{{ partyId }}
    </h2>
    <h3 class="mt-6 text-center text-1xl font-bold text-gray-900">
      Game status: {{ gameStatus }}
    </h3>
  </div>
</template>
<script>
export default {
  name: 'Title',
  props: {
    partyId: {
      type: String,
      required: true
    },
    gameStatus: {
      type: String,
      required: true
    }
  }
}
</script>
