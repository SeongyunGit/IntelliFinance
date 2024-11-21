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
  
  // 설문 초기값
  const initialSurveyData = {
    'id': 0,
    'user': null,
    'type_a': null,
    // 'today' # auto_now=True
    // 'fin_co_no': None,
    'kor_co_nm': [],  // 은행이름
    // 'intr_rate_type': None,
    'intr_rate_type_nm': ["단리", "복리"],  // 이자율(단리,복리)
    'save_trm': ["1","3","6","12","24","36"],  // 저축기간
    'intr_rate': 100,  // 기본금리
    'intr_rate2': 100,  // 우대금리
    // 'rsrv_type': None,
    'rsrv_type_nm': ['정액적립식', '자유적립식'],  // 적립식종류
    // 'rpay_type': None,
    'rpay_type_nm': ['분할상환방식', '만기일시상환방식'],  // 상환방식
    // 'lend_rate_type': None,
    'lend_rate_type_nm': ['고정금리', '변동금리'],  // 금리유형
    'lend_rate_min': 100,  // 최소 금리
    'lend_rate_max': 100,  // 최대 금리
    'lend_rate_avg': 100,  // 평균 금리
    // 'mrtg_type': None,
    'mrtg_type_nm': ['아파트', '아파트외']  // 담보 유형
  }
  
  // surveyData 객체
  const surveyData = ref({
    'deposit' : { ...initialSurveyData },
    'saving' : { ...initialSurveyData },
    'mortgageLoan' : { ...initialSurveyData },
    'rentHouseLoan' : { ...initialSurveyData },
  });
  const type_a_4 = ['deposit', 'saving', 'mortgageLoan', 'rentHouseLoan']

  const mPK = ref()
  const token = ref(null)
  const Uname = ref('name')
  const Uemail = ref('abc@abcd.com')
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

    let { username, email, password , password2, birth_date } = payload
    console.log({ username, email, password, password2, birth_date })
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, email, password, birth_date
      }
    })
      .then((res) => {
        // console.log(res)
        console.log('회원가입 성공')
        username = email
        const password = password2

        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,  // 로그인 API
      withCredentials: true,  // 쿠키와 함께 전송
      data: {
        username: username,
        password: password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        mPK.value = res.data.user_pk
        Uname.value = res.data.username
        Uemail.value = username

        type_a_4.forEach(item => getSurveyData(mPK.value, item))
        
        router.push({ name: 'HomeView' })
        console.log('로그인 성공')
      })
      .catch((err) => {
        console.log(err)
      }
    )
  }
  
  // [추가기능] 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        mPK.value = null
        surveyData.value = {
          'deposit' : { ...initialSurveyData },
          'saving' : { ...initialSurveyData },
          'mortgageLoan' : { ...initialSurveyData },
          'rentHouseLoan' : { ...initialSurveyData },
        };  // 초기 상태로 되돌리기
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createSurvey = function (typea) {
    surveyData.value[typea].type_a = typea
    // console.log(token.value)
    // console.log('확인용', surveyData.value)
    axios({
      method: 'post',
      url: `${API_URL}/accounts/survey/start/`,
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: surveyData.value[typea],
    }
  )
    .then((response) => {
      surveyData.value[typea] = response.data
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
  // api요청
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
  // api요청
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
  // api요청
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
  // api요청
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
  // 데이터베이스 요청
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

  // survey 데이터 가져오는 함수
  const getSurveyData = function (user_id, type) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/survey/${user_id}/${type}`,  // survey 데이터를 가져올 API endpoint
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then((response) => {
        const survey = response.data
        console.log(survey)
        if (!survey) {
          console.log('Survey생성',survey)
          createSurvey(type)
        } else {
          console.log('Survey확인',survey)
          surveyData.value[type] = survey.surveyData
        }
        console.log('Survey Data Loaded:', surveyData.value)
      })
      .catch((err) => {
        console.log('Error loading survey data:', err)
      })
  }

  // survey 데이터 수정 함수 (PUT 요청)
  const updateSurveyData = function (SurveyId, updatedData, typea) {
  axios({
    method: 'put',
    url: `${API_URL}/accounts/survey/${SurveyId}/`,  // 특정 surveyId에 해당하는 URL로 PUT 요청
    data: updatedData,  // 수정할 데이터
  })
    .then((response) => {
      console.log('Survey Data Updated:', response.data)
      surveyData.value[typea] = response.data  // 수정된 데이터를 업데이트
    })
    .catch((err) => {
      console.log('Error updating Survey data:', err)
    })
}

  //공지사항
  const announcements = ref({})
  const getAnnouncementData = function () {
    
    axios({
      method: 'get',
      url: `${API_URL}/accounts/announcement/`,
    })
      .then((response) => {
        announcements.value = response.data
        console.log(announcements.value)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  //은행 타입
  const selected = ref(0)
  const checkType = function(sel) {
    selected.value = sel
  }
  
  return { companyList, companyListOption, 
    integrationProducts, integrationProductOptions, 
    API_URL, surveyData,
    getCompany, getIntegration, getcompany,
    getdeposit, getsaving, getmortgageLoan, getrentHouseLoan, delete_data,
    getSurveyData, updateSurveyData,
    signUp, logIn, token, isLogin, logOut,getAnnouncementData, 
    announcements, mPK, createSurvey, selected, checkType, 
    Uname, Uemail
   }
}, { persist: true })
