<template>
  <div>
    <div v-if="haveImage">
      <img :src="imagePath" alt="">
    </div>
    <p>{{ questionName }}</p>
    <ResponseInput />
  </div>
</template>

<script>
import ResponseInput from '@/components/party/ResponseInput'

export default {
  name: 'Question',
  components: { ResponseInput },
  computed: {
    currentQuestion () {
      return this.$store.state.party.currentQuestion
    },
    questionName () {
      if ('question' in this.currentQuestion) {
        return this.currentQuestion.question
      }
      return ''
    },
    haveImage () {
      if ('extension' in this.currentQuestion) {
        return !!this.currentQuestion.extension
      }
      return false
    },
    imagePath () {
      if (this.haveImage() && 'isBase64' in this.currentQuestion) {
        return this.currentQuestion.isBase64 ? 'data:image/' + this.currentQuestion.extention + ';base64,' + new TextDecoder('utf-8').decode(this.currentQuestion.image) : ''
      }
      return null
    }
  }
}
</script>
