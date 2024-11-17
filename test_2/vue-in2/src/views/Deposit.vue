<template>
  <div>
    <h1>deposit</h1>
    <DepositSurvey />
    <DepositList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DepositList from '@/components/DepositList.vue';
import DepositSurvey from '@/components/DepositSurvey.vue';

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getIntegration()
})
</script>

<style scoped>

</style>