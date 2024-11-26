<!-- Announcement.vue -->
<template>
  <div class="announcement-container max-w-7xl mx-auto py-8 px-4 bg-gradient-to-b from-indigo-600 to-indigo-500">
    <!-- 공지사항 목록 -->
    <div class="list-section bg-white shadow-lg rounded-lg p-6">
      <div class="header flex justify-between items-center mb-6">
        <h2 class="text-2xl font-semibold text-gray-800">공지사항</h2>
        <RouterLink
          v-if="store.isAdmin"
          to="/update"
          class="text-white bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-md text-sm font-medium transition duration-300"
        >
          데이터 업데이트
        </RouterLink>
      </div>

      <!-- 공지사항 목록 테이블 -->
      <table class="announcement-table w-full table-auto border-collapse">
        <thead>
          <tr>
            <th class="py-3 px-4 text-left text-sm font-medium text-gray-700">번호</th>
            <th class="py-3 px-4 text-left text-sm font-medium text-gray-700">제목</th>
            <th class="py-3 px-4 text-left text-sm font-medium text-gray-700">작성자</th>
            <th class="py-3 px-4 text-left text-sm font-medium text-gray-700">작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="announcement in store.announcements"
            :key="announcement.id"
            class="border-b border-gray-200 hover:bg-gray-50 transition duration-300"
          >
            <td class="py-3 px-4 text-sm text-gray-800">{{ announcement.id }}</td>
            <td class="py-3 px-4 text-sm text-gray-800">{{ announcement.announcement_title }}</td>
            <td class="py-3 px-4 text-sm text-gray-600">{{ announcement.announcement_content }}</td>
            <td class="py-3 px-4 text-sm text-gray-500">{{ formatDate(announcement.updated_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';

const announcements1 = ref([])
const store = useCounterStore()

onMounted(() => {
  store.getAnnouncementData()
  announcements1.value = store.announcements
})

defineProps({
  store: Object
})

// 날짜 형식을 "YYYY-MM-DD" 형식으로 변환하는 메서드
const formatDate = (date) => {
  const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return new Date(date).toLocaleDateString('ko-KR', options);
}


</script>

<style scoped>
.announcement-container {
  background-color: #f9fafb;
}
.list-section {
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
}
.announcement-table th,
.announcement-table td {
  text-align: left;
  padding: 0.75rem;
}
</style>