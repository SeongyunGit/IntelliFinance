<!-- Announcement.vue -->
<template>
  <div class="announcement-container">
    <!-- 공지사항 목록 -->
    <div class="list-section">
      <div class="header">
        <h2>공지사항</h2>
        <RouterLink v-if="store.isAdmin" to="/update" class="text-gray-700 hover:text-indigo-600 px-3 py-2 rounded-md text-sm font-medium">
          data update
        </RouterLink>
        <!-- <button v-if="isAdmin" @click="showForm = true" class="create-btn">
          새 공지사항
        </button> -->
      </div>
      <!-- 공지사항 목록 테이블 -->
      <table class="announcement-table">
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
            <th>작성일</th>
            <!-- <th v-if="isAdmin">관리</th> -->
          </tr>
        </thead>
        <tbody>
          
          <tr v-for="announcement in store.announcements" :key="announcement.id">
            <td>{{ announcement.id }}</td>
            <td>{{ announcement.announcement_title }}</td>
            <td>{{ announcement.announcement_content }}</td>
            <td>{{ announcement.updated_at }}</td>
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



</script>

<style scoped>
.announcement-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.create-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.announcement-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.announcement-table th,
.announcement-table td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

.announcement-table th {
  background-color: #f5f5f5;
}

.title-cell {
  cursor: pointer;
  color: #2c3e50;
}

.title-cell:hover {
  text-decoration: underline;
}

.content-expanded {
  padding: 15px;
  background-color: #f9f9f9;
  margin-top: 10px;
  border-radius: 4px;
}

.action-buttons button {
  margin-right: 5px;
  padding: 5px 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.edit-btn {
  background-color: #2196F3;
  color: white;
}

.delete-btn {
  background-color: #f44336;
  color: white;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 600px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.submit-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-btn {
  background-color: #9e9e9e;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.delete-confirm {
  text-align: center;
}

.confirm-buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.confirm-delete {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-delete {
  background-color: #9e9e9e;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}
</style>