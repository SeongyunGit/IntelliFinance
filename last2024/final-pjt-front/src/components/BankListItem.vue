<template>
  <div class="bg-white rounded-lg shadow-md p-6 space-y-6 relative min-h-[300px]">
    <!-- 은행 정보 -->
    <div>
      <h2 class="text-2xl font-semibold text-gray-800 mb-2">{{ bank.kor_co_nm }}</h2>
      <p class="text-sm text-gray-500">{{ bank.dcls_chrg_man }}</p>
      <p class="text-gray-500 text-sm truncate">{{ bank.homp_url }}</p>
    </div>

    <!-- 버튼 -->
    <div class="absolute bottom-6 left-0 right-0 flex justify-center">
      <button
        @click="toggleDetails(bank)"
        class="bg-gradient-to-r from-indigo-500 to-purple-600 text-white px-6 py-2 rounded-xl shadow-md hover:from-indigo-600 hover:to-purple-700 transition duration-300"
      >
        상세 정보
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  bank: Object,
  index: Number
})

const emit = defineEmits(['click'])

function toggleDetails(bank) {
  emit('click', bank)
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