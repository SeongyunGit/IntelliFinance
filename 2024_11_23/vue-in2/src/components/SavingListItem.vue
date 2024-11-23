<template>
  <div class="p-6 bg-indigo-50">
  <ul class="bg-white shadow-md rounded-lg p-6 max-w-4xl mx-auto">
    <!-- 설문 결과 제목 -->
    <h2 class="text-2xl font-semibold text-blue-600 mb-4">{{ bank.fin_prdt_nm }}</h2>

    <!-- 기본 정보 (클릭 시 옵션 보이도록 설정) -->
    <div
      class="mb-6 p-4 bg-blue-100 hover:bg-blue-200 rounded-lg cursor-pointer"
      @click="bank.open = !bank.open"
    >
      <h5 class="text-lg font-bold text-gray-800">{{ bank.kor_co_nm }}</h5>
      <p class="text-gray-600" v-html="formattedMtrtInt"></p>
      <p class="text-gray-600">상품 유형: 적금</p>
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
    </div>

    <!-- 해당 은행의 상품 옵션 (토글 되어 보여짐) -->
    <div v-if="bank.open">
      <h3 class="text-lg font-semibold text-gray-700 mb-2">추천 상품 옵션</h3>

      <div v-for="(option, index) in store.integrationProductOptions" :key="index" class="mb-4">
        <div
          v-if="option.fin_prdt_cd === bank.fin_prdt_cd
            && (saving.intr_rate_type_nm.length === 0 || saving.intr_rate_type_nm.includes(option.intr_rate_type_nm))
            && (saving.save_trm.length === 0 || saving.save_trm.includes(option.save_trm))
            && (saving.intr_rate > option.intr_rate || !saving.intr_rate)
            && (saving.intr_rate2 > option.intr_rate2 || !saving.intr_rate2)
            && (saving.rsrv_type_nm.length === 0 || saving.rsrv_type_nm.includes(option.rsrv_type_nm))
            "
          class="border rounded-lg shadow-sm"
        >
          <!-- 옵션 상세 정보 바로 보여줌 -->
          <div class="bg-gray-50 p-4">
            <p class="font-medium text-gray-800">{{ option.intr_rate_type_nm }}</p>
            <p class="text-gray-600">기간: {{ option.save_trm }}</p>
            <p class="text-gray-600">기본 금리: {{ option.intr_rate }}%</p>
            <p class="text-gray-600">우대 금리: {{ option.intr_rate2 }}%</p>
            <p class="text-gray-600">정립 방식: {{ option.rsrv_type_nm }}</p>
          </div>
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
const saving = store.surveyData.saving

const props = defineProps({
  bank: Object,
  product: Object
})
const formattedMtrtInt = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.mtrt_int.replace(/\n/g, "<br>");
});
</script>
<style  scoped>

</style>