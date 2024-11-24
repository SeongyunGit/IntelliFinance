<template>
  <div>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <MortgageLoanListItem
        v-if="bank.type_a === 'mortgageLoan' 
          && (store.surveyData.mortgageLoan.kor_co_nm.length === 0 || store.surveyData.mortgageLoan.kor_co_nm.includes(bank.kor_co_nm))
          && store.integrationProductOptions.some(option => 
            option.fin_prdt_cd === bank.fin_prdt_cd
            && (store.surveyData.mortgageLoan.rpay_type_nm.length === 0 || store.surveyData.mortgageLoan.rpay_type_nm.includes(option.rpay_type_nm))
            && (store.surveyData.mortgageLoan.lend_rate_type_nm.length === 0 || store.surveyData.mortgageLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm))
            && (store.surveyData.mortgageLoan.lend_rate_min > option.lend_rate_min || !store.surveyData.mortgageLoan.lend_rate_min)
            && (store.surveyData.mortgageLoan.lend_rate_max > option.lend_rate_max || !store.surveyData.mortgageLoan.lend_rate_max)
            && (store.surveyData.mortgageLoan.lend_rate_avg > option.lend_rate_avg || !store.surveyData.mortgageLoan.lend_rate_avg)
            && (store.surveyData.mortgageLoan.mrtg_type_nm.length === 0 || store.surveyData.mortgageLoan.mrtg_type_nm.includes(option.mrtg_type_nm))
          )"
        :bank="bank"
      />
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MortgageLoanListItem from '@/components/MortgageLoanListItem.vue'

const store = useCounterStore()

</script>
