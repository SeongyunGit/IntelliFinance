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
          && mortgageLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm)
          && mortgageLoan.lend_rate_type_nm.includes(option.lend_rate_type_nm)
          && mortgageLoan.lend_rate.includes(option.lend_rate)
          && (mortgageLoan.lend_rate_min > option.lend_rate_min || !mortgageLoan.lend_rate_min)
          && (mortgageLoan.lend_rate_max > option.lend_rate_max || !mortgageLoan.lend_rate_max)
          && (mortgageLoan.lend_rate_avg > option.lend_rate_avg || !mortgageLoan.lend_rate_avg)
          && mortgageLoan.mrtg_type_nm.includes(option.mrtg_type_nm)">
            <li>
              <p>{{ option.rpay_type_nm }}</p> <!-- 상환 방식 명 -->
              <p>{{ option.lend_rate_type_nm }}</p> <!-- 금리 유형 명 -->
              <p>금리 : {{ option.lend_rate }}</p> <!-- 금리 -->
              <p>최소 금리 : {{ option.lend_rate_min }}</p> <!-- 최소 금리 -->
              <p>최대 금리 : {{ option.lend_rate_max }}</p> <!-- 최대 금리 -->
              <p>평균 금리 : {{ option.lend_rate_avg }}</p> <!-- 평균 금리 -->
              <p>{{ option.mrtg_type_nm }}</p> <!-- 담보 유형 명 -->
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
const mortgageLoan = store.surveyData.mortgageLoan

defineProps({
  bank: Object
})
</script>
<style  scoped>

</style>