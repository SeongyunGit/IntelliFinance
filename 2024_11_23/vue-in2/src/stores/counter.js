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
    'intr_rate_type_nm': [],  // 이자율(단리,복리)
    'save_trm': [],  // 저축기간
    'intr_rate': null,  // 기본금리
    'intr_rate2': null,  // 우대금리
    // 'rsrv_type': None,
    'rsrv_type_nm': [],  // 적립식종류
    // 'rpay_type': None,
    'rpay_type_nm': [],  // 상환방식
    // 'lend_rate_type': None,
    'lend_rate_type_nm': [],  // 금리유형
    'lend_rate_min': null,  // 최소 금리
    'lend_rate_max': null,  // 최대 금리
    'lend_rate_avg': null,  // 평균 금리
    // 'mrtg_type': None,
    'mrtg_type_nm': []  // 담보 유형
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
  const isAdmin = ref(0)
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
        isAdmin.value = res.data.is_staff  // 관리자 여부 저장

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
        Uname.value = 'name'
        Uemail.value = 'abc@abcd.com'
        isAdmin.value = 0
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
  const getcompany2 = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/company/`,
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
      withCredentials:true,
      headers: {
        Authorization: `Token ${token.value}`
      },
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
  
  let bankId = 0
  const is_liked = ref({})
  const toggleLike = function (bank) {
    axios({
      method:'post',
      url: `${API_URL}/api/v1/api/bank/${bank}/like/`,
      withCredentials : true,
      data:{
        'user':mPK.value
      },
      headers: {
        Authorization: `Token ${token.value}`, // 토큰 포함
      },
    })
    .then((response) => {
      is_liked.value = response.data;
      console.log(is_liked)
      visibleItems()
      console.log("성공")
      console.log(response)

    // store의 deposit 데이터 업데이트
      // bankId = deposit.find((b) => b.id === bankId);
      if (bankId) {
        bankId.is_liked = is_liked; // Django에서 반환된 새로운 상태
      }
    })
    .catch((err) => {
      console.log(token.value)
      console.log(err)
      console.log("실패")
    })
  }
  const likeList=ref([])
  const visibleItems = function () {
    axios({
      method:'get',
      url: `${API_URL}/api/v1/api/bank/liked/`,
      withCredentials : true,
      headers: {
        Authorization: `Token ${token.value}`, // 토큰 포함
      },
    })
    .then((response)=> {
      likeList.value = response.data
      console.log(likeList.value)
    })
    .catch((err) => {
      console.log(err)
    })
  }
  

  return { companyList, companyListOption, 
    integrationProducts, integrationProductOptions, 
    API_URL, surveyData,
    getCompany, getIntegration, getcompany2,
    getdeposit, getsaving, getmortgageLoan, getrentHouseLoan, delete_data,
    getSurveyData, updateSurveyData,
    signUp, logIn, token, isLogin, logOut,getAnnouncementData, 
    announcements, mPK, createSurvey, selected, checkType, bankId, toggleLike,
    Uname, Uemail, visibleItems, likeList, is_liked, isAdmin
   }
}, { persist: true })
