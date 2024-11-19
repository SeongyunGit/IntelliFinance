<template>
  <div>
    <h3>Bank List</h3>
    <BankListItem 
      v-for="bank in store.companyList"
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
