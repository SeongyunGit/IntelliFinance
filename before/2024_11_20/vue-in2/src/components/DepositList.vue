<template>
  <div>
    <h3>deposit List</h3>
    <p>{{ store.surveyData }}</p>
    <DepositSurvey :surveyData="store.surveyData" />
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <DepositListItem v-if="bank.type_a === 'deposit' && store.surveyData.kor_co_nm.includes(bank.kor_co_nm)" :bank="bank"/>
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import DepositListItem from '@/components/DepositListItem.vue'
import { useCounterStore } from '@/stores/counter'
import DepositSurvey from '@/components/DepositSurvey.vue';

const store = useCounterStore()

</script>
