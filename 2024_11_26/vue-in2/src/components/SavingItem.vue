<template>
  <div v-if="bank.type_a=='saving'" class="bg-white rounded-lg shadow-md p-6 space-y-6 relative min-h-[300px]">
    <!-- 은행 이름과 상품명 -->
    <div>
      <h2 class="text-2xl font-semibold text-gray-800 mb-2">{{ index + 1 }}. {{ bank.fin_prdt_nm }}</h2>
      <p class="text-sm text-gray-500">{{ bank.kor_co_nm }}</p>
    </div>

    <!-- 금리 정보 -->
    <div class="border-t border-gray-200 pt-4 pb-16 space-y-3">
      <div class="text-sm text-gray-700">
        <p><span class="font-medium text-blue-600">만기 후 1개월 이내:</span> {{ bank.mtrt_int }}</p>
        <p><span class="font-medium text-blue-600">1개월 초과 6개월 이내:</span> {{ bank.loan_inci_expn }}</p>
        <p><span class="font-medium text-blue-600">6개월 초과:</span> 예금</p>
      </div>
    </div>

    <!-- 댓글 토글 버튼 -->
    <div class="absolute bottom-6 left-0 right-0 flex justify-center">
      <button
        @click="Commentshow(bank, index)"
        class="bg-gradient-to-r from-indigo-500 to-purple-600 text-white px-6 py-2 rounded-xl shadow-md hover:from-indigo-600 hover:to-purple-700 transition duration-300"
      >
        댓글 보기
      </button>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'; // Vue 상태 관리
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

defineProps({
  bank: Object,
  index: Number
})

const Commentshow = (bank, index) => {
  if (store.isLogin) {
    if (store.isCommentVisible === bank) {
      store.isCommentVisible = null
      store.indexnumber = null
    } else {
      store.isCommentVisible = bank
      store.indexnumber = index
    }
  } else {
    alert('로그인이 필요합니다.')
  }
}
</script>

<style scoped>
/* 스타일링 추가 */
.bg-white {
  background-color: #fff;
}

.text-blue-600 {
  color: #3b82f6;
}

.bg-gradient-to-r {
  background-image: linear-gradient(to right, #6366f1, #8b5cf6);
}

.shadow-md {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.shadow-inner {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.05);
}

.rounded-lg {
  border-radius: 12px;
}

.rounded-xl {
  border-radius: 20px;
}

.transition {
  transition: all 0.3s ease-in-out;
}

.hover\:bg-blue-600:hover {
  background-color: #2563eb;
}
</style>