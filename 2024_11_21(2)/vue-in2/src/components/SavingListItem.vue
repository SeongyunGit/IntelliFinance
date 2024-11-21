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
          && saving.intr_rate_type_nm.includes(option.intr_rate_type_nm)
          && saving.save_trm.includes(option.save_trm)
          && (saving.intr_rate > option.intr_rate || !saving.intr_rate)
          && (saving.intr_rate2 > option.intr_rate2 || !saving.intr_rate2)
          && saving.rsrv_type_nm.includes(option.rsrv_type_nm)">
            <li>
              <p>{{ option.intr_rate_type_nm }}</p>
              <p>기간 : {{ option.save_trm }}</p>
              <p>기본금리 : {{ option.intr_rate }}</p>
              <p>우대금리 : {{ option.intr_rate2 }}</p>
              <p>정립방식 : {{ option.rsrv_type_nm }}</p>
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
const saving = store.surveyData.saving

defineProps({
  bank: Object
})
</script>
<style  scoped>

</style>