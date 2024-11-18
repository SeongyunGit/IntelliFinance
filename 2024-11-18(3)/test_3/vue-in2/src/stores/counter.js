import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const companyList = ref([])
  const companyListOption = ref([])
  const integrationProducts = ref([])
  const integrationProductOptions = ref([])

  const API_URL = 'http://127.0.0.1:8000'

  const surveyData = ref({})

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
      {
        withCredentials:true
      }
    )
      .then((res) => {
        token.value = res.data.key
        console.log(res.data)
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
  
  // api요청
  const getCompany = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/get_combined_company_data/`,
    })
      .then((response) => {
        // console.log(response.data)
        companyList.value = response.data.companyList
        companyListOption.value = response.data.companyListOption
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getIntegration = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/get_combined_integration_data/`,
    })
      .then((response) => {
        // console.log(response.data)
        integrationProducts.value = response.data.integrationProducts
        integrationProductOptions.value = response.data.integrationProductOptions
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getcompany = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/company/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getdeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/deposit/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getsaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/saving/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 데이터베이스 요청
  const getmortgageLoan = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/mortgageLoan/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getrentHouseLoan = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/rentHouseLoan/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 데이터베이스 초기화
  const delete_data = function () {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/delete_product_data/`,
    })
      .then((response) => {
        console.log(response.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const ox = ref(1)
   // survey 데이터 가져오는 함수
  const getSurveyData = function (test) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/survey/`,  // survey 데이터를 가져올 API endpoint
    })
      .then((response) => {
        const survey = response.data.surveyData.find(item => item.id === test)
        // console.log(survey)
        if (survey) {
          ox.value = 1
        } else {
          ox.value = 0
        }
        // console.log(ox)
        // survey가 존재하면 해당 데이터를 surveyData에 할당
        surveyData.value = survey || {
          'kor_co_nm': null,
          'mtrt_int': null,
          'intr_rate_type_nm': '전체',
          'save_trm': '전체',
          'intr_rate': null,
          'intr_rate2': null
        }
        console.log('Survey Data Loaded:', surveyData.value)
      })
      .catch((err) => {
        console.log('Error loading survey data:', err)
      })
  }

  // survey 데이터 저장하는 함수 (새로 추가)
  const saveSurveyData = function (SurveyData) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/survey/`,  // 새로운 데이터 추가
      data: SurveyData,  // 서버에 보낼 데이터
    })
      .then((response) => {
        console.log('Survey Data Saved:', response.data)
        surveyData.value = response.data  // 데이터가 잘 저장되었으면 업데이트
      })
      .catch((err) => {
        console.log('Error saving Survey Data:', err)
      })
  }

  // survey 데이터 수정 함수 (PUT 요청)
  const updateSurveyData = function (SurveyId, updatedData) {
    axios({
      method: 'put',
      url: `${API_URL}/api/v1/survey/${SurveyId}/`,  // 특정 surveyId에 해당하는 URL로 PUT 요청
      data: updatedData,  // 수정할 데이터
    })
      .then((response) => {
        console.log('Survey Data Updated:', response.data)
        surveyData.value = response.data  // 수정된 데이터를 업데이트
      })
      .catch((err) => {
        console.log('Error updating Survey data:', err)
      })
  }
  
  return { companyList, companyListOption, 
    integrationProducts, integrationProductOptions, 
    API_URL, 
    surveyData,
    getCompany, getIntegration, getcompany,
    getdeposit, getsaving, getmortgageLoan, getrentHouseLoan, 
    delete_data,
    getSurveyData, saveSurveyData, updateSurveyData,
    ox, signUp, logIn, token, isLogin, logOut
   }
}, { persist: true })
