<template>
  <div>
    <h1>Home</h1>
    <!-- <p>{{ store.surveyData }}</p> -->
    <DepositList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

import DepositList from '@/components/DepositList.vue';

const store = useCounterStore()



onMounted(() => {
  if (store.isLogin) {
    store.getSurveyData(store.mPK, 'deposit')
  }
})


</script>

<style scoped>

</style>