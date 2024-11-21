<template>
  <div>
    <h3>deposit List</h3>
    <!-- <p>{{ store.surveyData }}</p> -->
    <hr>
    <p>{{ store.surveyData.deposit }}</p>
    <DepositSurvey :surveyData="store.surveyData.deposit" />
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <!-- <p>{{ bank }}</p> -->
      <DepositListItem 
      v-if="bank.type_a === 'deposit' 
      && store.surveyData.deposit.kor_co_nm.includes(bank.kor_co_nm)" :bank="bank"/>
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DepositListItem from '@/components/DepositListItem.vue'
import DepositSurvey from '@/components/DepositSurvey.vue';

const store = useCounterStore()
// const deposit = store.surveyData.deposit

</script>
