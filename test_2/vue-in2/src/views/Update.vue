<template>
  <div>
    <h1>Bank update</h1>
    <p>데이터 업데이트(삭제후 다시 저장)</p>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.delete_data()
  store.getdeposit()
  store.getsaving()
  store.getmortgageLoan()
  store.getrentHouseLoan()
  store.getcompany()
})
</script>

<style scoped>

</style>