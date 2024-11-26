<template>
  <div class=" bg-gradient-to-br from-indigo-50 to-blue-100 p-6 flex justify-center">
    <div class="w-full max-w-2xl bg-white rounded-3xl shadow-2xl overflow-hidden">
      <!-- 헤더 -->
      <div class="bg-indigo-600 text-white p-6 text-center">
        <h1 class="text-3xl font-bold mb-2">🏠 주택 담보 대출</h1>
        <p class="text-indigo-100">나만의 최적 주택 담보 대출 옵션을 찾아보세요!</p>
      </div>
      
      <div class="p-6 space-y-6">
        <!-- 은행 선택 드롭다운 -->
        <div class="bg-white rounded-2xl shadow-lg p-6 space-y-4">
          <div class="flex items-center space-x-3 text-lg font-semibold text-indigo-700">
            <span class="mr-2">🏦</span>
            <h2>1. 은행을 선택하세요</h2>
          </div>
        <div class="relative">
          <button 
            @click="isDropdownOpen = !isDropdownOpen"
            class="w-full flex items-center justify-between p-4 bg-gray-100 rounded-lg text-left"
          >
            <div class="flex items-center space-x-3">
              <span class="mr-2">🏦</span>
              <span>
                {{ surveyData.kor_co_nm.length > 0 
                  ? surveyData.kor_co_nm.join(', ') 
                  : '은행을 선택하세요' }}
              </span>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-gray-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4 4a.75.75 0 01-1.06 0l-4-4a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
            </svg>
          </button>
          
          <!-- 은행 드롭다운 메뉴 -->
          <div 
            v-if="isDropdownOpen" 
            class="absolute z-10 mt-2 w-full bg-white border rounded-lg shadow-lg max-h-60 overflow-auto"
          >
            <div 
              v-for="bank in allBanks" 
              :key="bank" 
              class="p-3 cursor-pointer hover:bg-indigo-50 flex items-center"
              @click="toggleBank(bank)"
            >
              <input 
                type="checkbox" 
                :value="bank" 
                :checked="surveyData.kor_co_nm.includes(bank)"
                class="mr-3 rounded text-indigo-600 focus:ring-indigo-500"
              />
              {{ bank }}
            </div>
          </div>
        </div>
        </div>
        <!-- 질문 2: 상환 방식 -->
        <div class="bg-white rounded-2xl shadow-lg p-6 space-y-4">
          <div class="flex items-center space-x-3 text-lg font-semibold text-indigo-700">
            <span class="mr-2">📊</span>
            <h2>2. 상환방식</h2>
          </div>
          
          <div class="grid grid-cols-2 gap-3">
            <label 
              v-for="type in ['분할상환방식', '만기일시상환방식']" 
              :key="type"
              class="flex flex-col items-center justify-center p-4 rounded-lg cursor-pointer transition text-center border border-purple-300"
              :class="surveyData.rpay_type_nm.includes(type) 
                ? 'bg-indigo-50 border-2 border-indigo-500' 
                : 'hover:bg-gray-50'"
            >
              <input 
                type="checkbox" 
                :value="type" 
                v-model="surveyData.rpay_type_nm"
                class="absolute opacity-0"
              />
              <span class="text-gray-700">
                {{ type }}
              </span>
            </label>
          </div>
        </div>



        <!-- 질문 3: 금리유형 -->
        <div class="bg-white rounded-2xl shadow-lg p-6 space-y-4">
          <div class="flex items-center space-x-3 text-lg font-semibold text-indigo-700">
            <span class="mr-2">⏳</span>
            <h2>3. 금리유형</h2>
          </div>
          
          <div class="grid grid-cols-2 gap-3">
            <label 
              v-for="type in ['고정금리', '변동금리']" 
              :key="type"
              class="flex flex-col items-center justify-center p-4 rounded-lg cursor-pointer transition text-center border border-purple-300"
              :class="surveyData.lend_rate_type_nm.includes(type) 
                ? 'bg-indigo-50 border-2 border-indigo-500' 
                : 'hover:bg-gray-50'"
            >
              <input 
                type="checkbox" 
                :value="type" 
                v-model="surveyData.lend_rate_type_nm"
                class="absolute opacity-0"
              />
              <span class="text-gray-700">
                {{ type }}
              </span>
            </label>
          </div>
        </div>
      

        <!-- 질문 4: 금리 입력 -->
        <div class="bg-white rounded-2xl shadow-lg p-6 space-y-4">
          <div class="flex items-center space-x-3 text-lg font-semibold text-indigo-700">
            <span class="mr-2">💰</span>
            <h2>4. 금리를 선택하세요</h2>
          </div>
          
          <div class="">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                최소 금리
              </label>
              <input 
                v-model="surveyData.lend_rate_min" 
                type="number" 
                placeholder="최소 금리 입력" 
                class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-300"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                최대 금리
              </label>
              <input 
                v-model="surveyData.lend_rate_max" 
                type="number" 
                placeholder="최대 금리 입력" 
                class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-300"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                평균 금리
              </label>
              <input 
                v-model="surveyData.lend_rate_avg" 
                type="number" 
                placeholder="평균 금리 입력" 
                class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-300"
              />
            </div>
          </div>
        </div>


        <!-- 질문 7: 담보 유형 -->
        <div class="bg-white rounded-2xl shadow-lg p-6 space-y-4">
          <div class="flex items-center space-x-3 text-lg font-semibold text-indigo-700">
            <span class="mr-2">💍</span>
            <h2>5. 담보 유형</h2>
          </div>
          
          <div class="grid grid-cols-2 gap-3">
            <label 
              v-for="type in ['아파트', '아파트외']" 
              :key="type"
              class="flex flex-col items-center justify-center p-4 rounded-lg cursor-pointer transition text-center border border-purple-300"
              :class="surveyData.mrtg_type_nm.includes(type) 
                ? 'bg-indigo-50 border-2 border-indigo-500' 
                : 'hover:bg-gray-50'"
            >
              <input 
                type="checkbox" 
                :value="type" 
                v-model="surveyData.mrtg_type_nm"
                class="absolute opacity-0"
              />
              <span class="text-gray-700">
                {{ type }}
              </span>
            </label>
          </div>
        </div>
      </div>
      
      <!-- 저장 버튼 -->
      <div class="bg-gray-100 p-6 text-center">
        <button 
          @click="submitSurvey"
          class="w-full py-4 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 transition duration-300 flex items-center justify-center space-x-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
          <span>저장</span>
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

const isDropdownOpen = ref(false);
const allBanks = ['한화생명보험주식회사','에이비엘생명보험주식회사','삼성생명보험주식회사','흥국생명보험주식회사','교보생명보험주식회사','하나생명보험주식회사','동양생명보험주식회사','삼성화재해상보험주식회사', '현대해상화재보험주식회사','주식회사KB손해보험', '푸본현대생명보험주식회사', '농협손해보험주식회사'];

const toggleBank = (bank) => {
  const banks = props.surveyData.kor_co_nm;
  const index = banks.indexOf(bank);
  
  if (index > -1) {
    // 이미 선택된 은행이면 제거
    banks.splice(index, 1);
  } else {
    // 선택되지 않은 은행이면 추가
    banks.push(bank);
  }
};

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