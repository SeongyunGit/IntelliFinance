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



// onMounted(() => {
//   if (store.isLogin) {
//     store.getSurveyData(store.mPK, 'deposit')
//   }
// })

</script>

<style scoped>

</style>