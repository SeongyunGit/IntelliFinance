<template>
  <hr>
  <ul>
    <div>
      <h2>
        <div>
          <h5>{{ bank.fin_prdt_nm }}</h5>
          <p>{{ bank.kor_co_nm }}</p>
          <p>{{ bank.mtrt_int }}</p>
          <p>{{ bank.type_a }}</p>
        </div>
      </h2>
      <div>
        <div v-for="option in store.integrationProductOptions" :key="option.fin_prdt_cd">
          <div v-if="option.fin_prdt_cd === bank.fin_prdt_cd
          && (rentHouseLoan.rpay_type_nm.length === 0 || rentHouseLoan.rpay_type_nm.includes(option.rpay_type_nm))
          && (rentHouseLoan.lend_rate_type_nm.length === 0 || rentHouseLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm))
          && (rentHouseLoan.lend_rate_min > option.lend_rate_min || !rentHouseLoan.lend_rate_min)
          && (rentHouseLoan.lend_rate_max > option.lend_rate_max || !rentHouseLoan.lend_rate_max)
          && (rentHouseLoan.lend_rate_avg > option.lend_rate_avg || !rentHouseLoan.lend_rate_avg)
          ">
            <li>
              <p>{{ option.rpay_type_nm }}</p>
              <p>{{ option.lend_rate_type_nm }}</p>
              <p>최소 금리 : {{ option.lend_rate_min }}</p>
              <p>최대 금리 : {{ option.lend_rate_max }}</p>
              <p>평균 금리 : {{ option.lend_rate_avg }}</p>
              <p>{{ option.mrtg_type_nm }}</p>
              <hr>
            </li>
          </div>
        </div>
      </div>
    </div>
  </ul>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const rentHouseLoan = store.surveyData.rentHouseLoan

defineProps({
  bank: Object
})
</script>
<style  scoped>

</style>