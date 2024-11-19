import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const Banks = ref({
    result:{}
  })
  const API_URL = 'http://127.0.0.1:8000'

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 Banks 저장하는 함수
  const getcompany = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/company/`,
    })
      .then((res) => {
        // console.log(res.data)
        Banks.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { Banks, API_URL, getcompany }
}, { persist: true })
