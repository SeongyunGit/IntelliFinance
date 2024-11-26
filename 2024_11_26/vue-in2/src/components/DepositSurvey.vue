<template>
  
    <div class="max-w-4xl mx-auto space-y-8">
      <!-- 페이지 헤더 -->
      <div class="text-center">
        <h1 class="text-3xl font-bold text-indigo-700">💬 예금</h1>
        <p class="text-gray-600 mt-2">Please fill out the form to find the best deposit options!</p>
      </div>

      <!-- 설문 내용 -->
      <div class="space-y-6">
        <!-- 질문 1: 은행 선택 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">1. 선호하는 은행을 선택하세요</h2>
          <div class="space-y-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.kor_co_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.kor_co_nm" @change="toggleAll('kor_co_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="bank in ['국민은행', '우리은행', '신한은행', '농협은행주식회사', '카카오']" :key="bank" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.kor_co_nm.includes(bank) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="bank" v-model="surveyData.kor_co_nm" @change="checkAllCondition('kor_co_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ bank }}</span>
            </label>
          </div>
        </div>

        <!-- 질문 2: 이자율 유형 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">2. 이자 유형을 선택하세요</h2>
          <div class="flex space-x-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.intr_rate_type_nm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.intr_rate_type_nm" @change="toggleAll('intr_rate_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="type in ['단리', '복리']" :key="type" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.intr_rate_type_nm.includes(type) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="type" v-model="surveyData.intr_rate_type_nm" @change="checkAllCondition('intr_rate_type_nm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ type }}</span>
            </label>
          </div>
        </div>

        <!-- 질문 3: 저축 기간 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">3. 저축 기간을 선택하세요</h2>
          <div class="grid grid-cols-4 gap-4 mt-4">
            <label class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="isAllSelected.save_trm ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" v-model="isAllSelected.save_trm" @change="toggleAll('save_trm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">전체</span>
            </label>
            <label v-for="term in ['1', '3', '6', '12', '24', '36']" :key="term" class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition hover:shadow-md" :class="surveyData.save_trm.includes(term) ? 'bg-indigo-100 border-indigo-500' : 'bg-white border-gray-300'">
              <input type="checkbox" :value="term" v-model="surveyData.save_trm" @change="checkAllCondition('save_trm')" class="form-checkbox h-5 w-5 text-indigo-600 focus:ring-indigo-500" />
              <span class="text-gray-700">{{ term }} 개월</span>
            </label>
          </div>
        </div>

        <!-- 질문 4, 5: 기본 금리와 우대 금리 -->
        <div class="bg-white shadow-lg rounded-xl p-6">
          <h2 class="text-lg font-semibold text-gray-800">4. 금리를 선택하세요</h2>
          <div class="space-y-4 mt-4">
            <div>
              <label class="block text-gray-700 font-medium mb-2">기본 금리</label>
              <input v-model="surveyData.intr_rate" type="number" placeholder="Enter interest rate" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
            </div>
            <div>
              <label class="block text-gray-700 font-medium mb-2">우대 금리</label>
              <input v-model="surveyData.intr_rate2" type="number" placeholder="Enter preferential interest rate" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-300" />
            </div>
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
  
</template>

<script setup>
import { ref, watch } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

const props = defineProps({
  surveyData: Object
});

const isAllSelected = ref({
  intr_rate_type_nm: false,
  save_trm: false,
  kor_co_nm: false
});

const toggleAll = (field) => {
  if (isAllSelected.value[field]) {
    if (field === 'intr_rate_type_nm') {
      props.surveyData[field] = ['단리', '복리'];
    } else if (field === 'save_trm') {
      props.surveyData[field] = ['1', '3', '6', '12', '24', '36'];
    } else if (field === 'kor_co_nm') {
      props.surveyData[field] = ['국민은행', '우리은행', '신한은행', '농협은행주식회사', '카카오'];
    }
  } else {
    props.surveyData[field] = [];
  }
};

const checkAllCondition = (field) => {
  if (field === 'intr_rate_type_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 2;
  } else if (field === 'save_trm') {
    isAllSelected.value[field] = props.surveyData[field].length === 6;
  } else if (field === 'kor_co_nm') {
    isAllSelected.value[field] = props.surveyData[field].length === 5;
  }
};

// 서베이 데이터를 저장하는 함수
const submitSurvey = () => {
  // 데이터를 저장하기 위한 객체
  const newSurveyData = {
    'kor_co_nm': props.surveyData['kor_co_nm'] || [],
    'intr_rate_type_nm': props.surveyData['intr_rate_type_nm'] || [],
    'save_trm': props.surveyData['save_trm'] || [],
    'intr_rate': props.surveyData['intr_rate'] || null,
    'intr_rate2': props.surveyData['intr_rate2'] || null
  }
  // 데이터가 이미 존재하면 업데이트
  console.log('수정', newSurveyData)
  store.updateSurveyData(props.surveyData.id, newSurveyData, 'deposit') 
}
</script>

<style scoped>
/* Customize styles for checkboxes, buttons, etc. */
</style>