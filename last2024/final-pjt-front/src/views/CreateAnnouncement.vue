<template>
  <div class="create-announcement-container max-w-7xl mx-auto py-8 px-4">
    <div class="form-section bg-white shadow-lg rounded-lg p-6">
      <h2 class="text-2xl font-semibold text-gray-800 mb-6">공지사항 작성</h2>
      
      <form @submit.prevent="submitAnnouncement" class="space-y-6">
        <div>
          <label for="title" class="block text-sm font-medium text-gray-700">제목</label>
          <input
            type="text"
            id="title"
            v-model="announcementData.announcement_title"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            required
          >
        </div>

        <div>
          <label for="content" class="block text-sm font-medium text-gray-700">내용</label>
          <textarea
            id="content"
            v-model="announcementData.announcement_content"
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            required
          ></textarea>
        </div>

        <div class="flex items-center">
          <input
            type="checkbox"
            id="important"
            v-model="announcementData.announcement_important"
            class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
          >
          <label for="important" class="ml-2 block text-sm text-gray-700">중요 공지</label>
        </div>

        <div class="flex justify-end space-x-4">
          <button
            type="button"
            @click="$router.push('/announcement')"
            class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-md"
          >
            취소
          </button>
          <button
            type="submit"
            class="px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 rounded-md"
          >
            작성
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const router = useRouter()

const announcementData = ref({
  announcement_title: '',
  announcement_content: '',
  announcement_important: false
})

const submitAnnouncement = async () => {
  try {
    await store.createAnnouncement(announcementData.value)
    router.push('/announcement')
  } catch (error) {
    console.error('공지사항 작성 실패:', error)
  }
}
</script>