<template>
  <div>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      
      <DepositListItem
        v-if="bank.type_a === 'deposit'
        && (store.surveyData.deposit.kor_co_nm.length === 0 || store.surveyData.deposit.kor_co_nm.includes(bank.kor_co_nm))
        && store.integrationProductOptions.some(option => 
          option.fin_prdt_cd === bank.fin_prdt_cd 
          && (store.surveyData.deposit.intr_rate_type_nm.length === 0 || store.surveyData.deposit.intr_rate_type_nm.includes(option.intr_rate_type_nm))
          && (store.surveyData.deposit.save_trm.length === 0 || store.surveyData.deposit.save_trm.includes(option.save_trm))
          && (!store.surveyData.deposit.intr_rate || store.surveyData.deposit.intr_rate > option.intr_rate)
          && (!store.surveyData.deposit.intr_rate2 || store.surveyData.deposit.intr_rate2 > option.intr_rate2)
        )"
        :bank="bank"
      />
     
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import DepositListItem from '@/components/DepositListItem.vue'
import Survey from '@/components/Survey.vue';

const store = useCounterStore()

</script>
