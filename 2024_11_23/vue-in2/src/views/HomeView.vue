<template>
  <div>
    <Survey />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

import DepositList from '@/components/DepositList.vue';
import Survey from '@/components/Survey.vue';

const store = useCounterStore()

onMounted(() => {
  // mount 되기전에 store에 있는 전체 게시글 요청 함수를 호출
  store.getIntegration()
//   if (store.isLogin) {
//     store.getSurveyData(store.mPK, 'deposit')
//   }
})

</script>

<style scoped>

</style>