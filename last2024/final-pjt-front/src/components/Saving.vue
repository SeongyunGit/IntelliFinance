<template>
  <div class="container mx-auto min-h-screen bg-gradient-to-b from-indigo-600 to-indigo-500 p-8">
    <h3 class="text-3xl font-bold text-center text-white mb-8">적금</h3>
    <!-- 카드 리스트 -->
    <div class="grid grid-cols-3 gap-4 p-4">
      <template v-for="(bank, index) in store.integrationProducts.filter(product => product.type_a === 'saving')" :key="bank.id">
        <SavingItem
          class="bg-white rounded-lg shadow-md p-6"
          :bank="bank"
          :index="index"
        />
        <!-- 댓글창 표시 로직 -->
        <div
          v-if="store.indexnumber !== null && shouldShowComment(index)"
          class="col-span-3 bg-gray-50 p-4 rounded-xl shadow-inner mt-4"
        >
          <CommentDetail :bank="store.isCommentVisible" />
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import SavingItem from "./SavingItem.vue";
import CommentDetail from "@/components/CommentDetail.vue";
import { onMounted } from 'vue';

const store = useCounterStore();

// 댓글창 표시 여부를 결정하는 함수
const shouldShowComment = (currentIndex) => {
  const clickedIndex = store.indexnumber;
  if (currentIndex < clickedIndex) return false;
  
  // 전체 상품 목록의 길이를 가져옴
  const totalItems = store.integrationProducts.filter(product => product.type_a === 'saving').length;
  
  // 마지막 행의 처리: 마지막 인덱스에서 댓글창 표시
  if (clickedIndex >= totalItems - 2 && currentIndex === totalItems - 1) {
    return true;
  }
  
  // 기존 로직
  return currentIndex % 3 === 2 && 
         currentIndex >= clickedIndex && 
         currentIndex === Math.ceil((clickedIndex + 1) / 3) * 3 - 1;
};

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.isCommentVisible = null
  store.indexnumber = null
})
</script>