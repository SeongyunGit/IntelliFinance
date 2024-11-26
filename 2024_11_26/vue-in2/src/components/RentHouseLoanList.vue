<template>
  <div>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <RentHouseLoanListItem
        v-if="bank.type_a === 'rentHouseLoan' 
          && (store.surveyData.rentHouseLoan.kor_co_nm.length === 0 || store.surveyData.rentHouseLoan.kor_co_nm.includes(bank.kor_co_nm))
          && store.integrationProductOptions.some(option => 
            option.fin_prdt_cd === bank.fin_prdt_cd
            && (store.surveyData.rentHouseLoan.rpay_type_nm.length === 0 || store.surveyData.rentHouseLoan.rpay_type_nm.includes(option.rpay_type_nm))
            && (store.surveyData.rentHouseLoan.lend_rate_type_nm.length === 0 || store.surveyData.rentHouseLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm))
            && (store.surveyData.rentHouseLoan.lend_rate_min > option.lend_rate_min || !store.surveyData.rentHouseLoan.lend_rate_min)
            && (store.surveyData.rentHouseLoan.lend_rate_max > option.lend_rate_max || !store.surveyData.rentHouseLoan.lend_rate_max)
            && (store.surveyData.rentHouseLoan.lend_rate_avg > option.lend_rate_avg || !store.surveyData.rentHouseLoan.lend_rate_avg)
          )"
        :bank="bank"
      />
    </div>
  </div>
</template>

<script setup>
// import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import RentHouseLoanListItem from '@/components/RentHouseLoanListItem.vue'

const store = useCounterStore()

</script>
