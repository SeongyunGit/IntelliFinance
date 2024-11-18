import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  // 회원가입 요청 액션
  const signUp = function (payload) {

    const { username, email, password , password2, birth_date } = payload
    console.log({ username, email, password, password2, birth_date })
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, email, password, birth_date
      }
    })
      .then((res) => {
        console.log(res)
        console.log('회원가입 성공')

        const password = password2
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    // const username = payload.username
    // const password1 = payload.password
    const { username, password } = payload
    console.log(payload)

    axios.post(
      'http://127.0.0.1:8000/accounts/login/',
      {
        username: username,
        password: password
      },
      {withCredentials:true}
    )
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'HomeView' })
        console.log(res.data)
        console.log('로그인 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // [추가기능] 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        console.log(res.data)
        token.value = null
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { articles, API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true })

