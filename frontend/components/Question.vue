<template>
  <div>
    <div v-if="isQuestionImage">
      <img :src="imagePath" alt="">
    </div>
    <p>{{ question_text }}</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 m-1">
      <div v-if="correctResponse==null">
        <div class="mt-1 relative rounded-md shadow-sm">
          <input
            v-model="response"
            type="text"
            name="response"
            placeholder="Entrez la réponse"
            class="focus:ring-indigo-500 focus:border-indigo-500 block w-full w-full px-3 py-2 pl-7 pr-12 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none sm:text-sm"
            pattern=""
          >
        </div>

        <!--
        @keypress.enter="sendResponse"
        <div class="absolute inset-y-0 right-0 flex items-center">
          <button
            class="hover:ring-indigo-500 hover:border-indigo-500 h-full py-0 pl-2 pr-7 border border-r-0 border-gray-300 bg-transparent text-indigo-600 hover:text-indigo-700 font-medium sm:text-sm rounded-md"
            @click="sendResponse"
          >
            Envoyer
          </button>
        </div>
        -->
      </div>

      <div v-else>
        <p>Reponce attendu : {{ correctResponse }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: {
    question: {
      type: Object,
      required: true
    },
    correctResponse: {
      type: String,
      required: false
    }
  },
  data () {
    return {
      response: null,
      question_text: this.question.question,
      isQuestionImage: !!this.question.extention,
      imagePath: this.question.isBase64 ? 'data:image/' + this.question.extention + ';base64,' + new TextDecoder('utf-8').decode(this.question.image) : ''
    }
  }
}
</script>

<style scoped>

</style>
