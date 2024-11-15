<template>
  <div>
    <h3>deposit List</h3>
    <div v-for="bank in store.integrationProducts"
      :key="bank.id"
      :bank="bank">
      <DepositListItem v-if="bank.type_a === 'deposit'" :bank="bank"/>
    </div>
  </div>
</template>

<script setup>
import DepositListItem from '@/components/DepositListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
</script>
