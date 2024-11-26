<template>
  <div class="p-6 bg-indigo-50 ">
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
        <p class="text-gray-600">상품 유형: 예금</p>
        
        <div class="flex justify-between mt-2">
          <!-- 좋아요 버튼 (왼쪽 정렬) -->
          <button 
            class="px-4 py-2 bg-red-200 hover:bg-red-200 rounded-lg text-red-600" 
            @click.stop="store.toggleLike(bank.id)"
          >
            <div v-if="store.is_liked.liked_articles && store.is_liked.liked_articles.find(item => item.id === bank.id)">
              {{ "❤️ 좋아요 취소" }}
            </div>
            <div v-else>
              {{ "🤍 좋아요" }}
            </div>
          </button>
          
          <!-- URL 버튼 (오른쪽 정렬) -->
          <button @click.stop="handclick">
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
            && (deposit.intr_rate_type_nm.length === 0 || deposit.intr_rate_type_nm.includes(option.intr_rate_type_nm))
            && (deposit.save_trm.length === 0 || deposit.save_trm.includes(option.save_trm))
            && (deposit.intr_rate > option.intr_rate || !deposit.intr_rate)
            && (deposit.intr_rate2 > option.intr_rate2 || !deposit.intr_rate2)"
            class="border rounded-lg shadow-sm"
          >
            <!-- 옵션 상세 정보 바로 보여줌 -->
            <div class="bg-gray-50 p-4">
              <p class="font-medium text-gray-800">{{ option.intr_rate_type_nm }}</p>
              <p class="text-gray-600">기간: {{ option.save_trm }}</p>
              <p class="text-gray-600">기본 금리: {{ option.intr_rate }}%</p>
              <p class="text-gray-600">우대 금리: {{ option.intr_rate2 }}%</p>
            </div>
          </div>
        </div>
      </div>
    </ul>
  </div>

</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { onMounted } from 'vue';
import { computed } from 'vue'

const store = useCounterStore()
const deposit = store.surveyData.deposit
// const bank = store.bank
const props = defineProps({
  bank: Object,
  product: Object
})

const handclick = () => {
  if (!store.token) {
    const errorMessage = err.response?.data?.error || '로그인이 필요합니다.';
    console.log('에러')
    alert(errorMessage)
  }
}
// onMounted(() => {
//   // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
//   store.visibleItems()
// })

const formattedMtrtInt = computed(() => {
  // bank.mtrt_int에서 개행 문자를 <br>로 변환
  return props.bank.mtrt_int.replace(/\n/g, "<br>");
});

store.integrationProductOptions.forEach(option => (option.open = false));
</script>
<style  scoped>

</style>