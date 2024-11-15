<template>
  <div>
    <h1>Bank Delete</h1>
    <p>데이터 삭제 완료</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.delete_data()
})
</script>

<style scoped>

</style>