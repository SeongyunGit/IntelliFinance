<template>
  <div class="min-h-screen bg-gradient-to-r from-indigo-100 to-blue-50 p-8">
  <div class="max-w-6xl mx-auto space-y-8">
    <!-- 페이지 헤더 -->
    <div class="text-center">
      <h3 class="text-3xl font-semibold text-indigo-700 mb-4">💬 설문</h3>
    </div>

    <div class="flex space-x-8">
      <div class="w-1/2">
        <!-- 금융 기관명 (체크박스, 복수 선택 가능) -->
        <ul class="select-list bg-white shadow-lg rounded-xl p-6 space-y-4">
          <li @click="fetchData(1)" class="cursor-pointer p-4 border-b hover:bg-indigo-50">
            <span :class="{ active: selected == 1 }" class="text-gray-800 text-lg font-medium">예금</span>
          </li>
          <li @click="fetchData(2)" class="cursor-pointer p-4 border-b hover:bg-indigo-50">
            <span :class="{ active: selected == 2 }" class="text-gray-800 text-lg font-medium">적금</span>
          </li>
          <li @click="fetchData(3)" class="cursor-pointer p-4 border-b hover:bg-indigo-50">
            <span :class="{ active: selected == 3 }" class="text-gray-800 text-lg font-medium">주택담보대출</span>
          </li>
          <li @click="fetchData(4)" class="cursor-pointer p-4 hover:bg-indigo-50">
            <span :class="{ active: selected == 4 }" class="text-gray-800 text-lg font-medium">전세자금대출</span>
          </li>
        </ul>
        <div class="mt-8">
          <DepositSurvey v-if="selected == 1" :surveyData="store.surveyData.deposit" />
          <SavingSurvey v-if="selected == 2" :surveyData="store.surveyData.saving" />
          <MortgageLoanSurvey v-if="selected == 3" :surveyData="store.surveyData.mortgageLoan" />
          <RentHouseLoanSurvey v-if="selected == 4" :surveyData="store.surveyData.rentHouseLoan" />
        </div>
      </div>

      <div class="w-1/2">
        <div class="space-y-8">
          <DepositList v-if="selected == 1" :surveyData="store.surveyData.deposit" />
          <SavingList v-if="selected == 2" :surveyData="store.surveyData.saving" />
          <MortgageLoanList v-if="selected == 3" :surveyData="store.surveyData.mortgageLoan" />
          <RentHouseLoanList v-if="selected == 4" :surveyData="store.surveyData.rentHouseLoan" />
        </div>
      </div>
    </div>
  </div>
</div>


</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref, watch } from 'vue'
import DepositSurvey from './DepositSurvey.vue';
import SavingSurvey from './SavingSurvey.vue';
import DepositList from './DepositList.vue';
import SavingList from './SavingList.vue';

import MortgageLoanSurvey from '@/components/MortgageLoanSurvey.vue';
import MortgageLoanList from '@/components/MortgageLoanList.vue';
import RentHouseLoanSurvey from '@/components/RentHouseLoanSurvey.vue';
import RentHouseLoanList from '@/components/RentHouseLoanList.vue';

// Store 사용
const store = useCounterStore()

const selected = ref(0)
const fetchData = (sel) => {
  selected.value = sel
}
// const deposit = store.surveyData.deposit
</script>

<style scoped>
</style>
