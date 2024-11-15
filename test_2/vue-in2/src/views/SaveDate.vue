<template>
  <div>
    <h1>Bank</h1>
    <p>새로운 데이터 저장</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getdeposit()
  store.getsaving()
  store.getmortgageLoan()
  store.getrentHouseLoan()
})
</script>

<style scoped>

</style>