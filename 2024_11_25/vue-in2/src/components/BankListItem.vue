<template>
  <div class="mb-8">
    <!-- 카드 내용 -->
    <div class="bg-white border border-gray-200 rounded-lg shadow-lg p-6 cursor-pointer" @click="toggleDetails">
      <h5 class="text-xl font-semibold text-gray-800 mb-2">{{ bank.kor_co_nm }}</h5>
      <p class="text-gray-600 text-sm mb-2">{{ bank.dcls_chrg_man }}</p>
      <p class="text-gray-500 text-sm mb-4">{{ bank.homp_url }}</p>
    </div>

    <!-- 클릭된 카드 아래에 상세 정보 표시 -->
    <div v-if="isDetailsVisible" class="bg-gray-50 p-6 rounded-md border border-gray-300">
      <h6 class="font-semibold text-lg mb-2">상세 정보</h6>
      <p class="text-gray-700">은행 코드: {{ bank.fin_co_no }}</p>
      <p class="text-gray-700">대표자: {{ bank.dcls_chrg_man }}</p>
      <p class="text-gray-700">홈페이지: <a :href="bank.homp_url" class="text-blue-500" target="_blank">{{ bank.homp_url }}</a></p>
      <p class="text-gray-700">주소: {{ bank.address || '정보 없음' }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  bank: Object,
  isDetailsVisible: Boolean
})

const emit = defineEmits(['click'])

// 카드 클릭 시 상세 정보 표시/숨기기
function toggleDetails() {
  emit('click')
}
</script>

<style scoped>
/* 필요에 따라 추가적인 스타일을 작성할 수 있습니다. */
</style>
