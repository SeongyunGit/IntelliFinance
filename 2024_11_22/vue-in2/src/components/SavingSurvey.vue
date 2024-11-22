<template>
  <div class="min-h-screen bg-gradient-to-r from-indigo-100 to-blue-50 p-8">
  <div class="max-w-4xl mx-auto space-y-8">
    <!-- 페이지 헤더 -->
    <div class="text-center">
      <h1 class="text-3xl font-bold text-indigo-700">💬 적금 설문</h1>
      <p class="text-gray-600 mt-2">Please fill out the form to find the best deposit options!</p>
    </div>

    <!-- 질문 카드 -->
    <div class="space-y-6">
      <!-- 질문 1: 은행 선택 -->
      <div class="bg-white shadow-lg rounded-xl p-6">
        <h2 class="text-lg font-semibold text-gray-800">1. 선호하는 은행을 선택하세요</h2>
        <div class="flex flex-wrap gap-4 mt-4">
          <label
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="isAllSelected.kor_co_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              v-model="isAllSelected.kor_co_nm"
              @change="toggleAll('kor_co_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">전체</span>
          </label>
          <label
            v-for="bank in ['국민은행', '우리은행', '신한은행', '농협은행주식회사', '카카오']"
            :key="bank"
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="surveyData.kor_co_nm.includes(bank) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              :value="bank"
              v-model="surveyData.kor_co_nm"
              @change="checkAllCondition('kor_co_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">{{ bank }}</span>
          </label>
        </div>
      </div>

      <!-- 질문 2: 이자율 유형 -->
      <div class="bg-white shadow-lg rounded-xl p-6">
        <h2 class="text-lg font-semibold text-gray-800">2. 이자율 유형을 선택하세요</h2>
        <div class="flex space-x-4 mt-4">
          <label
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="isAllSelected.intr_rate_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              v-model="isAllSelected.intr_rate_type_nm"
              @change="toggleAll('intr_rate_type_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">전체</span>
          </label>
          <label
            v-for="type in ['단리', '복리']"
            :key="type"
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="surveyData.intr_rate_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              :value="type"
              v-model="surveyData.intr_rate_type_nm"
              @change="checkAllCondition('intr_rate_type_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">{{ type }}</span>
          </label>
        </div>
      </div>

      <!-- 질문 3: 저축 기간 -->
      <div class="bg-white shadow-lg rounded-xl p-6">
        <h2 class="text-lg font-semibold text-gray-800">3. 저축 기간을 선택하세요</h2>
        <div class="grid grid-cols-4 gap-4 mt-4">
          <label
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="isAllSelected.save_trm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              v-model="isAllSelected.save_trm"
              @change="toggleAll('save_trm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">전체</span>
          </label>
          <label
            v-for="term in ['1', '3', '6', '12','24','36']"
            :key="term"
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="surveyData.save_trm.includes(term) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              :value="term"
              v-model="surveyData.save_trm"
              @change="checkAllCondition('save_trm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">{{ term }} 개월</span>
          </label>
        </div>
      </div>

      <!-- 질문 4, 5: 금리 입력 -->
      <div class="bg-white shadow-lg rounded-xl p-6">
        <h2 class="text-lg font-semibold text-gray-800">4. 금리를 입력하세요</h2>
        <div class="space-y-4 mt-4">
          <div>
            <label class="block text-gray-700 font-medium mb-2">기본 금리</label>
            <input
              v-model="surveyData.intr_rate"
              type="number"
              placeholder="Enter interest rate"
              class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300"
            />
          </div>
          <div>
            <label class="block text-gray-700 font-medium mb-2">우대 금리</label>
            <input
              v-model="surveyData.intr_rate2"
              type="number"
              placeholder="Enter preferential interest rate"
              class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300"
            />
          </div>
        </div>
      </div>

      <!-- 질문 6: 적립방식 유형 -->
      <div class="bg-white shadow-lg rounded-xl p-6">
        <h2 class="text-lg font-semibold text-gray-800">5. 적립방식을 선택하세요</h2>
        <div class="flex space-x-4 mt-4">
          <label
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="isAllSelected.rsrv_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              v-model="isAllSelected.rsrv_type_nm"
              @change="toggleAll('rsrv_type_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">전체</span>
          </label>
          <label
            v-for="type in ['정액적립식', '자유적립식']"
            :key="type"
            class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md"
            :class="surveyData.rsrv_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
            <input
              type="checkbox"
              :value="type"
              v-model="surveyData.rsrv_type_nm"
              @change="checkAllCondition('rsrv_type_nm')"
              class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500"
            />
            <span class="text-gray-700">{{ type }}</span>
          </label>
        </div>
      </div>
    </div>

    <!-- 저장 버튼 -->
    <div class="text-center mt-8">
      <button
        @click="submitSurvey"
        class="px-6 py-3 bg-indigo-600 text-white text-lg font-semibold rounded-full shadow-lg hover:bg-indigo-700 focus:outline-none focus:ring-4 focus:ring-indigo-300 transition duration-200"
      >
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
  intr_rate_type_nm: false,
  save_trm: false,
  kor_co_nm: false,
  rsrv_type_nm: false,
})

// `전체` 체크박스를 선택하거나 해제할 때 호출되는 함수
const toggleAll = (field) => {
  if (isAllSelected.value[field]) {
    // '전체'가 체크되면 모든 항목을 선택
    if (field === 'intr_rate_type_nm') {
      props.surveyData[field] = ['단리', '복리']
    } else if (field === 'save_trm') {
      props.surveyData[field] = ['1', '3', '6', '12', '24', '36']
    } else if (field === 'kor_co_nm') {
      props.surveyData[field] = ['국민은행', '우리은행', '신한은행', '농협은행주식회사', '카카오']
    } else if (field === 'rsrv_type_nm') {
      // 적립방식 선택지 (정액적립식, 자유적립식)
      props.surveyData[field] = ['정액적립식', '자유적립식']
    }
  } else {
    // '전체'가 해제되면 모든 항목을 해제
    props.surveyData[field] = []
  }
}

// 각 항목의 체크 상태를 반영하여 '전체' 체크박스를 업데이트
const checkAllCondition = (field) => {
  if (field === 'intr_rate_type_nm') {
    // '단리', '복리'가 모두 체크되면 '전체' 체크
    isAllSelected.value[field] = props.surveyData[field].length === 2 
  } else if (field === 'save_trm') {
    // 1, 3, 6, 12개월이 모두 체크되면 '전체' 체크
    isAllSelected.value[field] = props.surveyData[field].length === 6
  } else if (field === 'kor_co_nm') {
    // 모든 은행이 체크되면 '전체' 체크
    isAllSelected.value[field] = props.surveyData[field].length === 5 
  } else if (field === 'rsrv_type_nm') {
    // '정액적립식'과 '자유적립식'이 모두 체크되면 '전체' 체크
    isAllSelected.value[field] = props.surveyData[field].length === 2;
  }
}

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || [],
    'intr_rate_type_nm': props.surveyData['intr_rate_type_nm'] || [],
    'save_trm': props.surveyData['save_trm'] || [],
    'intr_rate': props.surveyData['intr_rate'] || null,
    'intr_rate2': props.surveyData['intr_rate2'] || null,
    'rsrv_type_nm': props.surveyData['rsrv_type_nm'] || [],
  }
  // 데이터가 이미 존재하면 업데이트
  console.log('수정', newSurveyData)
  store.updateSurveyData(props.surveyData.id, newSurveyData, 'saving') 
}
</script>

<style scoped>
</style>
