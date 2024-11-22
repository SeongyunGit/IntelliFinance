<template>
  <div class="p-6 bg-indigo-50">
    <ul class="bg-white shadow-lg rounded-lg p-6 max-w-4xl mx-auto">
      <!-- 설문 결과 제목 -->
      <h2 class="text-2xl font-semibold text-blue-600 mb-4">{{ bank.fin_prdt_nm }}</h2>

      <!-- 기본 정보 (클릭 시 옵션 보이도록 설정) -->
      <div
        class="mb-6 p-4 bg-blue-100 hover:bg-blue-200 rounded-lg cursor-pointer"
        @click="bank.open = !bank.open"
      >
        <h5 class="text-lg font-bold text-gray-800">{{ bank.kor_co_nm }}</h5>
        <p class="text-gray-600">만기 이자: {{ bank.mtrt_int }}</p>
        <p class="text-gray-600">상품 유형: {{ bank.type_a }}</p>
      </div>

      <!-- 해당 은행의 상품 옵션 (토글 되어 보여짐) -->
      <div v-if="bank.open">
        <h3 class="text-lg font-semibold text-gray-700 mb-2">추천 상품 옵션</h3>

        <div v-for="(option, index) in store.integrationProductOptions" :key="index" class="mb-4">
          <div
            v-if="option.fin_prdt_cd === bank.fin_prdt_cd
            && (mortgageLoan.rpay_type_nm.length === 0 || mortgageLoan.rpay_type_nm.includes(option.rpay_type_nm))
            && (mortgageLoan.lend_rate_type_nm.length === 0 || mortgageLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm))
            && (mortgageLoan.lend_rate_min > option.lend_rate_min || !mortgageLoan.lend_rate_min)
            && (mortgageLoan.lend_rate_max > option.lend_rate_max || !mortgageLoan.lend_rate_max)
            && (mortgageLoan.lend_rate_avg > option.lend_rate_avg || !mortgageLoan.lend_rate_avg)
            && (mortgageLoan.mrtg_type_nm.length === 0 || mortgageLoan.mrtg_type_nm.includes(option.mrtg_type_nm))
            "
            class="border border-gray-300 rounded-lg shadow-sm"
          >
            <div class="bg-gray-50 p-4">
              <p class="font-medium text-gray-800">{{ option.rpay_type_nm }}</p>
              <p class="text-gray-600">대출 금리 유형: {{ option.lend_rate_type_nm }}</p>
              <p class="text-gray-600">최소 금리: {{ option.lend_rate_min }}%</p>
              <p class="text-gray-600">최대 금리: {{ option.lend_rate_max }}%</p>
              <p class="text-gray-600">평균 금리: {{ option.lend_rate_avg }}%</p>
              <p class="text-gray-600">담보 유형: {{ option.mrtg_type_nm }}</p>
            </div>
            <hr class="my-4" />
          </div>
        </div>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const mortgageLoan = store.surveyData.mortgageLoan

defineProps({
  bank: Object
})
</script>

<style scoped>
/* Scoped styling can be added here if needed */
</style>
