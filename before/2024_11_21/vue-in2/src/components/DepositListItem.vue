<template>
  <hr>
  <ul>
    <div>
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
          <div v-for="option in store.integrationProductOptions">
            <div v-if="option.fin_prdt_cd === bank.fin_prdt_cd
            && deposit.intr_rate_type_nm.includes(option.intr_rate_type_nm)

            && deposit.save_trm.includes(option.save_trm)
            
            && (deposit.intr_rate > option.intr_rate || !deposit.intr_rate)
            && (deposit.intr_rate2 > option.intr_rate2 || !deposit.intr_rate2)">
              <li>
                <p>{{ option.intr_rate_type_nm }}</p>
                <p>기간 : {{ option.save_trm }}</p>
                <p>기본금리 : {{ option.intr_rate }}</p>
                <p>우대금리 : {{ option.intr_rate2 }}</p>
                <hr>
              </li>
            </div>
          </div>
        </div>
      </div>
    </div>
  </ul>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const deposit = store.surveyData.deposit

defineProps({
  bank: Object
})
</script>
<style  scoped>

</style>