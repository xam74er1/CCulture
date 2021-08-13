<template>
  <div class="flex flex-col">
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  <Question correct-response="question.response" />
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="response in allResponse" :key="response.name">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                      {{ response.name }}
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-gray-900">
                        {{ response.answer }}
                      </div>
                    </div>

                    <div class="ml-4">
                      <label class="inline-flex items-center">
                        <input
                          v-model="response.valid"
                          type="checkbox"
                          class="form-checkbox text-green-500"
                          :value="response.valid"
                        >

                      </label>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="mt-1">
          <a
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click="validAnswer"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3" />
            Valider
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Question from './Question'

export default {
  name: 'AnswerList',
  components: { Question },
  props: {
    allResponse: {
      type: Array[Object],
      required: true
    }
  },
  data () {
    return {
      socket: null
    }
  },
  mounted () {
    this.socket = this.$nuxtSocket({ name: 'main', persist: 'mainSocket' })
  },

  methods: {
    validAnswer () {
      this.socket.emit('Evt_party_set_valid_answers', this.allResponse)
    }
  }
}
</script>

<style scoped/>
