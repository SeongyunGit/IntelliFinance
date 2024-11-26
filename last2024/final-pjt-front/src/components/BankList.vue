<template>
  <div class="container mx-auto min-h-screen bg-gradient-to-b from-indigo-600 to-indigo-500 p-8">
    <h3 class="text-3xl font-bold text-center text-white mb-8">은행</h3>
    
    <!-- 카드 리스트 -->
    <div class="grid grid-cols-3 gap-4 p-4">
      <template v-for="(bank, index) in store.companyList" :key="bank.fin_co_no">
        <BankListItem
          :bank="bank"
          :index="index"
          @click="toggleDetails(index)"
        />
        <!-- 상세 정보 표시 -->
        <div
          v-if="clickedCardIndex !== null && shouldShowDetails(index)"
          class="col-span-3 bg-gray-50 p-4 rounded-xl shadow-inner mt-4"
        >
          <div class="details p-6">
            <h6 class="font-semibold text-lg text-gray-800 mb-4">상세 정보({{ store.companyList[clickedCardIndex].kor_co_nm }})</h6>
            <p class="text-gray-700 mb-2">은행 코드: {{ store.companyList[clickedCardIndex].fin_co_no }}</p>
            <p class="text-gray-700 mb-2">대표자: {{ store.companyList[clickedCardIndex].dcls_chrg_man }}</p>
            <p class="text-gray-700 mb-2">
              홈페이지: 
              <a 
                :href="store.companyList[clickedCardIndex].homp_url" 
                class="text-blue-500 hover:underline" 
                target="_blank"
              >
                {{ store.companyList[clickedCardIndex].homp_url }}
              </a>
            </p>
            <p class="text-gray-700">주소: {{ store.companyList[clickedCardIndex].address || '정보 없음' }}</p>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import BankListItem from '@/components/BankListItem.vue'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore()
const clickedCardIndex = ref(null)

function toggleDetails(index) {
  clickedCardIndex.value = clickedCardIndex.value === index ? null : index
}

// 상세 정보 표시 여부를 결정하는 함수
const shouldShowDetails = (currentIndex) => {
  const clickedIndex = clickedCardIndex.value
  if (currentIndex < clickedIndex) return false
  
  const totalItems = store.companyList.length
  
  if (clickedIndex >= totalItems - 2 && currentIndex === totalItems - 1) {
    return true
  }
  
  return currentIndex % 3 === 2 && 
         currentIndex >= clickedIndex && 
         currentIndex === Math.ceil((clickedIndex + 1) / 3) * 3 - 1
}
</script>