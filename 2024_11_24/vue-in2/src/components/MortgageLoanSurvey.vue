<template>
  <div class="min-h-screen bg-gradient-to-r from-indigo-100 to-blue-50 p-8">
    <div class="max-w-4xl mx-auto space-y-8">
      <!-- 페이지 헤더 -->
      <div class="text-center">
        <h1 class="text-3xl font-bold text-indigo-700">💬 주택 담보 대출</h1>
        <p class="text-gray-600 mt-2">Please fill out the form to provide your lending preferences.</p>
      </div>

      <!-- 설문 내용 -->
      <div class="space-y-6">
        <!-- 질문 1: 은행 이름 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">1. 은행이름</h2>
          <div class="space-y-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.kor_co_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.kor_co_nm" @change="toggleAll('kor_co_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="bank in ['한화생명보험주식회사', '삼성생명보험주식회사', '흥국생명보험주식회사', '교보생명보험주식회사', '하나생명보험주식회사']" :key="bank" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.kor_co_nm.includes(bank) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="bank" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ bank }}</span>
            </label>
          </div>
        </div>

        <!-- 질문 2: 상환 방식 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">2. 상환방식</h2>
          <div class="space-y-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.rpay_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.rpay_type_nm" @change="toggleAll('rpay_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="type in ['분할상환방식', '만기일시상환방식']" :key="type" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.rpay_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="type" v-model="surveyData.rpay_type_nm" @change="checkAllCondition('rpay_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ type }}</span>
            </label>
          </div>
        </div>

        <!-- 질문 3: 금리 유형 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">3. 금리유형</h2>
          <div class="space-y-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.lend_rate_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.lend_rate_type_nm" @change="toggleAll('lend_rate_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="type in ['고정금리', '변동금리']" :key="type" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.lend_rate_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="type" v-model="surveyData.lend_rate_type_nm" @change="checkAllCondition('lend_rate_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ type }}</span>
            </label>
          </div>
        </div>

        <!-- 질문 4, 5, 6: 금리 입력 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">4. 금리를 선택하세요</h2>
          <div class="space-y-4 mt-4">
            <div>
              <label class="block text-gray-700 font-medium mb-2">최소 금리</label>
              <input v-model="surveyData.lend_rate_min" type="number" placeholder="Enter minimum interest rate" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
            </div>
            <div>
              <label class="block text-gray-700 font-medium mb-2">최대 금리</label>
              <input v-model="surveyData.lend_rate_max" type="number" placeholder="Enter maximum interest rate" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
            </div>
            <div>
              <label class="block text-gray-700 font-medium mb-2">평균 금리</label>
              <input v-model="surveyData.lend_rate_avg" type="number" placeholder="Enter average interest rate" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
            </div>
          </div>
        </div>

        <!-- 질문 7: 담보 유형 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">5. 담보유형</h2>
          <div class="space-y-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.mrtg_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.mrtg_type_nm" @change="toggleAll('mrtg_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="type in ['아파트', '아파트외']" :key="type" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.mrtg_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="type" v-model="surveyData.mrtg_type_nm" @change="checkAllCondition('mrtg_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ type }}</span>
            </label>
          </div>
        </div>
      </div>

      <!-- 저장 버튼 -->
      <div class="text-center mt-8">
        <button @click="submitSurvey" class="px-6 py-3 bg-indigo-600 text-white text-lg font-semibold rounded-full shadow-lg hover:bg-indigo-700 focus:outline-none focus:ring-4 focus:ring-indigo-300 transition duration-200">
          저장
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'

// Store 사용
const store = useCounterStore()

const props = defineProps({
  surveyData: Object
});

// `전체` 체크박스를 선택했는지 여부를 추적하는 객체
const isAllSelected = ref({
  kor_co_nm: false,
  rpay_type_nm: false,
  lend_rate_type_nm: false,
  mrtg_type_nm: false
})

// `전체` 체크박스를 선택하거나 해제할 때 호출되는 함수
const toggleAll = (field) => {
  if (isAllSelected.value[field]) {
    if (field === 'kor_co_nm') {
      props.surveyData[field] = ['한화생명보험주식회사', '삼성생명보험주식회사', '흥국생명보험주식회사', '교보생명보험주식회사', '하나생명보험주식회사']
    } else if (field === 'rpay_type_nm') {
      props.surveyData[field] = ['분할상환방식', '만기일시상환방식']
    } else if (field === 'lend_rate_type_nm') {
      props.surveyData[field] = ['고정금리', '변동금리']
    } else if (field === 'mrtg_type_nm') {
      props.surveyData[field] = ['아파트', '아파트외']
    }
  } else {
    props.surveyData[field] = []
  }
}

// 각 항목의 체크 상태를 반영하여 '전체' 체크박스를 업데이트
const checkAllCondition = (field) => {
  if (field === 'kor_co_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 5
  } else if (field === 'rpay_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  } else if (field === 'lend_rate_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  } else if (field === 'mrtg_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2
  }
}

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || [],
    'rpay_type_nm': props.surveyData['rpay_type_nm'] || [],
    'lend_rate_type_nm': props.surveyData['lend_rate_type_nm'] || [],
    'lend_rate_min': props.surveyData['lend_rate_min'] || null,
    'lend_rate_max': props.surveyData['lend_rate_max'] || null,
    'lend_rate_avg': props.surveyData['lend_rate_avg'] || null,
    'mrtg_type_nm': props.surveyData['mrtg_type_nm'] || [],
  }
  // 데이터가 이미 존재하면 업데이트
  console.log('수정', newSurveyData)
  store.updateSurveyData(props.surveyData.id, newSurveyData, 'mortgageLoan') 
}
</script>

<style scoped>
</style>