<template>
  <div v-if="bank.type_a=='saving'">
    <h2 class="text-lg font-bold text-gray-800 mb-4">{{ bank.fin_prdt_nm }}</h2>
    <p class="text-sm text-gray-500 mb-4">{{ bank.kor_co_nm }}</p>
    <div class="border-t pt-4">
      <div class="text-sm text-gray-600 space-y-2">
        <p><span class="font-medium">만기 후 1개월 이내:</span> {{ bank.mtrt_int }}</p>
        <p><span class="font-medium">1개월 초과 6개월 이내:</span> {{ bank.loan_inci_expn }}</p>
        <p><span class="font-medium">6개월 초과:</span> {{ bank.type_a }}</p>
      </div>
    </div>
    <!-- 댓글 토글 버튼 -->
    <div class="mt-4 text-center">
      <button
        @click="toggleComment"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        {{ isCommentVisible ? '댓글 숨기기' : '댓글 보기' }}
      </button>
    </div>

    <!-- 댓글 컴포넌트 -->
    <div v-if="isCommentVisible" class="mt-4">
      <CommentDetail :bank="bank" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'; // Vue 상태 관리
import CommentDetail from '@/components/CommentDetail.vue';

defineProps({
  bank: Object
})

// 댓글 보임 상태 관리
const isCommentVisible = ref(false);

// 토글 함수
const toggleComment = () => {
  isCommentVisible.value = !isCommentVisible.value;
};
</script>
  