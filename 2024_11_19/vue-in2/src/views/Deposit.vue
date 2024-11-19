<template>
  <div>
    <h1>deposit</h1>
    <DepositList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DepositList from '@/components/DepositList.vue';

const store = useCounterStore()
const user_id = 1

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getIntegration()
  // survey 데이터를 불러옴
  store.getSurveyData(user_id, 'deposit')
})
</script>

<style scoped>

</style>