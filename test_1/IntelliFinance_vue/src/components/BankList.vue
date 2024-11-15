<template>
  <div>
    <h3>Bank List</h3>
    <!-- <p>{{ store.Banks.result }}</p> -->
    <!-- <p v-for="bank in store.Banks.result.baseList">{{ bank }}</p> -->
    <BankListItem 
      v-for="bank in store.Banks.result.baseList"
      :key="bank.fin_co_no"
      :bank="bank"
    />
  </div>
</template>

<script setup>
import BankListItem from '@/components/BankListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
