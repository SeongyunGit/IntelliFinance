<template>
  <div v-if="bank.type_a=='rentHouseLoan'" class="bg-white rounded-lg shadow-md p-6 space-y-6">
    <!-- 은행 이름과 상품명 -->
    <div>
      <h2 class="text-2xl font-semibold text-gray-800 mb-2">{{ bank.fin_prdt_nm }}</h2>
      <p class="text-sm text-gray-500">{{ bank.kor_co_nm }}</p>
    </div>

    <!-- 금리 정보 -->
    <div class="border-t border-gray-200 pt-4 space-y-3">
      <div class="text-sm text-gray-700">
        <p><span class="font-medium text-blue-600">만기 후 1개월 이내:</span> {{ bank.mtrt_int }}</p>
        <p><span class="font-medium text-blue-600">1개월 초과 6개월 이내:</span> {{ bank.loan_inci_expn }}</p>
        <p><span class="font-medium text-blue-600">6개월 초과:</span> 주택 담보 대출</p>
      </div>
    </div>

    <!-- 댓글 토글 버튼 -->
    <div class="flex justify-center">
      <button
        @click="toggleComment"
        class="bg-gradient-to-r from-indigo-500 to-purple-600 text-white px-6 py-2 rounded-xl shadow-md hover:from-indigo-600 hover:to-purple-700 transition duration-300"
      >
        {{ isCommentVisible ? '댓글 숨기기' : '댓글 보기' }}
      </button>
    </div>

    <!-- 댓글 컴포넌트 -->
    <div v-if="isCommentVisible" class="mt-6 bg-gray-50 p-4 rounded-xl shadow-inner">
      <CommentDetail :bank="bank" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; // Vue 상태 관리
import CommentDetail from '@/components/CommentDetail.vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

defineProps({
  bank: Object
})

// 댓글 보임 상태 관리
const isCommentVisible = ref(false);

// 토글 함수
const toggleComment = () => {
  if (store.isLogin) {
    isCommentVisible.value = !isCommentVisible.value;
  } else {
    alert('로그인이 필요합니다.')
  }
};
</script>
  