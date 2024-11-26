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
        <p class="text-gray-600" v-html="formattedMtrtInt"></p>
        <p class="text-gray-600" v-html="formattedMtrtInt1"></p>
        <p class="text-gray-600" v-html="formattedMtrtInt2"></p>
        <p class="text-gray-600" v-html="formattedMtrtInt3"></p>
        <p class="text-gray-600">상품 유형: 전세 자금 대출</p>
        
        <div class="flex justify-between mt-2">
        <button
    class="mt-2 px-4 py-2 bg-red-100 hover:bg-red-200 rounded-lg text-red-600"
    @click.stop="store.toggleLike(bank.id)"
  >
  <!-- <p>{{ store.is_liked.liked_articles.id.includes(bank.id) }}</p> -->
     <div v-if="store.is_liked.liked_articles && store.is_liked.liked_articles.find(item => item.id === bank.id)">
      {{ "❤️ 좋아요 취소" }}  
    </div>
    <div v-else>
      {{ "🤍 좋아요" }}
    </div> 
  </button>
      <button>
          <div v-for="item in store.companyList">
            
            <a 
              v-if="item.kor_co_nm === bank.kor_co_nm" 
              :href="item.homp_url"
              class="px-4 py-2 bg-teal-200 hover:bg-blue-200 rounded-lg text-blue-600 inline-block"
            >
            🏦 홈페이지 바로가기
            </a>
          </div>
        </button>
      </div>
      </div>

      <!-- 해당 은행의 상품 옵션 (토글 되어 보여짐) -->
      <div v-if="bank.open">
        <h3 class="text-lg font-semibold text-gray-700 mb-2">추천 상품 옵션</h3>

        <div v-for="(option, index) in store.integrationProductOptions" :key="index" class="mb-4">
          <div
            v-if="option.fin_prdt_cd === bank.fin_prdt_cd
            && (rentHouseLoan.rpay_type_nm.length === 0 || rentHouseLoan.rpay_type_nm.includes(option.rpay_type_nm))
            && (rentHouseLoan.lend_rate_type_nm.length === 0 || rentHouseLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm))
            && (rentHouseLoan.lend_rate_min > option.lend_rate_min || !rentHouseLoan.lend_rate_min)
            && (rentHouseLoan.lend_rate_max > option.lend_rate_max || !rentHouseLoan.lend_rate_max)
            && (rentHouseLoan.lend_rate_avg > option.lend_rate_avg || !rentHouseLoan.lend_rate_avg)
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
import { computed } from 'vue'

const store = useCounterStore()
const rentHouseLoan = store.surveyData.rentHouseLoan


const props = defineProps({
  bank: Object,
  product: Object
})
const formattedMtrtInt = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.loan_inci_expn.replace(/\n/g, "<br>");
});

const formattedMtrtInt1 = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.erly_rpay_fee.replace(/\n/g, "<br>");
});

const formattedMtrtInt2 = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.dly_rate.replace(/\n/g, "<br>");
});

const formattedMtrtInt3 = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.loan_lmt.replace(/\n/g, "<br>");
});




</script>

<style scoped>
/* Scoped styling can be added here if needed */
</style>