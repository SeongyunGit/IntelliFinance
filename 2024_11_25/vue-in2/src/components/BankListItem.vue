<template>
  <div class="mb-8">
    <!-- 카드 내용 -->
    <div class="bg-white border border-gray-200 rounded-lg shadow-lg p-6 cursor-pointer card hover:shadow-2xl transition-all duration-300 transform hover:scale-105 card"  @click="toggleDetails">
      <h5 class="text-xl font-semibold text-gray-800 mb-2">{{ bank.kor_co_nm }}</h5>
      <p class="text-gray-600 text-sm mb-2">{{ bank.dcls_chrg_man }}</p>
      <p class="text-gray-500 text-sm mb-4 truncate">{{ bank.homp_url }}</p>

      <!-- 클릭된 카드 아래에 상세 정보 표시 -->
      <div v-if="isDetailsVisible" class="details mt-4 bg-gray-50 p-6 rounded-md border border-gray-300">
        <h6 class="font-semibold text-lg text-gray-800 mb-2">상세 정보</h6>
        <p class="text-gray-700 mb-2">은행 코드: {{ bank.fin_co_no }}</p>
        <p class="text-gray-700 mb-2">대표자: {{ bank.dcls_chrg_man }}</p>
        <p class="text-gray-700 mb-2">홈페이지: <a :href="bank.homp_url" class="text-blue-500 hover:underline" target="_blank">{{ bank.homp_url }}</a></p>
        <p class="text-gray-700">주소: {{ bank.address || '정보 없음' }}</p>
      </div>
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
.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%; /* 카드 높이를 일정하게 맞추기 */
  background-color: #f7fafc; /* 배경색 설정 */
}
.details {
  transition: max-height 0.3s ease-out; /* 상세 정보가 부드럽게 확장되도록 */
  overflow: hidden; /* 상세 정보 영역 넘침 방지 */
  max-height: 0; /* 기본 상태에서 숨겨두기 */
}
.card .details {
  max-height: 500px; /* 상세 정보가 확장될 최대 높이 */
}
</style>