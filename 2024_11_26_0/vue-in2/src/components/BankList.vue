<template>
  <div class="container mx-auto p-6">
    <h3 class="text-3xl font-semibold mb-8 text-center text-white">은행</h3>
    
    <!-- 카드 리스트 -->
    <div class="grid grid-cols-3 gap-4 p-4">
      <BankListItem
        v-for="(bank, index) in store.companyList"
        :key="bank.fin_co_no"
        :bank="bank"
        @click="toggleDetails(index)"
        :is-details-visible="clickedCardIndex === index"
      />
    </div>
  </div>
</template>

<script setup>
import BankListItem from '@/components/BankListItem.vue'
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore()

// 클릭된 카드의 인덱스를 저장
const clickedCardIndex = ref(null)

// 카드 클릭 시 인덱스 변경
function toggleDetails(index) {
  clickedCardIndex.value = clickedCardIndex.value === index ? null : index
}
</script>

<style scoped>

/* 필요에 따라 추가적인 스타일을 작성할 수 있습니다. */
</style>
