<template>
  <div>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <SavingListItem
        v-if="bank.type_a === 'saving' 
          && (store.surveyData.saving.kor_co_nm.length === 0 || store.surveyData.saving.kor_co_nm.includes(bank.kor_co_nm))
          && store.integrationProductOptions.some(option => 
            option.fin_prdt_cd === bank.fin_prdt_cd
            && (store.surveyData.saving.intr_rate_type_nm.length === 0 || store.surveyData.saving.intr_rate_type_nm.includes(option.intr_rate_type_nm))
            && (store.surveyData.saving.save_trm.length === 0 || store.surveyData.saving.save_trm.includes(option.save_trm))
            && (store.surveyData.saving.intr_rate > option.intr_rate || !store.surveyData.saving.intr_rate)
            && (store.surveyData.saving.intr_rate2 > option.intr_rate2 || !store.surveyData.saving.intr_rate2)
            && (store.surveyData.saving.rsrv_type_nm.length === 0 || store.surveyData.saving.rsrv_type_nm.includes(option.rsrv_type_nm)))"
        :bank="bank"
      />
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import SavingListItem from '@/components/SavingListItem.vue'

const store = useCounterStore()

</script>
